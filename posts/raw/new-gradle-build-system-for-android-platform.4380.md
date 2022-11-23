weitjong | 2018-08-05 04:06:40 UTC | #1

I have pushed the initial Gradle build system for Android to `gradle-kotlin-dsl` development branch. <del>It is still WIP.</del> I haven't finished clean up the CMake build script to remove now old and redundant fixtures for Android build. I have only tested it on Linux host system with symlink workaround I mentioned in https://github.com/urho3d/Urho3D/issues/743. <del>The workaround only works when invoking gradle wrapper from the CLI (Still haven't figured out how to prevent the Android plugin bug to manifest itself during Android Studio "gradle sync"). However, if you don't modify the gradle build script in Android Studio editor then you should not see the problem at all. Please test the build system on Urho3D project only, or if you want to try it on your own project then make sure you have a proper backup plan due to symlink bug. You have been warned.</del>

For CLI user, after checking out the development branch, cd to the Urho3D project root and run:

```
./gradlew build
```

For Android Studio user, open the project using the IDE. It should prompt you to auto-import the Gradle project. <del>Before building the project, press Ctrl+Alt+S and type "configure on demand" in the search box, locate the option and deselect it.</del>

-------------------------

weitjong | 2018-09-12 00:44:42 UTC | #2

Just managed to get the Android CI build run successfully this morning. In the process I found out one more thing user need to do in order to build successfully. The Android plugin has opinionated to use “ninja” build (not surprising as it was created by Google too) instead of the usual GNU Make. However, it is done by specifying a hard-coded path to the SDK embedded “ninja” command. This is fine for CMakeLists.txt file that the plugin invokes directly. It does not cater for any “external” invocation indirectly done by our CMake scripts and therefore the overall CMake configuration ends up with a failure because of “ninja” command is not found. <del>So, user needs to either:</del>

<del>
    a) install ninja-build globally, or
    b) adjust the PATH env var to include the path to SDK embedded “ninja” command, or
    c) change the default make program to GNU Make, this require modifying the provided build.gradle.kts though.
</del>

Edit: this prerequisite is not needed anymore as the new build script will automatically pass along the path to embedded “ninja” when invoking CMake in external child process.

-------------------------

rku | 2018-07-13 12:10:52 UTC | #3

Should we not simply use gradle all the time?

-------------------------

weitjong | 2018-07-13 12:30:26 UTC | #4

Not sure I understand you. Gradle by itself has nothing to do with Android build. It is the Android plugin for Gradle does. But the standard Android plugin does not cater for all our needs. How it trips up on handling symlink is just one example.

-------------------------

rku | 2018-07-16 12:27:45 UTC | #5

[quote="weitjong, post:2, topic:4380"]
It does not cater for any “external” invocation indirectly done by our CMake scripts and therefore the overall CMake configuration ends up with a failure because of “ninja” command is not found.
[/quote]
I guess i am not sure what that means. Project i am working on - i never touch cmake directly in android builds. Always use gradle (either from android studio or cli) and it takes care of calling cmake. Is that not an option?

-------------------------

weitjong | 2018-07-16 13:33:53 UTC | #6

I am sorry if I cannot make it clearer. English is not my primary language. The Android plugin does not scan the root CMakeLists.txt and all its children, so it does not know when somewhere in the script it spawns child processes that calls external CMake to load other CMakeLists.txt files. The latter is the problem because the plugin could not inject the hard-coded path to "ninja" for those external invocation as it could do for root CMakeLists.txt.

-------------------------

rku | 2018-07-16 13:42:48 UTC | #7

Ah i see. Build system overhere does not do any of that so that is why i had no issues. Sorry for the noise ;)

-------------------------

weitjong | 2018-07-16 14:08:38 UTC | #8

The external invocation are mainly for host tool building.

-------------------------

weitjong | 2018-08-01 01:45:38 UTC | #9

I have made another push to the dev branch. Our new Gradle build system is almost ready for general use now. The earlier issues with Gradle sync and “configuration on demand” in Android Studio should now be resolved. It should work out of the box as it can be. Feedback is most welcome, especially for those testing it on Windows host system.

Due to yet another bug in Android plugin, I am forced to use a symlink to configure the asset directory. Check the github comment if you want more detail. So for Windows users, after checking out the branch, you may have to perform a manual copy to prep the asset dir for now.

-------------------------

Miegamicis | 2018-08-01 06:24:27 UTC | #10

Sounds good! Will check this out!

-------------------------

elix22 | 2018-08-01 12:23:30 UTC | #11

Fails on my Windows machine 
 
Partial log  

 Task :android:urho3d-lib:generateJsonModelDebug
