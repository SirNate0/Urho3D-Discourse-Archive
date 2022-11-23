Pablo | 2017-01-02 00:59:28 UTC | #1

Hi,

I'm getting the following error when trying to link SDL with MinGW32 when building Urho3D as a shared library:

[quote]Linking CXX shared library C:\Urho3D\Bin\Urho3D.dll
..\ThirdParty\SDL\libSDL.a(SDL_mmjoystick.c.obj):SDL_mmjoystick.c:(.text+0x37): undefined reference to `joyGetNumDevs@0'
..\ThirdParty\SDL\libSDL.a(SDL_mmjoystick.c.obj):SDL_mmjoystick.c:(.text+0xa2): undefined reference to `joyGetPosEx@8'
..\ThirdParty\SDL\libSDL.a(SDL_mmjoystick.c.obj):SDL_mmjoystick.c:(.text+0xc3): undefined reference to `joyGetDevCapsA@12'
..\ThirdParty\SDL\libSDL.a(SDL_mmjoystick.c.obj):SDL_mmjoystick.c:(.text+0x602): undefined reference to `joyGetPosEx@8'
Engine\CMakeFiles\Urho3D.dir\build.make:5784: recipe for target 'C:/Urho3D/Bin/Urho3D.dll' failed
CMakeFiles\Makefile2:939: recipe for target 'Engine/CMakeFiles/Urho3D.dir/all' failed
Makefile:135: recipe for target 'all' failed
c:/mingw/bin/../lib/gcc/mingw32/4.8.1/../../../../mingw32/bin/ld.exe: ..\ThirdParty\SDL\libSDL.a(SDL_mmjoystick.c.obj): bad reloc address 0x20 in section `.eh_frame'
collect2.exe: error: ld returned 1 exit status
mingw32-make[2]: *** [C:/Urho3D/Bin/Urho3D.dll] Error 1
mingw32-make[1]: *** [Engine/CMakeFiles/Urho3D.dir/all] Error 2
mingw32-make: *** [all] Error 2
23:55:55: The process "C:\MinGW\bin\mingw32-make.exe" exited with code 2.
Error while building/deploying project Urho3D (kit: Desktop)
When executing step 'Make'[/quote]

My CMake configuration is -DURHO3D_OPENGL=1 -DURHO3D_LIB_TYPE=SHARED and the output:
[quote]-- The C compiler identification is GNU 4.8.1
-- The CXX compiler identification is GNU 4.8.1
-- Check for working C compiler: C:/MinGW/bin/gcc.exe
-- Check for working C compiler: C:/MinGW/bin/gcc.exe -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: C:/MinGW/bin/g++.exe
-- Check for working CXX compiler: C:/MinGW/bin/g++.exe -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Using SSE2 instead of SSE because SSE fails on some Windows ports of GCC
-- Disable SSE with the CMake option -DURHO3D_SSE=0 if this is not desired
-- Looking for include file stdint.h
-- Looking for include file stdint.h - found
-- Looking for include file wbemcli.h
-- Looking for include file wbemcli.h - not found
-- Building SDL without DX joystick support due to missing wbemcli.h
-- For MSVC, get it from Windows 7 SDK. For MinGW, get it from eg. Wine sources or from MinGW-w64
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR - Success
-- Found Urho3D: as CMake target
-- Configuring done
-- Generating done
-- Build files have been written to: C:/Urho3D/Build[/quote]

I got an error previously because I was missing ddraw.h which I took from directx-devel.tar.gz. I don't quite get why would I need anything from DirectX if I'm compiling with URHO3D_OPENGL set to true, but I have installed DirectX (Jun 2010) just in case.

Both compilation and linking go smoothly if I try to build Urho3D as a static library. I also have a different issue trying to compile in debug mode with Assimp's object sizes being too large:

[quote]Building CXX object Engine/CMakeFiles/Urho3D.dir/Physics/PhysicsWorld.cpp.obj
c:/mingw/bin/../lib/gcc/mingw32/4.8.1/../../../../mingw32/bin/as.exe: CMakeFiles\Assimp.dir\code\IFCReaderGen.cpp.obj: too many sections (33064)
C:\Users\Pablo\AppData\Local\Temp\ccAqKUoY.s: Assembler messages:
C:\Users\Pablo\AppData\Local\Temp\ccAqKUoY.s: Fatal error: can't write CMakeFiles\Assimp.dir\code\IFCReaderGen.cpp.obj: File too big
c:/mingw/bin/../lib/gcc/mingw32/4.8.1/../../../../mingw32/bin/as.exe: CMakeFiles\Assimp.dir\code\IFCReaderGen.cpp.obj: too many sections (33064)
C:\Users\Pablo\AppData\Local\Temp\ccAqKUoY.s: Fatal error: can't close CMakeFiles\Assimp.dir\code\IFCReaderGen.cpp.obj: File too big
ThirdParty\Assimp\CMakeFiles\Assimp.dir\build.make:2769: recipe for target 'ThirdParty/Assimp/CMakeFiles/Assimp.dir/code/IFCReaderGen.cpp.obj' failed
mingw32-make[2]: *** [ThirdParty/Assimp/CMakeFiles/Assimp.dir/code/IFCReaderGen.cpp.obj] Error 1
CMakeFiles\Makefile2:1362: recipe for target 'ThirdParty/Assimp/CMakeFiles/Assimp.dir/all' failed
mingw32-make[1]: *** [ThirdParty/Assimp/CMakeFiles/Assimp.dir/all] Error 2[/quote]

Any ideas? Thanks in advance.

-------------------------

alexrass | 2017-01-02 00:59:28 UTC | #2

With mingw-w64 builds perfect.

-------------------------

weitjong | 2017-01-02 00:59:28 UTC | #3

The build scripts are tested almost everyday with mingw-w64 in our CI build using a Linux build system and cross-compiling for Windows as target system. It can build for both 32- and 64-bit despite its name. The MinGW32 has not been thoroughly tested as much as MinGW-W64, I believe.

Regarding the Assimp's object sizes being too large issue on debug configuration build, I thought we have worked around the issue with the changes in the Assimp's CMakeLists.txt. Have a look at this file Source/ThirdParty/Assimp/CMakeLists.txt at lines 11-16. I suppose you are not cross-compiling so the workaround does not kick in. Can you try to remove the CMAKE_CROSSCOMPILING in the if condition and report back if it solves the issue. Thanks.

-------------------------

Pablo | 2017-01-02 00:59:28 UTC | #4

Thanks a million to both of you for the hint.

I downloaded MinGW-w64 for Windows and the shared library compilation worked out of the box. No need to copy ddraw.h etc as in MinGW32 because it's already within the w64's include folder.
I had to change the lines weitjong suggested to compile the debug version, though. I left it as follows:

[quote]if (MINGW)
    # The IFCReaderGen.cpp.obj has too many sections in DEBUG configuration build
    # Since GCC does not support /bigobj compiler flags as in MSVC, we use optimization flags to reduce the object file size
    set (CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -O1")
    set (CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -O1")
endif ()[/quote]

Anyway, is quite a strange thing that MinGW32 is not able to get some SDL symbols if compiled as a shared library.

-------------------------

weitjong | 2017-01-02 00:59:29 UTC | #5

Thanks for the confirmation. I have removed the CMAKE_CROSSCOMPILING condition check in the latest master branch.

-------------------------

Pablo | 2017-01-02 00:59:29 UTC | #6

I tried to compile the 32bit version of Urho3D and I ran into some problems. It turns out I didn't get the proper MinGW-w64 version to do so.
In case someone's interested, this is what worked for me:

Download the MinGW-w64 installer from [url]http://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/installer/mingw-w64-install.exe/download[/url]
Select the following options when installing. I chose GCC 4.8.3 to have the same stable version I have in the rest of OS's.

[img]http://i.snag.gy/62wpt.jpg[/img]

My issue was that I left the exception model by default: which is seh, and is only compatible for 64bits. The compiler was throwing the following error at the very beginning of the compilation (cstdlib):
[quote]error: expected unqualified-id before '__int128' inline __int128[/quote]

To know more about the exception handling and the thread model of MinGW-w64: [url]http://qt-project.org/wiki/MinGW-64-bit[/url]

I hope it helps.

-------------------------

alexrass | 2017-01-02 00:59:29 UTC | #7

I use mingw 4.8.2 i686 posix dwarf rev3
also i try 4.9.0 i686 posix dwarf rev2
working good

-------------------------

