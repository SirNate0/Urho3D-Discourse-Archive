carl | 2017-01-02 00:59:31 UTC | #1

Hi, I'm trying to get the point on a certain model where I click with the cursor. I've managed to get it working, except when there's another model in between.
I want the point in the model A, but there's a model B in the way. The raycast should ignore B and keep going until it hits A.
I'm using the viewMask for that.

octree:RaycastSingle(cameraRay, RAY_TRIANGLE, M_INFINITY, DRAWABLE_GEOMETRY, 0x80000000)

Only A has a viewMask = 0x80000000. But still, it gets the point on B. 

Am I doing something wrong? Should it work?


Alternatively, I could use the other RayQueryResult[]@ Raycast(..) and compare the node's name to find the one I want. However I don't know how to iterate on that array in lua, it says bad argument #1 to 'ipairs' (table expected, got userdata)

-------------------------

cadaver | 2017-01-02 00:59:31 UTC | #2

The viewmasks use an AND operation, and pass if the result is nonzero. The default viewmask of all drawable components is 0xffffffff, so if you want to use the highest bit to discriminate (mask 0x80000000 in query) you'll need to set the mask on object B to not have the highest bit set, eg. 0x7fffffff.

-------------------------

carl | 2017-01-02 00:59:31 UTC | #3

Then I'm pretty sure it's not working properly. Whatever I put in the viewMask for the RaycastSingle doesn't do anything. I even put 0 and still it hits everything.

-------------------------

cadaver | 2017-01-02 00:59:31 UTC | #4

In this case it seems to be a Lua bindings bug, where the query viewmask is being ignored. In AngelScript (or C++) passing a 0 gives no objects, as expected.

-------------------------

carl | 2017-01-02 00:59:31 UTC | #5

I was looking at the wrong API, from AngelScript. It seems that the Lua binding doesn't have viewMask in the Raycast

RayQueryResult RaycastSingle(const Ray& ray, RayQueryLevel level, float maxDistance, char drawableFlags) const

Which is still odd...

-------------------------

cadaver | 2017-01-02 00:59:31 UTC | #6

The viewMask parameter has been added to the master branch.

-------------------------

carl | 2017-01-02 00:59:31 UTC | #7

That's fast, thank you! Now it works perfectly.

-------------------------

jorbuedo | 2017-01-02 00:59:32 UTC | #8

I'm working with Terrains and it looks like Raycasts don't hit them. Other drawables like static models are hit, but terrain heightmaps aren't.
I'm using the navigable example with the terrain from the vehicle example. I removed the navigable mesh and just teleport Jack to anywhere I click. I can move him to the boxes, mushrooms or even to himself. Everything but the ground.

Is that normal behaviour?

-------------------------

cadaver | 2017-01-02 00:59:32 UTC | #9

When position & normal were added to RayQueryResult, TerrainPatch raycast code was not updated. So it would return hits with correct distance, but with incorrect position. This is now fixed in the master branch.

-------------------------

gabdab | 2017-01-02 01:07:48 UTC | #10

[SOLVED] My bad , physics world was retrieved from a non existent node, so empty.
Does it currently work in c++ ?
I am unable to get ray collisions with rigid bodies ,but I have collisions response with them  .
Strangely enough SphereCast works against the floor rigid body , but not when I perform it  against another rigid body  (layer and mask matching).
:
[code]
Quaternion dir(node_model->GetRotation().YawAngle(), Vector3::UP);
Vector3 laserStartPos = node_model->GetPosition();
Vector3 laserTargetPos = node_model->GetPosition()+ dir * Vector3(0.0f, 0.0f, 3000);
PhysicsRaycastResult result1;
Ray ray1(laserStartPos,laserTargetPos - laserStartPos);
float l=(laserTargetPos - laserStartPos).Length();
globals::instance()->physical_world->RaycastSingle(result1, ray1, l, 2);
 if (result1.body_){
        laserTargetPos = laserStartPos + ray1.direction_ * (result1.distance_ - 0.5f);

 }
//  if (result1.body_)
         std::cout<<result1.body_<<std::endl;[/code]

-------------------------

josuemnb | 2019-08-23 10:06:12 UTC | #11

Good day.
For a couple of days that i've been working on raycast bug.
Now i can present my conclusion.
Was very weird at the beginning when started to test urhosharp, and raycast was perfect.
but now testing raycast with nodes at higher distances like 5000 from scene root node, can't detect it. 
if i decrease it to 1000, it's working better.

what could be the problem?

-------------------------

Modanung | 2019-08-26 20:27:28 UTC | #12

7 posts were split to a new topic: [About UrhoSharp and possible alternatives](/t/about-urhosharp-and-possible-alternatives/5512)

-------------------------

lezak | 2019-08-26 19:42:34 UTC | #19

Back to the topic - it may not be a bug and it may indeed be Urho3d thing (not only c# version). Are You using Octree::Raycast? If yes, have You tried increasing octree size (default size is 1000)?

-------------------------

