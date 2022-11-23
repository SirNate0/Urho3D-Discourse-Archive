Eugene | 2017-05-19 21:57:55 UTC | #1

I have some problem with animation synchronization: it is sligthly trembling.
I can't reproduce it in examples, probably this trembling is just too small.
Consider the following scene: Character is moving forward (in X+ direction) with walk animation (with e.g. Period=1), camera is static.
**Chrarcter is moving forward during fixed update**
It is obvious that animation time and character position are connected: `time = fract(X/speed)`

Let's take a look on timing:
FixedUpdate times are incremented every 1/60 second:
`[0; 0.0166; 0.0333; 0.05; 0.0666; 0.0833; ...]`
Chrarcter's X positions are incremented every 1/60 second too:
`[0; 0.1; 0.2; 0.3; 0.4; 0.5; ...]`
Example frame times:
`[0; 0.021; 0.04; 0.059; 0.082; ...]`

Frame at 0.04 is rendered in the following way:
Character is at X=0.2 (this position was set during fixed update at 0.0333)
So, character's "true" animation time is 0.0333 (see formula above).
But animtion is updated during non-fixed update, so real animation time is 0.04.

So, animation gets non-synchronized, and small trembling is visible when foot is grounded.

Any ideas how to synchronize animations? Let's suppose that I can't make updates non-fixed.
I've temporarily made animation update during fixed update too, but it is not the best solution IMO.

-------------------------

Modanung | 2017-05-19 23:59:20 UTC | #2

Fixed update is where you should update physics (apply forces and the like). If you're not using physics to move your nodes, you're best off using the ordinary update since it's synchronous with the graphical update.

-------------------------

Eugene | 2017-05-20 08:11:41 UTC | #3

Example characters are driven by physics, so I emulated the same situation.

-------------------------

slapin | 2017-05-20 15:03:17 UTC | #4

Update might make fun of you if you don't use physics but would like to do something spread at regular intervals, if you run on slow or loaded device. So for continuous process I'd stick to FixedUpdate,
but do not abuse it.

-------------------------

slapin | 2017-05-20 15:05:25 UTC | #5

Please show your motion code. I think it is the source of a problem.

-------------------------

Eugene | 2017-05-20 21:00:11 UTC | #6

*My* code doesn't have anything interesting:

    void FixedUpdate(float timeStep)
    {
        const float walkSpeed = 1.5;
        node.worldPosition = node.worldPosition + Vector3(1, 0, 0) * timeStep * walkSpeed;
    }

-------------------------

Modanung | 2017-05-21 08:55:36 UTC | #7

Exactly: This is _not_ using physics and should be handled within `Update`, not `FixedUpdate`.

-------------------------

Eugene | 2017-05-21 11:44:36 UTC | #8

[quote="Modanung, post:7, topic:3137"]
This is not using physics
[/quote]
Why? It _is_, actually, very limited physics.
If I add gravity and acceleration later, I won't be able to use Update instead of FixedUpdate because I want stable computation.

-------------------------

Modanung | 2017-05-21 20:24:49 UTC | #9

Let me explain with more words...

You are not using the Physics Subsystem with accompanying PhysicsWorld and RigidBody, which update with a fixed interval. In a situation where you _would_ be using these built-in Bullet physics the node transform is interpolated based on the physics simulation. So even there the node position would be updated every frame to avoid this trembling, while saving resources by updating the physics simulating with a fixed interval.

Also...
Physics: M'ass ;)
> **F = m * a**

-------------------------

Eugene | 2017-05-21 16:01:45 UTC | #10

Actually, I didn't thought that way... Somewhy I thought that physics
itself doesn't do any interpolation between steps.
Great, thank you!

-------------------------

Mike | 2017-05-21 19:44:49 UTC | #11

You can also set body to kinematic when you want to 'manually' update node position instead of moving it through physics simulation.

-------------------------

