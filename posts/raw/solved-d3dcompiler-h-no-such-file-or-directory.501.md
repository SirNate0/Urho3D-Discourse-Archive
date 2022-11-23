kestli | 2017-01-02 01:00:54 UTC | #1

Hello friends
I have one problem when compile Urho3D for Direct3D under MinGW width Eclipse.
I have installed D3D_SDK 2010, und set directory path in Eclipse project "C:\Program Files (x86)\Microsoft DirectX SDK (june 2010)\Include"
I use Win8.1 
[quote][ 63%] Building CXX object Engine/CMakeFiles/Urho3D.dir/Graphics/Direct3D9/D3D9ShaderVariation.cpp.obj
cd /d E:\Downloads\Urho3D-1.31\Build\Engine && C:\mingw64\bin\g++.exe   -DENABLE_ANGELSCRIPT -DENABLE_FILEWATCHER -DENABLE_LOGGING -DENABLE_PROFILING -DHAVE_STDINT_H -DURHO3D_STATIC_DEFINE -Wno-invalid-offsetof -ffast-math -m64 -static -static-libstdc++ -static-libgcc -O2 -DNDEBUG @CMakeFiles/Urho3D.dir/includes_CXX.rsp   -o CMakeFiles\Urho3D.dir\Graphics\Direct3D9\D3D9ShaderVariation.cpp.obj -c E:\Downloads\Urho3D-1.31\Source\Engine\Graphics\Direct3D9\D3D9ShaderVariation.cpp
E:\Downloads\Urho3D-1.31\Source\Engine\Graphics\Direct3D9\D3D9ShaderVariation.cpp:34:25: fatal error: d3dcompiler.h: No such file or directory
compilation terminated.[/quote]

My cmake_eclipse.bat
[quote]
cmake -E make_directory Build
set "OPT=-Wno-dev -DENABLE_64BIT=1 -DUSE_OPENGL=0 -DENABLE_SSE=0" 
cmake -E chdir Build cmake %OPT% -G "Eclipse CDT4 - MinGW Makefiles" %* ..\Source
[/quote]

Vielen Dank

-------------------------

weitjong | 2017-01-02 01:00:54 UTC | #2

Guten Tag

