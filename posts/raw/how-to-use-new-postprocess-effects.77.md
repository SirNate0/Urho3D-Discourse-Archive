szamq | 2017-01-02 00:57:48 UTC | #1

I tried to append it to renderpath like in demo with GrayScale and I have all screen green

[code]
    RenderPath@ effectRenderPath = viewport.renderPath.Clone();
    effectRenderPath.Append(cache.GetResource("XMLFile", "PostProcess/GammaCorrection.xml"));
    //effectRenderPath.SetEnabled("GammaCorrection", false);
    viewport.renderPath = effectRenderPath;	
[/code]

When I uncomment third line, program looks good but obviously without the effect. Changing effect name to old ones (EdgeFilter, Bloom...) works and effect is visible.
Win7 Opengl enabled

-------------------------

friesencr | 2017-01-02 00:57:50 UTC | #2

I am doing basically the same thing in the viewport example but with windows + directx.

I am getting results but it seems like the the SetEnabled("GreyScale", false) is being overriden? and is enabled on start.  The toggle works fine.  Oddly the bloom didn't start out that way so there something funny going on.

Also I don't think you are supposed to eat the shrooms...
[img]https://dl.dropboxusercontent.com/sh/empwv5npk7oh352/5Tqe7A8w8S/urho-acid-trip.PNG?token_hash=AAFIoI4lUSY8uWrOcmzuvQZh1gvEF83KWR-zDK7JlyIiZw[/img]

-------------------------

cadaver | 2017-01-02 00:57:50 UTC | #3

Hmm, on a Win7 OpenGL build (NVIDIA GPU) I didn't see odd things like the screen turning green on any of the effects.

If there's anything odd with toggling the effects on/off, check the tag names in the postprocess effects to make sure what you're enabling/disabling/toggling. ToneMap effect actually contains 3 different effects, of which TonemapReinhardEq3 is enabled by default and the rest are disabled.

-------------------------

szamq | 2017-01-02 00:57:50 UTC | #4

Here is my little report with postprocess effects. Some of them not working when using OpenGL, using clean master source.

Blur- DX working, OGL -Black screen
ColorCorection - both DX and OGL can't really see difference when toggling this effect
EdgeFilter- both works
GammaCorrection - works
GreyScale - works
Tonemap - works
AutoExposure - I love this effect, looks cool, however it works only with DX. With OpenGL screen is all white.
Bloom - looks awesome when BloomMix increased to some value like -10 10
BloomHDR - works, but I needed to change BloomHDRMix to higher values to see some changes

-------------------------

cadaver | 2017-01-02 00:57:50 UTC | #5

There's probably a shader error in GLSL Blur. Didn't actually notice there was a matching postprocess effect for that shader. It shouldn't be hard to fix.

I remember I got the "screen constantly white" on one run in AutoExposure / OpenGL, then it worked on a subsequent run. It's using data from the previous frame and actually the renderpath framework doesn't guarantee that a render texture allocated for a renderpath would be the same on a subsequent frame, so it needs adding a mechanism for that.

EDIT: Blur postprocess definition fixed. Added the concept of persistent rendertargets, and initial clearing of float rendertargets on OpenGL. I suspect the constant white effect was from the 1x1 luminance texture containing illegal value (NaN) which meant it would never converge correctly. On Direct3D9 this would not happen.

-------------------------

friesencr | 2017-01-02 00:57:50 UTC | #6

I will check again later if i can reproduce the enabled when set disabled.  Lasse you are probably right.

as for that picture it was me horsing around with the color correct shader.  i should have specified.  i was having fun.  i was trying to make the most obnoxious change to LUTIdentity.png.  I have found adding noise is pretty obnoxious.  I might try doing some time effect and shifting  the coordinates of the texture lookup based on time.  I'll have won if i can get a cat to puke.

Seriously thought these new post effects are super cool.  Some of them like the the tonemap I don't understand as well.  I don't understand the origins of the reinhard algorithm.  It is just squashing the brights and darks to more the mid range.

Something I don't have a grasp on yet is shader cost.  In my blissfully ignorant world I assumed addition/multiplication/sqrt all had the same computational cost.  It turns out this isn't true at all!?!   Is the math on the tonemap cheaper then using a texture lookup  on color correct?  color correct obviously uses a 16x256 texture for memory.

-------------------------

szamq | 2017-01-02 00:57:50 UTC | #7

Thanks, now everything works great on OGL.
Also I just figured out that I need to modify LUTIdentity.png texture to actually see something changed with ColorCorrection effect.
@Chris, looks like I ate one of your shrooms
[spoiler][img]https://googledrive.com/host/0B-FH5cooowQpRHVFMGN5eVFuZms/Urho3DPlayer%202014-02-06%2019-20-34-21.jpg[/img][/spoiler]

-------------------------

friesencr | 2017-01-02 00:57:51 UTC | #8

:smiley: that's pretty obnoxious.  i am imagining teenagers going over to rift parties where they put on an occulus rift and see how long they can go without getting a seizure.

its like all my favorite bad 80s, 90s scifi is coming to life.

-------------------------

