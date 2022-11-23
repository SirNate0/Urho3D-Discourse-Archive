George1 | 2020-05-21 15:13:00 UTC | #1

Here's the tweak to avoid character head going through wall.

       // Set a capsule shape for collision
	float diameter = sqrt(object->GetBoundingBox().max_.x_ * object->GetBoundingBox().max_.x_ + object->GetBoundingBox().max_.z_ * object->GetBoundingBox().max_.z_);
    auto* shape = objectNode->CreateComponent<CollisionShape>();
    shape->SetCapsule(diameter, 1.8f, Vector3(0.0f, 0.9f, 0.0f));

Below is a tweak to limit forward jumping force.  Change in 3 places.
 
Define a jump resistance variable.
float jumpResistance = 1.0f;

    if (controls_.IsDown(CTRL_BACK))
	{
		moveDir += Vector3::BACK;
		jumpResistance = JUMP_FORCE*0.9f;
	}

     // If in air, allow control, but slower than when on ground
    body->ApplyImpulse(rot * moveDir * (softGrounded ? MOVE_FORCE : INAIR_MOVE_FORCE* jumpResistance));


     if (okToJump_)
     {
		jumpResistance = 1.0f;
        body->ApplyImpulse(Vector3::UP * JUMP_FORCE);
        okToJump_ = false;
        animCtrl->PlayExclusive("Models/Mutant/Mutant_Jump1.ani", 0, false, 0.2f);
     }

-------------------------

SirNate0 | 2020-05-21 16:06:25 UTC | #2

Just curious, but what is the jumpResistance supposed to do?

-------------------------

George1 | 2020-05-22 03:15:39 UTC | #3

It prevent over jumped if you are jumping between platforms.  Makes it easier to jump :).

It basically apply braking in the air.

-------------------------

