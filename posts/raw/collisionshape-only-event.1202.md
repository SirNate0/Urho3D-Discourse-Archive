Xtreme | 2017-01-02 01:06:02 UTC | #1

hi,

just tried to use a CollisionShape onyl e.g. to add a "punch sphere".
But the event "E_PHYSICSCOLLISION" isn't fired if i move the sphere (sphere is green rendered) into another physics collision shape.

I've added this to the Characterdemo.cpp -> CreateCharacter function
[code]	// Find the correct child scene node recursively
	 boneNode = objectNode->GetChild("Bip01_L_Forearm", true);
	if (!boneNode)
	{
		LOGWARNING("Could not find bone Bip01_L_Forearm for creating ragdoll physics components");
		return;
	}

	PunchShape = boneNode->CreateComponent<CollisionShape>();
	PunchShape->SetEnabled(true);

	//Vector3 size(0.125f, 0.4f, 0.125f);
	Vector3 size(0.3f, 0.3f, 0.3f);
	Vector3 position(0.2f, 0.0f, 0.0f);
	Quaternion rotation(0.0f, 0.0f, 90.0f);

	PunchShape->SetSphere(size.x_, position, rotation);

	SubscribeToEvent(boneNode, E_PHYSICSCOLLISION, HANDLER(CharacterDemo, HandleNodeCollision));[/code]

-------------------------

thebluefish | 2017-01-02 01:06:02 UTC | #2

You will still need a RigidBody component. Just make it a trigger, and it will only fire events and not respond to the collision.

-------------------------

