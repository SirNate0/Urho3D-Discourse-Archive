claudeHasler | 2020-03-30 16:21:36 UTC | #1

Im displaying a model which works fine most of the time, but occasionally when i change the position and direction of the camera, the model disapears:
![image|648x500](upload://6Z34k9xZ7wQD9CjYdQBZYnj0bYG.png) 
![image|690x497](upload://tEM3irc2ejXVXb3kGD4RI6kWj1P.png) 
![image|502x500](upload://rPaP9BzKMGQUjeFUYVKouMsRrMh.png) 

I dont understand how this can be happening, two of those images are in very similar positions so i dont believe it is the lighting, what else could cause this kind of effect? What i have noticed is that when the model is in the upper third of the screen it seems to disapear

-------------------------

SirNate0 | 2020-03-30 16:37:54 UTC | #2

I would guess a bounding box issue is probably the cause. Or possibly occlusion - is the white square an occluder?

-------------------------

claudeHasler | 2020-03-30 16:45:18 UTC | #3

no the white box is simply some debugrenderer output so i have some frame of reference.

How could a boundingbox be an issue? being outside the camera clip range?

-------------------------

SirNate0 | 2020-03-30 17:00:21 UTC | #4

Yes. If the bounding box doesn't actually contain all of the model for whatever reason and ends up outside the camera's frustum then the model won't display even though it should visually. Hopefully the import process got that correct, but it's worth checking to see for problems like these.

-------------------------

claudeHasler | 2020-03-30 17:59:47 UTC | #5

So it turns out the model is not to blame, instead it is because i am using a large projection offset, almost half of my screen dimensions. The reason for this is that i am developing a projected reality application, and the projector (an inverse camera) calibration demands this offset.

[Code]cameraNode_->GetComponent<Camera>()->SetProjectionOffset(Vector2(offsetX,offsetY)); [/Code]

Is there a way to get this to render anyway?

-------------------------

SirNate0 | 2020-03-30 21:26:05 UTC | #6

You did remember to divide by the viewport dimensions, right? From the documentation for SetProjectionOffset: "Set projection offset. It needs to be calculated as (offset in pixels) / (viewport dimensions.)"

-------------------------

WangKai | 2020-03-31 07:55:36 UTC | #7

Maybe you should check the far clip distance of the camera to make sure it is far than your model.

-------------------------

claudeHasler | 2020-03-31 18:54:51 UTC | #8

Both the distance and the projection offset are correct

[Code] 
viewport->SetCullCamera(cullCamera);
[/Code]

I solved the issue by setting a separate cullCamera with a large FoV

-------------------------

SirNate0 | 2020-03-31 21:40:39 UTC | #9

Would you mind sharing the parameters you set for the camera? I'd like to look into the issue a bit more as your solution sounds more like a band-aid hiding the underlying issue (which probably works fine for your application, but it would be best to fix it if it is a bug).

-------------------------

claudeHasler | 2020-04-01 18:05:59 UTC | #10

sure:

position
141.693 -60.6896 -107.592
rotation matrix
0.741284 -0.0941694 -0.664552 0.238699 0.962368 0.129889 0.627312 -0.254913 0.735866
Fov:21.1675
OffsetX:-0.009375   OffsetY:-0.32963

Its the offsetY which seems to be the problem. Let me know if you need anything else

-------------------------

George1 | 2020-04-02 01:45:30 UTC | #11

You should enable debug line to show model bounding box.
Also play with set far and near clip.

-------------------------

Sinoid | 2020-04-07 04:15:09 UTC | #12

Use debug-draw to show your Octree as well. Assuming your type derives from Drawable add a debug-draw override to draw a line from itself to the center of it's Octant.

Your mesh is being assigned to an Octant not in view.

-------------------------

