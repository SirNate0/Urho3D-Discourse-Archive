burt | 2018-02-14 14:54:39 UTC | #1

I've been trying to make a particle bounce off the floor without much luck. Is it possible to have gameobjects, affected by physics, act as a particle system? Is there a way I can link them?

-------------------------

Eugene | 2018-02-14 15:36:28 UTC | #2

There is fork with SPARK particle engine integration. AFAIK it has colliders (static, probably) for particles.

Unfortunatelly, underlying Bullet Physics doesn't support true physical particles. Although, it may be possible to emulate particles even in Bullet, but I never tried it.

-------------------------

burt | 2018-02-16 23:07:54 UTC | #3

Never heard of that engine before, thanks a lot. For the curious:

https://www.gamedev.net/forums/topic/519900-spark--free-opensource-particle-engine-in-c/
https://www.youtube.com/watch?v=F1sTQ2oMdSM

The only thing I couldn't find is an up-to-date documentation. But it looks great!

-------------------------

