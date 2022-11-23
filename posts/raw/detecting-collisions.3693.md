Sean221 | 2017-10-30 02:00:01 UTC | #1

I'm having trouble with collisions. I looked on the forums and found that i should be using 

SubscribeToEvent(_node, E_NODECOLLISION, URHO3D_HANDLER(Main, HandleCollision)); 

but how do i tell which rigidbody has collided with the object?

Also can someone tell me why when i try and put the SubscribeToEvent in a different class that isn't inheriting from Sample it doesn't recognize it?


If anyone else cant figure it out this worked for me
RigidBody* body = static_cast<RigidBody*>(eventData[NodeCollision::P_BODY].GetPtr());

-------------------------

Eugene | 2017-10-29 17:21:16 UTC | #2

[quote="Sean221, post:1, topic:3693"]
but how do i tell which rigidbody has collided with the object?
[/quote]

Maybe I didn't understand the question, but event parameter contain enough data, don't they?
https://github.com/urho3d/Urho3D/blob/ee054a1507cb3518c57d4ebc43cfd6dc93de9a27/Source/Urho3D/Physics/PhysicsEvents.h#L90

[quote="Sean221, post:1, topic:3693"]
Also can someone tell me why when i try and put the SubscribeToEvent in a different class that isn’t inheriting from Sample it doesn’t recognize it?
[/quote]
You shoud have your class derived from the `Object`. Should be enough.

-------------------------

Sean221 | 2017-10-29 18:30:16 UTC | #3

How would i go about getting the URHO3D_PARAM?

ive tried RigidBody* body = static_cast<RigidBody*>(eventData[P_BODY].GetPtr());

but that didnt work

-------------------------

Eugene | 2017-10-29 18:50:52 UTC | #4

[quote="Eugene, post:2, topic:3693"]
NodeCollision
[/quote]

What about `NodeCollision::P_BODY`? Well, just use any sampe or piece of engine code as reference.

-------------------------

