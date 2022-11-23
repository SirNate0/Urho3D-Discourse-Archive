gabdab | 2017-01-02 01:07:48 UTC | #1

[SOLVED]
Loading precomputed navmesh is a lot quicker .
...
It takes more than 30 secs on a 6 core amd processor to compute navmesh on a :
-2000x2000 size plane
-242 faces ..
Is there a way to precompute navmesh and save it in any format ?

-------------------------

cadaver | 2017-01-02 01:07:48 UTC | #2

When the scene or node containing the NavigationMesh is saved / loaded (Save / SaveXML / Load / LoadXML / Instantiate / InstantiateXML) the navigation data is carried along as a binary blob without recomputation.

You can also try calling NavigationMesh's SetNavigationDataAttr() and GetNavigationDataAttr() functions manually to set or retrieve the binary blob.

However just for level design sanity I believe you should tweak your navmesh parameters or break it up to several smaller navmeshes to fix the computation time.

-------------------------

gabdab | 2017-01-02 01:07:49 UTC | #3

[quote="cadaver"]
However just for level design sanity I believe you should tweak your navmesh parameters or break it up to several smaller navmeshes to fix the computation time.[/quote]
Setting up navmesh on a node instead of scene doesn't work apparently(sample 39_CrowdNavigation substituting scene with planeNode) .
Will it work by setting up the scene with more nodes and passing the whole scene to navmesh as for breaking it up to smaller navmeshes ?

-------------------------

cadaver | 2017-01-02 01:07:49 UTC | #4

That could be a bug, will verify. 

If there's a single navmesh component, the amount of nodes that comprise the level geometry don't matter, because all navigable geometry in the hierarchy below the navmesh will be collected into it as triangles, then calculated as one.

-------------------------

gabdab | 2017-01-02 01:07:49 UTC | #5

Navmesh on scene works fine .
I can't grasp how it scales with mesh size (voxels and stuff parameters), is there an idiot's guide reference somewhere ?

-------------------------

cadaver | 2017-01-02 01:07:50 UTC | #6

Verified that you don't have to put navmesh to the scene root. But you must ensure that all navigable geometry, that you want under a certain navmesh, resides in child nodes of the navmesh node, and is marked with the Navigable component, as usual.

-------------------------

gabdab | 2017-01-02 01:07:50 UTC | #7

[SOLVED] DynamicNavigationMesh has to be set on Scene, while Node is set to Navigable (    planeNode->CreateComponent<Navigable>() ) .

-------------------------

