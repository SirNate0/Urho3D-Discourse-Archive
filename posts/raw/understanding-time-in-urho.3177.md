smellymumbler | 2017-05-30 13:14:55 UTC | #1

Unity has a global Time object that people use extensively across their code. It has a few concepts that i'm finding very hard to grasp in Urho:

https://docs.unity3d.com/ScriptReference/Time.html

* **deltaTime**: The time in seconds it took to complete the last frame
* **smoothDeltaTime**: A smoothed out Time.deltaTime
* **time**: The time at the beginning of this frame. This is the time in seconds since the start of the game.

In Urho, when you have a component, you get a float called timeStep in the FixedUpdate() and Update() classes. That timeStep is the number of seconds since the beginning of the frame? Or is it the time it took to complete the last frame? What would be the equivalent in Urho to those Unity variables?

-------------------------

Pencheff | 2017-05-31 08:41:04 UTC | #2

The analog in Urho3D would be [Urho3D Time](https://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_time.html), available as a subsystem. 

**deltaTime** -> not sure there's exact analog

**smootDeltaTime**:[code]float smoothDeltaTime = GetSubsystem<Engine>()->GetNextTimeStep();[/code]
**time**: [code]float time = GetSubsystem<Time>()->GetTimeStep();[/code]

In Update(), timeStep is the the same as smoothDeltaTime. I'm not sure about FixedUpdate(), judging by the code in PhysicsWorld.cpp, it is **float internalTimeStep = 1.0f / fps_;**, that is if you run physics at 60fps, it would be 16.667ms :)

-------------------------

