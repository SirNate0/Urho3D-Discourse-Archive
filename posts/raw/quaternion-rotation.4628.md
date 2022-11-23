mrchrissross | 2018-10-30 21:58:01 UTC | #1

Hi Everyone,

I'm having a bit of trouble with my spacecraft. I've spent days on this, and really need help.

I'm able to use the mouse to move around the scene and I'm able to move upside down.

The problem I'm having is I'm unable (for the life of me) to get the space craft to rotate around sideways **with the camera**. Here is my code:

Update function:
```
    #pragma region MouseControl
	// Use this frame's mouse motion to adjust camera node yaw and pitch.  
	IntVector2 mouseMove = input->GetMouseMove();
	bool reverseYaw = false;
	
	if (pitch_ < -90.0f || pitch_ > 90.0f)
		reverseYaw = true;
	else 
		reverseYaw = false;

	if (pitch_ > 270.0f)
		pitch_ = -90;
	else if (pitch_ < -270.0f)
		pitch_ = 90;
	
	if(!reverseYaw)
		yaw_ += mouseSensitivity * mouseMove.x_; 
	else if(reverseYaw)
		yaw_ -= mouseSensitivity * mouseMove.x_;

	pitch_ += mouseSensitivity * mouseMove.y_;
#pragma endregion

    #pragma region KeyInfo
	if (!input->GetKeyDown(KEY_C)) // Look Around
	{
		mSpaceship.rb->SetMass(0.0f);
		mSpaceship.rb->SetMass(1.0f);

		Quaternion rotation = mSpaceship.rb->GetRotation().Slerp(Quaternion(0, yaw_ + 90, pitch_), 0.4);
		mSpaceship.rb->SetRotation(rotation);
	}

	if (input->GetKeyDown(KEY_W) && !input->GetKeyDown(KEY_C)) // Move Forward
	{ 
		mSpaceship.rb->SetLinearVelocity(cameraNode_->GetDirection().Normalized() * movementSpeed);

		fireEffect->SetMinEmissionRate(500); fireEffect->SetMaxEmissionRate(800);
		smokeEffect->SetMinEmissionRate(50); smokeEffect->SetMaxEmissionRate(100);
	}
	else 
	{ 
		mSpaceship.rb->SetLinearVelocity(Vector3::ZERO);
		
		fireEffect->SetMinEmissionRate(0); fireEffect->SetMaxEmissionRate(0);
		smokeEffect->SetMinEmissionRate(0); smokeEffect->SetMaxEmissionRate(0);
	}

	if (input->GetKeyDown(KEY_Q)) // Deploy Mine
	{
		if (!mine.node->IsEnabled())
		{
			mine.node->SetEnabled(true);
			mine.node->SetPosition(Vector3(0, -1, 0));
		}
	}

	if (input->GetKeyPress(KEY_P)) // Toggle Fullscreen
	{ 
		if (!GetSubsystem<Graphics>()->GetFullscreen())
		{ 
			GetSubsystem<Graphics>()->SetMode(screenRes.x_, screenRes.y_);
			boostButton->SetPosition((screenRes.x_ - boostButton->GetWidth()) / 2, screenRes.y_ - (screenRes.y_ / 6));
		}
		else
		{
			GetSubsystem<Graphics>()->SetMode(screenRes.x_ / 2, screenRes.y_ / 2);
			boostButton->SetPosition(((screenRes.x_ / 2) - boostButton->GetWidth()) / 2, (screenRes.y_ / 2) - ((screenRes.y_ / 2) / 6));
		}

		GetSubsystem<Graphics>()->ToggleFullscreen();
	}

	if (input->GetKeyDown(KEY_F) && !mMissile.enabled && !input->GetKeyDown(KEY_C))	ShootMissile(); // Fire Missile
	
	if (input->GetKeyPress(KEY_O)) drawDebug = !drawDebug; // Draw Debug Lines

	//if (input->GetKeyDown(KEY_S))  mSpaceship.node->Translate(Vector3::RIGHT * movementSpeed * timeStep);
	if (input->GetKeyDown(KEY_A))
	{
		mSpaceship.node->Rotate(Quaternion(-100 * timeStep, 0.0f, 0.0f), TS_LOCAL);		// Space, Q, A, S, D Keys not needed
		cameraNode_->Rotate(Quaternion(0.0f, 0.0f, 100 * timeStep), TS_LOCAL);
	}
	if (input->GetKeyDown(KEY_D))
	{
		mSpaceship.node->Rotate(Quaternion(100 * timeStep, 0.0f, 0.0f), TS_LOCAL);		// Space, Q, A, S, D Keys not needed
		cameraNode_->Rotate(Quaternion(0.0f, 0.0f, -100 * timeStep), TS_LOCAL);
	}
	//if (input->GetKeyDown(KEY_SPACE))  mSpaceship.node->Translate(Vector3::UP * movementSpeed * timeStep);
	
#pragma endregion
```
HandlePostUpdate Function:
```
    void Game::HandlePostUpdate(StringHash eventType, VariantMap& eventData)
{
	// Physics update has completed. Position camera behind vehicle
	Quaternion dire(yaw_, Vector3::UP);
	dire = dire * Quaternion(0, Vector3::UP);
	dire = dire * Quaternion(pitch_, Vector3::RIGHT);

	Vector3 cameraStartPos = mSpaceship.node->GetPosition();
	Vector3 cameraTargetPos = cameraStartPos - dire * Vector3(0.0f, -2.0f, 15.0f);

	// Raycast camera against static objects (physics collision mask 2)
	// and move it closer to the vehicle if something in between
	Ray cameraRay(cameraStartPos, cameraTargetPos - cameraStartPos);
	float cameraRayLength = (cameraTargetPos - cameraStartPos).Length();
	
	PhysicsRaycastResult result;
	scene_->GetComponent<PhysicsWorld>()->RaycastSingle(result, cameraRay, cameraRayLength, 2);
	if (result.body_)
		cameraTargetPos = cameraStartPos + cameraRay.direction_ * (result.distance_ - 0.5f);

	cameraNode_->SetPosition(cameraTargetPos);
	cameraNode_->SetRotation(dire);
}
```
I think this is all you guys will need code wise.

