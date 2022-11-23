OMID-313 | 2017-02-13 16:28:54 UTC | #1

Hi,

I want to create a scene with several viewports.
Some of these viewports shall have a rotated initial position. I mean, I want a rotated rectangle.

I tried adding the following line to 09_MultipleViewports.as example, but it gives errors!

`rearViewport.Rotate(Quaternion(180.0f, Vector3(0.0f, 1.0f, 0.0f)));`

So, how can I achieve this !?

-------------------------

Eugene | 2017-02-13 16:43:05 UTC | #2

Your video card cannot rotate viewports.
Use render to texture.

-------------------------

OMID-313 | 2017-02-14 05:31:44 UTC | #3

Thanks @Eugene for your reply.

Ok then. How can I rotate the camera's picture that comes to the viewport?
Say, we have1 camera and 4 viewports in a scene.

Viewport1 -> Camera's picture
Viewport2 -> Camera's picture 90' rotated
Viewport3 -> Camera's picture horizontal flipped
Viewport4 -> Camera's picture 180' rotated + vertical flipped

How can I achieve this !?

-------------------------

1vanK | 2017-02-14 05:55:40 UTC | #4

You can flip image in shader

> Viewport2 -> Camera's picture 90' rotated

just create another camera and rotate camera

-------------------------

OMID-313 | 2017-02-14 06:31:57 UTC | #5

Thanks @1vanK for your reply.

Is it possible to use shader for rotation too?
Because I don't want to create several cameras.

By the way, what is the correct syntax for flipping images using shader?

-------------------------

1vanK | 2017-02-14 06:41:50 UTC | #6

[quote="OMID-313, post:5, topic:2791"]
Is it possible to use shader for rotation too?
[/quote]

What if texture not square?

You should mix rotated texture as post process

-------------------------

OMID-313 | 2017-02-14 06:52:28 UTC | #7

Actually, I don't truly know the difference between shader, texture, ...
This is similar to what I want to achieve:
Several viewports with the same image, but some rotated, flipped, etc.

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/06f3f80b18c8f41071a8335878844e67aae8d988.jpg" width="690" height="388">

The closest example code I found was **09_MultipleViewports.as**. But I don't know how to add rotation and flip.

I would be thankful if you help me do this.
(sorry for being amateur.)

-------------------------

1vanK | 2017-02-14 06:59:36 UTC | #8

Flip vertically in shader: vScreenPos = vec2 (vScreenPos.x, 1 - vScreenPos.y);

-------------------------

