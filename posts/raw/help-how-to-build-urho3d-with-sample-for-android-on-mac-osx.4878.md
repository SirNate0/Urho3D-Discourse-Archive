majhong | 2019-01-29 08:09:38 UTC | #1

i use cmake with gui, it can not find a toolchain!

the flow is my step.
step1:
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/9/9741d856e24203ac52662fb2aa9a97a4fb5107a2.jpeg'>
step2:
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/3/35a64fc15fcadc083c9522621d0596fead92c8be.jpeg'>
step3: find path
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/1/17938cc5efd61e03f4fe814b3f11b90f20c5ba09.jpeg'>

-------------------------

majhong | 2019-01-29 03:54:52 UTC | #2

I switch ANDROID_TOOLCHAIN_NAME from arm-linux-androideabi-clang  to  arm-linux-androideabi-4.9 
set path :   xxxxxx/toolchains/arm-linux-androideabi-4.9/prebuilt/darwin-x86_64/bin
xxxxxx is my ndk path!

the error is the same !

-------------------------

weitjong | 2019-01-29 04:39:14 UTC | #3

We have already migrated our Android build system to use Gradle in master branch. If you want to use release 1.7 tag then you have to use an old version of Android build tool. Search the forum for old threads with that subject.

-------------------------

majhong | 2019-01-29 06:12:22 UTC | #4

I get another error when i switch gradle .

