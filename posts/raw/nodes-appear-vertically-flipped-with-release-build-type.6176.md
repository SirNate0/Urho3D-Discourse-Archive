mikolan | 2020-05-25 10:56:47 UTC | #1

I have a Urho3D 1.5 based digital signage application which generates some flat rectangular models and textures them with images.
This has run fine on Raspberry Pi 3 and Intel AMD64 cpu's for quite a while.

Recently, I've tried building against different hardware (I've had to rebuild because the new HW does not support some of the instruction set for the older platform) and I've noticed a common issue, where my textures will appear flipped vertically.
This only appears when linking against the Urho3D library built with Release build type.
Has anyone run into anything like this?

-------------------------

SirNate0 | 2020-05-26 13:41:57 UTC | #2

Maybe related to the -ffast-math option?
If that's the case see https://discourse.urho3d.io/t/problems-with-3d-samples-on-win10/4894/15 and https://discourse.urho3d.io/t/weird-output-for-any-program/4446/8 for potentially related issues.

-------------------------

mikolan | 2020-05-26 13:42:58 UTC | #3

Thank you!

Commenting out the -ffast-math lines from the Urho3D CMake module seems to have done the trick!

-------------------------

