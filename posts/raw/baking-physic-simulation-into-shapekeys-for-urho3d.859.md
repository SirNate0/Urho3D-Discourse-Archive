codingmonkey | 2017-01-02 01:03:35 UTC | #1

Hi folks!
Recently, I tried to understand this topic. And that's what I got:

[video]http://www.youtube.com/watch?v=7-ny5e6P0-4[/video]

Maybe for someone this will be useful. And if someone wants to learn how to do it. 
In the video, there is the process of creating this type of animation.
 
I think that in Urho shapekeys are very expensive in terms of computation. Therefore it is necessary to use this technique carefully and in small doses)

[b]BakedShape[/b]

[b]h[/b]
[spoiler][pastebin]SxDBBhuJ[/pastebin][/spoiler]
[b]cpp[/b]
[spoiler][pastebin]xhjn7WdF[/pastebin][/spoiler]

using
[spoiler][pastebin]k6pPh6UA[/pastebin][/spoiler]

-------------------------

cadaver | 2017-01-02 01:03:35 UTC | #2

Yes, that's old-school vertex animation which has to calculate every vertex on the CPU and reupload the vertex buffer. That is necessarily very performance-heavy.

-------------------------

codingmonkey | 2017-01-02 01:03:36 UTC | #3

I thought that if the shapekeys are calculated on top of (after) the skeletal animation, then we can make the effects of micro movements (from the wind) for clothes, in local bone space.

> that's old-school vertex animation which has to calculate every vertex on the CPU 
Is it possible to upgrage this animations to gpu-based calculations, maybe only for desktop graphics and not for mobile ?
I recently viewed turso3d, what there already is working well, I run the examples. And I want to ask - there will be support for GPU animation or maybe there are plans to introduce it even Urho3D ?

-------------------------

cadaver | 2017-01-02 01:03:36 UTC | #4

Supporting morph targets in vertex shader means the vertex stream would have to contain all morph shape vertex positions interleaved, and they need to affect the whole mesh. Currently you can't define arbitrary vertex declarations in Urho3D (ie. multiple position attributes) so it would not work without some changes to the model format, exporters, and the graphics API. I will not give any promises on this, and neither on Turso3D's capabilities. Turso3D is for now mostly a toy engine for testing things and it will develop (for example get animation features) if I have a use and interest for it, but you should certainly not count on that.

See [antongerdelan.net/opengl/blend_shapes.html](http://antongerdelan.net/opengl/blend_shapes.html) for an example of how morphing would be done with shaders. I'm somewhat skeptical of this as a scalable solution, as the vertex size and the amount of streamed data on GPU grows for each morph shape, and even more if you would also include multiple normals & tangents. For one morph shape it would likely be fine though.

-------------------------

OvermindDL1 | 2017-01-02 01:03:37 UTC | #5

I recently wrote a Model importer for an ancient game model format, which supports the usual vertex/normal/tangent/color/uv mappings per point, in addition to skeletal animation with up to 4 weights per vertex, and the most painful of which was adding in support for its vertex animation, which I currently handle by updating vertex information from the CPU rather painfully...  I am considering writing a shader and uploading the morph information via texture where the normal interpolation between values can be used as it should work well for the format I use and all of its morph information is well encoded.

Yes, it was a pain...

EDIT:  The models are really old, the polygon count tends to average from 100-800 per model so I could do it this way without too much effort..

-------------------------

boberfly | 2017-01-02 01:03:38 UTC | #6

Hi,

I've had a thought about this once before. Perhaps for a real-time engine some kind of deformation modifier stack could be made that works like the render-path system where it is data-driven but defines an order of deformers which is abstract enough to do things like GPU transform feedbacks for you or generates a special 'uber' vertex shader (or perhaps compute shaders or uses a CPU approach that uses something like ISPC with a fast upload path to GPU with glBufferSubData fallback) for you that combines all of your deformers which need to be applied to your model. Bullet has a softbody CL kernel doesn't it? This might be a good compute shader candidate for instance.

Naturally mixing GPU/CPU deformation would bottleneck things or not be compatible with each other, so this system might not be very flexible. Also this would probably make more sense in Turso3D where GL3.x+/DX10+ features are exposed like transform feedback, compute shaders, TBOs/UAVs. Food for thought.

Cheers
-Alex

-------------------------

cadaver | 2017-01-02 01:03:38 UTC | #7

My gut feeling is that this would be much easier to do in a custom renderer where you get to the API level with your own code directly, rather than "fighting" a multiple-API framework such as Urho3D.

-------------------------

codingmonkey | 2017-01-02 01:03:38 UTC | #8

>See for an example of how morphing would be done with shaders.

I guess what i'm doing this Vertex animation (Tweening) in similar way before.
When i'm starting learn shaders on gl and doing some experiments with exporting model from blender.
I don't remember exactly but there must be two binded vertex buffer (with full length vertex animation(all frames in each buffer)) then we just set range(this range is calculated by cpu-side and based on current animation time) for one and second vertex buffer and mix factor for shader (gpu-side).

-------------------------

