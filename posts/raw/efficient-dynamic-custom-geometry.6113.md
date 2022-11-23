najak3d | 2020-04-23 07:03:42 UTC | #1

We are making good headway with Urho3D for our port to 3D.

One thing our mapping app does is deals with 1000's of dynamic lines, rendered over a map, and bodies of water (filled shapes).  We have it all rendering very nicely now (anti-aliased lines with outlines)... but need to make it more efficient.

How do you modify Custom Geometry vertex locations from UrhoSharp?  Does it allow access to modify the actual vertex data directly?  Or do you have to modify it in a source array and just use "SetData()" to set the new data (which means you need two copies)...   Namely, since we change it so often, we're wanting to NOT thrash memory by recreating a new data array in memory each iteration.  Instead we'd just like to modify vertex data in-place, and re-use it (no memory allocations required after the first big one).

Does anyone have hints about the more efficient way to do this?

-------------------------

SirNate0 | 2020-04-23 12:23:53 UTC | #2

VertexBuffer, at least, has a "[SetDataRange](https://urho3d.github.io/documentation/1.7/class_urho3_d_1_1_vertex_buffer.html#a20dd4ccb7666c5acc1abcf5034fcea00) (const void *data, unsigned start, unsigned count, bool discard=false)" method that seems to allow what you would like. I don't know that this behavior is exposed I'm the CustomGeometry class, you may have to switch to using a Model with regular Geometry instances that you update the VertexBuffers for. Possibly it is handled internally in CustomGeometry, likely in the Commit method, but I am guessing it's not. I didn't check the source, so I can't say either way.

I do have a recommendation, though. If this is not what you're doing, feel free to ignore it, this is mostly a guess. It sounds like you're adding all of your lines/models/something to the same large custom geometry and then wish to update them, probably as the user moves around the map? If that is the case, I would switch to a tile- or chunk-based system where you decide the map into smaller sections that become an unchanging set of data, and then unload the distant tiles when the user gets to far away/as memory usage requires.

Also, I'm glad you got your initial version working so quickly. Congratulations on the progress!

-------------------------

najak3d | 2020-04-23 15:20:18 UTC | #3

Thank's I saw that SetDataRange() and we'll try that today.  It seems to be exposed in UrhoSharp as well.

We'll do a programmatic stress test to verify that whatever we do won't be an issue.  We do have tiled data, but the presentation of this data will be swapped out for new data frequently.  Where possible, when the new data comes in, we just want to *overwrite* the memory where the previous data existed (pooling techniques), and just wanted to make sure that we can do something fairly efficient in this manner.

Are there ANY contributors still hanging out here?  This is odd, because Microsoft Xamarin STILL calls UrhoSharp the best solution for 3D in Xamarin.  And we spent a week looking for something better (and more alive) and could not find anything better.  Urho is it for us, it seems.

-------------------------

