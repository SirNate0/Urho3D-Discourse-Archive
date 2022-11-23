AppaXD | 2017-12-16 20:02:36 UTC | #1

So, uh, I don't know if you guys like still maintain the editor or if you removed it or something (I'm new), but when I run editor.bat I get this error:

![image|558x133](upload://msrnzffgg2ZtkEor898wJDLnYcT.png)

-------------------------

Eugene | 2017-12-16 21:07:24 UTC | #2

What's the Urho3D-1.7? Cloned sources, build binraies or SDK installation?
Do you have Urho3DPlayer exe?

-------------------------

AppaXD | 2017-12-17 21:27:22 UTC | #3

I do not have Urho3DPlayer.exe. When I downloaded Urho3D I downloaded the zip from the github website, is there like an install or something?

-------------------------

Eugene | 2017-12-17 21:32:42 UTC | #4

[quote="AppaXD, post:3, topic:3855"]
When I downloaded Urho3D I downloaded the zip from the github website, is there like an install or something?
[/quote]

Well, if you downloaded source code from GitHub, you have to build it like any other C++ CMake framework.

-------------------------

AppaXD | 2017-12-17 22:11:42 UTC | #5

Was the zip supposed to come with Urho3DPlayer.exe?

-------------------------

Eugene | 2017-12-17 22:14:23 UTC | #6

Binary packages from here, probably.
https://sourceforge.net/projects/urho3d/files/Urho3D/
Never used them tho.

-------------------------

weitjong | 2017-12-18 00:51:05 UTC | #7

The prebuilt binary packages may come from AppVeyor CI server (using VS) or Travis CI server (using MinGW). The former is slow (because its free service only provides 1 CPU with minimal capabilities) so we set it up to disable the tool building option on normal CI build. The release build should have the tool built-in.

-------------------------

