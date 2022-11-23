Vivek | 2017-01-02 01:01:54 UTC | #1

I have window 7, and installed :
JDK8,
Android studio(for android SDK)
Android NDK r10d

and followed [urho3d.github.io/documentation/1 ... lding.html](http://urho3d.github.io/documentation/1.32/_building.html)

but i received quite of few errors, the output is as


c:\u3d>cmake_android.bat -DURHO3D_MKLINK=1
The system cannot find the path specified.
The system cannot find the path specified.

c:\u3d>cmake -E chdir android-Build cmake  -G "Unix Makefiles" -DCMAKE_TOOLCHAIN_FILE=..\Source\CMake\Toolchains\android
.toolchain.cmake -DLIBRARY_OUTPUT_PATH_ROOT=.  -DURHO3D_MKLINK=1 ..\Source
CMake Error: CMake was unable to find a build program corresponding to "Unix Makefiles".  CMAKE_MAKE_PROGRAM is not set.
  You probably need to select a different build tool.
CMake Error: Error required internal CMake variable not set, cmake may be not be built correctly.
Missing variable is:
CMAKE_C_COMPILER_ENV_VAR
CMake Error: Error required internal CMake variable not set, cmake may be not be built correctly.
Missing variable is:
CMAKE_C_COMPILER
CMake Error: Could not find cmake module file: C:/u3d/android-Build/CMakeFiles/3.1.0-rc2/CMakeCCompiler.cmake
CMake Error: Error required internal CMake variable not set, cmake may be not be built correctly.
Missing variable is:
CMAKE_CXX_COMPILER_ENV_VAR
CMake Error: Error required internal CMake variable not set, cmake may be not be built correctly.
Missing variable is:
CMAKE_CXX_COMPILER
CMake Error: Could not find cmake module file: C:/u3d/android-Build/CMakeFiles/3.1.0-rc2/CMakeCXXCompiler.cmake
-- Configuring incomplete, errors occurred!
CMake Error at CMakeLists.txt:2 (project):
  No CMAKE_C_COMPILER could be found.

  Tell CMake where to find the compiler by setting the CMake cache entry
  CMAKE_C_COMPILER to the full path to the compiler, or to the compiler name
  if it is in the PATH.


CMake Error at CMakeLists.txt:2 (project):
  No CMAKE_CXX_COMPILER could be found.

  Tell CMake where to find the compiler by setting the CMake cache entry
  CMAKE_CXX_COMPILER to the full path to the compiler, or to the compiler
  name if it is in the PATH.


CMake Error: CMAKE_C_COMPILER not set, after EnableLanguage
CMake Error: CMAKE_CXX_COMPILER not set, after EnableLanguage

c:\u3d>cd android-Build

c:\u3d\android-Build>android update project -p . -t 1
Updated project.properties
Updated local.properties
----------
build.xml: Failed to find version-tag string. File must be updated.
In order to not erase potential customizations, the file will not be automatically regenerated.
If no changes have been made to the file, delete it manually and run the command again.
If you have made customizations to the build process, the file must be manually updated.
It is recommended to:
        * Copy current file to a safe location.
        * Delete original file.
        * Run command again to generate a new file.
        * Port customizations to the new file, by looking at the new rules file
          located at <SDK>/tools/ant/build.xml
        * Update file to contain
              version-tag: custom
          to prevent file from being rewritten automatically by the SDK tools.
----------
Updated file C:\u3d\android-Build\proguard-project.txt

c:\u3d\android-Build>make -j4
'make' is not recognized as an internal or external command,
operable program or batch file.

c:\u3d\android-Build>

-------------------------

weitjong | 2017-01-02 01:01:54 UTC | #2

We haven't upgraded our Android/CMake toolchain to support NDK r10d yet.

-------------------------

weitjong | 2017-01-02 01:01:54 UTC | #3

It should be supported now in the master branch. However, I will wait until the first Android CI using that NDK r10d passed the test first.

EDIT: all is good.

-------------------------

