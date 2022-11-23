Bluemoon | 2017-01-02 01:04:37 UTC | #1

I got the master branch of yesterday (9th April 2015), tried building it and got the packaging tool issue below

[code]
[ 76%] Built target PackageTool
[ 76%] Checking and packaging resource directories
Source\Tools\Urho3DPlayer\CMakeFiles\RESOURCE_CHECK.dir\build.make:48: recipe fo
r target 'Source/Tools/Urho3DPlayer/CMakeFiles/RESOURCE_CHECK' failed
mingw32-make[2]: *** [Source/Tools/Urho3DPlayer/CMakeFiles/RESOURCE_CHECK] Error
 1
CMakeFiles\Makefile2:1097: recipe for target 'Source/Tools/Urho3DPlayer/CMakeFil
es/RESOURCE_CHECK.dir/all' failed
mingw32-make[1]: *** [Source/Tools/Urho3DPlayer/CMakeFiles/RESOURCE_CHECK.dir/al
l] Error 2
Makefile:132: recipe for target 'all' failed
mingw32-make: *** [all] Error 2

C:\Urho3D_Master\Build>
[/code]

both URHO3D_PACKAGING and URHO3D_TOOLS were selected in the cmake option.

Any idea what might be wrong?    :neutral_face:

-------------------------

weitjong | 2017-01-02 01:04:37 UTC | #2

That combination was known to have caused problem and we should have fixed the problem about 11 days ago. Perhaps you need to recreate your build tree from scratch again. BTW, I have just tested a clean build with these two build options enabled using MinGW compilers both on my Linux host system and Windows7 VM. Both built without encountering any problem.

-------------------------

Bluemoon | 2017-01-02 01:04:37 UTC | #3

I just tried building it again but still received the same issue

-------------------------

weitjong | 2017-01-02 01:04:37 UTC | #4

But did you create another build tree first? Perhaps you can also post all the build options you use and also the steps you have taken to generate the build tree. And also let us know if you have in anyway altered or customized our CMake build rules or build scripts.

This is what I get on my Windows7 VM. I know it does not help you much but it just to show you that the build rules on RESOURCE_CHECK does work.
[code]C:\Users\weitjong\SDKs\urho3d\Urho3D>rake make mingw target=RESOURCE_CHECK
[  0%] [  1%] [  1%] Built target LZ4
Built target toluapp
Built target minilua
[  6%] Built target FreeType
[  7%] [  7%] [  8%] Built target JO
Built target rapidjson
Built target PugiXml
[  8%] [ 10%] Built target STB
Built target StanHull
[ 15%] [ 15%] Built target AngelScript
Built target Civetweb
[ 19%] Built target kNet
[ 20%] [ 34%] Built target Detour
[ 35%] Built target SDL
Built target Recast
[ 35%] [ 42%] Built target GLEW
[ 42%] Built target Box2D
Built target LibCpuId
[ 61%] [ 62%] Built target Bullet
Built target buildvm
[ 64%] Built target LuaJIT
[ 64%] Built target tolua++
[100%] Built target Urho3D
[100%] Built target PackageTool
[100%] Checking and packaging resource directories
Packaging C:/Users/weitjong/SDKs/urho3d/Urho3D/bin/CoreData...
Packaging C:/Users/weitjong/SDKs/urho3d/Urho3D/bin/Data...
[100%] Built target RESOURCE_CHECK[/code]

-------------------------

Bluemoon | 2017-01-02 01:04:38 UTC | #5

I actually deleted everything, both the build tree and the source folder, redownloaded the master branch (todays version) and built from scratch. But still got the error earlier noted. No modifications were made except setting Urho3D build options using CMake GUI, .

Below is the Urho3D options sections from my builds CMakeCache.txt

[code]
//Enable 64-bit build, on MSVC default to 0, on other compilers
// the default is set based on the 64-bit capability of the chosen
// toolchain on host system
URHO3D_64BIT:BOOL=OFF

//Enable AngelScript scripting support
URHO3D_ANGELSCRIPT:BOOL=ON

//Use Direct3D11 instead of Direct3D9 (Windows platform only);
// overrides URHO3D_OPENGL option
URHO3D_D3D11:BOOL=OFF

//Generate documentation as part of normal build
URHO3D_DOCS:BOOL=ON

