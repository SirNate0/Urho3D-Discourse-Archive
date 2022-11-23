ChunFengTsin | 2017-05-27 18:27:48 UTC | #1

Hi ,everyone 
I just want to know how build a apk to install;
my computer os is ubuntu 16.04 , and is proplems when：

$ android update Urho3d -p . -t 1

*************************************************************************
The "android" command is deprecated.
For manual SDK, AVD, and project management, please use Android Studio.
For command-line tools, use tools/bin/sdkmanager and tools/bin/avdmanager
*************************************************************************
Invalid or unsupported command "update Urho3d -p . -t 1"

Supported commands are:
android list target
android list avd
android list device
android create avd
android move avd
android delete avd
android list sdk
android update sdk

Any master know how I build a simple "hello world" project in AndroidStudio?
I really not know how to start;
Thanks very much;

-------------------------

weitjong | 2017-05-28 01:53:47 UTC | #2

We have not updated our build scripts for Android platform. Currently the documentation is still using old instructions and is still referring to now-defunct ```android``` sub-command when you use the latest Android SDK. This is a known issue. Use the "Search" functionality in the forum to see how others solve the issue. There was also a discussion to modernise the build script to use Gradle. I would even advocate to use gradle-script-kotlin (I found the new DSL in release 0.90 is quite nice to work with already). The question is, who will do it first for Urho3D project.

-------------------------

