capelenglish | 2018-07-26 15:31:15 UTC | #1

At a certain point in my game I need to reposition nodes that have rigidbody physics attached to them. When I use SetRotation the physics engine kicks in causes the nodes interact with other components in the scene. I would like to temporarily suspend the physics engine while I reposition the nodes and then turn it back on again. Any suggestions on how to do this?

-------------------------

guk_alex | 2018-07-26 15:53:02 UTC | #2

Very easy. You can disable whole physics world or only certain components.
To disable whole physics world use:

    auto* physicsWorld = node_->GetScene()->GetComponent<PhysicsWorld>();    
    physicsWorld->SetUpdateEnabled(false);

To disable physics of one object use:

    auto* rigidBody = object->GetNode()->GetComponent<RigidBody>();
    rigidBody->SetEnabled(false);

To enable it again set 'true' in these functions.

-------------------------

guk_alex | 2018-07-26 16:10:31 UTC | #3

Also, you can stop the time.

    Scene* scene = node_->GetScene();
    scene->SetTimeScale(0.f);

-------------------------

capelenglish | 2018-07-26 16:51:44 UTC | #4

Thanks, this is just what I was looking for.

-------------------------

Modanung | 2018-07-28 22:18:39 UTC | #5

Instead of `Scene::SetTimeScale(float)` you could also use `Scene::SetUpdateEnabled(bool)`.

-------------------------

