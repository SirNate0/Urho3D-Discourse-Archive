Enhex | 2018-04-17 19:46:32 UTC | #1

Is Urho3D fixed update deterministic? Including the physics simulation?
If not what needs to be changed to make them deterministic?

-------------------------

Enhex | 2018-04-17 22:40:26 UTC | #2

So far I noticed `PhysicsWorld::SetInterpolation()` should be set to `false`, otherwise Urho3D feeds Bullet variable timestep.

-------------------------

Sinoid | 2018-04-17 22:37:46 UTC | #3

You have to go x64 only and replace the transcendentals and square-roots with fixed-point or tabled versions (IIRC I was able to find a list). Otherwise Bullet3 is already deterministic on the same machine and it's just those functions that aren't guaranteed to be the same you have to fix.

I did give a whirl using entirely Q32.32 in Bullet and SoftFloat as well. Fixed-point didn't go well, it generally exploded within a few seconds (based on the Allegro stuff for FP). SoftFloat worked but was too slow, slow enough to not even need to profile to know it was dead.

Edit: Forgot SoftFloat is C#, here's a dump of the C++ port I threw together to screw with: https://hastebin.com/xisupixace.cpp

-------------------------

Enhex | 2018-04-18 09:12:49 UTC | #4

In my experimentation disabling interpolation was enough to make the fixed update deterministic.

Do you have links to explanations of all the things you mention? Are they really non-deterministic (same instructions with the same input can give different result?).

Cross-platform/compiler determinism is another issue (because it can potentially compile into different instructions/binary), for example if you want players from different platforms to play together on the same server. Though I haven't looked into it yet.

-------------------------

