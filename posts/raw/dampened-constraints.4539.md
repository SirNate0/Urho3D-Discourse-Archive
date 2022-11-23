HaeferlKaffee | 2018-09-15 20:12:26 UTC | #1

I'm trying to create a smoother physics-style movement controller for a character, one that works well at high speeds on slightly varying surfaces such as terrain, so I'm using a "lifter" body that is always atop the terrain, and a "bumper" body that attempts to be above that lifter at a certain height, and I'm using a point constraint to keep their distance. 
The problem is that the constraints are too sharp, and I need a dampened transition - is there a way to add dampening or friction to constraint solving? I think it's possible in Bullet, but I can't find anything for Urho

-------------------------

Modanung | 2018-09-16 07:21:02 UTC | #2

If it's possible with Bullet, it should be possible with Urho.

-------------------------

