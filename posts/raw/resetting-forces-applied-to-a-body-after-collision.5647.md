zedraken | 2019-10-04 09:11:48 UTC | #1

Dear all,
I am currently facing a little problem for which you may have some tips.
I have two objects which have both a rigid body with a non null mass and a bounding box collision shape.
One object is moving toward the second one which is not moving.
When the collision occurs (it is correctly detected), the non moving object is thrown away by rotating on himself is all directions (its mass is much lower than the one of the moving object).
For now, everything seems to work fine.
What I want to achieve is to cancel all forces applied to the second object simply by pressing a key on my keyboard.
For that, in my keydown handler, I tried to call several functions like this:

`body->ResetForces();` 

with no effects. The second object is still moving and rotating after the collision.

I have also tried:

`body->SetRotation(Quaternion::IDENTITY);`

no more results…

`body->ApplyForce(Vector3::ZERO);`

no success.

I also tried to cancel operations applied on the object node like that:

`node->SetRotation(Quaternion::IDENTITY);`
`node->SetWorldRotation(Quaternion::IDENTITY);`

nothing seems to be able to reset all forces/transform applied to either the body or the node.

It would be very helpful if you can provide me with some tips to get closer to the solution.

Thanks a lot!

-------------------------

PsychoCircuitry | 2019-10-04 18:30:11 UTC | #2

I haven't tried it to test, but I think you may want to use SetLinearVelocity and SetAngularVelocity on the rigid body you want to stop. Setting both to Vector3::ZERO I think will stop it. Hope that is of some help.

-------------------------

zedraken | 2019-10-04 18:29:31 UTC | #3

That's it! I did not think at those two functions. So I made a test and by setting angular and linear velocities to ZERO, everything goes as expected, the body does not move or rotate anymore.
Thanks a lot for the help!
Regards.

-------------------------

