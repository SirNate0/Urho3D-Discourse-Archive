throwawayerino | 2022-01-31 17:49:50 UTC | #1

I want to put crosshairs on screen and invert the color according to what's on screen. What should I put in the technique/shaders?

-------------------------

Eugene | 2022-01-31 19:10:44 UTC | #2

Urho cannot do that out of the box.
You need to add custom `BlendMode` for this.

In OpenGL it would be `op=GL_FUNC_SUBTRACT`, `src=GL_ONE`, `dest=GL_ONE`, and render simple white crosshair with this blend mode.

-------------------------

throwawayerino | 2022-02-01 01:06:31 UTC | #3

Are you talking about the shader on UI part? I do see that you can add materials to them

-------------------------

JTippetts1 | 2022-02-01 02:22:10 UTC | #4

You can set a Material to a BorderImage, but it sounds like you want access to the framebuffer to read the pixel that is already there in order to invert it, and to do that you can't use just any material. Eugene suggests an approach that doesn't require you actually reading the framebuffer, but instead using a blend mode (that you can't really set without the modification he suggests) to perform the color inversion during the blend step.

You might take a look at the Water sample for an example of a material that reads the framebuffer in the shader. The material uses a technique that renders during the "refract" pass, a pass during which the framebuffer is set as the environment texture uniform so you can sample it in the shader. I honestly don't know how well this would combine with UI rendering, but it might be worth attempting.

-------------------------

