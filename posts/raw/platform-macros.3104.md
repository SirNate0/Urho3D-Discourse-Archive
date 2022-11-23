KVADRO | 2017-05-05 13:49:02 UTC | #1

Hello world! Does Urho3D provide platform identify macros such as CC_TARGET_PLATFORM, CC_PLATFORM_IOS,... in cocos2d-x?

-------------------------

weitjong | 2017-05-05 15:06:08 UTC | #2

We don't explicitly define the preprocessor macros for each platform, but only when it has not been defined yet. See these lines of code.

https://github.com/urho3d/Urho3D/blob/60f4a3b80f2a2f987e2f119caa1a150a0945c753/Source/Urho3D/Core/ProcessUtils.cpp#L389-L408

-------------------------

