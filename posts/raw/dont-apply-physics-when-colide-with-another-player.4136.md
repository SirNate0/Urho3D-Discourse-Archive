dev4fun | 2018-03-29 01:59:56 UTC | #1

Hey, on my game if I collide with another player, I apply impulse on him, this way player slides on the map, I dont want this. 

https://puu.sh/zREQx/aa20bd1bc7.mp4

When some player 1 collide with another player 2, I want that player 1 dont be able to walk and player 2 keep on same place.

Have something to do on rigidbody? Or I should to do myself function for this?

Thanks.

-------------------------

Bluemoon | 2018-03-29 08:08:17 UTC | #2

Could SetKinematic() method of RigidBody be what you are looking for?

-------------------------

Eugene | 2018-03-29 09:24:14 UTC | #3

~~Give all your players some specific bit in collision layer and reset this bit in collision mask.~~ Damn, i misunderstood the question.

-------------------------

Modanung | 2018-03-29 08:54:08 UTC | #4

First thing I think of is to drastically increase the friction of standing feet.

-------------------------

dev4fun | 2018-03-29 15:55:49 UTC | #5

Hmm if I set Kinematic to rigidbody, I can't walk with character, I keep on same place, freezed.

-------------------------

Bluemoon | 2018-03-29 16:23:45 UTC | #6

If you set kinematic to true for the rigidbody then you'll need to move the character manually I guess

-------------------------

Eugene | 2018-03-29 19:57:17 UTC | #7

+1 for @Modanung
Just play with friction if you want to use rigid bodies.
E.g. set it to some really large number.

-------------------------

Sinoid | 2018-03-29 20:49:21 UTC | #8

[quote="dev4fun, post:5, topic:4136, full:true"]
Hmm if I set Kinematic to rigidbody, I can’t walk with character, I keep on same place, freezed.
[/quote]

You're probably using forces to move it. Kinematic bodies don't respond to forces, you have to explicitly move them.

-------------------------

dev4fun | 2018-03-29 20:51:58 UTC | #9

Hmm ya, but yet it isnt thats I want. With a large number to friction, I can stop movement immediately, but yet I can push the another character...

-------------------------

dev4fun | 2018-03-29 20:53:56 UTC | #10

Im using this to movement:

    Vector3 cVelocity = cRotation * cMoveDirection * 10.0f;
    Vector3 cImpulse = (cVelocity - pRigidBody->GetLinearVelocity()) * pRigidBody->GetMass();
    pRigidBody->ApplyImpulse( cImpulse );

I can use kinematic, but yes if I collide with another rigid body, I will be able to walk over another character, right? Thats I dont want too haha.

@ Do you guys believe that change PhysicBullets code to do what I want, its a bad solution?

-------------------------

dev4fun | 2018-03-29 20:58:45 UTC | #11

That its exactly what I need:
https://puu.sh/zSaE9/a409bb7aae.mp4

-------------------------

johnnycable | 2018-03-30 07:56:35 UTC | #12

in kabucode:

if "I'm a character" and "I'm immovable" -> I become a wall
if "I'm a character" and "I have to move" -> I become a character
move=talk=interact...

-------------------------

Lumak | 2018-03-30 22:15:05 UTC | #13

The last video that you posted shows player-vs-npc interaction.  If npc interaction is what you're after then set the npc's rigidbody.mass = 0.0f.  However, if you want the npc to move about then set its mass to thousands of magnitude higher than the player's, as to not allow npcs to be moved by the player.

If you're actually looking for a player-vs-player interaction and don't want the player to be moved by another player, take a look at 18_CharacterDemo, the
**void Character::HandleNodeCollision(StringHash eventType, VariantMap& eventData)** fn., this block:
[code]
        Vector3 contactPosition = contacts.ReadVector3();
        Vector3 contactNormal = contacts.ReadVector3();
        /*float contactDistance = */contacts.ReadFloat();
        /*float contactImpulse = */contacts.ReadFloat();
[/code]

the **contactImpulse** is commented out, but that tells you the impulse which was applied to the other body.  Check whether the otherbody is a player and store that impulse and apply that on the next frame in FixedUpdate.  Apply on the next frame because the collision callback indicates that the physics cycle has completed and will do nothing if you apply it in that function.

edit: err, I hope you understand that when I say store and apply the impulse, that I mean negate/reverse the impulse which was applied. I might be mistaken about applyImpulse in collisionHandler. I know applying force and torque from that function gets thrown out, but impulse might stick.

-------------------------

dev4fun | 2018-03-30 22:35:02 UTC | #14

Hmm ya, I understand it. I was thinking about my character movement, and ApplyImpulse its the best way to do what I want? Because I was checking this repository:

https://github.com/1vanK/Urho3DKinematicCharacterController/

And I guess that I needed something custom like this... 'll try another solution different than ApplyImpulse.

-------------------------

Lumak | 2018-03-31 00:07:11 UTC | #15

Oh, nice that you're using 1vank's kinematic controller. It'll be beneficial to hear your progress.

-------------------------

dev4fun | 2018-04-01 01:26:35 UTC | #16

Here we go. My solution for now was: on client side Im using character kinematic controller, while all anothers units on server side uses normal rigidbody with Kinematic seted on true.

https://puu.sh/zTEIc/8eb7ab1268.mp4

I don't know if this way will works on anothers projects, because I rewrote somethings of Scene Replication and Network system to fulfill what I want on a MMORPG (example: the replication of character position, in the video Im with simulated latency on 300ms, if I used the Urho3D way, it would be a problem).

-------------------------

