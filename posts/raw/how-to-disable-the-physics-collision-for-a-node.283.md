hualin | 2017-01-02 00:59:22 UTC | #1

Hi,
I disable the RigidBody  by RigidBody::SetEnabled(false), but this way has no effect.

What I want is that the node is enabled and without physic collision in some time or specified area. How can I do?

Thank you.

-------------------------

cadaver | 2017-01-02 00:59:23 UTC | #2

Calling SetEnabled(false) on the RigidBody will remove it from the physics simulation completely, meaning that it also stops moving.

Other things you can do is to remove or disable the CollisionShape component in the same node, in which case the rigidbody still moves, but won't collide. Or you can enable trigger mode on the rigidbody, meaning it will only signal collision events but cause no collision impact forces. Or finally, if you set the rigidbody's collision mask to zero, it shouldn't collide any more.

-------------------------

