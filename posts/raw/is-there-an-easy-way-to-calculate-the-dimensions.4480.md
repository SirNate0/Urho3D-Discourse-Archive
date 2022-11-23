berrymooor | 2018-08-19 17:03:08 UTC | #1

Is there a simple way to calculate the height, width in pixels of an element (node, billboard...) that it occupies on the physical screen of the device. Something like the 2D bounding box of the element...

-------------------------

Modanung | 2018-08-19 17:31:42 UTC | #2

There is the `Vector2 Camera::WorldToScreenPoint(Vector3)` which you could apply on all points of a `Drawable`'s bounding box (or world position of its vertices for higher precision) after which the extremes of this result multiplied by the screen resolution should give you an approximate screen bounding box.

-------------------------

