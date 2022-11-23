KamiGrave | 2017-11-26 15:21:27 UTC | #1

I'm hoping I can get some help on how to build an android version of my app. I've maybe gone about this the wrong way but let me try and explain what I have so far:

* Downloaded Urho3D
* Exported Windows version and scaffolding project
* Moved things around a little bit into their own folders (including moving Urho3DPlayer scaffolding files into another folder)
* Built part of my game

Now the game was always intended for android, but I was using windows to develop it because it's easier. Now I've come to the point where I need to be able to run it on android (which I should have done weeks ago).

I see Urho3D does not really support a scaffolding project for android very well. I can build Urho3D to android and run the samples. What I can't figure out, is how to get it building for my scaffolding project with the code I already have. I've been trying for days with various forum posts and battling the NDK and the SDK at the same time.

Is there any good android support coming in soon? Does anyone have android working with an existing scaffolding project? Should I give up and just make windows games?

I understand the scaffolding project needs some setup. Mainly build.xml and android.manifest, but I know there's some other steps that I still don't know about.

Any help is appreciated.

-------------------------

rasteron | 2017-10-21 04:51:30 UTC | #2

Hey there KamiGrave, Welcome to the forums. Have you tried building the sample player / demos on Android? That seems to be a good starting scaffolding project so you can get familiar with Urho3D Android build.

-------------------------

KamiGrave | 2017-10-21 11:02:16 UTC | #3

I've gotten that far. Can run and play the samples, and even my own scripts. I'm coding in C++, so I only have a few test scripts that don't run my main game.

But, while I can build my own project to a library, I haven't been able to play it through the samples. I've been trying to use Urho3D as an external library, rather than writing my game into the engine code. Works great for PC, but it seems android has some hidden steps that I can't find or figure out.

If I do figure it out, I might try and write a similar rake file for doing an android scaffold that will copy over res folders and whatever else it needs. First, I need to figure out how to get it running or give up on the game or switch engine again to one that's a little bit more mobile friendly.

-------------------------

Lumak | 2017-10-21 16:52:05 UTC | #4

Have you considered importing your project to Android Studio? All you'd have to do build your project with cmake_android, passing a few build options, and import what's build directly into Android Studio.

-------------------------

KamiGrave | 2017-10-22 09:58:27 UTC | #5

I attempted that but I can't even get the scripts to run now. I'm at the point now where I'm ready to give up. It've wasted several days trying to get this to work and it just doesn't, both on this existing project and a new one. Android studio doesn't seem to import anything, the scripts now fail to run and for some reason cmake_android.bat makes it want to build for visual studio 2015.

All I need is some definitive guide to build the scaffolding project for android, and get it running using my own Urho3DPlayer.cpp, just like the windows one.

The only thing I've found on it is:

WARNING: As of this writing, this rake scaffolding task does not yet create a complete new project suitable for Android platform. You need to supply the missing bits manually yourself for now.

But it doesn't tell me what bits are missing and what to do to get it running so I've been trying to piece information from several forum and github posts with nothing but errors from the SDK, NDK or Urho3D the entire way. The only thing I've been able to successfully run on android is the Urho3D samples.

-------------------------

weitjong | 2017-10-22 10:37:50 UTC | #6

Have you tried to setup an Android project before using Android Studio or what have you? If not then I suggest you learn to do that first. Although the rake task does not cover Android platform right now, you can always see how Urho3D sample app is being structured for Android platform and use that as the prototype.

-------------------------

KamiGrave | 2017-10-22 14:35:28 UTC | #7

I don't even really want to use android studio at all. I'm fine building using ant and make, as it seems a lot simpler than importing the existing urho3D project as android-studio does not to a good job of it and then fails to recognise it as something it can build or run. It seems no matter what I do there's hoops I need to jump through to get anything working.

I've seen how the sample app works too and had a go at modifying it so I could build a different application. But now my entire project is messed up because of some conflict between the version of Urho3D I've built for android and the original windows version (URHO3D_HOME is now pointing at the wrong version and my existing windows application now fails to build). Now nothing builds so I'm actually further away from a working solution than what I was when I started.
I'm giving up on it now because clearly no one has an answer how to actually solve this. There's plenty of suggestions of things to try, or things to look at, but nothing on how to actually get it running.

-------------------------

Lumak | 2017-10-22 19:23:54 UTC | #8

Importing your build into Android Studio is really simple, takes less than 5 mins.  Here's the steps:
1) make your build to a [b]clean folder[/b], I'm specifying my tool chain from android-ndk-r15c
[code]
cmake_android PathToCleanBuildFolder -DANDROID_TOOLCHAIN_NAME=x86-4.9 -DURHO3D_LUA=0 -DURHO3D_PACKAGING=0 -DURHO3D_TOOLS=0
[/code]

2) go into your build folder and build
[code]
make
[/code]
3) open your Android Studio and import your build
* File -> New -> Import Project -- and select your build folder

That simple. In Android Studio create an emulation device compatible with what's defined in Urho3D/AndroidManifest.xml, and this example is a build for x86 device -> choose x86 emulation device.

-------------------------

KamiGrave | 2017-10-22 18:55:14 UTC | #9

OK. Fair enough, I didn't know about specifying the toolchain, so that's new to me.
But even after doing that, I end up with the android project I can already get working but now it's in android-studio. I don't see what advantage that gives me with trying to set up the scaffolding project for android. I just want a single codebase for windows and android with a bit of extra java to start the activity and call the C++ code.

Or even, what does the calling cmake_android on the scaffolding project actually do? Can I even support multiple platforms such as windows and android? Or do I need separate Urho3D builds and app folders?
It seems the only way I will be able to get it to work is to get the Urho3D samples calling my library (like it can do with the Urho3DPlayer) and copy and paste my code from windows into another project that'll build it into a library that can be called from the Urho3D Activity.

