johnnycable | 2017-03-22 10:29:09 UTC | #1

I'm trying to deploy Urho for Android by using a modern, Android Studio, latest Cmake toolchain.
To be more clear, I want to support a process decoupling the upstream Urho3d library from the downstream app building.
As of now, the android build only support building "one-way", that is upstream. If I use the same build on the downstream app, I end up having an upstream library rebuild in the downstream app directory, and that's not what I want. I want a modern, decoupled, lightweight (possibly) command line building process, much in the so fashionable CI style which is current today... :wink:
More, I want it to run flawlessly in both Android Studio and gradle wrapper. Please no rake / cmake cube-enter-the-build-line-fix-it-again, I've already tried them all in all possible combination, there's no way to make them work good, or at least I'm unable.
As of now, I've create the cmd line utils, built the general downstream structure, and created a new Cmakefiles.txt for android studio 2.3 to work. After some troubling, Cmake appears to work generally, but maybe there's something missing, something that's inside the inner build process / android toolchain, because when I run gradlew assembleDebug i get a **mmintrin** related error as follows:


> FAILURE: Build failed with an exception.

> * What went wrong:
> Execution failed for task ':app:externalNativeBuildDebug'.
> > Build command failed.
>   Error while executing process /usr/local/android/cmake/3.6.3155560/bin/cmake with arguments {--build /Users/max/Developer/Stage/Workspace/AndroidStudio/MyApplication12/app/.externalNativeBuild/cmake/debug/armeabi-v7a --target native-lib}
>   [1/2] Building CXX object CMakeFiles/native-lib.dir/Users/max/Developer/Stage/Workspace/Urho/prima/src/prima.cpp.o
>   FAILED: /usr/local/android/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/clang++  -target armv7-none-linux-androideabi -gcc-toolchain /usr/local/android/ndk-bundle/toolchains/arm-linux-androideabi-4.9/prebuilt/darwin-x86_64 --sysroot=/usr/local/android/ndk-bundle/platforms/android-9/arch-arm  -Dnative_lib_EXPORTS -I/usr/local/Urho/Urho3D-1.6/build/android/Debug/include -isystem /usr/local/android/ndk-bundle/sources/cxx-stl/gnu-libstdc++/4.9/include -isystem /usr/local/android/ndk-bundle/sources/cxx-stl/gnu-libstdc++/4.9/libs/armeabi-v7a/include -isystem /usr/local/android/ndk-bundle/sources/cxx-stl/gnu-libstdc++/4.9/include/backward -g -DANDROID -ffunction-sections -funwind-tables -fstack-protector-strong -no-canonical-prefixes -march=armv7-a -mfloat-abi=softfp -mfpu=vfpv3-d16 -fno-integrated-as -mthumb -Wa,--noexecstack -Wformat -Werror=format-security -fno-exceptions -fno-rtti -g -DANDROID -ffunction-sections -funwind-tables -fstack-protector-strong -no-canonical-prefixes -march=armv7-a -mfloat-abi=softfp -mfpu=vfpv3-d16 -fno-integrated-as -mthumb -Wa,--noexecstack -Wformat -Werror=format-security -fno-exceptions -fno-rtti  -O0 -fno-limit-debug-info -O0 -fno-limit-debug-info  -fPIC -MD -MT CMakeFiles/native-lib.dir/Users/max/Developer/Stage/Workspace/Urho/prima/src/prima.cpp.o -MF CMakeFiles/native-lib.dir/Users/max/Developer/Stage/Workspace/Urho/prima/src/prima.cpp.o.d -o CMakeFiles/native-lib.dir/Users/max/Developer/Stage/Workspace/Urho/prima/src/prima.cpp.o -c /Users/max/Developer/Stage/Workspace/Urho/prima/src/prima.cpp
>   In file included from /Users/max/Developer/Stage/Workspace/Urho/prima/src/prima.cpp:8:
>   In file included from /usr/local/Urho/Urho3D-1.6/build/android/Debug/include/Urho3D/Core/CoreEvents.h:25:
>   In file included from /usr/local/Urho/Urho3D-1.6/build/android/Debug/include/Urho3D/Core/../Core/Object.h:26:
>   In file included from /usr/local/Urho/Urho3D-1.6/build/android/Debug/include/Urho3D/Core/../Core/Variant.h:29:
>   In file included from /usr/local/Urho/Urho3D-1.6/build/android/Debug/include/Urho3D/Core/../Math/Matrix3x4.h:25:
>   In file included from /usr/local/Urho/Urho3D-1.6/build/android/Debug/include/Urho3D/Core/../Math/../Math/Matrix4.h:25:
>   In file included from /usr/local/Urho/Urho3D-1.6/build/android/Debug/include/Urho3D/Core/../Math/../Math/Quaternion.h:28:
>   In file included from /usr/local/android/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/../lib64/clang/3.8.256229/include/emmintrin.h:27:
>   In file included from /usr/local/android/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/../lib64/clang/3.8.256229/include/xmmintrin.h:27:
>   /usr/local/android/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/../lib64/clang/3.8.256229/include/mmintrin.h:39:5: error: use of undeclared identifier '__builtin_ia32_emms'; did you mean '__builtin_isless'?
>       __builtin_ia32_emms();
>       ^
>   /usr/local/android/ndk-bundle/sources/cxx-stl/gnu-libstdc++/4.9/include/cmath:885:14: note: '__builtin_isless' declared here
>         return __builtin_isless(__type(__f1), __type(__f2));
>                ^
>   In file included from /Users/max/Developer/Stage/Workspace/Urho/prima/src/prima.cpp:8:
>   In file included from /usr/local/Urho/Urho3D-1.6/build/android/Debug/include/Urho3D/Core/CoreEvents.h:25:
>   In file included from /usr/local/Urho/Urho3D-1.6/build/android/Debug/include/Urho3D/Core/../Core/Object.h:26:
>   In file included from /usr/local/Urho/Urho3D-1.6/build/android/Debug/include/Urho3D/Core/../Core/Variant.h:29:
>   In file included from /usr/local/Urho/Urho3D-1.6/build/android/Debug/include/Urho3D/Core/../Math/Matrix3x4.h:25:
>   In file included from /usr/local/Urho/Urho3D-1.6/build/android/Debug/include/Urho3D/Core/../Math/../Math/Matrix4.h:25:
>   In file included from /usr/local/Urho/Urho3D-1.6/build/android/Debug/include/Urho3D/Core/../Math/../Math/Quaternion.h:28:
>   In file included from /usr/local/android/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/../lib64/clang/3.8.256229/include/emmintrin.h:27:
>   In file included from /usr/local/android/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/../lib64/clang/3.8.256229/include/xmmintrin.h:27:
>   /usr/local/android/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/../lib64/clang/3.8.256229/include/mmintrin.h:39:25: error: too few arguments to function call, expected 2, have 0
>       __builtin_ia32_emms();
>                           ^
>   /usr/local/android/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/../lib64/clang/3.8.256229/include/mmintrin.h:45:19: error: use of undeclared identifier '__builtin_ia32_vec_init_v2si'
>       return (__m64)__builtin_ia32_vec_init_v2si(__i, 0);
>                     ^
>   /usr/local/android/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/../lib64/clang/3.8.256229/include/mmintrin.h:51:12: error: use of undeclared identifier '__builtin_ia32_vec_ext_v2si'
>       return __builtin_ia32_vec_ext_v2si((__v2si)__m, 0);
>              ^
>   /usr/local/android/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/../lib64/clang/3.8.256229/include/mmintrin.h:69:19: error: use of undeclared identifier '__builtin_ia32_packsswb'
>       return (__m64)__builtin_ia32_packsswb((__v4hi)__m1, (__v4hi)__m2);
>                     ^
>   /usr/local/android/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/../lib64/clang/3.8.256229/include/mmintrin.h:75:19: error: use of undeclared identifier '__builtin_ia32_packssdw'
>       return (__m64)__builtin_ia32_packssdw((__v2si)__m1, (__v2si)__m2);
>                     ^
>   /usr/local/android/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/../lib64/clang/3.8.256229/include/mmintrin.h:81:19: error: use of undeclared identifier '__builtin_ia32_packuswb'
>       return (__m64)__builtin_ia32_packuswb((__v4hi)__m1, (__v4hi)__m2);
>                     ^
>   /usr/local/android/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/../lib64/clang/3.8.256229/include/mmintrin.h:87:19: error: use of undeclared identifier '__builtin_ia32_punpckhbw'
>       return (__m64)__builtin_ia32_punpckhbw((__v8qi)__m1, (__v8qi)__m2);
>                     ^
>   /usr/local/android/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/../lib64/clang/3.8.256229/include/mmintrin.h:93:19: error: use of undeclared identifier '__builtin_ia32_punpckhwd'
>       return (__m64)__builtin_ia32_punpckhwd((__v4hi)__m1, (__v4hi)__m2);
>                     ^
>   /usr/local/android/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/../lib64/clang/3.8.256229/include/mmintrin.h:99:19: error: use of undeclared identifier '__builtin_ia32_punpckhdq'
>       return (__m64)__builtin_ia32_punpckhdq((__v2si)__m1, (__v2si)__m2);
>                     ^
>   /usr/local/android/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/../lib64/clang/3.8.256229/include/mmintrin.h:105:19: error: use of undeclared identifier '__builtin_ia32_punpcklbw'
>       return (__m64)__builtin_ia32_punpcklbw((__v8qi)__m1, (__v8qi)__m2);
>                     ^
>   /usr/local/android/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/../lib64/clang/3.8.256229/include/mmintrin.h:111:19: error: use of undeclared identifier '__builtin_ia32_punpcklwd'
>       return (__m64)__builtin_ia32_punpcklwd((__v4hi)__m1, (__v4hi)__m2);
>                     ^
>   /usr/local/android/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/../lib64/clang/3.8.256229/include/mmintrin.h:117:19: error: use of undeclared identifier '__builtin_ia32_punpckldq'
>       return (__m64)__builtin_ia32_punpckldq((__v2si)__m1, (__v2si)__m2);
>                     ^
>   /usr/local/android/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/../lib64/clang/3.8.256229/include/mmintrin.h:123:19: error: use of undeclared identifier '__builtin_ia32_paddb'; did you mean '__builtin_arm_qadd'?
>       return (__m64)__builtin_ia32_paddb((__v8qi)__m1, (__v8qi)__m2);
>                     ^
>   /usr/local/android/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/../lib64/clang/3.8.256229/include/mmintrin.h:123:19: note: '__builtin_arm_qadd' declared here
>   /usr/local/android/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/../lib64/clang/3.8.256229/include/mmintrin.h:123:40: error: cannot initialize a parameter of type 'int' with an rvalue of type '__v8qi' (vector of 8 'char' values)
>       return (__m64)__builtin_ia32_paddb((__v8qi)__m1, (__v8qi)__m2);
>                                          ^~~~~~~~~~~~
>   /usr/local/android/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/../lib64/clang/3.8.256229/include/mmintrin.h:129:19: error: use of undeclared identifier '__builtin_ia32_paddw'; did you mean '__builtin_arm_qadd'?
>       return (__m64)__builtin_ia32_paddw((__v4hi)__m1, (__v4hi)__m2);
>                     ^
>   /usr/local/android/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/../lib64/clang/3.8.256229/include/mmintrin.h:123:19: note: '__builtin_arm_qadd' declared here
>       return (__m64)__builtin_ia32_paddb((__v8qi)__m1, (__v8qi)__m2);
>                     ^
>   /usr/local/android/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/../lib64/clang/3.8.256229/include/mmintrin.h:129:40: error: cannot initialize a parameter of type 'int' with an rvalue of type '__v4hi' (vector of 4 'short' values)
>       return (__m64)__builtin_ia32_paddw((__v4hi)__m1, (__v4hi)__m2);
>                                          ^~~~~~~~~~~~
>   /usr/local/android/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/../lib64/clang/3.8.256229/include/mmintrin.h:135:19: error: use of undeclared identifier '__builtin_ia32_paddd'; did you mean '__builtin_arm_qadd'?
>       return (__m64)__builtin_ia32_paddd((__v2si)__m1, (__v2si)__m2);
>                     ^
>   /usr/local/android/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/../lib64/clang/3.8.256229/include/mmintrin.h:123:19: note: '__builtin_arm_qadd' declared here
>       return (__m64)__builtin_ia32_paddb((__v8qi)__m1, (__v8qi)__m2);
>                     ^
>   /usr/local/android/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/../lib64/clang/3.8.256229/include/mmintrin.h:135:40: error: cannot initialize a parameter of type 'int' with an rvalue of type '__v2si' (vector of 2 'int' values)
>       return (__m64)__builtin_ia32_paddd((__v2si)__m1, (__v2si)__m2);
>                                          ^~~~~~~~~~~~
>   fatal error: too many errors emitted, stopping now [-ferror-limit=]
>   20 errors generated.
>   ninja: build stopped: subcommand failed.


