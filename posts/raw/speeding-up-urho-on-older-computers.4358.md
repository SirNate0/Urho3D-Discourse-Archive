smellymumbler | 2018-06-27 14:59:02 UTC | #1

Do you guys recommend any tweaks or changing compile time options to speed up the engine on older computers?

-------------------------

S.L.C | 2018-06-27 19:12:34 UTC | #2

How old? And this depends on the game itself too. Because you can make a game/application with Urho that even new hardware has trouble running it. So is it old and weak or is it old but powerful? Does it lack full support of necessary features? (_performs some form emulation internally to achieve that_) Give an example of such "old" hardware and so that people can have a base.

But most of the time. Most of the performance can be gained from the game assets and effects.

-------------------------

smellymumbler | 2018-06-27 20:26:51 UTC | #3

Yes, it depends on the game, that's why I'm focusing on speeding up the included samples. The one I'm using right now is CharacterDemo. By choosing this as a base, I know how fast things can run and keep policing myself when adding new content, handling scenes, etc. 

How old: any i3 laptop with generic Intel GMA.

-------------------------

smellymumbler | 2018-06-27 20:30:32 UTC | #4

Some data: Today this demo runs at ~110 FPS. I wanted 200+.

FYI: 42_PBRMaterials runs at 30 FPS.

-------------------------

slapin | 2018-06-27 21:07:35 UTC | #5

Have you enabled profiler and found where all the performance go?

-------------------------

Eugene | 2018-06-27 22:08:56 UTC | #6

[quote="smellymumbler, post:4, topic:4358"]
Some data: Today this demo runs at ~110 FPS. I wanted 200+.
[/quote]

What's the point of speeding up samples?
You won't play samples, you will play games.
What's the point of wanting 200 FPS?
You won't see more than 60 FPS.
If you want to use 120+Hz display with such old hardware, you are doing things wrong,

Some hints:
- Forward Render path
- Accurate Octree setup
- No scripts
- Less active physic objects
- Less logic components
- Less node updates
- Less drawables, more manual batching for small static objects
- Less custom geometries
- Less shadows
- Less lights (if I implement lightmapping in nearest future)

You see, these are quite obvious. If you want to make things faster, compute less.

-------------------------

smellymumbler | 2018-06-27 23:56:56 UTC | #7

[quote="Eugene, post:6, topic:4358"]
Accurate Octree setup
[/quote]

Can you elaborate on this?

-------------------------

fnadalt | 2018-06-28 01:48:44 UTC | #8

My PC is about to celebrate its 10th birthday... 
4.17.2-1-ARCH
AMD Athlon(tm) 64 X2 Dual Core Processor 4600+
NVIDIA Corporation MCP61
Cedar [Radeon HD 5000/6000/7350/8350 Series]
HD SATA 1
2GB RAM!!!

I tried other proprietary and open source 3d engines and Urho3D surprised me

-------------------------

Eugene | 2018-06-28 06:31:31 UTC | #9

[quote="smellymumbler, post:7, topic:4358"]
Can you elaborate on this?
[/quote]

Default Octree size is 2k*2k, it's ok default size, but could be tuned better.
Also don't make your scene bigger than Octree bbox, all objects that don't fit the Octree are culled one-by-one.

-------------------------

smellymumbler | 2018-06-28 15:41:07 UTC | #10

Thanks! How can I tweak this option? What's the rule of thumb here, the octree should be about the same as total scene size?

-------------------------

Eugene | 2018-06-28 16:22:10 UTC | #11

Scene bounding box shall be as small as possible and contain _most_ of the objects.
Play with Octree parameters (max depth and BBox) and check what's better. It may give you small benefit during scene update.

-------------------------

