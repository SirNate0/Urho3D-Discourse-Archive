Pacho | 2017-05-05 14:25:40 UTC | #1

I'm talking about a sprite that has a position inside the scene. It should always be rendered on top of anything that is 3D.

Using the UI system would work, but I would have to manually update the sprite's position every frame according to camera movement etc.

Using StaticSprite2D means that it rotates along with the node it is attached to, which I don't want. I only want it to move with the node. And I can't be 100% sure that the sprite is rendered on top of anything 3D, unless I raise the y position substantially, but that brings its own problems with a perspective camera.

Is there an easy solution?

-------------------------

smellymumbler | 2017-05-05 22:08:51 UTC | #2

So... like a Doom sprite?

-------------------------

Pacho | 2017-05-06 07:23:35 UTC | #3

I'm not sure. I'm doing a top-down RTS where when I select units a 2d health bar is shown for each unit, for example.

-------------------------

George1 | 2017-05-06 07:31:43 UTC | #4

I think you are talking about billboard right?

-------------------------

Pacho | 2017-05-06 13:20:43 UTC | #5

Yes, I forgot about billboard!
Sadly, there is still no option to render it on top of 3d. Of course I can offset the position, but with a perspective camera one can clearly see how much it is raised if the camera is not directly above it.

Edit: I tried using a material that alters the renderorder value to something larger than the deafult 128, but it still won't render on top of a 3d model.

-------------------------

Sinoid | 2017-05-07 12:31:49 UTC | #6

Create a specific material & technique combination for your *sprites*. Set the depth-test in your technique's passes to **always** so that they'll always pass the depth test, that will guarantee that their fragments pass Z-test. Leave shadow related passes alone, it won't matter there.

Render order still matters, leave it as something larger so that they'll render later than other things.

-------------------------

Pacho | 2017-05-07 12:33:31 UTC | #7

Setting depthtest to always did the trick, thanks!

-------------------------

