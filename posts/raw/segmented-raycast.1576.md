Enhex | 2017-01-02 01:08:37 UTC | #1

In my project I noticed that if I have a big scene with a lot of bodies (100's) a raycast from one end of the level to another becomes very expensive (in my case AI line of sight check).
I assume that the raycast implementation uses AABB to get all the bodies it needs to test against for intersection.
A possible way to optimize it is to segment the ray into several rays, so the sum of the volumes of the smaller AABBs is smaller than the single big AABB, so it will test against much less bodies.
In the case of returning the closest result, when a ray segment hits something there's no need to test the rest of the segments.
[img]http://i.imgur.com/On8MNSg.png[/img]

Since it's quite a general case (any big scene with many bodies), if I implement it would u accept a pull request?


EDIT:
I implemented it and in my case it [b]more than doubled[/b] the game framerate, and the performance relation is non-linear.

Made a pull request:
[github.com/urho3d/Urho3D/pull/1093](https://github.com/urho3d/Urho3D/pull/1093)

-------------------------

cadaver | 2017-01-02 01:08:38 UTC | #2

Certainly, it will be added.

-------------------------

Enhex | 2017-01-02 01:08:41 UTC | #3

Only PhysicsWorld::RaycastSingleSegmented(), a version of RaycastSingle, was part of the PR.

A RaycastSegmented should have 2 versions:
- One that returns all the intersections
- One that for each segment passes the results to a callback, and that callback can abort the rest of the segments by returning false.


The second version is useful for things like "RaycastSingle" that filters specific nodes, instead of using layer = 0 that will cause the body to be re-added to world.
Another example is getting the first N nodes.
Another example is penetrating bullets.

-------------------------

