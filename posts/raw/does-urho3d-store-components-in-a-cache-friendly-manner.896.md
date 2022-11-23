GoogleBot42 | 2017-01-02 01:03:54 UTC | #1

Title says it all.  I have a simple question.

Does Urho3D store components in a cache friendly manner?  For example, the latest version of [url=https://github.com/alecthomas/entityx]this project[/url] stores components in a cache friendly way.

-------------------------

cadaver | 2017-01-02 01:03:54 UTC | #2

No. Components are allocated with new from the heap when created.

However, there aren't actually any places in the code where it would need to iterate all components of a given type in order. For example Urho's rigidbody component just contains a pointer to the Bullet rigidbody object, and Bullet does all the heavy lifting of the physics simulation within its own data structures. Culling when rendering a view is another; we don't iterate all drawables, but rather those that are visible in the frustum.

A few weeks ago I profiled Ogre 2.1 which goes to quite significant pains to allocate the scene objects in a cache and SIMD friendly way. I did the 250 x 250 individual object test (20_HugeObjectCount), which on both Ogre 2.1 and Urho, results in the renderer first frustum culling all the objects, then forming instanced rendering batches of them. Urho was 2x faster :smiley:

-------------------------

GoogleBot42 | 2017-01-02 01:03:55 UTC | #3

[quote="cadaver"]A few weeks ago I profiled Ogre 2.1 which goes to quite significant pains to allocate the scene objects in a cache and SIMD friendly way. I did the 250 x 250 individual object test (20_HugeObjectCount), which on both Ogre 2.1 and Urho, results in the renderer first frustum culling all the objects, then forming instanced rendering batches of them. Urho was 2x faster :smiley:[/quote]

 :astonished:  That's crazy!  Wow!  I never would have guessed that the performance gap would be so great!

Just a quick question.  Will the rendering refactor update increase the speed even more?  Also will the rendering speed be improved for older versions of DirectX and OpenGL?  I use OpenGL 2.1. (yes my comp is pretty old  :confused: )

-------------------------

friesencr | 2017-01-02 01:03:56 UTC | #4

[quote="cadaver"]No. Components are allocated with new from the heap when created.

However, there aren't actually any places in the code where it would need to iterate all components of a given type in order. For example Urho's rigidbody component just contains a pointer to the Bullet rigidbody object, and Bullet does all the heavy lifting of the physics simulation within its own data structures. Culling when rendering a view is another; we don't iterate all drawables, but rather those that are visible in the frustum.

A few weeks ago I profiled Ogre 2.1 which goes to quite significant pains to allocate the scene objects in a cache and SIMD friendly way. I did the 250 x 250 individual object test (20_HugeObjectCount), which on both Ogre 2.1 and Urho, results in the renderer first frustum culling all the objects, then forming instanced rendering batches of them. Urho was 2x faster :smiley:[/quote]

I heard that last week. I twirled my mustache and laughed maniacally for you.

-------------------------

cadaver | 2017-01-02 01:03:56 UTC | #5

You can expect some CPU / memory related improvements across all APIs in the render-refactor branch, though not that dramatic. Note that the 2x measurement was done using that branch.

D3D11 will have less expensive state changes compared to D3D9, but I've also seen cases where D3D9 is actually faster; guess the driver vendors have optimized some cases like your standard "for (all objects) SetUniform(); Draw();" quite extremely. The full benefit remains to be seen. I did some Turso3D vs Urho3D tests earlier, where D3D11 looked like a clear winner, but those are not completely fair as Urho has far more features and more complex shaders. After finishing D3D11 I will examine GL3 vs GL2, where the only difference will be the use of constant buffers. I'm not expecting that large gains from that.

-------------------------

GoogleBot42 | 2017-01-02 01:03:56 UTC | #6

That makes sense.   :wink:   I really appreciate the effort of the Urho3D development team.  I am just a beginning CS student so I won't be of much help.   :confused:

-------------------------

cadaver | 2017-01-02 01:04:00 UTC | #7

Now I have some more test data from a complex scene with many objects & shadowcasting lights. On my dev machine D3D11 is 1.35x the speed of D3D9, which I find quite nice considering that the D3D11 code is still rather early yet.

-------------------------

hdunderscore | 2017-01-02 01:04:00 UTC | #8

That sounds great cadaver, looking forward to it!

-------------------------

