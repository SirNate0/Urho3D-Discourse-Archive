k7x | 2018-11-10 08:59:47 UTC | #1

Hi.

Is the easy way to get angle between points like Vector2(0, 0) and Vector2(3, 3) ?

-------------------------

orefkov | 2018-11-07 18:01:46 UTC | #2

Dot product of normalized vectors is cosine of angle between them.

-------------------------

JTippetts | 2018-11-07 18:39:19 UTC | #3

As @orefkov indicated, dot product gives you the angle between two vectors. Your example here, though, with one of the points being Vector2(0,0) indicates you might actually be looking for the angle of the line formed by the two points. In this case, a solution would be to subtract the first point from the second, then use [Atan2](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Math/MathDefs.h#L143) on the result Vector2's components (x,y) to calculate the angle of the line.

    Vector2 A(0,0), B(3,3);
    Vector2 C=B-A;
    float angle=Atan2(C.y_, C.x_);

-------------------------

k7x | 2018-11-08 14:48:25 UTC | #4

Thank you so much. I have already spent several nights solving this problem. Thank !

-------------------------