//Generate documentation as part of normal build, suppress generation
// process from sending anything to stdout
URHO3D_DOCS_QUIET:BOOL=ON

//Build extras (native and RPI only)
URHO3D_EXTRAS:BOOL=ON

//Enable filewatcher support
URHO3D_FILEWATCHER:BOOL=ON

//Path to Urho3D build tree or SDK installation location (external
// project only)
URHO3D_HOME:PATH=C:/Urho3D_Build

//Specify Urho3D library type, possible values are STATIC (default)
// and SHARED
URHO3D_LIB_TYPE:STRING=STATIC

//Enable logging support
URHO3D_LOGGING:BOOL=ON

//Enable additional Lua scripting support
URHO3D_LUA:BOOL=OFF

//Enable Lua scripting support using LuaJIT (check LuaJIT's CMakeLists.txt
// for more options)
URHO3D_LUAJIT:BOOL=OFF

//Enable navigation support
URHO3D_NAVIGATION:BOOL=ON

//Enable networking support
URHO3D_NETWORK:BOOL=ON

//Use OpenGL instead of Direct3D (Windows platform only)
URHO3D_OPENGL:BOOL=OFF

//Enable resources packaging support, on Emscripten default to
// 1, on other platforms default to 0
URHO3D_PACKAGING:BOOL=ON

//Enable physics support
URHO3D_PHYSICS:BOOL=ON

//Enable profiling support
URHO3D_PROFILING:BOOL=ON

//Build sample applications
URHO3D_SAMPLES:BOOL=ON

//Enable SSE instruction set
URHO3D_SSE:BOOL=ON

//Enable testing support
URHO3D_TESTING:BOOL=ON

//Number of seconds to test run the executables (when testing support
// is enabled only), default to 10 on Emscripten platform and 5
// on other platforms
URHO3D_TEST_TIMEOUT:STRING=5

//Build tools (native and RPI only)
URHO3D_TOOLS:BOOL=ON

//Enable 2D graphics and physics support
URHO3D_URHO2D:BOOL=ON

//Use console main() as entry point when setting up Windows executable
// targets (Windows platform only)
URHO3D_WIN32_CONSOLE:BOOL=OFF
[/code]

I'm building with Mingw32-w64 on Windows Vista

-------------------------

weitjong | 2017-01-02 01:04:38 UTC | #6

I have never tried to configure/generate the build tree using cmake-gui on Windows host system before. It is a long shot but can you check the "bin/tool" subdir in your build tree to see whether the PackageTool.exe is indeed being built successfully. And if so, try to execute it without any parameter. If it runs correctly then it should show the usage instruction. If it is not runnable then that is the problem causing RESOURCE_CHECK target to fail. Show the error message here if that is the case. If, however, the PackageTool.exe is not yet built then we have a bug on our hand here. If it is the latter case then you could try to workaround the problem first by calling 'make PackageTool' to ensure the tool is being built first then 'make RESOURCE_CHECK' then 'make all' in that order.

EDIT: At the moment our Urho3D cmake common module only setups rule to look for PackageTool.exe in the "bin/tool". It will not look for and use PackageTool_d.exe. So, that could be potentially the cause of your problem too.

-------------------------

Bluemoon | 2017-01-02 01:04:38 UTC | #7

I have the PackageTool built in the bin/tool folder and it runs well without parameters. But to build for RESOURCE_CHECK target fails

-------------------------

weitjong | 2017-01-02 01:04:38 UTC | #8

This is weird. If you have not, I guess the next thing to check is the generated build.make script for RESOURCE_CHECK to see why it fails. It would be easier if I could reproduce your problem locally, unfortunately I am not able to.

-------------------------

weitjong | 2017-01-02 01:04:38 UTC | #9

[quote="Sinoid"]Weird. MinGW - Windows 7 build works for me with the settings you posted. Note, I didn't use the cmake gui.

The only "issue" I run into is MinGW freaking out about a circular include path in SpritePacker that it resolves itself.

Does MinGW trigger cmake to update the tree for you? On my machines it doesn't, so I have to run the batch file every single time I change the config.[/quote]
Thanks for confirming that it works for you. At least now I know this is an isolated issue.

For me, the CMake is retriggered automatically whenever I change the config or any of the CMakeLists.txt. This is the case for all the host systems that I have worked with. The only time this is not done automatically is, when there are new source files being added in which case I would have to rerun the build script or the 'rake cmake' task manually.