-------------------------

Lumak | 2017-10-22 19:32:02 UTC | #10

[quote="KamiGrave, post:9, topic:3676"]
I end up with the android project I can already get working but now it’s in android-studio. I don’t see what advantage that gives me with trying to set up the scaffolding project for android. I just want a single codebase for windows and android with a bit of extra java to start the activity and call the C++ code.

Or even, what does the calling cmake_android on the scaffolding project actually do?
[/quote]

I don't mention scaffolding in my steps because it's not used.
edit: to be honest, I never considered using scaffolding method nor did I even try because I wanted to focus on running my builds on Android Studio from the onset of discovering this engine.

[quote="KamiGrave, post:9, topic:3676"]
Can I even support multiple platforms such as windows and android? Or do I need separate Urho3D builds and app folders?
[/quote]

Obviously, you'll need a separate build folder for each platform.
edit2: [b]and different build folder for each build options[/b], e.g. build folder for winOpenGL, winDX9, androidArm, androidX86, etc.

-------------------------

Culzean | 2017-11-23 09:46:35 UTC | #11

@Lumak your instructions are very clear,however I have run into a problem while building against android-ndk-r16
Cmake seems to build fine and creates the new android build. However when I go to folder and make I run into this issue where it seems to run into trouble with the header files.
> 
> CreateProcess(C:\Users\Daniel\AppData\Local\Temp\make2440-1.bat,C:\Users\Daniel\AppData\Local\Temp\make2440-1.bat,...)
> Live child 00000000026467E0 (Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/autofit/autofit.c.o) PID 40093120
> In file included from C:/local/android-ndk-r16/sources/cxx-stl/llvm-libc++/include/limits.h:58:0,
>                  from C:/local/Urho3D/Source/ThirdParty/FreeType/include/freetype/config/ftstdlib.h:59,
>                  from C:/local/Urho3D/Source/ThirdParty/FreeType/include/freetype/config/ftconfig.h:43,
>                  from C:/local/Urho3D/Source/ThirdParty/FreeType/include/freetype/freetype.h:33,
>                  from C:/local/Urho3D/Source/ThirdParty/FreeType/src/autofit/aftypes.h:37,
>                  from C:/local/Urho3D/Source/ThirdParty/FreeType/src/autofit/afangles.c:20,
>                  from C:/local/Urho3D/Source/ThirdParty/FreeType/src/autofit/autofit.c:22:
> c:\local\android-ndk-r16\toolchains\x86-4.9\prebuilt\windows-x86_64\lib\gcc\i686-linux-android\4.9.x\include-fixed\limits.h:168:61: error: no include path in which to search for limits.h
>  #include_next <limits.h>  /* recurse down to the real one */
>                                                              ^
> In file included from C:/local/Urho3D/Source/ThirdParty/FreeType/include/freetype/config/ftstdlib.h:78:0,
>                  from C:/local/Urho3D/Source/ThirdParty/FreeType/include/freetype/config/ftconfig.h:43,
>                  from C:/local/Urho3D/Source/ThirdParty/FreeType/include/freetype/freetype.h:33,
>                  from C:/local/Urho3D/Source/ThirdParty/FreeType/src/autofit/aftypes.h:37,
>                  from C:/local/Urho3D/Source/ThirdParty/FreeType/src/autofit/afangles.c:20,
>                  from C:/local/Urho3D/Source/ThirdParty/FreeType/src/autofit/autofit.c:22:
> C:/local/android-ndk-r16/sources/cxx-stl/llvm-libc++/include/string.h:61:25: fatal error: string.h: No such file or directory
>  #include_next <string.h>
>                          ^
> compilation terminated. 

I am not experienced using make files and don't really know how to debug this. does anyone have any ideas?
I will try downloading ndk 15c and see if that is the problem.

-------------------------

Culzean | 2017-11-23 14:19:09 UTC | #12

[quote="Lumak, post:8, topic:3676"]
cmake_android PathToCleanBuildFolder -DANDROID_TOOLCHAIN_NAME=x86-4.9 -DURHO3D_LUA=0 -DURHO3D_PACKAGING=0 -DURHO3D_TOOLS=0
[/quote]

I have downgraded to the ndk 15c and things are working much better. Perhaps this is something to report as a bug to the ndk repo?

@Lumak is it possible to list multiple toolchains arguments in a single call? I need armeabi for my device, but mips and x86 would also be desirable.

-------------------------

Lumak | 2017-11-23 16:14:05 UTC | #13

Yes, if you could report the compile error due to <string.h> not being found would be beneficial for all of us.

This was my very first post on the forum over two years ago, https://discourse.urho3d.io/t/deploying-urho3d-to-android-studio-in-windows/1107
And at the time, you could specify multiple android targets, but that option got removed since then (don't know which ndk version).

Easiest way to support multiple targets is by copying the alternate **.so** file from your build folder into android's build jni folder. Search for *how to deploy to multiple targets* at the android studio website and you should get the answer, but the gist is: 
1) import your 1st build into android studio, let's say it's in urho3d/builds/androidx86
2) build your 2nd target device, e.g. urho3d/builds/androidArm -- don't import this.
3) In the urho3d/builds/androidArm/libs there is a folder specifying the target build, e.g ./armeabi-v7a. Copy the entire folder to the project that was imported in 1) under app\src\main\jniLibs. There should already be a target folder for x86.

That's it. Now you support multiple devices.

-------------------------

johnnycable | 2017-11-23 18:34:11 UTC | #14

Did you check how many users are out there using mips?

-------------------------

Culzean | 2017-11-24 16:34:02 UTC | #15

You know I didn't, looks to be on death's door. Which makes things simpler.

-------------------------

1vanK | 2017-12-02 14:02:30 UTC | #16

