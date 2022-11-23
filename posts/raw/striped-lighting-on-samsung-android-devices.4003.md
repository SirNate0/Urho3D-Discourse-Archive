Dimous | 2018-02-10 05:25:56 UTC | #1

Hello!
I downloaded stable Urho3d 1.7 Android 32-bit STATIC release, built on Windows 10 64x, NDK r15c, default cmake_android settings and ran demos on 2 Samsung devices:

Samsung Galaxy J3, Android 5.1.1
![1|690x388](upload://ajQZXN0aJHDbPOZUz1mD1bI8FnZ.png)

New users can put only one image...

Everything seems to work fine, except lighting. Is it device-specific problem, or should I tune something in cmake?

-------------------------

Sinoid | 2018-02-10 06:46:20 UTC | #2

>  Is it device-specific problem, or should I tune something in cmake?

Wouldn't be anything in CMake for this.

**The early fading:**

On GLES (mobile) only 1 cascade is used for directional light shadow maps. The physics demo uses a really small first cascade of 10 so that's why you have the shadows fading off so soon.

It also probably doesn't help anything here.

**The banding:**

Probably a bias issue, there's the *Depth Constant Bias* and *Slope Bias*. I'd make the *Depth Constant Bias* on the light a little bigger (it's 0.00025 in the sample) first. 

I can reproduce somewhat similar issues on a desktop by using a bias that's too small, though there's differences.

![image|476x258](upload://qoY7zDWAIQvniDrgGPL1nInxlWL.jpg)

-------------------------

Dimous | 2018-02-11 05:29:10 UTC | #4

Thanks, Jonathan! I'll play with BiasParameters, when I get android demos _built from git_ working.

-------------------------

