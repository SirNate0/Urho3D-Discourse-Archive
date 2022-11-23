Pellucas | 2017-01-02 01:01:33 UTC | #1

Cannot move my FPS character diagonally.

Code(AngelScript), Update and FixedUpdate functions
[code]
void HandleUpdate(StringHash eventType, VariantMap& eventData) {
    controls.Set(CTRL_FORWARD | CTRL_BACK | CTRL_LEFT | CTRL_RIGHT | CTRL_JUMP, false);

    controls.Set(CTRL_FORWARD, input.keyDown['W']);
    controls.Set(CTRL_BACK, input.keyDown['S']);
    controls.Set(CTRL_LEFT, input.keyDown['A']);
    controls.Set(CTRL_RIGHT, input.keyDown['D']);
    controls.Set(CTRL_JUMP, input.keyDown[KEY_SPACE]);
}

void FixedUpdate(float delta) {
	RigidBody@ body = node.GetComponent("RigidBody");
	if(body is null) {    
		body = node.CreateComponent("RigidBody");
		body.mass = 1.0f;
	}

	if(!grounded)
		inAirTime += delta;
	else
		inAirTime = 0.0f;

	bool softGrounded = inAirTime < SOFT_TIME;

	Quaternion rot = node.rotation;
	Vector3 moveDir(0.0f, 0.0f, 0.0f);
	Vector3 velocity = body.linearVelocity;
	Vector3 planeVelocity(velocity.x, 0.0f, velocity.z);


    if (controls.IsDown(CTRL_FORWARD))
        moveDir += Vector3(0.0f, 0.0f, 1.0f);
    if (controls.IsDown(CTRL_BACK))
        moveDir += Vector3(0.0f, 0.0f, -1.0f);
    if (controls.IsDown(CTRL_LEFT))
        moveDir += Vector3(-0.1f, 0.0f, 0.0f);
    if (controls.IsDown(CTRL_RIGHT))
        moveDir += Vector3(0.1f, 0.0f, 0.0f);


    if (moveDir.lengthSquared > 0.0f)
       moveDir.Normalize();


    body.ApplyImpulse(rot * moveDir * (softGrounded ? moveForce : airMoveForce));

    
    if (softGrounded)
    {
        Vector3 t_brakeForce = -planeVelocity * brakeForce;
        body.ApplyImpulse(t_brakeForce);

        if (controls.IsDown(CTRL_JUMP))
        {
            if (okToJump)
            {
                body.ApplyImpulse(Vector3(0.0f, 1.0f, 0.0f) * jumpForce);
                okToJump = false;
            }
        }
        else
            okToJump = true;

    }
    grounded = true;
}
[/code]

The player only can move forward, backward, left and right but not diagonally.
I think the problem is [b]ApplyImpulse[/b] because it works perfectly when I use the Translate function.

What's the problem baby?

-------------------------

Pellucas | 2017-01-02 01:01:33 UTC | #2

I still can't solve the problem  :cry:

-------------------------

hdunderscore | 2017-01-02 01:01:33 UTC | #3

[code]if (controls.IsDown(CTRL_LEFT))
        moveDir += Vector3(-0.1f, 0.0f, 0.0f);
    if (controls.IsDown(CTRL_RIGHT))
        moveDir += Vector3(0.1f, 0.0f, 0.0f);
[/code]

Notice you have 0.1f, instead of 1.0f. When you normalize the moveDir vector for a diagonal, the forward/backwards 1.0 will have a huge weighting over the left/right 0.1.

-------------------------

Pellucas | 2017-01-02 01:01:33 UTC | #4

[quote="hd_"][code]if (controls.IsDown(CTRL_LEFT))
        moveDir += Vector3(-0.1f, 0.0f, 0.0f);
    if (controls.IsDown(CTRL_RIGHT))
        moveDir += Vector3(0.1f, 0.0f, 0.0f);
[/code]

Notice you have 0.1f, instead of 1.0f. When you normalize the moveDir vector for a diagonal, the forward/backwards 1.0 will have a huge weighting over the left/right 0.1.[/quote]

oooooooooh my bad!!  :laughing:  thank you so much hd_

-------------------------

