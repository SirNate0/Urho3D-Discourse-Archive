PsychoCircuitry | 2022-06-21 02:45:28 UTC | #1

The navigation mesh component appears to be in world space coordinates, regardless of what the local space is of the node that owns it.

Suppose I would want to move my whole scene in space, is there any way to move the navigation mesh without destroying it before the move and rebuilding it after?

That method works, but seems a little costly on performance. If that is the preferred method, any ideas of what I can look at to possibly increase the performance?

Thanks for any insight!

-------------------------

JSandusky | 2022-06-20 23:15:43 UTC | #2

Assuming rigid motion, you could add accounting for the node transform in the NavigationMesh classes. Queries and so on would need to transform from global space to local space and the reverse for information coming out. Debug draw also needs to apply the transform to world space so diagnostics are correctly displayed. Crowds also need to account for it if being used. Internally as far as detour is concerned everything would be the same as always.

That's also assuming you want the navmesh intact as it was when built, if what you want is something like the rolling navmesh of the surface of a Katamari Damacy rolling ball ... then you can only rebuild/partial-rebuild.

If what you have is something like an elevator, mario moving platform, etc then that's the worst case with no really good solution as far as Detour goes (at least off the top of my head I can't think of anything that isn't massive work). In theory you can move dtPolys however you like but the linking of polys and tiles is all very brittle and explicit. Associating a subset of polys to a specific object to transform relative to that is also making my brain hurt, while I can cook up solutions, none of them would be great.

-------------------------

PsychoCircuitry | 2022-06-21 02:44:49 UTC | #3

Thanks a bunch for your insight!

My intended use case is like your initial explanation. Like for a floating origin setup, box world "chunks" that re-center when necessary.

My simple testing arrangement, had about a 100ms frame spike destroying and rebuilding the (not dynamic) navigation mesh, which was not ideal.

I'll look into modifying the navigation system to account for the node's transform.


Edit: thanks again JSandusky for the help. I started digging around the navigation source code per your suggestion and as I was going thru it, I noticed that this world to local, local to world internal conversion was already there... turns out to be my error all along, using node position instead of world position after parenting everything to a "root node" I could move around, instead of directly to the scene.

The navigation meshes seem to follow the node they are attached to just fine. And all works as expected as long as I feed it world position values and not local values. Figures! But I'd have probably been at this all night without your help. So thanks again!

-------------------------

JSandusky | 2022-06-21 21:25:22 UTC | #4

Interesting, I wonder who did that as I have no memory of writing it so I assumed it wasn't in there (then it'll be git history will say "*yes, yes you did, you just forgot dum dum*"). Glad you figured it out.

-------------------------

