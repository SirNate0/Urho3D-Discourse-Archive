xenodora | 2017-08-08 13:40:49 UTC | #1

I've been messing around with soft bodies physics using the code from this thread: https://discourse.urho3d.io/t/bullets-softbody-physics-example/1319 , and have been able to get the jello mushroom working.

After doing this I started work on doing partial model soft body so that things like hair can be done. To achieve this, I found I need to be able to get the vertex weight values from weight groups, so that vertices can be marked as immobile, or affected by soft body physics.

I briefly thought about saving this data to separate weight files, but discarded the idea as it's a recipe for easy desynchronization. As such, I decided that this data should be saved in the model.

Presently I'm appending the vertex weight data file with a block formatted like this:

       'WGHT' - 4 byte identifier of the block
       block size - UInt the number of bytes in the block (not including the identifier and block size)
       vertex group count - UInt The number of vertex groups contained in this block.
       vertex group list - A list of Vertex Groups, with the format detailed just below.

    Vertex Groups:
       vertex group name - C string name of the group.
       index size - UInt Number of bytes in an index (2 or 4).
       vertex count - UInt
       vertex weight list - A list of Vertex Weights, with format detailed just below.

    Vertex Weights:
       vertex index - UShort or UInt The index of the vert
       weight - float A float in the range of 0.0 to 1.0 with the weight of the vertex.

So far it's working fine, but I'm not sure if this is the best way to add this feature into the Urho3D model file. Should the block be formatted differently? Should the data actually go else where in the file? Or are separate files a better option?

-------------------------

Lumak | 2017-08-08 14:47:43 UTC | #2

[quote="xenodora, post:1, topic:3432"]
So far it’s working fine, but I’m not sure if this is the best way to add this feature into the Urho3D model file. Should the block be formatted differently? Should the data actually go else where in the file? Or are separate files a better option?
[/quote]

Yeah, I wouldn't modify the Urho3D model file format but go with what you already suspect - a separate file option, leaving the Urho3D model file format unchanged would allow you to work with anyone's models.

-------------------------

Modanung | 2017-08-08 15:41:53 UTC | #3

But the models should already store vertex groups and weights somehow for bone animation, right? :confused:

-------------------------

xenodora | 2017-08-09 08:51:57 UTC | #4

[quote="Modanung, post:3, topic:3432"]
But the models should already store vertex groups and weights somehow for bone animation, right? :confused:
[/quote]
Not exactly, from my reading of Urho3D model file format, bone weightings are stored in the vertex, and only 4 bones can be associated with a single vertex, and those weights must add up to 1, which normally means they're rescaled. If the original model had more than 4 bones affecting a vertex, it would keep the 4 with the largest weights, and discard everything else.

I could certainly abuse the bone weight list by adding phantom bones or using special weight values, and ignoring the summing to 1 rule. However, that will involve rejigging the model loader to handle the special cases, and creating models that might behave badly if loaded into other Urho3D software that lack the rejigged loader. Additionally it would have a limit of 4 vertex groups for normally boneless models, and lower for models that use actual bones.

-------------------------

SirNate0 | 2017-08-09 19:33:40 UTC | #5

I don't know if the mdl file supports it, but I think you can declare somewhat arbitrary vertex semantics that would let you add the weights (I've never messed with it myself, though).

https://urho3d.github.io/documentation/1.6/_vertex_buffers.html

-------------------------

