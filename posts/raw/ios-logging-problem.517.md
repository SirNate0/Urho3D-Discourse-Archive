sabotage3d | 2017-01-02 01:01:02 UTC | #1

Hello I created an Xcode IOS project based on sample 18 Character Demo. But I cannot get any logging or debug information to print from Urho3d my output is completely empty can someone please check my project it I have done something wrong.  I uploaded my project to bitbucket, this is the link: [bitbucket.org/sabotage/urhotemplate/src](https://bitbucket.org/sabotage/urhotemplate/src)

Thanks in advance,

Alex

-------------------------

weitjong | 2017-01-02 01:01:03 UTC | #2

The logging on iOS would only work in DEBUG configuration build. Logging on iOS is a no-ops on other build configurations. Note that I did not look at your Xcode project setting, so my apology if that's not it.

-------------------------

sabotage3d | 2017-01-02 01:01:04 UTC | #3

It is set to debug configuration I saw it a few times logging in the output and after that it stopped seems something is messing with the output but I cannot figure what as it is hard to debug. Although I built Urho3d itself only in release is that a problem ?

-------------------------

weitjong | 2017-01-02 01:01:04 UTC | #4

I believe both Urho3D library and your own project has to be built in Debug configuration for iOS logging to work. In the Debug configuration build the following two compiler definition should be defined:
[ul][li]_DEBUG[/li]
[li]URHO3D_LOGGING[/li][/ul]
You did not say how your Xcode project is generated, so I have to ask. If you are using our CMake build scripts to configure and generate both the Urho3D project and your own projects then they should be taken care of for you automatically.

-------------------------

