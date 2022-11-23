Leith | 2019-03-14 04:56:39 UTC | #1

What is the best Urho3D event to "override the transform on bullet dynamic rigidbodies" in order to align them to the animated skeleton?

Kinematic bodies stick to my animated models like they were glued there, its really cool.
But under Bullet, kinematic objects don't get "restitution", or even "penetration correction" when collisions occur with anything else. Kinematic bodies are rarely useful! I need to drive dynamic bodies, with constraints would be a bonus

-------------------------

Modanung | 2022-01-11 13:44:53 UTC | #2

Kinematic bodies are ideal for triggers, which are not uncommon in games. And in general one should not expect behavior after explicitly disabling it. ;)

Maybe you could use point constraints? Also, how far are you planning to take this physical walking? You seem to be taking it further than IK. Will your zombies need a sense of balance? Maybe the animations could provide a reference for simulated muscles that would apply forces to the limb bodies instead of them being kinematic? Will you still need pre-made animations in the end? Or are you working towards something like...

[<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/b/bd6d930d0c2b2fbfee671029c41336b5de66931b.gif' alt='Bridge walk'>](https://invidious.kavin.rocks/embed/pgaEE27nsQw)

-------------------------

Leith | 2019-03-15 06:17:55 UTC | #3

@Modanung
I'm looking to create a hybrid controller, which has some IK, but stops short of full-body IK, and joint-motor velocity corrections.. the plan is merely to provide additive blending of poses generated from partial ragdoll chains and the animated pose.

-------------------------

Modanung | 2019-03-15 07:38:28 UTC | #4

What makes physics so important for this purpose?

The IK sample uses the `SceneDrawableUpdateFinished` event to apply IK, btw.

-------------------------

Leith | 2019-03-15 08:03:18 UTC | #5

Physics is important to me, I want full ragdolls (the easy part), and partial ragdolls, to inherit the momentum implied by the animated state they were in at the time they switched to ragdoll mode.
I want to be able to use a blend-solver to recover from full ragdoll mode, by determining poses for the physics objects based on the animated skeleton state and the motionstate offsets.
I want the simulator to deal with twitch animations resulting from hitting an animated ragdoll - not additive blending of canned animations. 

Yep, that's what I use for IK and foot-slipping - I assumed that animation would have been performed at this point, and I have a last chance to transform things, but so far, I get some strange results :)

-------------------------

