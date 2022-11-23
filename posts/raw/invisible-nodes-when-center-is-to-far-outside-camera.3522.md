AlexanderAtUrho | 2017-09-01 08:00:47 UTC | #1

Hi,

I am not sure how to explain this in a good way, and I am not sure about the proper terms, so please bear with me.

We have a situation where we have a node with a model, component and texture, and the centre of the node is somewhere outside what the camera can se. The model is big enough to be seen inside the camera, and as you would expect, it gets rendered in the scene and all is fine.

But, if I move the nodes centre a bit further away the model disappear from the scene. The model is still big enough to be visible in the scene, but for some reason it just disappear as soon as its position moves it "too far" away. It is moved outside, to the left or right so to speak, and not further into the scene.

I guess there is some optimisation going on, and that the SetViewport has part in it, but as the model should be visible in my scene, I do not want it to be optimized away :slight_smile:

Is there some parameter I should adjust? I have tried to play with the renderer and SetOccluderSizeThreshold and SetMaxOccluderTriangles without success. But honestly I do not know what I am doing.

Anyone got any suggestion? I would not be the least surprised if there is something obvious we have missed.

Sincerely,
Alexander Sundqvist

-------------------------

Eugene | 2017-09-01 09:00:07 UTC | #2

Any screenshots/vids?
Is model's bounding box valid?
Could you reproduce the problem with the standard assets?
If so, share the code.

-------------------------

AlexanderAtUrho | 2017-09-01 09:46:51 UTC | #3

Thanks for your answer.

The bounding box is valid. I will make screenshots to show the issue. But the screenshot will show a textured plane, and then the textured plane is gone. Not much to show.

I will have to look into if we can reproduce with standard assets or demo projects.

-------------------------

Eugene | 2017-09-01 10:27:34 UTC | #4

[quote="AlexanderAtUrho, post:3, topic:3522"]
I will have to look into if we can reproduce with standard assets or demo projects.
[/quote]

That's the best way if screenshots are not meaningul.

-------------------------

AlexanderAtUrho | 2017-09-01 13:43:27 UTC | #5

Hi,

After you asked about the bounding box I went back to make sure it was valid. It is walid.
However, if I make the box even bigger, in this case thicker, I can increase the distance for the plane center and still have a visible plane.

In other words, a thicker bounding box helps, but doesnt solve the problem. So the bounding box is clearely related to the issue.

I could not reproduce the problem using standard demo and assets.

Is there any drawback in having oversized boundingboxes? I our case, all elemnts in the scene are supposed to be visible all the time anyway.

Can I completely bypass the optimization and just show everything to save time?

-------------------------

Eugene | 2017-09-01 14:59:06 UTC | #6

[quote="AlexanderAtUrho, post:5, topic:3522"]
Is there any drawback in having oversized boundingboxes?
[/quote]

Nothing except performance.

[quote="AlexanderAtUrho, post:5, topic:3522"]
I could not reproduce the problem using standard demo and assets.
[/quote]

That's strange.
If you remove everything except the camera and the drawable, is the problem reproducible?
If you replace the drawable with scaled box with the same BB, is the problem reproducible?

-------------------------

