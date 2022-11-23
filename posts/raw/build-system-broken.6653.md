WangKai | 2021-01-16 15:53:45 UTC | #1

I have tested on Windows and Android. Failed to build them for both platforms.

https://github.com/urho3d/Urho3D/issues/2754
https://github.com/urho3d/Urho3D/issues/2755

-------------------------

1vanK | 2021-01-06 15:18:59 UTC | #2

I have never used `script\cmake_vs2019.bat`. This way works for me:

```
set "PATH=c:\Programs\CMake\bin;c:\Programs\Doxygen\;c:\Programs\Graphviz\bin\;c:\Program Files (x86)\HTML Help Workshop\"

mkdir Build
cd Build
cmake.exe ../Urho3D -G "Visual Studio 16" -A Win32 -DURHO3D_OPENGL=1 -DURHO3D_ANGELSCRIPT=1 -DURHO3D_LUA=1 -DURHO3D_STATIC_RUNTIME=1 -DURHO3D_SAMPLES=1 -DURHO3D_TOOLS=0 -DURHO3D_DOCS=0 -DURHO3D_LIB_TYPE=STATIC -DURHO3D_DATABASE_ODBC=1 -DURHO3D_GENERATEBINDINGS=1

```

-------------------------

WangKai | 2021-01-07 14:07:20 UTC | #3

Thank you @1vanK and your way works. I still expect the scripts got fixed though.

-------------------------

WangKai | 2021-01-07 14:13:40 UTC | #4

I've done most of my work on Tracy integration with my limited spare time, however, I'm stuck with current Android building which futher prevents me from analyzing a potential issue on Android platforms I noticed days ago.

Still wish every commit on the master branch working though sometimes it is not easy to cover every platform Urho supports.

-------------------------

weitjong | 2021-01-09 06:27:26 UTC | #5

When in doubt you can always use the git blame to trace the commit that introduced the code change and try to understand the rationale from the commit message and the rest of the changes in the same commit.

https://github.com/urho3d/Urho3D/commit/7937119e634ddf617d57d9e5fe90f2036d3cd207

In short there is nothing wrong with the provided build script, `cmake_generic.bat` and its derivaties like `cmake_vs2019.bat`. However, you have to adjust to use the expected argument format. If it has command line argument parsing issue then it would have failed in the CI/CD. The *.bat and *.sh are all tested in the CI/CD workflow. Note that for disabling LUA subsystem, you must pass this to turn off both  LUA vanilla and JIT build options: `-D URHO3D_LUA=0 -D URHO3D_LUAJIT=0`.

As for the Android cross-compiling on Windows host system, it should work with a caveat or two. This has been asked many times and I am tired of answering it in detail again. Basically if your build config requires a native host tool to be built (like "buildvm" for Lua or whatever) then you are going to need a native compiler toolchain (like MinGW).

BTW, I have a new pet project which would occupy most of my spare time. I won't be active in Urho3D development for the time being but I will still come to the forum once in awhile.

-------------------------

WangKai | 2021-01-14 14:00:45 UTC | #6

Hi @weitjong ,

I found that in the latest buid system for Android, when building Urho3DPlayer.so, SHARED version of Urho3D is depended on. I was a little confused, since I remembered it was STATIC Urho3D as the default configuration, am I right?

This means the default configuration in Android Studio will lead to an error when building `launcher-app` -
```log
Build command failed.
Error while executing process /usr/bin/ninja with arguments {-C {urho3d_folder}/android/launcher-app/.cxx/cmake/debug/armeabi-v7a Urho3DPlayer}
ninja: Entering directory `{urho3d_folder}/android/launcher-app/.cxx/cmake/debug/armeabi-v7a'

