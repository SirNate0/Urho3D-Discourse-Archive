gwald | 2017-01-02 01:11:40 UTC | #1

Android must be playing April fools on me  :confused: 
[url=http://discourse.urho3d.io/t/android-build-on-windowsxp-issues/1934/1]Installed with the same packages from winXP thread[/url]
Cmake, ndk, sdk, java, ant etc work from command line:

[code]

C:\Urho3D-master\build>android list
Available Android targets:
----------
id: 1 or "android-15"
     Name: Android 4.0.3
     Type: Platform
     API level: 15
     Revision: 5
     Skins: HVGA, QVGA, WQVGA400, WQVGA432, WSVGA, WVGA800 (default), WVGA854, W
XGA720, WXGA800
 Tag/ABIs : default/x86
----------
id: 2 or "Google Inc.:Google APIs:15"
     Name: Google APIs
     Type: Add-On
     Vendor: Google Inc.
     Revision: 3
     Description: Android + Google APIs
     Based on Android 4.0.3 (API level 15)
     Libraries:
      * com.android.future.usb.accessory (usb.jar)
          API for USB Accessories
      * com.google.android.media.effects (effects.jar)
          Collection of video effects
      * com.google.android.maps (maps.jar)
          API for Google Maps
     Skins: HVGA, QVGA, WQVGA400, WQVGA432, WSVGA, WVGA800 (default), WVGA854, W
XGA720, WXGA800
 Tag/ABIs : default/armeabi-v7a
Available Android Virtual Devices:
Available devices definitions:
id: 0 or "tv_1080p"
    Name: Android TV (1080p)
    OEM : Google
    Tag : android-tv
---------
[/code]

I've tried with 1.5 and master on github and both compile and links until: 

[code]
[ 0%]....
...
..
.
[ 54%] Building CXX object Source/ThirdParty/Bullet/CMakeFiles/Bullet.dir/src/Li
nearMath/btVector3.cpp.o
[ 54%] Linking CXX static library libBullet.a
[ 54%] Built target Bullet
Scanning dependencies of target tolua++
[ 54%] Creating directories for 'tolua++'
[ 54%] No download step for 'tolua++'
[ 55%] No patch step for 'tolua++'
[ 55%] No update step for 'tolua++'
[ 55%] Performing configure step for 'tolua++'
-- The C compiler identification is unknown
-- The CXX compiler identification is unknown
CMake Error at CMakeLists.txt:45 (project):
  No CMAKE_C_COMPILER could be found.

  Tell CMake where to find the compiler by setting either the environment
  variable "CC" or the CMake cache entry CMAKE_C_COMPILER to the full path to
  the compiler, or to the compiler name if it is in the PATH.


CMake Error at CMakeLists.txt:45 (project):
  No CMAKE_CXX_COMPILER could be found.

  Tell CMake where to find the compiler by setting either the environment
  variable "CXX" or the CMake cache entry CMAKE_CXX_COMPILER to the full path
  to the compiler, or to the compiler name if it is in the PATH.


-- Configuring incomplete, errors occurred!
See also "C:/Urho3D-master/build/Source/Urho3D/tolua++-prefix/src/tolua++-build/
CMakeFiles/CMakeOutput.log".
See also "C:/Urho3D-master/build/Source/Urho3D/tolua++-prefix/src/tolua++-build/
CMakeFiles/CMakeError.log".
make[2]: *** [Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-configure]
Error 1
make[1]: *** [Source/Urho3D/CMakeFiles/tolua++.dir/all] Error 2
make: *** [all] Error 2

C:\Urho3D-master\build>
[/code]

[code]
Compiling the C compiler identification source file "CMakeCCompilerId.c" failed.
Compiler: CMAKE_C_COMPILER-NOTFOUND 
Build flags: 
Id flags: 

The output was:
The system cannot find the file specified


Compiling the C compiler identification source file "CMakeCCompilerId.c" failed.
Compiler: CMAKE_C_COMPILER-NOTFOUND 
Build flags: 
Id flags: -c

The output was:
The system cannot find the file specified


Compiling the C compiler identification source file "CMakeCCompilerId.c" failed.
Compiler: CMAKE_C_COMPILER-NOTFOUND 
Build flags: 
Id flags: -Aa

The output was:
The system cannot find the file specified


Compiling the CXX compiler identification source file "CMakeCXXCompilerId.cpp" failed.
Compiler: CMAKE_CXX_COMPILER-NOTFOUND 
Build flags: 
Id flags: 

The output was:
The system cannot find the file specified


Compiling the CXX compiler identification source file "CMakeCXXCompilerId.cpp" failed.
Compiler: CMAKE_CXX_COMPILER-NOTFOUND 
Build flags: 
Id flags: -c

The output was:
The system cannot find the file specified

[/code]

[code]

#=============================================================================
# Target rules for targets named Bullet

# Build rule for target.
Bullet: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 Bullet
.PHONY : Bullet

# fast build rule for target.
Bullet/fast:
	$(MAKE) -f Source/ThirdParty/Bullet/CMakeFiles/Bullet.dir/build.make Source/ThirdParty/Bullet/CMakeFiles/Bullet.dir/build
.PHONY : Bullet/fast

#=============================================================================
# Target rules for targets named tolua++

# Build rule for target.
tolua++: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 tolua++
.PHONY : tolua++

# fast build rule for target.
tolua++/fast:
	$(MAKE) -f Source/Urho3D/CMakeFiles/tolua++.dir/build.make Source/Urho3D/CMakeFiles/tolua++.dir/build
.PHONY : tolua++/fast

#=============================================================================
# Target rules for targets named Urho3D

[/code]


 make -f Source/Urho3D/CMakeFiles/tolua++.dir/build.make Source/Urho3D/CMakeFiles/tolua++.dir/build

Source/Urho3D/CMakeFiles/tolua++.dir/build.make:
[code]# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


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

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = C:/CMake/bin/cmake.exe

# The command to remove a file.
RM = C:/CMake/bin/cmake.exe -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = C:/Urho3D-master

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = C:/Urho3D-master/build

# Utility rule file for tolua++.

# Include the progress variables for this target.
include Source/Urho3D/CMakeFiles/tolua++.dir/progress.make

Source/Urho3D/CMakeFiles/tolua++: Source/Urho3D/CMakeFiles/tolua++-complete


Source/Urho3D/CMakeFiles/tolua++-complete: Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-install
Source/Urho3D/CMakeFiles/tolua++-complete: Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-mkdir
Source/Urho3D/CMakeFiles/tolua++-complete: Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-download
Source/Urho3D/CMakeFiles/tolua++-complete: Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-update
Source/Urho3D/CMakeFiles/tolua++-complete: Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-patch
Source/Urho3D/CMakeFiles/tolua++-complete: Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-configure
Source/Urho3D/CMakeFiles/tolua++-complete: Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-build
Source/Urho3D/CMakeFiles/tolua++-complete: Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-install
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=C:/Urho3D-master/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Completed 'tolua++'"
	cd C:/Urho3D-master/build/Source/Urho3D && C:/CMake/bin/cmake.exe -E make_directory C:/Urho3D-master/build/Source/Urho3D/CMakeFiles
	cd C:/Urho3D-master/build/Source/Urho3D && C:/CMake/bin/cmake.exe -E touch C:/Urho3D-master/build/Source/Urho3D/CMakeFiles/tolua++-complete
	cd C:/Urho3D-master/build/Source/Urho3D && C:/CMake/bin/cmake.exe -E touch C:/Urho3D-master/build/Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-done

Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-install: Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-build
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=C:/Urho3D-master/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Performing install step for 'tolua++'"
	cd C:/Urho3D-master/build/Source/Urho3D/tolua++-prefix/src/tolua++-build && $(MAKE) install
	cd C:/Urho3D-master/build/Source/Urho3D/tolua++-prefix/src/tolua++-build && C:/CMake/bin/cmake.exe -E touch C:/Urho3D-master/build/Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-install

Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-mkdir:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=C:/Urho3D-master/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Creating directories for 'tolua++'"
	cd C:/Urho3D-master/build/Source/Urho3D && C:/CMake/bin/cmake.exe -E make_directory C:/Urho3D-master/Source/ThirdParty/toluapp/src/bin
	cd C:/Urho3D-master/build/Source/Urho3D && C:/CMake/bin/cmake.exe -E make_directory C:/Urho3D-master/build/Source/Urho3D/tolua++-prefix/src/tolua++-build
	cd C:/Urho3D-master/build/Source/Urho3D && C:/CMake/bin/cmake.exe -E make_directory C:/Urho3D-master/build/Source/Urho3D/tolua++-prefix
	cd C:/Urho3D-master/build/Source/Urho3D && C:/CMake/bin/cmake.exe -E make_directory C:/Urho3D-master/build/Source/Urho3D/tolua++-prefix/tmp
	cd C:/Urho3D-master/build/Source/Urho3D && C:/CMake/bin/cmake.exe -E make_directory C:/Urho3D-master/build/Source/Urho3D/tolua++-prefix/src/tolua++-stamp
	cd C:/Urho3D-master/build/Source/Urho3D && C:/CMake/bin/cmake.exe -E make_directory C:/Urho3D-master/build/Source/Urho3D/tolua++-prefix/src
	cd C:/Urho3D-master/build/Source/Urho3D && C:/CMake/bin/cmake.exe -E touch C:/Urho3D-master/build/Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-mkdir

Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-download: Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-mkdir
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=C:/Urho3D-master/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "No download step for 'tolua++'"
	cd C:/Urho3D-master/build/Source/Urho3D && C:/CMake/bin/cmake.exe -E echo_append
	cd C:/Urho3D-master/build/Source/Urho3D && C:/CMake/bin/cmake.exe -E touch C:/Urho3D-master/build/Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-download

Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-update: Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-download
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=C:/Urho3D-master/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "No update step for 'tolua++'"
	cd C:/Urho3D-master/build/Source/Urho3D && C:/CMake/bin/cmake.exe -E echo_append
	cd C:/Urho3D-master/build/Source/Urho3D && C:/CMake/bin/cmake.exe -E touch C:/Urho3D-master/build/Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-update

Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-patch: Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-download
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=C:/Urho3D-master/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "No patch step for 'tolua++'"
	cd C:/Urho3D-master/build/Source/Urho3D && C:/CMake/bin/cmake.exe -E echo_append
	cd C:/Urho3D-master/build/Source/Urho3D && C:/CMake/bin/cmake.exe -E touch C:/Urho3D-master/build/Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-patch

Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-configure: Source/Urho3D/tolua++-prefix/tmp/tolua++-cfgcmd.txt
Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-configure: Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-update
Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-configure: Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-patch
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=C:/Urho3D-master/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Performing configure step for 'tolua++'"
	cd C:/Urho3D-master/build/Source/Urho3D/tolua++-prefix/src/tolua++-build && C:/CMake/bin/cmake.exe -DDEST_RUNTIME_DIR=C:/Urho3D-master/build/bin/tool -DBAKED_CMAKE_SOURCE_DIR=C:/Urho3D-master -DURHO3D_UPDATE_SOURCE_TREE=OFF "-GUnix Makefiles" C:/Urho3D-master/Source/ThirdParty/toluapp/src/bin
	cd C:/Urho3D-master/build/Source/Urho3D/tolua++-prefix/src/tolua++-build && C:/CMake/bin/cmake.exe -E touch C:/Urho3D-master/build/Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-configure

Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-build: Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-configure
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=C:/Urho3D-master/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_8) "Performing build step for 'tolua++'"
	cd C:/Urho3D-master/build/Source/Urho3D/tolua++-prefix/src/tolua++-build && $(MAKE)
	cd C:/Urho3D-master/build/Source/Urho3D/tolua++-prefix/src/tolua++-build && C:/CMake/bin/cmake.exe -E touch C:/Urho3D-master/build/Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-build

