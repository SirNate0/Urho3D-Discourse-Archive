GodMan | 2018-12-17 00:21:29 UTC | #1

I suppose my c++ skills are rusty here. I'm trying to make it where if your press M the animation controller plays a different animation. This code is in CharacterDemo.cpp the main entry point file.

```
if (input->GetKeyPress(KEY_M))
    animCtrl->PlayExclusive("Models/stand_sword_melee%1.ani", 0, false, 0.2f);
```

The issue is that animCtrl is defined in another .cpp file Character.cpp.

```
AnimationController* animCtrl = node_->GetComponent<AnimationController>(true);
```

I'm using the characterdemo if anyone needs a good reference.

Normally I use a pointer to animCtrl and define it in the header file that's included in CharacterDemo.cpp, but this does not work this time.

-------------------------

Modanung | 2018-12-15 21:46:34 UTC | #2

If you can get to the node you should be able to _get_ any component that's on there.

```
AnimationController* animCtrl{ otherNode->GetComponent<AnimationController>() };
```

-------------------------

GodMan | 2018-12-15 22:47:11 UTC | #3

I tried what you suggested, and it crashes now when I hit M key.

I also tried this: `AnimationController* animCtrl = character_->GetNode()->GetComponent<AnimationController>() ;`

To get the node that ` character_` is pointing to, but it still crashes when I hit the M key.

-------------------------

GodMan | 2018-12-15 23:05:52 UTC | #4

It does not crash anymore. I left off the boolean.

```
`AnimationController* animCtrl{ otherNode->GetComponent<AnimationController>(true) };`
```
But it will not play the animation.

-------------------------

