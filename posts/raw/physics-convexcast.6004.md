GodMan | 2020-03-18 17:27:34 UTC | #1

So i found a post on ConvexCast, but I'm not sure how to use this properly. I am trying to use it for handling melee detection. Does convexcast help with the swiping motion, and make the ray casting more accurate?

-------------------------

SirNate0 | 2020-03-18 19:03:51 UTC | #2

Just to answer your last questions, the idea is that you can use a single convex cast to represent the attack (or whatever) rather than a series of *ray* casts (which are infinitely thin). Consider a baseball example - if you wanted to represent swinging the bat with raycasts you would have to use a raycasts spaced by at most the spacing of the baseball and could still miss some if you had a situation like (ball): where the colon dots are the raycasts. So it's a combination of accuracy and performance that causes the convex cast to be preferable.

-------------------------

Modanung | 2020-03-18 19:38:52 UTC | #3

```
/// Perform a physics world swept convex test using a user-supplied
/// collision shape and return the first hit.
void ConvexCast(PhysicsRaycastResult& result, CollisionShape* shape,
                const Vector3& startPos, const Quaternion& startRot,
                const Vector3& endPos, const Quaternion& endRot,
                unsigned collisionMask = M_MAX_UNSIGNED);
```

@GodMan Could you be more specific concerning your uncertainties?

-------------------------

GodMan | 2020-03-18 20:14:23 UTC | #4

Is the collision shape suppose to be the sword? Or does it want a bullet physics shape like the capsule or box shape?

-------------------------

Modanung | 2020-03-18 21:31:31 UTC | #5

Either will do, but keep it low-poly.

-------------------------

SirNate0 | 2020-03-18 21:57:08 UTC | #6

The built-in shapes are typically faster, and after that low vertex convex hulls, but if there aren't too many of these casts happening you probably shouldn't worry about it. I believe a capsule or box would be the fastest shape that could give you a sword-like shape, and unless you're specifically simulating sword battles probably give you a good enough effect. You could go even further and use two objects for the casts - one is the sharp edge that cuts, the other can be a dull edge that doesn't on a single edged sword.

-------------------------

GodMan | 2020-03-19 02:29:16 UTC | #7


    void AIMelee::melee(StringHash eventType, VariantMap& eventData)
    {
    	scene_ = node_->GetScene();

    	CollisionShape* shape_ = handboneNode->CreateComponent<CollisionShape>();
    	shape_->SetCapsule(2.0f, 2.0f, Vector3::ZERO, Quaternion::IDENTITY);

    	PhysicsRaycastResult raycResult;
    	auto* physicsWorld = scene_->GetComponent<PhysicsWorld>();

    	const Vector3 start = body->GetPosition();
    	const Vector3 end = start + (Vector3::DOWN * 100.0f);

    	physicsWorld->ConvexCast(raycResult, shape_, start, Quaternion::IDENTITY, end, Quaternion::IDENTITY);
    }

I have this, but I have no idea what I'm doing.

-------------------------

Modanung | 2020-03-19 12:59:30 UTC | #8

You could use the "animation - timestep" as the starting transform and the bone's current state as end transform for the swipe. Does that make sense?
Also I don't think you'll want to create a component every time the sword is swept, it doesn't even have to be part of the scene. Just keep a reference somewhere. Something like:
```
swordShape_ = MakeShared<CollisionShape>()
```

I must add I never walked this path, so take these instructions with a grain of salt. Maybe someone else could provide more detailed steps.

As a side note: Appending underscores tends to be reserved for member variables, and is used for discerning them from local variables.

-------------------------

extobias | 2020-03-19 16:15:54 UTC | #9

It's ok, then you need the check if the cast has any result

    // result.body_ is the other body of the collision
    if (result.body_)
    {
         // check others properties of cast result 
    }

-------------------------

GodMan | 2020-03-19 17:08:41 UTC | #10

Thanks for the post everyone. @Modanung I though about using the animation trigger similar to the way sounds are handled for footsteps. I was not sure how to go about that. Also I will remove it from the events.

I will post back later thanks.

-------------------------

GodMan | 2020-03-19 18:02:55 UTC | #11

Is there a way to visualize what is going on, for the ConvexCast? I feel like I'm taking shots in the dark. If I could see whats going on I would probably understand this more.

-------------------------

Modanung | 2020-03-19 18:09:33 UTC | #12

`DebugRenderer::AddTriangleMesh(...)` should be able to help you with that.

-------------------------

GodMan | 2020-03-19 18:10:36 UTC | #13

Okay thanks man as usual

-------------------------

Modanung | 2020-03-19 18:11:12 UTC | #14

...or maybe a cylinder will do. `DebugRenderer::AddCylinder(...)`

-------------------------

