Enhex | 2017-01-02 01:04:57 UTC | #1

I'm getting those weird shadow glitches which include 2 main things:
1. Shadows deforming when changing camera angle.
2. light slipping through geometry.

[img]http://i.imgur.com/1r9P7ga.jpg[/img]
[img]http://i.imgur.com/bGw7iNL.jpg[/img]
[img]http://i.imgur.com/oLBMZW5.jpg[/img]
[img]http://i.imgur.com/sS5IWM6.jpg[/img]

I assume that it happens because of a naive implementation of my level editor's file format.
I'm using custom geometry to create the level.
My level format defines shapes that have faces, and each face can have a different material.
My naive implementation creates each face as a submesh so it can have different material.

The shadow gaps can be explained by the shadow bias, but what causes the deformation?
Does the deformation have something to do with using custom geometry?

-------------------------

