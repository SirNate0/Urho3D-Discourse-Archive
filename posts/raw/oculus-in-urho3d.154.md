GIMB4L | 2017-01-02 00:58:26 UTC | #1

Integration of the Oculus has exposed a few issues with the engine in terms of shader capability.

First, there's no projection matrix post-multiplication. I implemented a matrix for that myself in the Camera class, but I'm not entirely sure it worked. Here's what I did:

[code]ret = postfixMult_ * ret;[/code]

Where postfixMult is a translation matrix you can set the translation of. Note that this happens AFTER the vertices are in clip space, so its a POST multiplication. 

Second, the lack of reading from a specific viewport made it difficult to write the shader since you have to accomodate the entire screen now.

Third, the postprocessing XMLs don't allow you to scale a texture up -- which is a crucial part of the Oculus display.

Note that a lot of these issues also apply to other applications, mainly post-processing wise.

-------------------------

cadaver | 2017-01-02 00:58:26 UTC | #2

Do you need the initial (undistorted) scene render to be larger than the viewport on screen? Or do you just need an intermediate texture which is larger than the viewport?

The first point would be a rather elaborate change. The second would be just addition of a simple parameter.

Something like this [opserver.de/ubb7/ubbthreads. ... ber=432348](http://www.opserver.de/ubb7/ubbthreads.php?ubb=showflat&Number=432348) should already be perfectly doable, but I don't understand Oculus well enough to know if that's enough.

Note that you can bypass the viewport size issue, and also the "both viewports in same texture" issue by manually creating rendertarget textures that are the size you want (can be larger than the viewport) and have a scene rendering renderpath in them without the distortion effect. (Look into the RenderToTexture sample for how to set this up.) Then set a different renderpath into the backbuffer viewport(s) that doesn't render the scene at all, but just samples these textures using the distortion effect. You will need to give names to the textures and register them as manual resources to the ResourceCache so that you can refer to them by name in the backbuffer renderpaths.

If you do this there's btw. some inefficiency in the View class currently: if you point the backbuffer viewports in this case to your full scene, it would unnecessarily re-cull the scene, because it doesn't understand that the renderpath contains no scene passes. The workaround for this would be to create a separate empty scene (with just an Octree component so that View is happy and doesn't abort rendering) and point the backbuffer viewports to that.

-------------------------

GIMB4L | 2017-01-02 00:58:27 UTC | #3

I'll try getting the texture to scale, but how exactly do I specify a render target that's larger than the screen? Also, am I doing the projection matrix [b]post-multiplication[/b] correctly?

-------------------------

cadaver | 2017-01-02 00:58:27 UTC | #4

Create the rendertarget texture in code, not in renderpath xml (look at the sample) then you're free to specify size for it just as you want.

The multiplication looks OK.

-------------------------

GIMB4L | 2017-01-02 00:58:30 UTC | #5

I should clarify that I only need the diffuse texture coming from the scene pass to be scaled up. If this isn't an easy fix, could I just use another shader which samples from the backbuffer and just scales it up into another rendertarget?

-------------------------

