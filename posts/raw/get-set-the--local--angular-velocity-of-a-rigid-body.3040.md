rico.decho | 2017-04-24 12:59:02 UTC | #1

I need to do change the _local_ yaw/pitch/roll rotation speeds of a bullet rigid body, in _radians per second_, independently of its mass.

How can I convert the global angular velocity of a rigid body to its local angular velocity, and vice versa ?

-------------------------

TheComet | 2017-04-24 12:03:18 UTC | #2

You should be able to just multiply it with the node's transformation matrix.

    Vector3 localAngularVelocity = node->GetWorldTransform().Inverse() * globalAngularVelocity;
    Vector3 globalAngularVelocity = node->GetWorldTransform() * localAngularVelocity;

Turns out Node already has methods for this:

    Vector3 localAngularVelocity = node->WorldToLocal(globalAngularVelocity);
    Vector3 globalAngularVelocity = node->LocalToWorld(localAngularVelocity);

-------------------------

rico.decho | 2017-04-24 13:08:47 UTC | #3

Thank you so much ! You made my day !!!

-------------------------

