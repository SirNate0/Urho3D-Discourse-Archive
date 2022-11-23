JamesK89 | 2017-01-02 01:09:10 UTC | #1

I'm trying to convex cast a swept sphere to test a potential path in the environment.
I figure maybe I'm just not understanding how it works properly.

My code to initialize my collision shape looks like this:
[code]
/* ... */
	shape_ = new CollisionShape(context);
	shape_->SetCapsule(2.0f, 2.0f, Vector3::ZERO, Quaternion::IDENTITY);
/* ... */
[/code]

Then during a fixed step update (I'm not really sure it is necessary to do it here since Bullet dynamics is separate from Bullet collision but I did so just to be safe):
[code]
/* ... */
	PhysicsRaycastResult raycResult;

	const Vector3 start = body->GetPosition();
	const Vector3 end = start + (Vector3::DOWN * 100.0f);

	physWorld->ConvexCast(raycResult, shape_, start, Quaternion::IDENTITY, end, Quaternion::IDENTITY);
/* ... */
[/code]

So the problem is that raycResult always comes back as never having hit anything. I stepped through into the ConvexCast code and discovered this if-branch evaluates to true (the [i]!shape->GetCollisionShape()[/i] condition in particular):
[code]
/* ... */
    if (!shape || !shape->GetCollisionShape())
    {
        URHO3D_LOGERROR("Null collision shape for convex cast");
        result.body_ = 0;
        result.position_ = Vector3::ZERO;
        result.normal_ = Vector3::ZERO;
        result.distance_ = M_INFINITY;
        result.hitFraction_ = 0.0f;
        return;
    }
/* ... */
[/code]

Basically the shape doesn't have a btCollisionShape. So is ConvexCast only for arbitrary polygonal models and do I have to manually build a convex capsule mesh, or is it otherwise not acting as intended?

On a semi-related note, you'll have to forgive my ignorance on the Bullet API, I notice that [i]PhysicsRaycastResult[/i] doesn't return a list of contacts but rather just a single contact point. I was wondering if there is some technical reason why the list of contacts can't be retrieved (such as a limitation of the Bullet API) or if it just hasn't been implemented yet?

Thanks

-------------------------

Enhex | 2017-01-02 01:09:10 UTC | #2

Did you check if shape_ is null by the time u try to cast?

-------------------------

JamesK89 | 2017-01-02 01:09:10 UTC | #3

I took a look at it again tonight and I discovered the problem: I was creating the CollisionShape object directly instead of creating it as a component.

Let this be a lesson against tired coding!

-------------------------

Enhex | 2017-01-02 01:09:11 UTC | #4

[quote="JamesK89"]I took a look at it again tonight and I discovered the problem: I was creating the CollisionShape object directly instead of creating it as a component.

Let this be a lesson against tired coding![/quote]

By the way you can create the Bullet collision shape directly, skipping urho's API. That's sort of what SphereCast does internally.
ConvexCast has a version that takes in btCollisionShape*.

It may be the proper approach for your case, since it doesn't seem like you need a component since you don't use a node.

-------------------------

