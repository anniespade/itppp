##Documention

[LINK TO MY PROJECT](https://editor.p5js.org/anniespade/full/SWDWKQNDD)

I used Chat GPT to help code this and the whole conversation can be found [here] (https://chatgpt.com/share/67e58539-0e88-8013-98e7-d242a9a8c83b)


First of all I went into Chat GPT and pasted the codealong and the decription of the assignment:

It sent out this:


let soundL, soundM, soundN;


function preload() {
	
  soundFormats('wav', 'mp3');  // Add any other formats if needed
  
  soundL = loadSound('soundL.wav');  // Replace with your actual file names
  
  soundM = loadSound('soundM.wav');
  
  soundN = loadSound('soundN.wav');
  
}


function setup() {
	
  createCanvas(500, 300);
  
  background(0);
  
  fill(255);
  
  textSize(20);
  
  textAlign(CENTER, CENTER);
  
  text("Press 'L', 'M', or 'N' to play different sounds", width / 2, height / 2);
  
}


function keyPressed() {
	
  console.log("Key pressed:", key);
  

  if (key.toLowerCase() === 'l') {
	  
    playSound(soundL, 'L');
	
  } else if (key.toLowerCase() === 'm') {
	  
    playSound(soundM, 'M');
	
  } else if (key.toLowerCase() === 'n') {
	  
    playSound(soundN, 'N');
	
  }
  
}


function playSound(soundFile, keyLabel) {
	
  if (soundFile.isLoaded()) {
	  
    soundFile.play();
	
    console.log(`Sound ${keyLabel} played.`);
	
  } else {
	  
    console.log(`Sound ${keyLabel} not loaded yet.`);
	
  }
  
}

I then look this code and went in to change the keys from 'L M and N' and changed them to V B and N. I also found a pack of piano samples on Splice, in the various triad chords in Cmaj and took samples of the chords Cmaj, Fmaj, and Gmaj. I loaded the samples into p5js and changed the sample code to play the piano files with v= Cmaj b=F maj and n= Gmaj.I did this by changing the file names from 'soundL.wav'in the code, to the name of the piano file.


It didn't work so I pasted everything into chatGPT and asked why. It was becayse I had left the function setup canvas (that the program automatically has when you start) and thus there was two canvas setups which is why it didn't wokr. I deleted the first one and everything worked great!


After this! The midterm was done!


but I got a little excited and so ask chat GPT if p5js could transpose audio samples. After getting a yes, I pasted my updated code and asked it this:


Change this code so that I can have four files play on keys v b n and m (with M being Dmin). Also add code that makes it so when I press 'u', it transposes everthing down a half step and if I press 'i' it transposes everything down a half step. and if I press 'o' it resets to it's orginal pitch


However it didn't work, I opened ChatGPT again and asked why, it gave me four different troubleshooting options and after confirming the case-sensitivity, that my audio files where uplaoded, that events were allowed from site, and that the file names were correct, it worked!



I then added a kick, a snare, and a clap sound on keys 'd' 's' and 'a'


And now my keyboard is a little two piece band!


