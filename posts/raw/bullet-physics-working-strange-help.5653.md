Elendil | 2019-10-07 14:33:33 UTC | #1

I created box and move it with physics. Problem is, when physic object is moving, the box (drawable) have "lags". If physics is under debug mode, collision box moving perfectly smooth, but box as drawable object is not smooth.

here is video how it looks like
https://youtu.be/aFkeZUhDWpA

I dont know where can be problem.
Here is code which can be related. Btw I fogrot create PhysicsWorld component (and it works), but after create it, it didnt help.

    void MyGApp::Start()
    {
    	scene_ = new Scene(context_);
    	scene_->CreateComponent<Octree>(); 
    	scene_->CreateComponent<DebugRenderer>();
    	PhysicsWorld * pw = scene_->CreateComponent<PhysicsWorld>();

    	// ...
    }

---

    void Urho3D::PlayerShip::mf_Start(Scene * scene)
    {
    	// ...

    	m_node = scene->CreateChild("Spaceship");
    	m_node->SetPosition(Vector3(0, -2.0, -10.0f));
    	//m_node->SetRotation(Quaternion(0, 0, 0));
    	m_node->SetScale(Vector3(1.0f, 1.0f, 1.0f));
    	
    	// Static model
    	m_node_spaceship = m_node->CreateChild("Spaceship_model");
    	m_spaceship = m_node_spaceship->CreateComponent<StaticModel>();
    	m_spaceship->SetModel(cache->GetResource<Model>("Models/Box.mdl")); // Spaceship1
    	m_spaceship->SetMaterial(cache->GetResource<Material>("Materials/Stone.xml"));
    	m_spaceship->SetCastShadows(true);

    	// Physics
    	m_spaceship_rb = m_node_spaceship->CreateComponent<RigidBody>();
    	m_spaceship_rb->SetMass(5.0f);
    	m_spaceship_rb->SetFriction(0.5f);
    	m_spaceship_rb->SetUseGravity(false);
    	m_spaceship_rb->SetCollisionEventMode(COLLISION_ALWAYS);
    	m_spaceship_rb->SetCcdRadius(0.1f);
    	m_spaceship_rb->SetCcdMotionThreshold(0.1f);


    	CollisionShape * collision_shape = m_node_spaceship->CreateComponent<CollisionShape>();
    	collision_shape->SetBox(Vector3(1.0f , 1.0f, 1.0f));
    	// ---------------------------------------------------------------------------
    	// ...
    }
---
    void Urho3D::PlayerShip::mf_Update(StringHash eventType, VariantMap & eventData)
    {
    	float timeStep = eventData[Update::P_TIMESTEP].GetFloat();
    	m_node_camera->LookAt(m_spaceship_rb->GetPosition());
    	if (m_under_control)
    	{
    		MoveDirection = Vector3::ZERO;
    		float MS = m_speed; // m_speed = 2.0f;

    		if (input->GetKeyDown(KEY_SHIFT))
    		{
    			MS *= 10;
    		}
    		if (input->GetKeyDown(KEY_UP))
    		{
    			MoveDirection += (Vector3(0, 0, 1.0f) * MS);
    		}
    		if (input->GetKeyDown(KEY_DOWN))
    		{
    			MoveDirection += (Vector3(0, 0, -1.0f) * MS);
    		}

    		if (input->GetKeyDown(KEY_LEFT))
    		{
    			MoveDirection += (Vector3(-1.0f, 0, 0) * MS);
    		}

    		if (input->GetKeyDown(KEY_RIGHT))
    		{
    			MoveDirection += (Vector3(1.0f, 0, 0) * MS);
    		}


    	}

    	const Quaternion& rot = m_node_spaceship->GetRotation();
    	m_spaceship_rb->ApplyImpulse(MoveDirection);

    	m_node_spaceship->SetRotation(m_node->GetRotation());
    	const Vector3& velocity = m_spaceship_rb->GetLinearVelocity();
    	Vector3 brakeForce = (-velocity * 0.2f);
    	m_spaceship_rb->ApplyImpulse(brakeForce);
    }

-------------------------

Elendil | 2019-10-07 17:30:43 UTC | #2

I partially solve it, but this is not solution.
I created model in separate node and update SetTransform from RigidBody. It is moving smooth then. 

Problem looks like node position to physic RigidBody position is strangely calculated. Like when it want to be in exact position as RigidBody and another time want to be late and it is switching between two states.

-------------------------

Modanung | 2019-10-08 00:27:00 UTC | #3

Forces should be applied during `FixedUpdate` to prevent what you call lags.

-------------------------

Elendil | 2019-10-08 09:44:33 UTC | #4

You mean E_PHYSICSPRESTEP?

Btw I found what cause this problem.

    m_node_camera->LookAt(m_spaceship_rb->GetPosition()); // this make this unwanted effect

    m_node_camera->LookAt(m_node_spaceship_model->GetWorldPosition()); // change to this, it solve problem

-------------------------

Modanung | 2019-10-08 09:38:56 UTC | #5

[quote="Elendil, post:4, topic:5653"]
You mean E_PHYSICSPRESTEP?
[/quote]

Ah yes, that's the name of the actual event. `LogicComponent`s have a virtual function called `FixedUpdate` that can be overridden which is called by its `HandlePhysicsPreStep`.

-------------------------

Elendil | 2019-10-08 09:43:58 UTC | #6

Thanks. Unfortunately it not solve problem. Problem cause camera looking at rigidbody. Even if I put code in to `FixedUpdate` or split it in to `E_UPDATE` and `E_PHYSICSPRESTEP`. Solution is look at node or model instead rigid body, which is strange for me.

-------------------------

Modanung | 2019-10-08 09:52:47 UTC | #7

`Node` transforms are interpolated based on its `RigidBody` component when the `Scene` is updated.

-------------------------

Elendil | 2019-10-08 09:54:15 UTC | #8

But strange thing is what cause the "lag" for model (`Drawable` or `StaticModel`) if I look at rigid body. That is the question.

-------------------------

Modanung | 2019-10-08 11:14:40 UTC | #9

The physics simulation runs at a fixed interval, node transform updates and rendering do not.

I lost track of your exact setup.

-------------------------

1vanK | 2019-10-08 22:30:02 UTC | #10

Update camera in PostUpdate (because you own Update can be called before physics processing)

-------------------------

