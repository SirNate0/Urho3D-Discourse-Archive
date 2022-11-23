Azaratur | 2019-04-05 09:06:46 UTC | #1

Latest question before going in a meeting to decide which engine use for our newer projects.

We release a lot of game for android using NDK i read in the forum someone that says we may use 15c.

I did a fast test using latest ndk and i got a clang.exe error, so i have to ask it.
Which version of ndk should be used?

-------------------------

weitjong | 2019-04-05 11:02:46 UTC | #2

The latest recommended approach for Android build is to use “embedded” NDK-bundle from Android SDK, instead of using standalone NDK.

-------------------------

johnnycable | 2019-04-05 15:04:27 UTC | #3

Go with the latest version unless you need an old one because of some sort of  backward compatibility. 
Regarding this, I've used as old as 12b without problems.

-------------------------

Azaratur | 2019-04-05 16:18:46 UTC | #4

I had a little problem with an already known issue.. (cmd.exe command too long) but i guess i fixed it by manually change the build.ninja files.
It was annoying but necessary.
Basically when a string is longer than 7800 char i cut the string and save in a file in the same directory and leave at its place this kind of command:
POST_BUILD = cmd.exe /C azafix6.txt

This seems did the trick.

-------------------------

weitjong | 2019-04-06 04:21:21 UTC | #5

Just wonder how many places you need to patch it. IMHO, this is a bug in the CMake/ninja generator when it is generating on Windows 10 host system. The bug does not appear when it is generating on Windows 7 host system, i.e. it knows when to use the response file correctly. To make it worse, the Android plugin for Gradle uses its own embedded `CMake` from the Android SDK and not the standalone `CMake` installed on the host system. Thus, upgrading the latter does not fix this issue. Someone should log this issue to Google Android dev team or at least bring the attention to the dev who has the bright idea of forking CMake inside the Android SDK package.

-------------------------

johnnycable | 2019-04-06 16:13:10 UTC | #6

[quote="weitjong, post:5, topic:5079"]
Android plugin for Gradle uses its own embedded `CMake` from the Android SDK and not the standalone `CMake` installed on the host system
[/quote]

There's a renowned cmake bug on Android running since something 3.0x to 3.9 I think, I can't recall exactly, but I can check my notes if you need. So there's no escaping using embedded Android cmake, which, in turn, has got "optimized" for the platform so that it "overperforms", for instance while building ninja/cmake, and... well you got the picture.

-------------------------

weitjong | 2019-04-06 17:19:49 UTC | #7

I can probably understand why they need to do that quickly at the time. It may seem to be a good idea to fork and fix the bug in-house and shipped it as part of their package. Hey, even we do that with our 3rd-party libs. The problem is, their CMake version appears to stay at 3.6.4111459 while the upstream has moved beyond that version with new improvement on its side too. Anyway, that's not my point of bringing this up. My point is, their embedded (read "optimized") CMake/ninja generator does not do its job well and they probably don't know it yet.

-------------------------

Bluemoon | 2019-04-06 17:36:00 UTC | #8

Now I'm very much interested in how you did this cause I've been trying to get this same thing resolved for like ages.

Hope you don't mind sharing the details? I would really appreciate

-------------------------

Azaratur | 2019-04-07 08:38:52 UTC | #9

Here i am!
Well to be honest i don't know yet, i was compiling it when i was in office friday evening and i went home.
I will let you know on monday if everythings went fine.
Anyway i'll try to explain what the cause is and how we could do the fix (if mine did not work).

Basically ninja create some files named build.ninja those file try to call "cmd.exe /C (path)" where path is a long string.
What is the problem?
The problem is that cmd.exe can only handle 8192 char in 64 bit or 2100 and something in 32bit.
Microsoft suggest to use shorter name (fuck you microsoft) or use a txt file with the parameters on it as for example:
cmd.exe /c file.txt

So i did a very annoying job, i got every build.ninja file that was generated and manually scroll searching line longer than 7900 char.
I found that eventually those are 4-5 line per arm.
BE CAREFULL if you do this, modify only the line with cmd.exe.
There are other long lines but those has no any problem.
I cut off the text from there and create a txt file in the same path, and add the filename.txt where i removed the line.

