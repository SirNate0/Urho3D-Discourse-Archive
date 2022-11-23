GodMan | 2020-02-15 21:14:23 UTC | #1

Soon I will be trying to implement melee damage for my NPC against the player. I am just curious how other Urho3d users have gone about this.

Thanks

-------------------------

Modanung | 2020-02-15 22:22:17 UTC | #2

It depends a bit on the exact situation and what you already have. Is there something that stores health or do you even have ranged attacks already implemented?
And by _melee_, do you mean colliding with the enemy, something more akin to a swinging sword or a (delayed) distance check?

-------------------------

GodMan | 2020-02-15 22:48:13 UTC | #3

I mean a sword colliding with a node and a set damage is deducted from the health amount. I have it where the NPC is within a certain range of the player the NPC will swipe at the player. Nothing really fancy at this moment.

-------------------------

Modanung | 2020-02-15 23:22:07 UTC | #4

Part of the sword/enemy FixedUpdate function could include a physics swipe (similar to casting a ray) covering the area it passed through in the current frame. The component keeping track of health could then be retrieved through the rigid body node with functions like `Node::HasComponent<T>()`, `Node::GetComponent<T>()`, `Node::GetDerivedComponent<T>()` and similar functions (see Node.h). Then you could call `Destructable::Hit(damage)` or something of the sort, depending on your exact implementation.

-------------------------

GodMan | 2020-02-15 23:23:30 UTC | #5

Sounds like a good idea. I need to dig around and see. I will post back later. Thanks

-------------------------

GodMan | 2020-02-16 18:07:31 UTC | #6

@Modanung Do you have any more info on the swipe idea?

-------------------------

Modanung | 2020-02-16 18:21:16 UTC | #7

I think using a `PhysicsWorld::ConvexCast` - or multiple raycasts - would make most sense.
```
/// Perform a physics world swept convex test using a user-supplied collision shape and return the first hit.
void ConvexCast(PhysicsRaycastResult& result, CollisionShape* shape, const Vector3& startPos, const Quaternion& startRot, const Vector3& endPos, const Quaternion& endRot, unsigned collisionMask = M_MAX_UNSIGNED);

/// Perform a physics world raycast and return all hits.
void Raycast(PODVector<PhysicsRaycastResult>& result, const Ray& ray, float maxDistance, unsigned collisionMask = M_MAX_UNSIGNED);
```
Do you have experience with physics raycasting? A demonstration of this can be found in the _inverse kinematics_ sample (45).

-------------------------

Lumak | 2020-02-16 18:25:40 UTC | #8

Perhaps, use physics collision object instead of raycast
https://imgur.com/a/KSwljmV

-------------------------

Modanung | 2020-02-16 18:49:39 UTC | #9

This would require one of the bodies to be a trigger, right? To prevent - likely unwelcome - forces from being applied. `RigidBody::SetTrigger(true)`

As Bullet expects triggers to be stationary, wouldn't this introduce the risk of the blade passing through objects unnoticed? Especially at low frame rates.

With a convex cast a collision mask could be used to single out relevant targets.

-------------------------

GodMan | 2020-02-16 19:30:34 UTC | #10

@Modanung I don't care if the sword passes through the player or against another NPC as long as the damage and other things still work.

-------------------------

Modanung | 2020-02-16 19:31:59 UTC | #11

But it should not pass through the player and ignore this fact, right?

-------------------------

GodMan | 2020-02-16 20:09:13 UTC | #12

I mean I guess it depends on the approach right? If I use the sword as an actual physics mesh then I guess not. I'm just saying it does not have to be that precise unless your saying with your approach that it needs to behave this way than that's fine.

-------------------------

Modanung | 2020-02-16 20:54:18 UTC | #13

If neither of both the bodies involved is a trigger - and their layers and masks overlap - one will _not_ be able to pass through the other and you should only apply forces to make them move, refraining from setting positions and velocities directly. That includes no attribute animations. This to not mess up the physics simulation.

-------------------------

GodMan | 2020-02-16 21:23:47 UTC | #14

So what approach do you recommend? Yours or Lumak?

-------------------------

Modanung | 2020-02-16 22:40:49 UTC | #15

I am hoping @Lumak can convincingly refute or confirm my statements.
Until then *I'd* do it my way. :slightly_smiling_face:

-------------------------

GodMan | 2020-02-16 23:31:08 UTC | #16

Well let me go look at sample 45. 😁

-------------------------

Modanung | 2020-02-16 23:44:12 UTC | #17

Other samples that utilize physics raycasting - to position the camera - are 18, 19 and 46.

-------------------------

SirNate0 | 2020-02-17 04:22:14 UTC | #18

You might also look into a Bullet Ghost Object. This thread has a bit of discussion about one, though there may be a couple other threads as well (and also search engines).
https://discourse.urho3d.io/t/support-for-ghostobject-collision-events/5215

-------------------------

GodMan | 2020-02-17 16:58:50 UTC | #19

What are the benefits of the ghost object method?

-------------------------

Modanung | 2020-02-17 17:44:53 UTC | #20

Bullet does not expect them to be stationary, yet objects pass through them. As such they are ideal for this situation and - like convex casting - would not suffer the risk that moving triggers do.

-------------------------

GodMan | 2020-02-17 18:16:53 UTC | #21

Okay. Time to try and understand his post on Ghost Objects.

-------------------------

GodMan | 2020-02-17 23:10:51 UTC | #22

I think I might try Raycast first. I have not done anything real fancy with the Physics part of Urho3d.

-------------------------

