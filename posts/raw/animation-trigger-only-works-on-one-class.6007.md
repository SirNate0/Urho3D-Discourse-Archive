GodMan | 2020-03-20 05:17:27 UTC | #1

So this may seem odd. I tried to give my AI class an animation trigger for movements and such, but for some reason their animation trigger fires on my Character class. So for example my AI class has an animation sound trigger for their footsteps which is a completely different sound for testing purposes. When they move nothing happens. When my character moves it plays their sound. I think I made a mistake in my class somewhere, but not to sure. 

AIMelee.h

    #pragma once

    #include <Urho3D/Input/Controls.h>
    #include <Urho3D/Scene/LogicComponent.h>
    #include <Urho3D/Audio/SoundSource3D.h>
    #include <Urho3D/Audio/Sound.h>
    #include <Urho3D/Audio/AudioEvents.h>

    using namespace Urho3D;

    /// Character component, responsible for physical movement according to controls, as well as animation.
    class AIMelee : public LogicComponent
    {
    	URHO3D_OBJECT(AIMelee, LogicComponent);

    public:
    	/// Construct.
    	AIMelee(Context* context):
    	LogicComponent(context),
    	elapsedTime_(0.0f)
    	{
    		SetUpdateEventMask(USE_FIXEDUPDATE);
    		SetUpdateEventMask(USE_UPDATE);
    	}


    	/// Register object factory and attributes.
    	static void RegisterObject(Context* context);

    	/// Handle startup. Called by LogicComponent base class.
    	virtual void Start();

    	virtual void DelayedStart();

    	/// Handle physics world update. Called by LogicComponent base class.
    	virtual void FixedUpdate(float timestep);

    	virtual void Update(float timestep);

    	virtual void PlaySound(const String& soundName);

    	virtual void HandleAnimationTriggerZombie(StringHash eventType, VariantMap& eventData);

    	virtual void loadResources();

    	virtual void bigHead(StringHash eventType, VariantMap& eventData);

    	virtual void melee(StringHash eventType, VariantMap& eventData);

    	virtual void setHealth(int h)
    	{
    		health = h;
    	}

    	int getHealth()
    	{
    		return health;
    	}
    	virtual void setDeath(bool d)
    	{
    		dead_ = d;
    	}

    	bool getDeath()
    	{
    		return dead_;
    	}

    	/// Movement controls. Assigned by the main program each frame.
    	Controls controls_;

    	SoundSource3D* soundSrc;
    	ResourceCache* cache;
    	AnimationController* idle;
    	SharedPtr<Node> handboneNode;
    	WeakPtr<Scene> scene_;
    	DebugRenderer* debug;
    	AnimatedModel* swordObject;

    private:
    	/// Handle physics collision event.
    	void HandleNodeCollision(StringHash eventType, VariantMap& eventData);

    	/// Grounded flag for movement.
    	bool onGround_;
    	/// Grounded flag for movement.
    	bool dead_ = false;
    	/// Jump flag.
    	bool okToJump_;
    	/// In air timer. Due to possible physics inaccuracy, character can be off ground for max. 1/10 second and still be allowed to move.
    	float inAirTimer_;
    	/// elapsed time
    	float elapsedTime_;

    	int health;
    	SharedPtr<Node> head;
    	RigidBody* body;
    	CollisionShape* shape;

    };



