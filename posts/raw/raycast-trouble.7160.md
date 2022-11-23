GodMan | 2022-01-29 01:21:02 UTC | #1

So I am trying to have my energy sword cast a constant ray to check if an enemy is within range. However when I turn on the debug render I cannot get the raycast ray to show. I've been able to set this up for other parts of my code with no issues. Some of the code has been moved around for debugging. 




```
void EnergySword::RegisterObject(Context* context)
{
	context->RegisterFactory<EnergySword>();
}

void EnergySword::Start()
{
	loadResources();

	// Component has been inserted into its scene node. Subscribe to events now
	SubscribeToEvent(GetNode(), E_NODECOLLISION, URHO3D_HANDLER(EnergySword, HandleNodeCollision));
}

void EnergySword::DelayedStart()
{
	SubscribeToEvent(node_->GetChild("right_hand_marker", true), E_POSTRENDERUPDATE, URHO3D_HANDLER(EnergySword, MeleeLunge));
	SubscribeToEvent(GetNode(), E_ANIMATIONTRIGGER, URHO3D_HANDLER(EnergySword, HandleAnimationTriggerZombie));
}

void EnergySword::FixedUpdate(float timeStep)
{
}

void EnergySword::loadResources()
{
	cache = GetSubsystem<ResourceCache>();

	node_->SetScale(Vector3(0.025f, 0.025f, 0.025f));

	swordObject = node_->CreateComponent<AnimatedModel>();
	swordObject->SetModel(cache->GetResource<Model>("Models/plasma_sword.mdl"));
	swordObject->ApplyMaterialList("Materials/plasma_sword.txt");

	meleeshape_ = node_->CreateComponent<CollisionShape>();
	meleeshape_->SetBox(Vector3(50.0f, 20.0f, 2.0f), Vector3::ZERO, Quaternion::IDENTITY);
}

void EnergySword::HandleNodeCollision(StringHash eventType, VariantMap& eventData)
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
		}
	}
}

void EnergySword::PlaySound(const String& soundName, float gain, float nearAttenuation, float farAttenuation)
{
	ResourceCache* cache = GetSubsystem<ResourceCache>();

	// Create the sound source node
	Node *sound_node = node_->CreateChild("Sound source node");

	Sound* sound = cache->GetResource<Sound>(soundName);

	soundSrc = node_->CreateComponent<SoundSource3D>();
	soundSrc->SetNearDistance(nearAttenuation);
	soundSrc->SetFarDistance(farAttenuation);

	// Create the listener node
	Node *listener_node = scene_->GetChild("Player", true);
	// Create the listener itself
	SoundListener *listener = listener_node->CreateComponent<SoundListener>();

	// Set the listener for that audio subsystem
	cache->GetSubsystem<Audio>()->SetListener(listener);

	soundSrc->SetGain(gain);
	soundSrc->Play(sound);
	soundSrc->SetAutoRemoveMode(REMOVE_COMPONENT);
}

void EnergySword::HandleAnimationTriggerZombie(StringHash eventType, VariantMap& eventData)
{
	using namespace AnimationTrigger;
	AnimatedModel* model = node_->GetComponent<AnimatedModel>();
	if (model)
	{
		AnimationState* state = model->GetAnimationState(eventData[P_NAME].GetString());

		if (eventData[P_NAME].GetString() == "Melee 002")
		{
			bone = node_->GetChild(eventData[P_DATA].GetString(), true);



			if (bone != NULL)
			{
				PlaySound("Sounds/sword_melee%2.ogg", 0.5f, 0.1f, 10.0f);
			}

		}
		if (state == NULL)
		{
			return;

		}

	}

}

void EnergySword::DrawDebug(DebugRenderer* debug, bool depthTest)
{
	Vector3 size_{ 50.0f, 20.0f, 2.0f };
	Vector3 startPos_{};
	Vector3 endPos_{};
	Quaternion startRot_{};
	Quaternion endRot_{};

	const BoundingBox bounds{ -size_ * .5f, size_ * .5f };
	debug->AddBoundingBox(bounds, { startPos_, startRot_, 1.f }, Color::GREEN, depthTest);
	debug->AddBoundingBox(bounds, { endPos_, endRot_, 1.f }, Color::RED, depthTest);
	debug->AddLine(startPos_, endPos_, Color::YELLOW, depthTest);
}

void EnergySword::MeleeLunge()
{
	PhysicsWorld* physicsWorld_ = scene_->GetComponent<PhysicsWorld>();
	PhysicsRaycastResult result;
	Vector3 pos(node_->GetWorldPosition());
	Ray ray(pos, node_->GetWorldDirection());  // the given vector is the direction
	physicsWorld_->RaycastSingle(result, ray, 40.0f, 1);
	debug->AddLine(pos, Vector3(0, 0, 0), Color::RED, false);
	if (result.distance_ <= 40)
	{
	}
}
```