Variant=debug ABI=armeabi-v7a :-- Check for working C compiler: C:/Users/bea034/AppData/Local/Android/sdk/ndk-bundle/toolchains/llvm/prebuilt/windows-x86_64/bin/clang.exe
Variant=debug ABI=armeabi-v7a :-- Check for working C compiler: C:/Users/bea034/AppData/Local/Android/sdk/ndk-bundle/toolchains/llvm/prebuilt/windows-x86_64/bin/clang.exe -- broken
Variant=debug ABI=armeabi-v7a :CMake Error at C:/Users/bea034/AppData/Local/Android/sdk/cmake/3.6.3155560/share/cmake-3.6/Modules/CMakeTestCCompiler.cmake:61 (message):
Variant=debug ABI=armeabi-v7a :  The C compiler
Variant=debug ABI=armeabi-v7a :  "C:/Users/bea034/AppData/Local/Android/sdk/ndk-bundle/toolchains/llvm/prebuilt/windows-x86_64/bin/clang.exe"
Variant=debug ABI=armeabi-v7a :  is not able to compile a simple test program.
Variant=debug ABI=armeabi-v7a :  It fails with the following output:
Variant=debug ABI=armeabi-v7a :   Change Dir: C:/GAME-ENGINES/Urho3D-gradle-kotlin/android/urho3d-lib/.externalNativeBuild/cmake/debug/armeabi-v7a/CMakeFiles/CMakeTmp
Variant=debug ABI=armeabi-v7a :
Variant=debug ABI=armeabi-v7a :  Run Build
Variant=debug ABI=armeabi-v7a :  Command:"C:\Users\bea034\AppData\Local\Android\sdk\cmake\3.6.3155560\bin\ninja.exe"
Variant=debug ABI=armeabi-v7a :  "cmTC_127a9"
Variant=debug ABI=armeabi-v7a :  [1/2] Building C object CMakeFiles/cmTC_127a9.dir/testCCompiler.c.o
Variant=debug ABI=armeabi-v7a :  FAILED: null
Variant=debug ABI=armeabi-v7a :  C:\Users\bea034\AppData\Local\Android\sdk\ndk-bundle\toolchains\llvm\prebuilt\windows-x86_64\bin\clang.exe
Variant=debug ABI=armeabi-v7a :  --target=armv7-none-linux-androideabi
Variant=debug ABI=armeabi-v7a :  --gcc-toolchain=C:/Users/bea034/AppData/Local/Android/sdk/ndk-bundle/toolchains/arm-linux-androideabi-4.9/prebuilt/windows-x86_64
Variant=debug ABI=armeabi-v7a :  --sysroot=C:/Users/bea034/AppData/Local/Android/sdk/ndk-bundle/sysroot
Variant=debug ABI=armeabi-v7a :  -isystem
Variant=debug ABI=armeabi-v7a :  C:/Users/bea034/AppData/Local/Android/sdk/ndk-bundle/sysroot/usr/include/arm-linux-androideabi
Variant=debug ABI=armeabi-v7a :  -D__ANDROID_API__=17 -g -DANDROID -ffunction-sections -funwind-tables
Variant=debug ABI=armeabi-v7a :  -fstack-protector-strong -no-canonical-prefixes -march=armv7-a
Variant=debug ABI=armeabi-v7a :  -mfloat-abi=softfp -mfpu=vfpv3-d16 -mthumb -Wa,--noexecstack -Wformat
Variant=debug ABI=armeabi-v7a :  -Werror=format-security -fPIE -o
Variant=debug ABI=armeabi-v7a :  CMakeFiles/cmTC_127a9.dir/testCCompiler.c.o -c
Variant=debug ABI=armeabi-v7a :  C:\GAME-ENGINES\Urho3D-gradle-kotlin\android\urho3d-lib\.externalNativeBuild\cmake\debug\armeabi-v7a\CMakeFiles\CMakeTmp\testCCompiler.c
Variant=debug ABI=armeabi-v7a :  CreateProcess failed: The system cannot find the file specified.
Variant=debug ABI=armeabi-v7a :  ninja: build stopped: subcommand failed.

-------------------------

weitjong | 2018-08-01 14:23:53 UTC | #12

[quote="elix22, post:11, topic:4380"]
Variant=debug ABI=armeabi-v7a : -D__ANDROID_API__=17 -g -DANDROID -ffunction-sections -funwind-tables
[/quote]

Do you have "Android SDK Platform 17" package installed? I believe you need API level 17 for 32-bit ABI and level 21 for 64-bit ABI. Alternatively, if you have other higher API level installed in your system then you may try to reconfigure the "minSdkVersion" setting in the `build.gradle.kts`.

-------------------------

elix22 | 2018-08-01 14:42:23 UTC | #13

[quote="weitjong, post:12, topic:4380"]
Do you have “Android SDK Platform 17” package installed?
[/quote]

Yes I have them all installed from API level 10  till  API level 28 .

I guess it has todo with the CMake  compiler check option , it tries to compile "testCCompiler.c"
I guess this option should be disabled

-------------------------

weitjong | 2018-08-01 14:50:54 UTC | #14

That test is part of how CMake perform the initial configuration. I don't think it should be skipped. Have you checked the CMakeFiles/CMakeError.log located inside the `.externalNativeBuild` dirctory? or Have you tested your Android SDK installation to build other things successfully?

-------------------------

elix22 | 2018-08-01 15:16:06 UTC | #15

[quote="weitjong, post:14, topic:4380"]
Have you tested your Android SDK installation to build other things successfully?
[/quote]

Yes I have tested it On Godot just now , compiled Godot for Android successfully, followed the instructions in this link .
http://docs.godotengine.org/en/latest/development/compiling/compiling_for_android.html 

C:\godot> scons platform=android target=release
C:\godot> cd platform/android/java
C:\godot\platform\android\java> gradlew build

-------------------------

weitjong | 2018-08-01 15:32:50 UTC | #16

I think you misunderstood me. You have to test the Android SDK + Android NDK with the CMake as the build system for the native library. Godot uses SCons as the build system for the native library, so it does not prove anything here.

-------------------------

weitjong | 2018-08-01 15:47:02 UTC | #17

Can you post to somewhere the content of your CMakeError.log? It might give some clues why the initial compiler detection failed in your case.

-------------------------

elix22 | 2018-08-01 15:55:03 UTC | #18

Scons in Godot = CMake in Urho3D .
Both are using the same SDK + NDK underneath  .

I will  upload CMakeError.log  by tomorrow (going home now).
In addition I will try later today at my home on another laptop .

-------------------------

weitjong | 2018-08-01 16:02:50 UTC | #19

[quote="elix22, post:18, topic:4380"]
Scons in Godot = CMake in Urho3D .
Both are using the same SDK + NDK underneath .
[/quote]

If your error happened somewhere else and not at the CMake initial configuration then your comparison with Godot could make sense. However in your case, the failure you had is with CMake and that is one thing Godot does not have. So, your Godot build success does not mean your Android SDK/NDK/CMake installation on Windows is good or bad. It does not prove anything at all for the problem you faced.

-------------------------

elix22 | 2018-08-01 16:04:45 UTC | #20

[quote="weitjong, post:19, topic:4380"]
However in your case, the failure you had is with CMake and that is one thing Godot does not have
[/quote]

I agree. 
I am sorry I will provide you more information by tomorrow  .

-------------------------

weitjong | 2018-08-02 01:32:01 UTC | #21

FWIW, I just noticed you are not using the latest bundled CMake version available. I have also just performed a quick search on Google and found other having quite similar problem as yours using that same old bundle version.

-------------------------

elix22 | 2018-08-02 11:25:17 UTC | #22

I installed the latest , 3.12.0
Still having the same errors .

CMakeError.log output : 

Determining if the C compiler works failed with the following output:
Change Dir: C:/GAME-ENGINES/Urho3D-gradle-kotlin/android/urho3d-lib/.externalNativeBuild/cmake/debug/armeabi-v7a/CMakeFiles/CMakeTmp

