slapin | 2017-03-12 17:46:43 UTC | #1

Hi, all!

I render 50+ NPCs each containing of 16 meshes, 20K triangles each.
Render consumes 50% of frame, and I don't like it. So I have some questions.

1. If I change 4 x 1-texture materials to 1 x 4-texture material will it be faster? I don't want to make textures too big as this will limit hardware support (or can Urho handle this automatically?).

2. Will merging .mdls to a set of multi-geometry mdls do me anything good?

3. It looks like script fire simulation consumes 0.25 of frame each, is there some
shader-based method to simulate light from candle/fire which would not consume CPU so much?

4. What are steps to reduce CPU consumption by animations? I used animationLodBias to seriously
reduce CPU load. If I swap character models to special low-poly one for distant characters, will that
improve situation? I really don't want to do this as this leads to somewhat ugly results an graphics
looks like from 1990s, but anyway...

-------------------------

Modanung | 2017-03-12 23:35:19 UTC | #2

Adding LODs to your models could help. Here's a [quick tutorial](http://discourse.urho3d.io/t/how-to-exporting-lods-with-blender/2083) on how to achieve this in Blender.

Turning down the range of the lights and their shadow detail will also save on rendering time.

-------------------------

