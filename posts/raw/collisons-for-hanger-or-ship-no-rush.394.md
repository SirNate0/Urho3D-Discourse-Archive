vivienneanthony | 2017-01-02 01:00:07 UTC | #1

Hello

I want to try to setup a hanger in a space ship. I was thinking of setting a invisible collision box for the hanger/ship then testing if collision of a character to that box.

Doing a override of the gravity if in the box collision or if not.

Vivienne


This would be useful I think.[quote]
void 	SetUseGravity (bool enable)
 	Set whether gravity is applied to rigid body.
 
void 	SetGravityOverride (const Vector3 &gravity)
 	Set gravity override. If zero, uses physics world's gravity.[/quote]

-------------------------

cadaver | 2017-01-02 01:00:07 UTC | #2

For the collision box, you can make a static (mass 0) rigidbody and collisionshape as usual, then call SetTrigger(true) for that rigidbody. You'll get physics collision events like normally, but because it's a trigger, the box doesn't apply forces to the colliding object, so any objects get freely inside the box. In the collision event handlers, you can then decide how to react. There are separate start, ongoing and end collision events, see PhysicsEvents.h.

-------------------------

