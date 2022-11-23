Pencheff | 2017-04-10 18:56:58 UTC | #1

I've got stuck trying to build Urho3D on latest Android Studio 2.3. Previous tutorials on how to build for Android are outdated, the command "android update project" is no longer supported. So I've imported the project as Eclipse project, then added a cmake step to the gradle script that builds the native library. Couple of problems appear:

1. **CheckCompilerToolchain.cmake - check_extension and check_feature_enabled** fail with error **"Could not check compiler toolchain as it #does not handle '-E -dM' compiler flags correctly"**. If I comment out the FATAL_ERROR message, it compiles just fine. This happens with clang as default compiler, if I specify gcc, I get errors when linking - "relocation overflow in R_ARM_THM_CALL".

2. Linker fails with **undefined reference to armFuncR0**, I turned of AngelScript just for the sake of compiling. 

3. **ThirdParty/ik/src/platform/linux/backtrace_linux.cpp** can't find [code]#include <execinfo.h>[/code] . Removing the include compiles fine. 

Help much appreciated on bringing this up and running.

-------------------------

Pencheff | 2017-04-09 08:26:12 UTC | #2

Nevermind, I got it running. Here's my gradle script for anyone else trying to figure it out.

[code]
apply plugin: 'com.android.application'
android {
    compileSdkVersion 21
    buildToolsVersion "25.0.2"
    defaultConfig {
        applicationId "com.github.urho3d"
        minSdkVersion 11
        targetSdkVersion 21
        ndk {
            abiFilters 'armeabi-v7a', 'arm64-v8a'
            stl = "stlport_static" // gnustl fails with cstddef not found
        }
        externalNativeBuild {
            cmake {
                arguments "-DANDROID_TOOLCHAIN=clang", "-DURHO3D_ANGELSCRIPT=FALSE", "-DURHO3D_LIB_TYPE=SHARED"
            }
        }
    }
    buildTypes {
        release {
            minifyEnabled = false
            proguardFiles getDefaultProguardFile('proguard-android.txt')
        }
    }
    externalNativeBuild {
        cmake {
            path '../../../Urho3D/CMakeLists.txt' // relative path to the Urho3D CMakeLists.txt
        }
    }
    sourceSets.main {
        jniLibs.srcDirs = ['libs']
    }
}
[/code]

-------------------------

johnnycable | 2017-04-10 14:11:21 UTC | #3

Same here. I confirm angelscript issue, but only with arm64-v8a abi. No problem with others abis...
My intention is to come up with a generalized approach. Android build is very convoluted... 
This script is for building the library and the app in just one executable, right?
One last thing. Have you tried building the full installation with examples on android? I did, and when I tap the icon to launch it, one time in four i doesn't even start! Let alone there's no way to opt out of an example without removing it from memory...:confused:

-------------------------

johnnycable | 2017-04-10 15:57:17 UTC | #4

It works!
Building from upstream urho3d library, to downstream urho3d app, in android studio 2.3, with custom setup project, run native, pack apk, and debugger.
Tried on Samsung Galaxy Note 4, android 4.4.4

-------------------------

Pencheff | 2017-04-10 16:18:53 UTC | #5

Yes I've managed to run the examples. The project after importing requires to manually copy the output libraries to a lib subdirectory of the project.  I've run them on my phone OnePlus3t android 7.0,  Lg G3 6.0 and a cheap kodi box with 5.1...everything runs fine.

-------------------------

johnnycable | 2017-04-10 18:04:55 UTC | #6

I've tried just now on my old 2011 lgp920 with android 2.3.5... 512mb memory... a couple of example with sound and particles. Everything seems fine.

-------------------------

Pencheff | 2017-04-10 20:22:12 UTC | #7

Just curios, how did you migrate the project ? 
I'm importing it but it doesn't include the CoreData/Data/Autoload folders and the libraries, so I imported them manually.

-------------------------

johnnycable | 2017-04-11 10:24:20 UTC | #8

Exactly that. I doesn't import them, i just did a script which imports them

-------------------------

sabotage3d | 2017-04-14 20:05:08 UTC | #9

Hey guys what would be the gradle build script if we want to build against already build Urho3d lib for seperate project? I am getting these errors when I try to build my project:
>     CMake Error at CMake/Modules/CheckCompilerToolchain.cmake:161 (message):
>       Could not check compiler toolchain as it does not handle '-E -dM' compiler
>       flags correctly
>     Call Stack (most recent call first):
>       CMake/Modules/UrhoCommon.cmake:98 (include)
>       CMakeLists.txt:18 (include)
>     -- Configuring incomplete, errors occurred!

-------------------------

