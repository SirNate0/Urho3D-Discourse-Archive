mcmordie | 2021-01-13 18:59:08 UTC | #1

For application specific reasons I must render to a texture and then retrieve that texture back into system memory.  This is currently painfully slow (~10 fps) and results in CPU and GPU idle bubbles.  It would help if I could either use the GPU to handle the blitting or overlap the GetData with the beginning of the next frame.  Are either of these options viable in Urho3D D3D9 / D3D11 or OpenGL?

I noticed there is a project to implement this functionality as a plugin for Unity:

[https://github.com/SlightlyMad/AsyncTextureReader](https://github.com/SlightlyMad/AsyncTextureReader)

Not sure how well it works, but I was looking through the code to see if I could staple this into what I have in Urho3D as a starting point.

-------------------------

Eugene | 2021-01-13 21:16:32 UTC | #2

TL;DR: There is no async API for GAPI objects in Urho.

Try calling GetData in the beginning of next frame and remove/cache all redundant work from it
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/Direct3D11/D3D11Texture2D.cpp#L327

-------------------------

mcmordie | 2021-01-13 23:16:56 UTC | #3

[quote="Eugene, post:2, topic:6658"]
and remove/cache all redundant work from it
[/quote]

Thanks for your response.  I didn't understand this: how would I identify what work is redundant and cache or remove it?

Also: is D3D11 the fastest way to run this in Windows or should I try either OpenGL or D3D9?

-------------------------

JSandusky | 2021-01-14 19:17:42 UTC | #4

Your best possible situation is to split it up. You'll end up with a stream of readback-tasks.

Fire off the readback like it was any other graphics-call.

Then do the actual map and read later so you aren't forcing the CPU to wait until the GPU has copied everything into staging-texture's CPU-local mem has finished until you truly must. You can use DO_NOT_WAIT in the map call to return an error if it would have blocked (then you handle it again later when it finally doesn't return an error).

If you can't wait a frame or 2 you're kind of sunk so you'll either need to rework your stuff to understand that there's a delay, or swallow the wait and settle with at least not blocking for the whole time.

-------------------------

Eugene | 2021-01-14 07:45:56 UTC | #5

[quote="mcmordie, post:3, topic:6658"]
Thanks for your response. I didn’t understand this: how would I identify what work is redundant and cache or remove it?
[/quote]
I linked relevant line of code that causes a lot of delay (besides GPU-CPU sync): `CreateTexture2D`

[quote="mcmordie, post:3, topic:6658"]
Also: is D3D11 the fastest way to run this in Windows or should I try either OpenGL or D3D9?
[/quote]
I never tested it.

-------------------------

mcmordie | 2021-01-14 18:15:38 UTC | #6

[quote="Eugene, post:5, topic:6658"]
I linked relevant line of code that causes a lot of delay (besides GPU-CPU sync): `CreateTexture2D`
[/quote]

Okay makes sense & thanks for the clarification.  To my understanding (not a D3D person), the staging texture is needed and certainly when I attempt to copy directly from the texture I get an empty buffer.

With reference to this I am going to try rotating the staging textures and of course keeping them in a queue rather than creating them on the fly:

[https://stackoverflow.com/questions/40808759/id3d11devicecontextmap-slow-performance](https://stackoverflow.com/questions/40808759/id3d11devicecontextmap-slow-performance)

-------------------------

mcmordie | 2021-01-14 18:19:24 UTC | #7

[quote="JSandusky, post:4, topic:6658"]
Then do the actual map and read later so you aren’t forcing the CPU to wait until the GPU has copied everything into staging-texture’s CPU-local mem has finished until you truly must. You can use DO_NOT_WAIT in the map call to return an error if it would have blocked (then you handle it again later when it finally doesn’t return an error).
[/quote]

Makes sense and I think this aligns with the approach listed in the StackOverflow post-- the ResourceCopies are necessary, but apparently they can overlap with other GPU work if the staging buffers are used in sequence?

-------------------------

Eugene | 2021-01-14 19:17:42 UTC | #8

Simplest thing you can try is to keep staging texture created in texture itself, and call GetData in the beginning of next frame. See if it makes things better.

-------------------------

mcmordie | 2021-01-14 19:19:13 UTC | #9

Alright, using a ring buffer of staging textures was good enough to get me from 60 to 98% GPU utilization.  Not sure which one of you to click solution on, thank you both for your help on this!

-------------------------

