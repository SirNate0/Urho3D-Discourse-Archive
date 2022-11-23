Don | 2017-04-30 21:07:42 UTC | #1

I'm a completely new developer to Urho3d, and our team saw this project and it seemed to fit the bill. We are looking at making a real-time terrain renderer with a focus on graphical quality. Has anyone worked on something like this in Urho that can help us get started with what shaders/techniques we should use? Based on what I have seen on the forums and features list, I assume we will have to manually implement the following:

-SSAO
-Improved water shader with vertex displacement
-LOD with vegetation (such as automatic bill-boarding)

I apologize for being a bit unspecific or technical, since I don't have too much experience with OpenGL/graphics. Anyways, if someone could help us understand roughly the process for getting where we want, it would be much appreciated. Thanks!

-------------------------

smellymumbler | 2017-04-30 22:26:50 UTC | #2

There's some SSAO stuff here:

https://github.com/sabotage3d/UrhoSSAO

And some GI here:

https://github.com/reattiva/Urho3D/commits/GI_work

But if you want an open-source engine with photorealistic rendering capabilities, i suggest Panda: https://github.com/tobspr/RenderPipeline

-------------------------

dragonCASTjosh | 2017-05-01 23:13:50 UTC | #3

Depends what you are looking for within the engine is self there is PBR (no terrain support but should be easy to add), area lights(PBR only), physical light values such as lumens and Kelvin. There is also HDR, Bloom, Auto Exposure and a tonemapper that would help. Look at the PBR sample for a base.

In the community there is loads, IV seen realtime GI, 2016 Doom's motion blur, SSAO, Parallax occlusion mapping, Atmospheric scattering and much more. Anything you can't find you can suggest and most of the time someone is willing to lend a hand.

-------------------------

artgolf1000 | 2017-05-02 01:56:15 UTC | #4

Urho3D has no Global illumination now, I am afraid that only Unreal 4 can give you what you want.

-------------------------

Don | 2017-05-02 14:06:47 UTC | #5

Thanks for the many suggestions. While I wish UE4 was an option, their cross platform support isn't as extensive as Urho's. It sounds like Urho can be modified (and has). Since features like SSAO have at least been started on, our team will modify that work for our own project. Thanks again !

One last thing, is there any good documentation on the intersection of materials/techniques/render paths? I am unfamiliar with any of these terms from OpenGL.

-------------------------

