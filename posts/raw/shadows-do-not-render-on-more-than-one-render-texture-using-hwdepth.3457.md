SeanV | 2019-05-23 13:20:02 UTC | #1

Hello, I'm working on integrating OpenVR into Urho3D, but I've noticed a problem when using more than one Render Texture with hardware depth.

Only the last texture to have SetSize() called on it will have shadows. The other texture will have no shadows rendered -- yet if the camera itself is in shadow then the entire scene will be in shadow.

![rendertexture|645x500](upload://TPSefVPXYyZOGjYnsAyMhH3cvb.jpg)

This can be verified by altering the RenderToTexture sample to have two cameras and two screens. The first render texture will only have shadows if the second render texture is out of view. I can provide this code if necessary!

This bug only occurs when using render paths that make use of HWDepth, like PBRDeferredHWDepth. Notably, the bug does not come up when using ForwardHWDepth.

-------------------------

cadaver | 2017-08-19 14:01:07 UTC | #2

Recommend to make a Github issue, so that this isn't forgotten.

-------------------------

SeanV | 2017-08-20 05:08:12 UTC | #3

Thanks, I'll do that. I was hoping I was just doing something wrong!

-------------------------

