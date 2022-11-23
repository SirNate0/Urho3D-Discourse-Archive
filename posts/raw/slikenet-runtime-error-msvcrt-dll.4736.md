green-zone | 2018-12-12 11:59:15 UTC | #1

Compilation - MinGW, Windows XP 32bit
Master branch from 7 Dec 2018

With URHO3D_NETWORK
Compilation - OK
RunTime:
An entry point to the _vsnprintf_s procedure was not found in the msvcrt.dll library

Without URHO3D_NETWORK - there are no runtime errors

CMake scripts or code use msvcrt.dll - version for Vista+ OS
But SLikeNet library say:
OS support: Windows XP (SP3), Windows XP x64 (SP2)
https://github.com/SLikeSoft/SLikeNet

Also strange combination MinGW and Visual Studio runtime library (msvcrt.dll)

Message duplicated here - https://github.com/urho3d/Urho3D/pull/2302#issuecomment-446548586

-------------------------

green-zone | 2018-12-12 16:26:30 UTC | #2

linux_adapter.h
osx_adapter.h
FormatString.cpp and others .cpp files
use vsnprintf_s (not _vsnprintf_s) function.
Maybe the problem is in the build scripts or generated for library headers?

-------------------------

rku | 2018-12-12 17:12:44 UTC | #3

This is probably MingW bug. I myself am having [similar issues](https://sourceforge.net/p/mingw-w64/bugs/775/) with that thing.

-------------------------

green-zone | 2018-12-12 18:12:40 UTC | #4

Other (ThirdParty) libs do not produce this error

ThirdParty\AngelScript\source\as_config.h (608 and 448)
https://github.com/urho3d/Urho3D/blob/master/Source/ThirdParty/AngelScript/source/as_config.h

ThirdParty\Assimp\code\StringUtils.h (48)
https://github.com/urho3d/Urho3D/blob/master/Source/ThirdParty/Assimp/code/StringUtils.h

somehow trying to get around problem.

RakNet not use this string functions.
Urho3D and other libs (i think) also.

I think this is a SLikeNet  problem or build process

-------------------------

