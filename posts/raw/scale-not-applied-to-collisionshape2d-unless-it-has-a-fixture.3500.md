ricab | 2017-08-28 17:13:16 UTC | #1

CollisionShape2D does not reflect the right scale when a the following sequence of operations is applied:

1. create collision shape (e.g. box) in node N
2. scale node N
3. create collision body in node N

Some superficial testing seems to indicate this can be fixed by removing line [CollisionShape2D.cpp:323](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Urho2D/CollisionShape2D.cpp#L323)

Does anyone know of a reason why that shouldn't be done? Notice that the fixture is still checked for nullptr whenever it would be affected. Having the check outside prevents the shape from being updated though.

-------------------------

