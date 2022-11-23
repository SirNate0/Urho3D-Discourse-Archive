Bluemoon | 2020-01-12 16:38:47 UTC | #1

After successfully building urho3d for android, I noticed that the resultant files have an unusually large size. The samples each are roughly 70mb with Urho3D Player reaching 90mb. I though release build was the default build.

On close observation and searching through the build artifacts, I noticed that the clang++ build command for urho3d has **-g** in it which is actually meant for release build but with debug symbols embedded.

I would be glad if someone can give me a pointer(s) on what I'm meant to do

-------------------------

Pencheff | 2019-12-13 13:51:58 UTC | #2

Is Android Studio actually building Release configuration ? My whole APK is 35MB bundled with everything from CoreData/Data, my own libraries and bunch of third party libraries which alone are 10MB.

-------------------------

Bluemoon | 2019-12-13 14:08:20 UTC | #3

Wow, then there is definitely something wrong with my build. Though I actually run from the command line and below is what I type

> gradlew.bat -P URHO3D_ANGELSCRIPT=1 -P URHO3D_LUA=0 -P URHO3D_DATABASE_SQLITE=1 -P URHO3D_LIB_TYPE=STATIC -P URHO3D_SAMPLES=1 -P ANDROID_ABI=x86,armeabi-v7a,arm64-v8a assembleRelease

-------------------------

Pencheff | 2019-12-13 14:14:57 UTC | #4

Well, 70MB seems reasonable for 3 architectures you're targeting. What happens if you only build for armeabi-v7a for example ? 
You can use analyze apk files in Android Studio to figure out file sizes inside the apk.

-------------------------

jmiller | 2019-12-13 15:19:39 UTC | #5

Shared builds (URHO3D_LIB_TYPE=SHARED) should be much smaller and faster to link.

-------------------------

Bluemoon | 2019-12-13 17:59:31 UTC | #6

Sorry I didn't make myself clear enough... the 70mb is for the .so file not even for the .apk the size of the apk is on a whole new level.

So if your are to navigate to x86 ABI output directory you see all the samples .so file are roughly 70mb each :pensive: 
![post|690x398](upload://xJWRgzDymlWnma0ugAt9a4te5G2.png)

-------------------------

kakashidinho | 2020-01-12 16:38:37 UTC | #7

The intermediate .so file is generally larger than the .so that will be packaged inside apk. Android toolchain will strip debug symbols before putting it inside the final apk. Maybe you should check the size of apk to see whether it is smaller than 70MB for each arch or not

-------------------------

Bluemoon | 2019-12-14 06:12:32 UTC | #8

Thanks a lot @kakashidinho  this really explained what was almost driving me crazy.  I made a single standalone app with the generated libs for armeabi-v7a and as @Pencheff said I got an apk size of roughly 35MB. Adding x86 ABI to it increased it to 57MB which seems fair I guess.

What had actually deceived me in terms of the earlier apk file size was Autoload assets of urho3d that I included. When I removed it my apk file size drastically reduced.

Once more thanks a lot everyone

-------------------------

Bluemoon | 2020-01-07 12:24:44 UTC | #9

Sorry to raise this up again. I think I've seen what might **actually** be causing the files to be large and it does have to do with **-g** compiler option that is used in building on android. 
It turns out that the android NDK's `android.toolchain.cmake` sets **-g** as part of the compiler generic flag:

> list(APPEND ANDROID_COMPILER_FLAGS
  -g
  -DANDROID
  -fdata-sections
  -ffunction-sections
  -funwind-tables
  -fstack-protector-strong
  -no-canonical-prefixes)

Just to be sure, I removed **-g**, did a release build of Urho3D , and just as expected the size of the output files ( .so binaries and libUrho3D.a ) were reduced by more than 50% and still worked well.

So it's apparent that the current android built injects debug symbol regardless of the selected build type.

-------------------------

weitjong | 2020-01-08 14:55:21 UTC | #10

You only tell half of the story. The `android.toolchain.cmake` also setup the `strip` command which does exactly the reverse. It is my understanding that Google provided Android plugin for Gradle will invoke the `strip` command at some point to remove the debugging symbols for Release build. The stocked plugin and the cmake toolchain file go together. Although I haven't checked it up specifically, but I will be really surprise if it is true that "they" forget to issue the strip command at all and no one else realizes it until now.

-------------------------

Bluemoon | 2020-01-08 16:15:39 UTC | #11

There is a very high chance that you are right, however it seems the `strip` command does not remove all the debugging symbols. I have two android release builds of libUrho3D.a both of them for armeabi-v7a. That which had the un-altered `android.toolchain.cmake` is 162mb in size whereas the one that **-g** was  removed from its `android.toolchain.cmake`  is 47mb.

-------------------------

weitjong | 2020-01-08 17:19:56 UTC | #12

Are you building a released APK? The *.a file is not included in the APK right?

-------------------------

Bluemoon | 2020-01-08 18:01:39 UTC | #13

Yes the builds are release build, and no the *.a file is not included in the apk. 

I even did a size comparison between two apk of the same code but linked to the two different cases of release build i.e with and without -g flag in the android toolchain. Below is the size observations

> **default android.toolchain.cmake**
> output *.so file: 60.5mb
> final apk file: 35.1mb
>
> **modified android.toolchain.cmake ( -g flag removed)**
> output *.so file: 10.5mb
> final apk file: 20.3mb

**side note**: I'm actually not having any issue with this (at least for now). The size difference is just an observation I thought of bringing up.

-------------------------

weitjong | 2020-01-09 15:27:23 UTC | #14

I reckon your observation is made using Windows host system. I wonder does the Linux or Mac host systems also has similar problem?

@Bluemoon Have you tried to extract the APK and double check all the *.so to see if they are actually stripped? Not sure how to do that on Windows but on Linux we can use "file" command to check that easily.

-------------------------

Bluemoon | 2020-01-12 16:38:37 UTC | #15

I rebuilt using the default `android.toolchain.cmake` , unzipped the generated apk for launcher app and noticed that the *.so files where indeed stripped.

Later found out the problem was from my end. I actually use a custom command line based build pipeline ( no gradle) which enables me use VS Code for urho3d apps development for android instead of android studio. Unfortunately this custom pipeline does not strip the *.so files.

I'll get that fixed.

Thanks for your assistance.

-------------------------