GodMan | 2018-12-16 04:02:50 UTC | #5

     #include <Urho3D/Core/Context.h>
    #include <Urho3D/Graphics/AnimationController.h>
    #include <Urho3D/IO/MemoryBuffer.h>
    #include <Urho3D/Physics/PhysicsEvents.h>
    #include <Urho3D/Physics/PhysicsWorld.h>
    #include <Urho3D/Physics/RigidBody.h>
    #include <Urho3D/Scene/Scene.h>
    #include <Urho3D/Scene/SceneEvents.h>
    #include <Urho3D/Input/Input.h>

    #include "Character.h"

    Character::Character(Context* context) :
        LogicComponent(context),
        onGround_(false),
        okToJump_(true),
        inAirTimer_(0.0f)
    {
        // Only the physics update event is needed: un-subscribe from the rest for optimization
        SetUpdateEventMask(USE_FIXEDUPDATE);
    }

    void Character::RegisterObject(Context* context)
    {
        context->RegisterFactory<Character>();

        // These macros register the class attributes to the Context for automatic load / save handling.
        // We specify the Default attribute mode which means it will be used both for saving into file, and network replication
        URHO3D_ATTRIBUTE("Controls Yaw", float, controls_.yaw_, 0.0f, AM_DEFAULT);
        URHO3D_ATTRIBUTE("Controls Pitch", float, controls_.pitch_, 0.0f, AM_DEFAULT);
        URHO3D_ATTRIBUTE("On Ground", bool, onGround_, false, AM_DEFAULT);
        URHO3D_ATTRIBUTE("OK To Jump", bool, okToJump_, true, AM_DEFAULT);
        URHO3D_ATTRIBUTE("In Air Timer", float, inAirTimer_, 0.0f, AM_DEFAULT);
    }

    void Character::Start()
    {
        // Component has been inserted into its scene node. Subscribe to events now
        SubscribeToEvent(GetNode(), E_NODECOLLISION, URHO3D_HANDLER(Character, HandleNodeCollision));
    }

    void Character::FixedUpdate(float timeStep)
    {
        /// \todo Could cache the components for faster access instead of finding them each frame
        RigidBody* body = GetComponent<RigidBody>();
        AnimationController* animCtrl = node_->GetComponent<AnimationController>(true);
    	Input* input = GetSubsystem<Input>();

        // Update the in air timer. Reset if grounded
        if (!onGround_)
            inAirTimer_ += timeStep;
        else
            inAirTimer_ = 0.0f;
        // When character has been in air less than 1/10 second, it's still interpreted as being on ground
        bool softGrounded = inAirTimer_ < INAIR_THRESHOLD_TIME;

        // Update movement & animation
        const Quaternion& rot = node_->GetRotation();
        Vector3 moveDir = Vector3::ZERO;
        const Vector3& velocity = body->GetLinearVelocity();
        // Velocity on the XZ plane
        Vector3 planeVelocity(velocity.x_ * 0.5f, 0.0f, velocity.z_ * 0.5f);

        if (controls_.IsDown(CTRL_FORWARD))
            moveDir += Vector3::FORWARD;
        if (controls_.IsDown(CTRL_BACK))
            moveDir += Vector3::BACK;
        if (controls_.IsDown(CTRL_LEFT))
            moveDir += Vector3::LEFT;
        if (controls_.IsDown(CTRL_RIGHT))
            moveDir += Vector3::RIGHT;


        // Normalize move vector so that diagonal strafing is not faster
        if (moveDir.LengthSquared() > 0.0f)
            moveDir.Normalize();

        // If in air, allow control, but slower than when on ground
        body->ApplyImpulse(rot * moveDir * (softGrounded ? MOVE_FORCE : INAIR_MOVE_FORCE));

        if (softGrounded)
        {
            // When on ground, apply a braking force to limit maximum ground velocity
            Vector3 brakeForce = -planeVelocity * BRAKE_FORCE;
            body->ApplyImpulse(brakeForce);

            // Jump. Must release jump control between jumps
            if (controls_.IsDown(CTRL_JUMP))
            {
                if (okToJump_)
                {
                    body->ApplyImpulse(Vector3::UP * JUMP_FORCE);
                    okToJump_ = false;
    				animCtrl->PlayExclusive("Models/stand_sword_airborne.ani", 0, false, 0.2f);
                }
            }
            else
                okToJump_ = true;
        }

        if ( !onGround_ )
        {
    		animCtrl->PlayExclusive("Models/stand_sword_airborne.ani", 0, true, 0.2f);
        }
        else
        {
            // Play walk animation if moving on ground, otherwise fade it out
            if (softGrounded && !moveDir.Equals(Vector3::ZERO))
    			animCtrl->PlayExclusive("Models/stand_sword_move_front.ani", 0, true, 0.2f);

            else
    			animCtrl->PlayExclusive("Models/stand_sword_idle.ani", 0, true, 0.2f);

            // Set walk animation speed proportional to velocity
    		animCtrl->SetSpeed("Models/stand_sword_move_front.ani", planeVelocity.Length() * 0.3f);
        }
    	// Play walk animation if moving on ground, otherwise fade it out
    	if (softGrounded && moveDir.Equals(Vector3::RIGHT))
    	{
    		animCtrl->PlayExclusive("Models/stand_sword_move_right.ani", 0, true, 0.2f);
    	}
    	// Play walk animation if moving on ground, otherwise fade it out
    	if (softGrounded && moveDir.Equals(Vector3::LEFT))
    	{
    		animCtrl->PlayExclusive("Models/stand_sword_move_left.ani", 0, true, 0.2f);
    	}
    	// Play walk animation if moving on ground, otherwise fade it out
    	if (softGrounded && moveDir.Equals(Vector3::BACK))
    	{
    		animCtrl->PlayExclusive("Models/stand_sword_move_back.ani", 0, true, 0.2f);
    	}
    	// Switch between 1st and 3rd person
    	if (input->GetKeyPress(KEY_M))
    		animCtrl->PlayExclusive("Models/stand_sword_melee%1.ani", 0, false, 0.2f);

    	// Play walk animation if moving on ground, otherwise fade it out
    	if (inAirTimer_ > 3.5f)
    	{
    		animCtrl->PlayExclusive("Models/stand_sword_dead_airborne.ani", 0, true, 0.2f);
    	}

        // Reset grounded flag for next frame
        onGround_ = false;

    }

    void Character::HandleNodeCollision(StringHash eventType, VariantMap& eventData)
    {
        // Check collision contacts and see if character is standing on ground (look for a contact that has near vertical normal)
        using namespace NodeCollision;

        MemoryBuffer contacts(eventData[P_CONTACTS].GetBuffer());

        while (!contacts.IsEof())
        {
            Vector3 contactPosition = contacts.ReadVector3();
            Vector3 contactNormal = contacts.ReadVector3();
            /*float contactDistance = */contacts.ReadFloat();
            /*float contactImpulse = */contacts.ReadFloat();

            // If contact is below node center and pointing up, assume it's a ground contact
            if (contactPosition.y_ < (node_->GetPosition().y_ + 1.0f))
            {
                float level = contactNormal.y_;
                if (level > 0.75)
                    onGround_ = true;
            }
        }
    }


I have moved my key press function into the Character.cpp file. If I press M it tries to play the animation, but the character just kinda jitters. Something in this file stops it from playing.

-------------------------

GodMan | 2018-12-16 20:36:50 UTC | #7

