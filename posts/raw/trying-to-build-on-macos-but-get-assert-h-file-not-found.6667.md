Askhento | 2021-01-18 00:45:10 UTC | #1

Here is a full error 
```
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/../include/c++/v1/cassert:20:10: fatal error: 'assert.h' file not found
#include <assert.h>
         ^~~~~~~~~~
1 error generated.
CMake Error at cmake/Modules/UrhoCommon.cmake:1289 (message):
  Could not generate dependency list for PCH.  There is something wrong with
  your compiler toolchain.  Ensure its bin path is in the PATH environment
  variable or ensure CMake can find CC/CXX in your build environment.
Call Stack (most recent call first):
  Source/Urho3D/CMakeLists.txt:408 (enable_pch)

```
Command line tools installed.

-------------------------

vmost | 2021-01-18 13:44:51 UTC | #2

You may want to check [this post](https://discourse.urho3d.io/t/info-using-urho3d-with-old-mac-osx-10-11/6304). MacOS can't use the pre-compiled header (PCH).

-------------------------

Askhento | 2021-01-18 13:46:50 UTC | #3

Ok this helped, but after I run make, get this error at 92%
```
/GameEngines/Urho3D_repo/Source/ThirdParty/Assimp/contrib/zlib/gzlib.c:252:9: error: 
      implicit declaration of function 'lseek' is invalid in C99
```
Maybe I don't need to compile the engine in the first place? Have never done this before.

-------------------------

vmost | 2021-01-18 14:00:06 UTC | #4

Edit: [see this](https://github.com/Blosc/python-blosc/issues/229). Building things on mac is always a hack-a-thon...

You have to go into the file at `/GameEngines/Urho3D_repo/Source/ThirdParty/Assimp/contrib/zlib/gzguts.h` (not gzlib.c) and include `#include <unistd.h>`

-------------------------

Askhento | 2021-01-18 15:15:22 UTC | #5

Finally! Thanks you really helped)
![image|345x170](upload://5Q6Z6tBe0V9Jz7JJlZQ2OSHXXjZ.png)

-------------------------

