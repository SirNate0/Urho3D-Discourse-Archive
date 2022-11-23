Taqer | 2022-01-13 17:17:46 UTC | #1

Hello, I've encountered a weird problem lately.

I've been struggling with this for a few hours.

If I spawn a few objects that use any of material that has transparency, (or material that has ALPHAMASK psdefine)
and then I spawn some ribbon trails and after a short amount of time I destroy them and spawn again very quickly, I can see some glitching, the materials with transparency are weirdly flickering, which you can see there:

[flickering cat boxes (not virus)](https://streamable.com/bnofbu)

It also happens when I'm quickly switching their emitting by SetEmitting() function. In the video I spawned like 100 of ribbon trails, but this glitch seems to appear independently of their count.

For ribbon trail I use default SlashTrail.xml material, but If I change its technique to non-alpha, the flickering disappears.

I encountered this problem when working in my game where I switch ribbon trails often, and manipulate their's lifetime to give them better look, but I can't stand this flickering.

I'm using Urho 1.7

-------------------------

SirNate0 | 2022-01-13 21:10:19 UTC | #2

Do your transparent materials provide all the textures they should be (e.g. you actually have an normal map for DiffNormalAlpha), and were all of them successfully loaded? I sometimes slightly similar effects when a texture wasn't found where a model will flicker between multiple different patterns based on model happened to be rendered before it.

Also, I would recommend switching to the master branch. There is a chance that you're encountering a bug that has since been fixed. Maybe something like this:

https://github.com/urho3d/Urho3D/issues/2326

https://discourse.urho3d.io/t/urho3d-v1-7-released/3464/15

-------------------------

Taqer | 2022-01-13 21:35:35 UTC | #3

I'm pretty sure it's not about textures since I know this bug and checking it was one of first things I've done.
I will test if it happens on never version though.
Thanks for tip.

-------------------------

Taqer | 2022-01-15 14:29:45 UTC | #4

I checked and it still happens on newest Urho. :frowning_with_open_mouth:

-------------------------

Taqer | 2022-01-27 22:35:49 UTC | #5

Is anyone able to reproduce this?

-------------------------

JTippetts1 | 2022-01-28 00:44:21 UTC | #6

Can you produce a minimal example that exhibits the behavior for people to test?

-------------------------

Taqer | 2022-02-05 21:04:20 UTC | #7

Yes, thanks for reply
sorry for late response, haven't had much time lately, here's example: [example](https://ufile.io/obfw4q2t)

I placed there code and assets, example has only CatCube material, Cat texture and DiffAlphaMask technique added to standard Urho assets, I also modified EP_RESOURCE_PREFIX_PATHS in Setup method but forgot to change that, so set it to your project name.

-------------------------

Taqer | 2022-02-10 08:10:49 UTC | #8

Anyone getting similar results?

-------------------------