I may have confused you own the jittering. Here is a video watch until the end. [Video](https://youtu.be/Lm05-39ld1o) That is when I repeatedly press the M key. I tried assigning the melee key to the controls in `CharacterDemo.cpp` on this line "not shown".
    // Clear previous controls
            character_->controls_.Set(CTRL_FORWARD | CTRL_BACK | CTRL_LEFT | CTRL_RIGHT | CTRL_JUMP, false);

Then in` Character.h`
    const int CTRL_FORWARD = 1;
    const int CTRL_BACK = 2;
    const int CTRL_LEFT = 4;
    const int CTRL_RIGHT = 8;
    const int CTRL_JUMP = 16;

I assign the `const int CTRL_MELEE` I am not sure what int value goes for the M key, because I don't know where these numbers came from. The animation would play if I hit the M key, but it kept trying to move my character in one of the directions no matter what int I assigned `CTRL_MELEE`. I was able to add the other thing quite easily like left and right animation. A falling animation, but this turned quite complicated for the melee animation.

-------------------------

GodMan | 2018-12-17 00:21:06 UTC | #9

Well everything is working now. Thanks for the help everyone. I believe part of the problem was that I did not have the bit number right for the melee action.

For anyone in the future this is the updated code for `Character.cpp`

    void Character::FixedUpdate(float timeStep)
    {
    /// \todo Could cache the components for faster access instead of finding them each frame
    RigidBody* body = GetComponent<RigidBody>();
    AnimationController* animCtrl = node_->GetComponent<AnimationController>(true);
    	Input* input = GetSubsystem<Input>();

    // Update the in air timer. Reset if grounded
    if (!onGround_)
        inAirTimer_ += timeStep;
    else
        inAirTimer_ = 0.0f;
    // When character has been in air less than 1/10 second, it's still interpreted as being on ground
    bool softGrounded = inAirTimer_ < INAIR_THRESHOLD_TIME;

    // Update movement & animation
    const Quaternion& rot = node_->GetRotation();
    Vector3 moveDir = Vector3::ZERO;
    const Vector3& velocity = body->GetLinearVelocity();
    // Velocity on the XZ plane
    Vector3 planeVelocity(velocity.x_ * 0.5f, 0.0f, velocity.z_ * 0.5f);

    if (controls_.IsDown(CTRL_FORWARD))
        moveDir += Vector3::FORWARD;
    if (controls_.IsDown(CTRL_BACK))
        moveDir += Vector3::BACK;
    if (controls_.IsDown(CTRL_LEFT))
        moveDir += Vector3::LEFT;
    if (controls_.IsDown(CTRL_RIGHT))
        moveDir += Vector3::RIGHT;


    // Normalize move vector so that diagonal strafing is not faster
    if (moveDir.LengthSquared() > 0.0f)
        moveDir.Normalize();

    // If in air, allow control, but slower than when on ground
    body->ApplyImpulse(rot * moveDir * (softGrounded ? MOVE_FORCE : INAIR_MOVE_FORCE));

    if (softGrounded)
    {
        // When on ground, apply a braking force to limit maximum ground velocity
        Vector3 brakeForce = -planeVelocity * BRAKE_FORCE;
        body->ApplyImpulse(brakeForce);

        // Jump. Must release jump control between jumps
        if (controls_.IsDown(CTRL_JUMP))
        {
            if (okToJump_)
            {
                body->ApplyImpulse(Vector3::UP * JUMP_FORCE);
                okToJump_ = false;
    				animCtrl->PlayExclusive("Models/stand_sword_airborne.ani", 0, false, 0.2f);
            }
        }
        else
            okToJump_ = true;
    }

    	// On air
    	if (!onGround_) {

    		// Falling a lot
    		if (inAirTimer_ > 3.5f)	{
    			animCtrl->PlayExclusive("Models/stand_sword_dead_airborne.ani", 0, true, 0.2f);

    			// Falling a bit		
    		}
    		else {
    			animCtrl->PlayExclusive("Models/stand_sword_airborne.ani", 0, true, 0.2f);
    		}

    		// On ground
    	}
    	else {

    		// On ground with movement
    		if (softGrounded && !moveDir.Equals(Vector3::ZERO)) {

    			// Moving forward
    			if (softGrounded && moveDir.Equals(Vector3::FORWARD)) {
    				animCtrl->PlayExclusive("Models/stand_sword_move_front.ani", 0, true, 0.2f);
    				animCtrl->SetSpeed("Models/stand_sword_move_front.ani", planeVelocity.Length() * 0.3f);
    			}

    			// Moving back
    			if (softGrounded && moveDir.Equals(Vector3::BACK)) {
    				animCtrl->PlayExclusive("Models/stand_sword_move_back.ani", 0, true, 0.2f);
    				animCtrl->SetSpeed("Models/stand_sword_move_back.ani", planeVelocity.Length() * 0.3f);
    			}

    			// Moving left
    			if (softGrounded && moveDir.Equals(Vector3::LEFT)) {
    				animCtrl->PlayExclusive("Models/stand_sword_move_left.ani", 0, true, 0.2f);
    				animCtrl->SetSpeed("Models/stand_sword_move_left.ani", planeVelocity.Length() * 0.3f);
    			}

    			// Moving right
    			if (softGrounded && moveDir.Equals(Vector3::RIGHT))	{
    				animCtrl->PlayExclusive("Models/stand_sword_move_right.ani", 0, true, 0.2f);
    				animCtrl->SetSpeed("Models/stand_sword_move_right.ani", planeVelocity.Length() * 0.3f);
    			}

    			// On ground idle
    		}
    		else {
    			animCtrl->PlayExclusive("Models/stand_sword_idle.ani", 0, true, 0.2f);
    		}

    	}

    	if (controls_.IsDown(CTRL_MELEE)) {
    		animCtrl->PlayExclusive("Models/stand_sword_melee%1.ani", 0, false, 0.0f); // Try tweaking the last value.
    		animCtrl->SetSpeed("Models/stand_sword_melee%1.ani", 1.0f); // Try tweaking the last value.
    	}

    // Reset grounded flag for next frame
    onGround_ = false;

    }

-------------------------

