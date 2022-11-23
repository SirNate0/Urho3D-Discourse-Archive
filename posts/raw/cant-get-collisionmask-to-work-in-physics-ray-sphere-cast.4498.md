Dave82 | 2018-08-28 03:45:45 UTC | #1

I have a character and a ground body set up various collision mask to perform sphere cast. I'm trying to get the distance between player head and the ground so i have set it up like this : 
[code]
enum eCollisionMask
{
      CLM_NONE,
      CLM_LEVELMESH = 1,
      CLM_PLAYER = 2,
      CLM_RAYCASTABLE = 4,
}

characterBody->SetCollisionMask(CLM_PLAYER | CLM_LEVELMESH);
groundPlaneBody->SetCollisionMask(CLM_LEVELMESH | CLM_RAYCASTABLE);
[/code]

And perform a sphere cast (Note : i want to perform a spherecast from the top of the player's head so i  want to ignore bodies that have CLM_PLAYER flag set.
[code]
SphereCast(result , ray , radius , maxGroundDistance , CLM_RAYCASTABLE);
[/code]
The problem is there's no body in result and distance is set to infinity when it clearly should be a hit.

if i ignore the viewMask flag in the SphereCast function (using MAX_UNSIGNED) and set the characterBody collision flag to 0 before perform the spherecast then restore it back after spherecast it works perfectly , however this method is most likely slow and it just doesn't seem right.
[code]
unsigned oldMask= characterBody->GetCollisionMask();
characterBody->SetCollisionMask(0);
SphereCast(result , ray , radius , maxGroundDistance , MAX_UNSIGNED);
characterBody->SetCollisionMask(oldMask);

// It Works !

[/code]

Am i missing something ? BTW im using 1.5

-------------------------

Modanung | 2018-08-29 03:18:23 UTC | #2

The collision mask defines what _layers_ an object collides _with_. The _layer_ of a body can be set using `RigidBody::SetCollisionLayer(unsigned)`.

-------------------------

Dave82 | 2018-08-29 03:18:59 UTC | #3

It works now ! Thanks !

-------------------------