Run Build Command:"C:\Users\bea034\AppData\Local\Android\sdk\cmake\3.6.3155560\bin\ninja.exe" "cmTC_13e0c"
[1/2] Building C object CMakeFiles/cmTC_13e0c.dir/testCCompiler.c.o

FAILED: null C:\Users\bea034\AppData\Local\Android\sdk\ndk-bundle\toolchains\llvm\prebuilt\windows-x86_64\bin\clang.exe  --target=armv7-none-linux-androideabi --gcc-toolchain=C:/Users/bea034/AppData/Local/Android/sdk/ndk-bundle/toolchains/arm-linux-androideabi-4.9/prebuilt/windows-x86_64 --sysroot=C:/Users/bea034/AppData/Local/Android/sdk/ndk-bundle/sysroot   -isystem C:/Users/bea034/AppData/Local/Android/sdk/ndk-bundle/sysroot/usr/include/arm-linux-androideabi -D__ANDROID_API__=17 -g -DANDROID -ffunction-sections -funwind-tables -fstack-protector-strong -no-canonical-prefixes -march=armv7-a -mfloat-abi=softfp -mfpu=vfpv3-d16 -mthumb -Wa,--noexecstack -Wformat -Werror=format-security   -fPIE -o CMakeFiles/cmTC_13e0c.dir/testCCompiler.c.o   -c C:\GAME-ENGINES\Urho3D-gradle-kotlin\android\urho3d-lib\.externalNativeBuild\cmake\debug\armeabi-v7a\CMakeFiles\CMakeTmp\testCCompiler.c

CreateProcess failed: The system cannot find the file specified.

ninja: build stopped: subcommand failed.

-------------------------

weitjong | 2018-08-02 13:52:38 UTC | #23

[quote="elix22, post:22, topic:4380"]
Run Build Command:“C:\Users\bea034\AppData\Local\Android\sdk\cmake\3.6.3155560\bin\ninja.exe” “cmTC_13e0c”
[/quote]

Based on the log, you were still using the same old version. Currently I don't think Android Plugin (at least not the version we are currently using) is capable of using vanilla CMake provided by cmake.org. Android plugin can only use the Android SDK bundled CMake. I supposed they do so because they have forked and modified the code which are not made available upstream (yet). I am not exactly sure.

Thus, you have to use the SdkManager to update your bundled CMake version and try again. Good luck.

-------------------------

elix22 | 2018-08-02 14:41:05 UTC | #24

[quote="weitjong, post:23, topic:4380"]
Based on the log, you were still using the same old version
[/quote]

You are right , I thought it was using vanilla CMake , 
I updated to latest CMake using the SDKManager , still getting these errors .
I will try to debug it during the weekend .

Determining if the C compiler works failed with the following output:
Change Dir: C:/GAME-ENGINES/Urho3D-gradle-kotlin/android/urho3d-lib/.externalNativeBuild/cmake/debug/armeabi-v7a/CMakeFiles/CMakeTmp

Run Build Command:"C:\Users\bea034\AppData\Local\Android\sdk\cmake\3.6.4111459\bin\ninja.exe" "cmTC_43c9e"
[1/2] Building C object CMakeFiles/cmTC_43c9e.dir/testCCompiler.c.o

FAILED: null C:\Users\bea034\AppData\Local\Android\sdk\ndk-bundle\toolchains\llvm\prebuilt\windows-x86_64\bin\clang.exe  --target=armv7-none-linux-androideabi --gcc-toolchain=C:/Users/bea034/AppData/Local/Android/sdk/ndk-bundle/toolchains/arm-linux-androideabi-4.9/prebuilt/windows-x86_64 --sysroot=C:/Users/bea034/AppData/Local/Android/sdk/ndk-bundle/sysroot   -isystem C:/Users/bea034/AppData/Local/Android/sdk/ndk-bundle/sysroot/usr/include/arm-linux-androideabi -D__ANDROID_API__=17 -g -DANDROID -ffunction-sections -funwind-tables -fstack-protector-strong -no-canonical-prefixes -march=armv7-a -mfloat-abi=softfp -mfpu=vfpv3-d16 -mthumb -Wa,--noexecstack -Wformat -Werror=format-security   -fPIE -o CMakeFiles/cmTC_43c9e.dir/testCCompiler.c.o   -c C:\GAME-ENGINES\Urho3D-gradle-kotlin\android\urho3d-lib\.externalNativeBuild\cmake\debug\armeabi-v7a\CMakeFiles\CMakeTmp\testCCompiler.c

CreateProcess failed: The system cannot find the file specified.

ninja: build stopped: subcommand failed.

-------------------------

weitjong | 2018-08-02 15:16:01 UTC | #25

I am sorry to hear that. I only have Win7 VM and am now trying to get the newly downloaded Android Studio IDE installed there and see whether I can reproduce your issue. To be honest, I would not expect it to differ from Linux host system by too much.

-------------------------

weitjong | 2018-08-02 16:37:30 UTC | #26

I am able to reproduce the issue! It was caused by this line:

add("-DANDROID_CCACHE=${System.getenv("ANDROID_CCACHE")}")

In my setup on Linux and also in CI, I always have "ccache" made available. There is no ccache on Windows. It is anyway a mistake on my side to have that option always defined. I thought define it to "" is equals to not define it. I was wrong apparently.

Thanks for reporting this.

I also found another mistake in the path handling which causes the "Gradle sync" to fail on Windows system. In Windows the path separators are going the wrong way compared to *NIX.

I will try to fix these mistakes tomorrow.

-------------------------

weitjong | 2018-08-03 16:44:51 UTC | #27

Those two issues should have been fixed in my local branch. However, I delay the push as I want to also fix one more other minor issue which causes the initial gradle sync on Android Studio to temporary fail, even on Linux host system, until a build is made and then the retry of gradle sync would become ok. CLI user does not have this last issue as initial “gradle build” from scratch will always work. I hope to get the initial “gradle sync” to work cleanly too.

-------------------------

weitjong | 2018-08-04 06:36:25 UTC | #28

Made another push to the dev branch. Tested it to be both working on my Linux host system and on my Win7 VM. Here are roughly the steps I took on Windows system:

1. Check out the branch.
2. Prep the asset dirs in both the modules, i.e. change the Linux symlink to Windows MKLINK. Call `git add` to stage the changes, so that git won't bother with them afterward.
3. Set the gradle property to disable "URHO3D_LUA".
4. Open the project root in the Android Studio IDE. Accept the default to import the Gradle project.
5. After the "gradle sync" completed without any error, press Ctrl+F9 to build the project or Shift+F10 to run the launcher app.