-------------------------

GodMan | 2022-01-29 01:23:02 UTC | #3

@wand I have updated the code above. 

I'm trying to get my raycast in MeleeLunge() to show up in the debug render so I can begin coding the next parts, however I cannot get the ray to render.

-------------------------

dertom | 2022-01-29 01:35:26 UTC | #5

Did you debug if the event is called at all? I would guess that E_POSTRENDERUPDATE isn't triggered 'on' the node at all but only globally. Try to remove the binding to the node:

```
SubscribeToEvent(E_POSTRENDERUPDATE, URHO3D_HANDLER(EnergySword, MeleeLunge));
```

-------------------------

GodMan | 2022-01-29 02:02:33 UTC | #6

So I made the changes, but when I change what @dertom suggested it crashes. Ptr.h line 124

-------------------------

Modanung | 2022-01-29 04:31:58 UTC | #7

Is the `EnergySword` properly instantiated?

-------------------------

GodMan | 2022-01-29 05:17:30 UTC | #8

I think so. If I comment out the SubscribeToEvent line everything work fine. I am using the EnergySword class in my main like this. Everything loads fine. 


```
player_handBoneNode = objectNode->GetChild("right_hand_marker", true);
player_handBoneNode->CreateComponent<EnergySword>();
player_handBoneNode->GetComponent<AnimatedModel>()->SetViewMask(3);
```

-------------------------

dertom | 2022-01-29 09:30:47 UTC | #9

The method MeleeLunge has not the right signature for an event-callback. (The one that seems to be kicked also replied this just before me, now his reply is deleted...would have guessed you read that).
Change MeleeLunge to:
```
void EnergySword::MeleeLunge(StringHash eventType, VariantMap& eventData)
```

-------------------------

Modanung | 2022-01-29 11:16:44 UTC | #10

I'm a master of disguises. :magic_wand:
And back before Monday, it seems.

-------------------------

Modanung | 2022-01-29 11:21:22 UTC | #11

Also, as mentioned in the memory hole, I'd change:
```
debug->AddLine(pos, Vector3(0, 0, 0), Color::RED, false);
if (result.distance_ <= 40)
{
}
````

To something like:
```
if (result.body_)
{
   debug->AddLine(pos, result.position_, Color::RED, false);
}
````

-------------------------

George1 | 2022-01-29 11:51:37 UTC | #12

I remember Lumak has an example of ray cast with the ribbon trail slashing a dummy.  It might be useful if you can locate it.

-------------------------

GodMan | 2022-01-29 18:50:36 UTC | #13

So I have made all the changes. @George1  do you have a link to Lumaks example? 

I suspect my issue maybe is that the node the EnergySword is used on is a child node of another node. I could be wrong though.

I've tried this:
`SubscribeToEvent(GetNode()->GetChild("right_hand_marker", true), E_POSTRENDERUPDATE, URHO3D_HANDLER(EnergySword, MeleeLunge));`

It does not crash, but nothing happens.

-------------------------

dertom | 2022-01-29 20:11:14 UTC | #14

[quote="GodMan, post:13, topic:7160"]
It does not crash, but nothing happens.
[/quote]
Yes, because this event is not triggered on this node. 
You need to call as I suggested in the first post and it crashed because you had the method-signature of MeleeLunge wrong,no? Did you change as I suggested in the second post?

-------------------------

GodMan | 2022-01-29 23:17:30 UTC | #15

@dertom Yes I believe I made the changes you suggested. Here is the new code:


