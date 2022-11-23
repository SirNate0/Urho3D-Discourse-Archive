freever | 2020-06-22 22:32:00 UTC | #1

Hi folks

I am building a scene in which a player is on a planet. The planet is an icosphere built using a subdivided icosahedron with a radius set to the planet's radius, and sampled so that only the area around the player's location is rendered. 

To place the player on the surface of the planet, I move the camera outwards from the origin to the surface of the planet and then rotate it so that the player is looking along the surface rather than towards the origin:

![image|690x344](upload://kcqmgHxcpRnxaweXZ5u8KkU5f30.png) 

The problem now is that the player's "root" visual fram of reference is not the same as the camera's, so when I rotate the camera around the Y and X axes to simulate looking around and up and down, the camera will roll and produce other highly non-intuitive reactions to panning actions. 

Is there a way to tell the camera that the direction it is looking in now should be considered the new visual root - ie force the values in the screenshot to show Pitch 0. 

Setting camera direction, setting the transform, setting the rotation... nothing seems able to alter this property of the camera. Is there a way to do this?

-------------------------

SirNate0 | 2020-06-22 22:32:24 UTC | #2

Probably you can just add node between the camera and the scene that's oriented according to the coordinate system that you want. So Scene > Transform node > camera node. Personally I'd go with planning that intermediate node at the surface of the planet as well, then your camera position is measured in elevation from the ground instead of the center of the planet. Be sure you don't use GetWorldRotation in that case, or you'll still have the same results you do now.
Careful when you choose how to do this though - if you go with spherical coordinates you might have trouble at the north and south pole with the camera flipping direction or something (going from yaw of zero is North, crossing the north pole, and now the camera should have yaw of 90 and point south or you'll get a sudden flip).

-------------------------

freever | 2020-06-22 15:24:20 UTC | #3

Brilliant, thank you - that worked a treat!

![image|690x444](upload://og8DiSuog6UqARRnyAkmx38EbnO.png)

-------------------------

