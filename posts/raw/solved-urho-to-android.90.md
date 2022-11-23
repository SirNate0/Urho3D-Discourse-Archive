lexx | 2017-01-02 00:57:54 UTC | #1

Hi.
I got newest urho from git, then followed the documentation and tried to run urho3d in android but cannot get it to work.
I got Urho3D-debug.apk 9598KB and tried it with emulator and Bluestacks, but it doesnt start. 
Does Urho3D-debug.apk contain NinjaSnowWar? At least it did some time ago last year if I remember correctly.

(w7x64, android-ndk-r9c)

logcat:
[quote]
E/AndroidRuntime(  295): FATAL EXCEPTION: main
E/AndroidRuntime(  295): java.lang.UnsatisfiedLinkError: onNativeResize
E/AndroidRuntime(  295):        at org.libsdl.app.SDLActivity.onNativeResize(Native Method)
E/AndroidRuntime(  295):        at org.libsdl.app.SDLSurface.surfaceChanged(SDLActivity.java:568)
E/AndroidRuntime(  295):        at android.view.SurfaceView.updateWindow(SurfaceView.java:549)
E/AndroidRuntime(  295):        at android.view.SurfaceView.dispatchDraw(SurfaceView.java:348)
E/AndroidRuntime(  295):        at android.view.ViewGroup.drawChild(ViewGroup.java:1644)
.
.
.
[/quote]

-------------------------

carlomaker | 2017-01-02 00:57:55 UTC | #2

