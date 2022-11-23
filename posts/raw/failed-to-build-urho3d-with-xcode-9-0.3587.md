projector | 2017-09-22 18:34:07 UTC | #1

I could not build Urho3D for iOS system after upgraded XCode to version 9 (it was working with last Xcode 8 version). I have tried building Urho3D 1.7 and 1.6, both gave the same error and warning :

Error :
/Source/ThirdParty/Lua/src/loslib.c:43:22: 'system' is unavailable: not available on iOS

Warning :
'tmpnam' is deprecated: This function is provided for compatibility reasons only.  Due to security concerns inherent in the design of tmpnam(3), it is highly recommended that you use mkstemp(3) instead.

-------------------------

weitjong | 2017-09-22 18:34:01 UTC | #2

I believe this error has already been fixed in the master branch just after 1.7 was released.

-------------------------

projector | 2017-09-22 12:44:45 UTC | #3

I have just tested with latest source code from master branch, yes, it's works with xcode 9. Thanks for your help.

-------------------------

