Sheridan | 2018-11-28 12:06:23 UTC | #1

Greetings, friends. I am writing another minecraft clone and I want to combine the blocks into a single object. I want to make the union not by chunks, but “each with a neighbor” when placed. The architecture for this solution has already been invented and implemented, it remains to "write one function" :)
I read this forum, but have not yet understood where to start.
What is now incomprehensible:
1. how to combine meshes? Are there any tools for this or do you need to do it manually?
2. Is it possible to use different materials? That is, is an object possible with a single mesh and different materials in different parts?
3. How to apply a texture to the resulting complex structure? Generate a large texture dynamically (I am doing this for cubes now) or is it possible to impose a texture separately on each face?

ps I have never done 3D before. I’m writing the last three weeks :)

-------------------------

Sinoid | 2018-11-28 01:38:34 UTC | #2

Not following your first paragraph.

1. I have a collection of [procedural geometry helpers](https://github.com/JSandusky/Urho3DProcGeom/tree/master/ProcGeom)
    - Those should show you how to work with the raw geometry functions
    - It's easier if you can just define a known `vertex struct` instead of working with raw buffers
    - Basically you have to transform and concatenate the vertex/index buffers in order to merge meshes
       - there isn't a function to do that in there, but I could add a limited one that requires identical vertex layouts
2. Each mesh in a model gets a single material, there's no fixed limit on the number of meshes in a model
    - you can work around that in a pixel-shader (like the terrain splat shader does)
3. Options:
    - use an atlasing scheme and set the UV coords for each face
    - use texture arrays and an encoding scheme such as UDIM
    - use multiple meshes in each model, one for each material containing only the faces relevant
        - because of depth-test this isn't as *bad* as it sounds, still not great, but not terrible

Again, couldn't quite follow your first paragraph so this next paragraph might be irrelevant:

Ideally however you don't do this by merging geometries. You should really be using some kind of surfacing algorithm, whether naive or greedy meshing (see the [0fps articles](https://0fps.net/2012/06/30/meshing-in-a-minecraft-game/) if you haven't already gone through them, they're reasonable introductory material.

-------------------------

