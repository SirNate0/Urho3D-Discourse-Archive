krstefan42 | 2017-01-02 01:13:35 UTC | #1

Hi there. I want to implement linear-space rendering in Urho3D. Normally input textures are stored in sRGB color space, which is gamma corrected. Does Urho3D re-linearize textures before performing shading? And does it perform any gamma correction step on output? Because those two steps are what's necessary for linear rendering, I think. (I almost feel like I asked this before, but I didn't see it in my previous posts).

-------------------------

cadaver | 2017-01-02 01:13:35 UTC | #2

In short: textures have SetSRGB() (srgb mode can also be specified in texture config xml) to enable conversion in sampling, similarly Graphics class has SetSRGB() to perform backbuffer conversion. Additionally there's GammaCorrection postprocess. By default none of these are enabled; you can mix and match for your pipeline as you wish.

-------------------------

