Enhex | 2017-01-02 01:08:00 UTC | #1

Hi,

I updated to HEAD and my character controller broke, and the log says:
WARNING: Physics: Overflow in AABB, object removed from simulation.

(My character controller ISN'T based on the character demo)

Anyone knows what can cause it, and how to fix it?

-------------------------

Enhex | 2017-01-02 01:08:01 UTC | #2

Found the problem:

The reason was that BoundingBox default constructor changed to use infinities, to mark invalid AABB, instead of zero values.
That caused my recovery from penetration code to merge penetrations into an invalid AABB instead of starting with zeroed one.

That's kinda weird because max = -inf and min = inf, so shouldn't merging points into it create a valid AABB and still work?

-------------------------

