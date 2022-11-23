Nfs | 2018-08-09 19:18:57 UTC | #1

Hello urho world !

I'm trying to compile and test Urho for the first time, So I grabbed the source code, compiled using codelite and everything worked fine, until I run a sample.
textures and models seems to be loaded correctly, but i get this weird output

![crowdnavigation|641x500](upload://zAkAvxspiLr8Mf9cbOTWl1xTm1G.jpeg)

I have the same result for every program i run after compiling myself, downloaded binary sample for windows works fine, any ideas on what can cause this ?

I followed this : https://github.com/urho3d/Urho3D/wiki/Compiling-Urho3D-on-Windows 

Env : 
windows 10 64b
codelight IDE 12
urho 1.7 latest downloaded from source forge
Compiler : mingw 8.1
Graphic card : GTX 1060

-------------------------

Enhex | 2018-08-09 18:44:31 UTC | #2

what's ur GPU? does it support the version of OpenGL/D3D you're using with Urho?

-------------------------

Nfs | 2018-08-09 18:58:53 UTC | #3

Nvidia gtx  1060, all setup is by default  so urho should use dx9 right ? In that case, yes it's supposed to be supported

-------------------------

Eugene | 2018-08-09 19:12:14 UTC | #4

What compiler do you use?

-------------------------

Nfs | 2018-08-09 19:25:25 UTC | #5

Mingw 8.1 *updated in my original post

Building urho with option  -DURHO3D_D3D11=1, give me a colored screen without anything else.

I will look at this more tomorrow

-------------------------

SirNate0 | 2018-08-09 20:52:49 UTC | #6

You followed all of these directions? (I ask because I don't think mingw-w64 has that high a version released, but I may be wrong as that's from a very brief search and I develop mostly on Linux)

> If using MinGW to compile, DirectX headers may need to be acquired separately. They can be copied to the MinGW installation eg. from the following package: https://www.libsdl.org/extras/win32/common/directx-devel.tar.gz. These will be missing some of the headers related to shader compilation, so a MinGW build will use OpenGL by default. To build in Direct3D mode, the MinGW-w64 port is necessary: http://mingw-w64.sourceforge.net/. Using it, Direct3D can be enabled with the "-DURHO3D_OPENGL=0" build option.

Does the same result occur building for OpenGL?

-------------------------

weitjong | 2018-08-10 21:01:35 UTC | #7

Most probably related to this.

https://github.com/urho3d/Urho3D/issues/2326

-------------------------

alexrass | 2018-08-10 21:01:36 UTC | #8

Urho3D from master or tagged 1.7?
From master working perfect with mingw 8.1.
If 1.7, need remove "-ffast-math" option.

-------------------------

Nfs | 2018-08-10 21:05:27 UTC | #9

> [SirNate0](https://discourse.urho3d.io/u/SirNate0)
You followed all of these directions? (I ask because I don’t think mingw-w64 has that high a version released, but I may be wrong as that’s from a very brief search and I develop mostly on Linux)

Same here, used to linux, i'm completely lost regarding windows.

I confirm this is related to the gcc 8.1 bug, removing -ffast-math solved the problem

Thanks for the help

-------------------------

