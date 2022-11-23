throwawayerino | 2019-08-13 14:04:17 UTC | #1

When I call `FindPath` it gives me a path that sends my character sinking downwards. The problem isn't with my start/end position since the path sends it sloping downwards then towards the end position. Any help here?

-------------------------

throwawayerino | 2019-08-13 14:17:21 UTC | #2

Right now I'm offsetting each vector in the path by +0.25 to the y axis. It works but I'm curious why the sample doesn't have this problem

-------------------------

Modanung | 2019-08-13 14:37:05 UTC | #3

Could it be you're moving a node towards that point which *is* at a different height?

-------------------------

JTippetts | 2019-08-13 14:42:20 UTC | #4

Recast uses a voxel volume, to which it rasterizes polygons marked as navigable. Depending on the coarseness of your voxel height, and where inside a voxel volume a polygon intersects when it is rasterized, the navmesh can sit above or below the actual geometry by some amount, so it is possible that the polygons of your navmesh lie below the geometry, and your character is sinking because it follows the navmesh topology. I've run afoul of that before. You can do a simple raycast against your real geometry using a navigation point, to get the actual Y of the point to keep the character from clipping. Other than that, I have also placed "dummy" geometry below the actual level geometry to offset the bounding box and alter the way the geometry is rasterized into the volume. You can also use a smaller cell height value to increase the vertical density of voxels, and minimize the magnitude of the error.

-------------------------

