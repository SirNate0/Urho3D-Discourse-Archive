topotheo | 2018-02-27 21:22:36 UTC | #1

I want to write a 2.5d game (platformer which uses 3d models instead of 2d sprites). This is my first 3d game.
At the moment I am deciding between either using a full fledged engine like godot (or maybe but probably not unity/unreal) or using something that is more of a framework for the 3d graphics like Irrlicht or Urho3D.

I like doing my stuff in C/C++ and also having freedom around how I write my game logic, that is what speaks for Irrlicht or Urho.
But what bothers me is that if I look at trailers for Unity/Unreal games on youtube, they all have this kind of "modern" (this is subjective of course) light/cute/colourful graphics as seen here: https://www.youtube.com/watch?v=_xXD_9vS56E or here: https://www.youtube.com/watch?v=43wQ-3sV6nE
When I look at youtube videos of Urho3D demos or check out the default installed examples which come with urho they all look very greyish/a bit edgy to me (same goes for Irrlicht). 
They very much remind me of 200x games like Morrowind.

Now I don't know which of the following is the case:
1. The engines just have different shaders and "default" graphics
2. The engines are just from different times and use different technologies which makes the outcome look different

And in both cases, how hard is it to get this kind of more colourful graphics in Urho3d? Do I have to learn about shaders for that? (Or about what?) And how much do I have to learn?

Thanks very much in advance

-------------------------

Dave82 | 2018-02-27 23:50:06 UTC | #2

Well the demo you posted has nothing special Urho3d can't do , except SSAO.As far as i know Urho3D does not support SSAO at the moment. To achive similar effect you could use baked lightmaps but that would be PITA on large levels (critical memory usage probably not suitable for mobiles)

-------------------------

Don | 2018-02-28 02:52:50 UTC | #3

Dave pretty much hit it on the head. The only effect which is outside the repertoire of Urho3D is SSAO, which you would definitely need for that style (first link especially). Outside of that, you could probably achieve a similar look by picking your materials and lighting very carefully. Evidence of this is https://discourse.urho3d.io/t/playing-with-low-poly/3380 which I believe is mostly stock Urho3D except the ambient occlusion and UI styling.

Overall, I would say Godot is a better choice if you wish to steer clear of shader code, but I hear that it is difficult to write a whole project only using C++.

Best of luck on your project.

-------------------------

jmiller | 2018-02-28 03:23:57 UTC | #4

Re. effects, the forum is full of gems like shaders, especially in the Showcase area.

**reattiva**'s SSAO, I like the results.
https://discourse.urho3d.io/t/alchemy-ambient-occlusion/662

rasteron's toon shader (GLSL)
https://discourse.urho3d.io/t/toon-shader-glsl/1800

-------------------------

topotheo | 2018-02-28 16:27:07 UTC | #5

Thanks for all the answers, this already really helps me. I don't know anything about graphics yet, so knowing that this example I was showing uses "SSAO" which I googled afterwards also already helped me. 
As I understand it Dave said to achieve a similar effect you need a lot of memory and Don and carnalis both gave examples of people implementing SSAO in Urho3D. Are these implementations using a lot of memory as Don said or are these actual SSAO implementations in Urho, just not developed by the official engine developers but by the users?

I am not afraid to learn about graphics and shaders. It is quite the opposite. I really would like to learn the basics and apply a few custom effects to my game if time allows. I just don't know how much work this is? I mean to understand enough to get nice looking graphics (for example using this SSAO) in a game as above, how much more development time should I take account for: A few weeks? Months?

-------------------------

Eugene | 2018-02-28 16:40:18 UTC | #6

You've raised great question, @topotheo
The most important, maybe.
Urho lacks good demos, and this is the major disadvantage comparing to.. meh.. other engines.

> And in both cases, how hard is it to get this kind of more colourful graphics in Urho3d?

TL;DR: It's harder than with e.g. Unity, but it's doable. Effort depends on what graphic style do you want to have.

