suppagam | 2019-12-19 22:53:24 UTC | #1

It's my first time creating a ragdoll and I'm confused about the process of setting limits and weights. For example: how can I tell the system not to rotate the arm so much that it looks like it is broken? Can ragdolls respect Foot IK? 

As for weights, how can I tell it that left arm is lighter than left leg, and both are lighter than torso?

-------------------------

Modanung | 2019-12-19 22:52:32 UTC | #2

1. Indeed it would be nice to have a (better) visual editor for this
2. Physics and IK should not operate on the same node, I think
3. The mass can be set on the `RigidBody`s

-------------------------

suppagam | 2019-12-20 14:46:19 UTC | #3

Thanks for the answer! Regardless of having an editor or not, is it possible to set those limits? If so, how? 

As for Physics and IK not operating on the same node, what do you mean? Physics can't respect the IK rules on a skeleton?

-------------------------

Modanung | 2019-12-20 14:58:42 UTC | #4

As I understand it, IK is meant to override skeletal animations to make them fit the environment. Both directly modify node transforms, which would conflict with a physics simulation. There are conceivable workarounds, but one might not call them trivial.
You could - for instance - use the IK to determine a transform _target_ and implement any joints in the skeleton as motors. That would work. But it's easier to separate your graphics from the physics.

[quote="suppagam, post:3, topic:5776"]
is it possible to set those limits?
[/quote]

The ragdoll sample uses different constraints to limit the movement of limbs, did you take look at that?

-------------------------