> * Try:
> Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output.

I've read some other topics about this but they seem different or related to building, afaiu, android upstream library without SSE.
Is there someone who can confirm this and / or shed some light?
I'm up to get to the end of this, and I'd like to contribute a solution for this. I don't like being defeated by a build system whatever complicated it can be...:sunglasses:

-------------------------

weitjong | 2017-03-22 11:35:24 UTC | #2

Since when the building of Urho3D library is coupled with downstream project? Our build scripts for the library building are complex because they are cross-platform. So, what do you want to achieve by making it work just for Android platform?

-------------------------

johnnycable | 2017-03-22 14:01:41 UTC | #3

Thank you for your prompt answer. Very simply put, what I want is:
- upstream, normal Urho3D build, as usual, for android (and the other platforms)
- spawn my own apps downstream, by linking to the upstream prebuilt libraries...
This way, I'll be having a prebuilt libraries (for android and all other platforms) in UHRO3D_HOME, and a group of apps that links against them without having to rebuild liburho3d.a over and over again in the downstream.
So as you say I want to mantain them decoupled (a Urho3d build tree somewhere, a stage dir somewhere else), while building against a library installed somewhere. Quite a common solution. I want to avoid downstream library building again and again, if I'm creating an app. I've did it successfully with os x and ios, but I'm getting problems with android... so I'm guessing if it's possible in that platform.

