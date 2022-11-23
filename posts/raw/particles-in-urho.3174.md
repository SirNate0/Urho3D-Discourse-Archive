smellymumbler | 2017-05-29 13:59:41 UTC | #1

Since Urho doesn't seem to have a particle editor, how would you guys implement a simple particle system like this one?

https://www.youtube.com/watch?v=Jz4CFst2pKA

Or maybe this one:

https://www.youtube.com/watch?v=u8GK2oGerrM

-------------------------

Enhex | 2017-05-29 10:41:35 UTC | #2

Urho3D got a basic particle editor in its editor:
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/3e6105e908b3dd73ffc22a0d9715d8867e131c7e.png'>

-------------------------

smellymumbler | 2017-05-29 14:23:10 UTC | #3

Can particles be affected by physics?

-------------------------

Modanung | 2017-05-29 17:36:37 UTC | #4

Not as such. You can set a constant force, which _can_ be modified during runtime. But that's about it.
Bouncing off surfaces would require extra code at this point.

Other things the particle system would need to be awesome are, in my opinion:

- Random texture from the set for newly spawned particles
- Spline curves for more control over parameters

-------------------------

