godan | 2017-04-25 15:56:25 UTC | #1

Yep, just got it working ([test it out here](https://meshgeometry.github.io/Demos/PBR/IogramPlayer.html)): 

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/e98c3092b4264db5847ea9e6b673c83598b170f0.jpg" width="690" height="377">

Controls:
- RMB to orbit
- CTRL + RMB to zoom
- SHIFT + RMB to pan

Also, this probably won't run on mobile. Would be great to hear back about any issues on various browsers/platforms, though.

-------------------------

KonstantTom | 2017-04-25 14:13:50 UTC | #2

Windows 7, FIrefox 53.0 (64-bit).
All works perfect! But FPS is very low.

-------------------------

godan | 2017-04-25 14:16:31 UTC | #3

@KonstantTom what are your system specs?

-------------------------

KonstantTom | 2017-04-25 14:30:36 UTC | #4

@godan I found the problem: it's because Intel HD Graphics is default video card on my PC. After I force Firefox to use Nvidia GeForce, FPS become normal. :slight_smile:

-------------------------

Mike | 2017-04-25 15:39:53 UTC | #5

Works great :slight_smile:
Controls are RMB instead of LMB.

-------------------------

johnnycable | 2017-04-25 18:45:05 UTC | #6

Works good on my mac! Great job!
No way on ipad browser: it shows the scene, but doesn't move.

-------------------------

godan | 2017-04-25 21:04:55 UTC | #7

Well, I don't think I've coded a touch version of the orbit cam, so it might actually be working fine! I will get on that :slight_smile:

Can you move the slider at all?

-------------------------

dragonCASTjosh | 2017-04-25 22:00:22 UTC | #9

@godan Do you intend to merge these changes back into master. If not would you be willing to share your changes so PBR can be accessed on all platforms.

-------------------------

monkeyface | 2017-04-25 23:22:21 UTC | #10

Very cool! Now all we need is realtime reflections.

-------------------------

godan | 2017-04-26 00:17:49 UTC | #11

[Like this?](https://meshgeometry.github.io/Demos/FancyPBR/IogramPlayer.html)

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/91a021c6bb0017e057d1e64306e000fc19555d91.png" width="690" height="378">

-------------------------

dragonCASTjosh | 2017-04-26 00:48:53 UTC | #12

I'd assume the reflection there are done by updating the reflection probe. If I get time id like to look into Screen Space Reflections but i have been very busy at the moment

-------------------------

monkeyface | 2017-04-26 09:06:44 UTC | #13

That looks cool @godan !
Would you be able to get that into the Urho core or does it rely on your framework too much?

I would really like to use your cool shader stuff in a game but tbh I can't really tell how it can be used outside the Iogram editor.

-------------------------

godan | 2017-04-26 12:59:35 UTC | #14

> @godan Do you intend to merge these changes back into master. If not would you be willing to share your changes so PBR can be accessed on all platforms.

Yes, I will definitely push the PBR changes back to the main repo. The changes are actually minimal and entirely in the shaders. The trick was finding them! Debugging webgl is such a pain :slight_smile:

As for the reflection probes, I'm still experimenting with them (also would like to hear more about your screen space reflection idea), but yes, I would be fine with pushing that back to Urho as well.

-------------------------

johnnycable | 2017-04-26 13:38:24 UTC | #15

I was able to move the slider just once

-------------------------

Modanung | 2017-04-26 13:46:29 UTC | #16

Nice progress!
Apart from an unresponsive script warning while loading it works fine here in Firefox 52.0.2 on 64-bit Linux Mint.

-------------------------

lexx | 2017-04-26 15:03:46 UTC | #17

Works great (up-to-date chrome,  w7 x64,  amd 7870). All controls works.

-------------------------

dragonCASTjosh | 2017-04-26 20:32:08 UTC | #18

[quote="godan, post:14, topic:3046"]
I'm still experimenting with them (also would like to hear more about your screen space reflection idea)
[/quote]

Screen Space Reflections is a way to do real time reflections doing reflection traces as a screen space effect. There are many ways of doing it but the best i found was probably frostbites approach [found here](http://www.frostbite.com/2015/08/stochastic-screen-space-reflections/).

Pros:
 - good performance compared to other solutions(planar, realtime cubemaps)
 - high quality results
 - intergrates well with PBR (e.g per pixel roughness)

Cons:
 - only reflects what is vissible
- sometimes color diffrances between SSR and Cubemaps causes distracting reflections

-------------------------

Lumak | 2017-05-01 19:18:42 UTC | #19

Isn't this similar to how light probes work? Looking forward to your release.

-------------------------

