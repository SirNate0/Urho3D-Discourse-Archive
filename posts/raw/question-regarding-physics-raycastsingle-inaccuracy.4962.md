Leith | 2019-02-25 05:31:31 UTC | #1

I'm getting some crazy stuff happening when I tried to introduce Foot IK (using sourcecode borrowed from our IK Sample). I get "crazy legs" !!

When I started debugging the relevant code, I noticed something strange.
Just like our sample, I begin by casting a ray down from each foot to the ground.
In my case, the ground in question is a static plane pointing directly up (0,1,0).
I cast a ray directly down onto it, and I get a collision result, but the normal in the result is not pointing directly straight up! Close, but not quite.
Nevertheless, I now cast a second ray from each foot, back along the resulting normal (as per the Sample code). This time, the collision result is something like (0,0.5,0.89) - what the hell?
I'm using collision layers and masks appropriately, although I'm yet to check for absolutely certain that I am indeed hitting the ground, and not something else.

Firstly - why is the result of the first raycast not EXACTLY (0,1,0) ?
Secondly - why is the result of the second raycast (almost straight down) not even CLOSE to (0,1,0)?
It's much closer to (0,0,1) which absolutely makes no sense to me...

[EDIT]
Bullet physics provides for a maximum of 16 collision filter layers (16 bit layer and mask values).
I currently define 7 bits - the default bullet ones, plus a couple more.
My ray (cast from one unit up from the foot position) is hitting the Left Upper Leg body, which has specifically been assigned to the "64" layer (non player character), with a collision mask of "34" (player character=32 | static=2)
My physics query is using a mask to query only objects in the static layer (2).
Yet, I am getting a collision of the query ray, with the Upper Leg of my character.
It appears there is a bug in the RaycastSingle code - either in our current urho master, or in Bullet itself.
Our physicsworld.cpp contains the following code in RaycastSingle:
[code]
rayCallback.m_collisionFilterGroup = (short)0xffff;
rayCallback.m_collisionFilterMask = (short)collisionMask;
[/code]

It appears that the Group flag is not being double-checked against the Mask in Bullet's ray query.
I'd like to confirm this before I go crying to Erwin, what version of Bullet are we on?

[EDIT AGAIN]
I failed to mention that I am creating this scene in code, saving it, then loading it back in.
It could be a failure of our scene loader to set the mask correctly on physics bodies.
Since I am saving the scene to XML, I can confirm that the layer and mask are being serialized correctly, but I can't be sure yet that deserializing in Urho is not the culprit.

-------------------------

Sinoid | 2019-02-25 06:50:32 UTC | #2

It's 2019, use `SphereCast`, then report back. People need to stop with the raycast nonsense, yes ... your rays get trapped in local minima and are prone to FPU exceptions - use the damn sphere-cast like you should be using - how old is the Nettle paper? Answer: really old.

If you still have issues with sane SphereCasts then create a repro case. Without a repro no one can help you beyond silly banter. If you refuse to get with 1998 and use sphere-casts then still provide a repro so you can get more help than more silly banter.

-------------------------

Leith | 2019-02-25 07:21:45 UTC | #3

The problem has been narrowed down to incorrect handling of collision layers (groups in bullet) and their masks "after reloading the scene" - so it looks very much like our deserializer is in question, not bullet, not raycasts
Happy to switch to spherecasting, but expecting the same issue "after scene load".
I have confirmed that the correct values are being serialized, but am yet to check the masks on rigid bodies after deserializing/loading. Running down bugs for over thirty years now, getting close to the bug is something of a specialty.

-------------------------

Leith | 2019-02-26 06:58:54 UTC | #4

I've just done some checking and debugging - it appears that Urho is correctly deserializing the collision layer and mask, which means there must be a bug in Bullet!

Here are my collision filter values, used to define collision layers and masks:
[code]
enum CollisionFilter
{
        Default = 1,
        Static = 2,
        Kinematic = 4,
        Debris = 8,
        Trigger = 16,
        PlayerCharacter = 32,
        NonPlayerCharacter = 64,
        Everything = -1 //all bits sets: DefaultFilter | StaticFilter | KinematicFilter | DebrisFilter | SensorTrigger
};
[/code]

The rigidbodies in question have a collision layer value of 64 (non player character) and collision mask of 34 (static | player character). In binary, we have layer = 1000000, mask = 0100010

Raycast is using layer (1111111), and mask = 0000010. It should ONLY be detecting collision with the "static" layer (2) - but I am detecting collision against layer 64!
This is not meant to happen, right guys?

I have carefully checked that all the values are what I expected - I have carefully applied my collision filter layers and masks - I specifically intended to omit raycast collisions against certain bodies, yet I am detecting the collision.

