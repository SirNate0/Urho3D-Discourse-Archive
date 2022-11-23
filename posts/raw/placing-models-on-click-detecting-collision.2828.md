smellymumbler | 2017-02-28 23:08:41 UTC | #1

One of the challenges i'm facing when migrating away from Unity is re-implementing this system: https://www.assetstore.unity3d.com/en/#!/content/45147

Basically, it allows me to place models at runtime, based on a grid. I've started a small proof of concept, but i'm having a hard time:

* Snapping models together
* Snapping models to the terrain. This is, by far, the hardest. What's the most effective way of checking how i can place a model on a terrain?

-------------------------

hdunderscore | 2017-03-01 04:04:47 UTC | #2

To specifically get the height on a terrain, you can use the GetHeight() method: 
https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_terrain.html

If you wanted a more generic way to query different geometry snapping locations, you could use OctreeQuery: 
https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_octree_query.html
https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_ray_octree_query.html

Usually these kinds of modular setups require some basic model preparation -- if you set up the origin of the model to be at the bottom and have the model contained entirely in the positive axis, then placing them is a lot more managable.

-------------------------

smellymumbler | 2017-03-01 04:07:21 UTC | #3

Thank you. Also, for snapping on sibiling model edges, any tips? :)

-------------------------

hdunderscore | 2017-03-01 04:20:11 UTC | #4

My first attempt would be to use the bounding box to determine the approximate size of the model and space them based on that. I haven't played with the asset you linked to, so I'm not aware of any advanced behaviours they might have used.

-------------------------

darkirk | 2017-04-29 18:38:14 UTC | #5

Is there any further info on this subject? I'm also struggling to create something like this:

https://www.youtube.com/watch?v=SIU8LxGu-zI

In Urho.

-------------------------

darkirk | 2017-05-19 20:21:14 UTC | #6

Anyone, please? I keep having problems with geo. An example would be great. :(

-------------------------

SirNate0 | 2017-05-21 21:01:35 UTC | #7

My suggestion would be to not do it based in geometry. Use prefabs instead of just models and include snap-points in them - up to you how to do this, but I would suggest either categorical ones - window here, door here, floor/wall/door here, or size based ones. The snap points can just be other nodes in the prefab, and just copy the world position and rotation from them when adding a new node. Another suggestion is looking into how snapping weapons to hands and such is usually done.

Alternatively, it you have only regularly sized components (like Minecraft), you can define a grid system whenever you add a component, unless it meets some criteria to add it to the grid of a previous one.

If you're just looking into how to do it statically (not as part of the game), I would look into how to do it in Blender, etc. and then just import the scene.

-------------------------

smellymumbler | 2017-05-22 20:43:39 UTC | #8

Are prefabs possible in Urho3D? Are they just serialized scenes?

-------------------------

