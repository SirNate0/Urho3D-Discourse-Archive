xlat | 2021-12-06 07:52:22 UTC | #1

What Compiler is recommended for building Urho3D under Windows 7 32 bit?

Code::Block MSYS GCC 10.3 + 32 libs
On Windows 7 32bits Urho3DPlayer-32bits.exe **APP CRASH crashes!**

On Windows 10 64bits Urho3DPlayer-32bits.exe  all good ...

-------------------------

weitjong | 2021-12-06 13:24:17 UTC | #2

Have you tried MinGW-w64? Despite its name, it has 32-bit version and 64-bit version. Both versions of the compiler should work well.

-------------------------

xlat | 2021-12-06 13:30:07 UTC | #3

Yes, I'm doing experiments now.
There are a lot of different compilers and their versions around me, and the compilation time is quite long. And while compiling decided to ask here.

-------------------------

weitjong | 2021-12-06 13:55:54 UTC | #4

Good luck. Make sure you don’t forget to use the “-j” option to utilize all the CPU cores during compilation.

-------------------------

