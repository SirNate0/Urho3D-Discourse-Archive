atai | 2017-01-02 01:09:07 UTC | #1

Hi, just curious, do the Urho3d developers allow making the audio functionality optional?  for example I am thinking of using Urho3d for simple visualization and I do not necessarily have audio functions on the hardware (and that is not needed) for visualization.

-------------------------

ghidra | 2017-01-02 01:09:07 UTC | #2

I have considered this question myself... only because i compile on my work computer to test a few things out purely visual where my work machine does not have the alsa dev libraries installed.. which breaks the compile. I'm chiming in incase this is something that is possible to do, I'd be interested as well.

-------------------------

weitjong | 2017-01-02 01:09:08 UTC | #3

I think the question is, can SDL sub-library be built without audio subsystem?

-------------------------

atai | 2017-01-02 01:09:08 UTC | #4

On a standard SDL 2.0.3 distribution and on GNU/Linux (Fedora 22), the following configure seems to disable audio:

../SDL2-2.0.3/configure --disable-audio

...
SDL2 Configure Summary:
Building Shared Libraries
Building Static Libraries
Enabled modules : atomic video render events joystick haptic power filesystem threads timers file loadso cpuinfo assembly
Assembly Math   : mmx 3dnow sse sse2
Audio drivers   :
Video drivers   : dummy x11(dynamic) opengl opengl_es2
...

-------------------------

weitjong | 2017-01-02 01:09:09 UTC | #5

That's good to know, so it is technically feasible then.

-------------------------

