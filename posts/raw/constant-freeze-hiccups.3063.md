Enhex | 2017-04-28 17:01:05 UTC | #1

Some of my FPS game users get "freeze hiccups" - game freezes for a short moment once in a short while.
For some users the freezes can last few seconds.
Some users reported it can be caused just by rotating the camera.

I can't reproduce the problem on my machine, thus can't debug it.

Anyone knows what could possible cause such problem?

-------------------------

1vanK | 2017-04-28 17:20:24 UTC | #2

Many times I noticed this when a new object showed on the screen, never shown before (I think resources is sending to GPU in this moment)

-------------------------

Enhex | 2017-04-28 17:37:50 UTC | #3

It happens constantly, not just on first appearance of things.

You're right that first loading an object's resources can cause a freeze, but that's not the case.

-------------------------

Eugene | 2017-04-28 17:40:45 UTC | #4

Maybe it is environment issue?
Does lag appear if Urho is single-threaded?

-------------------------

Enhex | 2017-04-28 19:07:53 UTC | #5

I got a tester to run the game with -nothreads and it seems to solve the problem.
So there's a problem with Urho's threading?

I got a tester to run a performance profiler and here are some functions that came up:
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/bc32aa4fdb41735c12b4c99b8e6f24338d6058d5.png'>

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/d5a85b7cde9a6a2ceab5d17b016d82e6847fa1a6.png'>

I don't know if these functions are relevant since it depends on how much time the tester's app spent being frozen while he profiled.

-------------------------

Eugene | 2017-04-28 21:54:19 UTC | #6

[quote="Enhex, post:5, topic:3063"]
So there's a problem with Urho's threading?
[/quote]

I don't think that Urho itself has some code or design problem with threading.
I'd blame tester's environment: OS, CPU, background tasks that consume CPU.
I don't trust occlusion very much, also. Try to disable it instead of threads.

-------------------------

Enhex | 2017-04-28 22:29:06 UTC | #7

Blaming the user's hardware while any other game runs fine on it is quite biased.

I tried setting the occlusion triangle count to 0, but it didn't solve it.
Occlusion culling is very important for performance in my game.

-------------------------

Victor | 2017-04-29 00:50:08 UTC | #8

This may not be related to the issue, but out of curiosity, what compiler are you using to distribute your builds? Also, in the CMake settings, I've noticed that I've had to set the option below to generic for it to run on other PCs. I compile using MingGW for my builds.

// Specify the minimum CPU type on which the target binaries are
// to be deployed (Linux, MinGW, and non-Xcode OSX native build
// only), see GCC/Clang's -march option for possible values; Use
// 'generic' for targeting a wide range of generic processors
URHO3D_DEPLOYMENT_TARGET:STRING=generic

-------------------------

Enhex | 2017-04-29 07:24:24 UTC | #9

I don't see URHO3D_DEPLOYMENT_TARGET option available, [documentation](https://urho3d.github.io/documentation/HEAD/_building.html) says it isn't for Windows.

-------------------------

Victor | 2017-04-29 09:06:33 UTC | #10

Ah, you're right. I compile on Windows, but I use CLion + MingW, so it was available to me.

-------------------------

Enhex | 2017-04-29 19:45:51 UTC | #11

Made some progress. It isn't related to threading, had two testers had different issues.

