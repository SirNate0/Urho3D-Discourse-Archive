HaeferlKaffee | 2019-07-04 14:38:05 UTC | #1

I'm essentially using the implementation here:
[https://discourse.urho3d.io/t/kinematic-character-controllers/3555](https://discourse.urho3d.io/t/kinematic-character-controllers/3555)

It works fantastically other than that if you want a velocity-based movement system, you can't use Bullet's internal "velocity" (.setLinearVelocity(), etc.), and must use *setWalkDirection()* instead, otherwise the character won't 'step' over objects.

My solution has been to define a velocity variable in my implementation the controller, accelerating in the input direction with some maths to create friction when grounded and limit acceleration based on Quake's dot-product method.

The problem is that if this character hits an angled wall (say a small wall at 45° to the direction of the controller's velocity), no absorption/restitution/friction occurs, and they simply slide along the wall then continue in their original direction. Collisions are obviously not able to affect the velocity because it's in my implementation, but even if I use setLinearVelocity(), which again is not ideal due to not stepping, it still ignores these collisions.

Ideally without changing Bullet's library code, how can I add a function/listener that handles the collisions made by the controller's ghost object? Adding a collision callback like with rigid bodies in Urho3D doesn't work (It simply doesn't recognise the collisions). **Is there a way to add a callback for Bullet's collisions?**

---------------------------------------- 
EDIT:
*(Currently I'm using a large sphere, a child of the controller, that detects collisions and applies a repulsive force to cancel out the velocity in that direction, which works sometimes but fails are high speeds because it's not in the same place as the ghost object - bit of a headache. Also, using a sphere larger than the capsule collider of course causes issues at low speeds where the player is prevented from moving in a certain direction even though the capsule isn't actually touching the wall, but the sphere is.)*

    // node_ has a btKinematicCharacterController implementation attached.
    SubscribeToEvent(node_, E_PHYSICSCOLLISIONSTART, URHO3D_HANDLER(CrabCharacterController, DebugGhostCollision));
    
    ...
    
    void CrabCharacterController::DebugGhostCollision(StringHash eventType, VariantMap& eventData) {
        using namespace PhysicsCollisionStart;

	    RigidBody *rb1 = (RigidBody*)eventData[P_BODYA].GetPtr();
	    btTransform t;
	    rb1->getWorldTransform(t);
	    if (t == ghostObject_->getWorldTransform()) {
		    int done = 1;               // Breakpoint here, just to test if the event rigidbody is the same as the ghost object, not efficient but just to test
	    }
    }

-------------------------

Leith | 2019-07-05 05:38:18 UTC | #2

Hi! Yes I ran into this one too... I addressed exactly this issue recently, you are welcome to use it and change it any way you like :slight_smile:

[quote]
https://discourse.urho3d.io/t/support-for-ghostobject-collision-events/5215
[/quote]

If you need more help, that's cool too, just yell out if you get stuck.

-------------------------

Leith | 2019-07-06 04:24:03 UTC | #3

with respect to high speed tunneling bugs, turn on ccd - instead of instant position testing for collisions, we will use quadratic equations, swept tests, extrusions of the moving shape over time - in my opinion, any modern physics engine should DEFAULT to using CCD in collision tests, and never call the instantaneous "query" tests, which we reserve for specific queries outside of the physics step

-------------------------

