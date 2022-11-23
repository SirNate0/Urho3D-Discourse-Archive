kmckisicwd | 2019-09-25 22:33:39 UTC | #1

How do you keep a camera or even objects within a certain horizontal distance?

-------------------------

GoldenThumbs | 2019-09-26 03:25:09 UTC | #2

What do you mean? Like, let's say you have a third person camera and you want it to be able to zoom out but only to a certain extent. Is that what you mean? If that's what you mean you could just clamp the distance. That'll let you define a min and a max distance.

-------------------------

Modanung | 2019-09-26 10:06:03 UTC | #3

@kmckisicwd Welcome to the forums! :confetti_ball: :slightly_smiling_face:

Could you indeed elaborate what you are trying to do, maybe with some pseudo-code or a drawing?

You're likely required to familiarize yourself with basic vector math for this (like addition, substraction and the dot product) and maybe `Vector3::Lerp` and `Clamp(T value, T min, T max)`. With it you could calculate the desire position of the camera for the current frame and set it during the `Update` event with `cameraNode->SetPosition(thatVector3)`.

-------------------------

zedraken | 2019-09-27 10:43:44 UTC | #4

My understanding (I might be wrong) is that the camera shall stay at a certain distance from an object whatever the object movements are.
In such a case, you can create the camera node as a child on the object node and set a camera node position relative to that object.
By doing that, the camera will follow the object and the distance between the object and the camera will never change.

-------------------------

