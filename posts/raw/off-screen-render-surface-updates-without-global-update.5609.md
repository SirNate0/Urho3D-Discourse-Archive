Avagrande | 2019-09-21 10:13:08 UTC | #1

I am working on animated transitions between two different states of a render surface. 
But to accomplish this I have to create a image for the current and next state so I can render their stills together during the animation.

The way I accomplish this is by fetching the image from the texture bound to my render surface and copying it into a new texture. However I cannot update a canvas without rendering it to the screen so the users sees a brief flash of the next frame before the transition begins as I use `GetEngine():RunFrame()` to force a render target to be filled with the next state. 

This works as intended although with undesirable Update event which is unnecessary and in some cases it causes a flash of the frame I never want the user to see.

Is there a way I can update a singular render surface without causing a global update? I only want this one updated.

-------------------------

SirNate0 | 2019-09-21 13:34:57 UTC | #2

You should be able to render to a texture instead of the screen's render target. I believe there's a couple threads with code to set such a thing up, as well as an example in the samples. It kind of sounds like you may already be doing this, so if that's the case sorry for not being able to help.

-------------------------

Bananaft | 2019-09-21 16:59:24 UTC | #3

Do you want a cross-fade transition effect between two shots, right? 
I feel like it should be done entirely on GPU by switching renderpath commands.

You can make a post-effect that draws old copied frame on top of current render result and then slowly fade it out.

-------------------------

Avagrande | 2019-09-22 02:17:43 UTC | #4

yeah that's pretty much it but I would like to have control over the two images on the cpu for arbitrary transitions. Doing it purely on the gpu is not ideal for me. 

It would work as long as I have the ability to perform a update on the render surface immediately without running a frame. I assume that the gpu method would need two render targets correct? If so I think I can do the effect by creating two render surfaces to render it off screen without displaying the result.  I would really like to avoid that though since it misses the central problem of updating a single surface on demand, which I need later anyway. I don't think there is a way to do that currently so I will try to implement it.

-------------------------

