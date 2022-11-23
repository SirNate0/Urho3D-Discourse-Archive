smellymumbler | 2019-04-02 17:48:47 UTC | #1

I wanted to make sure that I'm not crazy or stupid by doing it this way. I'm building all my levels on Blender and, therefore, generating a box collision mesh or something wouldn't work. So, I'm manually building a collision mesh inside Blender, on top of my level, that my custom exporter separates based on the prefix of the meshes inside Blender. 

Kinda like this: https://www.katsbits.com/smforum/index.php?topic=837.0

But for the whole level. Is that the "right" way to do it?

-------------------------

Modanung | 2019-04-02 20:53:09 UTC | #2

In some cases I too consider this the best approach, but it's usually probably best avoided.

-------------------------

Leith | 2019-04-02 21:41:05 UTC | #3

I recently worked on a commercial 3D networked racing game, which involved tracks with a half-pipe shape. We ended up getting our artists to cut the static world into 16 pieces in a regular grid, and simplifying the collision meshes from those cell geometries based on an angular error term. Cutting up the world allowed both the physics sim and the renderer to cull things - but too many things is also bad.

-------------------------

Modanung | 2019-04-03 22:55:55 UTC | #4

The common solution is to split up your world into reusable parts combined with terrain.

-------------------------