step1: download  master branch (https://github.com/urho3d/Urho3D.git)

step2:  ./gradlew build

step3: error -->

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/9/96b400a2b12c8365c44d68dfdc62c076d0e7402b.jpeg'>

add --stacktrace
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/4/469cd4acbeffb450b4d0d78a8ccd4b55e8ef4f69.jpeg'>

-------------------------

weitjong | 2019-01-29 06:30:39 UTC | #5

The error is already clearly stated. Read the HEAD version of the online doc for Android build.

-------------------------

majhong | 2019-01-29 08:08:57 UTC | #6

sorry! i am a newer of android studio.

i got a new error 

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':android:urho3d-lib:generateJsonModelDebug'.
> Build command failed.
  Error while executing process /Users/leeco/Library/Android/sdk/cmake/3.6.4111459/bin/cmake with arguments {-H/Users/leeco/game_dev/Urho3D-master -B/Users/leeco/game_dev/Urho3D-master/android/urho3d-lib/.externalNativeBuild/cmake/debug/armeabi-v7a -DANDROID_ABI=armeabi-v7a -DANDROID_PLATFORM=android-17 -DCMAKE_LIBRARY_OUTPUT_DIRECTORY=/Users/leeco/game_dev/Urho3D-master/android/urho3d-lib/build/intermediates/cmake/debug/obj/armeabi-v7a -DCMAKE_BUILD_TYPE=Debug -DANDROID_NDK=/Users/leeco/Library/Android/sdk/ndk-bundle -DCMAKE_TOOLCHAIN_FILE=/Users/leeco/Library/Android/sdk/ndk-bundle/build/cmake/android.toolchain.cmake -DCMAKE_MAKE_PROGRAM=/Users/leeco/Library/Android/sdk/cmake/3.6.4111459/bin/ninja -GAndroid Gradle - Ninja -DANDROID_CCACHE=/usr/local/opt/ccache/libexec -DGRADLE_BUILD_DIR=/Users/leeco/game_dev/Urho3D-master/android/urho3d-lib/build -DURHO3D_PLAYER=0 -DURHO3D_SAMPLES=0}
  -- Check for working C compiler: /Users/leeco/Library/Android/sdk/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/clang
  -- Check for working C compiler: /Users/leeco/Library/Android/sdk/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/clang -- broken
  CMake Error at /Users/leeco/Library/Android/sdk/cmake/3.6.4111459/share/cmake-3.6/Modules/CMakeTestCCompiler.cmake:61 (message):
    The C compiler
    "/Users/leeco/Library/Android/sdk/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/clang"
    is not able to compile a simple test program.

    It fails with the following output:

     Change Dir: /Users/leeco/game_dev/Urho3D-master/android/urho3d-lib/.externalNativeBuild/cmake/debug/armeabi-v7a/CMakeFiles/CMakeTmp

-------------------------

weitjong | 2019-01-30 01:45:01 UTC | #7

In this case you will probably need to start slow by following getting started guide from Android Developer website. You probably want to retry the build from scratch again. Remove the build tree and all the hidden dirs generated by Android plugin for Gradle.

-------------------------

majhong | 2019-01-29 10:37:38 UTC | #8

i got this error!

Users/leeco/game_dev/Urho3D-master/Source/ThirdParty/SDL/src/cpuinfo/SDL_cpuinfo.c:47:10: fatal error: 'sys/sysctl.h' file not found
#include <sys/sysctl.h>
         ^~~~~~~~~~~~~~
1 error generated.
ninja: build stopped: subcommand failed.

-------------------------

weitjong | 2019-01-29 12:34:23 UTC | #9

Which version of the Android build tool are you using? These are the one we use in our CI build via docker.

```
ARG tool_url=https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip
ARG tool_version=27.0.3
ARG cmake_version=3.6.4111459
```

Although the CI uses Linux host and not macOS, the Android build is really a cross-compiling build. So which host machine you use should not be relevant, well except for Windows host.

-------------------------

majhong | 2019-01-29 14:05:29 UTC | #11

i downloaded a new master-branch 
i got a new error this time.
(first build)


In file included from /Users/leeco/game_dev/Model/Urho3D-master/Source/ThirdParty/Bullet/src/BulletCollision/BroadphaseCollision/btQuantizedBvh.h:31:
../../../../../../Source/ThirdParty/Bullet/src/LinearMath/btVector3.h:343:7: error: argument value 10880 is outside the valid range [0, 255] [-Wargument-outside-range]
                y = bt_splat_ps(y, 0x80);
                    ^~~~~~~~~~~~~~~~~~~~
../../../../../../Source/ThirdParty/Bullet/src/LinearMath/btVector3.h:47:32: note: expanded from macro 'bt_splat_ps'
#define bt_splat_ps( _a, _i )  bt_pshufd_ps((_a), BT_SHUFFLE(_i,_i,_i,_i) )
                               ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
../../../../../../Source/ThirdParty/Bullet/src/LinearMath/btVector3.h:45:35: note: expanded from macro 'bt_pshufd_ps'
#define bt_pshufd_ps( _a, _mask ) _mm_shuffle_ps((_a), (_a), (_mask) )
                                  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/Users/leeco/Library/Android/sdk/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/lib64/clang/8.0.2/include/xmmintrin.h:2608:11: note: expanded from macro '_mm_shuffle_ps'
  (__m128)__builtin_ia32_shufps((__v4sf)(__m128)(a), (__v4sf)(__m128)(b), \
          ^
In file included from /Users/leeco/game_dev/Model/Urho3D-master/Source/ThirdParty/Bullet/src/BulletCollision/BroadphaseCollision/btQuantizedBvh.cpp:18:
In file included from ../../../../../../Source/ThirdParty/Bullet/src/LinearMath/btAabbUtil2.h:20:
In file included from ../../../../../../Source/ThirdParty/Bullet/src/LinearMath/btTransform.h:21:
../../../../../../Source/ThirdParty/Bullet/src/LinearMath/btMatrix3x3.h:882:17: error: argument value 10880 is outside the valid range [0, 255] [-Wargument-outside-range]
    __m128 vk = bt_splat_ps(_mm_load_ss((float *)&k), 0x80);
                ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
../../../../../../Source/ThirdParty/Bullet/src/LinearMath/btVector3.h:47:32: note: expanded from macro 'bt_splat_ps'
#define bt_splat_ps( _a, _i )  bt_pshufd_ps((_a), BT_SHUFFLE(_i,_i,_i,_i) )
                               ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
../../../../../../Source/ThirdParty/Bullet/src/LinearMath/btVector3.h:45:35: note: expanded from macro 'bt_pshufd_ps'
#define bt_pshufd_ps( _a, _mask ) _mm_shuffle_ps((_a), (_a), (_mask) )
                                  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/Users/leeco/Library/Android/sdk/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/lib64/clang/8.0.2/include/xmmintrin.h:2608:11: note: expanded from macro '_mm_shuffle_ps'
  (__m128)__builtin_ia32_shufps((__v4sf)(__m128)(a), (__v4sf)(__m128)(b), \
          ^
2 errors generated.


sorry, i use gradlew firstly.

-------------------------

weitjong | 2019-01-29 15:10:39 UTC | #12

Like I said previously, you probably would want to learn the basic first before trying to build Urho3D engine. Although we have done everything possible to make it build out of the box, it still requires certain level of competency (and luck) to get it done.

One thing I notice about your reported "compilation error" is that they change from one attempt to another. You last error is unexplainable too. There is no "10880" magic constant used anywhere in our code. So, probably you were just seeing things. Perhaps it was caused by insufficient memory to build all the Android ABI in one go, I really don't know. However, you can try one thing. Try build one single ABI at a time, like so: `./gradlew -PANDROID_ABI=armeabi-v7a clean build`.

Good luck.

-------------------------

majhong | 2019-02-11 03:19:37 UTC | #13

thank you weitjong !
it worked on armeabi-v7a ,it is enought for me 

i have a litter time for compiling a android demo .(my game has already run on mac osx,but i need illustrate it on a android mobilephone)

the urho3d is one of the best game engine for c/c++ programer,Thank you for your contribution！

-------------------------

majhong | 2019-01-30 09:54:08 UTC | #14

My  suggestion for compilation：
splite it into two apart
one is cmake build for c/c++ (product  .a  and .so)
the other is a android stuido project for build a apk (it is a loader only)
in this way, it a flexible solution for both c/c++ and java/kotlin

i want only a game and i don't need all of them( java/kotlin/gradlew/androidstuido.....)

-------------------------

weitjong | 2019-02-11 03:19:37 UTC | #15

You still think in term of old Android build using CMake and Ant. The Gradle build with google provided Android plugin internally actually does just that, but all nicely wrapped into a “build” task. There are other tasks available too. You have seen “clean” task in action above, just to name another example. So, I don’t know what else needs to be improved.

-------------------------

fnadalt | 2019-03-23 00:55:59 UTC | #16

I had the same error when compiling for x86 and the solution I found was to add -Wno-argument-outside-range in UrhoCommon.cmake:

495: elseif (CMAKE_CXX_COMPILER_ID MATCHES Clang)
496:    set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wno-argument-outside-range")

Compiled fine.

-------------------------

weitjong | 2019-03-23 02:07:24 UTC | #17

At one time I had carefully aligned all our compiler flags for our Android build to follow as close as possible the flags being set when using the Android ndk-build approach, but it has been a while now and I don't know if anything has changed after that. Having said that, currently our Android-CI builds for all the ABIs (including the x86) are tested to go well without the extra compiler flag you mentioned above. I already explained that since Android-build itself is a cross-compiling build, it makes no difference to perform the build on any *nix host machine (including Mac OSX).

-------------------------