AIMelee.cpp
    #include <iostream>   // std::cout
    #include <string>

    #include <Urho3D/Core/CoreEvents.h>
    #include <Urho3D/Core/Context.h>
    #include <Urho3D/Graphics/AnimationController.h>
    #include <Urho3D/Graphics/AnimatedModel.h>
    #include <Urho3D/Graphics/DrawableEvents.h>
    #include <Urho3D/IO/MemoryBuffer.h>
    #include <Urho3D/Physics/PhysicsEvents.h>
    #include <Urho3D/Physics/PhysicsWorld.h>
    #include <Urho3D/Physics/RigidBody.h>
    #include <Urho3D/Physics/CollisionShape.h>
    #include <Urho3D/Scene/Scene.h>
    #include <Urho3D/Scene/SceneEvents.h>
    #include <Urho3D/Input/Input.h>
    #include <Urho3D/Audio/Sound.h>
    #include <Urho3D/Audio/SoundSource3D.h>
    #include <Urho3D/Audio/SoundListener.h>
    #include <Urho3D/Audio/AudioEvents.h>
    #include <Urho3D/Resource/ResourceCache.h>
    #include <Urho3D/Navigation/CrowdAgent.h>
    #include <Urho3D/Graphics/DebugRenderer.h>
    #include <Urho3D/IO/Log.h>

    #include "AIMelee.h"

    void AIMelee::RegisterObject(Context* context)
    {
    	context->RegisterFactory<AIMelee>();
    }

    void AIMelee::Start()
    {
    	loadResources();
    	// Component has been inserted into its scene node. Subscribe to events now
    	SubscribeToEvent(E_NODECOLLISION, URHO3D_HANDLER(AIMelee, HandleNodeCollision));
    }

    void AIMelee::DelayedStart()
    {
    	SubscribeToEvent(E_ANIMATIONTRIGGER, URHO3D_HANDLER(AIMelee, HandleAnimationTriggerZombie));
    	SubscribeToEvent(E_POSTRENDERUPDATE, URHO3D_HANDLER(AIMelee, bigHead));

    }

    void AIMelee::FixedUpdate(float timeStep)
    {
    }

    /// Handle scene update. Called by LogicComponent base class.
    void AIMelee::Update(float timeStep)
    {
    	CrowdAgent* agent = node_->GetComponent<CrowdAgent>();

    	if (health <= 0 && dead_ == false)
    	{
    		PlaySound("Sounds/death_mjr.ogg");
    		idle->PlayExclusive("Models/combat_landing_dead.ani", 0, false, 0.5f); // Try tweaking the last value.

    		if (node_->HasComponent<CrowdAgent>())
    		{
    			agent->Remove();
    		}
    		shape->SetCapsule(15.0f, 5.0f, Vector3(0.0f, 5.0f, 0.0f));
    		body->SetMass(1000000.0f);
    		dead_ = true;
    	}

    	float duration_ = 2.5f;
    	elapsedTime_ += timeStep;

    	if (dead_ == true)
    	{
    		// Disappear when duration expired
    		if (duration_ >= 0)
    		{
    			duration_ -= timeStep;
    			if (duration_ <= 0)
    			{
    				node_->Remove();
    			}
    		}
    	}

    	return;
    }

    void AIMelee::loadResources()
    {
    	cache = GetSubsystem<ResourceCache>();

    	// Create the rendering component + animation controller
    	AnimatedModel* object = node_->CreateComponent<AnimatedModel>();
    	object->SetModel(cache->GetResource<Model>("Models/masterchief.mdl"));
    	object->ApplyMaterialList("Materials/zombie.txt");
    	object->SetOccludee(true);

    	idle = node_->CreateComponent<AnimationController>();

    	handboneNode = node_->GetChild("right_hand_marker", true);

    	swordObject = handboneNode->CreateComponent<AnimatedModel>();
    	swordObject->SetModel(cache->GetResource<Model>("Models/plasma_sword.mdl"));
    	swordObject->ApplyMaterialList("Materials/plasma_sword.txt");

    	// Create rigid body, and set non-zero mass so that the body becomes dynamic
    	body = node_->CreateComponent<RigidBody>();
    	body->SetCollisionLayer(1);
    	body->SetMass(1.0f);

    	// Set zero angular factor so that physics doesn't turn the character on its own.
    	// Instead we will control the character yaw manually
    	body->SetAngularFactor(Vector3::ZERO);

    	// Set the rigid body to signal collision also when in rest, so that we get ground collisions properly
    	body->SetCollisionEventMode(COLLISION_ALWAYS);

    	// Set a capsule shape for collision
    	shape = node_->CreateComponent<CollisionShape>();
    	shape->SetCapsule(40.0f, 70.0f, Vector3(0.0f, 35.0f, 0.0f));

    	// Create a CrowdAgent component and set its height and realistic max speed/acceleration. Use default radius
    	auto* agent = node_->CreateComponent<CrowdAgent>();
    	agent->SetHeight(1.0f);
    	agent->SetMaxSpeed(9.0f);
    	agent->SetMaxAccel(9.0f);




    }

    void AIMelee::bigHead(StringHash eventType, VariantMap& eventData)
    {
    	head = node_->GetChild("head", true);
    	head->SetScale(Vector3(2.5f, 2.5f, 2.5f));

    }

    void AIMelee::melee(StringHash eventType, VariantMap& eventData)
    {
    	scene_ = node_->GetScene();
    	debug = scene_->GetComponent<DebugRenderer>();

    	CollisionShape* shape_ = handboneNode->CreateComponent<CollisionShape>();
    	shape_->SetCapsule(2.0f, 2.0f, Vector3::ZERO, Quaternion::IDENTITY);

    	PhysicsRaycastResult raycResult;
    	auto* physicsWorld = scene_->GetComponent<PhysicsWorld>();

    	const Vector3 start = handboneNode->GetWorldPosition();
    	const Vector3 end = start + (Vector3::FORWARD * 100.0f);

    	physicsWorld->ConvexCast(raycResult, shape_, start, Quaternion::IDENTITY, end, Quaternion::IDENTITY);

    	debug->AddCylinder(handboneNode->GetWorldPosition(), 0.025f, 0.025f, Color::RED, false);

    	RigidBody* resultBody{ raycResult.body_ };
    	AIMelee* _Node;
    	int damage = 100;

    	if (resultBody)
    	{

    		Node* resultNode{ resultBody->GetNode() };

    		if (_Node = resultNode->GetDerivedComponent<AIMelee>())
    		{
    			_Node->setHealth(_Node->getHealth() - damage);
    			resultBody->ApplyImpulse(Vector3(1.0f, 1.0f, 1.0f)* 1.0f);
    		}

    	}
    }

    void AIMelee::HandleNodeCollision(StringHash eventType, VariantMap& eventData)
    {
    	// Check collision contacts and see if character is standing on ground (look for a contact that has near vertical normal)
    	using namespace NodeCollision;

    	RigidBody* body = node_->GetComponent<RigidBody>(true);

    	MemoryBuffer contacts(eventData[P_CONTACTS].GetBuffer());

    	while (!contacts.IsEof())
    	{
    		Vector3 contactPosition = contacts.ReadVector3();
    		Vector3 contactNormal = contacts.ReadVector3();
    		/*float contactDistance = */contacts.ReadFloat();
    		/*float contactImpulse = */contacts.ReadFloat();

    		// If contact is below node center and pointing up, assume it's a ground contact
    		if (contactPosition.y_ < (node_->GetPosition().y_ + 1.0f))
    		{
    			float level = contactNormal.y_;
    			if (level > 0.75)
    				onGround_ = true;
    		}
    	}
    }

    void AIMelee::PlaySound(const String& soundName)
    {
    	ResourceCache* cache = GetSubsystem<ResourceCache>();

    	Sound* sound = cache->GetResource<Sound>(soundName);

    	soundSrc = node_->CreateComponent<SoundSource3D>();
    	soundSrc->SetNearDistance(5.0f);
    	soundSrc->SetFarDistance(15.0f);
    	soundSrc->SetGain(1.0f);
    	soundSrc->SetSoundType(SOUND_EFFECT);  // optional
    	soundSrc->Play(sound);
    	soundSrc->SetAutoRemoveMode(REMOVE_COMPONENT);
    }

    void AIMelee::HandleAnimationTriggerZombie(StringHash eventType, VariantMap& eventData)
    {
    	using namespace AnimationTrigger;
    	AnimatedModel* model = node_->GetComponent<AnimatedModel>();
    	if (model)
    	{
    		AnimationState* state = model->GetAnimationState(eventData[P_NAME].GetString());
    		if (state == NULL)
    			return;


    		Node* bone = node_->GetChild(eventData[P_DATA].GetString(), true);

    		URHO3D_LOGDEBUG("Made it!");

    		if (bone != NULL)
    			PlaySound("Sounds/NutThrow.wav");

    	}

    }

