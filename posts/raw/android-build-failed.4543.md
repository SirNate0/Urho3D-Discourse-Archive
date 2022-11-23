CaptainCN | 2018-09-17 10:17:06 UTC | #1

I'm runing  ./gradlew build -PANDROID_ABI=armeabi-v7a
system: Windows 10

 [216/953] Running utility command for rapidjson
  FAILED: cmd.exe /C

... 

 ???????????
  ninja: build stopped: subcommand failed.

-------------------------

weitjong | 2018-09-17 06:56:28 UTC | #2

I guess when in Rome, do as the Romans do. Use gradlew.bat instead of ./gradlew.

-------------------------

CaptainCN | 2018-09-17 07:23:05 UTC | #3

:sweat_smile: I tried. Got follow errors.

 -- Detecting CXX compile features - done
  CMake Error at E:/test/Urho3D-me/CMake/Modules/CheckCompilerToolchain.cmake:193 (message):
    Could not check compiler toolchain as it does not handle '-E -dM' compiler
    flags correctly
  Call Stack (most recent call first):
    E:/test/Urho3D-me/CMake/Modules/UrhoCommon.cmake:123 (include)
    CMakeLists.txt:46 (include)


  -- Configuring incomplete, errors occurred!
  See also "E:/test/Urho3D-me/android/urho3d-lib/.externalNativeBuild/cmake/debug/armeabi-v7a/Source/Urho3D/tolua++-prefix/src/tolua++-build/CMakeFiles/CMakeOutput.log".
  ninja: build stopped: subcommand failed.

-------------------------

weitjong | 2018-09-17 07:33:02 UTC | #4

It’s a common pitfall for Windows host as our build system requires native compiler toolchain to be made available for host tool building. Read the online doc or do some search in the forum. Also make sure you are using master branch.

-------------------------

weitjong | 2018-09-17 08:33:54 UTC | #5

Also try to nuke your old build tree before retrying. Sometime previous failed attempts may get in the way.

-------------------------

CaptainCN | 2018-09-17 08:56:08 UTC | #6

Still failed.

![image|559x231](upload://oI9QuyDoFV8mKfJqHXDQv23YDgM.png) 

![image|676x416](upload://qVNi3xchTuBNl2jrjScs413zA1w.png) 
![image|403x215](upload://ytc8BZxAiGqAgQ2ZJUxM3Yjo5XP.png) 

What is ‘native compiler toolchain’ ？

-------------------------

weitjong | 2018-09-17 09:01:28 UTC | #7

If you don’t understand what that meant, perhaps you should start by disabling the LUA subsystem first. Our build system tries to build host tool using native compiler toolchain in one go while crosscompiling. This has been asked and answered a few times in the forum. It gets old for me. So, I am sorry if my response is not very useful.

-------------------------

CaptainCN | 2018-09-18 09:38:18 UTC | #8

I think this error not about lua.

![image|690x214](upload://uxJiEgS6DAVBlGg1EakmelkJmjy.png) 
I copy this command in a bat and run.
I got 
![image|209x79](upload://sJ26tqNqYkpljO3DJf1mhpmBS8Z.png) 

command too long.

-------------------------

CaptainCN | 2018-09-18 09:47:11 UTC | #9

I changed my pc language to English. And rebuild Urho3d.
Got error message in English:
![image|690x227](upload://A2qEGm3siyZS7BWpEevC1SrnS8I.png)

-------------------------

weitjong | 2018-09-19 00:38:49 UTC | #10

Yup, that’s another common pitfall for Windows users after managing to clear the compiler toolchain check. See https://discourse.urho3d.io/t/new-gradle-build-system-for-android-platform/4380/63. At this point I am also not sure why Windows 10 has this issue while it seems Windows 7 is fine.

-------------------------

Bluemoon | 2018-09-19 07:53:18 UTC | #11

This pitfall was really heartbreaking for me :sweat:

I even tried the response file solution but it seems not to work ( I might probably be doing something wrong) so I actually gave it a break for a while. It would be nice if there could be a solution

-------------------------

Modanung | 2018-09-19 07:54:53 UTC | #12

[quote="Bluemoon, post:11, topic:4543"]
It would be nice if there could be a solution
[/quote]

:man_facepalming:
It's called Linux.

-------------------------

Bluemoon | 2018-09-19 07:57:33 UTC | #13

:laughing::laughing::laughing:

-------------------------

weitjong | 2018-09-19 14:13:25 UTC | #14

[quote="Bluemoon, post:11, topic:4543"]
I even tried the response file solution but it seems not to work ( I might probably be doing something wrong) so I actually gave it a break for a while. It would be nice if there could be a solution
[/quote]

It may worth your while by getting yourself familiar with Docker. Perhaps I should not say much until the whole thing materialized but there is a good chance Windows users (or as a matter of fact users on any hosts that could run docker image) would be able to pull Urho3d prepared docker image from Docker Hub that targets a  specific platform, run it  locally to build the project, and get the build artifacts as the result.

-------------------------

