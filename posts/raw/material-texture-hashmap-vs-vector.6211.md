SirNate0 | 2020-06-17 22:14:58 UTC | #1

I was looking through the material code, and I was wondering why Material used a `HashMap<TextureUnit, SharedPtr<Texture> >` rather than a `Vector<SharedPtr<Texture>>` or even just a `SharedPtr<Texture>[(int)MAX_TEXTURE_UNITS]` to store its textures?

Even on a 64 bit system that should only require 128 bytes on Desktop, so ~8000 materials to get 1 Megabyte of extra memory used by using the fixed size array (assuming there were no textures in any of the material - the more units that are used, the less the comparative increase, and presumably at the point of having thousands of materials that will be negligible compared to the number of textures in use). From my (limited) understanding, using an array of contiguous memory should be faster than using the HashMap, and that would reduce checking if a texture unit is present to simply checking against nullptr rather than having to check the map.

Granted, I may have just missed something that should make it obvious, or may be misunderstanding the map-vs-array tradeoff.

-------------------------

QBkGames | 2020-06-19 04:39:38 UTC | #2

My (semi-educated) guess is that Urho3D development started a while ago before all the latest engine design hype of ECS, procedural programming and CPU cache optimizations. And in order to develop a general purpose engine you sometimes have to compromise performance in order to have flexibility (see also the Godot engine design philosophy document).

Having said that, I'm very convinced that there are many areas of performance improvement for Urho3D, but there just aren't enough developers around with the necessary time (and maybe skills) to work on them. But the greatest benefit of a free, open source project is that you can always go into the code and hack anything you want.
One of the first things I've hacked into my custom branch is a StringView hack. If you think your material is not optimized, how about every time you pass a String around (and that's everywhere), memory is allocated on the heap, the string is copied into that allocated block and that's just to pass it to a function and then when you return from the function the memory is released to the heap.
So yeah, there are many areas of improvements for sure, but the good thing is no one is stopping you from fixing them (at least in your own branch :slight_smile:).

-------------------------

Eugene | 2020-06-19 09:48:07 UTC | #3

I think the only reason is being simpler to use. With hash map, one always know how many textures are set and can apply only them. With vector, one have to check all the slots.

Having said that, I don't believe that this is a place that needs to be fixed. Not until it's proved otherwise.
You know, I can spend an evening listing things that are impacting performance _more_ than container used in material.

-------------------------

QBkGames | 2020-06-19 04:41:33 UTC | #4

Can you list a few major ones, I'm trying to squeeze the maximum performance for my game so I might look into hacking a few things if possible (at least in my custom branch)!?

-------------------------

Eugene | 2020-06-19 08:53:45 UTC | #5

Okay.

1) Scene Octree is fully traversed two times: to collect zones and occluders, and to collect geometries and lights. Even if you have no occluders, or only a few, Urho checks every single geometry for being occluder. So, double work for drawable collection. See `View::GetDrawables`.

2) Moreover, Octree traversal tend to be slower than brute-force in multithreaded environment.

3) Major part of `View` is single-threaded without any fundamental reason. Theoretically, all operations except rendering itself can be multithreaded. Practically, only `UpdateBatches` and `UpdateGeometry` are truly multithreaded in Urho. Lights processing is somewhat multithreaded too, but only if you have a lot of small lights. If you have single dominant light (i.e. any outdoors scene with sun), it's not multithreaded.

4) There's no real lighting option except using per-pixel lights. And they cause x2-xN triangle and batch count. If you want to make mobile game, you have to ensure you have one draw call per object in 95% of cases. But how would you do so if you need more than one light? Urho has no baked lighting. Urho *does* have per-vertex lights, but they are worthless. First, per-vertex lights are literally broken now (but this is fixable). Second, when limit of per-vertex lights per-object is reached, they "fallback" to pixel lights. This defeats the point, a bit. Third, when you have per-vertex lights and per-pixel light(s), *object is rendered at least twice, unconditionally*. This completely defeats the point of using per-vertex lights on mobiles.

5. Constant buffers are misused in Urho. Urho updates constant buffers before every draw op, even tho it is recommended to update constant buffers as rarely as possible.
This leads to one funny consequence. Constant buffers are supposed to be an optimization, but they actually make rendering slower and they are disabled in Urho OpenGL backend unconditionally. So, if you are using Urho DX11 backend, you receive penalty for using constant buffers all the time, because they are not optional in DX11. I actually did some crude testing with Urho Graphics backend. When I optimized constant buffers, I got about +10% FPS in stress test scenario. Don't blindly trust this number, tho, because I didn't do any propper testing and profiling.

This is what I remember right now. I'll update my post here if I recall something else later.

PS. In (4) I ignore Deferred rendering because it's not always acceptable option. But yea, you can use it and pray it will make things faster and not slower.

PPS. Yeah, I'm listing things that are hard to fix. If they were easy to fix, they would have already been fixed.

-------------------------

Eugene | 2020-06-20 15:10:55 UTC | #6

Oh, I've just remembered one more thing, about deferred render path this time.

6. Urho cannot tell if drawable is opaque (and can use deferred rendering) or translucent (and must use forward rendering) until the very last moment. Therefore, even if you enable deferred rendering and have no translucent objects, Urho will do significant part of forward-rendering-only stuff even if the results will never be used.

-------------------------

