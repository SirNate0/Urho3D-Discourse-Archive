halcyonx | 2017-05-28 10:51:57 UTC | #1

Hi everyone! I created classic application "Hello world" for android using Urho3D. I've used Urgho3D_repo/Android for this purpose. In Android/ locates dir src/com/github/urho3d in this folder exists 3 java sources:
1. SampleLauncher.java
2. ScriptPicker.java
3. Urho3D.java
Should I use this files from my own application? Is this java sources necessary to correct work my app? There is sence to write own java source, or I can use these 3 files and just replace all "Urho3D" and "Urho3DPlayer" entries?
Also in Android/src there is org/libsdl/app/SDLActivity.java this file also is necessary for work android application?

I want create simple 2d game for android. I want to write main logic in C++ in VisualStudio and part of logic and configures in Lua.

P.S. Sorry for my poor English.

-------------------------

weitjong | 2017-05-28 12:49:49 UTC | #3

You only need the Java classes from SDL package. You don't necessarily keep the classes from com.github.urho3d package. But of course your project will always need and depend on Urho3D library.

-------------------------

