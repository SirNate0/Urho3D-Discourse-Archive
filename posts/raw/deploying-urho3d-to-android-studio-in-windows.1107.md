Lumak | 2017-11-25 19:11:33 UTC | #1

This is my first post. After spending a few days on learning Urho3D and its build process, Android Studio SDK, Android NDK, and other tools required to build and deploy to Android platform (emulators and devices) in Windows, I found all of it a bit over whelming and thought I should share my easy steps taken to do this and hope that this information can help others.  Disclaimer, I am new to Urho3D and Android (mobile development in general) and Android Studio SDK/NDK, so I wanted to use the least number of tools and find a way to wrap all of this into something really easy.  If there is a faster/easier way to do this, I'd like to learn it.  But here we go.

1) goal - to deploy to [b]Android Studio in Windows[/b] by using least number of tools, based on reference: [b]urho3d.github.io/documentation/1.4/_building [/b] (can't post the actual URL in my very first post).
[ul]
   a) Tools required (other than Urho3D source tree): Android Studio SDK, NDK and these require - Java JDK, Gradle, Ant., and CMake required by Urho3D.
   b) Tools avoided: Eclipse and other tools listed in the reference.
        Why avoid Eclipse?  I decided to avoid using Eclipse after reading the below quote on the Android Studio site:
        [quote][b]Note:[/b] If you have been using Eclipse with ADT, be aware that Android Studio is now the official IDE for Android, so you should migrate to Android Studio to receive all the latest IDE updates. For help moving projects, see Migrating to Android Studio.[/quote]
And since I've never used Eclipse, I didn't want to bother with it.
     [/ul]
2) install-
[ul]
[li] Java JDK[/li]
[li] CMake[/li]
~~[li] Gradle[/li]~~
~~[li] Ant (Apache-Ant)[/li]~~
[li] Android Studio SDK[/li]
[li] Android NDK[/li][/ul]
Not necessarily in that order, install Java JDK before Android SDK, and be sure to have added bin and tools path in your Windows environment.

edit: removed unnecessary components

3) cmake android build - Open a cmd terminal in your <Urho3D> folder and type:
[code]cmake_android builds\android-samples -DURHO3D_SAMPLES=1[/code]
The [b]URHO3D_SAMPLES[/b] option is to build [b]executable[/b] sample code (bypassing urho3dplayer) that comes with Urho3D (missing in the build reference).  [b]Note:[/b] this builds [b]armeabi-v7a[/b] by default as indicated in the build reference. For other devices, use, e.g. [b]-DANDROID_ABI=x86[/b]

4) make - make android target build. Continuing in the cmd terminal from above
[code]
cd builds\android-samples
android list target
[/code]
'android list target' command is to see and choose the build target you want to build. Index id of 5 gives me API-16 for armeabi-v7a and x86. Let's choose that as the target (-t) for this example.
[code]
android update -p . -t 5
make -j8
[/code]
Done building for android platform build.

5) import - to Android Studio:
[ul]
a) Open Android Studio
b) Create a new project by: File -> New -> Import Project...
c) navigate to your newly build android folder. This example assumes it's <Urho3d>\builds\android-samples\ folder.
d) choose the destination project folder location, e.g. F:\Android\projects\Urho3D-Android-samples\ 
e) OK - done
[/ul]

6) deploy to an emulator or device. Do this by clicking on the [b]Play[/b] button.

That's it!

[u]Imported folder location[/u]
Following the example, under F:\Android\projects\Urho3D-Android-samples\ (let's call this <project>), 
the executables imported in 5) are found in:
<project>\app\src\main\jniLibs, specifically in the $(TARGET_ARCH_ABI) folder, for this example you should see 'armeabi-v7a' folder.
You should see number of .so files (sample code executables) along with libUrho3DPlayer.so file.
When you deploy to a device, you should see an item selection app which lists all these .so apps (see image 1).
*note* Most of these .so files should be deleted and only keep the ones that you want to test, as you probably don't have the memory to upload all these apps to your emulation device.

