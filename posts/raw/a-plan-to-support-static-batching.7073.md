Sunc | 2021-12-01 03:45:39 UTC | #1

I see this is an absence feature of Urho3D, but it really helps the rendering overhead. So I intend to do the implementation by my self, however suggestions is needed by you experts. What would I do is the static batch like what Unity have done, I read its' manual page about this feature and thought about it deeper and... Wow, it's not so easy like my first thought about it. There apears much rendering mechanism details in my head such about what should the quantity limitation of VBO and IBO be, how about the semi-transparent objects, what about LOD, in which way to produce the merged mesh(pre or runtime), and blablabla... At first I thought may be the StaticModelGroup component would be a good place to dig in, but I found it's just a way to speed up GPU intancing. So, now I am lost in thought, 
looking forward you guys suggestions.

-------------------------

SirNate0 | 2021-12-01 13:48:43 UTC | #2

I'm certainly not an expert (and I've not read about Unity's implementation, so you probably know more than me), but here are my thoughts:

- quantity limitation of VBO and IBO: You'll need to test on several machines to determine an optimal size.
- semi-transparent objects: Forbidden except for ALPHAMASK objects, as it would probably be more of a pain to deal with than it's worth, and you'd probably need the depth sorting for each object anyways.
- LOD: provided per batch only. So a room might be a good example of a batch, as when the player is in it it would have the highest LOD, and when they are in a distant room looking in through a door a lower LOD may be acceptable.
- way to produce the merged mesh(pre or runtime): beforehand since it's static. You're choice whether it's completely separate with another tool (e.g. added to the editor or something) or whether it's done at startup and cached to the disk (could also be done at level load, but as a player I'd prefer a one-time several minute setup when installing and first running the game over a several second longer load every level. Unless it is really short to do (<0.5 seconds per level or so), in which case truly doing it at runtime may be acceptable.

And I have a question: How does the method handle different textures/materials? Do the textures need to be combined into an atlas and the materials need to be the same other than the textures?

-------------------------

Eugene | 2021-12-02 15:10:58 UTC | #3

This is one of many features that suffer from fully dynamic nature of Urho3D as engine.
Urho does not have the concept of "compilation", therefore "editor-time logic" and "run-time logic" are the same thing, therefore there's no such thing as "static object" and, consequently, "static batching".

Urho has _some_ things that are 100% editor-time, and they are always explicitly invoked by user, e.g. `NavigationMesh` build.
Your best bet would be to make something similar. Utility class that:
1) Iterates over Drawables in Scene or Node
2) Checks whether to batch each specific Drawable
3) Disable and/or remove such drawables
4) Generates new Drawables somewhere else

The exact algorithm is almost pure heuristics, but you can _tecnhically_ accumulate arbitrary amount of `StaticModel`s in one `StaticModel`, and you can pack multiple Materials in one Material if they use same shader and same parameters.

It's probably going to be an offline tool expicitly used by the user.
If you want Unity-like static batching which is almost hidden from user... I am not sure you can.

-------------------------

Sunc | 2021-12-02 23:13:53 UTC | #4

Thanks for reply. 
Last few days, I thought more about the subjects above.

● quantity limitation of VBO and IBO: There are different limitations on different platforms which determined by either hardware or software, according to the unity manual it says "Batch limits are 64k vertices and 64k indices on most platforms (48k indices on OpenGLES, 32k indices on macOS)".
● semi-transparent objects: The sorting job is needed by arrange objects from far to near at runtime, but it makes extra CPU cost.
● LOD: An object may group up with several LOD meshs which differs at number of triangles but represents the same stuff. I would batch all the LOD type geometries into N groups which N stands for the maximum LOD level among them, the downside is it costs more memory but suitable level mesh could be chosen to display.
● way to produce the merged mesh(pre or runtime): I tend to preprocess(or "bake") much more, cause it saves the overhead of merging vertices. The job should be done at editor side.

And about your question: I didn't mean to merge objects with different materials, only objects with same materials is concerned. But try best to let more objects share the same material is a good advise to modelers, such as make the use of atlas textures.

-------------------------

Sunc | 2021-12-02 23:30:07 UTC | #5

Thanks for reply.
I would take your suggestions into considering, and later I would try to make the design(maybe after a few days, start by a simple scratch). And now, allow me to think more about it, I would make a reply to you later.

-------------------------