-------------------------

SirNate0 | 2020-03-20 03:42:10 UTC | #2

[quote="GodMan, post:1, topic:6007"]
```
SubscribeToEvent(E_ANIMATIONTRIGGER, URHO3D_HANDLER(AIMelee, HandleAnimationTriggerZombie)); 
SubscribeToEvent(E_POSTRENDERUPDATE, URHO3D_HANDLER(AIMelee, bigHead)); 
SubscribeToEvent(E_ANIMATIONTRIGGER, URHO3D_HANDLER(AIMelee, melee)); 
```
[/quote]

Did you mean to subscribe to the animation trigger event for both `HandleAnimationTriggerZombie` and `melee`?

-------------------------

GodMan | 2020-03-20 05:16:52 UTC | #3

No. I was testing I removed the melee. I'll edit the post. Unfortunately it did not fix anything. I wonder if it has anything do with the models being the same. My character and NPC are the same 3d model just a palette swap. I would not think this would be the issue though.

-------------------------

Modanung | 2020-03-20 08:47:49 UTC | #4

I think `bone` may be null. Could you add a check within the if-statement to be sure it doesn't fail? Or an `assert(bone)` instead of the logging line.

[quote="GodMan, post:1, topic:6007"]
```
Node* bone = node_->GetChild(eventData[P_DATA].GetString(), true); 

URHO3D_LOGDEBUG("Made it!");

if (bone != NULL)
    PlaySound("Sounds/NutThrow.wav");
```
[/quote]

