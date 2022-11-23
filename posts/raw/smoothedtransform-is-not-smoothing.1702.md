bmcorser | 2017-01-02 01:09:35 UTC | #1

I'm playing with the SmoothedTransform component, which looks really sweet.

However, it doesn't appear to be smoothing how I expect it to be. When I call SetTargetPosition here:
[github.com/bmcorser/PolyDraw/bl ... ra.cpp#L99](https://github.com/bmcorser/PolyDraw/blob/140fc357ff1145f0539c2cf4a041f06408cd2d98/ThirdPersonCamera.cpp#L99)
Which in turn is called from here:
[github.com/bmcorser/PolyDraw/bl ... w.cpp#L260](https://github.com/bmcorser/PolyDraw/blob/140fc357ff1145f0539c2cf4a041f06408cd2d98/PolyDraw.cpp#L260)
Then the node i assume is being transformed ([github.com/bmcorser/PolyDraw/bl ... ra.cpp#L30](https://github.com/bmcorser/PolyDraw/blob/140fc357ff1145f0539c2cf4a041f06408cd2d98/ThirdPersonCamera.cpp#L30)) jumps to the target position.

On practicing01's advice I set Scene::SetSmoothingConstant and Scene::SetSnapThreshold both to 0.0001f but this didn't have any effect.

Is there some configuration of the component I am missing, or should I be subscribing to some events that I am not?

-------------------------

Enhex | 2017-01-02 01:09:36 UTC | #2

Does your node have a rigid body? If so setting position doesn't get interpolation because interpolation is done by Bullet using velocity.
If that's the case you could set velocity towards the new position to achieve interpolation.

-------------------------

