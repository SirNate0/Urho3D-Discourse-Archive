xahon | 2018-04-27 12:04:33 UTC | #1

I'm trying to compile android game.
I've compiled Urho3d via cmake and `make install` it
Then I created a dummy project from this [article](https://github.com/urho3d/Urho3D/wiki/First-Project)

And...

```
mkdir android
./cmake_android ./android -DANDROID_NATIVE_API_LEVEL=android-14
```

>CMake Error at CMake/Modules/FindUrho3D.cmake:346 (message):
  Could NOT find compatible Urho3D library in Urho3D SDK installation or
  build tree.  Use URHO3D_HOME environment variable or build option to
  specify the location of the non-default SDK installation or build tree.
  For Android platform, double check if you have specified to use the same
  ANDROID_ABI as the Urho3D library in the build tree or SDK.
Call Stack (most recent call first):
  CMake/Modules/UrhoCommon.cmake:238 (find_package)
  CMakeLists.txt:40 (include)

What did I do wrong?

-------------------------

KonstantTom | 2018-04-27 12:16:22 UTC | #2

As I understand, you must set environment variable `URHO3D_HOME` which contains path to your Urho3D installation (directory, generated by `make install`).

-------------------------

xahon | 2018-04-27 12:29:11 UTC | #3

```
echo $URHO3D_HOME 
/home/me/Programs/Urho3D

lh /home/me/Programs/Urho3D
total 496K
drwxrwxr-x 5 ilya ilya 4,0K апр 27 18:07 Android
drwxrwxr-x 6 ilya ilya 4,0K апр 27 20:38 bin
drwxrwxr-x 4 ilya ilya 4,0K апр 27 18:07 CMake
-rw-rw-r-- 1 ilya ilya 1,2K апр 27 18:07 cmake_android.bat
-rwxrwxr-x 1 ilya ilya 1,2K апр 27 18:07 cmake_android.sh
-rwxrwxr-x 1 ilya ilya 1,2K апр 27 18:07 cmake_arm.sh
... and others ...
```

-------------------------

xahon | 2018-04-27 13:20:38 UTC | #4

But you was partially right I've closed terminal window and my `export URHO3D_HOME` result gone. I've made export again and now it shows me more errors like

>/home/me/Android/Sdk/ndk-bundle13/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/lib/gcc/arm-linux-androideabi/4.9.x/../../../../arm-linux-androideabi/bin/ld:
  error: /home/me/Programs/Urho3D/lib/libUrho3D.a(LibraryInfo.cpp.o):
  incompatible target
  >CMakeFiles/cmTC_70a47.dir/CheckUrhoLibrary.cpp.o:/home/me/Programs/UrhoTest/CMake/Modules/CheckUrhoLibrary.cpp:function
  main: error: undefined reference to 'Urho3D::GetRevision()'

-------------------------

weitjong | 2018-04-27 14:34:09 UTC | #5

The linker error was “incompatible target”

It means your Urho3D lib was not built for the same target platform or architecture as your app.

-------------------------

xahon | 2018-04-27 14:58:54 UTC | #6

Do you mean I have compiled urho without android target?

-------------------------

weitjong | 2018-04-27 15:11:27 UTC | #7

Use the “file libUrho3D.a” command to verify.

-------------------------

xahon | 2018-04-27 15:20:29 UTC | #8

From which directory? `URHO3D_HOME/lib`?

-------------------------

weitjong | 2018-04-27 15:46:20 UTC | #9

Yes. And the fact it is in “lib” folder already gives a tell tale sign that it was not built for Android platform.

-------------------------

xahon | 2018-04-27 15:45:47 UTC | #10

I just ran `ccmake` and discovered no android settings at all. I cloned latest version of urho from github (master). Do I need to clone a specific branch?

-------------------------

