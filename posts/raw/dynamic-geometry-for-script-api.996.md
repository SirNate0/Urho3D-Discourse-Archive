Bananaft | 2017-01-02 01:04:41 UTC | #1

I noticed, there is no 34_DynamicGeometry example for script api, and there seems like no way to set and alter VertexBuffers from the script.

Well, that's pity, would be nice to be able to play around with VertexBuffers from the script too.

-------------------------

cadaver | 2017-01-02 01:04:42 UTC | #2

It should be possible to allow SetData() from a VectorBuffer into a Vertex or Index buffer. In script, you would then use WriteVector3(), WriteUInt() etc. to fill the data. This is not optimal compared to how you would do it in C++, but probably about the best you can get, as there can be no true freeform memory access in script.

-------------------------

Bananaft | 2017-01-02 01:04:42 UTC | #3

I see. Even if it will be super slow, It's still interesting for generating things once, at the start of the game.

-------------------------

cadaver | 2017-01-02 01:04:51 UTC | #4

VertexBuffer, IndexBuffer & Geometry classes are now exposed to script in the master branch, and DynamicGeometry example has been ported to AngelScript & Lua. More esoteric features like defining morphs and skeletons programmatically are not there (at least yet) but this should allow basic non-skinned dynamic geometry generation & update.

-------------------------

Bananaft | 2017-01-02 01:04:54 UTC | #5

Great, thank you. Can't wait to try.

-------------------------

