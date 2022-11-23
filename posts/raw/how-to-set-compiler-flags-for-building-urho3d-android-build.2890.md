projector | 2017-03-13 08:46:03 UTC | #1

I'm not familiar with Cmake, how do we set the compiler flags for building Urho3D or Urho3D android projects? I've tried modifying CMakeLists.txt by adding set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3") and add_definitions("-O3"), it does not seem to be working.

-------------------------

rku | 2017-03-13 08:55:14 UTC | #2

You can use `cmake_android.sh` or `cmake_android.bat` (main Urho3D folder). Or you can invoke command manually:

    cmake -DCMAKE_TOOLCHAIN_FILE=Urho3D/CMake/Toolchains/Android.cmake -DANDROID=1 -DANDROID_NATIVE_API_LEVEL=android-21 -DANDROID_ABI=armeabi

Make sure you have two environment variables pointing to android SDK and NDK:

    ANDROID_NDK=/path/to/android-ndk-r13b
    ANDROID_SDK=/path/to/android-sdk-linux

Now i do not remember for sure but `PATH` environment variable might need `/path/to/android-sdk-linux/platform-tools`.

More info in [docs](https://urho3d.github.io/documentation/1.6/_building.html#Building_Android).

-------------------------

projector | 2017-03-13 09:09:39 UTC | #3

Thank you for your response. Just to clarify, How if I want to set the compiler's level of optimisation(for exp, set to -O3)? could I just append -O3 at the end of the command?

-------------------------

rku | 2017-03-13 09:22:16 UTC | #4

You may use `-DCMAKE_BUILD_TYPE=Release` in case you want a release build. To set specific flags you should add `set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3")` (and maybe `set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -O3")` for C code) in appropriate place.

-------------------------

projector | 2017-03-14 01:38:40 UTC | #5

Thanks a lot for your help, it's very helpful. What is the default CPU optimization level for Release mode for Urho3D Android build?

-------------------------

weitjong | 2017-03-14 11:24:58 UTC | #6

Release build configuration uses -O3.

-------------------------

projector | 2017-03-15 14:42:20 UTC | #7

ok, thanks! If this is the case i just need to use "-DCMAKE_BUILD_TYPE=Release"

-------------------------

weitjong | 2017-03-15 15:36:01 UTC | #8

Actually Release is the default.

-------------------------