Here is a video to understand better:

https://imgur.com/k5QmUjg

Any help would be greatly appreciated, I've spent so long on this one!

-------------------------

Modanung | 2018-10-31 00:09:32 UTC | #2

I think you should use `RotateAround` on the camera node to get the result your looking for. Also you might want to correct the ship's pivot orientation to reduce confusion.

Starting to look pretty cool already, btw. :slight_smile:

-------------------------

mrchrissross | 2018-10-31 12:25:37 UTC | #3

Thank you :slight_smile: would it be possible to ask for an example of how to use RotateAround as I have never used it before? how can I correct the pivot orientation? Do I do this when the object is initialised?

-------------------------

jmiller | 2018-10-31 17:56:26 UTC | #4

Hi,

Starting to look interesting already. :)
There are more examples in forum than in Urho: https://discourse.urho3d.io/search?q=RotateAround

RotateAround() and other node methods
  https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_node.html

-------------------------

Modanung | 2018-11-01 08:36:17 UTC | #5

_Another option_ would be to parent the camera to an extra node which you would rotate.

-------------------------

mrchrissross | 2018-11-01 10:29:51 UTC | #6

I think i may just leave it as it is, I've tried quite a few ways parenting the camera to the spaceship being one of them however this takes away the Quaternion.Slerp

-------------------------

Modanung | 2018-11-01 11:06:38 UTC | #7

For objects that don't use physics you can safely get a `Node`'s rotation, `Slerp` and then reassign it using `Set`(`World`)`Rotation`.

Btw, for objects using physics one should refrain from setting their position or velocity directly. Instead you should apply forces and set damping parameters using methods like `ApplyForce`, `ApplyImpulse`, `ApplyTorque`, `ApplyTorqueImpulse`, `SetLinearDamping` and `SetAngularDamping`. Otherwise you are basically overriding the effects of any collisions that may occur.
`

-------------------------

