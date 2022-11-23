Handkoden | 2017-01-02 01:07:39 UTC | #1

Hi! Gotta say, I love the engine. I have one problem though, I can't get the engine to work correctly on iPad Air 2.
I did the following:
1. Pulled latest master-branch from github
2. Ran the cmake_ios.sh script both with and without -DURHO3D_64BIT=1, didn't make a difference.
3. Everything compiles in Xcode (v7) without errors.
4. If I try to run the Urho3DPlayer I get a bunch of warnings from Angelscript saying something like "Failed in call to function 'RegisterObjectMethod' with 'Engine' and 'int get_maxFps() const' (Code: -7)". It outputs warning for every single function it seems like. Then and empty message box from Urho3DPlayer appears on the iPad and then nothing else happens.

I also tried to compile the sample "04_StaticScene.cpp" and link it with the static library. This also works without errors, however when I run it on the iPad graphical glitches appear:
[img]http://i.imgur.com/ru4Zb0Z.jpg[/img]

I have tried this on three different devices with the following results:
iPad Air 2 (iOS 8.4) - The problems above happens.
iPad Air 2 (iOS 9.0) - The problems above happens.
iPad 2 (iOS 7.1) - Note that this is not an Air 2 but an older iPad 2. Everything seems to work correctly here, the Urho3DPlayer launches without problem and the 04_StaticScene runs without graphical glitches.

So there seems to be a problem involved with either the newer iOS versions or the newer devices. Has anyone else been able to solve this? Any help is appreciated :slight_smile:

-------------------------

Handkoden | 2017-01-02 01:07:39 UTC | #2

Update: I managed to solve the graphical issues by defining -DURHO3D_OPENGL=1 in my project, since it apparently included the D3D9-vertexbuffer header file instead of the OGL one.
The AngelScript issue still exists though, maybe some more compiler flags doesn't get set correctly for arm64?

-------------------------

weitjong | 2017-01-02 01:07:40 UTC | #3

Welcome to our forum.

Most likely. I will see what I can do with URHO3D_OPENGL build option. As for Urho3DPlayer crashes, I think it has to do with AngelScript library support for __arm64__. EDIT: Just checked. Angelscript library does not support native calling convention for ARM64. Unfrotunately, Urho3D API is currently only bound to AngelScript using native calling convention.

-------------------------

weitjong | 2017-01-02 01:07:40 UTC | #4

Re URHO3D_OPENGL. I cannot see any problem with our current existing script. This build option should be set for all non-Win32 platforms. The only potential problem I see where it might not be set correctly is when you have shared a build tree path between Win32 and non-Win32 platforms without first clearing the CMake cache. Something that could happen if you do not use out-of-source build tree for example. If this is not the case or if you can reproduce the problem again in a clean build tree then you can log this as an issue in Github.

-------------------------

Handkoden | 2017-01-02 01:07:40 UTC | #5

Thanks :slight_smile:
That's good to know about AngelScript. Luckily I will do everything native for now so it won't affect me too much.
The URHO3D_OPENGL build option was from an empty folder where I cloned the master branch into. I'll see if I can reproduce it later today

-------------------------