Pencheff | 2017-04-15 21:43:41 UTC | #10

Check the first post. 

1. Edit CheckCompilerToolchain.cmake - there are three places where you need to comment out the message(FATAL ...compiler doesn't​ handle -E -DM

2. Compile without angelscript - see above in the gradle script I provided.

3. ThirdParty/ik/src/platform/linux/backtrace_linux.cpp - comment the execinfo.h include and everything inside the function below.

-------------------------

artgolf1000 | 2017-04-25 14:02:35 UTC | #11

I use urho3d as an external library, and I can build my project with cmake_android.sh successfully, it can generate an .so library.

But since 'android update project' is no longer available, I can not use 'ant  Debug' now.

Must I use android studio 2.3? what should I do next?

-------------------------

weitjong | 2017-04-25 14:19:06 UTC | #12

Downgrade the build-tool to 25.2 or earlier. We still use 22.1 (I think) in one of our Android CI build job which tests artifact deployment to an AVD. You are on your own right now if you have to use Gradle instead of Ant.

-------------------------

Pencheff | 2017-04-25 14:39:17 UTC | #13

Well, I've managed to build with Gradle, where Urho3D and other dependencies of my project are built in a separate module, then my project builds as a module depending on the first one. I can just build with a standalone toolchain, but that requires me to create a separate toolchain for every ABI, armeabi-v7a, armeabi-v8, x86...etc, then build and then copy the output shared libraries somewhere where my project can find them, but linking to a different version depending on the main project ABI....and I don't like doing things manually when building. 

I can confirm Urho3D builds successfully with the $ANDROID_SDK/ndk-bundle/build/cmake/android.toolchain.cmake, you only have to patch ThirdParty/ik/src/platform/linux/backtrace_linux.cpp to remove the execinfo include. 

Also, I found out the reason why the libraries are not included in the APK - when Gradle runs CMake, it sets CMAKE_LIBRARY_OUTPUT_DIRECTORY to app/build/intermediates/cmake/debug/obj/armeabi-v7a (depending on the ABI) and expects to find the .so there. If you change CMAKE_LIBRARY_OUTPUT_DIRECTORY like I usually do, it won't even warn you about it and just proceed.

-------------------------

artgolf1000 | 2017-04-30 01:58:22 UTC | #14

Figure out the simplest way to use Android Studio 2.3.1 on macOS Sierra v10.12.4.

To build Urho3D and the samples:

1. Install Android Studio 2.3.1(Install Android Simulator, CMake, LLDB, NDK from the SDK manager)

2. Set NDK path
vi ~/bash_profile
export ANDROID_NDK=~/Library/Android/sdk/ndk-bundle

3. Genrate project
cd ~/Urho3D
// When using device
./cmake_android.sh ~/Urho3D-Android -DURHO3D_SAMPLES=1
// When using simulator
./cmake_android.sh ~/Urho3D-Android -DURHO3D_SAMPLES=1 -DANDROID_TOOLCHAIN_NAME=x86-clang
cd ~/Urho3D-Android
make

4. Import the generated project(~/Urho3D-Android) into Android Studio

5. Connect the phone or launch the simulator, build and run.

To build your own standalone project:

1. Copy the 'Android' subdirectory to your project, let 'Android/assets/CoreData' and 'Android/assets/Data' soft-link to your own data.

2. Copy the 'CMake' subdirectory to your project.

3. Modify CMakeLists.txt:
set (ENV{URHO3D_HOME} ~/Urho3D-Android).

4. Generate project.
cd ~/YourProject
// When using device
./cmake_android.sh ~/YourProject-Android
// When using simulator
./cmake_android.sh ~/YourProject-Android -DANDROID_TOOLCHAIN_NAME=x86-clang
cd ~/YourProject-Android
make

5. Rename your generated shared library to 'libUrho3DPlayer.so' or modify ~/YourProject/Android/src/com/github/urho3d/Urho3D.java, replace all strings of 'Urho3DPlayer' to your project name.

6. Import the generated project(YourProject-Android) into Android Studio

7. Connect the phone or launch the simulator, build and run.

Note: While you run Android Studio:

1. You need to remove all old android related variables from ~/bash_profile.

2. You need to remove the old ~/.android hidden directory, otherwise, the simulator may fail to launch.

3. You need to run 'Build->Clean Project' and 'Build->Rebuild Project' to ensure a clean build.

Android Studio 2.3.1's official simulators run much faster than iOS simulator, I like it very much.

-------------------------

hicup_82017 | 2017-08-27 08:54:39 UTC | #16

Hi artgolf,
Your reply helped me a lot in building urho3d examples for android. However, I just want to add few points so that another newbie like me would get benefited.

**In step3,**
Download, urho3d 1.7 tar fiile from link "https://urho3d.github.io/documentation/1.4/class_urho3_d_1_1_resource_cache.html" and extract and name it as "Urho3D "

**After step 5 in standalone project procedure**, i followed below as mentioned in documentation.

****Step b.6:** For building apk file.** 
 $ android list target
output =  different android targets that were installed. I chose id 1 from the list.
**step b.6.1:**
$ android update project -p . -t 1
**step b.6.2:** 
$ ant debug
output: unsigned debug apk file in the bin directory.

**step b.7: signing the apk file**

**step b.7.1:** get the keystore file,
For this you got to refer android websites and you shall end up with a key store file.
once you had the key store file, say "mykeystore1"

**step b.7.2:** make ant.properties file as below and 
open notebook,and add following lines,

key.store.password=test123
key.alias.password=test123
key.store=/media/hicup/mykeystore1
key.alias=business

save this as ant.properties file.

**step b.7.3:** place this file in your "YourProject-Android" folder.
**step b.7.4:** $ ant debug
output: you shall get signed debug file.
Now, this can be straight away installed into your mobile.

Additional info:
If you want speed up your testing, just issue 
**step b.8:** 
$ ant installd
output: This will automatically install the app in simulator. 

**Disclaimer:** I done this on ubuntu 16.04 version with Urho3d version 1.7

-------------------------

Taymindis | 2017-10-14 02:31:04 UTC | #17

@artgolf1000

This is working with just 1 time effort :slight_smile:

-------------------------

magic.lixin | 2017-11-07 02:38:41 UTC | #18

Hi
   I got a error when I try to run the samples in Android Simulator, it tells me SDL Error, fromIndex = -1, the version of my Android Studio is 3.0, do I need to downgrade to 2.3 ?

-------------------------

Taymindis | 2017-11-07 05:59:09 UTC | #19

[quote="magic.lixin, post:18, topic:2995"]
SDL Error, fromIndex = -1,
[/quote]

Can you dump the error log ?

-------------------------

magic.lixin | 2017-11-07 06:03:49 UTC | #20

well, I found the root cause is that libUrho3dPlayer.so is missing ...

because I didn't enable angle scripting and also lua scripting .... so there is no libUrho3dPlayer.so which is required by Urho3d.java :confused:

-------------------------

Taymindis | 2017-11-07 06:11:15 UTC | #21

You need to change the lib name to your built lib name

For android developement, jni need to load library, just follow this step,

Rename your generated shared library to 'libUrho3DPlayer.so' or modify ~/YourProject/Android/src/com/github/urho3d/Urho3D.java, replace all strings of 'Urho3DPlayer' to your project name.

-------------------------

magic.lixin | 2017-11-07 06:11:12 UTC | #22

yes, thanks for the tip, after replacing the Urho3DPlayer to "18_CharacterDemo", it works :slight_smile:

-------------------------

weitjong | 2017-11-07 14:19:15 UTC | #23

That is not how it supposed to work. Downstream application targeting Android platform is better of creating a new subclass of SDLActivity or using the SDLActivity class directly if no custom loading logic required.

-------------------------

ChunFengTsin | 2017-11-30 05:38:47 UTC | #24

when I build the samples project , 
the last step of "3.Generate project" , when I exec "make" at the Urho3D-Android , tips that:
  
 /ndk-bundle/sources/cxx-stl/llvm-libc++/include/string.h:61:15: fatal error: 'string.h' file not found
#include_next <string.h>
              ^~~~~~~~~~

why it can't find head file of ndk.....

-------------------------

ChunFengTsin | 2017-11-30 06:10:25 UTC | #25

I have the feeling that i'm missing an environment variable or some sort of configuration that tells the ndk where to look up for the string.h files, 
how should I config it...

-------------------------

weitjong | 2017-11-30 13:19:56 UTC | #26

I reckon you are using Android NDK r16. Change it to r15c and it should build cleanly. I will change the build system to support r16 when I have time later.

-------------------------

yushli1 | 2017-11-30 16:11:23 UTC | #27

official support for NDK r16 would be highly appreciated. r16 uses only unified headers, that may need some effort.

-------------------------

magic.lixin | 2017-12-01 06:18:15 UTC | #28

 you can just download older ndk version (NDK r15c), and extract it to some where, and set the environment variable ANDROID_NDK=/xxx/you-old-ndk-folder, it works for me with android studio 3.0

-------------------------

ChunFengTsin | 2017-12-01 15:21:37 UTC | #29

I get it, thank you all !

-------------------------

