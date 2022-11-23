Maco | 2021-08-25 17:16:59 UTC | #1

Hello i tried this but get error while building
rake new[UrhoApp,demo]
gradlew.bat build

```
        at java.lang.Thread.run(Thread.java:748)
    Caused by: java.lang.RuntimeException: java.nio.file.DirectoryNotEmptyException: C:\Urho3D\demo\UrhoApp\app\build\intermediates\merged_assets\debug\out\CoreData
        at com.android.ide.common.resources.MergedAssetWriter$AssetWorkAction.run(MergedAssetWriter.java:97)
        at com.android.build.gradle.internal.tasks.Workers$ActionFacade.run(Workers.kt:242)
        at org.gradle.workers.internal.AdapterWorkAction.execute(AdapterWorkAction.java:57)
        at org.gradle.workers.internal.DefaultWorkerServer.execute(DefaultWorkerServer.java:63)
        at org.gradle.workers.internal.NoIsolationWorkerFactory$1$1.create(NoIsolationWorkerFactory.java:67)
        at org.gradle.workers.internal.NoIsolationWorkerFactory$1$1.create(NoIsolationWorkerFactory.java:63)
        at org.gradle.internal.classloader.ClassLoaderUtils.executeInClassloader(ClassLoaderUtils.java:97)
        at org.gradle.workers.internal.NoIsolationWorkerFactory$1.lambda$execute$0(NoIsolationWorkerFactory.java:63)
        at org.gradle.workers.internal.AbstractWorker$1.call(AbstractWorker.java:44)
        at org.gradle.workers.internal.AbstractWorker$1.call(AbstractWorker.java:41)
        at org.gradle.internal.operations.DefaultBuildOperationRunner$CallableBuildOperationWorker.execute(DefaultBuildOperationRunner.java:200)
        at org.gradle.internal.operations.DefaultBuildOperationRunner$CallableBuildOperationWorker.execute(DefaultBuildOperationRunner.java:195)
        at org.gradle.internal.operations.DefaultBuildOperationRunner$3.execute(DefaultBuildOperationRunner.java:75)
        at org.gradle.internal.operations.DefaultBuildOperationRunner$3.execute(DefaultBuildOperationRunner.java:68)
        at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:153)
        at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:68)
        at org.gradle.internal.operations.DefaultBuildOperationRunner.call(DefaultBuildOperationRunner.java:62)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor.lambda$call$2(DefaultBuildOperationExecutor.java:76)
        at org.gradle.internal.operations.UnmanagedBuildOperationWrapper.callWithUnmanagedSupport(UnmanagedBuildOperationWrapper.java:54)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor.call(DefaultBuildOperationExecutor.java:76)
        at org.gradle.workers.internal.AbstractWorker.executeWrappedInBuildOperation(AbstractWorker.java:41)
        at org.gradle.workers.internal.NoIsolationWorkerFactory$1.execute(NoIsolationWorkerFactory.java:60)
        at org.gradle.workers.internal.DefaultWorkerExecutor.lambda$submitWork$2(DefaultWorkerExecutor.java:200)
        at java.util.concurrent.FutureTask.run(FutureTask.java:266)
        at org.gradle.internal.work.DefaultConditionalExecutionQueue$ExecutionRunner.runExecution(DefaultConditionalExecutionQueue.java:215)
        at org.gradle.internal.work.DefaultConditionalExecutionQueue$ExecutionRunner.runBatch(DefaultConditionalExecutionQueue.java:164)
        at org.gradle.internal.work.DefaultConditionalExecutionQueue$ExecutionRunner.run(DefaultConditionalExecutionQueue.java:131)
        at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:511)
        at java.util.concurrent.FutureTask.run(FutureTask.java:266)
        ... 6 more
    Caused by: java.nio.file.DirectoryNotEmptyException: C:\Urho3D\demo\UrhoApp\app\build\intermediates\merged_assets\debug\out\CoreData
        at sun.nio.fs.WindowsFileCopy.copy(WindowsFileCopy.java:162)
        at sun.nio.fs.WindowsFileSystemProvider.copy(WindowsFileSystemProvider.java:278)
        at java.nio.file.Files.copy(Files.java:1274)
        at com.android.ide.common.resources.MergedAssetWriter$AssetWorkAction.run(MergedAssetWriter.java:94)
        ... 34 more


FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':app:mergeDebugAssets'.
> A failure occurred while executing com.android.build.gradle.internal.tasks.Workers$ActionFacade
   > java.nio.file.DirectoryNotEmptyException: C:\Urho3D\demo\UrhoApp\app\build\intermediates\merged_assets\debug\out\CoreData

* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.
```

