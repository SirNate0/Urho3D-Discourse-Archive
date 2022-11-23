Enhex | 2017-01-02 01:05:53 UTC | #1

Hi,

I'm working on an offline lightmap baking system using Blender Cycles.
I have to face a batching problem, and I don't know how Urho's culling work in order to make the right decision. Here's the problem:
To use lightmaps another UV map and texture are added to the material.
In order to minimize the number of diffuse textures per lightmap I want to group the geometry with the same diffuse texture, so I get less combinations of diffuse & lightmap.

The thing is, I wonder how Urho3D is culling based on location.
If I simply group geometry with the same diffuse texture into a single model, the geometry can be spread all over the level and the model could have a huge AABB. Will it cause performance problems?
For optimal performance, is it required to group the geometry based on location too?

-------------------------

Enhex | 2017-01-02 01:05:53 UTC | #2

[quote="Sinoid"]
Your mileage is going to vary with vertex count and screen space consumed. Culling order is Octree->Frustum->Occlusion (I could be wrong though, and I don't believe occlusion is used for everything such as shadow casting lights etc). It'd work though.
[/quote]
Are the octree/frustum/occlusion per triangle or per model?
If some of them are per object, not grouping based on location will make them useless.

Also what do you mean by "implement lightmap support directly"?
I remember that the lightmap technique uses the emmisive slot for the lightmap texture.
How does the renderable sorting thing works in Urho?
I'm guessing it means you order the order of the rendered models by lightmap so they're batched together?
My current plan is to generate the materials in real-time.
Does Urho3D batch models by material by default?
If so is there an advantage for doing the batching your way?

-------------------------

cadaver | 2017-01-02 01:05:53 UTC | #3

All culling is per-object, not per-triangle.

The rendering will sort object drawcalls based on material, to minimize state changes, and also uses hardware instancing automatically for same object + same material combinations, to reduce draw calls. But it doesn't perform any vertex buffer manipulation to combine dissimilar static objects together into the same draw call.

-------------------------

friesencr | 2017-01-02 01:05:53 UTC | #4

There are some code paths that will cause a drawable not be drawn.  Camera/Object viewmask, object draw distance come to mind.  There are a few states I have produced in my own code where I was missing data in components and they were invalidated during the view rendering phase.  I have not of set the number of batches or didn't have a vertex stream or didn't set the world bounding box or something like that.

-------------------------