The error shown arises from an android build created in android studio 2.3 against latest android tools (SDK Build tools 25.0.2), while linking a cpp urho "helloworld" app to the URHO3D_HOME already built android library. While sure this is out of Urho's way for android and maybe I shouldn't be asking in the beginning, that would probably be possible so I wanted to give it a try... latest android fully supports this kind of builds (uses cmake and ninja). For instance, this is the CMakelists.txt created in android studio 2.3 as explained in https://developer.android.com/studio/projects/add-native-code.html

--------------------

CMakelists.txt

--------------------

    > # Sets the minimum version of CMake required to build the native library.

    > cmake_minimum_required(VERSION 3.4.1)

    > # Creates and names a library, sets it as either STATIC
    > # or SHARED, and provides the relative paths to its source code.
    > # You can define multiple libraries, and CMake builds them for you.
    > # Gradle automatically packages shared libraries with your APK.

    > #
    > # URHO_PROJECTDIR is the downstream android app dir
    > #

    > # get all sources
    > file (GLOB_RECURSE SOURCES $ENV{URHO_PROJECTDIR}/src/ FOLLOW_SYMLINKS $ENV{URHO_PROJECTDIR}/src/*.cpp )
    > file (GLOB_RECURSE HEADERS $ENV{URHO_PROJECTDIR}/src/ FOLLOW_SYMLINKS $ENV{URHO_PROJECTDIR}/src/*.h )

    > # get includes
    > include_directories ($ENV{URHO3D_HOME}/include/)

    > # set library name for downstream app
    > add_library( # Sets the name of the library.
    >              native-lib

    >              # Sets the library as a shared library.
    >              SHARED

    >              # Provides a relative path to your source file(s).
    >              ${SOURCES}
    >              )

    > # add urho3d library to link to
    > add_library ( Urho3D
    >               SHARED
    >               IMPORTED
    >               )

    > # get all the abis, it's coupled with gradle.build
    > set_target_properties( # Specifies the target library.
    >                        Urho3D

    >                        # Specifies the parameter you want to define.
    >                        PROPERTIES IMPORTED_LOCATION

    >                        # Provides the path to the library you want to import.
    >                        /usr/local/Urho/Urho3D-1.6/build/android/Debug/libs/${ANDROID_ABI}/libUrho3D.a

    >                        )

    > # Specifies libraries CMake should link to your target library. You
    > # can link multiple libraries, such as libraries you define in this
    > # build script, prebuilt third-party libraries, or system libraries.

    > target_link_libraries( # Specifies the target library.
    >                        native-lib

    >                        # Links the target library to the log library
    >                        # included in the NDK.
    >                        Urho3D
    >                        )

---------------------------

My guess and my asking is if that error arise for this kind of build and does not where I build upstream urho library because i'm not taking in Urho3D-CMake-common.cmake and all other cmake setups?
Linking against a library this way in c++ should work easily, just a source cpp file, a static library and cmake... very common...

-------------------------

weitjong | 2017-03-22 14:42:17 UTC | #4

This is what we expect our build system should do: build Urho3D library with ease on all the supported platforms. Once the library is built, it can be used as an external library in the downstream projects either directly from Urho3D's build tree or from an installation directory (if you call "make install" to install Urho3D first to somewhere in your file system as an SDK). From this point on, your downstream project does not need to constantly rebuild the Urho3D library. In fact you should treat it like any other 3rd-party libraries that you may want to use in your own project. No more and no less.

And about the Urho3-CMake-common.cmake (or in master branch it is now called UrhoCommon.cmake), no, you don't have to use it in your own project. This fact is not just applicable for Android platform, but also applicable to all platforms in general. You should use it when and only when you want to reuse the existing Urho3D build system for your own project, i.e you want your project becomes cross-platform for free using the already test-proven build system (I am not saying it is perfect, mind you). However, if you just want to target Android platform using Android Studio with Gradle/Maven or what have you, or you just want to create another Super-Editor for Urho3D using Qt Creator, or that you already have your own build system in place, then you don't need to use this file and also you don't need to structure your project based on Urho project. In fact you don't have to use CMake even in order to use the library. Just use it as any other libraries you have used before. There is an example in our online documentation where we use pkg-config to link against the Urho3D library, just like any other libraries. It is your project so it is your way. I would be sad if our users have a view that Urho3D project is forcing our users to do thing certain way only.

-------------------------

weitjong | 2017-03-22 15:05:31 UTC | #5

BTW, I am sorry that I didn't answer your question straight on. I am not an Android Studio user, so I could not comment much on your specific error you faced.

-------------------------

johnnycable | 2017-03-22 15:43:38 UTC | #6

Thank you very much. This is exactly as I expected.
I removed SSE option from android library builds, looks like it is related to Intel processors only, and now those errors are gone. Now I'm getting undefined reference to glDeleteBuffers and a lots of other open gl, and __android_log_print and so on... missing libraries...
Errors on Android are then related to mr. gradle I think. It appears old ndk-build system was a lot more soundproof...

-------------------------

18500864609 | 2018-12-15 09:35:11 UTC | #7

hello,I met a same problem like you met ,Have you solved this problem? Can you give me some suggestion?

-------------------------

weitjong | 2018-12-15 09:52:19 UTC | #8



-------------------------

weitjong | 2018-12-15 09:53:47 UTC | #9

We have migrated to use Gradle build system for Android platform.

-------------------------

