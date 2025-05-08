##Doocumentation

Goal: Make a live vocal processor that can toggle reverb and harmonies.

I started in Python. I tried to download Pyo and spent about 3 hours trying to downloaded it. My conversaton with ChatGpt is [here](https://chatgpt.com/share/681ce481-8d1c-8013-92ab-eb119b46de6e)

In the converstation I spend a long time trying to troubleshoot why I can't downloaed Pyo. I give up on Chatgpt and find a post on reddit that says I need to download an old version of python3. I unstall my current version, install the older version and it works! I run a live playback with pyo and it works but there's latency. I look online and find that there is almost no resources online for Pyo and decided to switch to Pyaudio, as there is many more posts and resourses.

In the converstation with Chatgpt, you can see that I get a playback and a reverb working!

I try many different version of the reverb before finding the best one:

[Convo 1](https://chatgpt.com/share/681ce581-3e1c-8013-9b24-5eb3ec65f277)

[Convo 2](https://chatgpt.com/share/681ce5ae-6840-8013-94ac-51afd39c0e92)

Trying different harmonies:

[Convo 1](https://chatgpt.com/share/681ce5ce-06c4-8013-8bd8-94fc33d42dce)

[Convo 2](https://chatgpt.com/share/681ce5ec-c0bc-8013-b0e9-0d03c86c523e)

As you can see in these very long converstations, I tried many different reverbs and harmonies, as well as trying different ones together to try and get the lowest latency.

Still, I couldn't really get the live harmony and reverb TOGETHER without the harmony sounding insane glitchy.

Then you (Professor Rome) said I should hack Sounddevice-- sadly looking up how to Hack in Python is very hard to do due to very very valid search filters. I couldn't find many resources on how to get into the code to allow it to use more CPU.

I did recall that compiler languages are faster, so I looked up if C++ would be faster than Python- got a strong yes. I hoped into VScode (and after asking Chatgpt how to open and save files properly) I was able to make a much faster version of my live local processor with reverb and harmonies!

[Convo with Chatgpt that helped me download C++](https://chatgpt.com/share/681ce701-8984-8013-b832-3b278341a5df)

[Convo where I wrote and troubleshooted the C++ code](https://chatgpt.com/share/681ce736-5c74-8013-8164-27a2a9a261c1)

[Convo to get the SMFL to work](https://chatgpt.com/share/681ce786-eb48-8013-bbb3-f7fcbfc20e66)