There are some projects that have acceptable (for me) quality of graphics (=I'm ready to play).

 https://discourse.urho3d.io/t/clinically-dead/1395
 https://discourse.urho3d.io/t/greatgame-project/3666
 [Hellbreaker](http://store.steampowered.com/app/793620/Hellbreaker/)
 https://discourse.urho3d.io/t/oblivion-lost-online/3010

BTW, have you checked standard PBR sample? It looks less shameful than other samples. 

___
___

[quote="topotheo, post:1, topic:4062"]
The engines just have different shaders and “default” graphics
The engines are just from different times and use different technologies which makes the outcome look different
[/quote]
These items are pretty close.

Urho has classic shaders written (or copy pasted) from old articles from the era of private commerical engines. Just light, just shadows, just N.L for diffuse and so on. Such shaders are obviously much less tuned and polished than current commerical solutions. AFAIK @dragonCASTjosh is working on some new graphics in the rogue fork.

Urho has no built-in nice features like SSR and SSAO, so the bucket of cubes would look like a bucket of cubes. Urho does only what you ask it to do and nothing more. It's good for somebody, but not very good for the showcase and newcomers.

There is also some set of missing features that could be hard to implement. E.g. physical particles, fluids, clothes, deformations and destructibles provided by PhysX engine. Modern pipelines like clustered lighting and multithreaded rendering, that's mostly about optimization. Personally I don't need it because I have no chance to provide AAA-quality content. But it's definietely impossible to make true AAA-game in Urho without re-writing and extending the engine.

-------------------------

Don | 2018-02-28 19:26:58 UTC | #7

Just a note on the SSAO. Any reasonable implementation should be fairly low on memory (should only be a couple extra framebuffers). What Dave was referring to was lightmapping, which require much more memory for texture storage. As Dave said, this is probably not something you want to do.

On another note, if you're looking into tinkering with shaders, you've come to the right place. Urho uses straight GLSL and HLSL, so modifications are straightforward. As carnalis said, you can probably copy most other users implementations with little or no modifications, so you have a place to get started.

-------------------------

Sinoid | 2018-02-28 20:30:10 UTC | #8

[quote="topotheo, post:1, topic:4062"]
The engines just have different shaders and “default” graphics
[/quote]

Pretty much - most of the Urho3D demos all use the same `Stone` material for everything - causes that *bleh* look and it's desirable for any sample that doesn't deliberately focus on graphics (which is all of them) be runnable on the minimum target (which is as far down as the Raspberry PI) ... so it sticks.

[quote="topotheo, post:5, topic:4062"]
I just don’t know how much work this is? I mean to understand enough to get nice looking graphics (for example using this SSAO) in a game as above, how much more development time should I take account for: A few weeks? Months?
[/quote]

Probably a week, maybe a month at most of graphics tweaks. The basic shaders should cover this case well enough and it's just the SSAO/SSDO thing you'd have to fill in and any other tweaks/niceties you find you need.

It might take you a bit to get used to Materials and Techniques - they're a little awkward at first. Just do it as usual, figure out everything in preproduction and then decide whether to roll with it or roll with something else.

[quote="Eugene, post:6, topic:4062"]
 and multithreaded rendering
[/quote]

To clarify this: there is threading for rendering preparation (gathering drawables, etc) but nothing along the lines of command buffer building ... which won't be terribly relevant for a while on PC outside of DX12.

Though there's also no AZDO/DX11 indirect either to begin with.

[quote="Don, post:7, topic:4062"]
On another note, if you’re looking into tinkering with shaders, you’ve come to the right place. Urho uses straight GLSL and HLSL, so modifications are straightforward. As carnalis said, you can probably copy most other users implementations with little or no modifications, so you have a place to get started.
[/quote]

Even internally the engine also doesn't go out of its' way to extensively hide things from you, so there's none of that PIMPL/handle garbage to dig through and fight against you. Even something as complicated as TressFX was pretty much just a drop-in and a little bit of plumbing to integrate ... would've been either a nightmare or a *"screw it, I'll just short circuit everything"* in one of the plethora of *"let's use bgfx!"* engines.

-------------------------

Leith | 2019-02-02 14:49:50 UTC | #9

So why can't we do SSAO? It's not that hard to achieve
Guess is that nobody here cares enough, or all the guys who knew how to write shaders left.
I am here now. And we have no SSAO? We'll see about that

-------------------------

I3DB | 2019-02-02 15:24:42 UTC | #10

HLSL and GLSL versions if you do please.

-------------------------

Leith | 2019-02-02 15:28:56 UTC | #11

I don't do microsoft anymore, someone else can transcode my gl, fair enough?
=

-------------------------

Modanung | 2019-02-02 16:42:09 UTC | #12

[quote="Leith, post:11, topic:4062"]
fair enough?
[/quote]

Sure, but don't expect a feature to end up in the master branch with half support.

-------------------------

Leith | 2019-02-03 12:36:09 UTC | #13

Hey, if I can get SSAO working for opengl, surely one of you kind gentlemen with more experience in urho would be willing to transcode one shader for hlsl? And if you won't I'll have to consider writing a transcoder, I am not spending my time transcoding when robots can do it. I am a qualified toolmaker, but I don't want to handcraft everything when it can be automated.

-------------------------

Sinoid | 2019-02-04 05:00:51 UTC | #14

Yes, but there's been multiple incarnations of SSAO over the years and all variants have caveats. There's HBAO+ code lurking around on the forums for instance.

Just write your code, make it available and if someone wants to port it they will.

-------------------------

Leith | 2019-02-04 05:31:47 UTC | #15

So, there have been many incarnations of SSAO, but we still have none. Seems doable.

-------------------------

Sinoid | 2019-02-04 05:34:24 UTC | #16

Did you do a search beforehand? There was a forum migration so some code could be lost, but I recall commenting on 5 implementations.

Same basic issue with all of them, they were in one language or the other. I know for certain I hand-held someone through porting an HLSL HBAO+ to GLSL.

-------------------------

Leith | 2019-02-04 07:11:26 UTC | #17

We only have two shader languages to deal with, and I don't need five implementations to sell a game.

-------------------------

JTippetts | 2019-02-05 03:08:53 UTC | #18

Only 2 shader languages, sure, but also multiple shader versions. D3D9/D3D11 and GL/GLES. Granted, that's still not a whole terrible lot, but it's still a hurdle and part of the reason a lot of things like AO are still not in core, because few who work on them now want to make the effort to implement in the environments that aren't their environment of choice. The old cliche holds: if it's worth doing, it's worth doing right. And expecting someone else to do your drudge work of writing shader language permutations is a good way for your project to NOT end up in master.

I think if someone were looking for a worthwhile project to take on, then writing some sort of unified shader architecture frontend that would allow a write once/run everywhere shader model might be a good project to tackle.

-------------------------

Eugene | 2019-02-05 13:18:10 UTC | #19

[quote="JTippetts, post:18, topic:4062"]
then writing some sort of unified shader architecture frontend that would allow a write once/run everywhere shader model might be a good project to tackle.
[/quote]

I'm actually interested in DiligentGraphics. It looks quite promising. Solves a lot of problems and intorduces much less problems...
When I eventually start playing with graphics again, I'll give it a try.

-------------------------

Sinoid | 2019-02-06 03:21:33 UTC | #20

> I’m actually interested in DiligentGraphics. It looks quite promising. Solves a lot of problems and intorduces much less problems…

The couple of times I've tried out it's shader converter it's done a pretty fair job. Haven't tried feeding it anything terribly complex yet though, might give a whirl with these toon shaders since only a few tweaks should be needed to *modernize* them (inputs).

-------------------------

Leith | 2019-02-06 05:11:07 UTC | #21

I'm strongly considering slapping together a GLSL to HLSL transcoder for Urho3D.
It's not that I don't have experience writing DX shaders, I started back on DX8, but I have spent a lot more time writing GL shaders over the years, and feel more comfortable writing and testing them, plus I don't (often) use Windows anymore. Still, it makes sense to me to automate the conversion of GLSL to HLSL, in order to future-proof any shaders that I decide are worth sharing, rather than expect others to do the dirty work, or myself to repeatedly deal with the same time-sapping chore.

-------------------------