-------------------------

SirNate0 | 2021-08-25 18:13:07 UTC | #2

[quote="Maco, post:1, topic:6978"]
`java.nio.file.DirectoryNotEmptyException: C:\Urho3D\demo\UrhoApp\app\build\intermediates\merged_assets\debug\out\CoreData`
[/quote]

Never used rake for my projects, and it's been years since I built for Android on Windows, but did you maybe have a build that failed in the middle and left something in the directory that the build system seems to expect to be empty?

-------------------------

Maco | 2021-08-26 08:32:13 UTC | #3

before build there was no build folder while building it creating itself and gets error

-------------------------

weitjong | 2021-08-26 09:41:16 UTC | #4

I must admit the Android build on Windows host is not well tested, at least we don't have it on CI yet. And, also it requires a manual correction that is currently undocumented for Windows host. As I recall it, I could not get the Android Gradle plugin to setup the "assets" directory as I originally wanted that works for Linux/macOS/Windows. I have mentioned my ordeal in this forum somewhere, but you will have to go search for it yourself. Suffice to say, in the end I have to live it with a working out of the box solution for Linux and macOS only because it relies on the concept of "symbolic link", which Windows host does not support (no, I am not referring to mklink). Obviously I don't want to check in the same assets twice in different places in our GitHub project. But either I am stupid or the Android plugin is stupid that I cannot declaratively split the content of the "bin" directory so that the "CoreData" go to one place (`android/urho3d-lib/src/main/assets`) and the "Data" go to another (`android/launcher-app/src/main/assets`). Why I mentioned this will be apparent shortly. I gave up and took a shortcut by making them as symbolic links.

At the time I was developing the new Android build system based on Gradle so that it would work with Android Studio, I have decided not to change the existing Urho3D project by too much. However, I was ambitious enough to want to have a separation between building the Urho3D library as AAR and building the Urho3D demo as Android app that depends on this AAR. So, where is the problem, you may ask. Well, you see Urho3D project has always provided the assets in the "CoreData" and "Data" (we can ignore "Autoload" for this discussion) relative to the project root. I have chosen to "CoreData" to be packaged inside the AAR, while the "Data" to be in the downstream app. Note that downstream app can put anything inside this "Data" directory in theory, not just the one provided by the Urho3D project. When building the app with the Urho3D AAR, the Gradle build system will automatically try to merge the assets directory found in the AAR with the one found in the individual app. Thus, the error you got looks like you have "CoreData" to be made available in both AAR side and the app side. This could happen if you have replaced the "symlinks" that I mentioned above wrongly. Make sure you copy the "bin/CoreData" only to the "urho3d-lib", while "bin/Data" only to "launcher-app".

HTH

-------------------------

SirNate0 | 2021-08-26 10:34:25 UTC | #5

[quote="weitjong, post:4, topic:6978"]
it relies on the concept of “symbolic link”, which Windows host does not support (no, I am not referring to mklink).
[/quote]

I've been trying to figure out the answer on Google for half an hour, but what are the relevant differences that makes the Windows symbolic links/directory junctions not a suitable alternative for the build system?

-------------------------

weitjong | 2021-08-26 10:47:36 UTC | #6

Well, the symlinks are actually checked in into git repository. As git came from the Linux world, it works with symlinks. Checking out a symlink from repo also just works. Those symlinks are not created on the fly dynamically, if they do then yes, we could probably put an if somewhere to choose between mklink and genuine symlinks.

-------------------------

SirNate0 | 2021-08-26 10:56:22 UTC | #7

I think it may be possible now to get git to work with symlinks in Windows, though it looks like it takes some work to set up:

https://www.joshkel.com/2018/01/18/symlinks-in-windows/

-------------------------

weitjong | 2021-08-26 11:55:54 UTC | #8

It would be nice that Windows could support symlinks correctly like all the other systems and all the tools will enable the support by default.

-------------------------

elix22 | 2021-08-26 13:11:45 UTC | #9

