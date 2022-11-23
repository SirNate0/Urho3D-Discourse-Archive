Cpl.Bator | 2017-01-02 01:12:30 UTC | #1

[url=http://www.hostingpics.net/viewer.php?id=302092shoot2.png][img]http://img15.hostingpics.net/thumbs/mini_302092shoot2.png[/img][/url]
[url=http://grom.hd.free.fr/Urho3DDestrucor.rar]Urho3DDestrucor.rar[/url]

Hello. i've got a question about force of impact between two bodies , in my case, bullet and crate.
what is the best method for get the impact power when two entities collide with angel script ?
i want to break some crate if the impact is high , else, nothing happen, just collide. i think there is a method with velocity and mass , but how ?

-------------------------

cadaver | 2017-01-02 01:12:30 UTC | #2

In a physics collision event, the Contacts buffer contains collision contact information. Reading it is slightly non-obvious, but NinjaSnowWar demostrates it, see WorldCollision() function in GameObject.as. The impulse is read but not actually used in this game.

[github.com/urho3d/Urho3D/blob/m ... eObject.as](https://github.com/urho3d/Urho3D/blob/master/bin/Data/Scripts/NinjaSnowWar/GameObject.as)

-------------------------

1vanK | 2017-01-02 01:12:31 UTC | #3

[code]/// Physics collision ongoing.
URHO3D_EVENT(E_PHYSICSCOLLISION, PhysicsCollision)
{
    URHO3D_PARAM(P_WORLD, World);                  // PhysicsWorld pointer
    URHO3D_PARAM(P_NODEA, NodeA);                  // Node pointer
    URHO3D_PARAM(P_NODEB, NodeB);                  // Node pointer
    URHO3D_PARAM(P_BODYA, BodyA);                  // RigidBody pointer
    URHO3D_PARAM(P_BODYB, BodyB);                  // RigidBody pointer
    URHO3D_PARAM(P_TRIGGER, Trigger);              // bool
    URHO3D_PARAM(P_CONTACTS, Contacts);            // Buffer containing position (Vector3), normal (Vector3), distance (float), impulse (float) for each contact
}
[/code]

I think Contacts.impulse is what you need

how to get data from contacts you can see in example 18_CharacterDemo

EDIT:
while I wrote, you have already answered :)

-------------------------

Cpl.Bator | 2017-01-02 01:12:31 UTC | #4

Thank you very much !

-------------------------