I know it's quite difficoult to follow, also i am not english native so this is even worst! 
Let me know!

-------------------------

weitjong | 2019-04-07 09:02:18 UTC | #10

You don't need to explain the root cause again because it is a known issue already to us. I just want to know how many places you need to patch it. If it is only a few of them and I can get a regex pattern to isolate them then I can probably cook up a post-cmake step *.batch file similar to what we have in "script/.bash_helpers.sh" to auto-patch the generated build tree. The thing is, I don't have Windows 10 at home so I cannot get this information myself. I don't work with Urho3D while I am at office.

-------------------------

Azaratur | 2019-04-07 10:42:10 UTC | #11

[Bluemoon](https://discourse.urho3d.io/u/Bluemoon) Ask me! :slight_smile:

-------------------------

Azaratur | 2019-04-07 10:43:00 UTC | #12

I will tell you something more on monday, i wanna be totally sure that everythings works as intended.

-------------------------

weitjong | 2019-04-07 16:32:06 UTC | #13

I just realized the Android SDK Manager now provides a newer CMake version (3.10.2.4988404). Are you using the newer version already?

-------------------------

Azaratur | 2019-04-07 18:24:44 UTC | #14

I checked for updates friday, so if they did not update in this 3 days i guess i have latest cmake.

-------------------------

Bluemoon | 2019-04-08 09:56:12 UTC | #15

Sure I'm asking :smile:

The command line length error of ninja on Win10 has had my head spinning for some months now. Getting it resolved would really be great

-------------------------

Azaratur | 2019-04-08 10:01:12 UTC | #16

Unfortunately my method did not work. I am trying something else but i have a bad feeling about this.

-------------------------

Azaratur | 2019-04-08 10:15:34 UTC | #17

We had an issue 2 years ago with android sdk, basically it did not update correctly and we got a lot of issue.

I have a clean computer here in my office i will install android studio from zero and try there.

We decide to use this engine so i have to let it works.

-------------------------

Bluemoon | 2019-04-08 10:25:04 UTC | #18

Wow :disappointed:

It can really be frustrating sometimes. I gave up for a while but will still return back. I need to explore the possibilities of games on mobile and my bias has been so heavy towards Urho3D.

-------------------------

Azaratur | 2019-04-08 10:40:58 UTC | #19

We have to release a lot of games on 3d for mobile and for html5, honestly speaking this engine works very well on html5 in terms of performance and in size (less to download).

-------------------------

Azaratur | 2019-04-08 11:25:31 UTC | #20

I don't want speak too earlier but with new android (released march 2019) and some modification to the gradle settings of the engine ninja rules are changed a bit.. I hope it will work correctly!

-------------------------

Azaratur | 2019-04-08 13:21:33 UTC | #21

@weitjong I am currently doing another test but i found a way to use standard cmake/ninja to android studio. Do you need it?

-------------------------

weitjong | 2019-04-08 15:15:42 UTC | #22

If you can share it here where we can all see it, sure, although I actually not sure what you meant by "standard cmake/ninja". I just do whatever it takes to make my build works and I did the Urho3D build migration to Gradle without copying from others. :)

-------------------------

Azaratur | 2019-04-08 15:17:35 UTC | #23

@Bluemoon @weitjong
I think i did it.. It's compiling all the sample right now so i am not totally sure but i never reached this point!

I am not sure why but even if i installed the newer version of cmake android studio keep using the older one. So i decide to force it and it went good.

You can force android studio to use the new cmake version by editing the local.properties in the engine root and add:
cmake.dir=c:\\Path\\To\\Android_Studio\\cmake\\3.10.2.4988404

You could also force the unmodified version of cmake there, but i am not sure how android studio will react to that.

-------------------------

weitjong | 2019-04-08 15:18:24 UTC | #24

That's a good news to all on Windows! I suppose you can ask the SDK Manager to uninstall the older cmake version first.

-------------------------

Azaratur | 2019-04-08 15:18:54 UTC | #25

ahaha unfortunately android studio will re-install that when you build!!!

-------------------------

