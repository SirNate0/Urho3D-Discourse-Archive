practicing01 | 2017-01-02 01:01:40 UTC | #1

Hello, I've successfully compiled/installed on linux/android but I'm new to c++ game development (I usually script and the last engine I used was in java).  When I didn't build with the samples flag, on android the default bevahiour was the ninja demo.  Where is this code located so I could remove it?  Upon removal, how would I proceed to add the template provided here: [urho3d.github.io/documentation/H ... _loop.html](http://urho3d.github.io/documentation/HEAD/_main_loop.html)  and what files would I have to modify so that cmake recognizes it?  Any links to information on these topics would be greatly appreciated.  Thanks for your time.

-------------------------

weitjong | 2017-01-02 01:01:40 UTC | #2

You may find one of the post made by zakk in this thread useful. [topic378.html#p2126](http://discourse.urho3d.io/t/solved-using-scripting-with-android/386/8)

-------------------------

practicing01 | 2017-01-02 01:01:59 UTC | #3

Arise ye rotting post!

I got the engine installed on my phone fine.  I used the "rake" method described here: [urho3d.github.io/documentation/H ... caffolding](http://urho3d.github.io/documentation/HEAD/_using_library.html#Scaffolding) to create a custom project.  I've made a game and am ready to test on my phone.  The android projects are not within android-Build though.  Am I supposed to copy/paste the engine's android-Build folder and modify that?  Any links to potential solutions would be greatly appreciated, thanks for your time.

Image incase that helps:
[img]http://img.ctrlv.in/img/14/12/14/548d1bad109c5.png[/img]

-------------------------

weitjong | 2017-01-02 01:02:00 UTC | #4

The rake scaffolding task is incomplete. It does not support scaffolding the Android project that well yet. If you read the steps by steps written by zakk in the post I linked earlier, you should see how he resolved this problem.

-------------------------

practicing01 | 2017-01-02 01:02:00 UTC | #5

Edit 5: Grepped for com.github.urho3d and changed those to my custom package name, also changed the directory structure of /src/com/github/urho3d to /src/my/custom/pkgName
Edit 4: App crash cus of portrait fixed, I forced landscape within the AndroidManifest.xml.  Now to figure out how to change the package name.
Edit 3:  The app crashes on startup if I hold my phone in portrait mode position but starts fine if in landscape.  I guess I should force landscape.  Any help on how to change the package name?
Edit 2: Alrighty got past the below problem by reverting the package name to com.github.urho3d.  BRB...
Edit 1:  Oops I missed a step (copying the contents of src).  After that, "ant debug" gives me this error:
[code]
-compile:
    [javac] Compiling 5 source files to /home/practicing01/Desktop/Programming/ClausOfFury/android-Build/bin/classes
    [javac] /home/practicing01/Desktop/Programming/ClausOfFury/android-Build/src/com/github/urho3d/SampleLauncher.java:51: error: package R does not exist
    [javac]         ArrayAdapter<String> adapter = new ArrayAdapter<String>(this, R.layout.samples_list_text_view);
    [javac]                                                                        ^
    [javac] /home/practicing01/Desktop/Programming/ClausOfFury/android-Build/src/com/github/urho3d/SampleLauncher.java:52: error: package R does not exist
    [javac]         setContentView(R.layout.samples_list);
    [javac]                         ^
    [javac] Note: /home/practicing01/Desktop/Programming/ClausOfFury/android-Build/src/org/libsdl/app/SDLActivity.java uses or overrides a deprecated API.
    [javac] Note: Recompile with -Xlint:deprecation for details.
    [javac] 2 errors

BUILD FAILED
/home/practicing01/Desktop/Programming/android-sdk-linux/tools/ant/build.xml:720: The following error occurred while executing this line:
/home/practicing01/Desktop/Programming/android-sdk-linux/tools/ant/build.xml:734: Compile failed; see the compiler error output for details.

[/code]

Thanks, I was able to install my project on the phone following the steps linked plus a few from the official docs.  However, I'm getting this error from logcat:
[code]
E/AndroidRuntime(18717): FATAL EXCEPTION: main
E/AndroidRuntime(18717): java.lang.RuntimeException: Unable to instantiate activity ComponentInfo{com.mds.cof/com.mds.cof.SampleLauncher}: java.lang.ClassNotFoundException: com.mds.cof.SampleLauncher
E/AndroidRuntime(18717): 	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2034)
E/AndroidRuntime(18717): 	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:2135)
E/AndroidRuntime(18717): 	at android.app.ActivityThread.access$700(ActivityThread.java:140)
E/AndroidRuntime(18717): 	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1237)
E/AndroidRuntime(18717): 	at android.os.Handler.dispatchMessage(Handler.java:99)
E/AndroidRuntime(18717): 	at android.os.Looper.loop(Looper.java:137)
E/AndroidRuntime(18717): 	at android.app.ActivityThread.main(ActivityThread.java:4921)
E/AndroidRuntime(18717): 	at java.lang.reflect.Method.invokeNative(Native Method)
E/AndroidRuntime(18717): 	at java.lang.reflect.Method.invoke(Method.java:511)
E/AndroidRuntime(18717): 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:1027)
E/AndroidRuntime(18717): 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:794)
E/AndroidRuntime(18717): 	at dalvik.system.NativeStart.main(Native Method)
E/AndroidRuntime(18717): Caused by: java.lang.ClassNotFoundException: com.mds.cof.SampleLauncher
E/AndroidRuntime(18717): 	at dalvik.system.BaseDexClassLoader.findClass(BaseDexClassLoader.java:61)
E/AndroidRuntime(18717): 	at java.lang.ClassLoader.loadClass(ClassLoader.java:501)
E/AndroidRuntime(18717): 	at java.lang.ClassLoader.loadClass(ClassLoader.java:461)
E/AndroidRuntime(18717): 	at android.app.Instrumentation.newActivity(Instrumentation.java:1068)
E/AndroidRuntime(18717): 	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2025)
E/AndroidRuntime(18717): 	... 11 more
[/code]

BTW the link you provided has the person compiling the engine on the phone.  I have successfully done that.  One thing to note though is that my project doesn't use scripts so I don't know if the SampleLauncher will work.  Any links that may lead to answers would be greatly appreciated.  Thanks for your time.

-------------------------