-------------------------

Bluemoon | 2017-01-02 01:04:39 UTC | #10

its obvious that there is something I'm doing wrong  :confused: 
I will give it a decent try once more perhaps using the included build scripts

-------------------------

weitjong | 2017-01-02 01:04:39 UTC | #11

In theory it should not make any differences between cmake-gui or cmake CLI (either calling it directly or via one of our convenient build scripts). I would be very interested to see how your "Source/Tools/Urho3DPlayer/CMakeFiles/RESOURCE_CHECK.dir/build.make" is being generated in your build tree. In the previous post I have asked you to check the content of this file. The most important part is this section.
[code]Source/Tools/Urho3DPlayer/CMakeFiles/RESOURCE_CHECK: bin/tool/PackageTool.exe
	$(CMAKE_COMMAND) -E cmake_progress_report C:\Users\weitjong\SDKs\urho3d\mingw-Build\CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Checking and packaging resource directories"
	cd /d C:\Users\weitjong\SDKs\urho3d\mingw-Build\Source\Tools\Urho3DPlayer && "C:\Program Files (x86)\CMake\bin\cmake.exe" -E touch C:/Users/weitjong/SDKs/urho3d/Urho3D/bin/CoreData && echo Packaging C:/Users/weitjong/SDKs/urho3d/Urho3D/bin/CoreData... && C:/Users/weitjong/SDKs/urho3d/mingw-Build/bin/tool/PackageTool.exe C:/Users/weitjong/SDKs/urho3d/Urho3D/bin/CoreData C:/Users/weitjong/SDKs/urho3d/mingw-Build/bin/CoreData.pak.new -c -q && "C:/Program Files (x86)/CMake/bin/cmake.exe" -E copy_if_different C:/Users/weitjong/SDKs/urho3d/mingw-Build/bin/CoreData.pak.new C:/Users/weitjong/SDKs/urho3d/mingw-Build/bin/CoreData.pak && "C:/Program Files (x86)/CMake/bin/cmake.exe" -E remove C:/Users/weitjong/SDKs/urho3d/mingw-Build/bin/CoreData.pak.new
	cd /d C:\Users\weitjong\SDKs\urho3d\mingw-Build\Source\Tools\Urho3DPlayer && "C:\Program Files (x86)\CMake\bin\cmake.exe" -E touch C:/Users/weitjong/SDKs/urho3d/Urho3D/bin/Data && echo Packaging C:/Users/weitjong/SDKs/urho3d/Urho3D/bin/Data... && C:/Users/weitjong/SDKs/urho3d/mingw-Build/bin/tool/PackageTool.exe C:/Users/weitjong/SDKs/urho3d/Urho3D/bin/Data C:/Users/weitjong/SDKs/urho3d/mingw-Build/bin/Data.pak.new -c -q && "C:/Program Files (x86)/CMake/bin/cmake.exe" -E copy_if_different C:/Users/weitjong/SDKs/urho3d/mingw-Build/bin/Data.pak.new C:/Users/weitjong/SDKs/urho3d/mingw-Build/bin/Data.pak && "C:/Program Files (x86)/CMake/bin/cmake.exe" -E remove C:/Users/weitjong/SDKs/urho3d/mingw-Build/bin/Data.pak.new[/code]
Check for anything out of place in your version of the generated "build.make", like incorrect path or extra space in the path without double quotes, etc. In short even if you use one of the provided build scripts but with exactly the same "settings" that you have used before then you would most likely encounter the same problem again, barring the case if indeed it is a cmake-gui bug.

-------------------------

Bluemoon | 2017-01-02 01:04:41 UTC | #12

Below is the content of my "Source/Tools/Urho3DPlayer/CMakeFiles/RESOURCE_CHECK.dir/build.make"

[code]
# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = C:\CMAKE\bin\cmake.exe

# The command to remove a file.
RM = C:\CMAKE\bin\cmake.exe -E remove -f

# The program to use to edit the cache.
CMAKE_EDIT_COMMAND = C:\CMAKE\bin\cmake-gui.exe

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = C:\Urho3D_Master

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = C:\Urho3D_Master\Build

# Utility rule file for RESOURCE_CHECK.

