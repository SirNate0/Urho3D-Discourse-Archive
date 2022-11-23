Enhex | 2017-01-02 01:06:28 UTC | #1

I tried to use scene.physicsWorld.RaycastSingle() in a script, and when using M_INFINITY it doesn't collide with anything.
Is it a bug?

-------------------------

cadaver | 2017-01-02 01:06:30 UTC | #2

Physics raycasts go to the Bullet library, and Bullet expects a start point and end point in space, so when you specify infinity it can't calculate an end point that makes sense. Could add a warning for that case.

-------------------------

Enhex | 2017-01-02 01:06:36 UTC | #3

By the way, M_INFINITY is the default argument, and it shouldn't be if it doesn't work.
So there shouldn't be a default argument for the physics raycasts.

-------------------------

cadaver | 2017-01-02 01:06:37 UTC | #4

Yes, there seems to be an error in the script API. In the C++ header there is no default value.

-------------------------

