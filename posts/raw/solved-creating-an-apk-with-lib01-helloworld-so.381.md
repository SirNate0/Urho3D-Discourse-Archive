zakk | 2017-01-02 00:59:59 UTC | #1

Hello,

I'm new to Urho3D, and i'm interested with its Android compatibility feature.

I'm using Linux, and Lua for scripting.
The Android NDK is installed.

I've compiled the Android library, using the gcc cmake script.
[code]./cmake_gcc.sh -DURHO3D_64BIT=1 -DURHO3D_LUA=1 -DURHO3D_SAMPLES=1[/code]

It seemed to compile without problems, and i got a bunch of libs here:
[code]~/sources/Urho3D/android-Build/libs/armeabi-v7a$
4,1M  8 ao?t  22:35 lib01_HelloWorld.so
 (?)
 35M  7 ao?t  16:37 libUrho3D.a
6,8M  8 ao?t  22:35 libUrho3DPlayer.so[/code]

Ok. So now, what can i do with those libs for getting a nice APK, which would launch the first sample on my phone ?
I guess the answer lies here

[code]
~/sources/Urho3D/Source/Android$ ls -l
-rw-r--r-- 1255  7 aug  14:12 AndroidManifest.xml
drwxr-xr-x 4096  8 aug  22:32 assets
-rw-r--r-- 3580  7 aug  14:12 build.xml
-rw-r--r--  183  7 aug  14:12 CopyData.bat
drwxr-xr-x 4096  7 aug  14:12 res
drwxr-xr-x 4096  7 aug  14:12 src
[/code]

Everything seems ready, but i'm missing the final step for creating the apk with all these.
My only experience with Android is compiling a native Lua interpreter, and sending it to the phone with ssh :slight_smile:

Thank you.

-------------------------

friesencr | 2017-01-02 00:59:59 UTC | #2

I have only done this a few times but I believe the apk is generated using ant.  Running `ant debug` or `ant release`  should generate the apk.  I think it is ran in Source/Android folder.

Here is a reference to the build instructions:
[urho3d.github.io/documentation/a00001.html](http://urho3d.github.io/documentation/a00001.html)

-------------------------

zakk | 2017-01-02 01:00:00 UTC | #3

Thank you for insisting on the documentation.

I had missed this part.

Now it works like a charm, i got the apk and all the samples seem to work.

Thanks again!

-------------------------

