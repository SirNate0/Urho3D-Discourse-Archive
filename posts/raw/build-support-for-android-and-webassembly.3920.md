gunbolt | 2018-01-07 13:01:48 UTC | #1

1. Proper instructions or easy way to build for Android using android studio.
2. Support webassembly.

-------------------------

rku | 2018-01-07 13:01:48 UTC | #2

Example of android build in AndroidStudio can be found in my fork. Just open [this folder](https://github.com/rokups/Urho3D/tree/master/Android) in AndroidStudio.

-------------------------

gunbolt | 2018-01-07 13:01:48 UTC | #3

Not useful because it doesn't work right out the box with latest Android Studio. There needs to be a proper official support for the latest Android studio and latest NDK release.

-------------------------

weitjong | 2018-01-08 05:28:48 UTC | #4

Our official online documentation for Android build support has not been updated to use Gradle yet. The Ant build instructions are indeed obsolete now. If you search the forum, you should be able to find a workaround solution to import the existing legacy Android project to Gradle. It can be done via Android Studio or IntelliJ. Granted that it is not the proper solution. There is an open issue in our GitHub issue tracker to upgrade the Android build support to use Gradle, even Gradle with kotlin-dsl (was called Gradle Script Kotlin back then). I have been waiting for the latter to reach production-ready state, and the wait is almost over now. I have been using it already in my project at work. Don't hold your breath though.

As for WebAssembly build support, you should be happy to learn that it is already supported since Urho3D 1.7 release. It is still being marked as experimental, so your mileage may vary.

-------------------------

