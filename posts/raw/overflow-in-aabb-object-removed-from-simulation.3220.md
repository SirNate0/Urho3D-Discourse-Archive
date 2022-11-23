redmouth | 2017-06-07 02:58:34 UTC | #1

06-07 02:56:13.468 4871-4900/ W/Urho3D: Physics: Overflow in AABB, object removed from simulation
06-07 02:56:13.468 4871-4900/ W/Urho3D: Physics: If you can reproduce this, please email bugs@continuousphysics.com
06-07 02:56:13.468 4871-4900/ W/Urho3D: Physics: Please include above information, your Platform, version of OS.
06-07 02:56:13.468 4871-4900/ W/Urho3D: Physics: Thanks.


Any suggestion to avoid this?

-------------------------

Eugene | 2017-06-07 09:47:02 UTC | #2

Any STRs for this bug?

-------------------------

redmouth | 2017-06-07 10:28:19 UTC | #3

what do you mean by STRs

-------------------------

Eugene | 2017-06-07 11:27:31 UTC | #4

I mean steps to reproduce this problem

-------------------------

jmiller | 2017-06-08 15:13:37 UTC | #5

I have seen this occur when a CollisionShape (I think I was using box) is created with very large scale and collides, 
*presumably with too many other shapes; in the case I observed, it might have been colliding with a large number of CustomGeometry shapes. Maybe there is a Bullet build option that can increase a limit.

-------------------------