tolua++: Source/Urho3D/CMakeFiles/tolua++
tolua++: Source/Urho3D/CMakeFiles/tolua++-complete
tolua++: Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-install
tolua++: Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-mkdir
tolua++: Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-download
tolua++: Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-update
tolua++: Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-patch
tolua++: Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-configure
tolua++: Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-build
tolua++: Source/Urho3D/CMakeFiles/tolua++.dir/build.make

.PHONY : tolua++

# Rule to build all files generated by this target.
Source/Urho3D/CMakeFiles/tolua++.dir/build: tolua++

.PHONY : Source/Urho3D/CMakeFiles/tolua++.dir/build

Source/Urho3D/CMakeFiles/tolua++.dir/clean:
	cd C:/Urho3D-master/build/Source/Urho3D && $(CMAKE_COMMAND) -P CMakeFiles/tolua++.dir/cmake_clean.cmake
.PHONY : Source/Urho3D/CMakeFiles/tolua++.dir/clean

Source/Urho3D/CMakeFiles/tolua++.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" C:/Urho3D-master C:/Urho3D-master/Source/Urho3D C:/Urho3D-master/build C:/Urho3D-master/build/Source/Urho3D C:/Urho3D-master/build/Source/Urho3D/CMakeFiles/tolua++.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : Source/Urho3D/CMakeFiles/tolua++.dir/depend

