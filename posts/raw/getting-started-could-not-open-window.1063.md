KNS | 2017-01-02 01:05:09 UTC | #1

Using the pre-built binaries and ones that I have built with GCC4.81 (Windows 64bit) I cannot run the samples.  They all stop with "could not open window".  Clearly I'm doing something wrong.  Any assistance would be most appreciated.

Thanks.

-------------------------

weitjong | 2017-01-02 01:05:09 UTC | #2

Welcome to our forum.

The "Could not open window" error could only happen in the OpenGL code path. In your Windows host system, do you have OpenGL graphic driver installed?

-------------------------

KNS | 2017-01-02 01:05:10 UTC | #3

GLView reports v4.4 for OpenGL on a GeForce GTX 660 Ti while dxdiag reports DirectX 11 installed.   Though it seems that the NVidia driver is performing as expected I`ll probably update.
In addition to trying the pre-built binaries I built for both OpenGL and DirectX, resulting in the same errors.


UPDATE: Though all seemed fine with the slightly older driver, updating to the most recent from NVidia solved the problem.

-------------------------

