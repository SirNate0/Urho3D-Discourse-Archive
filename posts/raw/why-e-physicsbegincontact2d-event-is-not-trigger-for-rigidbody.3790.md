Taymindis | 2017-11-26 15:20:17 UTC | #1

Below is Not working 
 SubscribeToEvent(**mainRigidBody**, E_PHYSICSBEGINCONTACT2D, URHO3D_HANDLER(Urho2DConstraints, HandleBallContactStart));


But this is working:
 SubscribeToEvent(**mainPhysicslWorld**, E_PHYSICSBEGINCONTACT2D, URHO3D_HANDLER(Urho2DConstraints, HandleBallContactStart));

-------------------------

Eugene | 2017-11-26 15:20:26 UTC | #2

> Why E_PHYSICSBEGINCONTACT2D event is not trigger for rigidBody?

Because `E_PHYSICS*` events are send from the physics world by design.
Nodes send `E_NODE*` events.

-------------------------

Taymindis | 2017-11-26 07:56:56 UTC | #3

[quote="Eugene, post:2, topic:3790"]
E_NODE* events.
[/quote]

Thanks, and it is work now :)

-------------------------

