tni711 | 2019-02-27 01:51:35 UTC | #1

Recently resumed to work on my little table tennis game and have some problem regarding how collision detection works. In my game, when a ball stay at rest on the table, I get a continuous stream of collision event triggered on the table. 
Is there a way to configure the collision so that it only happen once in this case? I tried to set the collision event mode to COLLISION_ACTIVE instead of COLLISION_ALWAYS but it does not make any difference. Thanks ahead for any help!

-------------------------

Leith | 2019-02-27 10:19:52 UTC | #2

It sounds like your bodies are in kinematic mode.

Dynamic bodies will be pushed away from each other when they intersect.
Kinematic bodies remain where they are, and it's your job to move them.

The final kind of body in Bullet physics (I am assuming we are in 3D?) is the ghost shape, otherwise known as a trigger volume, or sensor. These guys are effectively kinematic also.

I've only been here a month, so I can't offer too much advice about debugging physics issues just yet.
But have a look at the collision results, try to debug-print some stuff about which guys are colliding, basic trouble-shooting stuff.

-------------------------

Leith | 2019-02-27 10:46:42 UTC | #3

oh - if the ball is in ROLLING contact, then you can expect continual collision... it makes sense to me.

-------------------------

tni711 | 2019-02-27 11:56:00 UTC | #4

Thanks for the input.

Yes, the ball is in rolling contact and continual collision is exactly what I get. I am just wondering if there is a way to suppress the collision event trigger when the ball is finally at rest on the table. 

Neither the ball nor the table is setup as kinematic body as I need the ball to interact with the paddle base on physics.

auto* ballBody = ballNode->CreateComponent<RigidBody>();
ballBody->SetMass(0.027f);
ballBody->SetRollingFriction(0.02f);
ballBody->SetRestitution(0.9f);
ballBody->SetLinearDamping(0.1f);
ballBody->SetCollisionEventMode(Urho3D::COLLISION_ACTIVE);

auto* tableBody = tableNode->CreateComponent<RigidBody>();
tableBody->SetMass(0.0f); // set mass to zero will make it static
tableBody->SetRestitution(0.8f);
tableBody->SetLinearDamping(0.02f);
tableBody->SetCollisionLayer(2);
tableBody->SetCollisionEventMode(Urho3D::COLLISION_ACTIVE);

-------------------------

Leith | 2019-02-27 12:32:36 UTC | #5

bullet collision objects, by default, will enter a sleep mode in N seconds WHEN AT REST, i think the default is 2 - while asleep, they will stop doing that collision stuff UNLESS you set them as "always awake" (collision always) - "man, I have not moved in ages, in fact i have no momentum at all, I am therefore asleep, and i won't be used as a source / agitator in collision queries, though I can still be a target in collisions, in which case if I am hit, I will wake up"

-------------------------

tni711 | 2019-02-27 13:40:08 UTC | #6

In my case, when the ball stays at rest on the table or on the floor, the collision event triggers keep coming for more than 5 mins. Does not seems like it is going to stop anytime soon.
I am thinking to turn off the ball's collision reporting (Urho3D::COLLISION_NEVER) when its speed comes to zero if no other better way to do it.

-------------------------

Leith | 2019-02-28 01:31:06 UTC | #7

I suggest you start by enabling physics debug-drawing ... the colour of the wireframes will basically tell you if an object is kinematic, dynamic and awake, or dynamic and asleep. If the objects are sleeping (because their angular and linear momentum is close to zero for a couple of seconds) then collision events should not be firing, with the exception of COLLISION_ALWAYS having been set.
If you find your bodies are sleeping, but collisions are still occuring (and nothing is "hitting" them to wake them up) then I'd be happy to attempt to reproduce your issue and confirm or deny.

-------------------------

Modanung | 2019-02-28 02:06:08 UTC | #8

Maybe you're looking to set linear (and/or angular) rest thresholds? You could also choose to only listen to collision _start_ events.

-------------------------

Leith | 2019-02-28 03:10:35 UTC | #9

The default setup for bullet dynamic objects isn't bad... objects that are moving generally come to rest and go to sleep (even in the absence of friction! due to drag...) unless you specifically told them not to do so, and there's a few ways to do that.

-------------------------

tni711 | 2019-03-06 13:35:39 UTC | #10

Thanks for the input from both.
I turned on debug trace and indeed confirm the ball sometimes is still spinning even though it stays at the same position. That explains why I keep getting collision event notification as it is still spinning. The collision notification stops when the ball finally stay at rest, no spinning and not rolling!

![image|690x476](upload://8YbOubDBnNUEAhmBlxYVIa1DePJ.png)

-------------------------

Leith | 2019-03-01 07:44:40 UTC | #11

Great! You can apply some angular drag and friction to make sure the ball comes to angular rest :)

Today I solved my physics headache too.
I had a missing argument in some raycasts which caused my collision mask for the ray to be set to -1 (everything) so the result of the raycast ignored my mask and always collided with stuff I wanted it to ignore.

I believe I also found a bug in RigidBody::SetAttributes, when called during scene loading. I'm not going to issue PR on this, but I've at least made some posts that could be entirely relevant to the next guy who struggles with collision masking after scene loading.

-------------------------