```
void EnergySword::RegisterObject(Context* context)
{
	context->RegisterFactory<EnergySword>();
}

void EnergySword::Start()
{
	loadResources();

	// Component has been inserted into its scene node. Subscribe to events now
	SubscribeToEvent(GetNode(), E_NODECOLLISION, URHO3D_HANDLER(EnergySword, HandleNodeCollision));
}

void EnergySword::DelayedStart()
{
	SubscribeToEvent(GetNode()->GetChild("right_hand_marker", true), E_POSTRENDERUPDATE, URHO3D_HANDLER(EnergySword, MeleeLunge));
	SubscribeToEvent(GetNode(), E_ANIMATIONTRIGGER, URHO3D_HANDLER(EnergySword, HandleAnimationTriggerZombie));
}

void EnergySword::FixedUpdate(float timeStep)
{
}

void EnergySword::loadResources()
{
	cache = GetSubsystem<ResourceCache>();

	node_->SetScale(Vector3(0.025f, 0.025f, 0.025f));

	swordObject = node_->CreateComponent<AnimatedModel>();
	swordObject->SetModel(cache->GetResource<Model>("Models/plasma_sword.mdl"));
	swordObject->ApplyMaterialList("Materials/plasma_sword.txt");

	meleeshape_ = node_->CreateComponent<CollisionShape>();
	meleeshape_->SetBox(Vector3(50.0f, 20.0f, 2.0f), Vector3::ZERO, Quaternion::IDENTITY);
}

void EnergySword::HandleNodeCollision(StringHash eventType, VariantMap& eventData)
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
		}
	}
}

void EnergySword::PlaySound(const String& soundName, float gain, float nearAttenuation, float farAttenuation)
{
	ResourceCache* cache = GetSubsystem<ResourceCache>();

	// Create the sound source node
	Node *sound_node = node_->CreateChild("Sound source node");

	Sound* sound = cache->GetResource<Sound>(soundName);

	soundSrc = node_->CreateComponent<SoundSource3D>();
	soundSrc->SetNearDistance(nearAttenuation);
	soundSrc->SetFarDistance(farAttenuation);

	// Create the listener node
	Node *listener_node = scene_->GetChild("Player", true);
	// Create the listener itself
	SoundListener *listener = listener_node->CreateComponent<SoundListener>();

	// Set the listener for that audio subsystem
	cache->GetSubsystem<Audio>()->SetListener(listener);

	soundSrc->SetGain(gain);
	soundSrc->Play(sound);
	soundSrc->SetAutoRemoveMode(REMOVE_COMPONENT);
}

void EnergySword::HandleAnimationTriggerZombie(StringHash eventType, VariantMap& eventData)
{
	using namespace AnimationTrigger;
	AnimatedModel* model = node_->GetComponent<AnimatedModel>();
	if (model)
	{
		AnimationState* state = model->GetAnimationState(eventData[P_NAME].GetString());

		if (eventData[P_NAME].GetString() == "Melee 002")
		{
			bone = node_->GetChild(eventData[P_DATA].GetString(), true);



			if (bone != NULL)
			{
				PlaySound("Sounds/sword_melee%2.ogg", 0.5f, 0.1f, 10.0f);
			}

		}
		if (state == NULL)
		{
			return;

		}

	}

}

void EnergySword::DrawDebug(DebugRenderer* debug, bool depthTest)
{
	Vector3 size_{ 50.0f, 20.0f, 2.0f };
	Vector3 startPos_{};
	Vector3 endPos_{};
	Quaternion startRot_{};
	Quaternion endRot_{};

	const BoundingBox bounds{ -size_ * .5f, size_ * .5f };
	debug->AddBoundingBox(bounds, { startPos_, startRot_, 1.f }, Color::GREEN, depthTest);
	debug->AddBoundingBox(bounds, { endPos_, endRot_, 1.f }, Color::RED, depthTest);
	debug->AddLine(startPos_, endPos_, Color::YELLOW, depthTest);
}

void EnergySword::MeleeLunge(StringHash eventType, VariantMap& eventData)
{
	PhysicsWorld* physicsWorld_ = scene_->GetComponent<PhysicsWorld>();
	PhysicsRaycastResult result;
	Vector3 pos(node_->GetWorldPosition());
	Ray ray(pos, node_->GetWorldDirection());  // the given vector is the direction
	physicsWorld_->RaycastSingle(result, ray, 40.0f, 1);
	if (result.body_)
	{
		debug->AddLine(pos, result.position_, Color::RED, false);
	}
}
```

-------------------------

SirNate0 | 2022-01-29 23:29:45 UTC | #16

[quote="GodMan, post:15, topic:7160"]
```
void EnergySword::MeleeLunge(StringHash eventType, VariantMap& eventData)
{
	PhysicsWorld* physicsWorld_ = scene_->GetComponent<PhysicsWorld>();
	PhysicsRaycastResult result;
	Vector3 pos(node_->GetWorldPosition());
	Ray ray(pos, node_->GetWorldDirection());  // the given vector is the direction
	physicsWorld_->RaycastSingle(result, ray, 40.0f, 1);
	if (result.body_)
	{
		debug->AddLine(pos, result.position_, Color::RED, false);
	}
}
```
[/quote]

Given that you don't declare debug, does this code even compile?

-------------------------

dertom | 2022-01-29 23:31:44 UTC | #17

You subscribe on the node. Change it please like this. good luck...
[quote="dertom, post:5, topic:7160, full:true"]
Did you debug if the event is called at all? I would guess that E_POSTRENDERUPDATE isn’t triggered ‘on’ the node at all but only globally. Try to remove the binding to the node:

```
SubscribeToEvent(E_POSTRENDERUPDATE, URHO3D_HANDLER(EnergySword, MeleeLunge));
```
[/quote]

-------------------------

GodMan | 2022-01-29 23:42:56 UTC | #18

@SirNate0 Yes debug is defined in the header file. I will move this to the cpp for more clarity.
@dertom When I do this it just crashes on startup.

New Code:

