Numerator | 2018-06-14 22:56:03 UTC | #1

I tried to build the examples in 64 bit, but they do not render anything except the UI overlay.

I used cmake to create a Visual Studio 2017 Win64 project.

The 32 bit version works.

-------------------------

Eugene | 2018-06-14 23:04:54 UTC | #2

You should either update Visual Studio 2017 to the latest version or don't use unstable Visual Studio 2017 at all.

-------------------------

Numerator | 2018-06-14 23:05:47 UTC | #3

I am using the latest version of Visual Studio

-------------------------

TheComet | 2018-06-15 00:04:02 UTC | #4

What cmake command did you use?

-------------------------

Eugene | 2018-06-15 00:04:54 UTC | #5

Is it broken in Debug and/or Release build?
There was known problem fixed in 15.7

-------------------------

Numerator | 2018-06-15 01:16:39 UTC | #6

I used the Cmake GUI.  Target: Visual Studio 2017 Win64
Debug build

-------------------------

S.L.C | 2018-06-15 05:50:39 UTC | #7

Which backend? I remember I encountered this with dx11 on mingw. The window was just black and nothing happened.

-------------------------

Numerator | 2018-06-15 16:12:44 UTC | #8

The backend is D3D9.

-------------------------

Numerator | 2018-06-15 17:21:24 UTC | #9

I am getting a memory exception in DrawPrimitive in my application

-------------------------

Numerator | 2018-06-15 17:30:21 UTC | #10

I demos are not just blank, as I originally thought.  Depending on the camera position, the scene is blank.  If I move the camera slightly, the scene is correct.  Do you have a Windows 64 system to repro this?

-------------------------

Eugene | 2018-06-15 18:19:03 UTC | #11

Could you specify exact Visual Studio version?

-------------------------

DavidHT | 2018-06-15 19:12:20 UTC | #12

You need Visual Studio 2017, version 15.7.3.
The update is quite recent, and solves the matrix multiplication issue that caused this.

-------------------------

Numerator | 2018-06-15 20:17:11 UTC | #13

You are right.  I thought I had the latest version of VS since I recently updated.  I did not.  I updated and the demos work now.  

Thanks all.

-------------------------

Numerator | 2018-06-15 22:01:12 UTC | #14

I'm still getting the memory exception in DrawPrimitive, though.

-------------------------

Eugene | 2018-06-15 22:57:59 UTC | #15

Steps to reproduce and callstack, please.

-------------------------

Numerator | 2018-06-16 01:58:45 UTC | #16

The repro case is just https://github.com/aster2013/ParticleEditor2D
I updated the cmake file to Qt5 and use Win64.  It did not take too long to update it.

The default seems to be D3D

-------------------------

Numerator | 2018-06-16 02:20:27 UTC | #17

This version of the ParticleEditor is a fork or the original and has some work done.  It uses QtOpenGL, but also crashes most of the time.

https://github.com/kostik1337/ParticleEditor2D

-------------------------

George1 | 2018-06-16 13:31:21 UTC | #18

I never had this issue using vs 2015 as well as 2017.

-------------------------

