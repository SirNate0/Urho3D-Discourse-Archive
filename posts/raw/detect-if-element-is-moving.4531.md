darkowic | 2018-09-11 20:26:12 UTC | #1

Hello!

I am writing a simple billiards game. I want to detect if an element is moving or it just has stopped. Basically, I want to check if an element has kinematic energy. Is there any method in the engine for checking this?

I am asking because I see that collision shape is changing color in debug mode when my object stops moving.

Thank you :slight_smile:

-------------------------

darkowic | 2018-09-11 20:33:36 UTC | #2

Yeah - RigidBody->GetLinearVelocity is what I need probably :stuck_out_tongue:

-------------------------

Modanung | 2018-09-11 23:55:50 UTC | #3

Note that:
a) LinearVelocity is a `Vector3`, you can use its `Length()` as a velocimeter.
b) Alternatively could use `RigidBody::IsActive()` in your situation which will return true if either its linear _or_ angular velocity are above their respective thresholds.
c) Welcome to the forums! :confetti_ball: :)

-------------------------

TheComet | 2018-09-12 16:40:28 UTC | #4

Also note that if you don't actually need the length but a metric to compare against, use Vector3::LengthSquared() to save a call to sqrt()

-------------------------

darkowic | 2018-09-12 17:08:28 UTC | #5

My game is just a simple learning project and I didn't measure the performance of LengthSquared but comparing Vector to Vector::ZERO should not be much slower and maybe it is even faster :thinking: I am rather new to cpp and it is not the time for optimization :smile: Anyway both solutions will work just fine :slight_smile:

-------------------------

