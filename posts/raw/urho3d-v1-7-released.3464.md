cadaver | 2017-08-19 19:44:19 UTC | #1

Out now. Thanks to all contributors! Highlights include inverse kinematics, RaycastVehicle, AppleTV platform support, WebAssembly support. 

Release post: https://urho3d.github.io/releases/2017/08/19/urho3d-1.7-release.html
Source code: https://github.com/urho3d/Urho3D/tree/1.7
SourceForge file archives: https://sourceforge.net/projects/urho3d/files/Urho3D/1.7/

Note that there were already some debug build issues fixed in master, so the usual advice goes, use head revision for the latest. Possibly a new release with the fixes might be made sooner than usual.

-------------------------

Eugene | 2017-08-19 20:43:40 UTC | #2

Is our CI is C++11-compatible now?

-------------------------

DraGiuS | 2017-08-19 20:54:21 UTC | #3

Opengl 4.6/Vulkan support ?

-------------------------

Eugene | 2017-08-19 21:46:30 UTC | #4

Vulkan is not used by Urho. However, there were experiments with DX12. What do you mean by OpenGL 4.6 support?

-------------------------

DraGiuS | 2017-08-19 21:47:24 UTC | #5

https://www.khronos.org/news/press/khronos-releases-opengl-4.6-with-spir-v-support

-------------------------

Enhex | 2017-08-19 22:43:20 UTC | #6

I think putting efforts into other things will provide better value.
Using newer graphics APIs won't improve things much AFAIK.

There are other domains which need to be worked on. For example some GUI improvements (I got some improvements I plan to contribute), high level networking features(Client Side Prediction, NAT punchthrough), graphical features (ex. provide SSAO implementation, global illumination solution), audio effects (ex. Doppler Effect, reverb).

-------------------------

TheComet | 2017-08-20 01:02:07 UTC | #7

Congrats on the release!

[quote="Enhex, post:6, topic:3464"]
global illumination solution
[/quote]

This is something I'd particularly like to see in Urho, sooner than later.

-------------------------

Eugene | 2017-08-21 08:57:33 UTC | #8

@weitjong Does the CI use C++11 compatible compiler now?

-------------------------

weitjong | 2017-08-21 12:49:03 UTC | #9

For C++11 standard, yes.

-------------------------

Eugene | 2017-08-21 12:53:24 UTC | #10

Great!
So, URHO3D_C++11 build option and corresponding guards could be removed, couldn't they?

-------------------------

weitjong | 2017-08-21 13:16:15 UTC | #11

Even better, you could remove the URHO3D_C++11 build option all together, i.e. enable the standard by default and no option to turn it off, thus no compiler define guard needed as you pointed out. If you are brave enough, you can also try to use the modern CMake way to enable the C++11 compiler features instead.

-------------------------

Bluemoon | 2017-08-21 18:27:34 UTC | #12

Awesome work everyone. Congrats

-------------------------

johnnycable | 2017-08-22 10:25:12 UTC | #13

Great job!
Didn't know there were binaries... always compiled from source... :laughing:
me dumb... :roll_eyes:

-------------------------

coldev | 2017-08-22 14:50:52 UTC | #14


Thanks nice work .. !!  :heart_eyes:

Please next release with  instanced skeletal animation example... :blush:

-------------------------

weitjong | 2019-05-25 02:24:28 UTC | #15

The Urho3D 1.7 requires a small patch in order to make it build correctly with GCC 8 or newer without encountering the rendering issue during runtime. After a long delay we have decided to backport the patch and re-release 1.7 as 1.7.1. Everything else are the same as 1.7. So, this 1.7.1 is not recommended for anyone who plan to start a new project using Urho3D library, use our master branch instead.

-------------------------

