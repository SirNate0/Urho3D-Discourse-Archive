slapin | 2017-01-02 01:14:33 UTC | #1

Hi, all!

A simple question - I have 2 Rects
for example
[code]

Rect r1(-500, -500, 500, 500);
Rect r2(-500, -100, 300, 5);
[/code]

and I need to check if these are intersecting. How to do that in most effective way in AngelScript?
I need it for quadtree implementation.

-------------------------

slapin | 2017-01-02 01:14:35 UTC | #2

For reference - if rectangkes do not intersect, the Clip result will have infinite size.
I.e.
[code]
Rect r1(-1000, -1000,  -500, -500);
Rect r2(500, 5000,  1000, 1000);
r1.Clip(r2);
if (r1.length == M_INFINITY)
    Print("do not intersect")
else
    Print("intersect")
[/code]

So this is a way to test for intersection.

-------------------------

cadaver | 2017-01-02 01:14:35 UTC | #3

Would make sense to add a similar IsInside() overload as for BoundingBox, which would return the intersection result.

-------------------------

slapin | 2017-01-02 01:14:35 UTC | #4

Yeah, I think that would be more logical way.

-------------------------

TheComet | 2017-01-02 01:14:35 UTC | #5

QRect (from Qt) overloads the binary | & and bool operators, which will return a new rect that contains both, a new rect that defines the intersection, and returns true if position and size are not 0, respectively. I feel like those should be added to Urho as well. Checking if they intersect would then look like:
[code]if(r1 & r2) {
    // the two intersect
} else {
    // no intersection
}[/code]

-------------------------

