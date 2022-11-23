spwork | 2019-01-02 09:13:57 UTC | #1

I try do build android version in win7,it has some problem:
    FAILURE: Build failed with an exception.

    * Where:
    Build file 'D:\Documents\2\Urho3D-master\android\launcher-app\build.gradle.kts'
    line: 94

    * What went wrong:
    A problem occurred configuring project ':android:urho3d-lib'.
    > Failed to notify project evaluation listener.
       > NDK not configured.
         Download it with SDK manager.
       > Task with name 'bundleDebugAar' not found in project ':android:urho3d-lib'.

       > Task with name 'zipBuildTreeRelease' not found in project ':android:urho3d-
    lib'.

    * Try:
    Run with --stacktrace option to get the stack trace. Run with --info or --debug
    option to get more log output. Run with --scan to get full insights.

-------------------------

spwork | 2019-01-02 09:16:41 UTC | #2

I used the latest Urho 3D-Master build and gradlew. bat build with reference to the documentation, but if something goes wrong, who can tell me the specific process, it's better to tell me step by step, because I think Android build is too difficult.

-------------------------

spwork | 2019-01-02 15:21:42 UTC | #3

    exe" -E copy_if_different D:/U/Source/ThirdParty/rapidjson/include/rapidjson/str
    ingbuffer.h D:/U/android/urho3d-lib/build/tree/Debug/x86_64/include/Urho3D/Third
    Party/rapidjson/stringbuffer.h && cd /D D:\U\android\urho3d-lib\.externalNativeB
    uild\cmake\debug\x86_64\Source\ThirdParty\rapidjson && "E:\Android SDK\cmake\3.6
    .4111459\bin\cmake.exe" -E copy_if_different D:/U/Source/ThirdParty/rapidjson/in
    clude/rapidjson/writer.h D:/U/android/urho3d-lib/build/tree/Debug/x86_64/include
    /Urho3D/ThirdParty/rapidjson/writer.h"
      ???????????
      ninja: build stopped: subcommand failed.
can't build thisI also checked other posts and found no solution. Who can help me?

-------------------------

weitjong | 2019-01-03 12:45:34 UTC | #4

Have you read this thread https://discourse.urho3d.io/t/new-gradle-build-system-for-android-platform/4380/70, especially the last few posts. I also want to stress a few important points in the [Android build documentation](https://urho3d.github.io/documentation/HEAD/_building.html#Building_Android) for Windows users. Firstly, the asset dirs must be manually patched as per documented above. Secondly, set the environment variable to tell the build system where is your Android SDK and/or Android NDK when they are not in their default expected location. Set "ANDROID_HOME" for the former and set the "ANDROID_NDK" for the latter. In general, if you install Android SDK in the system default location and then use the provided "sdk manager" to download the embedded NDK and embedded CMake then there is no env-var that you need to manually set. Our documentation assumes the reader is familiar with Android build. If not, you need to head to https://developer.android.com/ first. And lastly, at the moment our Android build only works for Windows 7 host system because Ninja build only works well there and not in Windows 10. Good luck.

-------------------------

spwork | 2019-01-03 10:07:50 UTC | #5

I used linux to do the same thing, and finally succeeded, but there was another problem: too many files were compiled, 27G, my hard disk was full, would you also produce so many files?

-------------------------

weitjong | 2019-01-04 00:35:32 UTC | #6

There is no canonical way to build Urho3D. Depending on what build options are being enabled, one would get a different customized build result. Having said that, our default build options (when user does not explicitly set them one way or another) are decent one for native/desktop build, but that may not be so good for Android build. The default URHO3D_SAMPLES=1 and URHO3D_LIB_TYPE=STATIC alone would already generate 50+ *.so with Urho3D library statically linked, not to mention the Android Gradle plugin will do that twice (one for Debug build config and one for Release) and will do all of that 4 times over (one for each ABI). In short, tweak the build options to get the custom build result that you desired. Use split ABI and use SHARED lib type instead. Or turn off URHO3D_SAMPLES so the sample launcher will just launch script player (either AS or LUA or both). etc. etc.

-------------------------