Welcome to forum , pls post bug report on [url=https://github.com/urho3d/Urho3D/issues]gitHub[/url]

-------------------------

weitjong | 2017-01-02 00:57:56 UTC | #3

I don't think this is a bug, so I unlock this thread for further discussion.

I have some time this morning to try out the Android build again on Win7. I am still using android-ndk-r9b but I don't think that makes any difference. I use Eclipse IDE that comes with ADT bundle. After configuring the Urho3D Android project using the provided cmake_android.bat file and importing into Eclipse workspace, all I need to do next is Running the Urho3D project in the Eclipse IDE and Eclipse would build and deploy the apk for me to my Android (virtual) device. By default, our build script still uses Urho3DPlayer target (the target name has changed depends on when you last checking out Urho3D) for the Android build and it is still pre-configured to play NinjaSnowWar.as.

Here is logcat from my avd:
[code]
02-12 23:10:34.880: V/SDL(905): onResume()
02-12 23:10:36.180: V/SDL(905): surfaceCreated()
02-12 23:10:36.180: V/SDL(905): surfaceChanged()
02-12 23:10:36.180: V/SDL(905): pixel format RGB_565
02-12 23:10:36.180: V/SDL(905): Window size:768x1184
02-12 23:10:36.300: I/SDL(905): SDL_Android_Init()
02-12 23:10:36.300: I/SDL(905): SDL_Android_Init() finished!
02-12 23:10:36.500: D/gralloc_goldfish(905): Emulator without GPU emulation detected.
02-12 23:10:36.740: I/Urho3D(905): Added resource path /apk/CoreData/
02-12 23:10:36.850: I/Urho3D(905): Added resource path /apk/Data/
02-12 23:10:37.110: I/Urho3D(905): Set screen mode 768x1184 fullscreen
02-12 23:10:37.110: I/Urho3D(905): Initialized input
02-12 23:10:37.120: I/Urho3D(905): Initialized user interface
02-12 23:10:37.260: I/Urho3D(905): Initialized renderer
02-12 23:10:37.270: V/SDL(905): SDL audio: opening device
02-12 23:10:37.270: V/SDL(905): SDL audio: wanted stereo 16-bit 44.1kHz, 4096 frames buffer
02-12 23:10:37.530: V/SDL(905): SDL audio: got stereo 16-bit 44.1kHz, 4096 frames buffer
02-12 23:10:37.530: I/Urho3D(905): Set audio mode 44100 Hz stereo interpolated
02-12 23:10:44.800: I/Urho3D(905): Compiled script module Scripts/NinjaSnowWar.as
02-12 23:10:45.750: I/Urho3D(905): Loading scene from Scenes/NinjaSnowWar.xml
02-12 23:10:47.520: E/libEGL(905): called unimplemented OpenGL ES API
[/code]

The last error entry in the log was caused by my Win7 virtual machine does not provide a proper OpenGL ES driver implementation or otherwise Urho3D sample android app would run as per normal even on AVD running on a virtual machine! BTW, I have also just tried deploying Urho3D sample android app on a real device without any problem (it was build by Eclipse/ADT on my main Linux box, however).

If you don't use Eclipse IDE, I believe from the CLI invoking make and ant debug and ant installd should give you the same result. Perhaps you can elaborate more steps by steps how you setup and build your android project. And hopefully one of us can point out where you have done wrong. HTH.

-------------------------

lexx | 2017-01-02 00:57:56 UTC | #4

[quote]
	cd E:\CPP\Urho3D
	set path=%PATH%;e:\ANDROID_kamaa\android-ndk-r9c\prebuilt\windows-x86_64\bin
	set ANDROID_NDK=e:\ANDROID_kamaa\android-ndk-r9c
	cmake_android.bat
	cd source\android
	android update project -p . -t 1 
	make -j4
	ant debug
[/quote]

I tried   cmake_android.bat   -DANDROID_ABI=armeabi    too.


android list
[quote]
id: 1 or "android-10"
     Name: Android 2.3.3
     Type: Platform
     API level: 10
     Revision: 2
     Skins: HVGA, QVGA, WQVGA400, WQVGA432, WVGA800 (default), WVGA854
     ABIs : armeabi, x86
[/quote]


adb logcat   (shows interesting(?) line  "W/dalvikvm(  352): No implementation found for native Lorg/libsdl/app/SDLActivity;.onNativeResize (III)VD/AndroidRuntime(  352): Shutting down VM")

[quote]
I/ActivityManager(   61): Start proc com.googlecode.urho3d for activity com.googlecode.urho3d/.Urho3D: pid=352 uid=10034 gids={3003}
I/WindowManager(   61): Setting rotation to 1, animFlags=1
I/ActivityManager(   61): Config changed: { scale=1.0 imsi=310/260 loc=en_US touch=3 keys=2/1/2 nav=1/1 orien=2 layout=34 uiMode=17 seq=11}
V/SDL     (  352): onResume()
I/ActivityManager(   61): Displayed com.googlecode.urho3d/.Urho3D: +610ms
V/SDL     (  352): surfaceCreated()
V/SDL     (  352): surfaceChanged()
V/SDL     (  352): pixel format RGB_565
W/dalvikvm(  352): No implementation found for native Lorg/libsdl/app/SDLActivity;.onNativeResize (III)VD/AndroidRuntime(  352): Shutting down VM
W/dalvikvm(  352): threadid=1: thread exiting with uncaught exception (group=0x40015560)
E/AndroidRuntime(  352): FATAL EXCEPTION: main
E/AndroidRuntime(  352): java.lang.UnsatisfiedLinkError: onNativeResize
E/AndroidRuntime(  352):        at org.libsdl.app.SDLActivity.onNativeResize(Native Method)
E/AndroidRuntime(  352):        at org.libsdl.app.SDLSurface.surfaceChanged(SDLActivity.java:568)
E/AndroidRuntime(  352):        at android.view.SurfaceView.updateWindow(SurfaceView.java:549)
E/AndroidRuntime(  352):        at android.view.SurfaceView.dispatchDraw(SurfaceView.java:348)
E/AndroidRuntime(  352):        at android.view.ViewGroup.drawChild(ViewGroup.java:1644)
E/AndroidRuntime(  352):        at android.view.ViewGroup.dispatchDraw(ViewGroup.java:1373)
E/AndroidRuntime(  352):        at android.view.ViewGroup.drawChild(ViewGroup.java:1644)
.
.
.
[/quote]

-------------------------

weitjong | 2017-01-02 00:57:56 UTC | #5

I can't see anything wrong with your step. The difference between your setup and mine is that I configure it with additional build option -DUSE_MKLINK=1 to get the so called out-of-source project. So, my android project resides in android-Build\ directory instead of inside the source\ directory. Having said that, I don't expect the in-the-source project would cause this problem. I have not tried API level 10 on android-10 before. Usually I use API level 9 and level 19 (the two extremes) on nexus-4 or nexus-7 hardware profile. Have you tried to target different API levels? I am not sure if this post is helpful or not.

-------------------------

lexx | 2017-01-02 00:57:57 UTC | #6

Yeah, ok, tried API19 (android 4.2.2) and it works on emulator.

Android SDK Manager doesnt show API9 (there are API8 (android 2.2), and that API10 (android 2.3.3) which I cant get to work).

-------------------------

weitjong | 2017-01-02 00:57:57 UTC | #7

Glad to hear you get it works eventually. I may have not made myself clear in my earlier post. I meant to say that I set the min and max API level in the android manifest file to 9 and 19, and configure avd that runs API level 9 and 19 to test. But I always only use the latest SDK API level to build.

-------------------------

