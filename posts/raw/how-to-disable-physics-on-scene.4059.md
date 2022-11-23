Omid | 2018-02-27 15:21:47 UTC | #1

I looking for a way to disable the physics on scene.
First i try to don't create PhysicsWorld component and nothing change, still all the RigidBody working, then i try to set enable to false for PhysicsWorld and again same. I don't want to disable all rigid bodies one by one because scene have lot of nodes.

-------------------------

cadaver | 2018-02-27 15:22:17 UTC | #2

RigidBody forces the creation of a PhysicsWorld component in the scene, if one doesn't exist.

Maybe PhysicsWorld::SetUpdateEnabled(false)?

-------------------------

Omid | 2018-02-27 13:30:48 UTC | #3

That's worked :+1:
Thanks

-------------------------