ninja: error: '{urho3d_folder}/android/urho3d-lib/.cxx/cmake/debug/armeabi-v7a/lib/libUrho3D.so', needed by '../../../../build/intermediates/cmake/debug/obj/armeabi-v7a/libUrho3DPlayer.so', missing and no known rule to make it
```

-------------------------

weitjong | 2021-01-14 14:19:00 UTC | #7

Probably you have a problematic build tree again. You are right that the build system currently always defaulted to STATIC and when using the default build config the `libUrho3D.so` won't be built at all. If it does then something is wrong with your build tree. Not the build system itself. I am very sure of that. Have you tried to nuke your build tree and retry? I have added a custom Gradle task called "cleanAll" which should clean up everything as its name implies.
```
$ ./gradlew cleanAll
```

HTH

-------------------------

WangKai | 2021-01-14 14:40:30 UTC | #8

Thank you for the reply :slight_smile: 

I did `git clean` for many times and I'm trying `cleanAll`.

I'm not very familiar with the build system of Urho, however, it seems that on Android, if it's not Urho3D itself (Urho3DPlayer.so in our case, as a SHARED), `libUrho3D.so` will be used as the dependency, please correct me if I'm wrong -
https://github.com/urho3d/Urho3D/blob/36cabe96398da686cd220f66920f89b124d7c2d2/cmake/Modules/FindUrho3D.cmake#L87

-------------------------

weitjong | 2021-01-16 15:54:01 UTC | #9

The build tree is configured in `.gitignore`, so the `git clean df` does not do what you expect it to do. You have to nuke the build tree using `rm -rf` manually. You can do that using the `cleanAll` task I mentioned specifically for Android build with Gradle.

I think you already know this. For Android build, the main target that would be eventually shipped in the APK as "*.so", regardless of which Urho3D library type you use. The main target can still depend on any  library types: STATIC, SHARED, or even OBJECT (CMake-specific).

For the "Launcher app" that Urho3D project provides, the app itself is a launcher of all the 50+ samples (main targets), including the Urho3DPlayer (main target) as the script player. The launcher app allows user to pick one of the samples to launch OR to pick one the AngelScript/Lua scripts to play (by launching Urho3DPlayer behind the scene), one at a time. Again, each main target would contribute to one *.so, regardless of which Urho3D library type you use. The difference is whether the main target shares just one Urho3D library (SHARED lib type) or the main target has individually statically linked the engine into (STATIC lib type). The build system would only include the `libUrho3D.so` in the final APK for the former case.

So, to answer your question. The "Urho3DPlayer" will always depend on "Urho3D" library. The "libUrho3DPlayer.so" will always be built as SHARED, as that is the target type Android main target should be. The "libUrho3D.so" will be built and included in the APK when and only when the `URHO3D_LIB_TYPE` is set to SHARED in the build config.

Now in my last refactoring for Android build system I have made one important change in the STATIC build configuration in order to reduce the size of the final APK. This is achieved by only setting up the Urho3DPlayer script player as the main target and excluding all the other samples. So now the launcher app only allows user to pick the scripts to run via Urho3DPlayer, and all samples are not listed anymore. I think it is easy to understand the main target will be much bigger in size if Urho3D engine is statically linked. Putting 50+ of them inside one APK made the final APK becomes very big. It would also require more memory and disk space during build time. GitHub CI/CD workflow could not meet the requirement before I made the change. The SHARED build config is not changed in this respect. Thus, the final APK will either have:

* SHARED: libUrho3D.so, libUrho3DPlayer.so, lib01_HelloWorld.so, lib02_HelloGUI.so, and so on
* STATIC: libUrho3DPlayer.so

In other words, it does not make sense anymore to have a build config that uses STATIC lib type but disables both the Angelscript and Lua subystems for Android build, at least for the launcher-app module. I was forced to wrap up my work in a rush, so I am sorry it is not properly documented in the online doc.

-------------------------

WangKai | 2021-01-16 11:21:38 UTC | #10

Hi @weitjong ,

Thank you for the detailed explaination, I think the non-clean build tree was the issue. During setting up the Android Studio, it introduced some issue.

I have another question about Android Studio on Linux and I wonder if you know the answer. 
How can I set the environment variables so I can affect the gradle script used in Urho. 

e.g I add `export URHO3D_LUA=0` in `~/.bashrc` or `~/.bash_profile` seems does not affect the gradle in Android Studio.

Regards,
Kai

-------------------------

WangKai | 2021-01-16 14:18:01 UTC | #11

And how can I mark @weitjong 's last reply as the solution? Only **Support** category supports this feature?

-------------------------

Modanung | 2021-01-17 04:01:24 UTC | #12

Yes, that would require moving the thread - and refresh the page - before being able to mark a solution.

...or an admin/leader/moderator taking that initiative.

-------------------------

weitjong | 2021-01-17 03:32:07 UTC | #13

Glad to hear you have fixed your issue.

Your last question about the environment variable is not related to Urho3D specifically. It is a general question that many Linux newbie would have asked. Personally, I would set (and export) the env-var in the `~/.bash_profile`. The catch is, this file is only automatically sourced one time only during interactive shell login. So, you have to logout/login again to make it effective. If you want to keep using the current login session but want the change on the file to be applied immediately then you have to do `source ~/.bash_profile` manually yourself.

-------------------------

WangKai | 2021-01-17 08:56:22 UTC | #14

It's interesting that I tried the ways you use, however, there were still some issues. Maybe it's also dirty build tree related? I'd try it again later when I can find some time. Thank you @weitjong !

-------------------------

weitjong | 2021-01-17 12:05:40 UTC | #15

In the latest master branch, you need to disable both LUA and LUAJIT to disable it. Just URHO3D_LUA won’t do it anymore. At the time i made the change to auto-enable the JIT on the platform that support it, I didn’t think about this implication. Ideally, when LUA is off then both should be configured to off. Contribution is welcome to rectify this.

-------------------------

WangKai | 2021-01-17 13:34:19 UTC | #16

Hi @weitjong , I also find that I cannot build Urho3D successfully from Android Studio, while I can just use command line `./gradle build` successfully, w/ or w/o build options. I noticed that you have commited Android Studio build support recently.

Thanks.

-------------------------

weitjong | 2021-01-17 14:35:16 UTC | #17

I don't have any issue with CLI or with Android Studio or with IntelliJ, the last time I tried it. In the end all are just using Gradle the same.

-------------------------

WangKai | 2021-01-17 15:24:44 UTC | #18

I wonder if it is possible for you to show me you the versions of Android Studio, grade plugin, sdk, ndk, and project settings of Urho in Android Studio? 

I guess I may sound like a rookie, last time I have spent a lot of time fixing issues for Android and set up project besides libUrho but last pulling from upstream seems breaks Urho itself. There must be something wrong (on my side)

-------------------------

