mcnito | 2021-07-28 10:03:44 UTC | #1

Hello,

I'm trying docker for first time, but it is not working for me (via script):

mcnito@mcnito-MINT01:~/Urho3D$ sudo script/dockerized.sh linux rake build install
groupadd: GID '0' already exists
runuser: user urho3d does not exist


Any help?

Thanks!

-------------------------

weitjong | 2021-07-28 12:17:21 UTC | #2

Follow the instructions on the new website page. You should not use “sudo” at all.

-------------------------

mcnito | 2021-07-28 13:12:13 UTC | #3

[quote="mcnito, post:1, topic:6935"]
script/dockerized.sh linux rake build install
[/quote]

Without sudo:

mcnito@mcnito-MINT01:/media/mcnito/LINUX_DATA/Urho3D$ script/dockerized.sh linux rake build install
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get http://%2Fvar%2Frun%2Fdocker.sock/v1.24/version: dial unix /var/run/docker.sock: connect: permission denied
docker: Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/create: dial unix /var/run/docker.sock: connect: permission denied.
See 'docker run --help'.

I'm following this instructions: https://urho3d.io/docs/getting-started/quick-start

-------------------------

weitjong | 2021-07-28 13:31:39 UTC | #4

Use “podman” which is daemonless or complete the post installation step when continue to use “Docker Engine”. https://docs.docker.com/engine/install/linux-postinstall/

Either way you should test run your setup with a simple Docker image before heading back to use the DBE images.

-------------------------

mcnito | 2021-07-28 13:55:11 UTC | #5

Thanks a lot!

Completing the post installation step worked for me.

I will take a look at podman anyway.


Thanks again.

-------------------------

mcnito | 2021-07-28 15:56:56 UTC | #6

Hi,

It's me again...

It worked perfect for linux and web, but on Android its failing:

Starting a Gradle Daemon (subsequent builds will be faster)

FAILURE: Build failed with an exception.

* What went wrong:
A problem occurred configuring project ':android:launcher-app'.
> Failed to notify project evaluation listener.
   > java.io.FileNotFoundException: /media/mcnito/LINUX_DATA/Urho3D/android/launcher-app/.cxx/ndk_locator_record_4t6d141t.log (No such file or directory)
   > Task with name 'externalNativeBuildDebug' not found in project ':android:launcher-app'.

* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 2m 3s


Any help?

Thanks :slight_smile:

-------------------------

weitjong | 2021-07-28 16:08:44 UTC | #7

Is your Urho3D project root mounted from somewhere else? If so, make sure you have write permission on the “/media/…”. The difference between Android build and other builds is that Android grade plug-in writes all over the places in the project root dir, while the rest just writes into “build/“ relative to the project root.

-------------------------

mcnito | 2021-07-28 22:30:32 UTC | #8

Thanks a lot again.

I ran script from /home (I will check permisisons later) and it worked (well, bypassed the step).

Now Im getting this error:

> Task :android:launcher-app:externalNativeBuildDebug FAILED
Build Urho3DPlayer_armeabi-v7a
ninja: Entering directory `/home/mcnito/Urho3D/android/launcher-app/.cxx/cmake/debug/armeabi-v7a'
ninja: error: '/home/mcnito/Urho3D/android/urho3d-lib/.cxx/cmake/debug/armeabi-v7a/lib/libUrho3D.so', needed by '../../../../build/intermediates/cmake/debug/obj/armeabi-v7a/libUrho3DPlayer.so', missing and no known rule to make it

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':android:launcher-app:externalNativeBuildDebug'.
> Build command failed.
  Error while executing process ninja with arguments {-C /home/mcnito/Urho3D/android/launcher-app/.cxx/cmake/debug/armeabi-v7a Urho3DPlayer}
  ninja: Entering directory `/home/mcnito/Urho3D/android/launcher-app/.cxx/cmake/debug/armeabi-v7a'
  
  ninja: error: '/home/mcnito/Urho3D/android/urho3d-lib/.cxx/cmake/debug/armeabi-v7a/lib/libUrho3D.so', needed by '../../../../build/intermediates/cmake/debug/obj/armeabi-v7a/libUrho3DPlayer.so', missing and no known rule to make it

Sorry for asking that much, I feel I'm close to the end...

-------------------------

weitjong | 2021-07-29 02:32:58 UTC | #9

