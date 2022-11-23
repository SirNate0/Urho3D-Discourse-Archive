GodMan | 2020-02-28 04:40:34 UTC | #1

Do I need to enable debug data on the physics render to view a single raycast?

-------------------------

George1 | 2020-02-28 06:29:45 UTC | #2

You can use DebugRenderer to draw line...  There are many posts on this....

e.g.
DebugRenderer* debug = scene_->GetComponent<DebugRenderer>();
	debug->AddLine(Vector3(0, 0, 0), Vector3(mx, my, 0), Color(1, 1, 1, 1), false);

-------------------------

GodMan | 2020-02-28 16:54:07 UTC | #3

Oddly I tried this before creating this thread. For some reason it will not render the line. I use it for other things and it works fine.

-------------------------

Dave82 | 2020-02-28 17:38:02 UTC | #4

You need to draw things after the scene drawing is finished. Subscribe to the E_POSTRENDERUPDATE and do your drawings there.

-------------------------

GodMan | 2020-02-28 18:47:59 UTC | #5

Okay I will try this. Seems odd though. I don't do this for other cases and the lines render fine.

-------------------------

GodMan | 2020-02-29 03:35:46 UTC | #6

So I subscribe to the E_POSTRENDERUPDATE. I can see the ray briefly before it disappears. I'm try to raycast forward from a rocket. The line seems to be aiming right of the rocket projectile not it's forward facing. Maybe I have a mistake in my raycast. 

    PhysicsWorld* physicsWorld_ = scene_->GetComponent<PhysicsWorld>();
	PhysicsRaycastResult result;
	Vector3 pos(boxNode->GetWorldPosition());
	Ray ray(pos, boxNode->GetWorldDirection().FORWARD);  // the given vector is the direction
	physicsWorld_->RaycastSingle(result, ray, 250.0f, 1);
	debug->AddLine(pos, result.position_, Color::YELLOW,false);

-------------------------

Modanung | 2020-02-29 03:57:49 UTC | #7

[quote="GodMan, post:6, topic:5948"]
boxNode->GetWorldDirection().FORWARD
[/quote]

Remove the `.FORWARD`: A `Node`'s direction is already the local forward. The *constant* Vector3::FORWARD holds a `{ 0.0f, 0.0f, 1.0f }` vector. Similarly a `Node` has `GetUp()` and `GetRight()` functions which return `rotation_ * Vector3::UP` and `rotation_ * Vector3::RIGHT` respectively.

-------------------------

GodMan | 2020-02-29 04:00:47 UTC | #8

I removed the FORWARD part. The ray is still off. It does not travel the same direction as the moving rocket projectile.

-------------------------

Modanung | 2020-02-29 04:06:53 UTC | #9

Does it use physics? If so, you may want to use `rigidBody_->GetLinearVelocity().Normalized()` instead of the `Node`'s direction.

-------------------------

GodMan | 2020-02-29 04:06:13 UTC | #10

Okay I will try this

-------------------------

GodMan | 2020-02-29 17:55:05 UTC | #11

So I got the rigid body and used the `GetLinearVelocity().Normalized()`, but the same thing still happens.

-------------------------

Modanung | 2020-02-29 18:28:12 UTC | #12

Could you share a screenshot or video?

-------------------------

GodMan | 2020-02-29 18:45:03 UTC | #13

