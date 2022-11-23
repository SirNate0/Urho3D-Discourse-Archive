esakylli | 2017-03-24 15:16:07 UTC | #1

I have a hinge constraint between two bodies, with a 360 degrees free rotation (limit is set to [-180,180]) round the y-axis.
I rotate one of the bodies via ApplyTorque().
Now I want to lock/freeze the body/constraint in it's current angle.
I have tried setting the limit (both Low and High) to the body's current y-axis rotation.
This seems to work at first, but after some more rotation the body seems to "snap" some degrees wrong.
I think it's because the other body has rotated some of it's own, but I'm not sure.
Any help on this matter would be much appreciated.

-------------------------

esakylli | 2017-03-24 15:16:15 UTC | #2

It seems that the mistake I made was that I didn't take the angle difference between the two bodies.

-------------------------

