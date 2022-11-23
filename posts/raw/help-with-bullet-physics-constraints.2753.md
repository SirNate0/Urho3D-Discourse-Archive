esakylli | 2017-01-28 12:21:03 UTC | #1

I'm having some problems with Bullet physics constraints.
My scenario is the following:

I have body A and diagonally up to the left on top of it I place body B, through a hinge-constraint.
Now I want to rotate both round the Y-axis:
If I rotate A I want B to rotate along with it, in it's position relative to A.
If I rotate B I want it to rotate round it's own position, without affecting A.

The problems I got when rotating A are:
It doesn't rotate around it's own position, instead it rotates around the constraint's position (where B is located).
Body B doesn't follow along A's rotation, instead it sit's still in it's original position.
When I rotate B it works as expected, it rotates around it's own position (without affecting A).

I would appreciate any help round this matter.

-------------------------

Modanung | 2017-01-28 14:08:46 UTC | #2

Sharing the relevant code would probably help you in this case.

-------------------------

