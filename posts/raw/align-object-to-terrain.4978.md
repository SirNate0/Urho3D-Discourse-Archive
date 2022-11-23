QBkGames | 2019-03-05 07:34:53 UTC | #1

I'm trying to align a static object that has a random rotation and scale to the terrain at a random location. Is there a way to get the AABB of a game object, that has a static mesh and collision shape/rigid body? I'm pretty sure both the Octree and Bullet calculate it (somewhere, somehow), so does anyone know how to get the world transform based AABB from either the Octree or physics (preferably physics)?

-------------------------

Leith | 2019-02-28 03:16:47 UTC | #2

Bullet CollisionShape class has getAABB() method that you can call at runtime, it is (I believe) dynamic, ie its the oriented aabb, likely what you wanted... not sure if Urho's CollisionShape wrapper class has this, but it does have CollisionShape::GetCollisionShape() which returns the underlying bullet CollisionShape object.
But for object placement on a terrain, I generally like to create my objects somewhere high up in Y, cast a sphere down to the terrain, and set the Y position to the origin of the sphere with respect to the collision result (contact point).

-------------------------

I3DB | 2019-02-28 17:23:29 UTC | #3

[quote="QBkGames, post:1, topic:4978"]
I’m trying to align a static object that has a random rotation and scale to the terrain at a random location.
[/quote]

In [the water feature sample](https://github.com/urho3d/Urho3D/blob/9e48a8e02d4c68852dca7f09c76b67b782504043/Source/Samples/23_Water/Water.cpp#L131) blocks are placed at random locations over the terrain and aligned normally and height-wise with the terrain. [Those functions are here.](https://github.com/urho3d/Urho3D/blob/9e48a8e02d4c68852dca7f09c76b67b782504043/Source/Urho3D/Graphics/Terrain.cpp#L555)

[This shows that sample running](https://urho3d.github.io/samples/Urho3DPlayer.html?Scripts/23_Water.as), and you can see how the blocks are aligned, if that is what you're looking for.

-------------------------

QBkGames | 2019-03-01 09:10:43 UTC | #4

Thanks guys for the reply.

The problem is that if you have a rectangular box (not cubic), which could be rotated around any axis (say 90 deg for simplicity sake) and also scaled, then neither casting a sphere nor the simple functions in the Water sample would work. You can align to the terrain slope but how high should the box be positioned so that it neither sink in the ground nor levitate above the ground? You really need the AABB with all the node transformed applied to it. I could calculate it out myself, but the engine should already calculate it (possibly in 2 separate places), so it seems reasonable that you should be able to just get it and not calculate it a third time.

I'll check out the getAABB()  of the Bullet CollisionShape to see if it helps.

-------------------------

Leith | 2019-03-02 05:32:20 UTC | #5

It doesn't need to be a sphere - spheres are more accurate than raycasts on uneven terrain, but bullet has a ConvexCast method to cast any (convex) shape in some direction. Not sure that Urho has support for it, but you can get to the underlying bullet objects, so you can definitely do it yourself (just not in script, only in c++). Also, rotating a cube by 90 degrees was a pretty poor example lol.![Screenshot%20from%202019-03-02%2013-16-41|690x403](upload://ofxcZGBGPpmBkmfOtpov19ACJ6X.jpeg) 
im not far out but im not getting love and support.

-------------------------

QBkGames | 2019-03-05 04:29:10 UTC | #6

Looks like I end up answering my own question. The Drawable has a function GetWorldBoundingBox() which gets me what I want (though now I'm not sure if this is what I really need :stuck_out_tongue:).

-------------------------

