GodMan | 2020-03-07 02:41:51 UTC | #1

So I have a raycast from my projectile. I'm trying to get the raycast to applyimpulse to any rigidbody it hits.

This is in my main file.

            PhysicsWorld* physicsWorld_ = scene_->GetComponent<PhysicsWorld>();
    	PhysicsRaycastResult result;
    	Vector3 pos(boxNode->GetWorldPosition());
    	Ray ray(pos, boxNode->GetWorldDirection());  // the given vector is the direction
    	physicsWorld_->RaycastSingle(result, ray, 40.0f, 0);
    	if (result.distance_ <= 40)
    	{
    	       projectile->impact(result, ray);

    	}

This is in my projectile class.

    void impact(PhysicsRaycastResult result, Ray ray)
    	{
    		RigidBody* resultBody{ result.body_ };

    		if (resultBody) 
    		{

    			Node* resultNode{ resultBody->GetNode() };
    			resultBody->ApplyForce(Vector3(5.0f,5.0f,5.0f),
    			resultNode->WorldToLocal(result.position_));
    			URHO3D_LOGDEBUG("FIRED");
    		}
    	}

@Modanung helped me with some of the snippet. I see that the event does trigger in the console, but nothing happens to any rigidbody that the projectile hits.

-------------------------

Modanung | 2020-03-07 02:49:59 UTC | #2

I think the force might be a little low. Try it with `ApplyImpulse` instead of `ApplyForce` and `ray.direction_ * 9000.0f` instead of the "`Vector3::ONE * 5.0f`".

`Apply`**`Force`** is meant to be used during the `FixedUpdate` event, together with a timestep.

-------------------------

GodMan | 2020-03-07 02:54:00 UTC | #3

I used ApplyForce just for testing. I have it as ApplyImpulse. I'll try what you said.

-------------------------

GodMan | 2020-03-07 03:06:16 UTC | #4

What I got it working now. I believe the problem was two things. One like @Modanung said the Impulse may have been a small amount. Also I went to check the collision layers and it was suppose to be one not two.

Updated Code:

    	void impact(PhysicsRaycastResult result, Ray ray)
    	{
    		RigidBody* resultBody{ result.body_ };

    		if (resultBody) 
    		{

    			Node* resultNode{ resultBody->GetNode() };
    			resultBody->ApplyImpulse(Vector3(500.0f,500.0f,500.0f),ray.direction_ * 9000.0f);
    			URHO3D_LOGDEBUG("FIRED");
    		}
    	}

-------------------------

Modanung | 2020-03-07 03:08:41 UTC | #5

Be sure you use the function correctly.
```
/// Apply impulse at local position.
void ApplyImpulse(const Vector3& impulse, const Vector3& position);
```

-------------------------

