setzer22 | 2017-01-02 01:01:14 UTC | #1

Hello everyone!

I was trying to set up a simple character controller and I needed to check wether if a given rigidbody was grounded or not. I'm using this code snippet (got it from one of the examples)

[code]
MemoryBuffer contacts(eventData[P_CONTACTS].GetBuffer());
    while (!contacts.IsEof()) {

         Vector3 contactPosition = contacts.ReadVector3();
         Vector3 contactNormal = contacts.ReadVector3();
         float contactDistance = contacts.ReadFloat();
         float contactImpulse = contacts.ReadFloat();
         
         // If contact is below node center and mostly vertical, assume it's a ground contact
         if (contactPosition.y_ < (node_->GetPosition().y_ + 1.0f)) {
             float level = Abs(contactNormal.y_);
             if (level > 0.75)
                 onGround = true;
    	}
} [/code]

The compiler, though, keeps complaining about P_CONTACTS not being declared even though I'm including the same headers as the example (I know I don't need many of those but I just tried to make sure before asking):

[code]#include <iostream>
#include "MemoryBuffer.h"
#include "Context.h"
#include "PhysicsEvents.h"
#include "PhysicsWorld.h"
#include "Scene.h"
#include "SceneEvents.h"
#include "PhysicsEvents.h"[/code]

A grep through the source reveals that this P_CONTACTS constant is being used in PhysicsWorld.cpp and PhysicsEvents.h, but I couldn't find any declaration in either of them.

How can I solve this? Where is this variable declared and why does the example work but not my code?

-------------------------

codingmonkey | 2017-01-02 01:01:14 UTC | #2

>How can I solve this

mb you must use Urho3D namespace

-------------------------

scorvi | 2017-01-02 01:01:14 UTC | #3

it is declared in Source/Engine/Physics/PhysicsEvents.h  

[code]
/// Physics collision ongoing (sent to the participating scene nodes.)
EVENT(E_NODECOLLISION, NodeCollision)
{
PARAM(P_BODY, Body); // RigidBody pointer
PARAM(P_OTHERNODE, OtherNode); // Node pointer
PARAM(P_OTHERBODY, OtherBody); // RigidBody pointer
PARAM(P_TRIGGER, Trigger); // bool
PARAM(P_CONTACTS, Contacts); // Buffer containing position (Vector3), normal (Vector3), distance (float), impulse (float) for each contact
}
 [/code]

and you can use it to get the contacts as shown in the example 18_CharacterDemo.
here is the relevant code sample:

[code] // Check collision contacts and see if character is standing on ground (look for a contact that has near vertical normal)
using namespace NodeCollision;
MemoryBuffer contacts(eventData[P_CONTACTS].GetBuffer());[/code]

did you forget to use the appropriat namespace ? 
in this instance you have to use: "using namespace NodeCollision;"

if you dont know which namespace to use look which event you listen to and the second parameter in the event definition is the namespace:
[code]EVENT(E_NODECOLLISION, NodeCollision)[/code]

and also you have to use the Urho3d namespace, just like in the example ... 
[code]using namespace Urho3D;[/code]

-------------------------

setzer22 | 2017-01-02 01:01:15 UTC | #4

Thank you! I was missing the namespace, I was using Urho3D but not NodeCollision. Extra thanks for the tip on how to look for the Event's namespace.

-------------------------