To enable Lua/LuaJIT, the "ninja" build tool must be installed globally. The reason for this has been explained in my previous comment above in this thread. Lua needs a host tool to be built alongside.

-------------------------

elix22 | 2018-08-05 16:21:49 UTC | #29

It looks much better now , but fails during the actual compilation.

[138/922] Linking C static library Source\ThirdParty\ik\libik.a
...
...
...
 The command line is too long.
 ninja: build stopped: subcommand failed.

-------------------------

slapin | 2018-08-05 17:03:39 UTC | #30

Yeah, windows have quite limited command line size AFAIK

-------------------------

weitjong | 2018-08-06 02:19:49 UTC | #31

Try use a shorter directory name.

Another way to workaround the Windows “cmd” limitation is to tell CMake/Ninja generator to use “response files”. This workaround is currently used by our MinGW build on Windows host too, I believe. However, this way would slow down the build due to extra disk I/O. I will see how many users request for it before deciding to implement this.

-------------------------

weitjong | 2018-08-09 15:15:33 UTC | #32

The dev branch has been merged to master branch just now.

-------------------------

Bluemoon | 2018-08-13 11:39:51 UTC | #33

Are we to expect an update to Urho3D official build documentation for Android or does the current one suffice for this case?

-------------------------

weitjong | 2018-08-13 11:55:02 UTC | #34

It is already updated. Let us know if it is still not clear.

-------------------------

Bluemoon | 2018-08-13 12:11:23 UTC | #35

I've seen it, sorry I forget to select the HEAD option for the documentation. 

Thanks

-------------------------

Bluemoon | 2018-08-14 08:38:27 UTC | #36

I'm on Win10 and I've hit the "The command line is too long" error @elix22 encountered also. If this is going to be an issue with windows build I think it would be better to have the "response files" option implemented. 

Besides the earlier mentioned and shorter directory name, which other work arounds are available?

-------------------------

Miegamicis | 2018-08-14 11:12:22 UTC | #37

I tested the Android build system on Ubuntu 16.04. Seemed to work, altough I notices that when I open the sample applications on actual device, they close immediatelly without giving any error message. This doesn't happen all the time tho.

-------------------------

weitjong | 2018-08-14 11:24:00 UTC | #38

Thanks for your feedback. Personally I have tried it on Windows 7 host system and all went well. I didn’t intentionally shorten my directory name or anything but I guess I was just lucky that the generated ninja build scripts did not exceed the command line buffer limit. Personally I think it is better to workaround by choosing a shorter project directory name than having forced to use “response files”. Also see https://github.com/android-ndk/ndk/issues/397.

-------------------------

weitjong | 2018-08-14 11:25:59 UTC | #39

Any error from logcat?

-------------------------

Miegamicis | 2018-08-14 12:01:35 UTC | #40

Didn't yet looked in to that since I don't have configured Android workspace locally, I used prebuilt docker images to run builds. Can check that later at home.

-------------------------

weitjong | 2018-08-14 15:13:37 UTC | #41

I could not reproduce the issue on my rusty Samsung Galaxy Tab 7 running Jelly Bean 4.1. Tested launching a number C++ native samples, and also a number of AS and Lua scripts (via Urho3DPlayer) . It actually works better than I expected, much better than the previous launcher. The back button works now and a different selection can be made in the launcher without forcing to exit it first, like in the past.

BTW, I have just tested building the project via IntelliJ IDEA Ultimate 2018.2 and installed the dev APK to my Galaxy Tab using IDEA. It works as well as Android Studio, IMHO.

In case it makes any difference, I am using SHARED Urho3D lib type.

-------------------------

Miegamicis | 2018-08-15 07:15:05 UTC | #42

I was using circleci/android:api-28-alpha docker image to do builds. Nothing unusual appeared in the log files. I think the docker image itself might cause this problem, since there's the `alpha` tag on it. Will test out using different image.

Also is there any way how I can reduce the build directory size? When doing `./gradlew build` it takes >20GB of HDD space. I found a workaround using `./gradlew assembleRelease -P URHO3D_LUA=0 -P ANDROID_ABI=armeabi-v7a` command, but it still took a lot of space. This also might be caused by the faulty docker image tho.

-------------------------

weitjong | 2018-08-15 07:58:46 UTC | #43

It depends on what you want to build. If you just need the AAR for your own project then just build the lib module and then publish it locally. By default though, it will build both the lib and launcher app (and by that it will include all the 50+ samples). The default uses STATIC lib type so it’s 50+ *.so that all contain the same bits from the STATIC lib. To reduce the size, you can use the SHARED lib type. So it becomes 50+ much smaller *.so, plus “libUrho3D.so”.  Note the STATIC lib is not shipped in the APK, while the SHARED lib does.

-------------------------

weitjong | 2018-08-17 05:06:23 UTC | #44

Come to think about it, I believe it would be worthwhile to rename the “libUrho3D.so” to “libUrho3D_shared.so”, i.e. using the same naming convention as the shared STL runtime lib.

EDIT: after finished making the necessary changes, I have a second thought on this and decided not to commit it. Although I could simplify to remove a pair of Regex with normal string comparison on the Kotlin/JVM side, the changes would slightly complicate things on the CMake side in order to get the desired library output name.

-------------------------

weitjong | 2018-08-17 10:04:20 UTC | #45

[quote="Miegamicis, post:42, topic:4380"]
Also is there any way how I can reduce the build directory size?
[/quote]

There will be one more way to reduce the APK size for testing, if I have carried out my full plan. I have chosen to setup a multi-modules Gradle build for a few reasons. I have not mentioned it in the https://github.com/urho3d/Urho3D/issues/743 because at that time I was not even sure I could finish the initial work. One of the reason is to be able to have each sample being setup as a module in itself. I imagine user can just choose one of many sample apps in the IDE and be able to build and run the individual APK. This will be similar to how iOS sample apps are being setup currently.

-------------------------

Bluemoon | 2018-08-17 10:52:48 UTC | #46

I named my directory path as short as can be but still it complains that the command line is too long. I ask, won't it be better to break the long command into size-able ones since, as I noticed, that its just a concatenation of commands. Or is there a reason why it must be a whole monolithic chunk.

-------------------------

weitjong | 2018-08-17 12:45:07 UTC | #47

