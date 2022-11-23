Enhex | 2017-01-02 01:06:41 UTC | #1

If I have characters in different sizes, how would I be able to set a different height and radius for each one?
I only worked with NavigationMesh so far and it seems to require a rebuild after changing height/radius.
I fiddled with the crowd nav sample and the CrowdAgent height & radius only affect avoiding other CrowdAgents.

Can DynamicNavigationMesh handle height/radius change without rebuilding?
FindPath() doesn't seem to work with DynamicNavigationMesh.

-------------------------

JTippetts | 2017-01-02 01:06:41 UTC | #2

The height and radius are "baked in" to the nav mesh. So in order to support multiple heights and radii, you have to have multiple nav meshes, each baked to a given configuration. The reason for this is that collision geometry is voxelized, movable areas are "peeled" off and eroded based on the radius and agent height, so that the final nav mesh automatically takes into account the agent size. If you pick any random point on a nav mesh, an agent of size "radius/height" can stand there without colliding any collision geometry. But agents of a different size can't necessarily stand there without colliding, because the mesh wasn't eroded relative to their size. It's a drawback of this kind of pathfinding, sadly.

-------------------------

Enhex | 2017-01-02 01:06:44 UTC | #3

So several navMesh components can be attached to the scene, for each character type? Sounds like it could work.

-------------------------