![1|690x401](upload://kS232WQlDKojdywqmund2ySkA3F.png)

I tried Android Studio 3.01 and 2.3.3 and recive this error  every time

-------------------------

weitjong | 2017-12-02 16:17:27 UTC | #17

Call the gradle task from CLI to get more information on the error.

-------------------------

1vanK | 2017-12-02 19:43:40 UTC | #18

Sorry, I'm noob. Explain in more detail what I should type (and where)

-------------------------

1vanK | 2017-12-02 21:37:22 UTC | #19

with -s option show more info, but that this will help

![1|690x402](upload://eLblSOuGhQdRsouRIE78YUfcLNp.png)

```
Executing tasks: [:app:assembleDebug]

Configuration on demand is an incubating feature.
Incremental java compilation is an incubating feature.
:app:preBuild UP-TO-DATE
:app:preDebugBuild UP-TO-DATE
:app:checkDebugManifest
:app:prepareDebugDependencies
:app:compileDebugAidl UP-TO-DATE
:app:compileDebugRenderscript UP-TO-DATE
:app:generateDebugBuildConfig UP-TO-DATE
:app:generateDebugResValues UP-TO-DATE
:app:generateDebugResources UP-TO-DATE
:app:mergeDebugResources UP-TO-DATE
:app:processDebugManifest UP-TO-DATE
:app:processDebugResources UP-TO-DATE
:app:generateDebugSources UP-TO-DATE
:app:incrementalDebugJavaCompilationSafeguard UP-TO-DATE
:app:compileDebugJavaWithJavac UP-TO-DATE
:app:compileDebugNdk UP-TO-DATE
:app:compileDebugSources UP-TO-DATE
:app:mergeDebugShaders UP-TO-DATE
:app:compileDebugShaders UP-TO-DATE
:app:generateDebugAssets UP-TO-DATE
:app:mergeDebugAssets UP-TO-DATE
:app:transformClassesWithDexForDebug UP-TO-DATE
:app:mergeDebugJniLibFolders UP-TO-DATE
:app:transformNative_libsWithMergeJniLibsForDebug UP-TO-DATE
:app:transformNative_libsWithStripDebugSymbolForDebug UP-TO-DATE
:app:processDebugJavaRes UP-TO-DATE
:app:transformResourcesWithMergeJavaResForDebug UP-TO-DATE
:app:validateSigningDebug
:app:packageDebug FAILED

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':app:packageDebug'.
> Self-suppression not permitted

* Try:
Run with --info or --debug option to get more log output.

* Exception is:
org.gradle.api.tasks.TaskExecutionException: Execution failed for task ':app:packageDebug'.
	at org.gradle.api.internal.tasks.execution.ExecuteActionsTaskExecuter.executeActions(ExecuteActionsTaskExecuter.java:69)
	at org.gradle.api.internal.tasks.execution.ExecuteActionsTaskExecuter.execute(ExecuteActionsTaskExecuter.java:46)
	at org.gradle.api.internal.tasks.execution.PostExecutionAnalysisTaskExecuter.execute(PostExecutionAnalysisTaskExecuter.java:35)
	at org.gradle.api.internal.tasks.execution.SkipUpToDateTaskExecuter.execute(SkipUpToDateTaskExecuter.java:66)
	at org.gradle.api.internal.tasks.execution.ValidatingTaskExecuter.execute(ValidatingTaskExecuter.java:58)
	at org.gradle.api.internal.tasks.execution.SkipEmptySourceFilesTaskExecuter.execute(SkipEmptySourceFilesTaskExecuter.java:52)
	at org.gradle.api.internal.tasks.execution.SkipTaskWithNoActionsExecuter.execute(SkipTaskWithNoActionsExecuter.java:52)
	at org.gradle.api.internal.tasks.execution.SkipOnlyIfTaskExecuter.execute(SkipOnlyIfTaskExecuter.java:53)
	at org.gradle.api.internal.tasks.execution.ExecuteAtMostOnceTaskExecuter.execute(ExecuteAtMostOnceTaskExecuter.java:43)
	at org.gradle.execution.taskgraph.DefaultTaskGraphExecuter$EventFiringTaskWorker.execute(DefaultTaskGraphExecuter.java:203)
	at org.gradle.execution.taskgraph.DefaultTaskGraphExecuter$EventFiringTaskWorker.execute(DefaultTaskGraphExecuter.java:185)
	at org.gradle.execution.taskgraph.AbstractTaskPlanExecutor$TaskExecutorWorker.processTask(AbstractTaskPlanExecutor.java:66)
	at org.gradle.execution.taskgraph.AbstractTaskPlanExecutor$TaskExecutorWorker.run(AbstractTaskPlanExecutor.java:50)
	at org.gradle.execution.taskgraph.DefaultTaskPlanExecutor.process(DefaultTaskPlanExecutor.java:25)
	at org.gradle.execution.taskgraph.DefaultTaskGraphExecuter.execute(DefaultTaskGraphExecuter.java:110)
	at org.gradle.execution.SelectedTaskExecutionAction.execute(SelectedTaskExecutionAction.java:37)
	at org.gradle.execution.DefaultBuildExecuter.execute(DefaultBuildExecuter.java:37)
	at org.gradle.execution.DefaultBuildExecuter.access$000(DefaultBuildExecuter.java:23)
	at org.gradle.execution.DefaultBuildExecuter$1.proceed(DefaultBuildExecuter.java:43)
	at org.gradle.execution.DryRunBuildExecutionAction.execute(DryRunBuildExecutionAction.java:32)
	at org.gradle.execution.DefaultBuildExecuter.execute(DefaultBuildExecuter.java:37)
	at org.gradle.execution.DefaultBuildExecuter.execute(DefaultBuildExecuter.java:30)
	at org.gradle.initialization.DefaultGradleLauncher$4.run(DefaultGradleLauncher.java:153)
	at org.gradle.internal.Factories$1.create(Factories.java:22)
	at org.gradle.internal.progress.DefaultBuildOperationExecutor.run(DefaultBuildOperationExecutor.java:91)
	at org.gradle.internal.progress.DefaultBuildOperationExecutor.run(DefaultBuildOperationExecutor.java:53)
	at org.gradle.initialization.DefaultGradleLauncher.doBuildStages(DefaultGradleLauncher.java:150)
	at org.gradle.initialization.DefaultGradleLauncher.access$200(DefaultGradleLauncher.java:32)
	at org.gradle.initialization.DefaultGradleLauncher$1.create(DefaultGradleLauncher.java:98)
	at org.gradle.initialization.DefaultGradleLauncher$1.create(DefaultGradleLauncher.java:92)
	at org.gradle.internal.progress.DefaultBuildOperationExecutor.run(DefaultBuildOperationExecutor.java:91)
	at org.gradle.internal.progress.DefaultBuildOperationExecutor.run(DefaultBuildOperationExecutor.java:63)
	at org.gradle.initialization.DefaultGradleLauncher.doBuild(DefaultGradleLauncher.java:92)
	at org.gradle.initialization.DefaultGradleLauncher.run(DefaultGradleLauncher.java:83)
	at org.gradle.launcher.exec.InProcessBuildActionExecuter$DefaultBuildController.run(InProcessBuildActionExecuter.java:99)
	at org.gradle.tooling.internal.provider.runner.BuildModelActionRunner.run(BuildModelActionRunner.java:46)
	at org.gradle.launcher.exec.ChainingBuildActionRunner.run(ChainingBuildActionRunner.java:35)
	at org.gradle.tooling.internal.provider.runner.SubscribableBuildActionRunner.run(SubscribableBuildActionRunner.java:58)
	at org.gradle.launcher.exec.ChainingBuildActionRunner.run(ChainingBuildActionRunner.java:35)
	at org.gradle.launcher.exec.InProcessBuildActionExecuter.execute(InProcessBuildActionExecuter.java:48)
	at org.gradle.launcher.exec.InProcessBuildActionExecuter.execute(InProcessBuildActionExecuter.java:30)
	at org.gradle.launcher.exec.ContinuousBuildActionExecuter.execute(ContinuousBuildActionExecuter.java:81)
	at org.gradle.launcher.exec.ContinuousBuildActionExecuter.execute(ContinuousBuildActionExecuter.java:46)
	at org.gradle.launcher.daemon.server.exec.ExecuteBuild.doBuild(ExecuteBuild.java:52)
	at org.gradle.launcher.daemon.server.exec.BuildCommandOnly.execute(BuildCommandOnly.java:36)
	at org.gradle.launcher.daemon.server.api.DaemonCommandExecution.proceed(DaemonCommandExecution.java:120)
	at org.gradle.launcher.daemon.server.exec.WatchForDisconnection.execute(WatchForDisconnection.java:37)
	at org.gradle.launcher.daemon.server.api.DaemonCommandExecution.proceed(DaemonCommandExecution.java:120)
	at org.gradle.launcher.daemon.server.exec.ResetDeprecationLogger.execute(ResetDeprecationLogger.java:26)
	at org.gradle.launcher.daemon.server.api.DaemonCommandExecution.proceed(DaemonCommandExecution.java:120)
	at org.gradle.launcher.daemon.server.exec.RequestStopIfSingleUsedDaemon.execute(RequestStopIfSingleUsedDaemon.java:34)
	at org.gradle.launcher.daemon.server.api.DaemonCommandExecution.proceed(DaemonCommandExecution.java:120)
	at org.gradle.launcher.daemon.server.exec.ForwardClientInput$2.call(ForwardClientInput.java:74)
	at org.gradle.launcher.daemon.server.exec.ForwardClientInput$2.call(ForwardClientInput.java:72)
	at org.gradle.util.Swapper.swap(Swapper.java:38)
	at org.gradle.launcher.daemon.server.exec.ForwardClientInput.execute(ForwardClientInput.java:72)
	at org.gradle.launcher.daemon.server.api.DaemonCommandExecution.proceed(DaemonCommandExecution.java:120)
	at org.gradle.launcher.daemon.server.health.DaemonHealthTracker.execute(DaemonHealthTracker.java:47)
	at org.gradle.launcher.daemon.server.api.DaemonCommandExecution.proceed(DaemonCommandExecution.java:120)
	at org.gradle.launcher.daemon.server.exec.LogToClient.doBuild(LogToClient.java:60)
	at org.gradle.launcher.daemon.server.exec.BuildCommandOnly.execute(BuildCommandOnly.java:36)
	at org.gradle.launcher.daemon.server.api.DaemonCommandExecution.proceed(DaemonCommandExecution.java:120)
	at org.gradle.launcher.daemon.server.exec.EstablishBuildEnvironment.doBuild(EstablishBuildEnvironment.java:72)
	at org.gradle.launcher.daemon.server.exec.BuildCommandOnly.execute(BuildCommandOnly.java:36)
	at org.gradle.launcher.daemon.server.api.DaemonCommandExecution.proceed(DaemonCommandExecution.java:120)
	at org.gradle.launcher.daemon.server.health.HintGCAfterBuild.execute(HintGCAfterBuild.java:41)
	at org.gradle.launcher.daemon.server.api.DaemonCommandExecution.proceed(DaemonCommandExecution.java:120)
	at org.gradle.launcher.daemon.server.exec.StartBuildOrRespondWithBusy$1.run(StartBuildOrRespondWithBusy.java:50)
	at org.gradle.launcher.daemon.server.DaemonStateCoordinator$1.run(DaemonStateCoordinator.java:237)
	at org.gradle.internal.concurrent.ExecutorPolicy$CatchAndRecordFailures.onExecute(ExecutorPolicy.java:54)
	at org.gradle.internal.concurrent.StoppableExecutorImpl$1.run(StoppableExecutorImpl.java:40)
Caused by: java.lang.IllegalArgumentException: Self-suppression not permitted
	at com.android.build.gradle.tasks.PackageAndroidArtifact.doTask(PackageAndroidArtifact.java:467)
	at com.android.build.gradle.tasks.PackageAndroidArtifact.doFullTaskAction(PackageAndroidArtifact.java:321)
	at com.android.build.gradle.tasks.PackageApplication.doFullTaskAction(PackageApplication.java:75)
	at com.android.build.gradle.internal.tasks.IncrementalTask.taskAction(IncrementalTask.java:88)
	at org.gradle.internal.reflect.JavaMethod.invoke(JavaMethod.java:75)
	at org.gradle.api.internal.project.taskfactory.AnnotationProcessingTaskFactory$IncrementalTaskAction.doExecute(AnnotationProcessingTaskFactory.java:245)
	at org.gradle.api.internal.project.taskfactory.AnnotationProcessingTaskFactory$StandardTaskAction.execute(AnnotationProcessingTaskFactory.java:221)
	at org.gradle.api.internal.project.taskfactory.AnnotationProcessingTaskFactory$IncrementalTaskAction.execute(AnnotationProcessingTaskFactory.java:232)
	at org.gradle.api.internal.project.taskfactory.AnnotationProcessingTaskFactory$StandardTaskAction.execute(AnnotationProcessingTaskFactory.java:210)
	at org.gradle.api.internal.tasks.execution.ExecuteActionsTaskExecuter.executeAction(ExecuteActionsTaskExecuter.java:80)
	at org.gradle.api.internal.tasks.execution.ExecuteActionsTaskExecuter.executeActions(ExecuteActionsTaskExecuter.java:61)
	... 70 more
Caused by: java.lang.OutOfMemoryError: Java heap space


BUILD FAILED

Total time: 9.323 secs
```

EDIT:

with -s --debug option
 https://pastebin.com/g1wLFgR2

-------------------------

johnnycable | 2017-12-02 21:44:26 UTC | #20

If you are building on windows, check [this](https://stackoverflow.com/questions/41645747/android-studio-gradle-build-failing-java-heap-space)

-------------------------

1vanK | 2017-12-02 21:53:39 UTC | #21

I've already tried it :(

-------------------------

johnnycable | 2017-12-03 11:32:45 UTC | #22

Does your gradle.properties file has the line:

> org.gradle.jvmargs=-Xmx1536m

this sets the java heap size for gradle, that's what your error is about. If you fix that, and your are getting it the same, it means the same property is internally set somewhere by Android Studio, possibly...

-------------------------

1vanK | 2017-12-03 11:56:44 UTC | #23

Thanks, it helped me compile apk. But now I have problem when try to launch apk

![1|690x388](upload://8SBCaeIXAB55urJaHBptOfrkF9N.png)

-------------------------

johnnycable | 2017-12-03 12:23:52 UTC | #24

Use the monitor, restrict log using your project name string; uninstall then reinstall. When you install again, you will get the error stack

-------------------------

1vanK | 2017-12-03 12:59:19 UTC | #25

![1|690x388](upload://xz7KEoFBNToaWJTHdLIhADGYPZB.png)
![2|690x388](upload://lzssDjoe7ZpfpqekayouCUGO4kA.png)

-------------------------

johnnycable | 2017-12-03 13:51:51 UTC | #26

![31|519x500](upload://7fNuA13tIbiOYc6QihAtebq5LmB.png)
![54|690x499](upload://k7wGVvdA3K4SoIfokWFAsKmHnN7.png)

Just created.
Looks unable to enlarge the emulator size. Check your disk space.

-------------------------

1vanK | 2017-12-03 13:54:44 UTC | #27

> Looks unable to enlarge the emulator size. Check your disk space.

120 gb free space on C:

-------------------------

johnnycable | 2017-12-03 13:56:15 UTC | #28

Try creating the same emulator as my setting. Does it start? Do not install the app, just create it.

-------------------------

1vanK | 2017-12-03 14:25:34 UTC | #29

Any emulator works without problems. Just error when I install APK with *.so . When I just cmake (but do not call make, so libs do not compiled) I can install APK and start urho3D on emulator, but it show message 

![Безымянный|690x388](upload://rPeE8LmrBskBgIYVshVrz1CqMQA.png)

-------------------------

johnnycable | 2017-12-03 14:52:50 UTC | #30

Ah, ok. So you just cmake without make. That means you don't have the libraries bundled with apk and the app crashes on loadlibrary call. You need to make and bundle them in the apk.

-------------------------

1vanK | 2017-12-03 14:56:52 UTC | #31

I mean I can install APK without libs, but I can not install APK with libs

-------------------------

1vanK | 2017-12-03 15:06:32 UTC | #32

Also is strange. When I install APK without libs, Urho search libs in x86_64. But when I install APK with libs, its try to copy to x86

-------------------------

johnnycable | 2017-12-03 16:28:59 UTC | #34

Check apk contents with build/analyze apk.

-------------------------

1vanK | 2017-12-03 16:40:36 UTC | #35

Hm, when I rebuild Urho3D as Shared instead static
```
Urho3D\cmake_android.bat Build -DANDROID_TOOLCHAIN_NAME=x86-4.9 -DURHO3D_LUA=0 -DURHO3D_PACKAGING=0 -DURHO3D_TOOLS=0 -DURHO3D_LIB_TYPE=SHARED
```
everything worked

-------------------------

johnnycable | 2017-12-03 17:21:50 UTC | #36

Don't know, I never changed the option. So I always built it static...
Given the sandboxes in mobile architectures, probably shared doesn't work anyway...

-------------------------

weitjong | 2017-12-04 02:34:08 UTC | #37

Both static and shared lib type should work equally in android platform. When space is an issue then using shared has an advantage because all the samples *.so are smaller in size as the Urho shared lib is added separately to the APK. What weird to me is why you could not emulate bigger SDRAM in your test AVD.

-------------------------

1vanK | 2017-12-04 17:22:00 UTC | #38

is way to convert project to gradle using command line?

-------------------------

johnnycable | 2017-12-04 17:41:27 UTC | #39

Only up to build tools 25.0.2 and Android Studio 2.3 you can

>   android create project \
>   --name $URHO_APP \ _your app name_
>   --activity $URHO_GRADLE_ACTIVITY \ _possibly Urho3D_
>   --package $URHO_GRADLE_PACKAGENAME \ _com.github.urho3d_
>   --gradle-version $URHO_GRADLE_PLUGIN_VERSION \ _2.3.0+_
>   --target $URHO_ANDROID_TARGET \ _android target (number)_
>   --gradle \
>   --path $URHO_GRADLE_DIR _your app dir_

then you 

> cd $URHO_GRADLE_DIR
> gradlew assembleDebug

Later build tools / Android Studio versions don't allow command line afaik. If someone knows a workaround...
Possibly the gradle plugin number can be different, check android docs for 2.3. That is the last I used.

-------------------------

1vanK | 2017-12-04 18:05:27 UTC | #40

It seems grandle can import ant project with small one-line file https://docs.gradle.org/current/userguide/ant.html

build.gradle
```
ant.importBuild 'build.xml'
```

but I received error

-------------------------

weitjong | 2017-12-06 10:48:24 UTC | #41

IMHO there is no need to call Ant’s build.xml unless you really have custom tasks defined there. Although Urho’s build.xml has one such task, it is optional and can be safely ignored. The rest of the inherited tasks should be already taken care of by Gradle’s android plugin.

-------------------------

johnnycable | 2017-12-05 11:04:16 UTC | #42

Possibly you should prefer later gradle + cmake build path vs older ndk-build + ant, which is deprecated.

-------------------------

1vanK | 2017-12-05 23:01:54 UTC | #43

https://developer.android.com/studio/build/index.html

as far as I understand, we can just add a few simple files (build.gradle, settings.gradle) and this will allow compiling from command line with latest version Android Studio

https://docs.gradle.org/current/userguide/gradle_wrapper.html
https://www.mkyong.com/gradle/how-to-use-gradle-wrapper/

```
gradle wrapper         // generate gradlew.bat
gradlew
```

-------------------------

johnnycable | 2017-12-06 10:17:57 UTC | #44

Your android studio depends on android installation / build tools version to build android(java) and cmake version (Use the one in android installation, not the system one you have when building for android) for building ndk apps like urho (C++)

-------------------------

1vanK | 2017-12-06 10:22:27 UTC | #45

Android studio ask update 1000 time at any gesture. Installing old version it's a quest which even requires disconnecting the Internet

-------------------------

1vanK | 2017-12-06 10:35:02 UTC | #46

[quote="johnnycable, post:44, topic:3676"]
Use the one in android installation, not the system one you have when building for android) for building ndk apps like urho (C++)
[/quote]

I do so (except cmake)

```
set "ANDROID_NDK=c:\Programs\android-ndk-r15c"
set "ENGINE_OPTIONS=-DURHO3D_SAMPLES=1 -DURHO3D_LUA=0 -DURHO3D_ANGELSCRIPT=0 -DURHO3D_TOOLS=0 -DURHO3D_PACKAGING=0 -DURHO3D_LIB_TYPE=SHARED -DANDROID_TOOLCHAIN_NAME=x86-4.9"
set "PATH=c:\Programs\CMake\bin\;%ANDROID_NDK%\prebuilt\windows-x86_64\bin\"
Urho3D\cmake_android.bat Android_Build %ENGINE_OPTIONS%
cd Android_Build
make

-------------------------

1vanK | 2017-12-06 14:27:08 UTC | #47

I did not do anything, but the application just stopped running with SDL error. I even reinstalled the studio several times, but this does not help...

![1|690x388](upload://xVz0dZM02XdE8I55qzERXwSigxD.png)

-------------------------

johnnycable | 2017-12-06 15:19:06 UTC | #48

You may want to user cmake shipped with android sdk because of a long running cmake issue with android builds https://github.com/android-ndk/ndk/issues/254

-------------------------

johnnycable | 2017-12-06 15:23:08 UTC | #49

"Swap Behaviour" never heard of it.
Could be st. emulator related?
Have you tried on a real device?
Btw possibly most stable version is 2.3, if you can afford "building old way". But I guess it's forcing us using urho 1.6
Ads 3.0 is breaking gradle compatibiliy. Installed it and regret it.

-------------------------

1vanK | 2017-12-06 15:35:21 UTC | #50

> Have you tried on a real device?

I have no real android device

Is it possible to look Urho's log like desktop applications?

-------------------------

johnnycable | 2017-12-06 16:20:04 UTC | #51

adb shell
android file transfer
adb master or st like it
I never tried, but you'd be able to get urho.log in the app data dir...

-------------------------

1vanK | 2017-12-07 00:21:14 UTC | #52

Works:
```
call "Urho3D\cmake_android.bat" Andruid_Build -DURHO3D_LUA=0 -DURHO3D_PACKAGING=0 -DURHO3D_TOOLS=0 -DURHO3D_LIB_TYPE=SHARED -DANDROID_TOOLCHAIN_NAME=x86-clang
```

SDL error when launch (disabled angel script):
```
call "Urho3D\cmake_android.bat" Andruid_Build -DURHO3D_ANGELSCRIPT=0 -DURHO3D_LUA=0 -DURHO3D_PACKAGING=0 -DURHO3D_TOOLS=0 -DURHO3D_LIB_TYPE=SHARED -DANDROID_TOOLCHAIN_NAME=x86-clang
```

EDIT:
Maybe this is due to the fact that the UrhoPlayer is not compiled when AS and LUA disabled, but android try load UrhoPlayer?

-------------------------

weitjong | 2017-12-07 01:38:59 UTC | #53

The provided android manifest file is only a sample and it assumes Urho3DPlayer is always available to play the script samples. If that is not the case anymore then you have to adjust the manifest file accordingly, just like you would if you are working on a new Android project. Possibly require you to create or modify Java class too.

-------------------------

1vanK | 2017-12-07 10:43:07 UTC | #54

Ok, I have builded libUrho3D.so by clang. How to build my app linked with this lib?

```
d:\Android\Game\2_GameSrc\Android_Build>cmake.exe "../Src" -DURHO3D_ANGELSCRIPT=1 -DURHO3D_LUA=0 -DURHO3D_PACKAGING=0 -DURHO3D_TOOLS=0 -DURHO3D_LIB_TYPE=SHARED -DANDROID_TOOLCHAIN_NAME=x86-clang -DANDROID=1 -DCMAKE_TOOLCHAIN_FILE="D:\Android\Game\2_GameSrc\../1_Engine/Urho3D/CMake/Toolchains/Android.cmake"
-- Building for: Visual Studio 15 2017
CMake Error at CMakeLists.txt:2 (project):
  CMAKE_SYSTEM_NAME is 'Android' but 'NVIDIA Nsight Tegra Visual Studio
  Edition' is not installed.
```

I use same CMakeLists.txt https://urho3d.github.io/documentation/HEAD/_using_library.html

Why it starts generate for VS instead clang?

-------------------------

weitjong | 2017-12-07 12:03:34 UTC | #55

If you don’t use our provided script or batch file and invoke CMake directly AND if you don’t specify a generator to use then by default CMake would choose one for you (based on the things it can find in the PATH I think). So, on my Linux box it will be “Makefile” and on your case it will be “VisualStudio” as that what you have.

-------------------------

extobias | 2018-02-10 15:37:01 UTC | #56

Hi, I think that the option -Wl,--gc-sections used while linked samples is removing SDL_main entry.
That is why ain't working with static link.

-------------------------

weitjong | 2018-02-10 16:09:21 UTC | #57

Is it really so? Anybody else observing this? It has been awhile I tried building using Static build configuration for Android build. We used to generate and test run the APK using emulator in our CI build and if I recall correctly it was also only using Urho3D as Shared lib, so the Static build configuration is less tested in that sense. Will take a closer look later.

-------------------------

Dimous | 2018-02-11 11:12:47 UTC | #58

I'm observing this when compiling with mingw-w64. Demo launcher is starting, but when I choose demo from the list, it crashes with "SDL_main not found" error.

-------------------------

johnnycable | 2018-02-11 11:47:55 UTC | #59

I've been building with static since 1.6, and I always had to build the sdl main apart with an ad-hoc cmake file. A post [here](https://github.com/android-ndk/ndk/issues/436) is pointing to some sort of default ndk feature that's stripping it. I have to check it  on compile log.

-------------------------

weitjong | 2018-02-11 14:16:26 UTC | #60

Last year when I did the SDL version upgrade, I remember I need to fix a line in the `Main.h`.

https://github.com/urho3d/Urho3D/blob/b4732cf5551c58fe57800191c4adce588e74c8bd/Source/Urho3D/Core/Main.h#L74

It basically ensures the `SDL_main` symbol to be kept around. Although the circumstances why I need to do that may be different than what's in 1.6/1.7 releases but I think this might be the answer.

-------------------------

Dimous | 2018-02-12 14:20:03 UTC | #61

Built Urho from git and tried to run demos again. This is what I got in Logcat:

02-13 00:05:59.136 3561-3561/com.github.urho3d V/SDL: Device: t03g
02-13 00:05:59.136 3561-3561/com.github.urho3d V/SDL: Model: GT-N7100
02-13 00:05:59.136 3561-3561/com.github.urho3d V/SDL: onCreate()
02-13 00:05:59.136 3561-3561/com.github.urho3d V/SDL: nativeSetupJNI()
02-13 00:05:59.136 3561-3561/com.github.urho3d V/SDL: AUDIO nativeSetupJNI()
02-13 00:05:59.136 3561-3561/com.github.urho3d V/SDL: CONTROLLER nativeSetupJNI()
02-13 00:05:59.151 3561-3561/com.github.urho3d V/SDL: onResume()
02-13 00:05:59.261 3561-3561/com.github.urho3d V/SDL: surfaceCreated()
02-13 00:05:59.261 3561-3561/com.github.urho3d V/SDL: surfaceChanged()
02-13 00:05:59.261 3561-3561/com.github.urho3d V/SDL: pixel format RGB_565
02-13 00:05:59.261 3561-3561/com.github.urho3d V/SDL: Window size: 720x1280
02-13 00:05:59.261 3561-3561/com.github.urho3d I/SensorManagerA: getReportingMode :: sensor.mType = 1
02-13 00:05:59.261 3561-3561/com.github.urho3d D/SensorManager: registerListener :: 0, LSM330DLC Acceleration Sensor, 20000, 0,  
02-13 00:05:59.266 3561-3700/com.github.urho3d V/SDL: Running main function SDL_main from library lib03_Sprites.so
02-13 00:05:59.266 3561-3700/com.github.urho3d V/SDL: nativeRunMain()
02-13 00:05:59.266 3561-3561/com.github.urho3d V/SDL: nativeResume()
02-13 00:05:59.266 3561-3561/com.github.urho3d I/SensorManagerA: getReportingMode :: sensor.mType = 1
02-13 00:05:59.266 3561-3700/com.github.urho3d E/SDL: nativeRunMain(): Couldn't find function SDL_main in library lib03_Sprites.so
02-13 00:05:59.266 3561-3700/com.github.urho3d V/SDL: Finished main function
02-13 00:05:59.291 3561-3561/com.github.urho3d V/SDL: onWindowFocusChanged(): true
02-13 00:05:59.306 3561-3561/com.github.urho3d V/SDL: onPause()
02-13 00:05:59.306 3561-3561/com.github.urho3d V/SDL: nativePause()
02-13 00:05:59.306 3561-3561/com.github.urho3d I/SensorManagerA: getReportingMode :: sensor.mType = 1
02-13 00:05:59.311 3561-3561/com.github.urho3d D/SensorManager: unregisterListener ::   
02-13 00:05:59.326 3561-3561/com.github.urho3d V/SDL: onWindowFocusChanged(): false
02-13 00:05:59.341 3561-3561/com.github.urho3d V/SDL: surfaceDestroyed()
02-13 00:05:59.441 3561-3561/com.github.urho3d V/SDL: onDestroy()
02-13 00:05:59.441 3561-3561/com.github.urho3d V/SDL: nativeQuit()

-------------------------

weitjong | 2018-02-12 15:00:09 UTC | #62

Hmm. OK, you got me. Will double check that when I have time, if the issue remains outstanding by then. Just for my information, please let me know what is your host system.

-------------------------

Dimous | 2018-02-13 12:56:05 UTC | #63

Windows 10 x64

> ANDROID_HOME=C:\Users\kasimowsky\AppData\Local\Android\sdk
> ANDROID_NATIVE_API_LEVEL=19
> ANDROID_NDK=C:\Users\kasimowsky\AppData\Local\Android\ndk\r15c
> ANDROID_NDK_ROOT=C:\Users\kasimowsky\AppData\Local\Android\ndk\r15c
> ANDROID_SDK=C:\Users\kasimowsky\AppData\Local\Android\sdk
> CLPATH=C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin
> CMAKE=C:\Program Files\CMake\bin
> INCLUDE=;C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\include;C:\Program Files (x86)\Microsoft SDKs\Windows\v7.1A\Include
> INCLUDESDK=C:\Program Files (x86)\Microsoft SDKs\Windows\v7.1A\Include
> INCLUDEVC=C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\include
> JAVA_HOME=C:\Program Files\Java\jdk1.8.0_162
> LIB=;C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib;C:\Program Files (x86)\Microsoft SDKs\Windows\v7.1A\Lib
> LIBSDK=C:\Program Files (x86)\Microsoft SDKs\Windows\v7.1A\Lib
> LIBVC=C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib
> OS=Windows_NT
> Path=C:\ProgramData\Oracle\Java\javapath;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0;C:\Program Files (x86)\GtkSharp\2.12\bin;C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin;android-19;C:\Users\kasimowsky\Documents\Git\Urho3D;C:\Users\kasimowsky\AppData\Local\Android\sdk;C:\Users\kasimowsky\AppData\Local\Android\ndk;C:\Program Files\Git\cmd;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\Program Files\TortoiseGit\bin;C:\Users\kasimowsky\Documents\HaxeToolkit\haxe;C:\Users\kasimowsky\Documents\HaxeToolkit\neko;C:\Program Files (x86)\NVIDIA Corporation\PhysX\Common;C:\Users\kasimowsky\Documents\HaxeToolkit\haxe\;C:\Users\kasimowsky\Documents\HaxeToolkit\neko;C:\Program Files\dotnet\;C:\Program Files\Microsoft SQL Server\130\Tools\Binn\;C:\Program Files\nodejs\;C:\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit\;C:\Users\kasimowsky\AppData\Local\Microsoft\WindowsApps;C:\Program Files (x86)\Apache\maven\bin;C:\Program Files (x86)\Apache\ant\bin;C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin;;C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\include;C:\Program Files (x86)\Microsoft SDKs\Windows\v7.1A\Include;;C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib;C:\Program Files (x86)\Microsoft SDKs\Windows\v7.1A\Lib;C:\Users\kasimowsky\AppData\Local\Android\sdk\tools;C:\Users\kasimowsky\AppData\Local\Android\sdk\build-tools;C:\Users\kasimowsky\AppData\Local\Android\sdk\platform-tools;C:\Users\kasimowsky\AppData\Local\Android\ndk\r15c\build;C:\Users\kasimowsky\AppData\Local\Android\ndk\r15c\prebuilt\windows-x86_64\bin;C:\Program Files\MongoDB\Server\3.6\bin;C:\Program Files\Microsoft VS Code\bin;C:\Program Files\Java\jdk1.8.0_162\bin;C:\Users\kasimowsky\AppData\Roaming\npm;C:\Program Files\CMake\bin;
> PLATFORM=android-19
> PROCESSOR_ARCHITECTURE=AMD64
> PROCESSOR_IDENTIFIER=Intel64 Family 6 Model 58 Stepping 9, GenuineIntel
> PROCESSOR_LEVEL=6
> PROCESSOR_REVISION=3a09
> PSModulePath=C:\Program Files\WindowsPowerShell\Modules;C:\WINDOWS\system32\WindowsPowerShell\v1.0\Modules
> PUBLIC=C:\Users\Public
> URHO3D_HOME=C:\Users\kasimowsky\Documents\Git\Urho3D
> VS140COMNTOOLS=C:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7\Tools\

Urho revision 9ae2e2b5fce77f0555311e124d7156eb47d67a96

I can't properly setup ndk+clang build toolchain, so I use mingw. _I even tried generating "standalone build toolchain", but still no luck._

Thanks in advance!

-------------------------

weitjong | 2018-03-17 13:34:07 UTC | #64

This should be fixed now in the latest master branch. 
https://github.com/urho3d/Urho3D/commit/9eed60fc73ba7cdda3974a78213e999d359fe91e

-------------------------

