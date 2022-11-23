sabotage3d | 2017-01-02 01:15:27 UTC | #1

Hi,
I am having performance issue with Sprite2D. I am using ParticleEmitter2D to draw the sprites. If I draw 10k sprites with small size my frame rate is running at 60 fps, if I draw them with large size I can barely get 10fps. Is there anything that would explain this behaviour and anything that can reduce it?

-------------------------

TheEndOfUsAll | 2017-01-02 01:15:27 UTC | #2

Batching and drawing or simply direct drawing small or big sprites has the same cost, what you're hitting is GPU fill rate and overdraw limit

-------------------------

sabotage3d | 2017-01-02 01:15:27 UTC | #3

Is there way to minimize the cost I am drawing the same texture. Would it help changing the texture filtering?

-------------------------

TheEndOfUsAll | 2017-01-02 01:15:27 UTC | #4

If changing the sprite size is altering performance, that's surely a hardware limitation you're hitting, specifically the GPU, on modern GPUs changing the filter generally doesn't have much if any effect, what you could try is using a different shader if you're using something complex, and changing the blend mode but generally that's not an option, other than that, any GPU should easily be able to fill the whole screen many times much faster than you generally need, but if overdrawing is really a problem and there's no way to optimize that another way, in the worst case you could go with a software renderer that draws front-to-back and compares alpha against a threshold to see whether a pixel should be considered for rendering... generally that's not a good idea but since you can effectively discard a lot of overdrawing that could be an option if your problem is really that. Maybe you could even go with a custom renderer in OpenCL.

However, can you tell us more about your requirements and usage, including hardware details? I can only think of one or two situations where you'd really have to go that far.

-------------------------

sabotage3d | 2017-01-02 01:15:27 UTC | #5

I am drawing spritesheets with ParticleEmitter2D. The size of the sprite is1024x1024 and 128 pixels per grid. I am hitting the same issue both on Desktop OpenGL 3.3 and Mobile OpengGL ES 2.0 on relatively modern hardware. Is there a way to clamp or limit the opacity blending if I stack too many sprites on top of each other?
The blend mode is addalpha: [code]<pass name="alpha" depthwrite="false" blend="addalpha" />[/code]

-------------------------

