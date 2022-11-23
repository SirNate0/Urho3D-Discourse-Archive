Bananaft | 2018-09-20 20:39:13 UTC | #1

In my project I use deferred lighting, HDR and linear pipeline (not PBR).
There is this annoying banding in albedo. It happens on subtexel level, so after initial sampling and linear interpolation. All images are in lossless PNG.
Pic1 banding example: https://i.imgur.com/phMaSYr.png
Pic2 banding example: https://i.imgur.com/CWAnxLJ.png

A friend of mine suggested me to try and switch albedo buffer to sRGB. It worked:
Pic3 no banding https://i.imgur.com/6vmLvuB.png

But there is a problem. I have two types of geometry. regular polygonal geometry and raymarched geometry (fractal) drawn into the g-buffer by quad command after scene path. After I switched albedo buffer to sRGB polygonal geometry became darker, while raymarched one stayed the same: 

Pic4 before-after comparsion: https://i.imgur.com/47qFQxZ.png

I have to do liear-to-gamma pow(albedo, 1/2.2) in model's pixel shader to compensate for that. So it seems like GPU correctly converts information when quad command writes into sRGB rendertarget, and when lightpass reads it, but not when scene pass writes into it.

Is it a bug? a feature? 

I can also fix this banding by setting albedo buffer to rgba16f format. But that will increase memory bandwidth. And I can't see any quality compromises comparing 8bit srgb to 16bit.

-------------------------

Sinoid | 2018-09-20 21:35:27 UTC | #2

Assuming you're using a texture on the model, it's just how it works. `Read non-gamma corrected texture data -> write non-corrected data to gamma correct buffer -> conversion to gamma ends up darker than desired`. More of a *that's just how the math works out* than bug or feature.

You either correct in the shader or set your input texture to be sRGB as well, which does the 1/2.2 (`pow(1/2)` actually) by itself. 

Not sure if it applies to newer Intels, but the older ones hate using hardware sRGB - it was horrifyingly slow on an HD4000, pretty sure they just emulate it as a full buffer copy of the framebuffer (which murder an already fill-rate limited GPU).

-------------------------

Bananaft | 2018-09-20 22:17:28 UTC | #3

Thank you for reply. Yes, it seems like only models with textures are affected. All my albedo textures are set to srgb, however, with srgb albedo buffer I can see diferent behavior on same texture.

Just figured, that urho does not convert textures on load as I thought, so it seems that quad command and  scenepass model read textures diferently, rather than write rendertarget diferently.

-------------------------

Bananaft | 2018-09-21 06:41:51 UTC | #4

[quote="Sinoid, post:2, topic:4558"]
Not sure if it applies to newer Intels, but the older ones hate using hardware sRGB - it was horrifyingly slow on an HD4000, pretty sure they just emulate it as a full buffer copy of the framebuffer (which murder an already fill-rate limited GPU).
[/quote]
I have raymarched 3d fractal, deferred shading and light scattering, Intel 4000 can go straight to hell.

EDIT: I mean, you probably have to set resolution to 640x480 to get double digit fps, don't think extra buffer copy will make any difference.

I think even deferred shading alone is too much of fill rate overhead for HD 4000. I

-------------------------

