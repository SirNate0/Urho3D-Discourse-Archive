amit | 2017-01-02 01:03:08 UTC | #1

Hi, i am tryin to build android on mac, but am not able to do so.

there is no cmake_android.sh in 1.32
i tried "./cmake_gcc.sh -DANDROID_NDK=/Users/xxxx/Desktop/dev/android/android-ndk-r10c/ -DURHO3D_SAMPLES=1"

but resulted in,


[code]Native build
================================================================================
-- Configuring done
-- Generating done
CMake Warning:
  Manually-specified variables were not used by the project:

    ANDROID_NDK


-- Build files have been written to: /Users/amit/Desktop/dev/urho/Urho3D-1.32/Build[/code]

any help?

i am usin 1.32

-------------------------

weitjong | 2017-01-02 01:03:10 UTC | #2

ANDROID_NDK is an environment variable, not a build option.

-------------------------

amit | 2017-01-02 01:03:10 UTC | #3

Thanks, it worked.

-------------------------

