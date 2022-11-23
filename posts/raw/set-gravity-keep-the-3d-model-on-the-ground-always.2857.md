tybandara | 2017-03-06 19:09:34 UTC | #1

Hello experts,

We have a 3d model working with Urho3D and it's a human model that will dynamically follow a real human. i.e. it dynamically moves for the real movements of a human. 
We have noticed that when the both legs of the 3d model are lifted, the model goes above the earth surface level. Our intended behavious is for the model to always touch the earth surface no matter what the body movement is. 
Is there a simple way to implement this feature, like setting real gravity details? 

Thanks
Thilina

-------------------------

jmiller | 2017-03-06 22:25:46 UTC | #2

Hello Thilina :)

Perhaps these could be useful?
[url=https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_rigid_body-members.html]RigidBody[/url]::SetGravityOverride(const Vector3 &gravity) or SetUseGravity(false)
PhysicsWorld::SetGravity(const Vector3 &gravity)
  https://urho3d.github.io/documentation/HEAD/_physics.html

It is also possible, for example, to force the RigidBody to a Y coordinate in E_PHYSICSPRESTEP or E_PHYSICSPOSTSTEP event (I believe 18_CharacterDemo sets Pitch and Yaw similarly).

-------------------------

tybandara | 2017-03-08 10:58:40 UTC | #3

Hello carnalis,

We did try your advice. Now the 3D model keeps on moving towards gravitational force as expected. Now we want a method to stop it when it hit the floor.

> RigidBody body = node.CreateComponent<RigidBody>();
> body.UseGravity = true;
> body.Mass = 1.0f;

Now, we have a static floor model loaded. We want to stop the human model at the floor. At the moment, the human model goes below the floor even. 

Can you shed some light on this please?

-------------------------

slapin | 2017-03-08 11:43:04 UTC | #4

Are you against using another RigidBody for your floor?

-------------------------

slapin | 2017-03-08 11:46:52 UTC | #5

Also, set mass of new one to 0 - that will make it static.
If you insist on not using collisions you might be interested in kinematic = true, but in this case you will need
to simulate gravity yourself and control height manually, which is tedious IMHO, but there are many people here who wish to do everything manually scripted using shaders.

-------------------------

jmiller | 2017-03-08 17:58:26 UTC | #6

It is possible to expand or contract the margin a CollisionShape, which can help visually.
  collisionShape.margin_ = 0.1f

* also, to help the shape match the model, there is
  collisionShape.position_

-------------------------

