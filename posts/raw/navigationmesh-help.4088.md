davidpox | 2018-03-15 00:31:08 UTC | #1

Hi all, 

I'm a bit new to Navigation meshes and was wondering if anyone could help me get my head around something - I've made a few objects in Urho3D and would like the crowd agents to walk along them, however it appears my meshes are too small and no navigation mesh is being build for them. 

E.g. here: 
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/f/f21f8a7f01b5a5739787acd09bc2413f625b3a3f.png'> 


Does anyone know what settings I would have to change so they can both go inside the building and go along the upper path?

-------------------------

Sinoid | 2018-03-19 17:47:58 UTC | #2

With the navigation mesh (or dynamic navigation mesh) selected, pay attention to your skinny-path and adjust `Agent Radius` and/or `Cell Size` to be smaller. Prefer `Agent Radius` to `Cell Size` first, as `Cell Size` adjusts the voxel density which can make nav-mesh generation really slow if you go too small.

Check your building interior to see if it changing those sizes took care of that too, if not then adjust `Agent Height`.

-------------------------

davidpox | 2018-03-19 00:03:23 UTC | #3

@Sinoid 
OK thanks, May I just ask what the difference is between a standard Navigation Mesh and a Dynamic one? Does the Dynamic one allow to be updated?

-------------------------

Sinoid | 2018-03-19 01:55:51 UTC | #4

They're pretty similar. The DynamicNavigationMesh just stores a cache so it can rebuild tiles of the navigation mesh much more quickly. That allows `Obstacle` components that can be added/removed to insert cylindrical obstacles without requiring traversing all of the `Navigable` components for meshes in the scene to do a regular navigation mesh rebuild.

Full rebuilds take a smidget longer and the total memory use of a DynamicNavigationMesh is basically twice that of a regular NavigationMesh. In most cases DynamicNavigationMesh is a safe goto.

-------------------------

davidpox | 2018-03-19 02:22:16 UTC | #5

@Sinoid 
Okay thanks again!! One final question (for now, I hope); 

What is the best way to properly create obstacles/ barricades?
Suppose I have a large ocean in my map, that I don't want Agents to walk on - should I really use multiple of the Obstacles objects to create a barricade around it? Or is there more of an elegant solution? Also curious from a programming stand point why the Obstacles are  septagons, instead of something like a simple cube

-------------------------

Sinoid | 2018-03-19 02:45:37 UTC | #6

> Suppose I have a large ocean in my map, that I don’t want Agents to walk on - should I really use multiple of the Obstacles objects to create a barricade around it? Or is there more of an elegant solution?

Use a big `NavigationArea` (which is just a box) and set it's Area ID to be > 64, that will mark it as an unwalkable area.

> Also curious from a programming stand point why the Obstacles are septagons, instead of something like a simple cube

They're analytic cylinders, the actual shape in the navmesh will vary between a square, pentagon, hexagon, septagon, octagon, etc based on navmesh voxel resolution.

It's basically because of RVO (used by Crowd Navigation), authorial ease (sphere's suck), Nyquist frequency, execution simplicity of having all obstacles use the same shape type, and probably other things I don't know about. You'd have to ask Mikko himself (the author of Recast/Detour) for a more in-depth answer.

When I wrote the debug drawing for crowd agents and obstacles I just went with octagon's for no specific reason. Just a convenient low vertex count shape that got the idea across.

-------------------------

davidpox | 2018-03-19 13:42:52 UTC | #7

Thanks for your answer! Pretty interesting. 

I tried adding the large NavMesh area to places I dont want walkable, however they still walk through it without hesitation. Area ID is 128
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/d/dccc6fb6efdce790cbb7ef82f6d6bfaff8efb2bc.png[/img]

-------------------------

Sinoid | 2018-03-19 17:32:15 UTC | #8

You're right, only Area ID of 0 will remove.

-------------------------

