## Final Project Proposals

Title: Live Looper

Summary: An application that can record audio, loop it, and then record and loop additional layers on top of that recording.

Resources:
[Source 1](https://www.instructables.com/Py-Looper/)
[Source 2](https://github.com/qpwo/pylooper)
[Source 3](https://deepgram.com/learn/best-python-audio-manipulation-tools)


- Can hit a button, start recording a loop, hit another button to end the loop. Then the recording will immediatly start playing and looping itself. Then you can hit another button and it will record another layer onto the loop. The trick here, I think, is that I'll need make sure that when I want to add another layer to recording, I need to make sure that no matter when I hit the button, it will start recording again in the start of the next loop and finish when the first loop ends. And hitting another button will reset the loop. I already have Pyaudio installed on my computer, so I'm hoping to use that forthis project, or p5.js.

N/A for the work overlapping.

Good outcome: Application is able to get a short recording from the mic input and then loop it.

Better outcome: Application is able to get a short recording from the mic input, loop it, and add more layers of looped recordings from the mic input.

Best Outcome: Application is able to CLEANLY get a short recording from the mic input, loop it, and then CLEANLY add more layers of looped recordings from the mic input.

Week one goal: Have the basic functions down and keys working. Able to add at least two loops ontop of eachother.

Week two goal: Get the visuals of this application looking nice.

Week 3 goal: Troubleshooting and refining features.


##For Live Vocal Processor:

Summary: An application that can playback audio live and place effects such as a reverb and vocoder live.

Additional sources for live vocal processor:
[Source 1](https://github.com/danilobellini/audiolazy)
[Source 2](https://pypi.org/project/pysndfx/)

- For this project, I will code it in Pyaudio with some help from various other libraries. I have the live reverb working using Pyaudio. Currently, when run the program will playback what is coming from the mic, into my headphones. Then I hit 'x' and it adds reverb to my live playback. My biggest anticipated struggle is the method for getting the harmony live to work. I have tried having the vocal converted into midi and using a library that can create major 3rd harmonies using music theory. However,this put a lot of strain on my CPU and wasn't able to consistently work. So I am now trying a live harmony that simply pitches the voice up a 5th and down an octave. However, I think that getting the right tone for this will be my biggest struggle.


Good outcome: Getting the reverb live.

Better outcome: Getting the reverb and harmonies to work.

Best Outcome: Getting the Harmonies to sound good

Week one goal: Reverb done

Week two goal: Harmonies done

Week 3 goal: Troubleshooting and refining features.
