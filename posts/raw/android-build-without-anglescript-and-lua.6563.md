extobias | 2020-11-24 00:23:08 UTC | #1

Hi there, 
I'm trying to build a just cloned copy from the repository but without Angelscript and LUA, but it's not working, its compiling ThirdParty/AngelScript and ThirdParty\LuaJIT. It used to work with the command

>  gradlew.bat -P ANDROID_ABI=arm64-v8a -P URHO3D_ANGELSCRIPT=0 -P URHO3D_PCH=0 -P URHO3D_WEBP=0 -P URHO3D_LUA=0 -P URHO3D_LUAJIT=0 build

Also I've added URHO3D_LUAJIT_AMALG=0 but the result it's the same.
I'm missing something?
Cheers

-------------------------

Modanung | 2020-11-24 10:16:54 UTC | #2

Try prefixing `-D` to the flags. Or is `-P ` gradle logix? :confused: [#gradle-to-crave]()

[quote="weitjong, post:4, topic:6550"]
I am done with Urho3D for now.
[/quote]

[Dry](https://gitlab.com/luckeyproductions/dry) has Lua and D3D ripped out - and shorter flag names, naturally - seems like you wouldn't miss either.
[spoiler]
Although you _are_ in [bat country](https://grahamscrackers.files.wordpress.com/2012/03/batcountry.jpg).
[/spoiler]

-------------------------

extobias | 2020-11-24 13:56:05 UTC | #3

From doc https://urho3d.github.io/documentation/HEAD/_building.html#Building_Android

> The Gradle properties can be passed by using "-P" Gradle option, e.g.: "./gradlew -P URHO3D_LUA=0 build" to build without Lua subsystem

wait @weitjong is out too? :scream:

-------------------------

extobias | 2020-11-25 21:47:53 UTC | #5

I think only environment variables are taken by the new build system. 
Is this deliberately removed?  I could submit a PR (based on previous versions of the file) to support again command line options

-------------------------

WangKai | 2020-11-26 03:19:34 UTC | #6

Hi,

I think you can change these parameters to apply the build flags ( e.g. `
-D URHO3D_LUA=0`):
https://github.com/urho3d/Urho3D/blob/eb0e7677f67296a318fa7ad3404b43a20b2cfdd0/android/urho3d-lib/build.gradle.kts#L51
https://github.com/urho3d/Urho3D/blob/eb0e7677f67296a318fa7ad3404b43a20b2cfdd0/android/launcher-app/build.gradle.kts#L48

Hope it helps!

-------------------------

extobias | 2020-11-26 14:19:08 UTC | #7

Yes, you're right but by this way options are hardcoded in the build file. Before you could pass this options through command line.

-------------------------

WangKai | 2020-11-26 16:05:42 UTC | #8

I didn't try but I think you can try to modify the scripts to achive this-
https://stackoverflow.com/questions/34875637/how-to-pass-multiple-parameters-in-command-line-when-running-gradle-task

-------------------------

extobias | 2020-11-26 17:56:44 UTC | #9

I've found a way with previous build files and submit a PR. Still it would be nice to know why this changes were deliberately removed. Thanks anyway.

-------------------------

dertom | 2020-11-26 18:35:10 UTC | #10

when I see it right all you need to do is to export the cmake-options as environment-variable.

In liinux:
```
export URHO3D_ANGELSCRIPT=0
```

I guess in win (not sure :) ):
```
set URHO3D_ANGELSCRIPT=0
```
And then call gradlew

ps: for me to compile the example at all I had to set URHO3D_LIB_TYPE=SHARED

-------------------------

weitjong | 2020-11-29 12:32:14 UTC | #11

Sorry for late answer. In the last Gradle build system refactoring I have decided to remove the support for using "-P" to pass through the build option in order to simplify the build script and to reduce the possibility of conflict. The documentation file has been updated accordingly. If you guys ever look at the commit itself, you know it is intentional. Note that the site is no longer updated automatically anymore.
https://github.com/urho3d/Urho3D/commit/0d4e0388277cf3419e35ac8a9895aca6f8105e7d

Using "rake" command, the build option can be passed like this:
```
$ rake URHO3D_LIB_TYPE=SHARED URHO3D_ANGELSCRIPT=0 PLATFORM=android
```
It works on all host systems with Ruby/Rake installed. The last `PLATFORM` env-var is not needed when the command is invoked inside a running Android DBE docker container.

It is also possible to use "gradlew" directly like this:
```
$ URHO3D_LIB_TYPE=SHARED URHO3D_ANGELSCRIPT=0 ./gradlew build
```
However, this won't work on Windows. You may have to create a simple wrapper yourself to set the env-var before invoking gradlew.

-------------------------

extobias | 2020-11-29 12:32:12 UTC | #12

That's ok, I didn't know that the doc page doesn't update anymore, so I thought that you can still pass the options from the list. Well I guess that if it was intentionally removed we have revert the PR

-------------------------

dertom | 2020-11-30 11:45:48 UTC | #13

[quote="extobias, post:12, topic:6563"]
That’s ok, I didn’t know that the doc page doesn’t update anymore
[/quote]

The problem is that the docs of 1.7.1 are shown as default (can we change this somehow?). You need to set this to 'HEAD' (to be honest, I also struggled with that)
![image|337x249](upload://dqM6rISsmgT1qGmVhb6guFnmXBg.png)

-------------------------

extobias | 2020-11-30 13:26:27 UTC | #14

In HEAD still says that you have a list of  supported Gradle properties.

-------------------------

weitjong | 2020-12-04 02:50:55 UTC | #15

Slightly off-topic and for those who has not keep track of all the recent threads. The migration from Travis CI to GitHub Action CI/CD was kind of being rushed. The new CI/CD workflow has not reached the feature parity with the old one yet when I made the cut over. The site documentation update is one of the thing missing. There are people trying to play "politic" in this project. May be not the best way to describe it but I have lost interest to complete what I have started. So, let the project die slowly and let those people happy.

-------------------------

Modanung | 2020-12-05 01:07:03 UTC | #16

[details=Let's run...]
[![](https://gitlab.com/luckeyproductions/dry/-/raw/master/SourceAssets/DryLogo.svg)](https://gitlab.com/luckeyproductions/dry)

[![](https://assets.gitlab-static.net/uploads/-/system/group/avatar/10302039/Tools.png?width=96)](https://gitlab.com/explore/projects?tag=Dry)
[/details]

-------------------------

extobias | 2020-12-04 20:10:32 UTC | #17

Sad news indeed, but somehow you could see it coming. There is anywhere some doc about the features missing in the new workflow? Just in case that someday someone want to take the lead. 
And @weitjong thanks for your  contribution.

-------------------------

weitjong | 2020-12-05 03:03:21 UTC | #18

There is no roadmap nor migration plan. In fact I didn't even know how to do GitHub Actions workflow a few months back when I started, the main reason I did it is simply to learn new skill for myself. Anyway, one can just compare between the old `Rakefile` and the new `rakefile` to spot any missing logic not yet migrated over. It is an apple to orange comparison though as the underlying design has changed.

-------------------------

