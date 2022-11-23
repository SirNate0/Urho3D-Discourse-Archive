Leith | 2019-05-21 03:00:59 UTC | #1

I'm ready to start adding vfx to my project. 
Blood splatter decalemetry looks like a good place to start.

I noticed that the DecalSet class has support for applying decals to skinned meshes - is there any example implementation of this feature?

I also noticed that DecalSet and ParticleEmitter are quite unrelated classes - that's unfortunate but I can live with it...

-------------------------

George1 | 2019-05-21 03:40:52 UTC | #2

Search for Lumak car trail.

-------------------------

Modanung | 2019-05-21 12:42:56 UTC | #3

@George1 I suppose you mean this?
https://discourse.urho3d.io/t/vehicle-skid-strips/2018

I don't think that uses decals, but rather custom geometry.

[quote="Leith, post:1, topic:5168"]
is there any example implementation of this feature?
[/quote]

I am unaware of any, nor did I try this feature.

-------------------------

Leith | 2019-05-22 02:52:02 UTC | #4

I've spent some time examining the sourcecode of DecalSet to try to understand the skinning aspect of it... It appears that the magic happens in the AddDecal method, where we pass in a target Drawable.
If that drawable is skinned, then the whole DecalSet object switches into "skinned mode" (I don't know what happens to any static world decals we already added to the set?) which tracks bone transforms to drive the decals (again not sure what happens to existing static decals).

It looks like I need to dedicate at least one DecalSet to the static world, and another for each kinematic object, whether or not it is skinned.

Also, DecalSet appears to have no support for "AutoRemove"... that's not a good fit with particle splatter... the HandleScenePostUpdate method does remove decals whose lifetime has expired, but does not auto-remove the component when the count reaches zero - we're stuck with polling the count of all DecalSet instances manually, from outside of that class.

-------------------------

Modanung | 2019-05-22 05:53:52 UTC | #5

[quote="Leith, post:4, topic:5168"]
we’re stuck with polling the count of all DecalSet instances manually, from outside of that class.
[/quote]
You could inherit from `DecalSet` and add this functionality to the resulting class.

-------------------------

Leith | 2019-05-22 06:08:35 UTC | #6

Well I could indeed reinvent the wheel too, I'll tell you what, I'll do that - I'll derive a workable use case example and implementation, I'll push the changes back into DecalSet, and I'll issue a tiny PR.

I see a lot of scope for ParticleEmitter and DecalSet to work together, even though their parentage is very different, they should both be candidates for auto removal when their job is done.

-------------------------

Leith | 2019-05-25 05:07:57 UTC | #7

I tested decal skinning and it's very easy to implement.
Basically the decalset class is good to go - just use the sample #8 as a guide, to add decalsets to drawables and it will just work, though you may want to change the decal material technique and texture to meet your needs, and you may need to increase the default values for max vertices and indices in new decalset objects.

-------------------------

