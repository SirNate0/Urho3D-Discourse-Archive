evolgames | 2020-08-28 04:15:26 UTC | #1

Setting:
```
camera.zoom = 2
```
doesn't double the zoom, right? And 4 quadruple it and so on? I'm assuming it doesn't work like this.
The camera documentation just says "zoom." So suppose I set the zoom to 8. How is 8 represented here? Because it doesn't appear to be magnifying at each integer. It just looks like you would expect zoom to work in 3d modelling software.

So how can I calculate magnification? The application in this case is a sniper scope. I don't need realism, just something accurate enough to be believable by the player.

-------------------------

Eugene | 2020-08-28 07:52:29 UTC | #2

I'm not exactly sure what you call "magnification".
Use FOV if you want to get exact number of degrees.
Use zoom if you want to scale up final image (it should work this way, at least).

-------------------------

evolgames | 2020-08-28 13:02:49 UTC | #3

What I mean is, I need to zoom my image, but I'm not sure what the units are for zoom to make sure I'm at the right magnification.
Each scope "level" would be a magnification where 2x is twice as "zoomed" as camera.zoom = 1. 4x would be 4 times as zoomed.
Like a microscope does, too.
Is this something I can calculate or would it be easy to do this via postprocess and effectively double the image in xml?
https://www.youtube.com/watch?v=3KRMP_FLm48

-------------------------

Modanung | 2020-08-28 14:28:51 UTC | #4

There is no technical difference between zooming in and reducing the field of view. I'm not sure what SetZoom does, but my gut memory tells me it is more suitable for 2D. To zoom in using the FOV, simply divide the FOV by the zoom factor. This is how it was done in Unreal Tournament, and it still works today.
A second viewport and camera could create a difference between in and out of scope zoom.

-------------------------

JTippetts1 | 2020-08-28 19:07:11 UTC | #5

SetZoom() should work the way you expect. Here are some image results from a quick test:

![image|215x500](upload://bkHBvDu6zmLOcX51OJz12TE1qzi.jpeg) 

The top is a render of a scene with a gridded plane at zoom=1. The middle is at zoom=2, and the bottom is at zoom=4. You can see that at each step, the view is of half (vertically) of what the previous zoom step showed.

If you look at the Camera code, you can see that it uses Frustum to define the projection matrix. Frustum has a [method](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Math/Frustum.cpp#L75) that takes the fov, aspect ratio and zoom level to construct the frustum. Inside the body of that method you can see that zoom is used as a divisor of the tangent of the fov, meaning that if you choose zoom levels of 2, 4, 8, etc... each step halves the size of the near/far planes, meaning a 2x multiplication level.

-------------------------

evolgames | 2020-08-28 19:08:51 UTC | #6

Well that's good enough for me!
I didn't even consider testing it with a grid, that's clear as day.

-------------------------

