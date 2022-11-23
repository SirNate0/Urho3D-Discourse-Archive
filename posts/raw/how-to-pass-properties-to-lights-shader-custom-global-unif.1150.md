Bananaft | 2017-01-02 01:05:44 UTC | #1

So I hacking and messing with differed lighting. And I need a way to pass some extra properties to Directional Light. There will be always only one directional light, so this properties may be global. What is the easiest way to do it?

-------------------------

friesencr | 2017-01-02 01:05:44 UTC | #2

Without modifying any of urhos source you will have to add a parameter to every material that gets rendered.

If you modify the source you get more options.  The light queue process in the batch seems like a good place:

[github.com/urho3d/Urho3D/blob/m ... h.cpp#L306](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/Batch.cpp#L306)

-------------------------

Bananaft | 2017-01-02 01:05:44 UTC | #3

Thank you for such quick reply.
[quote="friesencr"]Without modifying any of urhos source you will have to add a parameter to every material that gets rendered.[/quote]
Yeah, that's kind of thing I want to avoid, especially with deferred lighting.

[quote="friesencr"]If you modify the source you get more options.  The light queue process in the batch seems like a good place:

[github.com/urho3d/Urho3D/blob/m ... h.cpp#L306](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/Batch.cpp#L306)[/quote]
Thanks for the link, I'll study it up.

I think, separate renderpath quad-command may also work for me, since you can add custom uniforms for it, and even change them from script. And directional light is just a screen sized quad as well.

-------------------------

