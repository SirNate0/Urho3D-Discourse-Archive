Oberos | 2018-06-10 07:50:16 UTC | #1

I'm getting this error when running the cmake_android.bat file. I'm stumped here, what other env-var am I missing, or is there something else? Has anyone have had recent success making the project for armeabi-v7a 32bit android-19? Any help would be greatly appreciated, thanks.

> -- Performing Test HAVE_NATIVE_COMPILER - Failed
> CMake Error at CMake/Modules/CheckCompilerToolchain.cmake:162 (message):
>   Could not find native compiler toolchain.  This is usually caused by wrong
>   PATH env-var value.
> 
>   CMake Error at C:/Program
>   Files/CMake/share/cmake-3.9/Modules/CMakeTestCCompiler.cmake:51 (message):
> 
>     The C compiler "C:/Program Files (x86)/Microsoft Visual Studio
>     14.0/VC/bin/cl.exe" is not able to compile a simple test program.
> 
>     It fails with the following output:
> 
>      Change Dir: C:/Play/Urho3D/droid/generated/CMakeFiles/CMakeTmp

**I have followed the documentation on both of theses links;**
https://discourse.urho3d.io/t/howto-urho3d-android-setup-on-win7/1938
https://urho3d.github.io/documentation/1.4/_building.html#Building_Android

**Added these to my environment variable PATH**
_C:\Android\sdk\platform-tools;_
_C:\Android\sdk\tools;_
_C:\Android\sdk\tools\bin;_
_C:\Android\sdk\ndk-bundle;_
_C:\Android\sdk\ndk-bundle\build;_
_C:\Android\sdk\ndk-bundle\prebuilt\windows\bin;_
_C:\Android\sdk\ndk-bundle\prebuilt\windows-x86_64\bin;_
_C:\Android\sdk\ndk-bundle\toolchains;_
_C:\Android\sdk\ndk-bundle\toolchains\arm-linux-androideabi-4.9\prebuilt\windows-x86_64;_

**And run the cmake_android.bat file with theses defines;**
_-DANDROID=1 -DANDROID_NATIVE_API_LEVEL=android-19 -DANDROID_ABI=armeabi-v7a -DANDROID_TOOLCHAIN_NAME=arm-linux-androideabi-clang_

-------------------------

rku | 2018-06-10 08:04:12 UTC | #2

Have you set `ANDROID_NDK` env/cmake variable to android ndk? You might also need `ANDROID_SDK` with a path to android sdk.

-------------------------

Oberos | 2018-06-10 19:01:12 UTC | #3

Thank you for replying, These are the other environment variables I have set before (I should have posted them first). I'm at the point of uninstalling all of Android Studio and SDK NDK and installing older versions. Maybe someone that does have everything running can post the versions they have, what environment variables, and what android version they are building for?

ANDROID_HOME C:\Android\sdk
ANDROID_SDK C:\Android\sdk
ANDROID_NDK C:\Android\sdk\ndk-bundle
ANDROID_NDK_HOME C:\Android\sdk\ndk-bundle
ANDROID_PLATFORM_TOOLS C:\Android\sdk\platform-tools
GRADLE_HOME C:\gradle
JAVA_HOME C:\Program Files\Java\jdk1.8.0_172

-------------------------

SirNate0 | 2018-06-14 02:33:19 UTC | #4

Try disabling the tools build (possibly more, like Lua maybe) - the error seems to be that it can't find a native compiler, not the Android ones, and I think that's because the build system looks for one to build the tools like the Asset Importer (and maybe a tolua program). Not sure if that's it, though...

-------------------------

Oberos | 2018-06-15 03:05:13 UTC | #5

Thank you for the suggestion, I've added -DURHO3D_TOOLS=0 but still run into the "– Performing Test HAVE_NATIVE_COMPILER - Failed" error as before. I've given up on getting this to work with Android and have moved onto  working on iOS and PC. Thanks to all for the help, maybe one day in the future I'll revisit getting Urho on Android.

-------------------------

weitjong | 2018-06-15 13:32:29 UTC | #6

SirNate is right. When performing a cross-compiling build (Android build included) and that a host tool build is required then both the cross-compiler and native compiler toolchains need to be installed. For *nix host system, the latter is almost always the case for any development box. However, that is not so for Windows host. So on Windows host you should install MinGW in order to get started easily for Android build that requires the host tool building.

Having said that, that is not the last hurdle you will find for Android build at the moment. So if you already giving up after hitting this, may be you have made a right decision to skip Android platform first.

-------------------------

WangKai | 2020-02-02 15:20:04 UTC | #7

Do I still need MinGW for windows when building Android APKs?

-------------------------

WangKai | 2020-02-02 15:34:14 UTC | #8

If I remembered correctly, the android project generation is as easy as Visual Studio's?

I don't know much about Android development, however, I think we need to simplify it a little bit or write a tutorial on how to handle Android platform.

-------------------------

weitjong | 2020-02-02 16:09:27 UTC | #9

This is an old thread that is no longer relevant. After switching to Gradle for Android build, the "cmake_android.bat" or "cmake_android.sh" are removed.

[quote="WangKai, post:7, topic:4302, full:true"]
Do I still need MinGW for windows when building Android APKs?
[/quote]
Yes, in short you still need it for building the host tool. But, if you do not use build options that require host tool building then you don't need it. This is the same for all host systems when performing a cross-compiling build and at the same time performing host tool building and use the host tool on the fly in the build itself. In this scenario the build would require a host/native compiler to be around. On Linux or Mac, it can be GCC or Clang. On Windows, it can be MinGW or what have you.

[quote="WangKai, post:8, topic:4302"]
If I remembered correctly, the android project generation is as easy as Visual Studio’s?
[/quote]
It depends on who you ask. For me, each platform has its own challenge and cross-compiling is always more so compared to native compiling.

-------------------------

weitjong | 2020-02-02 16:09:41 UTC | #10



-------------------------