[u]Continuing development in imported <project>[/u]
If you want to continue developing under Android Studio, you can and not have to rebuild Urho3D.
This continuation development is done in <project>\app\src\main folder.
This folder should contain similar files when you import a sample from NDK\samples to Android Studio.

[u]Windows development[/u]
Just to note, I found using x86 emulation devices on Windows faster (as expected) than emulating on an Arm device.  For emulation purposes, I choose x86 but I also deploy to my android phone and tablet for additional testing.

I hope these easy steps can help. Good luck!

----EDIT: added screenies ----
Image 1:
[img]http://i.imgur.com/ZuCYksD.png[/img]
Image 2:
[img]http://i.imgur.com/66TSXWV.png[/img]

-------------------------

gwald | 2017-01-02 01:11:38 UTC | #2

Good guide!
This didn't work for me:
[code]
android update -p . -t #
make -j8
[/code]

instead this worked:
[code]
android update project -t # -p . -s
[/code]

I have a make issue:[code]
C:\Urho3D-android\build3>make
[  0%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/
autofit/autofit.c.o
The system cannot find the path specified.
make[2]: *** [Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/autofit/aut
ofit.c.o] Error 1
make[1]: *** [Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/all] Error 2
make: *** [all] Error 2[/code]

I have my paths correct, I can run ant, make, ndk-build etc.
I like to win/android dev on a winXP VB, I haven't seen this before:
[code]
C:\Urho3D-android>cmake_android.bat build4
CMake Warning at CMake/Modules/Urho3D-CMake-common.cmake:193 (message):
  Could not use MKLINK to setup symbolic links as this Windows user account
  does not have the privilege to do so.  When MKLINK is not available then
  the build system will fallback to use file/directory copy of the library
  headers from source tree to build tree.  In order to prevent stale headers
  being used in the build, this file/directory copy will be redone also as a
  post-build step for each library targets.  This may slow down the build
  unnecessarily or even cause other unforseen issues due to incomplete or
  stale headers in the build tree.  Request your Windows Administrator to
  grant your user account to have privilege to create symlink via MKLINK
  command.  You are NOT advised to use the Administrator account directly to
  generate build tree in all cases.
Call Stack (most recent call first):
  CMakeLists.txt:47 (include)

[/code]

-------------------------

weitjong | 2017-01-02 01:11:39 UTC | #3

I haven't done any Android build using Windows host system, so I don't have any comment on your issue. However, the steps listed in the guide looks correct to me though. Regarding the last CMake warning, you can safely proceed. It is just a warning. I think the waning message is clear enough why you got it and how you could suppress it by setting up your Windows user account to have proper privilege.

-------------------------

Lumak | 2017-11-23 16:26:39 UTC | #4

Update ndk no longer supports multiple target builds and the **android update** is no longer supported. New steps:

1) make your build to a [b]clean folder[/b], I'm specifying my tool chain from android-ndk-r15c
[code]
cmake_android PathToCleanBuildFolder -DANDROID_TOOLCHAIN_NAME=x86-4.9 -DURHO3D_LUA=0 -DURHO3D_PACKAGING=0 -DURHO3D_TOOLS=0
[/code]

2) go into your build folder and build
[code]
make
[/code]
3) open your Android Studio and import your build
* File -> New -> Import Project -- and select your build folder

That simple. In Android Studio create an emulation device compatible with what's defined in Urho3D/AndroidManifest.xml, and this example is a build for x86 device -> choose x86 emulation device.

-------------------------

NiteLordz | 2017-11-25 14:59:00 UTC | #5

@Lumak

When i run the cmake_android command with the above parameters, i am getting "CMAKE_MAKE_PROGRAM is not set.  I am running on Windows 10 with Visual Studio 2017 and Android Studio installed.  What do i need to do to set the appropriate make program to use.

Thanks much

-------------------------

Lumak | 2017-11-25 19:35:17 UTC | #6

I remember having this error, and I believe it was to set:
**android-ndk-r15c\prebuilt\windows-x86_64\bin**
to the path.

edit: looked it up on the system settings:

-------------------------

NiteLordz | 2017-11-26 00:45:54 UTC | #7

Thanks, that did the trick!

-------------------------

