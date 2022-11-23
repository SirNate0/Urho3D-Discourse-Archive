NiteLordz | 2017-01-02 01:13:06 UTC | #1

I am trying to anchor a 3D model to the top right corner of the screen.  I can get it in the position i want, so that when i rotate the camera and move, it stays in the same location, however, if the window is resized, the model will eventually go off screen, not desired outcome.

I referenced the Character demo, and was thinking similar to how the third person camera works, however, this isn't the complete solution.

The below code puts the model in the corner, but only for the current resolution, and doesn't scale it properly.

[code]Vector3 aimPoint = cameraNode_->GetPosition() + cameraNode_->GetRotation() * Vector3(0.66f, 0.33f, 1.0f);[/code]

Thanks in advance

-------------------------

1vanK | 2017-01-02 01:13:06 UTC | #2

Camera::ScreenToWorldPoint()
Viewport::ScreenToWorldPoint()

And refresh pos of 3D object in Update()

-------------------------

1vanK | 2017-01-02 01:13:06 UTC | #3

Or you can calculate the position once and attach aim to camera node as chield (but u need recalculate position when resolution is changed)

-------------------------

NiteLordz | 2017-01-02 01:13:06 UTC | #4

Thank you sir!

Worked like a charm

-------------------------