I am not using rake ( I am not following the latest Urho3D master)
I am using Gradle tasks to do all the work , also to copy my assets .
Works great and fast on all platforms.

Some example below :

```
Make sure you delete these 2 folders entirely , (this is causing the error that you see on Windows)
Urho3D/android/launcher-app/src/main/assets
Urho3D/android/urho3d-lib/src/main/assets
```




```
Add  below task to
android/launcher-app/build.gradle.kts

tasks {
...
...
...
    register<Copy>("CopyAssets") {
        from ("../../bin")
        into ("src/main/assets")
    }  
}
```

Example of using it 
```
gradlew CopyAssets assembleDebug -P URHO3D_LUA=0  -P URHO3D_LIB_TYPE=SHARED
```

-------------------------

weitjong | 2021-08-26 14:20:31 UTC | #10

The Rake task is just another wrapper. Whether you use the cmake_android.bat or cmake_android.sh or call the gradle wrapper directly, it makes absolutely no difference. The key thing is to match the instructions with the commit/version of the source tree. The latest version in the master branch has moved away from the old way where people needs to hack into Urho3D build system in order to build their own Android project. With the new way, you just need to get the AAR ready and use the AAR library in your own project cleanly. So, the above instruction combining with AAR approach will actually produce the issue reported by the OP.

EDIT: I stand corrected. If you meant to delete "CoreData" from the AAR side and then add it back on the app side then of course it would work. However, the idea is to have the AAR build once and reuse multiple times and that it should be self-sufficient, so I still reject the above as correct workaround solution for Windows host.

-------------------------

elix22 | 2021-08-26 15:18:32 UTC | #11

[quote="weitjong, post:10, topic:6978"]
If you meant to delete “CoreData” from the AAR side and then add it back on the app side then of course it would work
[/quote]

Yes , that's exactly what I meant in my solution .
Moving "CoreData"  to the app side doesn't contradicts building  AAR once and reuse it .
By the end of the day you need both "CoreData" and "Data" to make a working APK .

-------------------------

weitjong | 2021-08-26 16:29:39 UTC | #12

Although the end of the merge result is the same, the user of the AAR will need to have multiple copies “CoreData” in each downstream app projects. Additionally, it will also make the AAR built from Windows host to be different than the one built from the rest of us on the other side of the digital divide.

-------------------------

Modanung | 2021-08-26 20:49:13 UTC | #13

Paths free of escape characters would also be an improvement. [spoiler]**#bat-country**[/spoiler]

-------------------------

elix22 | 2021-08-27 06:39:20 UTC | #14

[quote="weitjong, post:12, topic:6978"]
Although the end of the merge result is the same, the user of the AAR will need to have multiple copies “CoreData” in each downstream app projects
[/quote]

Right , it's additional ~ 450kB per app project on the desktop , will be the same size on the APK side .
It's noting in today standards and it will solve you some major headaches

In Urho.Net I am using it for all 3 Platforms (Linux,Mac,Windows) , I am not using symbolic links.
The first copy of all assets Data/CoreData takes ~3 seconds on my desktop , 
subsequent copy operations take milliseconds , it copies only updated files/resources.
The downside it doesn't delete files in the Android folder if the file was deleted in the bin source folder (I am too lazy to write an Task for that)
Just my 2 cents ...

Some reference 
https://github.com/Urho-Net/Urho.Net/blob/main/template/Android/app/build.gradle#L42

-------------------------

weitjong | 2021-08-27 07:09:57 UTC | #15

I have explained that I have failed to do it properly in the first place. Instead of "copying", I wanted to configure the build script so that I could declaratively point the assets dir to the right content. Similar to what symlink does. Only a "pointer to" and not an actual copying. If you or anyone could do that then I will accept that as the general solution.

It is not just wasting the space, you will also have to keep track of which "CoreData" goes to which version of AAR down the road. Granted that Lasse is not with us anymore and that for the past few years there were nothing major changed on the Graphics side that would invalidate the RenderPaths or Techniques or Shaders in the "CoreData". But we should not make the assumption that the same "CoreData" is perfect match of any Urho3D library. At the time I design the Urho3D AAR, I envision it to be published to MavenCentral. Android developer can just use the AAR in their own Android app project and regardless of which version they use, it will come with the documentation and core assets within itself in a nice package. The Urho3D AAR will be just another AAR used by the downstream project and there is nothing special to it.

-------------------------

