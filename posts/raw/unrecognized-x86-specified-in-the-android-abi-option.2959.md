ak88 | 2017-03-27 21:58:18 UTC | #1

Hi guys,

I prepared scripts to compile Urho3D binaries, for all the platforms one month ago.
For Android I used **ANDROID_ABI=x86** to have more performance on emulators.

But today I pulled master brunch and tried to compile fresh version of Urho3D and got the error on Android build:
> CMake Error at CMake/Toolchains/Android.cmake:242 (message):
>   Unrecognized 'x86' specified in the ANDROID_ABI option, supported values
>   are: "armeabi-v7a", "armeabi-v6", "armeabi".

at the same time native(linux-x64) and web builds compiled well.

Seems that something has changed in the Android building configuration since my last pull.
I use **android-ndk-r12b** and I also tried to compile on **android-ndk-r13b** and got the same error.

I investigated commits on master and found commit with message (23 days ago):
> Make the CMake/Android toolchain file compatible with NDK 13c.

but there is not NDK 13c on official site. Latest version is NDK 14, previous NDK 13b.

Guys, any suggestion, what can it be?
Urho does not support **ANDROID_ABI=x86** any more, does it?

Thanks in advance.

-------------------------

weitjong | 2017-03-28 02:24:48 UTC | #2

It is still supported. We have defaulted to use Clang instead of GCC for Android build now. Travis CI shows how it should be done. https://github.com/urho3d/Urho3D/blob/1bd123ecfb387bc36455b30f3e3d601b6f20f28d/.travis.yml#L278-L283

-------------------------

ak88 | 2017-03-28 02:24:28 UTC | #3

Thanks, using link that you attached I specified **-DANDROID_TOOLCHAIN_NAME=x86-4.9** and it helped in my case.

Are there any differences between **clang** and **gcc** compilation results?

-------------------------

weitjong | 2017-03-28 08:41:24 UTC | #4

You have to test that yourself with your application. Note that the move is the reaction to Android NDK release notes where GCC compiler toolchain is marked as deprecated and could be removed in future releases of NDK.

-------------------------

ak88 | 2017-03-30 23:05:00 UTC | #5

I tried to migrate to **clang**, but got another error:

> -- Check for working CXX compiler: /opt/sdks/android-ndk-r14b/toolchains/llvm/prebuilt/linux-x86_64/bin/clang++
> -- Check for working CXX compiler: /opt/sdks/android-ndk-r14b/toolchains/llvm/prebuilt/linux-x86_64/bin/clang++ -- broken
> CMake Error at /usr/share/cmake-3.5/Modules/CMakeTestCXXCompiler.cmake:54 (message):
>   The C++ compiler
>   "/opt/sdks/android-ndk-r14b/toolchains/llvm/prebuilt/linux-x86_64/bin/clang++"
>   is not able to compile a simple test program.

and a lot of errors like:

> /usr/bin/ld: cannot find Scrt1.o: No such file or directory

>   /usr/bin/ld: cannot find crti.o: No such file or directory

>   /usr/bin/ld: cannot find crtbeginS.o: No such file or directory

>   /usr/bin/ld: skipping incompatible
>   /opt/sdks/android-ndk-r14b/sources/cxx-stl/llvm-libc++/libs/x86/libc++_static.a
>   when searching for -lc++_static

>   /usr/bin/ld: cannot find -lc++_static

>   /usr/bin/ld: skipping incompatible

seems that clang compiler trying to load shared libs using native ld that is not compatible with them.

-------------------------

weitjong | 2017-03-31 02:10:45 UTC | #6

Sorry if this is not helpful for you but as I have shown you before that all our Android CI builds have moved to Clang for quite some time now and they are all fine since then. Although they still use Android NDK 13b but it should not make any differences. Also see this http://discourse.urho3d.io/t/urho3d-1-7-release-pending-work/2790/18. 

Ensure you have tested on a clean/new build tree.

-------------------------

