sovereign313 | 2017-01-02 01:09:23 UTC | #1

[ Edit ]
Solved it.  The NODE messages seem to only relate to the 3D physics world.  Using 2D physics, you need to subscribe to E_PHYSICSBEGINCONTACT2D and E_PHYSICSENDCONTACT2D.
[spoiler]SubscribeToEvent(E_PHYSICSBEGINCONTACT2D, URHO3D_HANDLER(Ember, HandleCollision));
SubscribeToEvent(E_PHYSICSENDCONTACT2D, URHO3D_HANDLER(Ember, HandleEndCollision));[/spoiler]

Hi,

I've recently started learning Urho3D, and I am trying to figure out how to make my character trigger a collision event when it collides with the ground.  As of right now, it's not registering.  I've setup the DebugRenderer to show me the boxes for collision detection, and the renderer itself changes the box color around my character upon collision (I'm guessing it changes color to indicate a collision).  Any help would be greatly appreciated.  I've checked out the SnowWarrior and Ragdoll.cpp.  I noticed that Ragdoll.cpp creates a new game component, and encapsulates all of the functionality in that object.  Is this a requirement?  Any help would be greatly appreciated.  Here are the relevant sections of code:

The Ground Rigidbody / Collisionbox
[code]
    groundNode = scene_->CreateChild("Ground");
    groundNode->SetPosition2D(Vector2(0.0f, -5.3f));
    groundNode->SetScale2D(Vector2(100.0f, 0.8f));

    // Create 2D rigid body for gound
    RigidBody2D* groundBody = groundNode->CreateComponent<RigidBody2D>();
    StaticSprite2D* groundSprite = groundNode->CreateComponent<StaticSprite2D>();
    groundSprite->SetSprite(boxSprite);
    groundBody->SetMass(1.0f);

    // Create box collider for ground
    CollisionBox2D* groundShape = groundNode->CreateComponent<CollisionBox2D>();
    groundShape->SetSize(Vector2(0.32f, 0.7f));
    groundShape->SetFriction(0.5f);
[/code]

The Animated Sprite RigidBody/CollisionBox
[code]
    runNode_ = gameNode->CreateChild("SpriterAnimation");
    spriterAnimatedSprite = runNode_->CreateComponent<AnimatedSprite2D>();
    spriterAnimatedSprite->SetAnimationSet(spriterAnimationSetIdle);
    spriterAnimatedSprite->SetAnimation(spriterAnimationSetIdle->GetAnimation(0));
    spriterAnimatedSprite->SetSpeed(4.0f);

    runNode_->SetPosition2D(Vector2(actorposX, actorposY));
    runNode_->SetScale2D(Vector2(0.9f, 0.9f));
    //runNode_->SetDeepEnabled(false);

    actorbody = runNode_->CreateComponent<RigidBody2D>();
    actorbody->SetBodyType(BT_DYNAMIC);
    actorbody->SetMass(1.0f);
    actorbody->SetLinearDamping(2.0f);
    actorbody->SetAngularDamping(2.0f);
    actorbody->SetGravityScale(1.0f);
    actorbody->SetLinearVelocity(Vector2(0.0f, 0.0f));
    actorbody->SetMassCenter(Vector2(0.0f, 0.0f));

    CollisionBox2D *actorshape = runNode_->CreateComponent<CollisionBox2D>();
    actorshape->SetSize(1.3f, 1.9f);
    actorshape->SetDensity(1.0f);
    actorshape->SetFriction(0.5f);
    actorshape->SetRestitution(0.6f);
[/code]

The Subscribing
[code]
void Ember::SubscribeToEvents()
{
    SubscribeToEvent(E_UPDATE, URHO3D_HANDLER(Ember, HandleUpdate));
    SubscribeToEvent(E_POSTRENDERUPDATE, URHO3D_HANDLER(Ember, HandlePostRenderUpdate));
    SubscribeToEvent(runNode_, E_NODECOLLISION, URHO3D_HANDLER(Ember, HandleCollision));
    SubscribeToEvent(groundNode, E_NODECOLLISION, URHO3D_HANDLER(Ember, HandleCollision));

    UnsubscribeFromEvent(E_SCENEUPDATE);  // Disable Pitch / Yaw in 2D
}
[/code]

And the Handler
[code]
void Ember::HandleCollision(StringHash eventType, VariantMap &eventData)
{
    actorbody->SetLinearVelocity(Vector2(0.0f, 0.0f));
    //runNode_->SetDeepEnabled(false);
    std::cout << "in collision" << std::endl;
}
[/code]

-------------------------

