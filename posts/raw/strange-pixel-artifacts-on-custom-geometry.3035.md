napard | 2017-04-22 14:11:16 UTC | #1

Hi everyone,

I'm working on custom geometry generation for a very minimal voxel engine (not true voxels technically speaking). On rendering stage I note some strange little holes like missing pixels on quad borders. They randomly appear and disappear when moving around. Has anyone experimented this issue? All vertex positions seem to be correct for me :confused:

 <img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/e38442a603603f32bc49e7393e57c482661f3b29.png" width="598" height="500">

I'd like to be sure I'm not missing something when setting up vertex positions...
Thanks in advance...

-------------------------

slapin | 2017-04-21 21:53:48 UTC | #2

My wild guess is bounding boxes...

-------------------------

napard | 2017-04-22 04:05:48 UTC | #3

It's not bounding boxes but...

Now I'm afraid it has to do with some identical polygons occupying the exact same place, maybe some mismatch at depth buffer level. The strange thing is, even if there are two polygons at the same place, they are oriented in reverse to have always one of them culled, but I think that's not enough and it produces weird rendering results on the corners where two or more quads touch themselves, I would need someone to please confirm this, I have not much experience with 3D graphics or OpenGL in general... Some behavior may seem odd to me but it's in fact the expected default.

I'll do some more testing on this...

And sorry for my English if there is any mistake, it's not my native language...
Cheers!

-------------------------

SirNate0 | 2017-04-22 05:29:55 UTC | #4

Depending on how you generate the mesh it could be an artifact related to T-Junctions in the edges of your mesh. See https://0fps.net/2012/07/07/meshing-minecraft-part-2/ for a brief discussion (he concludes it's not a problem, except possibly on some graphics cards, so this may not be the cause of your artifacts).

-------------------------

Enhex | 2017-04-24 15:42:33 UTC | #5

Looks like T-junctions. The cause of it is usually when you have two triangles with shared edge, but not shared vertices, and because of floating point precision error the edges don't perfectly align and you get those epsilon gaps which causes these pixels (which are what you got from behind).

A solution is to detect those shared edges and split them to make sure all vertices are shared.

imagine both edges are overlapping:
v1._____.v2

v3.__________.v4

Edges are on the same line, but v2 and v4 aren't at the same position, which causes precision error.

to fix the T-junction:
v1._____.v2

v3._____._____.v4
-----------v5

Added v5, which as the same position as v2, so the edges 1,2 and 3,5 use exactly the same vertex positions.

-------------------------

napard | 2017-04-22 14:15:56 UTC | #6

[quote="Enhex, post:5, topic:3035"]
Looks like T-junctions
[/quote]

Yes, 90% sure that's the case, thanks for the info, and I will have to deal with it as part of my poorly implemented but working greedy meshing method. Having tested on a cheapy integrated video board at work this problem is very visible, but there should be more factors related to this I think...

On a sidenote, if you look carefully, you can see the same issue on http://mikolalysenko.github.io/MinecraftMeshes2/ using "Sphere" as data source, but in his T-Junction test there isn't any cracks because the mesh in the test is quite simple compared to the sphere, so maybe it is not a good test ;)

-------------------------

Sinoid | 2017-04-24 03:21:58 UTC | #7

> On a sidenote, if you look carefully, you can see the same issue on http://mikolalysenko.github.io/MinecraftMeshes2/7 using "Sphere" as data source, but in his T-Junction test there isn't any cracks because the mesh in the test is quite simple compared to the sphere, so maybe it is not a good test :wink:

Probably just WebGL being WebGL, unless you're referring to the Z-fighting when edges are rendered.

-------------------------

rasteron | 2017-04-24 06:43:03 UTC | #8

Not sure if this is only in custom geometry, I also noticed this on most PBR demos here.

-------------------------

Sinoid | 2017-04-24 07:07:06 UTC | #9

[quote="rasteron, post:8, topic:3035, full:true"]
Not sure if this is only in custom geometry, I also noticed this on most PBR demos here.
[/quote]

sRGB and RGB mishaps perhaps? Hopefully ... those minor goofs will cause mishaps with abrasive artifacts both high or low.

-------------------------

rasteron | 2017-04-24 07:17:48 UTC | #10

[quote="Sinoid, post:9, topic:3035"]
Not sure if this is only in custom geometry, I also noticed this on most PBR demos here.

sRGB and RGB mishaps perhaps? Hopefully ... those minor goofs will cause mishaps with abrasive artifacts both high or low.
[/quote]

I don't know, but I already posted an issue and sample hilighted it [here](https://cloud.githubusercontent.com/assets/3676827/25325271/4c264836-28fd-11e7-9457-cb64220efa6a.png). There's a few more in there that I just missed out if you examine closely.

-------------------------

Sinoid | 2017-04-24 07:35:13 UTC | #11

Thank you. The rects around artifact areas is helpful.

-------------------------

rasteron | 2017-04-25 00:22:37 UTC | #12

sure thing JSands, just trying to help out and see these bugs as I see it, particularly if it is included in the demos or latest commits.

-------------------------