You could probably also reuse some code by making `AIMelee` inherit from `Character`.

-------------------------

GodMan | 2020-03-20 18:17:24 UTC | #5

bone is not returning NULL. It evens shows that the sound loads when the animation trigger fires.

		if (bone != NULL)
		{
			if (bone == NULL)
			{
				URHO3D_LOGDEBUG("Bone is null");
			}

			PlaySound("Sounds/NutThrow.wav");
		}

I'm starting to think maybe my 3D Sound setup has a mistake. Is my PlaySound setup correct? I'm trying to tie a 3d sound to my NPC, and have the sound attenuation from their locations. Maybe their is a problem with a listener node or something. I used the wiki and ninja snow wars, but they both do it differently.

-------------------------

GodMan | 2020-03-20 18:01:24 UTC | #6

So I did some more testing. I removed the event in the Character class, for the animation trigger. I only left the one above. Strangely it still plays the animation trigger from the NPC's class. I verified that my player node has the separate class Character only, and the NPC's have the AIMelee class, but for some reason the player keeps using their animation trigger.

-------------------------

Modanung | 2020-03-20 18:14:22 UTC | #7

Now the assertion is redundant.
Don't forget to wrap the body of your if-statement in accolades... and don't lose your head. :wink:

-------------------------

GodMan | 2020-03-20 18:17:41 UTC | #8

Okay. I just can't figure this out. I just don't see how the character class is using another classes animation trigger.

EDIT: Fixed above post.

-------------------------

JTippetts | 2020-03-20 18:23:01 UTC | #9

Can you post the source for your Character class? It seems likely that is where the problem lies.

Edit: Also note that if you subscribe to events in this manner:

SubscribeToEvent(E_ANIMATIONTRIGGER, URHO3D_HANDLER(AIMelee, melee)); 

you are subscribing to receive all animation triggers, originating from all sources that raise an animation trigger event. If you want to tighten down control, you need to register to only receive animation triggers from a specific (ie, the player or AI) node or controller.

-------------------------