[/code]

-------------------------

weitjong | 2017-01-02 01:11:40 UTC | #2

But this time you have just hit a common pitfall for Android build on Windows host. This issue has been asked a few times. Basically our build system builds the host tool(s) that it needs on the fly. The host tool building requires native compiler. In other words, your build tree needs two compiler toolchain: 1) Android NDK for target platform and 2) native compiler (usually we use MinGW here) for host platform. CMake must be able to see them both, i.e. they must be in the system PATH environment variables. You can quickly avoid this problem by turning off URHO3D_LUA build option, I think.

-------------------------

gwald | 2017-01-02 01:11:40 UTC | #3

Wow, thanks heaps man!
I was just going through makefiles.. 
There was no mention of this on the [url=http://urho3d.github.io/documentation/1.31/_building.html]build page[/url].

-------------------------

weitjong | 2017-01-02 01:11:40 UTC | #4

Although we have constantly updating our online documentation, some time we may have overlooked some places that we need to change. The Android build process section is slightly out-dated with our current build system now. The page was made when our build system still has not learnt how to build host tools on the fly and also at that time Lua has not come into picture yet, but now we even build Lua by default. Contribution is welcome to update the page, of course.

-------------------------

gwald | 2017-01-02 01:11:40 UTC | #5

Turning off URHO3D_LUA, didn't work, installing fixed it tdm-gcc-5.1.0-3 fixed it.
Ah cool, I can do an android guide.. maybe it can be added to the wiki
Thanks again!

-------------------------

gwald | 2017-01-02 01:11:41 UTC | #6

[quote="weitjong"]But this time you have just hit a common pitfall for Android build on Windows host. This issue has been asked a few times. Basically our build system builds the host tool(s) that it needs on the fly. [/quote]

FYI, I've tried searching android on the forum search but you can't, it must be blocked from search?:
[quote]The following words in your search query were ignored because they are too common words: android.
[/quote]

-------------------------