Azaratur | 2019-04-08 15:20:52 UTC | #26

@Bluemoon If you think to try it again let me know if this work for you too.

-------------------------

weitjong | 2019-04-08 15:35:42 UTC | #27

I use IntelliJ IDEA (big brother of Android Studio). After uninstalling, it got reinstalled back too. Fortunately, on Linux, either versions work fine.

-------------------------

Azaratur | 2019-04-08 15:37:24 UTC | #28

I suppose there is a sort of cache or settings somewhere, i did search it for a while but i gave up and search for another solution.

Sample compiled now is merging all together.. Finger cross

-------------------------

weitjong | 2019-04-08 15:40:14 UTC | #29

I think if it is re-downloaded during the build then it is something with our Gradle build script. I need to double check if I have accidentally hard-code that version anywhere. Mostly probably not though.

-------------------------

Azaratur | 2019-04-08 15:42:25 UTC | #30

I searched for the reference even on the engine files but did not found it.

-------------------------

weitjong | 2019-04-08 15:50:34 UTC | #31

I can confirm that.... then it is hard-wired inside the Android plugin for Gradle. :man_facepalming: But if this is the case then other peoples will face it too. Will google that tomorrow when I have time.

-------------------------

weitjong | 2019-04-09 15:38:36 UTC | #32

Just did a quick search this morning. I think it is because the Android plugin still defaulted to the lower version, but it should be configurable in our build script, to explicitly specify the version number we want to use. Later I will try to configure that and test. Incidentally I have a new dev branch `gradle-upgrade` which also exhibits the same issue insisting on re-downloading the older version.

-------------------------

Azaratur | 2019-04-09 08:16:59 UTC | #33

Ok so yesterday i build the engine.
When i try to launch the apk i got an error:
Createprocess command too long..
So now is ninja that fails..

In any cases the apk is created..
So probably we cannot run the apk directly from android studio but we can create it (create apk command, will test it and let you know).
As far as i know when you click run in android studio it did not create an apk it will compose the resources and install all on the phone, so this problem may be not an issue.


Apk did not work and the fault here is that MKLINK did not work (assets are empry except for the links).
I will copy the resources there and try to create the apk again.

We use cocos2dx often and they simply use a task to copy the resources when you build to android, maybe this will fix the issue for every users?

-------------------------

Azaratur | 2019-04-09 13:37:56 UTC | #34

Ok.. I give up.
Did not found any way to accomplish this.

Will probably work on it on mac.

-------------------------

Bluemoon | 2019-04-09 13:41:08 UTC | #35

Wow

Anyways, I made the manual changes to the ninja build files by creating the response files by hand for all the arch and so far the build is going on well... I just hope it completes without issue

-------------------------

Azaratur | 2019-04-09 13:50:24 UTC | #36

Unfortunately it will most probably fails in "createprocess" when you try to compile the apk or launch it.
In any cases let me know if you find a way, i honestly lose too much time on it.

We prefer to use windows since most of our tools are there, but in worst cases we can use mac.

-------------------------

weitjong | 2019-04-09 15:13:37 UTC | #37

I understand your frustration. That's why it is a long outstanding known issue. There is little thing we could do on our side as the issue is not in our build script.

The good news is, I figure out how to keep the older CMake version out. The launcher-app seems to be running fine in a quick emulator test run after a clean rebuild using CMake 3.10.2. I will push that out shortly.

-------------------------

Azaratur | 2019-04-09 15:29:32 UTC | #38

There should be a way to "limit the issue" but i know it will be very annoying.
Basically it's crashing because the linking is too long, reducing drastically the folder/subfolder MAY be reduce the problem.
Most of the file which cause the issue are the third part library.

But i know it's just a temporary fix, since adding more library will cause the issue to reapper.

-------------------------

weitjong | 2019-04-09 15:30:12 UTC | #39

BTW, do you happen to have Win7 in your shop? It has been reported to build just fine on Win7.

-------------------------

Azaratur | 2019-04-09 15:31:41 UTC | #40

I don't have a shop! :smile:
We don't have windows 7 installed in any machine.
Will try on mac this evening.

-------------------------

