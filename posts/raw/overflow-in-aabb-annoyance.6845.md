Dave82 | 2021-05-14 10:37:39 UTC | #1

So far everything worked nice when suddenly this annoying message started to ruin my game.
The annoyance happens randomly. Maybe 1 out of 15 runs. The log didn't tell squat about where , why, this happens... Any workarounds or ideas how to fix this ?

-------------------------

SirNate0 | 2021-05-14 16:26:44 UTC | #2

Do you have any custom models that could have extremely large bounding boxes from a bad vertex? Or do you have any objects that may have fallen off the world, effectively, and end up thousands/millions of units away? Could you provide the exact message from the log, it's easier to find where it's coming from that way.

-------------------------

Dave82 | 2021-05-14 18:27:40 UTC | #3

Hi ! The full log is this : 
> Physics: Overflow in AABB, object removed from simulation
> Physics: If you can reproduce this, please email [bugs@continuousphysics.com](mailto:bugs@continuousphysics.com)
> Physics: Thanks.

In the meantime i think i found the problem (Not fully tested yet so not sure) the error comes from uninitialized variable. Specifically the rotation of my btKinematicCharacterController must be set manually to a specific value after the object creation. It seems pretty weird and strange that a library like Bullet has such flaws like unitialized variables... So for now the error is gone but still testing to see if this was the culprit. I will come back after few tests

-------------------------

Eugene | 2021-05-15 05:51:47 UTC | #4

KinematicCharacterController is not really a part of bullet library, more like unsupported example.

-------------------------

JSandusky | 2021-05-16 07:28:33 UTC | #5

Yeah, there's a bunch of stuff in bullet that just detonates. I was recently trying to adapt the raw (not the optimized one) triangle mesh to support animation ... oh dear was that a can of worms and curse words. IIRC I saw this same error tons of times because deformations were changing things and stuff here or there wasn't getting deallocated.

I just scoffed and ran off to physx, never looking back again.

-------------------------

