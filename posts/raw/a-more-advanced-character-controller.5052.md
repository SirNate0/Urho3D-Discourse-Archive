Leith | 2019-03-29 07:24:50 UTC | #1

I'm unhappy with the character controller in the Sample. It's been around a month since I decided to have a crack at improving it - I opted to use the AnimationController component, rather than deal with driving the animations myself, which it seems was my first mistake, at least with respect to the local player character. My second mistake, it seems to me, was to adopt Dynamic physics as the driver for controlling the player character - in both cases, we get less control, and run into lots of unhandled corner cases.

I'm tempted to scrap my current implementation of character controller, switch to a kinematic controller for the character (which means more work for me on the physics side, at the least), and use a small FSM for animation controller (data driven, of course).

Does anyone have some words of wisdom with respect to controlling non-trivial characters? Especially interested in what you may have to say about root-motions, and velocity-versus-force based motion approaches, but interested generally in hearing about non-trivial control schemes for player characters.

-------------------------

smellymumbler | 2019-03-29 13:46:15 UTC | #2

https://discourse.urho3d.io/t/dynamic-kinematic-character-demo/3625
https://discourse.urho3d.io/t/character-controller/1468/2
https://discourse.urho3d.io/t/kinematic-character-control-with-bullet/3791
https://discourse.urho3d.io/t/kinematic-character-controllers/3555
https://github.com/hdunderscore/Urho3D-FPS-Controller

-------------------------

Leith | 2019-03-30 04:33:07 UTC | #3

Hey thanks man, I processed all that, and unfortunately I am no better off - a wider search online for decent character controllers also turned up empty.

I think I should start by deriving a new AnimationController, one that operates as a finite state machine, and understands conditional state transitions. Once I'm happy with that, I can look at implementing a kinematic character controller, combined with a dynamic ragdoll rig.

Our AnimationController is a manager for AnimationStates. But hardcoding logic switches on top of it is not as flexible as a data-driven approach.

-------------------------