johnnycable | 2019-04-09 15:37:02 UTC | #41

What if you try on mingw or Windows Subsystem for Linux, I mean something which allows you to work "unix like" on win?

-------------------------

weitjong | 2019-04-09 15:37:59 UTC | #42

I will be merging my `gradle-upgrade` dev branch to master soon after the latest round of CI build passed. Finger cross. The changes include specifically requested Android Plugin to use the latest CMake version. Now I don't know whether the Ninja generator in this latest version has fixed this particular issue or not, but I think it should worth your while to retry one more time.

-------------------------

Azaratur | 2019-04-09 15:41:31 UTC | #43

@weitjong when it's up i will surely retry but i won't lose too much time on it.

@johnnycable i can try that

-------------------------

weitjong | 2019-04-09 16:21:19 UTC | #44

Someone else try that in the past and, if I recall it right, didn't report back with good news. At one time I also believe WSL could work too, but then again if it is not fully tested then there are bound for small issues. It is really up to the person who has tried it has the capability and luck to figure the issues out or not.

-------------------------

weitjong | 2019-04-09 16:40:20 UTC | #45

I just merged the changes to master branch. Good luck.

-------------------------

Azaratur | 2019-04-10 08:20:44 UTC | #46

I am doing a test on mac right now, will test on pc later.

-------------------------

Azaratur | 2019-04-10 12:11:30 UTC | #47

@weitjong Android studio uses gradle 4.10.1 and buildtool 3.3.2
https://developer.android.com/studio/releases/gradle-plugin

-------------------------

weitjong | 2019-04-10 14:01:49 UTC | #48

Our builds are IDE-agnostics. In fact it can be built just by using Gradle wrapper on a command line. Unless you wanted to say you actually having a problem with Android Studio after the Grade version upgrade, which I doubt as I have tested it to be working fine with IntelliJ IDEA. The way I understood it, both IntelliJ IDEA and Android Studio simply rely on the Gradle to do the actual build. So, there is no different than invoking the Gradle manually in command line. If it works then it works everywhere (on *NIX).

-------------------------

Azaratur | 2019-04-10 14:08:14 UTC | #49

Yes i have problems on android studio.
I had to modify part of your modifications because it cannot be compiled in android studio at the current state.
It ask to upgrade android studio to 3.5.0 which does not exist.

-------------------------

weitjong | 2019-04-11 00:20:53 UTC | #50

Let me upgrade my Android Studio to 3.3.2 and test. The reason I want to bump the Gradle version from 4.9 to 5.x is because the `kotlin-dsl` release 1.0 is only made available on Gradle 5.x. The 4.9/4.10 only provides the RC version. One of the goal when I did the build system migration from Ant is to not just migrating to Gradle, but to also to use its latest DSL using Kotlin script rather than the legacy Groovy script. And I have been waiting for that 5.x release for quite some time now.

-------------------------

weitjong | 2019-04-10 14:26:09 UTC | #51

Bummer. I got the same message as yours. The 3.5.0 is required and the preview is available here https://developer.android.com/studio/preview. I think you can revert back the Gradle upgrade commit but keep the one which upgrade the embedded CMake version for now, if you cannot use the Preview version.

-------------------------

Azaratur | 2019-04-10 14:28:35 UTC | #52

I will try to download IntelliJ IDEA and try it on windows 10 to see if i can let it work.
Maybe this could be the way to avoid cmd.exe problems

-------------------------

Azaratur | 2019-04-10 15:36:44 UTC | #53

Ok i have successfully compile to android with a mac, so this mean that 95% of my problems are gone.

I did not had the time to build it on windows, i will try tomorrow.

-------------------------

Azaratur | 2019-04-11 10:58:50 UTC | #54

@weitjong Ok tested on windows 10 with android studio AND IntelliJ Idea but both failed for cmd.exe command too long.

Not sure why now is failing there again, since i was able to let the engine build in some of my tests, anyway i think i will not lose other time on it. 
We will work on mac.

-------------------------

Azaratur | 2019-04-11 11:11:57 UTC | #55

Reported the issue to google developer since most probably is their cmake that fails.

-------------------------