GodMan | 2020-03-20 18:45:34 UTC | #10

    #pragma once //Character.h 

    #include <Urho3D/Input/Controls.h>
    #include <Urho3D/Scene/LogicComponent.h>
    #include <Urho3D/Audio/SoundSource3D.h>
    #include <Urho3D/Audio/Sound.h>
    #include <Urho3D/Audio/AudioEvents.h>

    using namespace Urho3D;

    const int CTRL_FORWARD = 1;
    const int CTRL_BACK = 2;
    const int CTRL_LEFT = 4;
    const int CTRL_RIGHT = 8;
    const int CTRL_JUMP = 16;
    const int CTRL_MELEE = 32;
    const int CTRL_CROUCH = 64;

    const float MOVE_FORCE = 0.8f;
    const float INAIR_MOVE_FORCE = 0.05f;
    const float BRAKE_FORCE = 0.2f;
    const float JUMP_FORCE = 7.0f;
    const float YAW_SENSITIVITY = 0.1f;
    const float INAIR_THRESHOLD_TIME = 0.1f;

    const int LAYER_MOVE = 0;
    const int LAYER_ATTACK = 1;

    /// Character component, responsible for physical movement according to controls, as well as animation.
    class Character : public LogicComponent
    {
        URHO3D_OBJECT(Character, LogicComponent);

    public:
        /// Construct.
        Character(Context* context);
        
        /// Register object factory and attributes.
        static void RegisterObject(Context* context);
        
        /// Handle startup. Called by LogicComponent base class.
        virtual void Start();

    	virtual void DelayedStart();

        /// Handle physics world update. Called by LogicComponent base class.
        virtual void FixedUpdate(float timeStep);

    	virtual void PlaySound(const String& soundName);

    	virtual void HandleAnimationTrigger(StringHash eventType, VariantMap& eventData);

    	virtual void setHealth(int h)
    	{
    		health = h;
    	}

    	int getHealth()
    	{
    		return health;
    	}
    	virtual void setDeath(bool d)
    	{
    		dead_ = d;
    	}

    	bool getDeath()
    	{
    		return dead_;
    	}
        
        /// Movement controls. Assigned by the main program each frame.
        Controls controls_;

    	SoundSource* sound_source;
        
    private:
        /// Handle physics collision event.
        void HandleNodeCollision(StringHash eventType, VariantMap& eventData);
        
        /// Grounded flag for movement.
        bool onGround_;
    	/// Grounded flag for movement.
    	bool dead_ = false;
        /// Jump flag.
        bool okToJump_;
        /// In air timer. Due to possible physics inaccuracy, character can be off ground for max. 1/10 second and still be allowed to move.
        float inAirTimer_;

    	int health;
    	
    };





    //
    // Copyright (c) 2008-2017 the Urho3D project.
    //
    // Permission is hereby granted, free of charge, to any person obtaining a copy
    // of this software and associated documentation files (the "Software"), to deal
    // in the Software without restriction, including without limitation the rights
    // to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    // copies of the Software, and to permit persons to whom the Software is
    // furnished to do so, subject to the following conditions:
    //
    // The above copyright notice and this permission notice shall be included in
    // all copies or substantial portions of the Software.
    //
    // THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    // IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    // FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    // AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    // LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    // OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    // THE SOFTWARE.
    //

    #include <Urho3D/Core/Context.h>
    #include <Urho3D/Graphics/AnimationController.h>
    #include <Urho3D/Graphics/AnimatedModel.h>
    #include <Urho3D/Graphics/DrawableEvents.h>
    #include <Urho3D/IO/MemoryBuffer.h>
    #include <Urho3D/Physics/PhysicsEvents.h>
    #include <Urho3D/Physics/PhysicsWorld.h>
    #include <Urho3D/Physics/RigidBody.h>
    #include <Urho3D/Scene/Scene.h>
    #include <Urho3D/Scene/SceneEvents.h>
    #include <Urho3D/Input/Input.h>
    #include <Urho3D/Audio/SoundSource3D.h>
    #include <Urho3D/Audio/Sound.h>
    #include <Urho3D/Audio/AudioEvents.h>
    #include <Urho3D/Resource/ResourceCache.h>
    #include <Urho3D/Navigation/CrowdAgent.h>

    #include "Character.h"

    Character::Character(Context* context) :
        LogicComponent(context),
        onGround_(false),
        okToJump_(true),
        inAirTimer_(0.0f)
    {
        // Only the physics update event is needed: un-subscribe from the rest for optimization
        SetUpdateEventMask(USE_FIXEDUPDATE);
    }

    void Character::RegisterObject(Context* context)
    {
        context->RegisterFactory<Character>();

        // These macros register the class attributes to the Context for automatic load / save handling.
        // We specify the Default attribute mode which means it will be used both for saving into file, and network replication
        URHO3D_ATTRIBUTE("Controls Yaw", float, controls_.yaw_, 0.0f, AM_DEFAULT);
        URHO3D_ATTRIBUTE("Controls Pitch", float, controls_.pitch_, 0.0f, AM_DEFAULT);
        URHO3D_ATTRIBUTE("On Ground", bool, onGround_, false, AM_DEFAULT);
        URHO3D_ATTRIBUTE("OK To Jump", bool, okToJump_, true, AM_DEFAULT);
        URHO3D_ATTRIBUTE("In Air Timer", float, inAirTimer_, 0.0f, AM_DEFAULT);
    }

    void Character::Start()
    {
        // Component has been inserted into its scene node. Subscribe to events now
        SubscribeToEvent(GetNode(), E_NODECOLLISION, URHO3D_HANDLER(Character, HandleNodeCollision));
    }

    void Character::DelayedStart()
    {
    	//SubscribeToEvent(GetNode()->GetChild("AdjNode", true), E_ANIMATIONTRIGGER, URHO3D_HANDLER(Character, HandleAnimationTrigger));

    }

    void Character::FixedUpdate(float timeStep)
    {

        /// \todo Could cache the components for faster access instead of finding them each frame
        RigidBody* body = GetComponent<RigidBody>();
        AnimationController* animCtrl = node_->GetComponent<AnimationController>(true);
    	Input* input = GetSubsystem<Input>();
    	CrowdAgent* agent = node_->GetComponent<CrowdAgent>(true);

        // Update the in air timer. Reset if grounded
        if (!onGround_)
            inAirTimer_ += timeStep;
        else
            inAirTimer_ = 0.0f;
        // When character has been in air less than 1/10 second, it's still interpreted as being on ground
        bool softGrounded = inAirTimer_ < INAIR_THRESHOLD_TIME;

        // Update movement & animation
        const Quaternion& rot = node_->GetRotation();
        Vector3 moveDir = Vector3::ZERO;
        const Vector3& velocity = body->GetLinearVelocity();
        // Velocity on the XZ plane
        Vector3 planeVelocity(velocity.x_ * 0.5f, 0.0f, velocity.z_ * 0.5f);

        if (controls_.IsDown(CTRL_FORWARD))
            moveDir += Vector3::FORWARD;
        if (controls_.IsDown(CTRL_BACK))
            moveDir += Vector3::BACK;
        if (controls_.IsDown(CTRL_LEFT))
            moveDir += Vector3::LEFT;
        if (controls_.IsDown(CTRL_RIGHT))
            moveDir += Vector3::RIGHT;


        // Normalize move vector so that diagonal strafing is not faster
        if (moveDir.LengthSquared() > 0.0f)
            moveDir.Normalize();

        // If in air, allow control, but slower than when on ground
        body->ApplyImpulse(rot * moveDir * (softGrounded ? MOVE_FORCE : INAIR_MOVE_FORCE));

        if (softGrounded)
        {
            // When on ground, apply a braking force to limit maximum ground velocity
            Vector3 brakeForce = -planeVelocity * BRAKE_FORCE;
            body->ApplyImpulse(brakeForce);

            // Jump. Must release jump control between jumps
            if (controls_.IsDown(CTRL_JUMP))
            {
                if (okToJump_)
                {
                    body->ApplyImpulse(Vector3::UP * JUMP_FORCE);
                    okToJump_ = false;
    				animCtrl->PlayExclusive("Models/stand_sword_airborne.ani", 0, false, 0.2f);
                }
            }
            else
                okToJump_ = true;
        }

    	// On air
    	if (!onGround_) 
    	{

    		// Falling a lot
    		if (inAirTimer_ > 3.5f)	
    		{		
    			animCtrl->PlayExclusive("Models/combat_landing_dead.ani", 0, true, 0.2f);
    			static bool initialized;
    			if (!initialized)
    			{
    				PlaySound("Sounds/death_mjr.ogg");
    				initialized = true;
    				
    			}
    			// Falling a bit		
    		}
    		else 
    		{
    			animCtrl->PlayExclusive("Models/stand_support_high_airborne.ani", 0, true, 0.2f);
    			
    		}

    		// On ground
    	}
    	else 
    	{

    		// On ground with movement
    		if (softGrounded && !moveDir.Equals(Vector3::ZERO)) {

    			// Moving forward
    			if (softGrounded && moveDir.Equals(Vector3::FORWARD)) {
    				animCtrl->PlayExclusive("Models/combat_rifle_move_front.ani", LAYER_MOVE, true, 0.2f);
    				animCtrl->SetSpeed("Models/combat_rifle_move_front.ani", planeVelocity.Length() * 0.3f);
    				animCtrl->SetWeight("Models/combat_rifle_idle.ani", 0.0f);
    			}

    			// Moving back
    			if (softGrounded && moveDir.Equals(Vector3::BACK)) {
    				animCtrl->PlayExclusive("Models/stand_support_high_move_back.ani", LAYER_MOVE, true, 0.2f);
    				animCtrl->SetSpeed("Models/stand_support_high_move_back.ani", planeVelocity.Length() * 0.3f);
    				animCtrl->SetWeight("Models/combat_rifle_idle.ani", 0.0f);
    			}

    			// Moving left
    			if (softGrounded && moveDir.Equals(Vector3::LEFT)) {
    				animCtrl->PlayExclusive("Models/stand_support_high_move_left.ani", LAYER_MOVE, true, 0.2f);
    				animCtrl->SetSpeed("Models/stand_support_high_move_left.ani", planeVelocity.Length() * 0.3f);
    				animCtrl->SetWeight("Models/combat_rifle_idle.ani", 0.0f);
    			}

    			// Moving right
    			if (softGrounded && moveDir.Equals(Vector3::RIGHT))	{
    				animCtrl->PlayExclusive("Models/stand_support_high_move_right.ani", LAYER_MOVE, true, 0.2f);
    				animCtrl->SetSpeed("Models/stand_support_high_move_right.ani", planeVelocity.Length() * 0.3f);
    				animCtrl->SetWeight("Models/combat_rifle_idle.ani", 0.0f);
    			}

    			// On ground idle
    		}
    		else 
    		{
    			animCtrl->SetStartBone("Models/combat_rifle_idle.ani", "spine1");
    			animCtrl->Play("Models/combat_rifle_idle.ani", LAYER_ATTACK, true, 0.1f);
    			animCtrl->SetWeight("Models/combat_rifle_idle.ani", 0.99f);
    		}

    	}

    	if (controls_.IsDown(CTRL_MELEE)) 
    	{
    		animCtrl->PlayExclusive("Models/stand_sword_melee%1.ani", LAYER_MOVE, false, 0.0f); // Try tweaking the last value.
    		animCtrl->SetSpeed("Models/stand_sword_melee%1.ani", 1.0f); // Try tweaking the last value.
    	}
    	if (controls_.IsDown(CTRL_CROUCH) && softGrounded) 
    	{
    		animCtrl->PlayExclusive("Models/crouch_rifle_idle.ani", LAYER_MOVE, false, 0.25f); // Try tweaking the last value.
    		animCtrl->SetSpeed("Models/crouch_rifle_idle.ani", 0.5f); // Try tweaking the last value.
    	}

        // Reset grounded flag for next frame
        onGround_ = false;


    	if (health <= 0 && dead_ == false && softGrounded)
    	{
    		PlaySound("Sounds/death_mjr.ogg");
    		animCtrl->PlayExclusive("Models/combat_landing_dead.ani", LAYER_MOVE, false, 0.0f); // Try tweaking the last value.
    		animCtrl->StopAll(0);

    		if (node_->HasComponent<CrowdAgent>())
    		{
    			agent->SetEnabled(false);
    		}
    		
    		dead_ = true;
    		return;
    	}

    }

    void Character::HandleNodeCollision(StringHash eventType, VariantMap& eventData)
    {
        // Check collision contacts and see if character is standing on ground (look for a contact that has near vertical normal)
        using namespace NodeCollision;

    	RigidBody* body = node_->GetComponent<RigidBody>(true);

        MemoryBuffer contacts(eventData[P_CONTACTS].GetBuffer());

        while (!contacts.IsEof())
        {
            Vector3 contactPosition = contacts.ReadVector3();
            Vector3 contactNormal = contacts.ReadVector3();
            /*float contactDistance = */contacts.ReadFloat();
            /*float contactImpulse = */contacts.ReadFloat();

            // If contact is below node center and pointing up, assume it's a ground contact
            if (contactPosition.y_ < (node_->GetPosition().y_ + 1.0f))
            {
                float level = contactNormal.y_;
                if (level > 0.75)
                    onGround_ = true;
            }
        }
    }

    void Character::PlaySound(const String& soundName)
    {
    	ResourceCache* cache = GetSubsystem<ResourceCache>();

    	Sound* sound = cache->GetResource<Sound>(soundName);
    	// you can use an existing or a new node to append the sound to
    	Node* node = node_->CreateChild("SoundEffect");
    	sound_source = node->CreateComponent<SoundSource>();
    	sound_source->SetSoundType(SOUND_EFFECT);  // optional
    	sound_source->SetGain(0.2f);
    	sound_source->Play(sound);
    	sound_source->SetAutoRemoveMode(REMOVE_COMPONENT);
    }

    void Character::HandleAnimationTrigger(StringHash eventType, VariantMap& eventData)
    {
    	using namespace AnimationTrigger;
    	AnimatedModel* model = node_->GetChild("AdjNode", true)->GetComponent<AnimatedModel>();
    	if (model)
    	{
    		AnimationState* state = model->GetAnimationState(eventData[P_NAME].GetString());
    		if (state == NULL)
    			return;


    		Node* bone = node_->GetChild(eventData[P_DATA].GetString(), true);

    		if (bone != NULL)
    		PlaySound("Sounds/MasterchiefFootSteps.ogg");

    	}

    }



