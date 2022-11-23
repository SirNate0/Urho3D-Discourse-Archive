slapin | 2018-04-06 09:11:14 UTC | #1

Hi, all!

Recently I have been trying to reestablish attempts to find workflow to make 160+ bones
meshes work in Urho3D. Plain and simple we have 2 problems:
1. Bone count limit per geometry is quite small. While big engines like UE4 and Unity
somehow manage, Urho can't handle lots of bones. The solution which seems obvious is to split mesh using materials, and that is where we het second issue
2. For multi-geometry meshes, only first geometry is affected by skeletal deformation.
This issue can be addressed by mesh splitting (even naive approach works) but we have the following issue with split meshes:
Regardless of how meshes were produced, either exported as separated parts or multi-geometry, we have visible seams in shading. Also when bones are animated, we see holes in mesh.

So what I'm trying to do is finding seam vertices and make their normal and blend weights and indices the same (set from main geometry to all other parts). **Is this idea looks sane?**
If yes, what would be most efficient way to do that? Looping over all vbs for all positions seems extremely slow (takes about 20 minutes per model with 40K verts on i7). Is there some alternatives?

-------------------------

Lumak | 2018-04-06 10:08:37 UTC | #2

I've always been curious about how or why you have so many bones in your model. Can you PM me your fbx file - need it in fbx format if you can.

-------------------------

slapin | 2018-04-06 10:23:55 UTC | #3

That is makehuman character, nothing private.
It is simple - for lod0 I need fancy details.
we have 30 bones for each arm.
4 bones each limb
face rig and spine remains. Ubisoft and Naoghty Dog have much more (400-500 bones for runtime animation), so I try to achieve at least 164 bones, which is much less ambitious...

-------------------------

Lumak | 2018-04-06 10:31:32 UTC | #4

I'm not interested in installing makehuman to see the type of model you're working with. I imagine it's similar to Mixamo.  Too bad you can't just send me one of you fbx file.

-------------------------

slapin | 2018-04-06 10:34:47 UTC | #5