You didn’t say how you ended up in such situation, so it is difficult to pinpoint the exact step that lead to such error. But based on the log, I think the Gradle build process believed it has built the Urho3D library targets and then proceeded to build other dependent targets. They failed because the dependency library was in fact not found. So, I believe your Android build tree is in an inconsistent state. To recover, you could try:

```
script/dockerized.sh android ./gradlew cleanAll
```

After that, redo the `rake build install` using DBE. If the above Gradle “cleanAll” task also gave you error then you will have to clean all the directories generated by Android Gradle plugin yourself. Look for those dir with “.cxx” and “build” using `find` command and nuke them. Good luck.

-------------------------

mcnito | 2021-07-29 14:08:51 UTC | #10

Hi,

This not worked. I've even tried in a clean Linux Mint installation, with the following commands:

```
git clone https://github.com/urho3d/Urho3D.git
cd Urho3D
script/dockerized.sh android rake build install
```

And I still get the same error:

> Starting a Gradle Daemon, 1 incompatible and 1 stopped Daemons could not be reused, use --status for details

...

> Task :android:launcher-app:externalNativeBuildDebug FAILED
Build Urho3DPlayer_armeabi-v7a
ninja: Entering directory `/home/mcnito/Urho3D/android/launcher-app/.cxx/cmake/debug/armeabi-v7a'
ninja: error: '/home/mcnito/Urho3D/android/urho3d-lib/.cxx/cmake/debug/armeabi-v7a/lib/libUrho3D.so', needed by '../../../../build/intermediates/cmake/debug/obj/armeabi-v7a/libUrho3DPlayer.so', missing and no known rule to make it

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':android:launcher-app:externalNativeBuildDebug'.
> Build command failed.
  Error while executing process ninja with arguments {-C /home/mcnito/Urho3D/android/launcher-app/.cxx/cmake/debug/armeabi-v7a Urho3DPlayer}
  ninja: Entering directory `/home/mcnito/Urho3D/android/launcher-app/.cxx/cmake/debug/armeabi-v7a'
  
  ninja: error: '/home/mcnito/Urho3D/android/urho3d-lib/.cxx/cmake/debug/armeabi-v7a/lib/libUrho3D.so', needed by '../../../../build/intermediates/cmake/debug/obj/armeabi-v7a/libUrho3DPlayer.so', missing and no known rule to make it


* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.

* Get more help at https://help.gradle.org

Deprecated Gradle features were used in this build, making it incompatible with Gradle 7.0.
Use '--warning-mode all' to show the individual deprecation warnings.
See https://docs.gradle.org/6.7/userguide/command_line_interface.html#sec:command_line_warnings

BUILD FAILED in 12m 26s
40 actionable tasks: 40 executed

**My question is:**

Should I try podman?
Should I try on any other Linux Distro?

Thanks!

-------------------------

weitjong | 2021-07-29 15:05:43 UTC | #11

The same Android DBE image is being downloaded and used over and over again without issue so far. As I understood on how the container technology works, I believe the host operating system has no bearing on your issue. Locally I use "podman" but our CI uses "Docker Engine", so again you can rule this one out. From the experience I also know that once a docker image is good to run then it would run equally well everywhere. The only thing that I think your host machine could fail the Android build is the amount of memory it has. Since you didn't paste the whole log, could it be possible that it actually had failed earlier on when building the library target?

You need to have at least 16 GB of memory or more. If you don't have that many memory in your host then you could scale the Gradle build system down to only build for a single Android ABI at a time, instead of all 4 ABIs in one go (x86, x86_64, armeabi-v7a, and arm64-v8a). You can specify the ABI by using the `ANDROID_ABI` gradle property like so:

```
script/dockerized.sh android ./gradlew -P ANDROID_ABI=armeabi-v7a build publishToMavenLocal
```

You can also tell Gradle to build the target separately.

```
script/dockerized.sh android ./gradlew :android:urho3d-lib:build
```

This would just build the Urho3D library alone. So, you can see more easily if it builds OK or not.

-------------------------

mcnito | 2021-07-29 16:04:37 UTC | #12

Thanks for your help and for being so kind.

I've tried this on clean urho3d folder:

> script/dockerized.sh android ./gradlew :android:urho3d-lib:build

And this is what i get:

