najak3d | 2020-04-20 01:20:18 UTC | #1

From what I can tell, UrhoSharp is in good enough shape for us to use.  And it appears that Urho itself is quite a capable engine.   If there are issues with UrhoSharp specifically, we should be able to fix those wrapping issues, as they arise.

Does anyone know how to get a anti-aliased line drawing to work in Urho Sharp, similar what is described on this link:

https://developer.nvidia.com/gpugems/gpugems2/part-iii-high-quality-rendering/chapter-22-fast-prefiltered-lines


(in short, they only use one vertex per Poly-Point, but then use GPU magic to generate a line width that fades off as it gets further from the center line)

-------------------------

SirNate0 | 2020-04-20 02:16:54 UTC | #2

How much do you know about writing shaders? I feel like it would just be a matter of writing the appropriate pixel shader for a wireframe model. Others with more experience may be able to provide more useful assistance, though, as I have only a small amount of graphics programming experience.

-------------------------

najak3d | 2020-04-20 04:05:51 UTC | #3

I'm in process of brushing up on my shader knowledge now.  I've written some medium-complexity shaders in the past.

-------------------------

najak3d | 2020-04-20 04:10:32 UTC | #4

Where is an example project that uses shadows?  Oddly, shadow technique is entirely missing from the Urho Samples project.   That's worrisome.  I would have figured that Urho made Shadows able to turn on or off with relative ease.

-------------------------

JTippetts1 | 2020-04-20 06:05:04 UTC | #5

Almost all of the samples have shadows enabled.

-------------------------

najak3d | 2020-04-20 13:56:51 UTC | #6

Hmmm, NONE of the UrhoSharp version of these samples has shadows.  I'm very glad to hear that shadows for normal Urho3D is working, which means it probably can be accessed from UrhoSharp, just not sure why they haven't done it already.

-------------------------

najak3d | 2020-04-20 14:01:35 UTC | #7

OK - found the issue -- it's UWP that has the problem.  

https://github.com/xamarin/urho/issues/374

Does normal Urho3D have shadows working for UWP? (does Urho3D even run on UWP?)

-------------------------

JTippetts1 | 2020-04-20 15:01:13 UTC | #8

There hasn't been any work on UrhoSharp in a year. It's dead. I remember reading some years ago about UWP support in vanilla Urho, but I dont believe it is officially supported. Could probably get it going with a little effort.

-------------------------

