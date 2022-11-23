smellymumbler | 2017-03-14 04:28:12 UTC | #1

Does anyone recommend any good C++ tweening library?

-------------------------

Modanung | 2017-03-14 14:54:51 UTC | #2

[ValueAnimations](https://urho3d.github.io/documentation/1.6/_attribute_animation.html) won't do?

-------------------------

WangKai | 2017-09-09 12:35:59 UTC | #3

I just improved the camera of the editor. Actually CubicOut easing is used. I think it's very useful if we have a tweening library. Actually, it's only one file of code large. Additionally, Urho has 2D, so it's necessary.

Edit: for Urho 2D, tweening is essential.

-------------------------

johnnycable | 2017-09-08 19:45:39 UTC | #4

Something like http://robertpenner.com/easing/ ?

-------------------------

WangKai | 2017-09-09 12:33:53 UTC | #5

Yes, definitely. I have already used CubicOut in https://github.com/urho3d/Urho3D/pull/2115

-------------------------