This is really just the Character class that comes with Urho3d. Just some small changes. 

@JTippetts That makes sense. I removed that part about the melee trigger already though. 
So if I have this: `SubscribeToEvent(E_ANIMATIONTRIGGER, URHO3D_HANDLER(AIMelee, HandleAnimationTriggerZombie));` 
This will pickup all animation trigger events?

-------------------------

JTippetts | 2020-03-20 21:19:12 UTC | #11

Yes, if you subscribe to E_ANIMATIONTRIGGER in that fashion, then it will receive triggers from any and every object that ever sends an animation trigger event. You can see in Character::Start in your code, how it calls SubscribeToEvent(GetNode(), E_NODECOLLISION, ....) which means it will then only receive node collision events generated by it's own Node, and not from all the other potential sources of node collision out there.

In your AIMelee:::Start, you subscribe to E_NODECOLLISION events without specifying they should come from only the component's owning Node. Similarly, in DelayedStart you subscribe to E_ANIMATIONTRIGGER events without qualifying them as coming from it's own node. This means that each of those AIMelee objects will respond to trigger and collision events originating from every object in the game that sends those events, and not just from their own nodes.

You should always be very clear on the flow of events through your game, and on who can respond to a given event, as this can cause hard-to-find issues.

-------------------------

lezak | 2020-03-20 21:29:45 UTC | #12

