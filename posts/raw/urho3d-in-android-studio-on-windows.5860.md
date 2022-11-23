WangKai | 2020-02-03 14:58:30 UTC | #1

I've spend a lot of time try to sort out all the issues and build Urho3D using Android Studio on Windows 10, a lot of issues occur.

I think it's better to create a new thread here, so it would be clearer and may help other people as well.

If you know something about Android Studio + Windows, please give me a hand.

Thanks!

-------------------------

weitjong | 2020-02-03 16:07:48 UTC | #2

I am very sorry to hear that. I really want to help. I have tried to install Windows 10 using the ISO download provided by Microsoft to my new rig one or two months ago, however, I gave up after numerous attempts. My new rig does not have DVD/Bluray drive anymore and somehow I could not get the Linux tool to "burn" the ISO properly to my USB drive. So, until I solve my Windows 10 installation issue, I cannot do much to help you guys on that side of the digital divide.

p.s. I have a valid Win7 license key, which some suggested can be used to activate the Win10. But I have not really reached that point.

-------------------------

WangKai | 2020-02-03 16:26:19 UTC | #3

I understand, you've already done a lot.

I think I can just paste my issues, if someone know the possible answer, it would be solvable.


My #1 issue -

>CMake Error at D:/code/man/Urho3D/CMake/Modules/FindUrho3D.cmake:343 (message):
>  Could NOT find compatible Urho3D library in Urho3D SDK installation or
>  build tree or in Android library.  Use URHO3D_HOME environment variable or
>  build option to specify the location of the non-default SDK installation or
>  build tree.  For Android platform, double check if you have specified to
>  use the same ANDROID_ABI as the Urho3D Android Library, especially when you
>  are not using universal AAR.
>Call Stack (most recent call first):
>  D:/code/man/Urho3D/CMake/Modules/UrhoCommon.cmake:244 (find_package)
>  CMakeLists.txt:45 (include)

-------------------------

WangKai | 2020-02-03 16:50:00 UTC | #4

My #2 issue - **SOLVED after I installed MinGW**

