arunk | 2017-01-02 01:06:41 UTC | #1

I have downloaded the sources of the latest Urho3D 1.4 and I'm trying to run ./cmake_rpi.sh from the root of the source directory, but I get the following error:

cc1plus: error: bad value (cortex-a7) for -mcpu switch
CMake Error at CMake/Modules/Urho3D-CMake-common.cmake:662 (message):
  The configured compiler toolchain in the build tree is not able to handle
  all the compiler flags required to build the project.  Please kindly update
  your compiler toolchain to its latest version.  If you are using MinGW then
  make sure it is MinGW-W64 instead of MinGW-W32 or TDM-GCC (Code::Blocks
  default).  However, if you think there is something wrong with the compiler
  flags being used then please file a bug report to the project devs.
Call Stack (most recent call first):
  CMake/Modules/Urho3D-CMake-common.cmake:718 (enable_pch)
  CMake/Modules/Urho3D-CMake-common.cmake:774 (setup_target)
  Source/Urho3D/CMakeLists.txt:174 (setup_library)


-- Configuring incomplete, errors occurred!

Any help on what the issue might be? Searching for this error doesn't provide any helpful results. Thinking that cmake_rpi.sh was for cross-compile tools I tried running cmake_generic.sh but got the exact same error.

-------------------------

