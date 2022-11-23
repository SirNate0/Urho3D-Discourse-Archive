Durell | 2018-01-10 12:39:05 UTC | #1

Hi there.

Currently making a simple game where i have a character swimming around and colliding with fish. Currently, i have it setup so when i collide with anything, a log is output to the handleupdate() function in my character.cpp.

I want to make it so on collision with a fish a flag inside the fish header file is changed from false to true, causing it to not be rendered etc using "pObject->SetEnabled(false);"

I had a look on the documentation for physics and collision and the only things mentioned in detail are location of the object etc.

Currently I dont know how to grab the specific fish that im colliding with and apply that flag to that specific fish.

Thanks!

-------------------------

Eugene | 2018-01-10 13:00:11 UTC | #2

How do you handle collisions now?

-------------------------

Durell | 2018-01-10 13:23:01 UTC | #3

Currently in my character cpp: 

void Character::Start()
{
	SubscribeToEvent(GetNode(), E_NODECOLLISIONSTART,
		URHO3D_HANDLER(Character, HandleNodeCollision));
}

and

void Character::HandleNodeCollision(StringHash eventType, VariantMap& eventData)
{
	// Check collision contacts and see if character is standing on
	//ground(look for a contact that has near vertical normal)
	Log::WriteRaw("(Collision!");
	using namespace NodeCollision;


	MemoryBuffer contacts(eventData[P_CONTACTS].GetBuffer());
	while (!contacts.IsEof())
	{
		Vector3 contactPosition = contacts.ReadVector3();
		Vector3 contactNormal = contacts.ReadVector3();
		/*float contactDistance = */contacts.ReadFloat();
		/*float contactImpulse = */contacts.ReadFloat();
		// If contact is below node center and mostly vertical, assume
		//it's a ground contact
		if (contactPosition.y_ < (node_->GetPosition().y_ + 1.0f))
		{
			float level = Abs(contactNormal.y_);
			if (level > 0.75)
				onGround_ = true;
		}
	}

}

-------------------------

Eugene | 2018-01-10 13:32:30 UTC | #4

`eventData` contains collided `Node`s, see `E_NODECOLLISIONSTART` description.

-------------------------

Durell | 2018-01-10 13:44:32 UTC | #5

I have looked on the urho physics wiki and googled the term but i cant find any description about what it returns and how to access it etc.

-------------------------

Eugene | 2018-01-10 13:47:45 UTC | #6

[quote="Durell, post:5, topic:3933"]
have looked on the urho physics wiki and googled the term but i cant find any description about what it returns and how to access it etc.
[/quote]

Code is the best documentation ;)
Quite easy to read if you use IDE. Just navigate to event name declatation. Or look here:
https://urho3d.github.io/documentation/HEAD/_event_list.html

-------------------------

Durell | 2018-01-10 13:54:20 UTC | #7

Okay so ive found what i needed

NodeCollisionStart
Body : RigidBody pointer
OtherNode : Node pointer
OtherBody : RigidBody pointer
Trigger : bool

but now how do i access this information? Ive tried eventdata.???? and none of the options my ide gives me are the node its colliding with.

-------------------------

Eugene | 2018-01-10 13:58:32 UTC | #8

[quote="Durell, post:7, topic:3933"]
but now how do i access this information? Ive tried eventdata.??? and none of the options my ide gives me are the node its colliding with.
[/quote]

It's like any other event property: `eventData[P_OTHERNODE].GetPtr()` or `eventData["OtherNode"].GetPtr()` in script.

-------------------------

Durell | 2018-01-10 14:01:35 UTC | #9

is it also possible to despawn the object from the node pointer? Currently ive been using

 pObject->SetEnabled(true);
pObject->SetEnabled(false);

to toggle objects on or off but this is using the staticmodel of the object.

Can this be done just using information from this event?

-------------------------

Eugene | 2018-01-10 14:46:00 UTC | #10

[quote="Durell, post:9, topic:3933"]
but this is using the staticmodel of the object.
[/quote]

It's better to always toggle `Node`s instead of components. Unless you really _need_ the opposite.

-------------------------

Durell | 2018-01-10 14:51:22 UTC | #11

so just to clarify, do i assign  eventData[P_OTHERNODE].GetPtr() to a node first? such as 

node* nodetodelete = eventData[P_OTHERNODE].GetPtr()

then 

nodetodelete->SetEnabled(false)?

not quite sure how to turn an Urho3DRefCounted into an URHO3DNode

-------------------------

Eugene | 2018-01-10 15:14:31 UTC | #12

[quote="Durell, post:11, topic:3933"]
so just to clarify, do i assign  eventData[P_OTHERNODE].GetPtr() to a node first?
[/quote]
Yes.

[quote="Durell, post:11, topic:3933"]
not quite sure how to turn an Urho3DRefCounted into an URHO3DNode
[/quote]
Do `static_cast` for the pointer. Or `dynamic_cast` if you are paranoid about types.

-------------------------

Bluemoon | 2018-01-10 15:19:47 UTC | #13

Just as @Eugene rightly said, below is a line of code in one of my projects

> Node* otherNode = static_cast<Node*>(eventData[P_OTHERNODE].GetPtr());

-------------------------

