friesencr | 2017-01-02 01:05:35 UTC | #1

I have a situation where I generate some procedural content.  The most compatible interface is via the deserializer.  This way stuff can get loaded in full from disk or otherwise.  I made a deserializer I call Generator.  It is simultaneously a resource and a deserializer.  It has an option parameter hash that gets used on a callback when Read is called. 

[github.com/urho3d/Urho3D/compar ... :generator](https://github.com/urho3d/Urho3D/compare/master...friesencr:generator)

I added a dumb example of it copying a filestream to the destination pointer.

Does anyone likes this idea enough for me to polish and submit a pull request?  Almost all the resource types are too hard to generate by hand so this has a very limited use case.  In the case where the thing holding the resource creates the memory the memory of the procedural content has to be saved to the Generator.

I have a different branch where I have opengl texture arrays, texture buffers, unsigned integer vertex support. Texture buffers are less practical without the texelFetch in gl2.  I have been having lots of fun.  There was a good week or so where I lived in the render loop.

-------------------------

cadaver | 2017-01-02 01:05:35 UTC | #2

It looks like a workable idea. I guess that for example a procedural image generator needs to generate also the image header (PNG/BMP/whatever) so it's slightly hardcore.

If you can supply a new C++ sample and create a brief documentation page for it it could well go into master.

-------------------------

friesencr | 2017-01-02 01:05:44 UTC | #3

After playing around with this for a while it is kind of sort of working in practice.  Holding a pointer to a Deserializer is posible but they aren't supposed to be a long lived instance, they are really supposed to be a transient.  All of the current reloading happens via xml special cases, shadow data, or file watcher events.

I still like the idea of the generator but in practice but it seems like the idea of there being a generic way to recover/reload a resource after it has been loaded is lacking.  Can anyone think of a good way of handling this in Urho?

-------------------------

