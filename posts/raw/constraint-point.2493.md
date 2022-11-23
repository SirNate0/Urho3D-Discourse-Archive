slapin | 2017-01-02 01:15:47 UTC | #1

Hi, all!

Have anybody tried using point constraint?
It looks like there is some bug - constraint_ field is always NULL
and everything is silently ignored except warning about worldPosition.
All other constraints (hinge, conetwist, slider) do not have this problem.

-------------------------

godan | 2017-01-02 01:15:47 UTC | #2

Yep, I agree that this constraint does not seem to be working properly. I can get the rigid bodies moving, but no constraint interaction at all as far as I can see.

Also, what exactly is this thing supposed to do? My understanding is that, given two rigid bodies and two local frames, this constraints creates a spring between them (thus keeping them a certain distance apart). Is that right? If so, perhaps it should be renamed to Spring or Length constraint?

-------------------------

Mike | 2017-01-02 01:15:48 UTC | #3

It's Bullet 'Point to Point' constraint, hence its name in Urho3D.
It features rotation around the pivots, and no translation.
It works perfectly and can be used for example as a mouse picker, as demonstrated in Bullet demos.

-------------------------

slapin | 2017-01-02 01:15:48 UTC | #4

Well, it probably works in Bullet but definitely doesn't work in Urho as constraint_ is always NULL.

-------------------------

jmiller | 2017-01-02 18:19:38 UTC | #5

I'm using CONSTRAINT_POINT and it constrains correctly for me. Without it, the body is not constrained. I'm not sure why constraint_ (btTypedConstraint*) is NULL. Maybe someone can clarify.

-------------------------