I have not tried to build in that combination before but if I understand correctly our current CMake build scripts then I would say they do not handle such case well. In the Urho3D-CMake-common.cmake module ([github.com/urho3d/Urho3D/blob/1 ... ke#L83-L87](https://github.com/urho3d/Urho3D/blob/1.31/Source/CMake/Modules/Urho3D-CMake-common.cmake#L83-L87)) it says that it may work with MinGW-W64 distribution. I have a MinGW-W64 installed in my Win7 VM and I can confirm the "d3dcompiler.h" can be found in one of the "include" sub-dir shipped with the distribution. The question is still whether our CMake build scripts has configured the Makefile to look for the "d3dcompiler.h" there. Are you using MinGW-W64?

Also you may want to know that our CMake build scripts (in v1.31 and even current HEAD) do not attempt to find Direct3D SDK for non-MSVC compiler on Windows. So, unless you have manually altered the CMake build scripts I doubt that your generated Makefile is currently using the June 2010 SDK. You can double check that by searching for "DIRECT3D_INCLUDE_DIRS" variable in the Build/CMakeCache.txt. If you want to use the SDK then you have to modify the script to call "find_package (Direct3D)". Hint: [github.com/urho3d/Urho3D/blob/1 ... #L141-L149](https://github.com/urho3d/Urho3D/blob/1.31/Source/CMake/Modules/Urho3D-CMake-common.cmake#L141-L149). Note that someone may have attempted that and did not work in the past but YMMV, so do report back.

-------------------------

cadaver | 2017-01-02 01:00:54 UTC | #3

The DirectX SDK doesn't support other compilers than MSVC, so for compilers like MinGW one needs to rely on the include files & libs included with the compiler distribution.

With MinGW, you should always be able to at least make an OpenGL build with -DURHO3D_OPENGL=1. For DirectX related work I'd actually recommend installing some MSVC Express Edition, so that you can actually rely on MS's own SDK's, and not something hacked together by 3rd parties.

EDIT: there was a DirectX *linking* bug on MinGW, which should be fixed now. It should have no effect for d3dcompiler.h not being found, though.

-------------------------

kestli | 2017-01-02 01:00:56 UTC | #4

Thanks for the replies ... 
It all makes sense, and even talking about .dll's
Thank you for this wonderful game engine...

-------------------------

weitjong | 2017-01-02 01:00:56 UTC | #5

Sorry for the mess that I had created when I changed those hard-coded library reference while refactoring our CMake modules recently. I would give it another try to avoid hard-coding later when I have time. Having said that, the mistake that I made should cause linking error instead of compiling error. Anyway it is not important now. :slight_smile:

-------------------------

cadaver | 2017-01-02 01:00:57 UTC | #6

No worries. It might be more ideal to let the DirectX detection module run always (when using Direct3D instead of OpenGL) regardless of compiler, and it would setup the LIBRARIES in a hardcoded manner if using MinGW. That way later code would not need to have branching logic.

-------------------------

weitjong | 2017-01-02 01:00:57 UTC | #7

That's exactly what I am attempting now.

-------------------------

weitjong | 2017-01-02 01:00:57 UTC | #8

I need some help here. On my system even with the hard-coded library references, it fails to link because my MinGW cannot find -ld3dcompiler. That happened both with MinGW on my Win7 and MinGW on my Linux. I have to change it to "d3dcompiler_43" or "d3dcompiler_46" to work. Apparently only the libd3dcompiler_43.a or libd3dcompiler_46.a exists in my installation, but not the libd3dcompiler.a. What gives?

After the exe is built, it could not be launched because it complains that d3dcompiler_46.dll is missing. The VS 2013 express that I have on my Win7 VM only has d3dcompiler_47.dll. So, how do you guys build using MinGW having URHO3D_OPENGL=0?

-------------------------

cadaver | 2017-01-02 01:00:57 UTC | #9

This may depend on the MinGW build version. I have here one mingw-w64 install that is based on GCC 4.8.1, and it has both libd3dcompiler.a + several libd3dcompiler_xx.a, where xx ranges from 33 to 46. When compiling Urho with it, the resulting exe depends on d3dcompiler_43.dll.

You should get the missing d3dcompiler dlls by either updating the DirectX runtime, or from Microsoft's SDK's. The versions past the June 2010 SDK are actually only available as part of Windows SDK.

-------------------------

weitjong | 2017-01-02 01:00:59 UTC | #10

Thanks for the answer. I think I understand it a little bit better now. I have a slightly more recent MinGW build than yours on my F20 Linux and yet even newer build on my Win7 VM. By sheer luck both my MinGW installations really do not ship with libd3dcompiler.a. I do have a range of libd3dcompiler_xx.a (from version 33 to 46) installed, but just not the libd3dcompiler.a itself. Interestingly, only the oldest MinGW built that I got (on my Ubuntu 12.04 LTS VM) has this file. I guess I can simply create a "libd3dcompiler.a" symlink or mklink which actually points to one of the version that I want to use. I have just tested that successfully with mklink on Win7. My next problem is to hunt down the corresponding dll to test the executables. As you can see, I actually don't need the latest updated DirectX runtime, on the contrary I need their older versions. I only have version 47 from VS 2013 express but what I need is 46 dll. I should have kept my VS2012 express installed, if I knew this is going to happen.

I have spent more time to sort this out then the time I spent to fix the FindDirect3D.cmake module to avoid the hard-coding :slight_smile:.

EDIT: just completed the window search and see under "c:\Windows\System32" it has a few versions of dll there. Version 43 is the highest number (although the search result do find other higher versions but they are not in this directory and not being searched by default by our executables). Conclusion, pointing to the libd3dcompiler_43.a seems to be the best. With this knowledge, I think I am able to add a few more Travis-CI build with MinGW + OpenGL=0 combination.

-------------------------

weitjong | 2017-01-02 01:01:00 UTC | #11

@kestli, sorry to hijack your thread for my own quest :slight_smile:. But I think you would like know that in doing so, I was able to reproduce your exact compiling error on Travis-CI. It turns out that MinGW software package (distribution) is not created the same from version to version. The version that we have in Travis-CI is quite old and it does not come with "d3dcompiler.h". So, that could be what happened to your problem too (assuming you are using MinGW-W64 already). I solved the problem in Travis-CI by downloading the missing header from MinGW-W64 source package hosted in Ubuntu Launchpad. For your case, I think it is easier just to upgrade the MinGW distribution.

-------------------------

kestli | 2017-01-02 01:01:08 UTC | #12

Weitjong thanks for your time. It is an honor to create this kind of talk and learn from two people who know what they are talking ...
Following your advice I was able to compile Urho3D to Direct3D with MinGW-w64 on Windows8.1 (saving some new errors).

[quote]
1 - I upgraded MinGW to the latest version which includes libraries d3dcompiler_xx.a
2 - Rename d3dcompiler_46.a to d3dcompiler.a
3 - Specify the path C: \>SET LIBRARY_PATH="C:\mingw64\x86_64-w64-mingw32\lib"
4 - mingw32-make
5 - I copied the library d3dcompiler_46.dll alongside Urho3D.dll (SHARED lib option)
[/quote]
With these steps I was able to compile and run successfully  :smiley:

-------------------------