It would be lovely if someone here would take the time to attempt to reproduce this result before I take my complaint to Erwin Coumans :slight_smile:

1. Create a RigidBody (any shape will do), give it some mass, set layer to 64 and mask to 34,
2. Cast a ray against the rigidbody, with mask set to 2
3. Check result of raycast and confirm yes, we have a collision despite our careful masking.

-------------------------

Leith | 2019-02-26 08:33:14 UTC | #5

OK! I have some answers to this stressful thing.

Let's start with Urho code.
In PhysicsWorld::RaycastSingle, we're passing a btCollisionWorld::ClosestRayResultCallback struct to btCollisionWorld::rayTest method.
Even though this structure defines collisionlayer and mask members, they ARE NOT IMPLEMENTED by Bullet in the default implementation of ClosestRayResultCallback.
In order for PhysicsWorld::RaycastSingle to operate as intended, while respecting our wishes to IGNORE some objects,  we need to derive a NEW URHO3D CLASS!!! from ClosestRayResultCallback AND OVERRIDE  virtual needsCollision method (as per https://pybullet.org/Bullet/phpBB3/viewtopic.php?t=11536) - and implement the new derived struct in PhysicsWorld::RaycastSingle, in order for our filtering to be effective. If we don't do this, then Bullet IGNORES our layer and mask stuff, and just returns the FIRST object the ray hits, irrespective of our filter options. Must I issue a PR for this?

I have to admit, I'm quite surprised that a mature lib like Bullet is not enforcing the filtering by default - why provide the layer and mask members and then not apply them?

-------------------------

Dave82 | 2019-02-26 09:12:02 UTC | #6

I'm using SphereCast to detect falling and standing. And works perfectly.Calling : 
pw->RaycastSingle(rc , ray , maxGroundDistance , CL_LEVELMESH);

Casts a sphere from the center of the player downwards. As intended , the spherecast NEVER hits the player body because it has no CL_LEVELMESH flag set in player's CollisionLayer.
It works perfectly with RaycastSingle too

You're doing something wrong...

-------------------------

Leith | 2019-02-26 09:15:25 UTC | #7

I'm actually not doing anything wrong! I checked!
I don't doubt that spherecast is correctly implemented - but its using a totally different bullet method to perform that test.
There are complaints about this issue floating around for some years now, it's an incomplete feature issue in Bullet that can be worked around by deriving bullet's raycast result struct and implementing virtual needsCollision.
I'll report back when I've tested the changes.

-------------------------

Dave82 | 2019-02-26 09:34:10 UTC | #8

As i already stated RaycastSingle works too. Just tested it and works.

-------------------------

Leith | 2019-02-26 09:53:24 UTC | #9

Did you deliberately omit the object's collision layer as per my three step instructions?
And did you see a collision when you deliberately asked for none?
Or did you just go "yep - it collided, therefore its working"?
I do appreciate your comments, I did not mean that to sound so harsh. A second set of eyes is always good.

-------------------------

Dave82 | 2019-02-26 10:04:17 UTC | #10

My setup is like this : 
[code]
enum eCollisionLayer 
{
	CL_NONE,
	CL_LEVELMESH = 1,
	CL_PLAYER = 2,
	CL_RAYCASTABLE = 4,
	CL_ENEMY = 8,
	CL_ITEM = 16,
	CL_INVENTORYMESH = 32,	// A flag to tell if a mesh is visible in the invetory.
	CL_PARTICLES = 64,		// Particles and billboards.
	CL_COLLISIONONLY = 128,	// Not rendered ,used only for collision
	CL_NAVIGATIONMESH = 256,	// navigation mesh.
};

characterBody->SetCollisionLayer(CL_PLAYER);
characterBody->SetCollisionMask(CL_LEVELMESH);

staicMesh->SetCollisionMask(CL_LEVELMESH|CL_PLAYER);
staicMesh->SetCollisionLayer(CL_LEVELMESH|CL_RAYCASTABLE|CL_PLAYER);

[/code]

now everywhere i speherecast/raycast with a CL_RAYCASTABLE flag only bodies with this bit set to 1 are hit.

-------------------------

Leith | 2019-02-26 10:10:39 UTC | #11

That is the result I would have expected :( I'm using exactly the same logic, but for some reason, masking is failing. Urho is built from the current master on git. You? I'll keep digging / adding debug spew until I find the answer, but the issue is not in my code, I'm certain. I started debugging in my own code, now I've moved to urho engine code, while also keeping an eye on bullet sourcecode. Working my way from the bottom up. I'm a digital electronic engineer among other hats, I think I have a strong grip on binary logic.
Actually maybe you can tell me something useful - did we use the btcollisionshape userpointer to point at our urho collisionshape, so we can cast back from a bullet collisionobject to an urho collisionshape for debug purposes?

-------------------------

Leith | 2019-02-26 10:15:28 UTC | #12

The only difference between your stuff and mine, as I see it, is that I am using bit 1 (value 2), while your stuff is using bit 0 (value 1).

-------------------------

Dave82 | 2019-02-26 10:15:46 UTC | #13

No , i'm still using 1.5. But i doubt anything in this area was changed since except maybe in bullet itself.

-------------------------

Leith | 2019-02-26 10:23:04 UTC | #14

I'm not even sure which version of bullet is used in the current git master branch (of urho)... but thats the sourcecode im staring down - pretty much everything is golden in this branch, so when I found an anomaly I needed to start asking the stupid questions... I've now wasted two days on this, and I will go on wasting my time until I have my pound of flesh. This is very likely to be a bug in Bullet - Erwin has totally neglected Bullet lately, he's probably bored with it and relying on community support for bugfixes. Historically, there has been a number of issues with collision masking, I don't doubt that he's messed up and reverted some fixes. I'll find out when my eyes bleed.

-------------------------

Dave82 | 2019-02-26 10:30:11 UTC | #15

[quote="Leith, post:12, topic:4962, full:true"]
The only difference between your stuff and mine, as I see it, is that I am using bit 1 (value 2), while your stuff is using bit 0 (value 1).
[/quote]
That's not entirely true. I don't have CL_RAYCASTABLE flag set for bodies i don't want to be hit by raycast neither in mask or layer.

-------------------------

Leith | 2019-02-26 10:35:59 UTC | #16

ok sure - but the basic logic of using binary AND to check for matching bitflags holds true
"if (objA.layer & objB.mask) && (objB.layer & objA.mask)" - theres meant to be a doublecheck, which I think I mentioned somewhere in my rant

-------------------------

Dave82 | 2019-02-26 10:34:47 UTC | #17

You're right about that. The layers and masks are really cumbersome and at some point it doesn't make any sense.

-------------------------

Leith | 2019-02-26 10:37:52 UTC | #18

I personally suspect our urho raycastsingle is using group (layer) -1 , and the doublecheck isnt being enforced in bullet, its a wild guess after two days of staring

-------------------------

Dave82 | 2019-02-26 10:42:08 UTC | #19

Actually your code does make sense... if you set your body mask to 34 and perform a raycast with mask 2 then why do you expect your body to be ignored ? 32|2 == 34 and 34 & 2 is true when raycast performs filtering...

-------------------------

Leith | 2019-02-26 11:01:58 UTC | #20

yeah... just wow, it should not happen, but it does. It's clearly a bug, and I have pretty much cleared urho of responsibility too (man, I tend to blame urho first, its usually my fault, but occasionally its not my fault, this time not urho), which leaves bullet... whichever version we are using (in the master branch).
So far all I have confirmed with you, is that the older version of urho is stable, while the new one has some bugs introduced through third party lib updates.

I'm sure you are missing the point,  or the logic, or both.
I put my objects in group 64.
I put my mask as 34.

Raycast group is -1. Urho code.
Mask is set to 2.

lets compare.

object a layer (64) against object b mask (2) = 0
object b layer (-1) against object a mask (34) = 1.

Are both true?
no
(zombieland - always double-tap : a classic example of binary duality and doublecheck)


then no hit should be the result.

-------------------------

Leith | 2019-02-26 11:12:41 UTC | #21

Dave, as an experiment, would you mind grabbing the latest build from the repo? I'll send you my codeblocks project, you can confirm or deny the issue based on me telling you where to set the breakpoint, it would help me immensely to sleep at night knowing im right

-------------------------

Dave82 | 2019-02-26 11:55:24 UTC | #22

[quote="Leith, post:21, topic:4962, full:true"]
Dave, as an experiment, would you mind grabbing the latest build from the repo? I’ll send you my codeblocks project, you can confirm or deny the issue based on me telling you where to set the breakpoint, it would help me immensely to sleep at night knowing im right
[/quote]
Well i can't promise anything... i'm most likely on a road somewhere and when get home i'm dead tired and i barely have time to sit and do anything programming related...

-------------------------

Leith | 2019-02-27 09:55:44 UTC | #23

I've just disabled the construction of unrelated junk in the scene, so I can more easily and clearly see exactly what's going on - I've added some debug code in the engine, and doublechecked that all rigidbodies have appropriate layer and mask values.
Currently, the issue persists.

I'm struggling with time as well, I get home from work, cook dinner, try to relax, code a bit, and its time for bed.

-------------------------

