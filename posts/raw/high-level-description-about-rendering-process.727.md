abcjjy | 2017-01-02 01:02:30 UTC | #1

I read through the docs and got some basic idea about the engine. But I still don't understand how the renderer works. I looked up the source code and meet batches, queues and various of things. And the View class does a lot of work while rendering, but it is not mentioned in the document. Can anyone give a high level design description of the rendering process? How are the render commands organized? What is the responsibility of View? And how renderer, graphics and view collaborate with each other conceptually? 

BTW, I am curious about the shadow pass defined in technique, whereas there is no shadow pass defined in the renderpath. It seems a special case. After reading some code, I found it is not added to renderpath after all and shadow drawing is separate from the renderpath command. Is my understanding correct? If so, why not put every pass into the renderpath which is more consistent? 

Thanks

-------------------------

cadaver | 2017-01-02 01:02:31 UTC | #2

The "what happens" during rendering is documented on the [urho3d.github.io/documentation/1 ... paths.html](http://urho3d.github.io/documentation/1.32/_render_paths.html). To get to the details of "how it happens" it's best to study the engine code and perhaps step through a frame rendering in the debugger. The basic outline is that each frame Renderer finds out the viewports that needs to be rendered (either in backbuffer or in textures), it reserves a View object for each and instructs it to first prepare the view (get geometries, lights & batches) and later, during the frame's render phase, the View will render its prepared data using the Graphics subsystem.

Render path deals with things that are fixed each frame, like scene render passes and post processing, going either directly to the ultimate final output rendertarget or to intermediate targets. On the other hand shadow rendering happens dynamically according to the visible lights, so that's why the "shadow" pass is not mentioned in the render path. Supposedly we could have a "render shadow maps" command but the render path file would have little meaningful input to it, other than the pass name.

-------------------------

ghidra | 2017-01-02 01:02:31 UTC | #3

I can not claim to know all the answers accurately, however I will try to explain what I do know simply.

The RenderPath are you main instructions, and are executed in order, and are where you can specify passes to render.
Here you can render to the main viewport, you can render a quad, you can override shaders that you want to use on these passes.

The Techniques are also a set or instructions. You can have passes listed here that are not used in the renderpath. Passes that are set in the renderpath, uses the instructions here. You can set what shader to use specifically here as well. I do not know who gets priority when both the renderpath and the technique specify a shader, i havent tried yet.

The Material specifies which technique to use. As well as assign textures to use, and other attributes that get passes to shaders.

Then the Shaders.

Shadows are related to passes with the label with "lit" in it. Again, I cannot really elaborate much on this, as I just accept it and do what I can at this point.

-------------------------

