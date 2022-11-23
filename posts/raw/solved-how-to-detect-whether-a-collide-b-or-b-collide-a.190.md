hualin | 2017-01-02 00:58:45 UTC | #1

Hi,
I am using E_PHYSICSCOLLISIONSTART for a physic listener in class derived from Application, and now no matter whether node A collide node B or B collide A, the eventData is the same, the NodeA is A and NodeB is B, this confusing me.
Is there any way to distinguish which node collide with the other?
Thank you!

Edit:
Because my goal is detect whether back car collide with front car, the solution that the function RaycastSingle or Raycast is a perfect way to solve the problem.
Thank you all very much!

-------------------------

weitjong | 2017-01-02 00:58:46 UTC | #2

If you look at the code which sending this event, you will find a logic that sort the bodyA and bodyB, which in turns should make nodeA and nodeB always appear in the event data in a similar order when the pair collides with each other.
[github.com/urho3d/Urho3D/blob/m ... #L650-L654](https://github.com/urho3d/Urho3D/blob/master/Source/Engine/Physics/PhysicsWorld.cpp#L650-L654)

-------------------------

hualin | 2017-01-02 00:58:46 UTC | #3

Thank you for your reply, weitjong.
But I can't catch you.
My game has two car, the node A and node B, I can't distinguish which one collide with the other. The event data is the same, no matter A collide B or B collide A.
My meaning is that, if A collide B, then the event data will contains NodeA is A, and NodeB is B, and if B collide A, the event data would contains NodeA is B, and NodeB is A. Or is there any way to distinguish the two nodes?

-------------------------

cadaver | 2017-01-02 00:58:46 UTC | #4

From the point of the physics simulation (Bullet library) collision is interaction of two objects, so the question whether A collides with B or B collides with A is not relevant, or actually, both happen.

Collisions are hard to handle from that global collision event, as it's fired for every colliding pair of objects. It's possible that the "node A" or "node B" might swap between simulation steps (especially if the collision is broken off and then starts again) so you can't rely on which is which.

Typically a game might be running a car logic script or component in the same node as the car rigidbody/collisionshape, and each such car logic object would listen to its own node's collision events only: the NodeCollision category of events. Those events are easier to use as they have an "other node" parameter. Like this:

[code]
SubscribeToEvent(GetNode(), E_NODECOLLISIONSTART, HANDLER(MyLogicObject, HandleNodeCollisionStart));

void MyLogicObject::HandleNodeCollisionStart(StringHash eventType, VariantMap& eventData)
{
    using namespace NodeCollisionStart;
    Node* collidedWith = eventData[P_OTHERNODE].GetPtr();
    ...
}
[/code]

-------------------------

hualin | 2017-01-02 00:58:46 UTC | #5

Thank you, cadaver.

I digg into the source code of PhysicsWorld, the event E_NODECOLLISIONSTART is triggered  same as  E_PHYSICSCOLLISIONSTART, in other words, the nodeA and nodeB would receive the event NODECOLLISIONSTART too and in nodeA, the other body is B, and in nodeB, the other body is A, so I can't distinguish which is which. 

What I need is to know whether A is active to collide with B , or B is active. Because if A collide with B, the B will get speed UP, and A get speed DOWN. Conversely, the B will get speed DOWN and the A get speed UP.

Is there any way to do this?

-------------------------

cadaver | 2017-01-02 00:58:46 UTC | #6

Collision events include the world position & normal vector of the contact points, and the force those contact points exert, so try if you can work it out from those. Otherwise there's no other information that physics collisions carry. Reading the contact points is slightly convoluted, as they're in a byte array which you must interpret; for an example you can take a look at Character::HandleNodeCollision() function in Source/Samples/18_CharacterDemo/Character.cpp.

-------------------------

