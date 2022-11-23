smellymumbler | 2017-03-14 04:56:14 UTC | #1

Interesting implementation: https://ebruneton.github.io/precomputed_atmospheric_scattering/

-------------------------

jmiller | 2017-03-14 19:43:03 UTC | #2

It is a fantastic implementation (even better now that the codebase has been rewritten), highly GPU compliant with beautiful results... as seen in several videos like this.
https://www.youtube.com/watch?v=0I7Af2Ev5iQ

-------------------------

rasteron | 2017-03-15 23:57:56 UTC | #3

You can check out Bananaft's Zarevo experiment, it does have some nice atmospheric scattering among other stuff.

http://discourse.urho3d.io/t/zarevo-landscape-experiments/1256

https://github.com/Bananaft/zarevo/search?q=scattering&type=Commits&utf8=%E2%9C%93

-------------------------

bmcorser | 2017-03-16 13:11:50 UTC | #4

This stuff is damn beautiful. How expensive is the precomputation? Is it something that could feasibly happen in game, or does it take hours (eg. for the stuff that @Bananaft did) ... ? I would love to have generate geometry and precompute lighting "just in time" before it was visible to the player.

-------------------------

Bananaft | 2017-03-16 13:59:33 UTC | #5

Hello. My method is fully dynamic. Its also just an artistic coding and has nothing to do with physics.

Here is the basic formula:
https://www.shadertoy.com/view/MdtXD2
And another version with more mild colors:
https://www.shadertoy.com/view/ldyXRz
You can drag sun with mouse in both of them.

In terms of performance it's pretty light for a modern system.
Current github version is a bit broken, sorry.

-------------------------

bmcorser | 2017-03-16 14:57:29 UTC | #6

Oh, very cool -- I just looked at the images and assumed you were using the same technique.

Has anyone tried Eric Bruneton's code? I got about half way through attempting to compile the sources on OSX, but gave up. I'll have a go on my Linux box when I get back to it ...

-------------------------