# Include the progress variables for this target.
include Source/Tools/Urho3DPlayer/CMakeFiles/RESOURCE_CHECK.dir/progress.make

Source/Tools/Urho3DPlayer/CMakeFiles/RESOURCE_CHECK: bin/tool/PackageTool.exe
	$(CMAKE_COMMAND) -E cmake_progress_report C:\Urho3D_Master\Build\CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Checking and packaging resource directories"
	cd /d C:\Urho3D_Master\Build\Source\Tools\Urho3DPlayer && C:\CMAKE\bin\cmake.exe -E touch C:/Urho3D_Master/bin/CoreData && echo Packaging C:/Urho3D_Master/bin/CoreData... && C:/Urho3D_Master/Build/bin/tool/PackageTool C:/Urho3D_Master/bin/CoreData C:/Urho3D_Master/Build/bin/CoreData.pak.new -c -q && C:/CMAKE/bin/cmake.exe -E copy_if_different C:/Urho3D_Master/Build/bin/CoreData.pak.new C:/Urho3D_Master/Build/bin/CoreData.pak && C:/CMAKE/bin/cmake.exe -E remove C:/Urho3D_Master/Build/bin/CoreData.pak.new
	cd /d C:\Urho3D_Master\Build\Source\Tools\Urho3DPlayer && C:\CMAKE\bin\cmake.exe -E touch C:/Urho3D_Master/bin/Data && echo Packaging C:/Urho3D_Master/bin/Data... && C:/Urho3D_Master/Build/bin/tool/PackageTool C:/Urho3D_Master/bin/Data C:/Urho3D_Master/Build/bin/Data.pak.new -c -q && C:/CMAKE/bin/cmake.exe -E copy_if_different C:/Urho3D_Master/Build/bin/Data.pak.new C:/Urho3D_Master/Build/bin/Data.pak && C:/CMAKE/bin/cmake.exe -E remove C:/Urho3D_Master/Build/bin/Data.pak.new

RESOURCE_CHECK: Source/Tools/Urho3DPlayer/CMakeFiles/RESOURCE_CHECK
RESOURCE_CHECK: Source/Tools/Urho3DPlayer/CMakeFiles/RESOURCE_CHECK.dir/build.make
.PHONY : RESOURCE_CHECK

# Rule to build all files generated by this target.
Source/Tools/Urho3DPlayer/CMakeFiles/RESOURCE_CHECK.dir/build: RESOURCE_CHECK
.PHONY : Source/Tools/Urho3DPlayer/CMakeFiles/RESOURCE_CHECK.dir/build

Source/Tools/Urho3DPlayer/CMakeFiles/RESOURCE_CHECK.dir/clean:
	cd /d C:\Urho3D_Master\Build\Source\Tools\Urho3DPlayer && $(CMAKE_COMMAND) -P CMakeFiles\RESOURCE_CHECK.dir\cmake_clean.cmake
.PHONY : Source/Tools/Urho3DPlayer/CMakeFiles/RESOURCE_CHECK.dir/clean

Source/Tools/Urho3DPlayer/CMakeFiles/RESOURCE_CHECK.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" C:\Urho3D_Master C:\Urho3D_Master\Source\Tools\Urho3DPlayer C:\Urho3D_Master\Build C:\Urho3D_Master\Build\Source\Tools\Urho3DPlayer C:\Urho3D_Master\Build\Source\Tools\Urho3DPlayer\CMakeFiles\RESOURCE_CHECK.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : Source/Tools/Urho3DPlayer/CMakeFiles/RESOURCE_CHECK.dir/depend


[/code]

-------------------------

weitjong | 2017-01-02 01:04:41 UTC | #13

I only spotted one difference that may or may not be relevant to your issue. In your version the package tool is invoked without the .exe extension. I know in Windows command line you can invoke a binary without a .exe extension but I am not sure when it is inside a Makefile build rule.

I also noticed that your CMake version is quite old. I suggest you upgrade to the latest version first and probably your problem would go away. I have been using 3.1.1 on my Win7 VM. It appears that 3.2.1 has been out. I will upgrade to that version soon.

-------------------------

Bluemoon | 2017-01-02 01:04:42 UTC | #14

Wow.. to ever figure out that my cmake version could be the problem would have taken me age . Just got a newer version of cmake and the problem disappeared  :smiley: 

Thanks a million

-------------------------