Steps 
1. Download from http://www.mingw.org/
2. Install MinGW Installation Manager
3. Check & Install (**Apply Changes** from the menu) components as
![image|690x153](upload://bMyEbmcrFTzg6aIsD23hQuawjja.png) 
4. Add execute folders to path (Environment variable)
![image|368x51](upload://7MkyGh5yY6gB8imdLmxpWeJlgtz.png) 

>CMake Error at D:\code\man\Urho3D\CMake\Modules\CheckCompilerToolchain.cmake:162 (message):
>  Could not find native compiler toolchain.  This is usually caused by wrong
>  PATH env-var value.
>
>  CMake Warning (dev) in CMakeLists.txt:
>
>    No project() command is present.  The top-level CMakeLists.txt file must
>    contain a literal, direct call to the project() command.  Add a line of
>    code such as
>
>  
>
>      project(ProjectName)
>
>  
>
>    near the top of the file, but after cmake_minimum_required().
>
>  
>
>    CMake is pretending there is a "project(Project)" command on the first
>    line.
>
>  This warning is for project developers.  Use -Wno-dev to suppress it.
>
>  
>
>  CMake Error in CMakeLists.txt:
>
>    No CMAKE_C_COMPILER could be found.
>
>  
>
>    Tell CMake where to find the compiler by setting either the environment
>    variable "CC" or the CMake cache entry CMAKE_C_COMPILER to the full path to
>    the compiler, or to the compiler name if it is in the PATH.
>
>  
>
>  
>
>  CMake Error in CMakeLists.txt:
>
>    No CMAKE_CXX_COMPILER could be found.
>
>  
>
>    Tell CMake where to find the compiler by setting either the environment
>    variable "CXX" or the CMake cache entry CMAKE_CXX_COMPILER to the full path
>    to the compiler, or to the compiler name if it is in the PATH.
>
>  
>
>  
>
>Call Stack (most recent call first):
>  Source/Urho3D/CMakeLists.txt:210 (check_native_compiler_exist)
>
>

-------------------------

WangKai | 2020-02-04 06:58:52 UTC | #5

My #3 issue - **SOLVED by change compiler options in the Android Studio Settings**
![image|690x397](upload://mkajakiGUd5Cb7arsGxdlnB8gMI.png) 

https://stackoverflow.com/questions/33216248/passing-p-parameters-to-gradle-from-android-studio

----
How can I control build options in Android Studio?

According to 
https://urho3d.github.io/documentation/HEAD/_building.html#Building_Android

**"The Gradle properties can be passed by using "-P" Gradle option, e.g.: "./gradlew -P URHO3D_LUA=0 build" to build without Lua subsystem."**

I have tested with gradlew.bat, with -P parameters, it works, how can I achieve same in Android Studio?

-------------------------

Modanung | 2020-02-03 17:03:30 UTC | #6

Did you take a look at this?
https://developer.android.com/studio/build/

-------------------------

WangKai | 2020-02-03 17:07:40 UTC | #7

About 50%... apology for the lack of Android development knowledge.

-------------------------

weitjong | 2020-02-04 01:32:51 UTC | #8

Are you trying to build the library or use the library? Your first issue indicates the latter. Does that mean building part is already successfully done on Win10?

-------------------------

WangKai | 2020-02-04 05:27:17 UTC | #9

I'm building urho itself by open urho directory by Android Studio. I have built it by gradlew command line, I'm not sure if it will affect the Android Studio result. The configuration is success and the #1 issue disappeared later. Now I'm stuck with #3.

-------------------------

WangKai | 2020-02-04 07:00:08 UTC | #10

My #4 issue- Adding -P URHO3D_WEBP=0 for the compiling option will disable WebP, but it is not the solution.

>FAILED: Source/ThirdParty/WebP/CMakeFiles/WebP.dir/src/dsp/cpu.c.o 
>D:\AndroidDev\AndroidSDK\ndk\21.0.6113669\toolchains\llvm\prebuilt\windows-x86_64\bin\clang.exe --target=armv7-none-linux-androideabi17 --gcc-toolchain=D:/AndroidDev/AndroidSDK/ndk/21.0.6113669/toolchains/llvm/prebuilt/windows-x86_64 --sysroot=D:/AndroidDev/AndroidSDK/ndk/21.0.6113669/toolchains/llvm/prebuilt/windows-x86_64/sysroot -DURHO3D_ANGELSCRIPT -DURHO3D_FILEWATCHER -DURHO3D_IK -DURHO3D_LOGGING -DURHO3D_NAVIGATION -DURHO3D_NETWORK -DURHO3D_PHYSICS -DURHO3D_PROFILING -DURHO3D_STATIC_DEFINE -DURHO3D_THREADING -DURHO3D_URHO2D -DURHO3D_WEBP  -g -DANDROID -fdata-sections -ffunction-sections -funwind-tables -fstack-protector-strong -no-canonical-prefixes -D_FORTIFY_SOURCE=2 -march=armv7-a -mthumb -Wformat -Werror=format-security  -Qunused-arguments -fcolor-diagnostics -Wno-argument-outside-range -O0 -fno-limit-debug-info  -fPIC -MD -MT Source/ThirdParty/WebP/CMakeFiles/WebP.dir/src/dsp/cpu.c.o -MF Source\ThirdParty\WebP\CMakeFiles\WebP.dir\src\dsp\cpu.c.o.d -o Source/ThirdParty/WebP/CMakeFiles/WebP.dir/src/dsp/cpu.c.o   -c ../../../../../../Source/ThirdParty/WebP/src/dsp/cpu.c
>../../../../../../Source/ThirdParty/WebP/src/dsp/cpu.c:22:10: fatal error: 'cpu-features.h' file not found
>#include <cpu-features.h>
>         ^~~~~~~~~~~~~~~~
>1 error generated.

It is an error compiling WebP related code.

-------------------------

WangKai | 2020-02-04 07:52:45 UTC | #11

Definitely many places can be optimized **but Samples of Urho3D now can run and be debugged. Physical phone also runs.**

![image|690x356](upload://be3hO8l66PV84ttGptGPVX30TeG.jpeg) 

The default size of urho app is really big, storage of an emulater can be changed -
https://stackoverflow.com/questions/2239330/how-to-increase-storage-for-android-emulator-install-failed-insufficient-stora

-------------------------

Bluemoon | 2020-02-04 07:29:08 UTC | #12

Good to know you are making progress. 

For the app size, I assume your build was debug build so it's expected to be big

-------------------------

WangKai | 2020-02-04 07:37:25 UTC | #13

Yes. also IMO, there are other reasons.

1. ANDROID_ABI can be used, currently it is universal -
![image|400x115](upload://srWrVwbK3N52FuKc8feqEeLQQ1R.png) 

2. I also guess this should be used -

https://developer.android.com/studio/build/shrink-code

-------------------------

weitjong | 2020-02-04 09:42:06 UTC | #14

[quote="WangKai, post:10, topic:5860"]
…/Source/ThirdParty/WebP/src/dsp/cpu.c
…/…/…/…/…/…/Source/ThirdParty/WebP/src/dsp/cpu.c:22:10: fatal error: ‘cpu-features.h’ file not found
#include <cpu-features.h>
^~~~~~~~~~~~~~~~
1 error generated.
[/quote]
Your last issue is reproducible when using latest SDK. Last night I hit by this too after upgrading my Android SDK in my dockerized build environment. But it was late so I didn't look into it deeper yet.

[quote="WangKai, post:13, topic:5860"]
ANDROID_ABI can be used, currently it is universal
[/quote]
We provide build option for Gradle Android build to allow user to choose which ABI to be built. Our default is the default of Android plugin for Gradle provided by Google.

-------------------------

WangKai | 2020-02-04 12:44:29 UTC | #15

Yes, you are right. I checked the document. We can copy all cmake scripts and stuff and start a new project, using Urho3D as library. However, I have not figured out yet how to setup an project for Android, with all these android related scripts.

-------------------------

weitjong | 2020-02-08 11:44:56 UTC | #16

I will bump the version of some dependencies for Android build and modify the Gradle build script to work with latest Android SDK/NDK. I expect building of Urho3D library to work out of the box via CLI or IDE (IntelliJ and Android Studio, they internally invoke the same Gradle process anyway). Well, until newer SDK/NDK breaks it again.

As for using Urho3D as (Android) library with Gradle as the build system, you will have to learn how to use AAR. When I migrated the build system from Ant to Gradle, I have decided to go all the way to publish our AAR to a public repository and that downstream project should be able to easily setup to use Urho3D library as one of the project dependency. However, I dropped the ball somewhere and I haven't got time to finish what I have started. The AAR is already published by the CI automatically. See https://bintray.com/bintray/jcenter?filterByPkgName=urho3d-lib

Edit: the culprit was NDK 21.0.x. As a quick fix I configure the build script to use NDK 20.1.5948944, so I can move on for other changes. It means user will have to install Android NDK side by side with the right version and not the (deprecated) Android NDK-bundle anymore.

Edit2: after further investigation I actually did not find anything unusual in the NDK 21.0.6113669 as compared to NDK 20.1.5948944 in respect to cpu-features. Long story short, I have to adjust the build script so that it works for both versions now. In fact now I actually not sure how it worked in the past without the adjustment. Anyway...

-------------------------

weitjong | 2020-02-11 16:06:23 UTC | #17

The latest master branch works out of the box for Android Studio 3.5 now (tested on Linux host system). That's the good news. The bad news is, all the Lua samples do not work anymore via Urho3DPlayer because of FORTIFY check. I did't see this before using previous SDK. I know it is off-topic but I think you may want to know in case you re-enable Lua subsystem again in your build.

```
A/libc: FORTIFY: strchr: prevented read past end of buffer
    Fatal signal 6 (SIGABRT), code -1 (SI_QUEUE) in tid 6545 (SDLThread), pid 6443 (SDLActivity)
```

Edit: with LuaJIT, on the other hand, all the samples pass the test with flying colors.

-------------------------

WangKai | 2020-02-09 17:51:18 UTC | #18

Thank you @weitjong you are the best! I will find another day to try the new one and figure out how to build Urho as a library. Thank you again for the quick response and help!

-------------------------

