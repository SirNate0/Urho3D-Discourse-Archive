hsl9999 | 2017-01-02 01:05:23 UTC | #1

env:
win7 64
cmake 3.2.2
urho3d 1.4
mingw  x86_64-4.9.2-posix-seh-rt_v4-rev2
emsdk-1.30.0-portable-64bit 
    run:
    # Fetch the latest registry of available tools.
    ./emsdk update
    # Download and install the latest SDK tools.
    ./emsdk install latest
    # Make the "latest" SDK "active"
    ./emsdk activate latest
    emsdk_env.bat

error:
CMake Error at CMake/Toolchains/emscripten.toolchain.cmake:50 (message):
  Could not determine the emcc version.  Make sure you have installed and
  activated the Emscripten SDK correctly.

-------------------------

weitjong | 2017-01-02 01:05:23 UTC | #2

Welcome to our forum.

The bug has just been fixed in the master branch. Unfortunately our Emscripten CI build is only done on Linux host system (used to be on Mac OS X host system), so this issue on Windows host system was undetected earlier.

-------------------------

