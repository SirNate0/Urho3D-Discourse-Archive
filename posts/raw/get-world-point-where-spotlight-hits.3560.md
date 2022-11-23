nergal | 2017-09-12 11:49:04 UTC | #1

Is there a way to get the point in the world where a spotlight (LIGHT_SPOT) hits an object? And if not hitting an object, I would like to have the point where the spotlight ends when I've defined "SetRange(x)" for the light. 

If so, it would also be good if I could get the actual object being hit.

-------------------------

Modanung | 2017-09-12 12:33:46 UTC | #2

You'd probably want to use an octree raycast, as happens in several samples:
https://github.com/urho3d/Urho3D/blob/master/Source/Samples/08_Decals/Decals.cpp#L295

Instead of the `cameraRay` you would have a ray starting at the position of the spotlight with a `maxDistance` equal to the light's range.
Once you have a `RayQueryResult` you've got a `Node` which you can check for tags or derived components as well as the position where the ray hit.

-------------------------

nergal | 2017-09-12 12:32:01 UTC | #3

Thanks! Worked like a charm!

-------------------------

