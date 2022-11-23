haolly | 2017-11-27 12:21:03 UTC | #1

Hi @weitjong , I try to build Urho3D on my mac, using Ninja and Clion(with Clion, I mean  open the build tree in Clion, let Clion to automatic build ) , both complains error: no suitable precompiled header file found in directory '/Users/haolly/dev/Urho3D/Build/Source/Urho3D/Precompiled.h.pch'

This was asked on gitter, but someone suggest me to ask in the forum

-------------------------

Victor | 2017-11-29 06:33:20 UTC | #2

On Mac OSX (using CLion), I always have to set the following:

//Enable PCH support
URHO3D_PCH:BOOL=OFF

I hope that helps!

-------------------------

weitjong | 2017-11-28 01:52:09 UTC | #3

Victor is correct, that’s the manual workaround if the build script does not auto-turn off the PCH when Clang compiler toolchain is being detected. On Linux I have CLion setup to use my source tree and let it generate the build tree for me. HTH.

-------------------------

haolly | 2017-11-28 14:21:53 UTC | #4

I changed the option in CmakeCache.txt , and reload project in Clion, the same error still exits.

But add -DURHO3D_PCH=0 in Cmake Setting works for me

-------------------------

weitjong | 2017-11-29 00:18:05 UTC | #5

If you just import the build tree in Clion then modifying the CMakeCache.txt or any of the CMake build script will not have any effects to your already generated build tree. If you set it up to use source tree then the build tree will be auto-generated or automatically modified when CLion detects the changes and invoke the CMake to do the necessary.

-------------------------

haolly | 2017-11-29 13:28:56 UTC | #6

@weitjong 
One more question, the c++11 feature is not recognized by cmake
> CMake Warning:
>   Manually-specified variables were not used by the project:
> 
>     URHO3D_C++11

-------------------------

Eugene | 2017-11-29 14:10:26 UTC | #7

There is no such option anymore in Urho above 1.7
Where did you find it?

-------------------------

haolly | 2017-11-29 15:04:45 UTC | #8

https://urho3d.github.io/documentation/1.7/_building.html
Build options section

-------------------------

Eugene | 2017-11-29 15:16:04 UTC | #9

Thanks, I forgot to remove it.

-------------------------

