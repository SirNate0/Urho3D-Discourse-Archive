nergal | 2017-11-04 10:36:16 UTC | #1

How can I optimise physics so that it might be a little more blunt but more performant? 

I'm creating a voxel-engine and exploding parts are small physics blocks. But on my macbook pro (2x3.2GHz, 16GB RAM) I can only create like 800 blocks before the frame-rate drops heavily.

This is how I do it...

I'm creating a pool of blocks like this:

    node = context->GetSubsystem<Game>()->scene_->CreateChild("Box");
    node->SetPosition(Vector3((float)(rand()%1000+1000), (float)(rand()%1000)+1000, (float)(rand()%1000+1000)));
    node->SetScale(1.0f);
    model = node->CreateComponent<StaticModel>();
    model->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
    model->SetMaterial(cache->GetResource<Material>("Materials/vcolors2.xml"));
    model->SetCastShadows(true);

    shape = node->CreateComponent<CollisionShape>();
    shape->SetBox(Vector3::ONE);

    body = node->CreateComponent<RigidBody>();
    body->SetCollisionEventMode(COLLISION_NEVER);
    body->SetMass(10.1f);
    body->SetFriction(30.0f);
    body->SetRollingFriction(20.0f);
    model->SetEnabled(false);
    free = true;

Then I initiate a new block from the pool like this:
   
        node->SetPosition(pos);
        SharedPtr<Material> m = model->GetMaterial()->Clone();
        m->SetShaderParameter("MatDiffColor",Vector4(color.x_/255.0f, color.y_/255.0f, color.z_/255.0f, 0.2f));
        model->SetMaterial(m);
        body->SetLinearVelocity(velocity*(float)OBJECT_VELOCITY);
        model->SetEnabled(true);
        free = false;

Any suggestions how to increase performance so that I might add more than just 800 blocks (in this case).

Thanks in advance!

-------------------------

Bananaft | 2017-11-05 10:33:52 UTC | #2

If you want this blocks all fly around simultaneously, collide with static geometry and each other. 800 seems like a reasonable ceiling.

Now things you can try:

1) Using collision layers you can set up it so they will collide with static geometry and not eachother.

2) Use sphere collison shape. It could be faster.

3) Make it so only small ammount of all dynamic objects in the scene are active, and the rest are sleeping. I belive you can tweak sleeping parameters in bullet physics, making them more greedy.

-------------------------

nergal | 2017-11-05 21:31:38 UTC | #3

Thanks for your suggestions, I will try them out :)

-------------------------

Eugene | 2017-11-05 22:31:12 UTC | #4

Physics performance highly depends on number of simultaneoutly collided objects.
So, you keep thousands of objects somewhere, but if you make even ~1k objects activated at the moment, you will lag. Sample 12 called "PhysicsStress" for a reason.

-------------------------

nergal | 2017-11-06 07:11:27 UTC | #5

@Eugene yepp, I get that, but I just wanted to make sure that I didn't do something wrong that made my phys object limit low. And also to get some tips&trix to optimise :) I think layered approach would be good in my case.

-------------------------

