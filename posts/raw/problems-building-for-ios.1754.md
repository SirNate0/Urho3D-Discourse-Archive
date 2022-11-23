esak | 2017-01-02 01:09:54 UTC | #1

I cannot get my game built for iOS.
I managed to build Urho3D for iOS, but when I try to build my game it complains when linking to Urho3D.

The error message I get in Xcode is:
ld: warning: -headerpad_max_install_names is ignored when used with -bitcode_bundle (Xcode setting ENABLE_BITCODE=YES)
ld: warning: ignoring file /Users/esa/Urho3D-master-20150706/Urho3D-master/BuildIOS/lib/libUrho3D.a, file was built for archive which is not the architecture being linked (arm64): /Users/esa/Urho3D-master-20150706/Urho3D-master/BuildIOS/lib/libUrho3D.a
ld: entry point (_main) undefined. for architecture arm64

I'm not sure which architecture Xcode is building for, especially since only one lib-file is built...
In the Xcode project it says that the these architectures are supported: arm64, armv7, armv7s
I tried to just change to arm64 but without any luck.

When running cmake I have tried with and without -DURHO3D_64BIT=1
I can build for OS X without any problems.
Any help would be greatly appreciated.

EDIT:
I forgot to mention that I just get the build problem when trying to run om my hooked up iPad mini. On the simulator it works.
I just tested another thing now:
Select my device in Xcode + change build setting that it should just build for the active architecture.
I did this both when building Urho3D and my game, and it worked!  :slight_smile: 

But I'm still confused about the different architectures and what I should do when building for publishing to app store!?

-------------------------

