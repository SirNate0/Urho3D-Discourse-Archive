rifai | 2018-04-14 12:41:27 UTC | #1

I have several nodes with rigidbody. I want to "join" them as one object. 

A quick search on Bullet forum, I found the solution is using Fixed Constraint. But, Urho3d don't have the implementation of this constraint. Do anyone know alternative solutions?

-------------------------

Enhex | 2018-04-14 12:54:28 UTC | #2

Urho does have constraints.
Also if u just want to combine the shapes into a single rigid body you can create compound shapes.
read:
https://urho3d.github.io/documentation/HEAD/_physics.html

-------------------------

rifai | 2018-04-14 13:21:58 UTC | #3

Oh, I didn't know we can use several shapes. :rofl:
Thank you, this is what I'm looking for.

-------------------------