Sorry to hear that. What is the fully qualified path to Urho3D project in your system and what is the path to Android SDK?

When using CMake, we don't have the full control of what would be generated by its generator. We can only influence the outcome by configuring some CMake variables, and one of them is to tell it to generate all the command arguments into external response files. But we have already discussed that. There are no other ways I could think of, aside from disabling the IK subsystem if that is the only lib that caused your issue or just graduate from PC and move on to Mac or something better.

-------------------------

Bluemoon | 2018-08-17 13:06:51 UTC | #48

Fully qualified path to Urho3D project on my system is

> C:\U

and that of my Android SDK is
>C:\aSDK

I had to make them as short as possible :expressionless:

-------------------------

weitjong | 2018-08-17 13:10:31 UTC | #49

Then it is beyond saving... :slight_smile:
Still wondering how my Windows 7 can survive it though. I only disable Lua subsystem, the rest is as per default. And my project path and SDK path are way longer.

-------------------------

Bluemoon | 2018-08-17 13:22:23 UTC | #50

[quote="weitjong, post:49, topic:4380"]
Then it is beyond saving
[/quote]

:joy:

Can you tell me the exact config file that ninja uses, I'll like to make some tweaking locally to see if it can work for me

-------------------------

weitjong | 2018-08-18 04:03:47 UTC | #51

There is no specific config file for ninja, but you can get the inspiration from here to tweak some CMake variables.

https://github.com/urho3d/Urho3D/blob/70049ba58210ad26d8402363cf4d864f6c294155/CMake/Toolchains/Emscripten.cmake#L165-L173

Copy those lines and modify them as necessary to a top level CMakeLists.txt or UrhoCommon.cmake. Change the condition to become `if (ANDROID AND CMAKE_HOST_WIN32)` or something like that. Good luck.

-------------------------

elix22 | 2018-08-19 20:19:52 UTC | #52

I compiled it successfully on my MacBook Pro (armeabi-v7a  only ) .
Installed  it successfully on one of my low-cost Android devices.

Launcher 
C++ -  crashed for every second example (start first example successful , press back , start second example crashed)
AngelScript - works fine , switching successfully between the examples
Lua - works fine  , switching successfully between the examples

[weitjong](/u/weitjong) thank you for your time and contribution making the build system up to date .

I will try to debug the C++ examples crash issue during the weekend.

Thanks

-------------------------

weitjong | 2018-08-20 00:40:25 UTC | #54

Did you use STATIC or SHARED lib type? I have only tried SHARED during my testing and the launcher works fine in both an AVD and a real device.

-------------------------

elix22 | 2018-08-20 05:31:00 UTC | #55

STATIC , real device , Android version 4.4.4
I will collect some logs during the week , once I will have some spare time

-------------------------

elix22 | 2018-08-20 05:57:57 UTC | #56

I had some time now , before going to work.
Built the shared version (libUrho3D.so)  , everything works with no crashing.

SHARED library type , real device , Android version 4.4.4
===========================================
C++ -  works fine , switching successfully between the examples
AngelScript - works fine , switching successfully between the examples
Lua - works fine , switching successfully between the examples

STATIC library type , real device , Android version 4.4.4
==========================================
C++ - crashed for every second example (start first example successful , press back , start second example crashed)
AngelScript - works fine , switching successfully between the examples
Lua - works fine , switching successfully between the examples

-------------------------

weitjong | 2018-08-30 13:47:14 UTC | #57

Any update on the debug log or stack trace on the crash? I haven't got time to reproduce this myself. I am more interested to spend my free time in getting the build script works for downstream project in one form or another, perhaps by creating a custom Gradle plugin.

-------------------------

elix22 | 2018-08-30 14:58:57 UTC | #58

Sorry  , so far  I didn't have much time to debug it thoroughly , can't  find the spare time  .

I verified it  on additional 3 real devices  running Android Marshmallow , Nougat and Pie.
Reproducible 100%

I cherry picked some logs (starting an example , pressing back , starting example)

# Running  script examples  , doesn't crash

**05-29 11:00:02.895  4899  4899 V SDL     : onCreate(): com.github.urho3d.launcher**
**05-29 11:00:03.038  4899  4899 V SDL     : nativeSetupJNI(): com.github.urho3d.launcher**
**05-29 11:00:03.392  4899  5230 V SDL     : Running main function SDL_main from library libUrho3DPlayer.so: com.github.urho3d.launcher**
**05-29 11:00:08.405  4899  4899 V SDL     : onDestroy(): com.github.urho3d.launcher**
**05-29 11:00:08.406  4899  4899 V SDL     : nativeQuit(): com.github.urho3d.launcher**
** **
**05-29 11:00:13.801  4899  4899 V SDL     : onCreate(): com.github.urho3d.launcher**
**05-29 11:00:13.812  4899  4899 V SDL     : nativeSetupJNI(): com.github.urho3d.launcher**
**05-29 11:00:13.966  4899  5308 V SDL     : Running main function SDL_main from library libUrho3DPlayer.so: com.github.urho3d.launcher**
**05-29 11:00:19.941  4899  4899 V SDL     : onDestroy(): com.github.urho3d.launcher**
**05-29 11:00:19.941  4899  4899 V SDL     : nativeQuit(): com.github.urho3d.launcher**

# STATIC library type , 100% crash on the second example 

**05-29 10:52:02.564  4229  4229 V SDL     : onCreate(): com.github.urho3d.launcher**
**05-29 10:52:02.623  4229  4229 V SDL     : nativeSetupJNI(): com.github.urho3d.launcher**
**05-29 10:52:02.870  4229  4295 V SDL     : Running main function SDL_main from library lib06_SkeletalAnimation.so: com.github.urho3d.launcher**
**05-29 10:52:14.550  4229  4229 V SDL     : onDestroy(): com.github.urho3d.launcher**
**05-29 10:52:14.550  4229  4229 V SDL     : nativeQuit(): com.github.urho3d.launcher**

