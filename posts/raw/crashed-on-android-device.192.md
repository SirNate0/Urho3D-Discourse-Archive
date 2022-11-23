att | 2017-01-02 00:58:46 UTC | #1

hi,
I recently updated the urho3d engine code, and run my game demo on iOS and android device.
iOS is ok but on android device It just crash, I think something is wrong.
This is the crash log:

E/AndroidRuntime(23966): Process: com.github.urho3d, PID: 23966
E/AndroidRuntime(23966): java.lang.RuntimeException: Unable to start activity ComponentInfo{com.github.urho3d/com.github.urho3d.Urho3D}: java.lang.IndexOutOfBoundsException: Invalid index 0, size is 0
E/AndroidRuntime(23966): 	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2195)
E/AndroidRuntime(23966): 	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:2245)
E/AndroidRuntime(23966): 	at android.app.ActivityThread.access$800(ActivityThread.java:135)
E/AndroidRuntime(23966): 	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1196)
E/AndroidRuntime(23966): 	at android.os.Handler.dispatchMessage(Handler.java:102)
E/AndroidRuntime(23966): 	at android.os.Looper.loop(Looper.java:136)
E/AndroidRuntime(23966): 	at android.app.ActivityThread.main(ActivityThread.java:5017)
E/AndroidRuntime(23966): 	at java.lang.reflect.Method.invoke(Native Method)
E/AndroidRuntime(23966): 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:779)
E/AndroidRuntime(23966): 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:595)
E/AndroidRuntime(23966): Caused by: java.lang.IndexOutOfBoundsException: Invalid index 0, size is 0
E/AndroidRuntime(23966): 	at java.util.ArrayList.throwIndexOutOfBoundsException(ArrayList.java:255)
E/AndroidRuntime(23966): 	at java.util.ArrayList.get(ArrayList.java:308)
E/AndroidRuntime(23966): 	at com.github.urho3d.Urho3D.onLoadLibrary(Urho3D.java:50)
E/AndroidRuntime(23966): 	at org.libsdl.app.SDLActivity.onCreate(SDLActivity.java:104)
E/AndroidRuntime(23966): 	at android.app.Activity.performCreate(Activity.java:5231)
E/AndroidRuntime(23966): 	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1087)
E/AndroidRuntime(23966): 	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2159)
E/AndroidRuntime(23966): 	... 9 more
W/ActivityManager(  592):   Force finishing activity com.github.urho3d/.Urho3D
W/ActivityManager(  592):   Force finishing activity com.github.urho3d/.SampleLauncher

-------------------------

cadaver | 2017-01-02 00:58:46 UTC | #2

It looks like that crash would happen if you have no C++ shared libraries (.so files) in your android build, so that the list of libraries to load is empty. There should always be at least one .so (Urho3DPlayer.so in the default build) or else there's nothing to run.

-------------------------

att | 2017-01-02 00:58:46 UTC | #3

Yes, it is my fault, I cleaned my project and rebuild it and every thing is ok.
cadaver, thank you very much.

-------------------------

