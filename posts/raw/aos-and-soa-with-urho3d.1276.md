sabotage3d | 2017-01-02 01:06:32 UTC | #1

Have anyone have a simple example for AoS and SoA with Urho3d ?
I saw this video the other day and the techniques look interesting: [youtube.com/watch?v=ZHqFrNyLlpA](https://www.youtube.com/watch?v=ZHqFrNyLlpA) .

-------------------------

cadaver | 2017-01-02 01:06:32 UTC | #2

The scene graph in Urho is AoS and that is hard to change, so what you can do is writing your own subsystem code which updates some thing (probably something which there's a lot of, to benefit from optimization) in an SoA manner. And for that, there's nothing Urho-specific really.

To go even further back in time, on the Commodore 64 SoA is the most convenient way to access for example game entity information in assembly language, as you can use the processor's index registers (X or Y) to choose which entity to access :slight_smile:

-------------------------

sabotage3d | 2017-01-02 01:06:33 UTC | #3

Thanks a lot guys. If what he says its true when generating a lot of components and nodes in Urho3d, do we have to align the memory ourselves ?

-------------------------

cadaver | 2017-01-02 01:06:33 UTC | #4

The objects in Urho3D may not be friendly to aligning, as they're fairly large and arbitrarily sized (usually some multiple of 4 bytes in a 32bit-build).

IMO you should have an identified (with a profiler) performance bottleneck in some part of Urho before you start thinking of such modifications. Or if you want to experiment just for the fun of it, you could for example start writing a new SoA-friendly scene and component model, but that would mean almost a total rewrite. 

For example Ogre 2+ did some fairly substantial scene model rewrite to conform to SoA for the object transforms (and bounding boxes? not sure), and complicated their code, yet in practical tests it's roughly equal if not slower than Urho3D when rendering a "torture" scene of very many object instances all using the same material, similar to the HugeObjectCount sample. A huge number of similar objects all using the same materials is not a realistic scenario, but it sets the upper bound for performance: different objects using different materials isn't at least going to be faster.

-------------------------

sabotage3d | 2017-01-02 01:06:33 UTC | #5

Is it safe to use std::aligned_storage and std::align and std::align from C++11 with the objects you mentioned, or maybe a custom aligned allocator ?

-------------------------

cadaver | 2017-01-02 01:06:33 UTC | #6

The main issue is that scene and scene nodes already handle heap allocation of child nodes and components on their own, so you would have to hack the aligned allocation in. Or maybe tweak the object factories to use aligned storage. I don't expect you to benefit in performance for doing that, however, due to the reason I stated earlier.

-------------------------

sabotage3d | 2017-01-02 01:06:34 UTC | #7

Thanks cadaver :slight_smile:

-------------------------

friesencr | 2017-01-02 01:06:34 UTC | #8

I have been working on a voxel renderer for some time and found i was spending 15-20% of my time allocating memory.  The block data is ~ .75mb per chunk (64x128x64).  this video has a world of 256x256 chunks which is like ~50GB of data!!.
So yeah it eats allocations like a starving dragon.

[video]https://www.youtube.com/watch?v=nkQVUcNouno[/video]

-------------------------

sabotage3d | 2017-01-02 01:06:34 UTC | #9

Looks cool. Where is the exact bottleneck ? Would it work to allocate small batches on the stack ?

-------------------------

friesencr | 2017-01-02 01:06:34 UTC | #10

[quote="sabotage3d"]Looks cool. Where is the exact bottleneck ? Would it work to allocate small batches on the stack ?[/quote]

First I will say this video is a few months old and for some reason this kind of streaming is really hard to get right for me.  I am learning lots through this and I don't feel like I am a good optimizer.  The general summary is that there isn't one bottleneck.  It is very hard to use all the cpus.  In many cases I have had less cpu usage and better performance.  Also single threaded code winning in cases.

10% of the time is spent running perlin noise.  It runs 8 passes of perlin noise.  There isn't much that can be done about that.  I haven't spent more than a couple hours with the terrain generation.  This whole experiement is to have a very robust fitness test of the voxel engine so I can learn and share it with my Urho friends.  If i were making a better looking world that number would be much higher.   I will probably spend a while after I am happy with the results making the world look nice.

I have prototypes where i build the world in to files and read out of the files.  This gets rid of the realtime world generation factor.  Reading from file is 2x faster than a quad core i7 building in parallel w/ noise functions.  My latest working version I compress the files using run length encoding.  This was a huge relief to me since the game I want to make is aiming 4k by 4k tiles and it cuts the voxel maps down by 1/5th to 1/20th of the raw size and has linear speed.  Doing this was slower than reading the raw bytes.  I have plans to reading in a compressed page and read raw data out of that I think that will be faster than the original.

I found that by reading the whole file into a memory buffer and deserializing from a memory buffer was over 20x faster for run length decoding than reading byte by byte.  I had a version where I background loaded all the voxel maps to do all the decoding in parallel and this was actaully 2x slower than doing it single threaded.

A huge bottleneck is gpu uploading.  Waiting for the work queue is frustrating.  It also complicates the code to always block on the main thread.  A person should be able to upload to the gpu from another thread but drivers.  To overcome some of this problem I made a 2 slot system where the work happens on a slot and swaps back and forth so I can build while uploading. 

A very large challenge is conforming to how Urho does multithreading.  Urho does not like it if you leave workers working when it gets to the render phase.  It splits up the work based on the number of cores you have.  If it does not get all available cores it will hitch.  I had originally designed the system to build up over the render phase and this was disasterous.  A normal 10ms frame would hitch to 200ms if the queue wasn't flushed before the render phase.  I am used to dumb business programming where you can have 1 million concurrency because all the code sucks and is io limited.  I can't quite tell but things like memset might be optimized for multiple cores and might be affecting the overall output of other cores.  Even if you can run everything in parallel, synchronizing constantly and gpu uploads will always leave the system partially utilized. 

I rewrote the streaming last weekend.  I will be rewriting it again this weekend too.  Last weekend i rewrote the streaming into its own component.  I lost fix allocation from the stack in favor of using urho's resource memory limits.  The resource limit works really really well.  I had lost a little speed from the allocations, don't care about that yet.  On a side note I bet the resource cache limit is not a well know feature,  there is also a resource router to redirect requests for resources.  I am going to try to load the maps in an interleaved checker patter so I can hit the resource cache more.  A huge issue is that creating 1024x1024, this is a world size of 65 km ^ 2.  The resource references is like 500 MB in stupid strings!!!  I would rather use up 500mb for a giant billboard size jpeg of some cute cats than stupid strings.  I was using the resourceref to hold onto a reference back to disk.  Naturally this sucks.  I am creating a page for maps so that each page can hold 512 maps or something.  So reducing the amount of references by 512 times will make me happy.  It will also allow slower but in memory, linear queries to the rle voxel data.  I am having fun, there are tons of issues.  I have gained a deep respect for minecraft, I am also excited because this voxel format is more powerful, more compressed, and builds faster than minecraft's. Because it builds faster you can have bigger chunks in a draw call.  I also found out how easy it is to blow your vram budget.  

I wonder if buffered reads would help urho's loading speed in some formats where there are lots of read calls.

-------------------------

cadaver | 2017-01-02 01:06:35 UTC | #11

This actually sounds like it should be a good idea to be able to disable the Renderer's use of worker threads at will, if the main program itself is using workers heavily. Or there is a bug/inefficiency in the WorkQueue. It's better to take a slightly slower frame (typically even torture scenes run about only 1.5x max slower singlethreaded, as the use of work tasks is not as critical and widespread) than to hitch.

-------------------------

sabotage3d | 2017-01-02 01:06:35 UTC | #12

Would it be too complicated for an option for custom memory allocator in Urho3d ?
This post looks quite interesting : [bitsquid.blogspot.co.uk/2014/09/ ... ystem.html](http://bitsquid.blogspot.co.uk/2014/09/building-data-oriented-entity-system.html)  
It looks similar to what Urho3D is doing ?

-------------------------

cadaver | 2017-01-02 01:06:35 UTC | #13

It would take quite involved design to be flexible enough. For example AngelScript (and many other 3rd party libs used in Urho) allow to set own replacements for global new/delete, through use of macros. This is easy enough, but I suspect it's not enough for situations where you want e.g. per-object-type memory pools, a per-frame fast allocator etc.

The bottom line is that Urho is not a state-of-the-art engine (AAA-level) in regard to memory allocation and as it stands it doesn't intend to be so. Part of the reason is ease of use: you are simply able to new and delete both your own objects and Urho classes at will, without needing to specify how/where they should be allocated. For most cases this is enough and you will likely hit other bottlenecks like rendering, physics and script updates before running into memory allocation inefficiency.

-------------------------

sabotage3d | 2017-01-02 01:06:35 UTC | #14

I can see your point but some of the dependencies already use custom allocators like the btAlignedAllocator from the bullet physics library. Where you can simply add  [code]void btAlignedAllocSetCustom(btAllocFunc* allocFunc, btFreeFunc* freeFunc)[/code] for custom memory allocator. For Angelscript and Lua it could be completely ignored using a macro and left only for use in C++ .

-------------------------

codingmonkey | 2017-01-02 01:06:37 UTC | #15

[b]friesencr[/b]  
cool, minecraft-like voxels )
>It is very hard to use all the cpus. In many cases I have had less cpu usage and better performance. Also single threaded code winning in cases.
Did you see this tech? [openglinsights.com/](http://openglinsights.com/) 
[quote]"Chapter 22. Octree-Based Sparse Voxelization Using the GPU Hardware Rasterizer by Cyril Crassin and Simon Green" [/quote]
I think it absolutely win in performance case on modern gpus

-------------------------

friesencr | 2017-01-02 01:06:39 UTC | #16

[quote="cadaver"]This actually sounds like it should be a good idea to be able to disable the Renderer's use of worker threads at will, if the main program itself is using workers heavily. Or there is a bug/inefficiency in the WorkQueue. It's better to take a slightly slower frame (typically even torture scenes run about only 1.5x max slower singlethreaded, as the use of work tasks is not as critical and widespread) than to hitch.[/quote]

Do you think that allocating a pool of lower priority threads along side some normal priority threads would yield higher performance than to not have any multi threading and pay context switching costs in the renderer?

-------------------------

cadaver | 2017-01-02 01:06:41 UTC | #17

Not 100% sure, but my guess is that by allocating your low-priority threads manually outside of WorkQueue you might avoid the large frame hitch problem. However, whether that's faster or not than singlethreaded rendering depends highly on the scene content. In light scenes the whole WorkQueue use presents only a small boost to the frame time, and it's highly dependent on the ability of the worker threads to wake up quickly when there's work to be done.

-------------------------

boberfly | 2017-01-02 01:07:18 UTC | #18

Having a bit of a think about this one again, let me know if this is a good idea Cadaver.

To reach SoA in Urho3D with SIMD fun in terms of being performant/practical without breaking the API too much (if at all), perhaps in the Node class instead of storing position/rotation/scale, this could be stored in the one class that has contiguous PODVectors and just store the offset in the node? And this class should store some flags or a mask too.

Sure for the logic in the node class itself it isn't a win as there's indirection to look into this offsetted PODVector (or doing a for loop on changing their translation/rotation/scale using this API), but if the object that stores this contiguous PODVector has a similar transforming API but batches the whole vector, this could be a win? The flags could be used to store masks so that those big batch operations only do those ops on things with the right flag/mask.

For things like batch-updating the renderer which may have a global buffer full of transforms, or to the physics engine where a bunch of objects need to be manipulated by a large field (gravity/turbulence/etc.) this would be a huge win which is sort of what the huge object count benchmark is doing, especially if that operation is SIMD...

Edit: Pretty much spelling out what Cadaver already has said, whoops :slight_smile: but I think the big benefit from structuring it this way would be if you were to move more of these large amounts of operations to the work queue or start to use Vulkan or DX12 where you don't need to mash so many draw calls and state changes, you just fill up constant buffers with transforms and throw it at the API in multiple threads.

A good candidate to try this on would be the bone nodes of a character, where you know up front how many bones are inside to allocate your PODVector (and align it with the constant buffer you'll throw at the rendering API). Could be its own component and mini AoS scenegraph inside perhaps, to not break the existing system...

-------------------------

cadaver | 2017-01-02 01:07:20 UTC | #19

The idea to have a flat array of SIMD-friendly transforms is echoed in places like gamedev.net, Ogre 2.x source code etc. so yes it sounds like what a high-performance modern engine should be doing.

However we would have to consider what is actually the place that needs to batch-process these transforms. Currently there isn't one, e.g. Bullet stores its own transforms and invokes a callback to move the transform back to the rendering side, and rendering code updates bounding boxes on demand, and if an object doesn't move, there's nothing to update.

I believe these are best explored in a proof-of-concept engine, for example something that uses the Urho Graphics sub-library but rewrites the whole scene handling. In Turso3D I actually didn't move far enough into this direction, it's still holding transforms in individual objects just like Urho.

-------------------------

sabotage3d | 2017-01-02 01:07:20 UTC | #20

If anyone is interested I stumbled upon this article for android  where they recommend SoA for performance: [android-developers.blogspot.co.u ... ented.html](http://android-developers.blogspot.co.uk/2015/07/game-performance-data-oriented.html)

-------------------------

