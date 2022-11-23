rku | 2017-08-24 16:08:04 UTC | #1

How do i render some debug primitives on top of UI? I believe i somehow should convert result of `UIElement::GetScreenPosition()` to world coordinates and feed it to say `AddQuad()` bit it is not really clear to me. Help would be greatly appreciated. Thank you.

-------------------------

Enhex | 2017-08-14 13:49:40 UTC | #2

You might find this useful to convert screen space to world space:
https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_camera.html#abe7e6dda9b61ee392a557fe5f05fa7ad

-------------------------

rku | 2017-08-24 16:07:58 UTC | #3

After some digging turns out its `Viewport::GetScreenRay().origin_`. Not exactly obvious.

-------------------------

