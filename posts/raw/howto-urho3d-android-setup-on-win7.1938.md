gwald | 2017-01-02 01:11:41 UTC | #1

This is how I installed android dev env.
I'm no expert, I'm sure there's better ways or I did something wrong, please comment if so.

[url=http://discourse.urho3d.io/t/android-build-on-windowsxp-issues/1934/1]I've given up winXP as I couldn't fix the symbolic link issue on Android.[/url]

I Install (use the latest version) in this,  order look at my Console android-batch file for locations I use (with no spaces):
7Zip
Notepade++
Java JDK (I copy the jdk-folder to C:\JDK)
TDM-GCC (required for [url=http://discourse.urho3d.io/t/android-build-on-win7-issue-solved/1937/2]lua tool building[/url])
cmake
ant
gradle (not sure it's required)
Urho3D (C:\Urho3D-master)

Lastly, install the Android SDK.exe setup to C:\Android\ (not the studio install exe)
Then extract the Android NDK to C:\Android\android-ndk
So you should have:
C:\Android\android-ndk
C:\Android\android-sdk

Create the console android-batch file in C:\Urho3D-master:
[code]
set path=%path%;C:\Android\android-ndk\prebuilt\windows\bin;C:\ant\bin;C:\gradle\bin;C:\Android\android-ndk\build;C:\Android\android-sdk\tools;C:\Android\android-sdk\tools\bin;C:\Android\android-sdk\platform-tools
set  ANDROID_NDK=C:\Android\android-ndk
set  ANDROID_SDK=C:\Android\android-sdk
set JAVA_HOME=C:\JDK
set GRADLE_HOME=C:\gradle
cmd /k cd
[/code]

launch the android-batch file, and test:
cmake
make
ant
nkd-build
gcc
java
javac
android
gradle

They should all work! if not check the batch file paths/vars.

Next setup the SDK, run android
Click the Deselect all link.
From Tools -> tick the android SDK build tools, make sure platform-tool and SDK tools should be installed, if not also tick them.
Install Android 4.0.3 API 15 - This is the latest version which has an x86 image and is compatible with windows.
Tick SDK plaform, Intel x86 atom system image and google APIs.
I'm not familiar with all the packages here.
Click the install button and agree to everything.
It should download and install correctly.

Run:
android list target
You should get a list of targeted SDK, I use 1 Android-15

In the root Urho3D folder run:
cmake_android build -DURHO3D_SAMPLES=1 
[url=http://urho3d.github.io/documentation/1.31/_building.html]Adding other options required.[/url]

There should be no errors and the build folder should be created, cd into that folder and run:
android update project -p . -t 1
Where 1 is your targeted SDK ID 
It should out put a few lines, with no error message.

Next run:
make 
Optionally, add -j2 where 2 is the number of CPU cores you want to use to build.
It will compile the and link with ndk toolchain.
There should be no errors.
If so, the env isn't setup correctly, ie Android SDK, native gcc or paths issues

To build an apk, run:
 ant debug
Javac is used to create the Urho3D-debug.apk in the bin folder ie C:\Urho3D-master\build\bin\
Copy it to your mobile and install it, it should work.


rebuild.bat:
[code]call cmake_android build -DURHO3D_SAMPLES=1 
cd build
call android update project -p . -t 1
call make
call ant debug
[/code]

Debugging on Hardware:
Set your device up with USB debugging  and  stay awake on, under Dev options in Android settings .
On Android 4.2 and higher, the Developer options screen is hidden by default. To make it visible, go to Settings > About phone and tap Build number seven times. Return to the previous screen to find Developer options at the bottom.

Also, In screen setting, Turn sleep mode to never.

Make sure you have the [url=http://developer.android.com/sdk/win-usb.html]USB driver installed[/url]

To kill the server forcefully:
adb kill-server

To start the server:
adb start-server

plug  in device

run: adb devices
It should list your device


adb  install C:\Urho3D-master\build\bin\Urho3D-debug.apk 

[developer.android.com/tools/help/adb.html](http://developer.android.com/tools/help/adb.html)
[developer.android.com/tools/help/logcat.html](http://developer.android.com/tools/help/logcat.html)

References:
[urho3d.github.io/documentation/1 ... lding.html](http://urho3d.github.io/documentation/1.31/_building.html)
[topic1142.html](http://discourse.urho3d.io/t/deploying-urho3d-to-android-studio-in-windows/1107/1)
Thanks to weitjong for his help.

-------------------------

1vanK | 2017-12-02 11:16:08 UTC | #3

```
d:\Android\Urho3D_Current\Build>android update project
**************************************************************************
The "android" command is deprecated.
For manual SDK, AVD, and project management, please use Android Studio.
For command-line tools, use tools\bin\sdkmanager.bat
and tools\bin\avdmanager.bat
**************************************************************************

Invalid or unsupported command "update project"

Supported commands are:
android list target
android list avd
android list device
android create avd
android move avd
android delete avd
android list sdk
android update sdk
```

-------------------------

weitjong | 2017-12-02 16:16:20 UTC | #4

You need to downgrade the Android build tool version (version 24 is my memory serves me right), if you insist on using the old approach.

-------------------------

Miegamicis | 2017-12-04 07:56:01 UTC | #5

I got the Android build running when donwgraded the Android tools to these specific versions:

build-tools_r24.0.2
https://androidsdkoffline.blogspot.com/p/android-sdk-build-tools.html

platform-tools_r25
https://androidsdkoffline.blogspot.com/p/android-sdk-platform-tools.html

tools_r25.2.3
https://androidsdkoffline.blogspot.com/p/android-sdk-tools.html

I've found the versions numbers somewhere on the web.
Just downloaded and replaced the current tool versions with these ones and run everything else as specified in the Urho3D build documentation. Hope this helps!

-------------------------

Angramme | 2019-03-09 10:04:49 UTC | #6

Hi sorry for bothering, but what is the new approach of building Urho3D on Android? You said this the old one.

-------------------------

weitjong | 2019-03-09 10:44:35 UTC | #7

We have migrated to Gradle for Android build. Read the online doc for building the Urho3D lib. Make sure you use the HEAD version in the doc version switcher. Currently only tested to work on Win7, Linux and macOS host systems. YMMV on Windows 10.

-------------------------

WangKai | 2020-02-02 06:17:55 UTC | #8

Hi @weitjong

Would you please give the link of the document of building Urho3D with Gradle for Android?
Thanks!

-------------------------

weitjong | 2020-02-02 11:16:36 UTC | #9

Here is the link. https://urho3d.github.io/documentation/HEAD/_building.html#Building_Android

-------------------------

WangKai | 2020-02-02 12:50:17 UTC | #10

Thanks @weitjong

There is Gradle plugin issue from Android Studio -

![image|496x214](upload://9ETVxK1rV8SfxoaG5kxNJ6PmbIY.png)  

After choosing **Update**, it says -
![image|527x138](upload://h9CJFvpO1Jxl0qEtWXcWSW3Qkuk.png) 

I'm using Android Studio 3.5.3

-------------------------

WangKai | 2020-02-02 14:47:02 UTC | #11

Additionally, I'm not sure how to ***use Urho3D as a library for a standalone project while keeping using gradle and Android Studio*** -

https://urho3d.github.io/documentation/1.7.1/_using_library.html
(Taking advantage of CMake, but how to also use gradle?)

I work most on Window, so please inspire me with Android knowledge.
Thank you very much!

-------------------------

weitjong | 2020-02-02 16:16:07 UTC | #12

Change this line to the version you need.

https://github.com/urho3d/Urho3D/blob/master/buildSrc/src/main/kotlin/UrhoCommon.kt#L30

-------------------------

weitjong | 2020-02-02 16:16:40 UTC | #13

I am not using Windows, so others please help.

-------------------------

Bluemoon | 2020-02-02 23:23:14 UTC | #16

I'm on win10 and use a command line based build pipeline for standalone urho3d android apps instead of Android Studio and Gradle.  This pipeline was adapted from [here](https://www.hanshq.net/command-line-android.html) and is mainly composed of two batch files one to build the native *.so file and the other to wrap it into an apk . 
Though currently this has evolved more into a project template than a bunch of scripts

With it and  vscode as my IDE,  everything works as expected. But I must say it is a bit messy but could be made better :stuck_out_tongue: .

If you are interested I could clean it up, make it look presentable a bit, and then post here.

-------------------------

WangKai | 2020-02-03 03:23:03 UTC | #17

Is it debuggable? We can use our favorite IDE but the debugging capability is essential, IMHO.

-------------------------

Bluemoon | 2020-02-03 12:28:43 UTC | #18

Well, as it is, it is not yet debuggable. Though getting it to be debuggable sounds like an interesting task to take up if it's possible with the pipeline.

-------------------------

WangKai | 2020-02-03 13:47:30 UTC | #19

If we still can choose to use Android Studio, I guess debugging, log watching, emulation/device management would be better.

-------------------------

WangKai | 2020-02-03 13:50:01 UTC | #20

Even, if we use some kind of networking ability, we can update resouces via networking, to see the result of change immediately, just another random thinking.
Edit: or does Android allows us to patch the apk on the fly?

-------------------------

Bluemoon | 2020-02-03 14:00:32 UTC | #21

I really don't know if android allows on the fly patching of apk but that would be excellent to have

-------------------------

