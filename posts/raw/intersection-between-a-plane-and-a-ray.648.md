Vivek | 2017-01-02 01:01:52 UTC | #1

I am trying to build a to drag a 3d model over a plane. How do i find the intersection point between a ray cast and virtual plane.
I have not found any rayscene query for a virtual plane.

-------------------------

cadaver | 2017-01-02 01:01:52 UTC | #2

You should be able to use this member function in Ray. It returns the distance along the ray, from which you can calculate the hit position.

[code]
/// Return hit distance to a plane, or infinity if no hit.
float HitDistance(const Plane& plane) const;
[/code]
Note that on AngelScript you'd need to pull the latest master, binding for that function was missing and was just added.

-------------------------

Vivek | 2017-01-02 01:01:54 UTC | #3

works, thank you

-------------------------

