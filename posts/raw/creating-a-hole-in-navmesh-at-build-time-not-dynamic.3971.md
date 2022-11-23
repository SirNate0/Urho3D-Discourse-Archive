Alan | 2018-01-30 23:59:29 UTC | #1

Hello there.

I'm looking for a way to create a 'hole' in the generated navmesh, say for example I have some boulders on the terrain and want them to inhibit navmesh generation but I also don't want navmesh to generate on top of them. I know about Obstacle, but afaik that is intended for dynamic carving and it's not an arbitrary shape, it's an axis-aligned capsule.

-------------------------

Sinoid | 2018-01-31 00:32:58 UTC | #2

A NavArea with 0 or >63 for the area-id should mark out a hole. Only world-aligned box shapes are presently supported. You could implement convex poly support if needed by following what NavArea does, `rcMarkConvexPolyArea` instead of `rcMarkBoxArea`.

A 0 id is the null marker in Recast and any value greater than 63 is outside the legal walkable area range.

-------------------------

Alan | 2018-01-31 00:47:39 UTC | #3

Thanks @Sinoid, so that's currently not possible? I mean, in that use case boxes aren't very appropriate. I think it would be better to simple place a wall around the boulders for the navmesh generation, it won't be ideal because the insides would still be navigable but it's certainly better than an axis-aligned rectangle. Perhaps it's possible to 'remove' the inner navmesh island posteriorly? Maybe even from the navmesh data directly?

-------------------------

Sinoid | 2018-01-31 00:59:03 UTC | #4

Refer to recast for that. Messing with the navmesh itself would be a bad idea. 

https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Navigation/NavigationMesh.cpp#L384

Instead, you can filter out triangles before they reach recast, before rcRasterizeTriangles, or editing the cells of the compact heightfield. 

If you have static maps you could use a bitmap to wipe out whole columns of the compact heightfields. That'd be relatively little work.

-------------------------

George1 | 2018-01-31 03:05:48 UTC | #5

When I was using Irrlicht.
What I did was merging mesh buffers together and pass it through recast to generate the navmesh.

What you could do is mark navigatabe ID for meshes (Terrain, tunnel, dungeon, hole etc.). Then on loading use CSQ library to merge the mesh buffers together and then pass it through the recast to obtain new navmesh.

If the world is too large you need to use tilecache with some help from lod technique.

Best regards

-------------------------

Lumak | 2018-02-01 22:21:12 UTC | #6

@Alan, I use convex prune object to specify tiles as untraversable (or holes) using bit mask when building it then save my navmesh to a file to avoid constructing it at runtime, as shown here: https://discourse.urho3d.io/t/navigationmesh-convexpruneobject/3613

-------------------------

Alan | 2018-02-01 22:21:36 UTC | #7

Thanks Lumak! That seems to be the best approach.

-------------------------

Lumak | 2018-02-01 23:42:04 UTC | #8

It might be easier to create a simple tile editor using a raycast and placing a sphere to gather tiles to mark them to whatever bit flag, instead of convex prune object.  Didn't you write the terrain editor for Atomic? Maybe it was Darrlyn, anyway, it'll be easier than writing that.

-------------------------