The big freezes are related to this:
[quote]
[Sat Apr 29 22:19:08 2017] DEBUG: Removed unused occlusion buffer
[Sat Apr 29 22:19:08 2017] DEBUG: Removed unused screen buffer size 1680x1050 format 34842
[Sat Apr 29 22:19:08 2017] DEBUG: Removed unused screen buffer size 1680x1050 format 34842
[Sat Apr 29 22:19:08 2017] DEBUG: Removed unused screen buffer size 1680x1050 format 6408
[Sat Apr 29 22:19:08 2017] DEBUG: Removed unused screen buffer size 1680x1050 format 6408
[Sat Apr 29 22:19:08 2017] DEBUG: Removed unused screen buffer size 1680x1050 format 33190
[Sat Apr 29 22:19:08 2017] DEBUG: Removed unused screen buffer size 840x525 format 34842
[Sat Apr 29 22:19:08 2017] DEBUG: Removed unused screen buffer size 840x525 format 34842
[Sat Apr 29 22:19:08 2017] DEBUG: Removed unused screen buffer size 420x263 format 34842
[Sat Apr 29 22:19:08 2017] DEBUG: Removed unused screen buffer size 420x263 format 34842
[Sat Apr 29 22:19:08 2017] DEBUG: Removed unused screen buffer size 210x131 format 34842
[Sat Apr 29 22:19:08 2017] DEBUG: Removed unused screen buffer size 210x131 format 34842
[Sat Apr 29 22:19:08 2017] DEBUG: Removed unused screen buffer size 105x66 format 34842
[Sat Apr 29 22:19:08 2017] DEBUG: Removed unused screen buffer size 105x66 format 34842
[Sat Apr 29 22:19:08 2017] DEBUG: Set occlusion buffer size 256x160 with 5 mip levels and 1 thread buffers
[Sat Apr 29 22:19:08 2017] DEBUG: Allocated new screen buffer size 1680x1050 format 34842
[Sat Apr 29 22:19:08 2017] DEBUG: Allocated new screen buffer size 1680x1050 format 34842
[Sat Apr 29 22:19:08 2017] DEBUG: Allocated new screen buffer size 1680x1050 format 6408
[Sat Apr 29 22:19:08 2017] DEBUG: Allocated new screen buffer size 1680x1050 format 6408
[Sat Apr 29 22:19:08 2017] DEBUG: Allocated new screen buffer size 1680x1050 format 33190
[Sat Apr 29 22:19:08 2017] DEBUG: Allocated new screen buffer size 840x525 format 34842
[Sat Apr 29 22:19:08 2017] DEBUG: Allocated new screen buffer size 420x263 format 34842
[Sat Apr 29 22:19:08 2017] DEBUG: Allocated new screen buffer size 210x131 format 34842
[Sat Apr 29 22:19:08 2017] DEBUG: Allocated new screen buffer size 105x66 format 34842
[Sat Apr 29 22:19:08 2017] DEBUG: Allocated new screen buffer size 840x525 format 34842
[Sat Apr 29 22:19:08 2017] DEBUG: Allocated new screen buffer size 420x263 format 34842
[Sat Apr 29 22:19:08 2017] DEBUG: Allocated new screen buffer size 210x131 format 34842
[Sat Apr 29 22:19:08 2017] DEBUG: Allocated new screen buffer size 105x66 format 34842
[Sat Apr 29 22:19:09 2017] DEBUG: Removed unused occlusion buffer
[Sat Apr 29 22:19:09 2017] DEBUG: Removed unused screen buffer size 1680x1050 format 34842
[Sat Apr 29 22:19:09 2017] DEBUG: Removed unused screen buffer size 1680x1050 format 34842
[Sat Apr 29 22:19:09 2017] DEBUG: Removed unused screen buffer size 1680x1050 format 6408
[Sat Apr 29 22:19:09 2017] DEBUG: Removed unused screen buffer size 1680x1050 format 6408
[Sat Apr 29 22:19:09 2017] DEBUG: Removed unused screen buffer size 1680x1050 format 33190
[Sat Apr 29 22:19:09 2017] DEBUG: Removed unused screen buffer size 840x525 format 34842
[Sat Apr 29 22:19:09 2017] DEBUG: Removed unused screen buffer size 840x525 format 34842
[Sat Apr 29 22:19:09 2017] DEBUG: Removed unused screen buffer size 420x263 format 34842
[Sat Apr 29 22:19:09 2017] DEBUG: Removed unused screen buffer size 420x263 format 34842
[Sat Apr 29 22:19:09 2017] DEBUG: Removed unused screen buffer size 210x131 format 34842
[Sat Apr 29 22:19:09 2017] DEBUG: Removed unused screen buffer size 210x131 format 34842
[Sat Apr 29 22:19:09 2017] DEBUG: Removed unused screen buffer size 105x66 format 34842
[Sat Apr 29 22:19:09 2017] DEBUG: Removed unused screen buffer size 105x66 format 34842
[Sat Apr 29 22:19:09 2017] DEBUG: Set occlusion buffer size 256x160 with 5 mip levels and 1 thread buffers
[Sat Apr 29 22:19:09 2017] DEBUG: Allocated new screen buffer size 1680x1050 format 34842
[Sat Apr 29 22:19:09 2017] DEBUG: Allocated new screen buffer size 1680x1050 format 34842
[Sat Apr 29 22:19:09 2017] DEBUG: Allocated new screen buffer size 1680x1050 format 6408
[Sat Apr 29 22:19:09 2017] DEBUG: Allocated new screen buffer size 1680x1050 format 6408
[Sat Apr 29 22:19:09 2017] DEBUG: Allocated new screen buffer size 1680x1050 format 33190
[Sat Apr 29 22:19:09 2017] DEBUG: Allocated new screen buffer size 840x525 format 34842
[Sat Apr 29 22:19:09 2017] DEBUG: Allocated new screen buffer size 420x263 format 34842
[Sat Apr 29 22:19:09 2017] DEBUG: Allocated new screen buffer size 210x131 format 34842
[Sat Apr 29 22:19:09 2017] DEBUG: Allocated new screen buffer size 105x66 format 34842
[Sat Apr 29 22:19:09 2017] DEBUG: Allocated new screen buffer size 840x525 format 34842
[Sat Apr 29 22:19:09 2017] DEBUG: Allocated new screen buffer size 420x263 format 34842
[Sat Apr 29 22:19:09 2017] DEBUG: Allocated new screen buffer size 210x131 format 34842
[Sat Apr 29 22:19:09 2017] DEBUG: Allocated new screen buffer size 105x66 format 34842
[/quote]

