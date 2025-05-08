#include <iostream>
#include <vector>
#include <thread>
#include <atomic>
#include <rtaudio/RtAudio.h>
#include <termios.h>
#include <unistd.h>
#include <fcntl.h>
#include <cmath>
#include <rubberband/RubberBandStretcher.h>
#include <SFML/Graphics.hpp>
#include <SFML/Window.hpp>
#include <SFML/System.hpp>
#include <iostream>


using namespace RubberBand;

constexpr float sampleRate = 44100.0f;
float feedbackGain = 0.3f;  // Controls reverb feedback

constexpr int HARMONIZER_BLOCK_SIZE = 128;
std::vector<float> harmonizerInputBuffer(HARMONIZER_BLOCK_SIZE, 0.0f);
std::vector<float> harmonizerOutputBuffer(HARMONIZER_BLOCK_SIZE, 0.0f);
int harmonizerInputIndex = 0;
int harmonizerOutputIndex = HARMONIZER_BLOCK_SIZE; // Force refill on first run


enum ReverbMode { OFF, PLATE };
std::atomic<ReverbMode> currentMode(OFF);
std::atomic<bool> harmonizerOn(false);

constexpr unsigned int DELAY_SAMPLES = 88200; // ~2 seconds at 44.1kHz
std::vector<float> delayBuffer(DELAY_SAMPLES, 0.0f);
unsigned int delayIndex = 0;

std::unique_ptr<RubberBandStretcher> octaveUp, octaveDown, fifthUp, thirdUp;

void setupHarmonizers(float sampleRate) {
    RubberBandStretcher::Options options = RubberBandStretcher::OptionProcessRealTime |
                                           RubberBandStretcher::OptionPitchHighQuality;
    int channels = 1;
    octaveUp.reset(new RubberBandStretcher(sampleRate, channels, options));
    octaveDown.reset(new RubberBandStretcher(sampleRate, channels, options));
    fifthUp.reset(new RubberBandStretcher(sampleRate, channels, options));
    thirdUp.reset(new RubberBandStretcher(sampleRate, channels, options));

    octaveUp->setPitchScale(2.0);      // +12 semitones
    octaveDown->setPitchScale(0.5);    // -12 semitones
    fifthUp->setPitchScale(std::pow(2.0, 7.0 / 12.0));
    thirdUp->setPitchScale(std::pow(2.0, 4.0 / 12.0));
}

// Adds harmonics: octave up, octave down, 5th up, 3rd up
float applyHarmonizer(float inSample) {
    // Buffer input sample
    harmonizerInputBuffer[harmonizerInputIndex++] = inSample;

    // If output buffer is empty, fill it
    if (harmonizerOutputIndex >= HARMONIZER_BLOCK_SIZE) {
        float* inBuf[1] = { harmonizerInputBuffer.data() };

        // Process block
        octaveUp->process(inBuf, HARMONIZER_BLOCK_SIZE, false);
        fifthUp->process(inBuf, HARMONIZER_BLOCK_SIZE, false);
        thirdUp->process(inBuf, HARMONIZER_BLOCK_SIZE, false);
        octaveDown->process(inBuf, HARMONIZER_BLOCK_SIZE, false);


        float* outBuf[1] = { harmonizerOutputBuffer.data() };

        std::fill(harmonizerOutputBuffer.begin(), harmonizerOutputBuffer.end(), 0.0f);  // Clear output buffer

        if (octaveUp->available() >= HARMONIZER_BLOCK_SIZE &&
            fifthUp->available() >= HARMONIZER_BLOCK_SIZE &&
            thirdUp->available() >= HARMONIZER_BLOCK_SIZE &&
            octaveDown->available() >= HARMONIZER_BLOCK_SIZE) {

            std::vector<float> tempBuf(HARMONIZER_BLOCK_SIZE);

            // Mix harmonizers
            octaveUp->retrieve(&outBuf[0], HARMONIZER_BLOCK_SIZE);
            std::copy(harmonizerOutputBuffer.begin(), harmonizerOutputBuffer.end(), tempBuf.begin());

            octaveDown->retrieve(&outBuf[0], HARMONIZER_BLOCK_SIZE);
            for (int i = 0; i < HARMONIZER_BLOCK_SIZE; i++) {
                tempBuf[i] += harmonizerOutputBuffer[i];
            }

            fifthUp->retrieve(&outBuf[0], HARMONIZER_BLOCK_SIZE);
            for (int i = 0; i < HARMONIZER_BLOCK_SIZE; i++) {
                tempBuf[i] += harmonizerOutputBuffer[i];
            }

            thirdUp->retrieve(&outBuf[0], HARMONIZER_BLOCK_SIZE);
            for (int i = 0; i < HARMONIZER_BLOCK_SIZE; i++) {
                harmonizerOutputBuffer[i] = 0.2f * (tempBuf[i] + harmonizerOutputBuffer[i]);
            }
        }

        harmonizerOutputIndex = 0;
        harmonizerInputIndex = 0;
    }

    // Return one sample
    return harmonizerOutputBuffer[harmonizerOutputIndex++];
}