Ah, no problem, I will send it as I get to where it is (I currently babysitting, so I can't leave room for that, will do in a hour two, maybe three). It is immediately not accessible for me.

-------------------------

Sinoid | 2018-04-06 12:04:41 UTC | #6

[quote="slapin, post:1, topic:4152"]
Bone count limit per geometry is quite small. While big engines like UE4 and Unity
somehow manage, Urho can’t handle lots of bones.
[/quote]

1. You have the source, bump up the bone limits. There's room for at least 768 on desktop (UBOs  enabled on gl3) - you still want as few as possible because shader setup isn't free, especially not with a cbuffer near the cap. Or just implement CPU skinning and be done with it.

2. Create a proxy mesh+rig for MakeHuman that isn't absurd.

[quote="slapin, post:1, topic:4152"]
what would be most efficient way to do that? Looping over all vbs for all positions seems extremely slow (takes about 20 minutes per model with 40K verts on i7). Is there some alternatives?
[/quote]

You generate the canonicalized mesh first. Then iterate the canonicals and their colocals. The same as almost all mesh processing.

-------------------------

johnnycable | 2018-04-06 12:48:22 UTC | #7

Post a picture of the skeleton. I'm curious.
Having all that bones count for a lot of attachments...

-------------------------

slapin | 2018-04-06 13:38:13 UTC | #8

As forum for some reason does not allow fbx or blend upload here is link:
http://ossfans.org/test_male.fbx

-------------------------

slapin | 2018-04-06 13:39:37 UTC | #9

[quote="Sinoid, post:6, topic:4152"]
You generate the canonicalized mesh first. Then iterate the canonicals and their colocals. The same as almost all mesh processing.
[/quote]

I'm trying to read it again and again and my brain fails to understand. Could you please elaborate?

-------------------------

slapin | 2018-04-06 13:43:07 UTC | #10

Also I need to mention that this is LOD0 (max details possible). As I see, gamedev monsters easily use 300-500 animation bones (and 200+ directly controllable bones) for close detail layer without a problem.
With split geometry I want a compromise (lots of bones and still can go hardware for most platforms).
So I wonder what path should I aim for.

-------------------------

slapin | 2018-04-06 13:46:16 UTC | #11

btw, I did not include textures,
so don't worry about looks - the skeleton is still there.

-------------------------

slapin | 2018-04-06 13:50:06 UTC | #12

I was just told that I can breach bone counts somewhat using dual quaternion skinning.
Any idea what is this?

Also, is there some easy to use software skinning library, which would allow me to do partial skinning (software + hardware), with compatible license?

-------------------------

slapin | 2018-04-06 13:56:09 UTC | #13

To illustrate what I'm talking about: https://www.youtube.com/watch?v=myZcUvU8YWc&t=13m37s

https://www.gdcvault.com/play/1022411/Massive-Crowd-on-Assassin-s

-------------------------

johnnycable | 2018-04-06 15:26:43 UTC | #14

Ok. You have a (quasi) full facial rig. I suppose you want best control on face morphs.
I see a unusual number of bones in the feet, unless you want your character to play guitar with feet, those are probably never to be seen...
There's a double upperarm bone, but someone models it that way...
Not an high amount of bones, considering you have full face and full hands.
Only thing I can tell you could save on feet and eventually substitute facial for shape keys, if you can accept losing some control...

-------------------------

slapin | 2018-04-06 19:41:18 UTC | #15

I'd prefer to keep control as this allows some nice animations. Also if I remove some bones I will add them back as clothes rig (skirt/coat/attachment). So I'd be much more happy to know how to have sane workflow and keep bones. Currently I seems close as I do not have to split mesh to seoarate meshes in Blender, I just make it into a set of geometries by material. This should allow me to keep shading, but it doesn't for some reason (still visual seams and bone deform holes) and make number of of meshes on Blender scene sane, and splitting is done by C++ code, splitting separates geometries into separate models.

If I manually split everything, I don't have holes on bone bending, but still have visual seams. Not good.

-------------------------

Lumak | 2018-04-07 00:55:52 UTC | #16

I looked at your model and agree with johnnycable - you should do away with the toe joints (30 bones total) ... unless you're making some kind of foot-fetish game then you probably need it.

Judd from NaughtyDog's video talks about +- 85 runtime driven keys and +-241 animation sample joints, which are skinned skinned to something and described as just "baked" in Maya as if those joints are not exported. I don't quite understand what this means because "baking" animation in Maya that I know just quantizes animation keys per frames to gets rid of in-betweeners. Not sure if he's describing a in-house tool that does something special to reduce the overall runtime driven joints to +-85 joints.

In the Assassin's creed presentation, the bulk animation bone count is pretty high, but what it doesn't tell you is whether they're using a single mesh with that high bone count. They could possibly be swapping in separate high-res body model, head model, cothes, etc. at runtime to me would be more ideal than to have npcs with 300+ bone count on a single mesh.

[quote="slapin, post:15, topic:4152"]
If I manually split everything, I don’t have holes on bone bending, but still have visual seams. Not good.
[/quote]

This is exactly what I'd do if I were in your shoes. Create an attachable/exchangeable high-res face w/ bones and low-res face without bones will save you... from neck up, 63 bones. Doing this and removing the toe bones will reduce your runtime driven joints to ~72 joints.

-------------------------

slapin | 2018-04-07 01:36:27 UTC | #17

I found some remedy to a part of problems - using separate vertex buffers for each geometry, which magically fixes weights. I still have to split the mesh in code though. So no more visual seams for body.
The problem is I want to go a bit farther in this direction and use this method for character customization, i.e. when adding clothes, the body parts which are completely hidden should be removed from display - how can I do this? This is mainly to prevent body from poking through tight clothing at distance.

-------------------------

Sinoid | 2018-04-07 01:47:51 UTC | #18

[quote="slapin, post:9, topic:4152"]
I’m trying to read it again and again and my brain fails to understand. Could you please elaborate?
[/quote]

The perfect-graph mesh without any duplicates. You either maintain a table of indices for the colocal vertices or use an intrusive linked list from the first canonical vertex to each of the duplicates. For any given vertex you then have all access to all other vertices in the same location - colocal.

Any decent half-edge mesh library will do it as part of building the mesh, LibIGL and CGAL have helpers for the task as well. It's a basic requisite of any non-trivial mesh processing, from bent-normals, CSG, laplace to UV charting.

-------------------------

johnnycable | 2018-04-07 07:52:06 UTC | #19

Visual seams: generally because normal are not consistent across seams. Maybe uv not correctly unwrapped?
Flesh poking thru garments: it's a skinning problem, vertex weights on skin/garments are not consistent, so they deform differently.
Removing parts from display: it's dynamically driven by user choice so has to be done in code (a clothing application)
Separating vs complete mesh: in Blender it looks like area of influence is bound to the object, so separated objects behave per-se. Non sure to which extent this goes. Still elaborating on this.

You could check [Avastar](https://blog.machinimatrix.org/avastar/compare-to-workbench/) workbench for Second Life for Blender. It's a bit dated, but could be of help...

-------------------------

