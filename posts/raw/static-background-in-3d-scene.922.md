Vivek | 2017-01-02 01:04:06 UTC | #1

I want a static texture background.
I can create a skymap and use it but it is not static. It moves as we move the camera.
The 2D ui is always in the front so does not help either.
Any suggestions?

-------------------------

cadaver | 2017-01-02 01:04:06 UTC | #2

You could do a hack like attaching a plane mesh node as a child to the camera, or you can see the scene layering approach discussed here: [topic756.html](http://discourse.urho3d.io/t/how-to-layer-scenes/740/1)

-------------------------

TikariSakari | 2017-01-02 01:04:06 UTC | #3

[quote="Vivek"]I want a static texture background.
I can create a skymap and use it but it is not static. It moves as we move the camera.
The 2D ui is always in the front so does not help either.
Any suggestions?[/quote]

Did you try to add the skymap on same node as the camera so that it would take rotations from the camera itself?

Edit also there are billboards, and you could even try adding a single sided plane that is parented to cameras node, that is always certain distance away. You just need to calculate the width and height of the plane depending on whats the field of view angle.

-------------------------

Vivek | 2017-01-02 01:04:06 UTC | #4

I attach the node to the camera and its work as expected.
@ cadaver I didn't try scene layering approach as I think first approach would be more optimized.
Any calculation how much the plane should be scaled to fit the whole screen, given the distance from camera.
Thanks

-------------------------

cadaver | 2017-01-02 01:04:07 UTC | #5

You can use the camera's aspect ratio, which is normally auto-adjusted as resolution changes (X res / Y res).

-------------------------

weitjong | 2017-01-02 01:04:09 UTC | #6

I think you can also use a custom RenderPath to achieve this. Use a quad command after clear command to render the texture before the scenepass command.

-------------------------

Vivek | 2017-01-02 01:04:09 UTC | #7

@weitjong, I will try this.
Never tried custom RenderPath before, but I have to try it sooner or later.
Thanks for the approach.

@cadaver how do I use  camera's aspect ratio to get the desired scale for the plane/quad so that it fills the view. I understand the aspect ratio and would take the larger dimension of width or height but still miss how to find the scale or dimension of quad/plane. This can be solved by using ortho camera but that would require two viewport approach, so want to avoid that.

-------------------------