int audioCallback(void* outputBuffer, void* inputBuffer,
                  unsigned int nBufferFrames,
                  double /*streamTime*/, RtAudioStreamStatus /*status*/, void* /*userData*/) {
    float* in = static_cast<float*>(inputBuffer);
    float* out = static_cast<float*>(outputBuffer);

    for (unsigned int i = 0; i < nBufferFrames; i++) {
        float dry = in[i];

        float harmonized = harmonizerOn ? applyHarmonizer(dry) : 0.0f;
        float inputSignal = dry + (harmonizerOn ? harmonized : 0.0f);

        float wetL = 0.0f;
        float wetR = 0.0f;

        if (currentMode == PLATE) {
            const int preDelay = 882; // ~20ms
            int tapsL[] = { preDelay + 1800, 4500, 9100, 14500, 20500 };
            int tapsR[] = { preDelay + 1900, 4400, 8900, 14800, 20200 };
            float weights[] = { 0.5f, 0.4f, 0.3f, 0.2f, 0.15f };

            for (int j = 0; j < 5; ++j) {
                wetL += weights[j] * delayBuffer[(delayIndex + DELAY_SAMPLES - tapsL[j]) % DELAY_SAMPLES];
                wetR += weights[j] * delayBuffer[(delayIndex + DELAY_SAMPLES - tapsR[j]) % DELAY_SAMPLES];
            }

            wetL += 0.2f * delayBuffer[(delayIndex + DELAY_SAMPLES - 11000) % DELAY_SAMPLES];
            wetR += 0.2f * delayBuffer[(delayIndex + DELAY_SAMPLES - 11200) % DELAY_SAMPLES];
        }

        float outL = 0.3f * dry + 0.3f * harmonized + wetL;
        float outR = 0.3f * dry + 0.3f * harmonized + wetR;

        outL = std::clamp(outL, -1.0f, 1.0f);
        outR = std::clamp(outR, -1.0f, 1.0f);

        out[2 * i]     = outL;
        out[2 * i + 1] = outR;

        float feedbackSample = 0.5f * inputSignal + feedbackGain * 0.5f * (wetL + wetR);
        delayBuffer[delayIndex] = feedbackSample;
        delayIndex = (delayIndex + 1) % DELAY_SAMPLES;
    }

    return 0;
}

void setNonBlockingInput(bool enable) {
    static struct termios oldt;
    struct termios newt;

    if (enable) {
        tcgetattr(STDIN_FILENO, &oldt);
        newt = oldt;
        newt.c_lflag &= ~(ICANON | ECHO);
        tcsetattr(STDIN_FILENO, TCSANOW, &newt);
        fcntl(STDIN_FILENO, F_SETFL, O_NONBLOCK);
    } else {
        tcsetattr(STDIN_FILENO, TCSANOW, &oldt);
    }
}

int main() {
    // Create the window with corrected VideoMode constructor
    sf::RenderWindow window(sf::VideoMode(sf::Vector2u(800, 500)), "DSP Status", sf::Style::Titlebar | sf::Style::Close);

    // Load the font correctly using openFromFile
    sf::Font font;
    if (!font.openFromFile("/Users/anniespade/Documents/Roboto/Roboto-Italic-VariableFont_wdth,wght.ttf")) {
        std::cout << "Error loading font!" << std::endl;
        return -1; // Exit if font is not loaded
    }

    // Create text objects with the correct constructor
    sf::Text harmonizerText(font, "Harmonizer Status: OFF", 50);
    harmonizerText.setPosition(sf::Vector2f(20, 50));  // Corrected position with sf::Vector2f

    sf::Text reverbText(font, "Reverb Status: OFF", 50);
    reverbText.setPosition(sf::Vector2f(20, 100));  // Corrected position with sf::Vector2f

    // Setup audio stream and harmonizers
    RtAudio audio;
    if (audio.getDeviceCount() < 1) {
        std::cerr << "No audio devices found!" << std::endl;
        return 1;
    }

    setupHarmonizers(sampleRate);  // Initialize harmonizers

    RtAudio::StreamParameters iParams, oParams;
    iParams.deviceId = audio.getDefaultInputDevice();
    iParams.nChannels = 1; // mono input
    oParams.deviceId = audio.getDefaultOutputDevice();
    oParams.nChannels = 2; // stereo output

    unsigned int bufferFrames = 256;

    try {
        audio.openStream(&oParams, &iParams, RTAUDIO_FLOAT32, sampleRate, &bufferFrames, &audioCallback);
        audio.startStream();

        std::cout << "Hi There! Press: 's' to turn on plate reverb, 'q' to turn off reverb, 'h' to toggle harmonizer, Enter to quit <3\n";
        setNonBlockingInput(true);

        // Main loop (audio processing & GUI updates)
        while (window.isOpen()) {
            // Poll events for SFML window
            std::optional<sf::Event> event;
            while ((event = window.pollEvent())) {
            }

            // Terminal input handling (non-blocking)
            char c;
            if (read(STDIN_FILENO, &c, 1) > 0) {
                if (c == 's') {
                    currentMode = PLATE;
                    std::cout << "[Plate Reverb ON]" << std::endl;
                    reverbText.setString("Reverb Status: ON");
                } else if (c == 'q') {
                    currentMode = OFF;
                    std::cout << "[Reverb OFF]" << std::endl;
                    reverbText.setString("Reverb Status: OFF");
                } else if (c == 'h') {
                    harmonizerOn = !harmonizerOn;
                    std::cout << "[Harmonizer " << (harmonizerOn ? "ON" : "OFF") << "]" << std::endl;
                    harmonizerText.setString("Harmonizer Status: " + std::string(harmonizerOn ? "ON" : "OFF"));
                } else if (c == '\n') {
                    break;
                }
            }

            // Clear the window with pink color (magenta)
            window.clear(sf::Color(255, 105, 180)); // RGB value for pink

            // Draw the texts and display the window
            window.draw(harmonizerText);
            window.draw(reverbText);
            window.display();

            std::this_thread::sleep_for(std::chrono::milliseconds(50));  // Small delay for input polling
        }

        // Clean up and stop audio stream
        setNonBlockingInput(false);
        audio.stopStream();
    } catch (...) {
        std::cerr << "RtAudio error occurred." << std::endl;
        return 1;
    }

    return 0;
}
