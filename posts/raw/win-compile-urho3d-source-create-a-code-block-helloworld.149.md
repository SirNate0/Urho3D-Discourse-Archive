gasp | 2017-01-02 00:58:23 UTC | #1

=> DownloadCmake from [cmake.org/files/v2.8/cmake-2.8.12.2.zip](http://www.cmake.org/files/v2.8/cmake-2.8.12.2.zip), install it
=> Download MinGW-4.8.1 :
	[sourceforge.net/projects/mingwbu ... z/download](http://sourceforge.net/projects/mingwbuilds/files/host-windows/releases/4.8.1/32-bit/threads-win32/sjlj/x32-4.8.1-release-win32-sjlj-rev5.7z/download)
	install it to : C:\MinGW-4.8.1
Add the following Env variable in windows :
	=>PATH :  [b]C:\MinGW-4.8.1\bin[/b]
	=>URHO3D_HOME : [b]C:\Urho3dSource[/b] (needed later)
	
=> Download latest Urho3d into : c:\Urho3dSource
=> launch [b]cmake_clean.bat[/b] in c:\Urho3dSource (not mandatory)
=> [b]cmake_mingw.bat -URHO3D_OPENGL=1[/b]  (if you want to use Direct X don't put useOPENGL, i don't have Direct X SDK installed on this computer)
=> go into [i]"Build"[/i] directory, type : cmake . 
=> grab missing header file : [libsdl.org/extras/win32/comm ... vel.tar.gz](http://www.libsdl.org/extras/win32/common/directx-devel.tar.gz)), [b]put them into [/b]C:\MinGW-4.8.1 (directory will match
=> type : [b]mingw32-make.exe[/b] in "Build" directory
=> wait the compilation finish 100% :
[code]
Linking CXX static library libAssimp.a
[100%] Built target Assimp
Scanning dependencies of target AssetImporter
[100%] Building CXX object Tools/AssetImporter/CMakeFiles/AssetImporter.dir/Asse
tImporter.cpp.obj
Linking CXX executable c:\Urho3dSource\Source\Bin\AssetImporter.exe
[100%] Built target AssetImporter
Scanning dependencies of target OgreImporter
[100%] Building CXX object Tools/OgreImporter/CMakeFiles/OgreImporter.dir/OgreIm
porter.cpp.obj
Linking CXX executable c:\Urho3dSource\Source\Bin\OgreImporter.exe
[100%] Built target OgreImporter
Scanning dependencies of target PackageTool
[100%] Building CXX object Tools/PackageTool/CMakeFiles/PackageTool.dir/PackageT
ool.cpp.obj
Linking CXX executable c:\Urho3dSource\Source\Bin\PackageTool.exe
[100%] Built target PackageTool
Scanning dependencies of target RampGenerator
[100%] Building CXX object Tools/RampGenerator/CMakeFiles/RampGenerator.dir/Ramp
Generator.cpp.obj
Linking CXX executable c:\Urho3dSource\Source\Bin\RampGenerator.exe
[100%] Built target RampGenerator
Scanning dependencies of target ScriptCompiler
[100%] Building CXX object Tools/ScriptCompiler/CMakeFiles/ScriptCompiler.dir/Sc
riptCompiler.cpp.obj
Linking CXX executable c:\Urho3dSource\Source\Bin\ScriptCompiler.exe
[100%] Built target ScriptCompiler
[/code]



Normally now Urho3d is build from source, we will make a code::block ([codeblocks.org/](http://codeblocks.org/)) project with a sample, the hello World.

make c:\helloWord directory (name it whatever you like) 
	=> create the "bin" directory in c:\helloWorld\bin [b]mkdir c:\helloWorld\bin[/b]
	=> create the symlink (in an Administrator right cmd.exe ): 
		[b]mklink /d "C:\helloWorld\bin\Data" "c:\Urho3dSource\Bin\Data" [/b]
		[b]mklink /d "C:\helloWorld\bin\CoreData" "c:\Urho3dSource\Bin\CoreData"[/b]
	=> create c:\helloWorld\Source directory [b]mkdir c:\helloWorld\Source[/b]
		copy : HelloWorld.cpp, HelloWorld.h, Sample.h,Sample.inl from c:\Urho3dSource\Source\Samples\ && c:\Urho3dSource\Source\Samples\01_HelloWorld into the source directory
	=> create c:\helloWorld\Source\CMakeLists.txt, put the following content (taken from from [urho3d.github.io/documentation/a00004.html](http://urho3d.github.io/documentation/a00004.html)) :
[code]
# Set project name
project (MySuperDuperGame)
# Set minimum version
cmake_minimum_required (VERSION 2.8.6)
if (COMMAND cmake_policy)
cmake_policy (SET CMP0003 NEW)
endif ()
# Set CMake modules search path
set (CMAKE_MODULE_PATH $ENV{URHO3D_HOME}/Source/CMake/Modules CACHE PATH "Path to Urho3D-specific CMake modules")
# Include Urho3D Cmake common module
include (Urho3D-CMake-common)
# Find Urho3D library
find_package (Urho3D REQUIRED)
include_directories (${URHO3D_INCLUDE_DIRS})
# Define target name
set (TARGET_NAME Main)
# Define source files
define_source_files ()
# Setup target with resource copying
setup_main_executable ()
[/code]
	==> Create the "cmake_mingwCodeBlock.bat" in "C:\helloWorld\"
the content (slightly modified from cmake ming.bat :
[code]
::
:: Copyright (c) 2008-2014 the Urho3D project.
::
:: Permission is hereby granted, free of charge, to any person obtaining a copy
:: of this software and associated documentation files (the "Software"), to deal
:: in the Software without restriction, including without limitation the rights
:: to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
:: copies of the Software, and to permit persons to whom the Software is
:: furnished to do so, subject to the following conditions:
::
:: The above copyright notice and this permission notice shall be included in
:: all copies or substantial portions of the Software.
::
:: THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
:: IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
:: FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
:: AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
:: LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
:: OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
:: THE SOFTWARE.
::

@echo off
pushd %~dp0
cmake -E make_directory Build
echo on
:: \todo suppress policy warning (for 2.8.12 early adopters), remove this option when CMake minimum version is 2.8.12
set "OPT=-Wno-dev"
cmake -E chdir Build cmake %OPT% -G "CodeBlocks - MinGW Makefiles" %* ..\Source
@popd
[/code]

	==> type in c:\helloWorld\ directory : [b]cmake_mingwCodeBlock.bat -DUSE_OPENGL=1[/b]
[code]
-- The C compiler identification is GNU 4.8.1
-- The CXX compiler identification is GNU 4.8.1
-- Check for working C compiler: C:/MinGW-4.8.1/bin/gcc.exe
-- Check for working C compiler: C:/MinGW-4.8.1/bin/gcc.exe -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: C:/MinGW-4.8.1/bin/g++.exe
-- Check for working CXX compiler: C:/MinGW-4.8.1/bin/g++.exe -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Using SSE2 instead of SSE because SSE fails on some Windows ports of GCC
-- Disable SSE with the CMake option -DENABLE_SSE=0 if this is not desired
-- Found Urho3D: D:/Developpement/Urho3D/Lib/libUrho3D.a
-- Configuring done
-- Generating done
-- Build files have been written to: D:/Developpement/myProject/Source
[/code]

	==> open MySuperDuperGame.cbp  from "Build" directory with code::block
	==> select the "main" build option, and "build and run" icon
	==> Normally you will have somethings like that :

	[code]
-------------- Build: Main in MySuperDuperGame (compiler: GNU GCC Compiler)---------------

Running command: C:/MinGW-4.8.1/bin/mingw32-make.exe -f "D:/Developpement/myProject/Source/Makefile"  VERBOSE=1 Main
"C:\Program Files (x86)\CMake 2.8\bin\cmake.exe" -HD:\Developpement\myProject\Source -BD:\Developpement\myProject\Source --check-build-system CMakeFiles\Makefile.cmake 0
C:/MinGW-4.8.1/bin/mingw32-make.exe -f CMakeFiles\Makefile2 Main
mingw32-make.exe[1]: Entering directory 'D:/Developpement/myProject/Source'
"C:\Program Files (x86)\CMake 2.8\bin\cmake.exe" -HD:\Developpement\myProject\Source -BD:\Developpement\myProject\Source --check-build-system CMakeFiles\Makefile.cmake 0
"C:\Program Files (x86)\CMake 2.8\bin\cmake.exe" -E cmake_progress_start D:\Developpement\myProject\Source\CMakeFiles 1
C:/MinGW-4.8.1/bin/mingw32-make.exe -f CMakeFiles\Makefile2 CMakeFiles/Main.dir/all
mingw32-make.exe[2]: Entering directory 'D:/Developpement/myProject/Source'
C:/MinGW-4.8.1/bin/mingw32-make.exe -f CMakeFiles\Main.dir\build.make CMakeFiles/Main.dir/depend
mingw32-make.exe[3]: Entering directory 'D:/Developpement/myProject/Source'
"C:\Program Files (x86)\CMake 2.8\bin\cmake.exe" -E cmake_depends "MinGW Makefiles" D:\Developpement\myProject\Source D:\Developpement\myProject\Source D:\Developpement\myProject\Source D:\Developpement\myProject\Source D:\Developpement\myProject\Source\CMakeFiles\Main.dir\DependInfo.cmake --color=
Dependee "D:\Developpement\myProject\Source\CMakeFiles\Main.dir\DependInfo.cmake" is newer than depender "D:/Developpement/myProject/Source/CMakeFiles/Main.dir/depend.internal".
Dependee "D:/Developpement/myProject/Source/CMakeFiles/CMakeDirectoryInformation.cmake" is newer than depender "D:/Developpement/myProject/Source/CMakeFiles/Main.dir/depend.internal".
Scanning dependencies of target Main
mingw32-make.exe[3]: Leaving directory 'D:/Developpement/myProject/Source'
C:/MinGW-4.8.1/bin/mingw32-make.exe -f CMakeFiles\Main.dir\build.make CMakeFiles/Main.dir/build
mingw32-make.exe[3]: Entering directory 'D:/Developpement/myProject/Source'
"C:\Program Files (x86)\CMake 2.8\bin\cmake.exe" -E cmake_progress_report D:\Developpement\myProject\Source\CMakeFiles 1
[100%] Building CXX object CMakeFiles/Main.dir/StaticScene.cpp.obj
C:\MinGW-4.8.1\bin\g++.exe   -DENABLE_ANGELSCRIPT -DENABLE_FILEWATCHER -DENABLE_LOGGING -DENABLE_PROFILING -DENABLE_SSE -DGLEW_NO_GLU -DGLEW_STATIC -DURHO3D_STATIC_DEFINE -DUSE_OPENGL -Wno-invalid-offsetof -ffast-math -m32 -msse2 -static -static-libstdc++ -static-libgcc -O2 -DNDEBUG @CMakeFiles/Main.dir/includes_CXX.rsp   -o CMakeFiles\Main.dir\StaticScene.cpp.obj -c D:\Developpement\myProject\Source\StaticScene.cpp
Linking CXX executable c:\helloWorld\bin\Main.exe
"C:\Program Files (x86)\CMake 2.8\bin\cmake.exe" -E cmake_link_script CMakeFiles\Main.dir\link.txt --verbose=1
"C:\Program Files (x86)\CMake 2.8\bin\cmake.exe" -E remove -f CMakeFiles\Main.dir/objects.a
C:\MinGW-4.8.1\bin\ar.exe cr CMakeFiles\Main.dir/objects.a @CMakeFiles\Main.dir\objects1.rsp
C:\MinGW-4.8.1\bin\g++.exe   -Wno-invalid-offsetof -ffast-math -m32 -msse2 -static -static-libstdc++ -static-libgcc -O2 -DNDEBUG    -mwindows -Wl,--whole-archive CMakeFiles\Main.dir/objects.a -Wl,--no-whole-archive  -o c:\helloWorld\bin\Main.exe -Wl,--out-implib,libMain.dll.a -Wl,--major-image-version,0,--minor-image-version,0  c:\Urho3dSource\Source\Lib\libUrho3D.a -luser32 -lgdi32 -lwinmm -limm32 -lole32 -loleaut32 -lversion -luuid -lws2_32 -lwinmm -lopengl32 -limm32 -lole32 -loleaut32 -lversion -luuid -lws2_32 -lopengl32 -lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 -lole32 -loleaut32 -luuid -lcomdlg32 -ladvapi32 
mingw32-make.exe[3]: Leaving directory 'D:/Developpement/myProject/Source'
"C:\Program Files (x86)\CMake 2.8\bin\cmake.exe" -E cmake_progress_report D:\Developpement\myProject\Source\CMakeFiles  1
[100%] Built target Main
mingw32-make.exe[2]: Leaving directory 'D:/Developpement/myProject/Source'
"C:\Program Files (x86)\CMake 2.8\bin\cmake.exe" -E cmake_progress_start D:\Developpement\myProject\Source\CMakeFiles 0
mingw32-make.exe[1]: Leaving directory 'D:/Developpement/myProject/Source'
Process terminated with status 0 (0 minute(s), 4 second(s))
0 error(s), 0 warning(s) (0 minute(s), 4 second(s))
 

-------------- Run: Main in MySuperDuperGame (compiler: GNU GCC Compiler)---------------

Checking for existence: c:\helloWorld\bin\Main.exe
Executing: "c:\helloWorld\bin\Main.exe"  (in D:\Developpement\myProject\Bin)
Process terminated with status 0 (0 minute(s), 3 second(s))
[/code]

the hello World must pop show !!
The 2 next thing i will try to make :
	=> the same type of post for build for android (if this can help someone) 
	=> integrate an external lib in the hello world and link it with angel script (i don't know for now to make it, i will search in the cmake syntax to add a dependance or maybe just cpp file with the lib, will try diffrentent things)
	
	if i've make a mistake / language errors, don't hesitate to correct me

-------------------------

GIMB4L | 2017-01-02 00:58:23 UTC | #2

I had a similar issue, but I was using Visual Studio. Regardless, I tried to make my own project and do all the linking, include directories, etc, but I couldn't get it to compile. Then I found this page here: [url]http://urho3d.github.io/documentation/a00004.html[/url] which told me to use CMake to generate a standalone project. Following those instructions, the project built.

-------------------------

Hevedy | 2017-01-02 00:58:23 UTC | #3

The SDL source code are included in Urho3D source with all other libs
I use the code of Github in win7 x64 for compile Static x32 versions with VS 2012 and with Qt using VS and work fine

-------------------------

gasp | 2017-01-02 00:58:23 UTC | #4

The idea was to have a light solution, not use VIsual Studio (i'm not familiar with it).

Probably codelite is a better solution (it tend to support Cmake, i need to do some reseach to be able to compile from Urho3d Source and add the HelloWorld.cpp Sample.

-------------------------

gasp | 2017-01-02 00:58:24 UTC | #5

updated the 1st Post

-------------------------