Two side notes:
[quote="GodMan, post:1, topic:6007"]
SetUpdateEventMask(USE_FIXEDUPDATE); 
SetUpdateEventMask(USE_UPDATE);
[/quote]
This way You'll end up only with update event, You should use SetUpdateEventMask(USE_FIXEDUPDATE | USE_UPDATE)

[quote="GodMan, post:1, topic:6007"]
body->SetMass(1000000.0f);
[/quote]

Setting mass to 0 will make body static.

-------------------------

GodMan | 2020-03-20 21:34:11 UTC | #13

@JTippetts Thanks very informative. I have been studying what resources I could find. @lezak Thanks for the suggestions. I have made the new changes.

-------------------------

GodMan | 2020-03-21 19:31:28 UTC | #14

Okay everything seems to be working now. I also found out one of the animation trigger xml files for that animation the npcs where using has an issue. I may have fixed it before not realizing this. @JTippetts I hade called` GetNode()`  in my debugging steps, but nothing worked and I assumed that was wrong. Their were most likely a few issues.

One thing I never got working is the` node->Remove();` when the NPC dies and gets removed after a certain amount of time. I got it from NinjaSnowWars. Oddly I repurposed it for my custom projectile class and it works great.


**EDIT:** You guys are not going to believe this, but the animation xml file had a small space before the .xml. This may have been working the whole time. Thanks everyone for the informative information. This help me improve my class. 

I just need to figure out why the duration counter for node removal is not working.

**EDIT2** I fixed my Update issue. NPCs are now removed by the class after being dead for a certain amout of time. I also fixed the 3d sound issue. I was not using the player as the listener node. Now attenuation works great.

Thanks everyone

-------------------------

