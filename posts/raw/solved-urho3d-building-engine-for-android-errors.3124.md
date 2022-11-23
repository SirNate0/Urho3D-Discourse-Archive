halcyonx | 2017-05-15 19:50:13 UTC | #1

Hi, everyone! I spend some days trying to build Urho3D engine for android, I use this instructions but can't build engine
It seems guide from official site is deprecated, because 
> - android update project -p . -t <target-id> // - this does not work! android.bat says it deprecated tool
> - make -j <num_jobs>
> - ant debug
Log:
[spoiler]C:\Android>android update project -p . -t 1
**************************************************************************
The "android" command is deprecated.
For manual SDK, AVD, and project management, please use Android Studio.
For command-line tools, use tools\bin\sdkmanager.bat
and tools\bin\avdmanager.bat
**************************************************************************

Invalid or unsupported command "update project -p . -t 1"

Supported commands are:
android list target
android list avd
android list device
android create avd
android move avd
android delete avd
android list sdk
android update sdk[/spoiler]
Also I installed latest tools for android development with Urho3D: android-ndk-r14b, gradle-3.5, apache-ant-1.9.9, and android command line tool with sdkmanager.
I set my enviroment variables ANDROID_NDK and ANDROID_SDK, also Path, according with this instructions: https://urho3d.prophpbb.com/topic2026.html, but it seems also deprecated.

Then I use command: cmake_android AndroidBuild -DURHO3D_SAMPLES=1, runs cmake, there is some warnings and messages like this:
`-- Looking for malloc_usable_size - not found`
and 2 fails:
`-- Performing Test HAVE_PTHREAD_NP_H - Failed` 
Full cmake log in to of log in link below to pastebin (cant attach 2 link to post)

Finally, then I change directory to AndroidBuild, and run make, it starts normally building, but finally fails with compilation errors: https://pastebin.com/HBj8Nbb2
Why? How can I solve this problem?

-------------------------

weitjong | 2017-05-14 02:02:53 UTC | #2

During CMake initial run to generate the build tree, it is normal to see output that says this and that were not found or not passed the test, even when you have Android NDK properly installed (I think you have). During build time, you should not get any errors however. If you do then it means you have done something wrong at the early steps. Most probably you have tried too much but forgot to nuke everything clean before retrying. Try delete your build tree first and start from scratch again. For that reason we recommend to use separate directory for build tree, so user can easily delete the dir without affecting the source tree, or have multiple build trees during experimentation without interference from one another. 

After you get all the *.so built, only then you need the Android SDK to package them into apk. It is true that our documentation and, in fact, also our build system still does not adapt to the latest SDK. The easiest way to fix the deprecated issue is to downgrade the "build tool" component, just this component should do, leave the others to their latest. Alternatively search the forum here to see how other users workaround it by using Android Studio and Gradle.

-------------------------

halcyonx | 2017-05-14 04:24:12 UTC | #3

1. There is a way to know what version of Android SDK and Android NDK uses by Urho3D. may be in some configure files?
2. If I run make -j without N arguments it runs too many jobs, is it should build correct?

-------------------------

weitjong | 2017-05-14 05:37:37 UTC | #4

Your first question is kind of misleading. Urho3D library does not actually tie to a specific Android SDK or NDK version, but in general the latest is always the better. In the master branch we have rewritten our Android/CMake toolchain file from scratch to remove all the legacy burden so the new toolchain file only works from NDK 12b onward. However, if you want to use old NDK version for any reason then you can still do so but you have to grab the old copy of toolchain file and use that instead (Urho3D release 1.6 still uses the old toolchain file). Similarly for the Android SDK, it is almost certain the latest version is the best, barring the "android update project" sub-command issue, especially when you want to target newer Android devices. Use the "android sdk" GUI to downgrade the "build tool" to lower version (I am using 25.02) which still provide that sub-command. It is not the end of world issue. You can use Gradle script to update the Android manifest XML file or even just update that file manually to use the min/target SDK version and move on.

make -j without N argument simply tells make to spawn without limit. I have no idea why they have that option :) . You probably want to put a number closer to the number of your CPU physical cores or logical cores if your CPU supports hyperthreading.

-------------------------

artgolf1000 | 2017-05-14 23:39:41 UTC | #5