I haven't looked into it yet, but I asked one of the testers and he said it didn't happen before. Could it be regression bug with the recent monitor number/refresh rate features?

-------------------------

Enhex | 2017-04-30 19:22:42 UTC | #12

Running sample 04 with -deferred also allocates and removes the same screen buffers several times:
https://pastebin.com/URHmY90Q

I think there's also a bug that the new graphics::monitor_ never initialized or assigned by Urho. You can see its value in the log is -842150451.

-------------------------

Lumak | 2017-05-05 20:10:02 UTC | #13

This is disconcerting. I'd like this verified as a bug or not before 1.7 release.

-------------------------

Enhex | 2017-05-05 22:08:24 UTC | #14

The screen allocation seems to be an effect, not a cause. Screen buffers have a time limit before they're removed.

I got a user with severe freezes (up to few seconds, previous one had few 100's of ms) to send me a Very Sleepy report:
https://www.dropbox.com/s/lji2dexxt2chpvx/hell.sleepy?dl=0

-------------------------

Enhex | 2017-05-06 09:15:11 UTC | #15

Got a WPA record from a user that has long pauses (this one is a second long).
services.exe? Thread starting?
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/10f31815d7ef6badcde589c4d0772746828b6701.png'>

-------------------------

Enhex | 2017-05-06 19:41:15 UTC | #16

In the end it turns out users were running out of GPU RAM.

-------------------------

sabotage3d | 2017-05-07 17:02:08 UTC | #17

Is there a way to see the GPU ram usage in Urho3D?

-------------------------

Enhex | 2017-05-07 18:01:58 UTC | #18

If you view Urho3D's built-in profiler you have Resource type usage.
It doesn't explicitly say how much GPU ram is being used, AFAIK memory usage in it is a mix of both GPU and CPU, but you'll get a general idea.
Perhaps external tools can be used to check GPU ram usage.

-------------------------

S.L.C | 2017-05-08 11:09:31 UTC | #19

Process Explorer is a general purpose tool that I use that also comes with some per-process or global GPU monitoring features. <img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/351815fc7d4c341a75a156475ee5c15d60b0c1fb.png" width="645" height="500">

-------------------------

