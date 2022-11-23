Aliceravier | 2021-03-01 21:47:13 UTC | #1

Hi :slight_smile: 

I would like to send a boolean value from a sound processing application to a running Urho3D application on the raspberry pi4, under Raspbian; and be able to send an integer from the Urho application to the sound processing application. All this should be in realtime.

The sound processing is being done externally to Urho but it consists of an FFT IRR filter and some more processing to extract a frequency/note from an audio snippet. And also sending a frequency/note out onto a sound card.

Does anyone has any idea how this can be done, on the Urho side?

Alice

-------------------------

Modanung | 2021-03-01 21:07:45 UTC | #2

First thing that comes to mind is integrating Open Sound Control (OSC) into your program, since the sound processing application might support this. Although I do not have any personal experience with it, and may be somewhat overreaching.

Also, welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

S.L.C | 2021-03-01 21:10:06 UTC | #3

Maybe look for an [IPC](https://en.wikipedia.org/wiki/Inter-process_communication) library? I doubt you'll be unable to find one.

You failed to specify OS, language etc. So there's limited answers that anyone can give without context.

-------------------------

Aliceravier | 2021-03-01 21:47:40 UTC | #4

Thanks, I edited my question to address those issues

-------------------------

weitjong | 2021-03-02 16:05:48 UTC | #5

Have you checked out “jack-audio”? It should be a good fit for your use case. Plus, the SDL supports it as one of the audio driver, so it means Urho3D supports it too. It should be just a simple matter of having the development package for Jack-audio installed before rebuilding the engine from source. Good luck.

-------------------------

