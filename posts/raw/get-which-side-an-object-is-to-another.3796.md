nergal | 2017-11-27 20:56:36 UTC | #1

I have an box in front of my camera (0,0,-150) that I can see right in front of my camera. Then I have other objects on each side of my box. How can I determine which side of the camera (right/left) the other objects are?

Using Vector3.Angle I only get a positive angle (ofcourse) so I cannot determine side based on that. Same with distance, the distance will also be positive using regular Vector3 distance formula.

Any tips or trix?

-------------------------

Eugene | 2017-11-27 21:19:44 UTC | #2

Cross products are usually used to determine signed things.
Get `Right` vector from the node (or make your own one via cross product) and then check directions via dot product or angle.

-------------------------

nergal | 2017-11-28 15:21:35 UTC | #3

Ok, I elaborated a bit with what you said and perhaps there is a easier way (or I'm doing it wrong). But I will try to explain a bit better. The below image is showing my camera and it's direction vector. I just want to know if object1 is on left or right side of my direction vector and which side object2 is compared to my direction vector.

It would help if the left-objects angle compared to camera direction vector would be above 90 degrees (hence left side) and angle below 90 degrees would be right side. So I was testing:

     float v = camera_direction.Angle(object_position);
but it seems to never return > 90 degrees. Perhaps I'm missing something?

![04|608x487](upload://e3pcbyQmZnPWbsJxwUmF7RZqxPC.png)

-------------------------

George1 | 2017-11-28 15:36:54 UTC | #4

Eugene already answer you about cross product.

LH coordinate system.

direction_vector x (cross) vector_to_object.   

if -ve them object is on your left. If +ve then object on right.
If cross product = 1 then 90, -1 then -90, 0 then it's parallel to your direction vector.

-------------------------

nergal | 2017-11-28 15:38:26 UTC | #5

Ok, I will try to get a better grip of it! Thanks for the input.

-------------------------

Eugene | 2017-11-28 15:48:57 UTC | #6

[quote="nergal, post:3, topic:3796"]
The below image is showing my camera and it’s direction vector
[/quote]

What's the camera? If it's node and camera direction is `Node::GetDirection`, you should test the angle between object and `Node::GetRight`.
Otherwise, you should make the right verctor on your own.

-------------------------

Modanung | 2017-11-28 19:38:08 UTC | #7

How about:
```
Sign(cameraNode->WorldToLocal( objectNode->GetWorldPosition() ).x_)
```
Which would give `-1.0f` for `objectNode`s left of `cameraNode`, `1.0f` for right and `0.0f` for dead centre.

-------------------------

nergal | 2017-11-28 19:17:06 UTC | #8

That worked really well!
    
     Vector3 p = cameraNode->WorldToLocal(object_pos);

Thanks all for the help!

-------------------------