** **
**05-29 10:52:16.661  4229  4229 V SDL     : onCreate(): com.github.urho3d.launcher**
**05-29 10:52:16.738  4229  4229 V SDL     : nativeSetupJNI(): com.github.urho3d.launcher**
**05-29 10:52:16.954  4229  4363 V SDL     : Running main function SDL_main from library lib07_Billboards.so: com.github.urho3d.launcher**
**05-29 10:52:16.954  4229  4363 V SDL     : nativeRunMain(): com.github.urho3d.launcher**
**05-29 10:52:16.962  4229  4363 E Urho3D  : Failed to initialise SDL: Application didn't initialize properly, did you include SDL_main.h in the file containing your main() function?: com.github.urho3d.launcher**
**05-29 10:52:16.962  4229  4363 E Urho3D  : Failed to initialise SDL subsystem: Application didn't initialize properly, did you include SDL_main.h in the file containing your main() function?: com.github.urho3d.launcher**
**05-29 10:52:16.998  4229  4229 V SDL     : onWindowFocusChanged(): true: com.github.urho3d.launcher**
**05-29 10:52:17.037  4229  4363 F urho3d.launche: java_vm_ext.cc:542]     from int org.libsdl.app.SDLActivity.nativeRunMain(java.lang.String, java.lang.String, java.lang.Object): com.github.urho3d.launcher**
**05-29 10:52:17.037  4229  4363 F urho3d.launche: java_vm_ext.cc:542] "SDLThread" prio=5 tid=16 Runnable: com.github.urho3d.launcher**
**05-29 10:52:17.037  4229  4363 F urho3d.launche: java_vm_ext.cc:542]   native: #12 pc 005172b3  /data/app/com.github.urho3d.launcher-JdHf8rw-C4QWZI0dx2k58g==/lib/arm/lib07_Billboards.so (SDL_AndroidGetInternalStoragePath+110): com.github.urho3d.launcher**
**05-29 10:52:17.037  4229  4363 F urho3d.launche: java_vm_ext.cc:542]   native: #13 pc 00512c8f  /data/app/com.github.urho3d.launcher-JdHf8rw-C4QWZI0dx2k58g==/lib/arm/lib07_Billboards.so (SDL_GetPrefPath+18): com.github.urho3d.launcher**
**05-29 10:52:17.037  4229  4363 F urho3d.launche: java_vm_ext.cc:542]   native: #18 pc 00324155  /data/app/com.github.urho3d.launcher-JdHf8rw-C4QWZI0dx2k58g==/lib/arm/lib07_Billboards.so (SDL_main+28): com.github.urho3d.launcher**
**05-29 10:52:17.038  4229  4363 F urho3d.launche: java_vm_ext.cc:542]   native: #19 pc 00517035  /data/app/com.github.urho3d.launcher-JdHf8rw-C4QWZI0dx2k58g==/lib/arm/lib06_SkeletalAnimation.so (Java_org_libsdl_app_SDLActivity_nativeRunMain+1028): com.github.urho3d.launcher**
**05-29 10:52:17.038  4229  4363 F urho3d.launche: java_vm_ext.cc:542]   native: #20 pc 00006411  /data/app/com.github.urho3d.launcher-JdHf8rw-C4QWZI0dx2k58g==/oat/arm/base.odex (offset 6000) (org.libsdl.app.SDLActivity.nativeRunMain+160): com.github.urho3d.launcher**
**05-29 10:52:17.038  4229  4363 F urho3d.launche: java_vm_ext.cc:542]   native: #28 pc 0007f2d8  /data/app/com.github.urho3d.launcher-JdHf8rw-C4QWZI0dx2k58g==/oat/arm/base.vdex (org.libsdl.app.SDLMain.run+96): com.github.urho3d.launcher**
**05-29 10:52:17.038  4229  4363 F urho3d.launche: java_vm_ext.cc:542]   at org.libsdl.app.SDLActivity.nativeRunMain(Native method): com.github.urho3d.launcher**
**05-29 10:52:17.038  4229  4363 F urho3d.launche: java_vm_ext.cc:542]   at org.libsdl.app.SDLMain.run(SDLActivity.java:1004): com.github.urho3d.launcher**
**05-29 10:52:17.214  4229  4363 F urho3d.launche: runtime.cc:558] "SDLThread" prio=5 tid=16 Runnable: com.github.urho3d.launcher**
**05-29 10:52:17.214  4229  4363 F urho3d.launche: runtime.cc:558]   native: #17 pc 005172b3  /data/app/com.github.urho3d.launcher-JdHf8rw-C4QWZI0dx2k58g==/lib/arm/lib07_Billboards.so (SDL_AndroidGetInternalStoragePath+110): com.github.urho3d.launcher**
**05-29 10:52:17.214  4229  4363 F urho3d.launche: runtime.cc:558]   native: #18 pc 00512c8f  /data/app/com.github.urho3d.launcher-JdHf8rw-C4QWZI0dx2k58g==/lib/arm/lib07_Billboards.so (SDL_GetPrefPath+18): com.github.urho3d.launcher**
**05-29 10:52:17.214  4229  4363 F urho3d.launche: runtime.cc:558]   native: #23 pc 00324155  /data/app/com.github.urho3d.launcher-JdHf8rw-C4QWZI0dx2k58g==/lib/arm/lib07_Billboards.so (SDL_main+28): com.github.urho3d.launcher**
**05-29 10:52:17.214  4229  4363 F urho3d.launche: runtime.cc:558]   native: #24 pc 00517035  /data/app/com.github.urho3d.launcher-JdHf8rw-C4QWZI0dx2k58g==/lib/arm/lib06_SkeletalAnimation.so (Java_org_libsdl_app_SDLActivity_nativeRunMain+1028): com.github.urho3d.launcher**
**05-29 10:52:17.214  4229  4363 F urho3d.launche: runtime.cc:558]   at org.libsdl.app.SDLActivity.nativeRunMain(Native method): com.github.urho3d.launcher**
**05-29 10:52:17.214  4229  4363 F urho3d.launche: runtime.cc:558]   at org.libsdl.app.SDLMain.run(SDLActivity.java:1004): com.github.urho3d.launcher**

-------------------------

tni711 | 2018-09-05 18:10:49 UTC | #59

Hi,

I tested the new gradle build in my Ubuntu 16.04 machine. It works quite well except a few issues / questions I have. Maybe specific to my machine setup and configuration though.

1. java heap out of memory error
I got java heapspace out of memory exception. The problem is gone after I increased the heap size to 8G in the gradle.properties file.

