slapin | 2017-03-02 20:23:36 UTC | #1

Hi, all!

Have anybody scripted your build of Urho project for Android?
I'd like to see your scripts, as I want to script builds for Linux and Android under Jenkins.
I have implemented build for Linux so far, but I want to get builds for ARM cross-compilation
working (on Allwinner-based armbian). Then I want to build for android, and I hope somebody
did this before.

Thanks a lot!

-------------------------

rku | 2017-03-03 08:12:16 UTC | #2

https://urho3d.github.io/documentation/1.6/_building.html#Building_Android

-------------------------

johnnycable | 2017-03-03 09:38:06 UTC | #3

Not yet, but I'll be trying next days. The Urho3d android way proposed does not suit with android studio, and that's to be addressed!

-------------------------

rku | 2017-03-03 12:24:06 UTC | #4

I looked using android studio with urho3d just yesterday. Android studio does not support cmake therefore it is not really usable with urho3d. However i had no issues setting up android build in clion which even sends built apk to phone. The only missing part is debugging apk on the phone or emulator via remote gdb, but i am pretty sure it is doable.

-------------------------

johnnycable | 2017-03-03 15:27:54 UTC | #5

Wait, android studio officially supports cmake for native. It's the default build system now. Maybe you are using and old ndk?

-------------------------

rku | 2017-03-03 18:36:20 UTC | #6

Im using android-ndk-r11b and android studio 2.2.3. I open folder with cmake project but IDE does not pick it up somehow. What versions are you using?

-------------------------

johnnycable | 2017-03-03 22:54:59 UTC | #7

I'm using r12b. Have you looked at this? https://developer.android.com/ndk/guides/cmake.html

-------------------------

rku | 2017-03-04 08:04:34 UTC | #8

That page explains it:

> creating a CMake build script, and adding your CMake project **as a Gradle dependency**.

Urho3D is using ant for android builds. Guess we would have to improve android part of build system, but that can only be done when @weitjong merges his build refactor branch. Until then i dont think heavy build system contributions would be accepted.

-------------------------

weitjong | 2017-03-04 08:55:14 UTC | #9

I don't think there is any real dependency here. If anyone want to take a shot at this, please do.

We have actually talked about migrating the Ant build to Gradle build in [GitHub issue #743 ](https://github.com/urho3d/Urho3D/issues/743) about 2 years ago. Fortunately (or unfortunately) we managed to solve the issue at hand at the time. So, we/I didn't actually look into it afterward. Now, if I would have time to do that, I would probably migrate the build system to Gradle + migrate the Java code (that we maintain) to Kotlin. Once you have tasted them, it hard to go back to the old ways!

-------------------------

rku | 2017-03-04 09:29:41 UTC | #10

Migrating java to kotlin would be a mistake as kotlin is not the default language of android. Besides code amount is so small that there would be no gains, even maybe loss due o added confusion. More people are familiar with java and more resources exist on java.

-------------------------

weitjong | 2017-03-04 11:12:22 UTC | #11

This is getting off topic, but I believe your argument of rejecting Kotlin is moot.

-------------------------

weitjong | 2017-05-18 04:24:52 UTC | #12

https://techcrunch.com/2017/05/17/google-makes-kotlin-a-first-class-language-for-writing-android-apps/

-------------------------

johnnycable | 2017-05-18 12:17:49 UTC | #13

Expect Google to buy Jetbrains soon...

-------------------------

