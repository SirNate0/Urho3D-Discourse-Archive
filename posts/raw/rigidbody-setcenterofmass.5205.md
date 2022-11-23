Leith | 2019-05-31 04:15:26 UTC | #1


Urho3D's current implementation of RigidBody has a mechanism to offset the center of mass for models whose origin does not coincide with the center of mass. 
But it is private, and read-only!
There is a GetCenterOfMass method, but no SetCenterOfMass method.
It would be useful for me to be able to set that variable without having to hack the motionstate.

I have a model of a barrel, its origin is in the middle of one of the two endcaps.
When I apply a cylinder shaped rigidbody to it, the center of mass is at the origin of the model, which is completely wrong and leads to unexpected physical behavior. I shouldn't have to edit the model to make the origin coincide with the center of mass!

-------------------------

1vanK | 2019-06-02 09:49:46 UTC | #2

https://pybullet.org/Bullet/phpBB3/viewtopic.php?p=6244&f=9&t=1506

-------------------------

Leith | 2019-06-02 11:42:07 UTC | #3

hai, thanks for useless information - I already know about the motion state offset transform that Urho hides from us.

-------------------------

weitjong | 2019-06-02 13:17:26 UTC | #5

Please be civilized and mind the language.

-------------------------

Leith | 2019-06-03 08:22:32 UTC | #6

My apologies, just frustrated with roadblocks.

It's not well documented, but Urho's RigidBody class derives from btMotionState, and therefore implements that interface. This includes public access to "btTransform m_centerOfMassOffset" class member, so no workaround is needed to directly write to that offset transform.

This was a non-issue, so I've entirely made a fool of myself!
Would it be possible to include a mention in the docs to highlight the fact that Urho's RigidBody effectively "is a" btMotionState - thereby granting full access to the center of mass offset transform?

This is a handy arrangement, though it is not obvious, that RigidBody "is a" btMotionState, which "has a" btRigidBody (which "has a" btMotionState)

-------------------------