```
void EnergySword::RegisterObject(Context* context)
{
	context->RegisterFactory<EnergySword>();
}

void EnergySword::Start()
{
	loadResources();

	// Component has been inserted into its scene node. Subscribe to events now
	SubscribeToEvent(GetNode(), E_NODECOLLISION, URHO3D_HANDLER(EnergySword, HandleNodeCollision));
}

void EnergySword::DelayedStart()
{
	SubscribeToEvent(GetNode(), E_ANIMATIONTRIGGER, URHO3D_HANDLER(EnergySword, HandleAnimationTriggerZombie));
	SubscribeToEvent(E_POSTRENDERUPDATE, URHO3D_HANDLER(EnergySword, MeleeLunge));
}

void EnergySword::FixedUpdate(float timeStep)
{
}

void EnergySword::loadResources()
{
	cache = GetSubsystem<ResourceCache>();

	node_->SetScale(Vector3(0.025f, 0.025f, 0.025f));

	swordObject = node_->CreateComponent<AnimatedModel>();
	swordObject->SetModel(cache->GetResource<Model>("Models/plasma_sword.mdl"));
	swordObject->ApplyMaterialList("Materials/plasma_sword.txt");

	meleeshape_ = node_->CreateComponent<CollisionShape>();
	meleeshape_->SetBox(Vector3(50.0f, 20.0f, 2.0f), Vector3::ZERO, Quaternion::IDENTITY);
}

void EnergySword::HandleNodeCollision(StringHash eventType, VariantMap& eventData)
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
		}
	}
}

void EnergySword::PlaySound(const String& soundName, float gain, float nearAttenuation, float farAttenuation)
{
	ResourceCache* cache = GetSubsystem<ResourceCache>();

	// Create the sound source node
	Node *sound_node = node_->CreateChild("Sound source node");

	Sound* sound = cache->GetResource<Sound>(soundName);

	soundSrc = node_->CreateComponent<SoundSource3D>();
	soundSrc->SetNearDistance(nearAttenuation);
	soundSrc->SetFarDistance(farAttenuation);

	// Create the listener node
	Node *listener_node = scene_->GetChild("Player", true);
	// Create the listener itself
	SoundListener *listener = listener_node->CreateComponent<SoundListener>();

	// Set the listener for that audio subsystem
	cache->GetSubsystem<Audio>()->SetListener(listener);

	soundSrc->SetGain(gain);
	soundSrc->Play(sound);
	soundSrc->SetAutoRemoveMode(REMOVE_COMPONENT);
}

void EnergySword::HandleAnimationTriggerZombie(StringHash eventType, VariantMap& eventData)
{
	using namespace AnimationTrigger;
	AnimatedModel* model = node_->GetComponent<AnimatedModel>();
	if (model)
	{
		AnimationState* state = model->GetAnimationState(eventData[P_NAME].GetString());

		if (eventData[P_NAME].GetString() == "Melee 002")
		{
			bone = node_->GetChild(eventData[P_DATA].GetString(), true);



			if (bone != NULL)
			{
				PlaySound("Sounds/sword_melee%2.ogg", 0.5f, 0.1f, 10.0f);
			}

		}
		if (state == NULL)
		{
			return;

		}

	}

}

void EnergySword::DrawDebug(DebugRenderer* debug, bool depthTest)
{
	Vector3 size_{ 50.0f, 20.0f, 2.0f };
	Vector3 startPos_{};
	Vector3 endPos_{};
	Quaternion startRot_{};
	Quaternion endRot_{};

	const BoundingBox bounds{ -size_ * .5f, size_ * .5f };
	debug->AddBoundingBox(bounds, { startPos_, startRot_, 1.f }, Color::GREEN, depthTest);
	debug->AddBoundingBox(bounds, { endPos_, endRot_, 1.f }, Color::RED, depthTest);
	debug->AddLine(startPos_, endPos_, Color::YELLOW, depthTest);
}

void EnergySword::MeleeLunge(StringHash eventType, VariantMap& eventData)
{
	debug = scene_->GetComponent<DebugRenderer>();

	PhysicsWorld* physicsWorld_ = scene_->GetComponent<PhysicsWorld>();
	PhysicsRaycastResult result;
	Vector3 pos(node_->GetWorldPosition());
	Ray ray(pos, node_->GetWorldDirection());  // the given vector is the direction
	physicsWorld_->RaycastSingle(result, ray, 40.0f, 1);
	if (result.body_)
	{
		debug->AddLine(pos, result.position_, Color::RED, false);
	}
}
```

-------------------------

GodMan | 2022-01-30 00:29:39 UTC | #19

So after double checking my code. I forgot to pass the scene from my main to the EnergySword class. This is done to get things like the debug render of the current scene. After @SirNate0 comment I went to double check all my references. This explains why the other classes were working fine, but not this one. 

Thanks everyone for the suggestions.

-------------------------

