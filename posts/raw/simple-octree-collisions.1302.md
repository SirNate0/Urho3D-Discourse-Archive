sabotage3d | 2017-01-02 01:06:41 UTC | #1

Is there a way to do simple octree collisions as a fail-safe in case bullet physics penetrate an object ?

-------------------------

cadaver | 2017-01-02 01:06:42 UTC | #2

You can do raycasts and volume-based queries (AABB, sphere, frustum) into the octree, and it will return Drawables. Otherwise than that collisions are not explicitly supported; the Octree is meant to accelerate rendering and do tasks related to it (finding out objects in frustum, light influences etc.)

Note that only raycasts can be configured to be per-triangle, the volume queries test the query volume vs. the drawable AABB's.

-------------------------

Bananaft | 2017-01-02 01:06:42 UTC | #3

If you have a tunnelling problem, you should try more common ways to fight it:

1) Continuous collision detection. Search for it on this page: [urho3d.github.io/documentation/1 ... ysics.html](http://urho3d.github.io/documentation/1.32/_physics.html)
2) Using primitives and convexes for static collision shapes. If your level geometry is simple enough to be outlined by primitives.
3) Caping velocity and making sure your object's won't fly around at such ridiculous speeds, to move it's entire length in one physics step.

-------------------------

