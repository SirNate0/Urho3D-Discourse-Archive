Sleepy | 2019-03-10 16:08:39 UTC | #1

Hi, I've installed the latest release of Urho3D but when I run any of the bundled examples,  or the example [here](https://github.com/urho3d/Urho3D/wiki/First-Project), the Camera transforms are all incorrect. (see attached)
I think this may be due to the OpenGL version on my machine (4.6.0) - but I couldn't find where the gl version is sepecified in the CMake files for the projects. If it helps, I'm currently running Linux using the propriatary Nvidia drivers.![ss|690x388,50%](upload://1M67yjVrFOwXsixMhydyz2QEK5z.png) 
Any help would be greatly appreciated

-------------------------

jmiller | 2019-03-10 18:17:40 UTC | #2

Hello,
Welcome to the Urho community forum! :confetti_ball:

(It seems to me) the GL version used for desktop is specified here:
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/OpenGL/OGLGraphics.cpp#L371

This probably does not shed much light (I could not find in [issues](https://github.com/urho3d/Urho3D/issues) yet), but I think others are likely to.

-------------------------

Modanung | 2019-03-11 10:06:37 UTC | #3

@Sleepy Could you try...

[quote="NinjaPangolin, post:15, topic:4894"]
Removing `-ffast-math` from `Urho3D/CMake/Modules/UrhoCommon.cmake`
[/quote]
The deformations seem suspiciously similar to those @NinjaPangolin was experiencing. 
And indeed, welcome! :confetti_ball: :)

-------------------------

Sleepy | 2019-03-11 10:02:25 UTC | #4

Thanks for the swift responses! Clearly my OpenGL is more than a bit rusty :smile:. I tried removing the `-ffast-math` flag and re-building but that didn't seem to help. Since I'm on GCC 8.2.1, I'll try switching to clang when I get off work and report back.

-------------------------

Modanung | 2019-03-11 10:28:28 UTC | #5

Did you *clean* the build folder before rebuilding? Just to be sure.

-------------------------

Sleepy | 2019-03-11 10:53:47 UTC | #6

Hi @Modanung, I did clean the build folder before rebuilding but without any luck

-------------------------

weitjong | 2019-03-11 11:24:41 UTC | #7

Why not just bite the bullet to try out the master branch?

-------------------------

Sleepy | 2019-03-11 14:06:42 UTC | #8

I was able to rebuild with clang over lunch, which ended up fixing the deformations!

@weitjong - A mix of caution and laziness, I'm hesitant to use the master branches of any of the libraries I generally use, and as a result I didn't even consider using the master branch for Urho3D. Plus, having the latest release in the AUR is really convenient.

Thanks for all your help everyone :slight_smile:

-------------------------

weitjong | 2019-03-12 01:52:02 UTC | #9

The last version was released over a year ago and many things have changed under the hood since then. Although I totally understand your concern, it is a chicken and egg issue. If less people trying the master then it would also mean less people finding bugs in the current master and fixing them by submitting PR, so the master branch remains untested at large. We do not have anyone leading this project at the moment, but I personally think may be we can draft a release out and call it 1.8-RC or something so more people are willing to check it out.

-------------------------

Modanung | 2019-03-12 07:54:13 UTC | #10

@weitjong This also helps to signal some activity since the latest _release date_ is one of the first things people run into that one will judge a project's activity by.

-------------------------

