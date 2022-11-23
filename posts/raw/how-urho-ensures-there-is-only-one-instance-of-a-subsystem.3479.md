Bananaft | 2017-08-22 21:55:40 UTC | #1

I wrote two custom components,  one is a node component and another is the scene component. Let's name them myBody and myWorld, kinda like PhysicsWorld that takes care of all collision shapes and rigid bodies, myWorld takes care of all myBodies. And just like in RigidBody.cpp, myBody uses GetOrCreateComponent to register into myWorld.

Problem is, I sometimes getting multiple instances of myWorld and it breaks everything. Did I missed something in registration process? Can anyone hint me on how Urho does this check for its native subsystems?

-------------------------

slapin | 2017-08-22 22:26:52 UTC | #2

I wonder why you try to create multiple instances of component which should not be there...
But in case you want to debug this, you can create static class member counter and increment it in constructor.
And check thatthe resulting value is not > 1 (you also need to disable copy-constructor). In that case you can assert exit your app like abort() and get backtrace of the result.

-------------------------

slapin | 2017-08-22 22:25:57 UTC | #3

Also I need to note that you CAN create multiple components of anything in Urho in any node, unless specially protected
against.

-------------------------

cadaver | 2017-08-23 07:27:28 UTC | #4

Urho actually does not have checks for protecting against multiple subsystems. From what I remember, if you were to do it at the Context-level, the old subsystem would just be thrown out. For the scene subsystem components, there likewise is no checks (as recovery options are not obvious, should it delete the old one, crash, complain, or what?) so it's just a programmer error you should avoid.

-------------------------

Bananaft | 2017-08-25 08:51:02 UTC | #5

Thank you for clarification.

First of all it should complain, then replace old or do nothing. Both will work for me. I will probably write my own check for scene subsystem.

-------------------------