FAILED: Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/Generated_Classes.cpp.o 
  /usr/bin/ccache /android-sdk/ndk/21.3.6528147/toolchains/llvm/prebuilt/linux-x86_64/bin/clang++ --target=aarch64-none-linux-android21 --gcc-toolchain=/android-sdk/ndk/21.3.6528147/toolchains/llvm/prebuilt/linux-x86_64 --sysroot=/android-sdk/ndk/21.3.6528147/toolchains/llvm/prebuilt/linux-x86_64/sysroot  -DHAVE_SINCOSF -DHAVE_STDINT_H -DSTBI_NEON -DTOLUA_RELEASE -DURHO3D_ANGELSCRIPT -DURHO3D_FILEWATCHER -DURHO3D_IK -DURHO3D_IS_BUILDING -DURHO3D_LOGGING -DURHO3D_LUA -DURHO3D_NAVIGATION -DURHO3D_NETWORK -DURHO3D_PHYSICS -DURHO3D_PROFILING -DURHO3D_STATIC_DEFINE -DURHO3D_THREADING -DURHO3D_URHO2D -DURHO3D_WEBP -ISource/Urho3D -I../../../../../../Source/Urho3D -Iinclude/Urho3D/ThirdParty -Iinclude/Urho3D/ThirdParty/Bullet -Iinclude/Urho3D/ThirdParty/Detour -Iinclude/Urho3D/ThirdParty/LuaJIT -g -DANDROID -fdata-sections -ffunction-sections -funwind-tables -fstack-protector-strong -no-canonical-prefixes -D_FORTIFY_SOURCE=2 -Wformat -Werror=format-security   -Wno-invalid-offsetof -Qunused-arguments -fcolor-diagnostics -Wno-argument-outside-range -include "/home/mcnito/Urho3D/android/urho3d-lib/.cxx/cmake/release/arm64-v8a/Source/Urho3D/Precompiled.h" -Winvalid-pch -O2 -DNDEBUG  -fPIC -fvisibility=hidden -fvisibility-inlines-hidden   -std=c++11 -MD -MT Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/Generated_Classes.cpp.o -MF Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/Generated_Classes.cpp.o.d -o Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/Generated_Classes.cpp.o -c ../../../../../../Source/Urho3D/AngelScript/Generated_Classes.cpp
  clang++: error: unable to execute command: Killed
  clang++: error: clang frontend command failed due to signal (use -v to see invocation)
  Android (6454773 based on r365631c2) clang version 9.0.8 (https://android.googlesource.com/toolchain/llvm-project 98c855489587874b2a325e7a516b99d838599c6f) (based on LLVM 9.0.8svn)
  Target: aarch64-none-linux-android21
  Thread model: posix
  InstalledDir: /android-sdk/ndk/21.3.6528147/toolchains/llvm/prebuilt/linux-x86_64/bin
  clang++: note: diagnostic msg: PLEASE submit a bug report to https://github.com/android-ndk/ndk/issues and include the crash backtrace, preprocessed source, and associated run script.
  clang++: note: diagnostic msg: 
  ********************
  
  PLEASE ATTACH THE FOLLOWING FILES TO THE BUG REPORT:
  Preprocessed source(s) and associated run script(s) are located at:
  clang++: note: diagnostic msg: /tmp/Generated_Classes-00e626.cpp
  clang++: note: diagnostic msg: /tmp/Generated_Classes-00e626.sh
  clang++: note: diagnostic msg: 
  
  ********************
  ninja: build stopped: subcommand failed.
  


* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.

* Get more help at https://help.gradle.org

Deprecated Gradle features were used in this build, making it incompatible with Gradle 7.0.
Use '--warning-mode all' to show the individual deprecation warnings.
See https://docs.gradle.org/6.7/userguide/command_line_interface.html#sec:command_line_warnings

BUILD FAILED in 21m 4s
16 actionable tasks: 16 executed

How can i get and share full log?

Thank you.

-------------------------

weitjong | 2021-07-29 16:21:09 UTC | #13

Since you didn't answer my question regarding the memory, I will assume your host has enough memory. You can try two things from here:

1. Clear the build cache inside the docker volume in case earlier build attempts have produced bad cached objects. After that, retry the build install step again.

```
script/dockerized.sh android ccache -Cz
```

2. Temporarily disable AngelScript subsystem by toggling off the `URHO3D_ANGELSCRIPT` build option.

```
URHO3D_ANGELSCRIPT=0 script/dockerized.sh android
```

Unfortunately currently we have a known issue with the AngelScript subsystem in the master branch that it may produce generated source code with extra large object size when compiled. Still, if you indeed running into this issue then it may mean you actually don't have enough memory and/or disk space.

Monitor your disk and memory usage while the DBE runs.

-------------------------

mcnito | 2021-07-29 18:14:29 UTC | #14

Hi again,

Sorry for not replying about the memory. My computer has only 8GB, but I've tried this:

> script/dockerized.sh android ./gradlew -P ANDROID_ABI=armeabi-v7a build publishToMavenLocal

And gave the same error.

I have also tried this:

> script/dockerized.sh android ccache -Cz

and this:

> URHO3D_ANGELSCRIPT=0 script/dockerized.sh android

And still failed.

But...

I've tried this:

> URHO3D_ANGELSCRIPT=0 script/dockerized.sh android ./gradlew :android:urho3d-lib:build

And worked!

But later I've tried this:

> URHO3D_ANGELSCRIPT=0 script/dockerized.sh android ./gradlew -P ANDROID_ABI=armeabi-v7a build publishToMavenLocal

and this:

> URHO3D_ANGELSCRIPT=0 script/dockerized.sh android ./gradlew -P ANDROID_ABI=armeabi-v7a build publishToMavenLocal

And both failed.

Error:

> Error while executing process ninja with arguments {-C /home/mcnito/Urho3D/android/launcher-app/.cxx/cmake/debug/armeabi-v7a Urho3DPlayer}
>   ninja: Entering directory `/home/mcnito/Urho3D/android/launcher-app/.cxx/cmake/debug/armeabi-v7a'
>   
>   ninja: error: '/home/mcnito/Urho3D/android/urho3d-lib/.cxx/cmake/debug/armeabi-v7a/lib/libUrho3D.so', needed by '../../../../build/intermediates/cmake/debug/obj/armeabi-v7a/libUrho3DPlayer.so', missing and no known rule to make it

So... does this confirm is a RAM problem? Extending swap partition should fix this?

Thanks, a lot, again :slight_smile:

-------------------------

mcnito | 2021-07-29 20:03:39 UTC | #15

Added 16GB to swap and trying again

![image|690x242](upload://m1y0fx9r8oyYDiF7AixHY81m3NP.png)

I will tell results :slight_smile:

-------------------------

mcnito | 2021-07-29 20:36:14 UTC | #16

Failed again, sure its my fault, but i dont know what to try :pleading_face:

![image|690x354](upload://iJyyi1MxvyQLieIjFRq6fhl2saB.png)

Tomorrow will be another day...

-------------------------

weitjong | 2021-07-29 21:30:29 UTC | #17

No, this time it might be my fault forgetting to tell you to delete the old build tree first before flipping the “URHO3D_ANGELSCRIPT” build option. Having said that, I think 8 GB is too little for Android build.

-------------------------

mcnito | 2021-07-30 08:18:17 UTC | #18

Hi,

I've tried this:

>rm -r Urho3D/
git clone https://github.com/urho3d/Urho3D.git
cd Urho3D
script/dockerized.sh android ccache -Cz
URHO3D_ANGELSCRIPT=0 script/dockerized.sh android ./gradlew -P ANDROID_ABI=armeabi-v7a build publishToMavenLocal

And.. failed:

![image|690x210](upload://yUMV9UPHav8tULpCBGufKfdFWGF.png)

Maybe I can try any alternative, If I do an step back, my plan was...

1) Get docker working for easily deploy to:

  a) linux, for developing -> done
  b) web, for sharing -> done
  c) android, for testing real perfomance on device -> fail

2) Find a good IDE for developing and a fast way to test/compile again and again (I think I can make a script that builds linux via docker and runs it locally).

3) Integrate standard C++ libraries, like AdMob ( https://firebase.google.com/docs/admob/cpp/quick-start ).

4) Finally, also deploy it for iOS (I know I will have to do it via cmake way).

So, I'm very close to step 2, where I will start to port an abandoned Away3D project.

I dont own a 16GB computer (I can buy RAM, if is the only solution).

Extending SWAP (to 16GB) did not helped.

Do you think that trying podman could help?

Maybe I have docker not installed correctly?


Thanks a lot, any advice would be apreciated.

-------------------------

weitjong | 2021-07-30 09:28:05 UTC | #19

You just simply need more RAM.

I recall one of the user who got memory issue before reported that increasing the max heap size to 8 GB in the “gradle.properties” file helps. I haven’t verified that personally though. So, take the above advise with a grain of salt. I fixed memory issue with my Android build by putting more sticks into the machine 😁

-------------------------

mcnito | 2021-12-11 12:14:35 UTC | #20

Hi @weitjong ,

Sorry for late reply, but until today I had no access to >= 16GB RAM.

Today, a friend gave me RAM sticks and I've tried, in a clean Urho3D installation with 20GB RAM, and I get the same error:

![image|690x239](upload://hOhi3sq1KkBXPjBDZGs1eltnbd1.png)

If I try:

> URHO3D_LIB_TYPE=SHARED script/dockerized.sh android rake build install

or

> URHO3D_LIB_TYPE=STATIC script/dockerized.sh android rake build install

or

> URHO3D_ANGELSCRIPT=0 script/dockerized.sh android ./gradlew :android:urho3d-lib:build

all of them work, but none of them allow me to build and .apk of my app, also no sample apks are build.

Any help would be appreciated. Im having a lot of fun with Urho3D and Im focused on web deployment now, but anyday I know I will want to make apks.

Thanks a lot.

-------------------------

tarzeron | 2021-12-11 15:10:02 UTC | #21

```
URHO3D_LIB_TYPE=SHARED script/dockerized.sh android rake build install
```
This command work on linux mint. On my system 64 GB RAM, but for build was used ~13GB. After first execute I get errors, and I just executed the same command without cleaning and second build was successfully.

Why you use dockerized script? 

You can build without docker with this script and environment on linux mint:
```
# !/bin/sh 
export ANDROID_NDK=~/Android/Sdk/ndk/21.0.6113669
export ANDROID_SDK=~/Android/Sdk
export PATH=$ANDROID_NDK/toolchains/x86_64-4.9/prebuilt/linux-x86_64/bin:$ANDROID_NDK/build:$ANDROID_NDK/prebuilt/linux-x86_64/bin:$ANDROID_SDK/tools:$ANDROID_SDK/tools/bin:$ANDROID_SDK/platform-tools:$PATH

export URHO3D_HOME=~/workspace/Urho3D/android/urho3d-lib/build/outputs/aar

cd ./android

gradle wrapper --gradle-version 6.2 --distribution-type all
./gradlew Build

```
![Снимок экрана в 2021-12-11 17-08-10|630x500](upload://dEdBNM0a7QMkIY8gV1awSaNvhQJ.png)
![Снимок экрана в 2021-12-11 17-08-05|630x500](upload://sIwm1U7ibgbCL32mZyu1Ivue6j3.png)

-------------------------

mcnito | 2021-12-11 19:43:49 UTC | #22

Hi,

Thank you for your help.

I'm trying to do EXACTLY as you do, but Im doing something different...:

![image|661x264](upload://6ElISJI5sFyaZ2zMLJ8meuJ7aId.png)

I think only different thing could be Java version (btw If I use Gradle 6.4 I get other error).

Could you tell me your Java version please?

![image|618x85](upload://m2BrT57iFJO1fjZPaZHPHj9AE2B.png)

Thanks a lot!

-------------------------

tarzeron | 2021-12-11 22:00:17 UTC | #23

[quote="mcnito, post:22, topic:6935"]
Could you tell me your Java version please?
[/quote]

```
java --version
openjdk 11.0.11 2021-04-20
OpenJDK Runtime Environment (build 11.0.11+9-Ubuntu-0ubuntu2.20.04)
OpenJDK 64-Bit Server VM (build 11.0.11+9-Ubuntu-0ubuntu2.20.04, mixed mode, sharing)
```

I use this commit, it works with the SDK and NDK versions that I have installed
`3c4a0a54894e2ff346aa9f869af4e856cd1cc3ca`

The previous script is not what you need now, I use it to build my project. You need this script now, it will build the library and application with examples.

```
# !/bin/sh 
export ANDROID_NDK=~/Android/Sdk/ndk/21.0.6113669
export ANDROID_SDK=~/Android/Sdk
export PATH=$ANDROID_NDK/toolchains/x86_64-4.9/prebuilt/linux-x86_64/bin:$ANDROID_NDK/build:$ANDROID_NDK/prebuilt/linux-x86_64/bin:$ANDROID_SDK/tools:$ANDROID_SDK/tools/bin:$ANDROID_SDK/platform-tools:$PATH
gradle wrapper --gradle-version 6.2 --distribution-type all
./gradlew Build
```

To save disk space and speedup build you can set the target processor architecture in gradle.properties, for example:
`ANDROID_ABI=armeabi-v7a`

-------------------------