[spoiler]Your issue was caused by the NDK version, try downgrading to android-ndk-r12b[/spoiler].
Another solution is to use Android Studio to build your project:[https://discourse.urho3d.io/t/android-studio-2-3-build-with-gradle/2995/14](https://discourse.urho3d.io/t/android-studio-2-3-build-with-gradle/2995/14)
Edited: **It is the build tool version to be downgraded, not the NDK, I forgot it.**

-------------------------

halcyonx | 2017-05-14 14:32:28 UTC | #6

Oh, Yeah! I did this, I cleaned Urho3D directory, I removed dirs lib/, include/. This dirs was created at previous then I built Urho3D for Visual Studio 14 configuration. Now I used Cmake GUI for configuring and generation project, after that `make` done work clearly.
Btw, I didnot downgrade Android NDK, I downgrade Android SDK for correct work `android` and gradle from 3.5 -> 2.2.
Now it works!

Now I have the question. If I want to develop project in Visual Studio and test it on Windows environment and on my android device, I must create 2 independent folders for windows project and another for android? And then I want to run my project on android device I should copy sources of my code from win folder to android and rebuild this?

-------------------------

weitjong | 2017-05-14 14:57:09 UTC | #7

Glad to hear that.

No, you don't need to downgrade the Android NDK. You actually also do not need to downgrade the whole Android SDK but just the build-tool component, but I guess it is not important now.

And as for your last question. Don't do that. I mentioned about the source tree and build tree(s) for Urho3D project earlier. The same concept should be applied for your own project as well. Keep all your sources in a single source tree. Then use CMake to generate multiple build trees from it, i.e. one build tree for each  target platform.

-------------------------

halcyonx | 2017-05-14 15:51:12 UTC | #8

weitjong, thank you so much! Your advices really helped me. 

Also I want to ask about android develepment workflow. I run Cmake with specified the generator "Unix Makefiles" and chosen "Specify toolchain file for cross-compiling" after that I specify "C:/projects/Engine/Urho3D/CMake/Toolchains/Android.cmake" as toolchain. After configuring and generation, in my worktree appeared dir "Android\libs\armeabi-v7a\libTestedProject.so" I copied to near files:
Urho3D\libs\armeabi-v7a\libUrho3D.a 
Urho3D\libs\armeabi-v7a\libUrho3DPlayer.so 
// 1. Should I do this manually?

Also in my android project dir there is no AndroidManifest.xml and build.xml, why? Should I use `android` tool for create this manifests and other things?

After that I copied AndroidManifest.xml, build.xml, custom_rules.xml, project.properties from Urho3D\Android to my android project dir, after this I built it and my little sample runned on my device, but it still knows as `com.github.urho3d`.

I'm interested in the following: What is more `standard` development workflow with Urho3D for android? Should I use Android Studio in development, after all, mostly all the code in C++? Or android-sdk tools like android is enough for full project managment? Should I write my own java wrapper?

-------------------------

artgolf1000 | 2017-05-15 00:29:40 UTC | #9

Sorry for my wrong answer, I had forgotten the right answer.

I don't know what is the standard development workflow, the official way is the command line tools.

If you use Android Studio, just import the project generated with Urho3D(Of cause, you need to build the project with visual studio or unix style make tool to generate the shared library), Android Studio will automatically complete all java wrappers for you, you do not need to write any code, just click build and run, the app will be installed and run on your device or on the simulator.

I personally prefer Android Studio, I use it to wrap all the java side, and test the app on its various super fast simulators.

-------------------------

weitjong | 2017-05-15 02:17:11 UTC | #10

[quote="halcyonx, post:8, topic:3124"]
// 1. Should I do this manually?
[/quote]

No, you shouldn't. From the look of it, I believe you are building Urho3D as a STATIC lib. If so, your test target binary has already statically linked against it. In other words, all the necessary bits from the engine is already inside your test target. So, you are ready to go next step.

Currently our CMake-based build script does not know to generate the Android manifest file and other fixtures for new downstream project, so you have to prepare that yourself during your project scaffolding. Using Android Studio + Gradle may automate that. But like I said, we haven't updated our doc nor script to achieve that level of automation. Reusing manifest file from Urho3D project is not really what you want to do, as you have found out the hard way.

-------------------------

