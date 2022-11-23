dertom | 2019-12-30 20:23:11 UTC | #1

Hiho. I just finished writing a [blender addon to help bake materials](https://github.com/dertom95/addon_bake_groups) to textures and in this process to also create atlas-textures that have multiple bake results on one texture for multiple objects (with simple auto creation of the corresponding uvmaps).
My question. Let's say I have 4 buildings with different geometry but the same material and use those buildings multiple times in the scene. Does that have any noticeable performance effect in comparison to using one material per building? Instancing-wise there shouldn't be a difference
As I see it the only pro in using an atlas-texture and therefore having only one material for those objects would be that there are no state-changes needed, right? But I guess that this shouldn't be that much of a perfomance-boost, or does it? 

Two thing I have in mind how to make it useful after all: 
1) reanimate to merge (some) objects to one mesh in the exporter (maybe to specify collections or all children of one 'merge'-master)
2) to merge meshes at runtime. like [ogre's staticgeomerty](https://github.com/OGRECave/ogre/blob/master/OgreMain/include/OgreStaticGeometry.h)

Guess I will start with the 1)

-------------------------

S.L.C | 2019-12-31 01:54:15 UTC | #2

Technically it should have a significant improvement on the performance. As those models can be rendered in a single batch (so to speak).

I guess you need to use the profiler and see where your bottlenecks actually are (if indeed you have any). But yes, this approach should guarantee you better performance.

Couple of downsides is that you'll probably loose mip-mapping so you'll need to actually re-create the same model several times in lower details (LODs).

If you enable mip-mapping you should see some issues in the textures when rendering your morels at longer distances. So you definitely want to disable this feature and rely on LODs to reduce GPU usage.

And it might also make modeling a bit more tedious.

-------------------------

suppagam | 2019-12-31 16:40:58 UTC | #3

Would your add-on help me use Blender as a lightmap baker for Urho? Usually I use Blender's "link" functionality to create scenes using modular pieces (wall.blend, window.blend, etc), which then I bake into a single model and export to Urho, with lightmap in UV2.

-------------------------

dertom | 2020-01-01 10:13:02 UTC | #4

I'm not 100% sure. Maybe. I don't think that you could use the 'atlas creation' with linked objects... 

What my addon does, is just managing bake-processes. You create groups of objects where you specify the objects and its uvmaps that should be used for the baking process and select multiple bake-types 'diffuse','ao','shadow',etc and its corresponding textures to bake to.Once you hit 'bake' the objects are selected automatically and the list of bake-type is iterated over, baking it to the specified textures...

Here an example how it looks like:
![image|561x500](upload://e4MoT5nS2G1nNTj0UJ5VV7hdU5A.png) 

I'm actually neither an expert in baking nor in cycles,...In my special case it would have been fine to just convert bmp-textures to png but no,...I have to write an addon ;)

PS: If you give me a test-case of your setup and tell me exactly what you need, I'm will try to implement that to my plugin (if it fits)

-------------------------

