Dave82 | 2017-01-02 01:07:23 UTC | #1

Hi it seems that if i remove some rigid bodies from simulation , they are still cached/referenced on other rigid bodie's list , which leads to a crash if you try to access them before next physics update

[code]rigidBody1->Remove();

// if rigidBody2 was in collision with rigidBody1 previously , the list is invalid because rigidBody's pointer is still on the list...
rigidBody2->GetCollidingBodies(list);[/code]

Just an idea : maybe storing the colliding bodies as a [b]PODVector<SharedPtr<RigidBody> >[/b] could solve the problem

-------------------------

cadaver | 2017-01-02 01:07:23 UTC | #2

SharedPtr would keep the bodies alive until the next tick, which is not wanted.

Will have to test this. It's already iterating a structure of WeakPtr's held inside the PhysicsWorld component.

-------------------------

cadaver | 2017-01-02 01:07:25 UTC | #3

According to my test it was returning a null pointer on the list if the body taking part in collision was already destroyed. This is now fixed in the master branch. I didn't observe it returning dangling but non-null pointer to a destroyed body.

-------------------------

