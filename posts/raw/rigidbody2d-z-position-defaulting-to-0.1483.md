miz | 2017-01-02 01:08:05 UTC | #1

I am trying to move a RigidBody2D's z position.

[code]void Player::SetZ(int z)
{
	position.z_ = z;
	playerNode->SetPosition(position);
}[/code]

 But after I do, SetLinearVelocity() seems to force it back to 0. When I do not have SetLinearVelocity it keeps it's z position. But if I do manual movement with something like position+=velocity collisions stop working :frowning:

Anyone know how I could get around this?

Thanks :slight_smile:

-------------------------

thebluefish | 2017-01-02 01:08:05 UTC | #2

RigidBody2D works only on the X/Y axis (hence the 2D). I'm not surprised that attempting to use the Z-axis is not working.

-------------------------

miz | 2017-01-02 01:08:05 UTC | #3

Is there a way then to disable all rotation so that I can use RigidBody a bit like RigidBody2D?

-------------------------

codingmonkey | 2017-01-02 01:08:05 UTC | #4

all "Angular factors" to zero
or/and get world position of rigidbody and project it into some plane.

-------------------------

miz | 2017-01-02 01:08:05 UTC | #5

Oh, I found it. SetAngularFactor(Vector3(0,0,0)) will stop a RigidBody from rotating.

Now I just need to see if I can make 3D rigid bodies collide with 2d ones?..

-------------------------

thebluefish | 2017-01-02 01:08:06 UTC | #6

3D physics and 2D physics are done with two different physics engines, so a RigidBody will never interact with a RigidBody2D. If you need 2D physics in 3D space, you'll want to do everything as 3D physics.

-------------------------

Modanung | 2017-01-02 01:08:37 UTC | #7

...and rigidBody_->SetLinearfactor(Vector3::ONE - Vector3::UP); for a top-down game.

-------------------------

