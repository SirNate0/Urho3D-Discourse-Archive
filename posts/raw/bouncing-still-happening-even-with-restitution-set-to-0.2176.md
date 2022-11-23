miz | 2017-01-02 01:13:40 UTC | #1

I have set the restitution of a RigidBody to 0 but after it collides with a static wall (mass set to 0) it still bounces off.

I am even subscribing to E_PHYSICSCOLLISIONSTART and setting linear velocity of the RigidBody to 0,0,0 with the event handler but it still bounces. 

Anyone have a clue what could be happening?

[code]
	playerBody = playerNode->CreateComponent<RigidBody>();
	playerBody->SetMass(10);
	
	playerBody->SetUseGravity(false);
	playerBody->SetAngularFactor(Vector3(0, 0, 0));
	playerBody->SetRestitution(0);
[/code]

[code]void Player::HandleCollisionStart(StringHash eventType, VariantMap& eventData) {
	using namespace PhysicsCollisionStart;

	Node* nodeB = static_cast<Node*>(eventData[P_NODEB].GetPtr());
	Node* nodeA = static_cast<Node*>(eventData[P_NODEA].GetPtr());



	if ((nodeA->GetPosition() == playerNode->GetPosition() || nodeB->GetPosition() == playerNode->GetPosition())) {
		playerBody->SetLinearVelocity(Vector3(0, 0, 0));
	}
}[/code]

-------------------------

miz | 2017-01-02 01:13:41 UTC | #2

So I even tried changing my handler to:

[code]
void Player::HandleCollisionStart(StringHash eventType, VariantMap& eventData) {
   using namespace PhysicsCollisionStart;

   Node* nodeB = static_cast<Node*>(eventData[P_NODEB].GetPtr());
   Node* nodeA = static_cast<Node*>(eventData[P_NODEA].GetPtr());



   if ((nodeA->GetPosition() == playerNode->GetPosition() || nodeB->GetPosition() == playerNode->GetPosition())) {
      playerBody->SetLinearVelocity(Vector3(0, 0, 0));
      STOP = true;
   }

}
[/code]

and then in the in my update handler putting:


[code]
		if (STOP) {
			playerBody->SetLinearVelocity(Vector3(0, 0, 0));
			STOP = false;
		}
[/code]

Which still doesn't work but if I do:

[code]
		if (STOP) {
			playerBody->SetLinearVelocity(Vector3(0, 0, 0));
			//STOP = false; //--- disabled resetting STOP flag
		}
[/code]

Then it does come to a standstill. 

So it seems like whatever Urho3D is doing to change the velocity from the collision is happening after my event handlers and only the next frame after am I able to stop it?

-------------------------

Modanung | 2017-01-02 01:13:41 UTC | #3

Could it be the other object's restitution is non-zero? Then it's like pinball.

-------------------------

miz | 2017-01-02 01:13:41 UTC | #4

other object's restitution is also 0

-------------------------

hdunderscore | 2017-01-02 01:13:41 UTC | #5

[code]if ((nodeA->GetPosition() == playerNode->GetPosition() || nodeB->GetPosition() == playerNode->GetPosition())) {[/code]
This check is dicey at best. You can compare pointers or node names, etc instead.

-------------------------

miz | 2017-01-02 01:13:43 UTC | #6

I'm not having a problem with the check. The code inside the check gets run. It just doesn't stop the bouncing

-------------------------

zedraken | 2017-01-02 01:13:43 UTC | #7

Hello,
it seems that I have almost the same issue. 
I am trying to have a player (at first person view) walk on a terrain. The camera (the player view) is initially located above the terrain and when the simulation starts, the camera falls down until it collides with the terrain. 
Then, the camera starts gliding around on the terrain depending on the slope.

Beyond the implementation details given here (like setting the linear velocity to 0), I just want to be sure if I do it the right way. I mean that to have a first person view, I use the camera for which I create a rigid body with a collision shape. I give the camera a mass and a friction factor (I tried high values).
Thus, I manage the UP and DOWN keys along with the mouse orientation to make the camera move forward in the view direction. Note that is that case, the mouse also gives the vertical orientation of the camera.
However, like you, I am unable to stop the gliding movement, although I implemented the solution you propose (setting up a collision start event handler). Thus, when moving forward by pressing the UP key which is for making the player (the camera) move forward, I am able to cross some terrain parts which have a slope and be on the other side (below the terrain), which makes the camera fall down for the eternity.
So, my questions are :
1 - is it the best solution to implement a first person view walking on a terrain or is there a better way to achieve it ?
2 - if I do it the right way, is there an "elegant" solution for removing the gliding movement, having a simple walk movement based on pressing a "move forward" key, and using the mouse to give the camera direction ?

I can provide more details (code snippets) if needed. Maybe someone has already faced such issue ?

Thanks in advance for your answers.

-------------------------

zedraken | 2017-01-02 01:13:43 UTC | #8

I have quickly checked the "18_CharacterDemo" sample. Can it be a good starting point to understand how to solve the issue ? I saw that a brake force is applied?

-------------------------

miz | 2017-01-02 01:13:43 UTC | #9

It sounds as though you have your camera node and player node as the same node? I would have your camera node separate to you player node and just have it follow your player node. That way you can have the camera node without a body or shape and it won't just fall to the ground.

-------------------------

zedraken | 2017-01-02 01:13:43 UTC | #10

Hi miz, thank you for your reply.

In fact, I think that I really made a simplistic implementation in which I have the terrain node with its physics and collision shape created, and the camera node (also with its physics and collision shape).
I did not create another node so unlikely what is said in your answer, I do not have a player node (maybe my mistake ?).

I remember to have seen the following page on the wiki :
[url]http://urho3d.wikia.com/wiki/Physics[/url]

It seems, as you say, that a node shall be created for the player (with a static or animated model I guess) on which physics and collision shape are created. The camera node does not handle any physics but shall be located and oriented in such a way that it displays what the player sees (first person).

I will try that solution as soon as possible.

-------------------------

