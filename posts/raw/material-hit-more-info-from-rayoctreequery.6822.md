wieszak17 | 2021-04-23 13:54:25 UTC | #1

I have some object in scene with multiple materials. User clicks mouse button so i do rayoctreequery to find out what he hit. Ok, i got reference to that object, but i also need to know which material is at hit point. Something like some paint tools to apply on object's parts defined by material used. How i can get material index on that object?

-------------------------

Modanung | 2021-04-23 14:33:47 UTC | #2

In case of a `StaticModel`, the `RayQueryResult::subObject_` will coincide with the batch/geometry/material index of the model.

-------------------------

wieszak17 | 2021-04-23 14:33:24 UTC | #3

Ok, thanks for info.

-------------------------