![Screenshot_Sat_Feb_29_12_41_28_2020|690x291](upload://x1sX3aXGlNEFBuMSRtJtty4O5Xq.jpeg)

The rocket is not pointing forward because I removed any rotation on it. I thought this was causing my issue.

-------------------------

Modanung | 2020-02-29 18:54:49 UTC | #14

The line _does_ seem aligned with the launcher. Maybe a `DebugRenderer::AddNode(boxNode)` could help to understand what is going on. Did you check the *asset*'s alignment?

-------------------------

GodMan | 2020-02-29 18:57:32 UTC | #15

I noticed this as well. I'm sure I was using only the projectiles node though. I just spawn it slightly in front of the launcher. Here is a better screenshot I corrected the projectile rotation.

![Screenshot_Sat_Feb_29_12_54_53_2020|690x291](upload://fTrk6kec6dfyKLdL5sudJHNNLpc.jpeg)

-------------------------

GodMan | 2020-02-29 18:59:30 UTC | #16

	boxNode->SetPosition(Pos + Vector3(0.0f,0.0f,1.0f));
	boxNode->SetRotation(objectNode->GetWorldRotation() * Quaternion(-90, Vector3(0, 1, 0)));

Pos is the launchers world position. I move it forward slightly.

-------------------------

Modanung | 2020-02-29 19:23:15 UTC | #17

If your asset is not oriented correctly, *modify the asset*. When this is no option, the correction should happen by attaching the model component to a child node and rotating _that_ (90 degrees left) as to not mess up the logic with it.

-------------------------

GodMan | 2020-02-29 19:47:47 UTC | #18

Okay I will give this a try.

-------------------------

lezak | 2020-02-29 20:55:50 UTC | #19

[quote="GodMan, post:6, topic:5948"]
```
debug->AddLine(pos, result.position_, Color::YELLOW,false);
```
[/quote]

Is the line pointing towards the world position 0,0,0? You should check if there is a hit, because if not result.position_ will be Vector3::ZERO

-------------------------

GodMan | 2020-02-29 23:54:40 UTC | #20

That sounds about right. The ray always tries to point a certain direction no matter how much the character rotates.

Added this. 
```
if (result.distance_ < 250)
{
    objectNode->SetWorldPosition(result.position_);
}
```

-------------------------

GodMan | 2020-02-29 21:43:39 UTC | #21

So after more testing the ray is always to the left of the rocket. Even if I turn the character in the opposite direction.

Rocket in 3d max I don't see any issues:
![Untitled|690x291](upload://v8aI4TrHPtoqir1mvSzJs4od476.png)

**EDIT:** I disabled the physics on the rocket and rotated it in 3ds max and rest it's transofrmation. The rocket and the ray cast now point in the right direction. I just need to track down what the issue is.

-------------------------

Modanung | 2020-02-29 23:57:26 UTC | #22

[quote="GodMan, post:21, topic:5948"]
Rocket in 3d max I don’t see any issues:
[/quote]

See how the rocket points in the positive direction of the X-axis? _Foward_ in 3DsMAX is the direction the green Y arrow points to, which in Urho will be positive Z and correlates to the direction of the ray.

-------------------------

GodMan | 2020-03-01 01:03:31 UTC | #23

I rotated it to positive Y axis. Does this mean for every halo model I will have to reorient the models?

-------------------------

Modanung | 2020-03-01 01:09:21 UTC | #24

That would seem likely.

-------------------------

GodMan | 2020-03-01 01:13:15 UTC | #25

Also I found another thing that was causing the issue. In my projectile class I had this line:
`body->SetLinearVelocity(parentnode_->GetWorldRotation() * Vector3(0.0f, 0.0f, 1.0f) * speed_);`

This cause the rocket to rotate wrong. How can I get the rocket to spawn slightly in front of the launcher, but use the character or launchers forward that way the rocker and ray are correct and not lopsided.

-------------------------

Modanung | 2020-03-01 01:37:16 UTC | #26

Instead of setting the velocity of a rigid body directly, one should prefer applying forces and impulses.
You can use [Newton's 2nd law](https://en.wikipedia.org/wiki/Newton's_laws_of_motion#Newton's_second_law) to convert one to the other:
> force = mass * acceleration

`ApplyImpulse` is expected to be used as a single-shot push, wheras `ApplyForce` expects the force to be multiplied by the timestep of the `FixedUpdate` event.

-------------------------

GodMan | 2020-03-01 01:46:21 UTC | #27

@Modanung ApplyImpulse works great. Only down side is I cannot get the rocket to travel in the forward direction of the character. If I rotate the character and fire the rocket. The rocket travels the same.

-------------------------

GodMan | 2020-03-01 01:52:08 UTC | #28

Okay I got it working correctly now.

CODE: `boxNode->SetRotation(objectNode->GetRotation());` 
This sets the projectile node to the characters rotation. Then the physics with ApplyImpulse moves it in the forward facing direction. The ray cast is also spot on now. 

Thanks @Modanung

-------------------------

Modanung | 2020-03-01 11:18:28 UTC | #29

Do note that `SetRotation` and `GetRotation` are in _local transform space_, meaning this line will only function fine when the parents of both nodes have identical world space transforms. It will fail - for instance - if Master Chief would launch a missile while riding a bicycle.
To be safe, you can use `SetWorldRotation` and `GetWorldRotation` instead.

-------------------------

GodMan | 2020-03-01 17:47:08 UTC | #30

Okay I will update that. Thanks man

-------------------------

