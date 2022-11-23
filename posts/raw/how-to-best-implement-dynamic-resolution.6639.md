kairature888 | 2020-12-28 19:25:55 UTC | #1

I need the rendering to happen in a lowered resolution and then get stretched over the entire screen. I currently shrink the viewport to a small corner and am looking for a way to stretch this smaller corner over the entire screen. Something like rendering a fullscreen quad whcih samples from the smaller corner. Im not sure how to create a renderpath to do this.

-------------------------

SirNate0 | 2020-12-28 19:40:29 UTC | #2

Hi @kairature888, welcome to the forum!

For your problem I'd suggest rendering to a texture and then rendering that to the full screen. There might be better approaches, though. I'm no expert in rendering stuff.

-------------------------

kairature888 | 2020-12-29 09:09:26 UTC | #3

How do I set up a render path to achieve that?

-------------------------

jmiller | 2020-12-30 02:06:16 UTC | #4

You may want a persistent rendertarget..
as in [PostProcess/AutoExposure.xml](https://github.com/urho3d/Urho3D/blob/master/bin/Data/PostProcess/AutoExposure.xml) (demoed by [42_PBRMaterials](https://github.com/urho3d/Urho3D/tree/master/Source/Samples/42_PBRMaterials)).
You might also find the [10_RenderToTexture](https://github.com/urho3d/Urho3D/tree/master/Source/Samples/10_RenderToTexture) sample interesting.

-------------------------

evolgames | 2020-12-30 18:57:03 UTC | #5

This might help.
https://discourse.urho3d.io/t/whats-the-right-way-to-go-about-pixellation/5863/8

-------------------------

