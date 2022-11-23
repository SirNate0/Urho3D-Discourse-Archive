practicing01 | 2017-01-02 01:07:39 UTC | #1

Hello, I downloaded the latest to test the animation controller fixes and native compiles fine but android is giving me: 

[code]
/home/practicing01/Desktop/Programming/Urho3D/Source/Urho3D/Engine/../Core/../Core/../Core/../Math/../Math/../Math/Quaternion.h:28:23: fatal error: emmintrin.h: No such file or directory
[/code]

-------------------------

TikariSakari | 2017-01-02 01:07:39 UTC | #2

I had this error, and since I didn't create new android build directory after updating the source to githubs head, I just disabled the URHO3D_SSE from the androids build-directorys configuration file: CMakeCache.txt. That at least let me build the android version again.

-------------------------

weitjong | 2017-01-02 01:07:40 UTC | #3

The URHO3D_SSE build option and compiler define were previously switch on mistakenly for Android build also, but since there was no actual C++ code that uses that compiler define before, everything built just fine, well until recently where we have a big contribution from Jukka that utilizes SSE SIMD instruction set. The issue with URHO3D_SSE mistakenly switch on on Android build has already been fixed in the latest master branch, however, you will have to either a) regenerate your Android build tree from scratch again or b) change the URHO3D_SSE & URHO3D_DEFAULT_SSE variables to false in the CMakeCache.txt found in your existing Android build tree (as already pointed out by TikariSakari) in order to have this build option properly switch off in your build.

-------------------------