2. ccache permission error.
I got ccache permission error as my g++ during the initial build process. The issue is caused by improper setup oft he ccache. The which g++ command shows the g++ is pointed to /usr/bin/g++ instead of /usr/lib/ccache/g++. Resolved the issue after fixing this help (https://askubuntu.com/questions/470545/how-do-i-set-up-ccache)

2. The build process took quite a while (maybe my machine is not that fast). It seems the build process compile the source files multiple times. Is it correct it has to do with the number of android API installed in the system, meaning each file will be compiled for each API level?

3. At the end, I am able to deploy all the launcher with all sample applications to my Nexus 7 device. The issue I have here is, the apks created are quite big (the debug apk is around 1.35G)
and take a while to deploy to the device. 
How do I deploy my application only in this new process? I basically added my application as a new application in the samples folder and re-use everything for building the app.

4. Intermittent runtime exception when launching a sample application in the android device. It seems this problem apply for all sample applications. The application can run successfully the second time you launch it though.

-------------------------

weitjong | 2018-09-06 14:13:53 UTC | #60

Thanks for the feedback. As you aware our Gradle build system is still very new and still in active development in the master branch, you should expect things not working and things being drastically changed during the process. So at this moment, I actually do not recommend it to be used for your own project just yet, unless you are a technically inclined person. I will try to address/answer your issues/questions below though.

[quote="tni711, post:59, topic:4380"]
java heap out of memory error
I got java heapspace out of memory exception. The problem is gone after I increased the heap size to 8G in the gradle.properties file.
[/quote]

Initially when I started the development of this new Gradle build system, I also had a memory issue. But it was caused by my host system memory really not having enough RAM. After upgrading from 8GB to 16GB then I have not encountered any memory issues again. I notice that Android Studio (or IntelliJ IDEA) is quite a memory hog by itself, so for those who don't have enough RAM then trying the Gradle build system using CLI may be a better option. The Travis-CI has a low CPU and memory specs and yet it runs our Gradle build system just fine with the default JVM heap size.

[quote="tni711, post:59, topic:4380"]
ccache permission error.
I got ccache permission error as my g++ during the initial build process. The issue is caused by improper setup oft he ccache. The which g++ command shows the g++ is pointed to /usr/bin/g++ instead of /usr/lib/ccache/g++. Resolved the issue after fixing this help 
[/quote]

This is a common pitfall for Ubuntu distro. Fedora, the distro that I use, will setup the PATH environment variable correctly after the `ccache` package is installed. You probably need the following line as well as in our CI (which also uses Ubuntu) to fix the mistake of the Ubuntu `ccache` package.

https://github.com/urho3d/Urho3D/blob/0f01ee7ccc283924906651abdbb81ae70eb149ca/.travis.yml#L341

[quote="tni711, post:59, topic:4380"]
The build process took quite a while (maybe my machine is not that fast). It seems the build process compile the source files multiple times. Is it correct it has to do with the number of android API installed in the system, meaning each file will be compiled for each API level?
[/quote]

No, it is not due to the API level. By default the Android plugin for Gradle will build for 4 ABIs (x86, x86_64, armeabi-v7a, and arm64-v8a) and it will also build for 2 build-configs (Debug and Release). Thus, by default there will be 8 build trees being generated. You can, however, limit the number of ABIs by specifying the `ANDROID_ABI` property. See the documentation for more detail:

https://urho3d.github.io/documentation/HEAD/_building.html#Building_Android

[quote="tni711, post:59, topic:4380"]
At the end, I am able to deploy all the launcher with all sample applications to my Nexus 7 device. The issue I have here is, the apks created are quite big (the debug apk is around 1.35G)
and take a while to deploy to the device.
[/quote]

By default our build system uses STATIC library type. This has been discussed and commented before in this thread so I won't repeat myself again. If you want smaller APK size, use the SHARED library type; OR don't build the sample at all (URHO3D_SAMPLES=0) and just keep the URHO3D_PLAYER=1, so the launcher only contains the Urho3DPlayer app which is more than enough to demonstrate the launcher capability for playing the AngelScript and Lua scripts.

[quote="tni711, post:59, topic:4380"]
How do I deploy my application only in this new process? I basically added my application as a new application in the samples folder and re-use everything for building the app.
[/quote]

The build system is not designed to be used in this way.

[quote="tni711, post:59, topic:4380"]
Intermittent runtime exception when launching a sample application in the android device. It seems this problem apply for all sample applications. The application can run successfully the second time you launch it though.
[/quote]

This is a known issue and has been reported by @elix22. I/we don't have time to debug it yet. You are welcome to contribute the fix.

-------------------------

tni711 | 2018-09-06 14:34:16 UTC | #61

Hi, thank you for the clear and detail responses to all my questions. Fully understood this new build process is quite complex and would take time to streamline. I think it is pretty smooth already at this stage. It is almost a one tick process from start to complete :slight_smile:
I don't have much experience in Android platform but if I find something I can contribute in the future, I definitely will.  Thank you again.

-------------------------

weitjong | 2018-09-08 13:58:07 UTC | #62

Minor update: just figured out how to do away with the global installation of "ninja-build" prerequisite. Now the build system will use the embedded CMake and the embedded Ninja (as provided by Android SDK/NDK) to build Android modules as well as host tools. This should make build with Lua/LuaJIT enabled easier.

-------------------------

weitjong | 2018-09-11 14:12:42 UTC | #63

[quote="weitjong, post:51, topic:4380"]
There is no specific config file for ninja, but you can get the inspiration from here to tweak some CMake variables.

https://github.com/urho3d/Urho3D/blob/70049ba58210ad26d8402363cf4d864f6c294155/CMake/Toolchains/Emscripten.cmake#L165-L173

Copy those lines and modify them as necessary to a top level CMakeLists.txt or UrhoCommon.cmake. Change the condition to become `if (ANDROID AND CMAKE_HOST_WIN32)` or something like that. Good luck.
[/quote]

I find out something interesting regarding Ninja on Windows host system. It seems to me that it automatically does the right thing already, i.e. using the response file if and only if it is needed. This is so even without setting the above CMake variables. At least this is what I observed in my Win7 VM, which BTW explains why I have no issue at all with the new build system. The response file is used when linking SLikeNet, WebP, Bullet, and Urho3D (if it is STATIC lib type) and not used for all the other 3rd-party STATIC libs. Having said that, I am not sure why the other Windows user(s) had issue though. Anyway, I am done wasting my time with my Win7 for now.

-------------------------

rku | 2018-09-21 08:01:49 UTC | #64

Hey @weitjong hows android build system work going? Is it stable enough to start using it?

P.S. I noticed `Android` was renamed to `android` and some other dirs with first letter being lower-case introduced. Most of project dirs follow convention of first letter being upper-case. Things are a bit inconsistent.

-------------------------

weitjong | 2018-09-21 14:48:01 UTC | #65

No. I haven’t found time to continue the plugin development. And also partly because I got  distracted by dockerizing the build environment.

Good that you notice it. I intend to gradually  turn all dir names to lower case. It will take time though. So the new dir names are using that convention already. Don’t think it’s important to say it out loud.

-------------------------

slapin | 2018-09-21 23:23:45 UTC | #66

Will you share your Dockerfile and scripts?

-------------------------

weitjong | 2018-09-22 02:19:46 UTC | #67

[quote="slapin, post:66, topic:4380, full:true"]
Will you share your Dockerfile and scripts?
[/quote]

This is off-topic now, but the answer is yes.

-------------------------

dertom | 2018-09-30 09:57:05 UTC | #68

I'm trying to compile my application alongside the samples. My app is basically a modified Sample and also resides in the Sample-Folder. (Compiling on desktop(linux) works as intended). Any hint how to tell urho3d-gradle to compile this as well would be very appreciated. 

Looking in [urho3d]/android/launcher-app/build.gradle.kts where cmake is configured, it looks like "URHO3D_SAMPLES" are activated as expected but my app is ignored and no shared-lib is created. 

I made a gradlew clean and build with ./gradlew -PANDROID_ABI=armeabi-v7a build

EDIT: oh man,...seems like 'gradlew clean' was not enough. I removed the whole 'android/launcher-app/build'-folder which seems to make the job. I guess 'gradlew clean' did not clear cmake's build-releated files....

-------------------------

weitjong | 2018-09-30 10:38:46 UTC | #69

Initially the “clean” task was customized to delete the CMake build tree as well, but that customization is later changed to just make sure CMake re-run will take place (instead of a full regeneration) for speed/performance reason. In any case, your approach is not the intended use case of the new Android build system. Stay tune for a proper support in the near future.

-------------------------

tni711 | 2018-09-30 13:50:03 UTC | #70

I have a similar setup and have no problem building for android debug mode so far.

Maybe you can try the build sequence below while waiting. This approach assume you a android device connected your machine:

1. cd to the Urho3D directory.
2. ./gradlew build
3. ./gradlew assembleDebug
4. ./gradew installDebug.

I have tested this with current master version with my Nexus 7 and Samsung Notes4 devices. It works quite consistent so far and faster than using Android Studio.

-------------------------

dertom | 2018-09-30 16:20:31 UTC | #71

Yes, it worked as soon as I deleted the whole build-folder as the gradle cmake did not detect that there is a new sample folder that needed to be taken into account (see my EDIT-section). Thx for your hint. Those install commands will become handy...

-------------------------

weiyuemin | 2018-11-08 14:56:15 UTC | #72

Hi, I'm on Win7, I'm new to android development, maybe a silly question..

when I run 

gradlew build -PANDROID_ABI=armeabi-v7a -PURHO3D_LIB_TYPE=SHARED

it successfully produce a launcher-app-armeabi-v7a-debug.apk in android\launcher-app\build\outputs\apk\debug\

but it's only 7623k, I guess the assets are not in the apk. i do copy the CoreData folder to android\urho3d-lib\, and copy Autoload and Data folder to android\launcher-app, but it seems not taking effect.

am i miss something?

Thank you!

-------------------------

weitjong | 2018-11-08 15:56:11 UTC | #73

This is the first report I received (not counting myself) that the new Gradle build system works for Windows 7 without hitting cmd.exe buffer length issue. Good job.

For the asset dir preparation, make sure you copy them while preserving the sub-directory structure. That is, inside the "assets" dir, there is a sub-dir called "CoreData" and so on. Below just the illustration from my Linux system. Good luck.

```
[weitjong@igloo android]$ pwd
/home/weitjong/ClionProjects/urho3d/Urho3D/android
[weitjong@igloo android]$ ls -ltr urho3d-lib/src/main/assets/
total 0
lrwxrwxrwx. 1 weitjong weitjong 27 Aug 22 18:00 CoreData -> ../../../../../bin/CoreData
[weitjong@igloo android]$ ls -ltr launcher-app/src/main/assets/
total 0
lrwxrwxrwx. 1 weitjong weitjong 23 Aug 22 18:00 Data -> ../../../../../bin/Data
lrwxrwxrwx. 1 weitjong weitjong 27 Aug 22 18:00 Autoload -> ../../../../../bin/Autoload
```

-------------------------

weiyuemin | 2018-11-09 01:07:43 UTC | #74

Thank you! it works for me, I missed the 'src/main/assets' part before. 
after using mklink to create directory link and removing all '*_assets' like folders in build/intermediates, it successfully produce a 5x M apk and runs well.

-------------------------

weitjong | 2019-05-02 01:02:01 UTC | #75

Almost one year has passed since i first started this and I think I may have learnt enough of Gradle this time round to configure a source set with custom asset dir without using symlink. I will try that later tonight.

-------------------------

weitjong | 2019-05-04 05:34:48 UTC | #76

I have wasted some time on this (again). It appears the include/exclude of `srcDir` does not take any effect at all. After some searching it looks like I have hit the same bug as reported in this [issue on Google issue tracker](https://issuetracker.google.com/issues/36988285) since 2014!

-------------------------

Pencheff | 2019-05-04 13:05:19 UTC | #77

I also spent some nerves on this, I didn't find anything good. I'm currently copying assets from Urho3D to my bin directory and then this:
[code]
buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
            signingConfig signingConfigs.config
            sourceSets {
                main {
                    // TODO: find a better way to copy assets from cmake build folder
                    assets.srcDirs = ['.externalNativeBuild/cmake/release/armeabi-v7a/bin']
                }
            }
        }
        debug {
            debuggable true
            sourceSets {
                main {
                    // TODO: find a better way to copy assets from cmake build folder
                    assets.srcDirs = ['.externalNativeBuild/cmake/release/armeabi-v7a/bin']
                }
            }
        }
    }
[/code]

-------------------------

weitjong | 2019-05-04 14:50:52 UTC | #78

Exactly that is what I want to avoid, another *copy* task. When I could not get the exclude/include filter works the last time, the symlink/mklink is the next best thing that I chose to use.

-------------------------

