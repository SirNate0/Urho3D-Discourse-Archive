Spongeloaf | 2019-08-17 20:02:42 UTC | #1

I've repurposed a bunch of sample code for a simple 2D game project. I need to be able to see the physics collision box of my objects for debugging purposes. However, I've copied all of the debug drawing code as best I can find from the samples into my own project and it doesn't work. The sprite is drawn, as expected, but nothing else.

In CreateScene() I do the following:

        // Create 2D physics world component and debug renderer
	PhysicsWorld2D* physicsWorld = scene_->CreateComponent<PhysicsWorld2D>();
	debug = scene_->CreateComponent<DebugRenderer>();
	physicsWorld->SetDrawAabb(true);
	physicsWorld->SetDrawCenterOfMass(true);
	physicsWorld->SetDrawJoint(true);
	physicsWorld->SetDrawPair(true);
	physicsWorld->SetDrawShape(true);

And then I have an  event handler for E_POSTRENDERUPDATE that calls a draw debug function:

        // Draw 2D physics debug geometry
	PhysicsWorld2D* physicsWorld = scene_->CreateComponent<PhysicsWorld2D>();
	physicsWorld->DrawDebugGeometry(debug, true);

Now if I understand correctly, it should draw any CollisionEdge2D, CollisionCircle2D, CollisionBox2D, etc. according to this [document](https://urho3d.github.io/documentation/1.5/_urho2_d.html). 

I have only one physics object, and it looks like this:

        // create sun
	Node* sun_node = scene_->CreateChild("sun");
	sun_node->SetPosition(Vector3(0.0f, 0.0f, 0.0f));
	sun_node->SetScale(Vector3(1.0f, 1.0f, 0.0f));

	CollisionCircle2D* sun_collider = sun_node->CreateComponent<CollisionCircle2D>();
	StaticSprite2D* sun_sprite_ptr = sun_node->CreateComponent<StaticSprite2D>();
	RigidBody2D* sun_body = sun_node->CreateComponent<RigidBody2D>();

	sun_sprite_ptr->SetSprite(sun_sprite);
	sun_collider->SetRadius(0.32f);
	sun_collider->SetDensity(1.0f);
	sun_collider->SetFriction(0.5f);
	sun_collider->SetRestitution(0.1f);
	sun_body->SetGravityScale(0.0);
	sun_body->SetBodyType(BT_DYNAMIC);

Have I setup my debug rendering wrong? Or has the collision box been made incorrectly? I did try making some other shapes, but I can't see them either. For the record, the sample I took this from - 32_Urho2DConstraints - compiles, runs, and debugs just fine. 

Can anyone help?

-------------------------

Modanung | 2019-08-16 01:36:36 UTC | #2

Welcome to the forums! :confetti_ball: :slightly_smiling_face:

Did you _subscribe_ to the post-render update event with `SubscribeToEvent(...)`?

-------------------------

Spongeloaf | 2019-08-16 01:53:51 UTC | #3

Yup. 

    SubscribeToEvent(E_POSTRENDERUPDATE, URHO3D_HANDLER(KickGame, DrawDebug));

This is called right after the scene is created and the viewport is setup in 'virtual void KickGame::Start()'

Here is [a link](https://github.com/Spongeloaf/kick_asteroids/blob/master/src/kick_main.cpp) to the file on github, if anyone wants to see everything.

-------------------------

Modanung | 2019-08-16 13:00:03 UTC | #4

Just wondering; why no separate header file? It'll often save on compilation time.

-------------------------

Modanung | 2019-08-16 13:01:43 UTC | #5

To make sure your virtual functions are actually overridden you could use `override` _instead_ of `virtual`.

-------------------------

Modanung | 2019-08-16 16:05:20 UTC | #6

...but I think _this_ might be the problem:
```
// Draw 2D physics debug_ geometry
PhysicsWorld2D* physicsWorld = scene_->CreateComponent<PhysicsWorld2D>();
physicsWorld->DrawDebugGeometry(debug_, true);
```
`Create` should be `Get`.

-------------------------

Spongeloaf | 2019-08-16 16:05:18 UTC | #7

You were right it should have been GetComponent. I'd been staring at it for so long, but somehow didn't notice that. 

Thanks!

As for the header file, I'm going to break things apart into other files and classes once I have a better understanding of how to use the engine and what my project structure will look like. Right now I'm just trying to understand how the key components work.

-------------------------

Modanung | 2019-08-16 21:13:24 UTC | #8

[quote="Spongeloaf, post:7, topic:5476"]
I’d been staring at it for so long, but somehow didn’t notice that.
[/quote]

When you look long enough you'll start to think you've seen it all. ;)
Glad I could help.

-------------------------

