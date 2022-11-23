slapin | 2017-04-28 09:08:58 UTC | #1

While working on character cutomization and processing Geometry class I wonder why
can we have multiple VertexBuffer per geometry but just single IndexBuffer.

How do IndexBuffer relate to multiple VertexBuffers?

-------------------------

Eugene | 2017-04-28 09:36:59 UTC | #2

IB <-> VSs relation is the same as before. The only exception is that data of single vertex is fetched from several VBs instead of one.

-------------------------

slapin | 2017-04-28 09:40:05 UTC | #3

How can I distinguish which data go from which VB?

-------------------------

slapin | 2017-04-28 09:44:42 UTC | #4

Another question while we're here - we have SEM_BLENDINDICES data which is 4 bytes
Is it just bone number? Does 0 have special meaning?

-------------------------

Eugene | 2017-04-28 10:40:28 UTC | #5

> How can I distinguish which data go from which VB?

VertexElement description must have a kind of VB index or stream index.

> Is it just bone number? Does 0 have special meaning?

Yes. No.

-------------------------

slapin | 2017-04-28 11:21:58 UTC | #6

can I expect that vertexBuffers[x].vertexElements[y] will always reference VB x, or is it shared upon
all VBs?

-------------------------

Eugene | 2017-04-28 11:34:03 UTC | #7

[quote="slapin, post:6, topic:3062"]
vertexBuffers[x].vertexElements[y] will always reference VB x
[/quote]

May you please re-phrase this part?

-------------------------

slapin | 2017-04-28 11:40:15 UTC | #8

each VertexBuffer have array of VertexElemant.
Can I rely that each array will contain elements belonging to corresponding VB or
these arrays are shared upon all VBs?

-------------------------

slapin | 2017-04-28 12:08:37 UTC | #9

This is what I currently do -

https://gist.github.com/anonymous/f15f99e8dac5de8ca37413b5969e522b

I set current model's IndexBuffer so that it will not contain vertices with blendindices not in range.
Am I on right way or I'm doing something wrong?

-------------------------

Eugene | 2017-04-28 12:18:42 UTC | #10

[quote="slapin, post:8, topic:3062"]
each VertexBuffer have array of VertexElemant.
[/quote]

Huh, I've forgotten about this implementation detail...
Yes, you can rely. VertexElement array describe elements stored in corresponding VB.

Elements from multiple VBs are "merged" into single set of elements before passing into Vertex Shader.

-------------------------

slapin | 2017-04-30 03:49:45 UTC | #11

@Eugene could you please help me again,
As I understad, Geometries with lod > 0 all share VB with Geometry with lod = 0, am I right?
But each Geometry with lod = 0 can have its own VB. Is it correct?

-------------------------

Eugene | 2017-04-30 05:40:41 UTC | #12

LODs don't have to interfer with each other, so every LOD could (but don't have to) have its own set of buffers.

-------------------------

slapin | 2017-04-30 05:42:27 UTC | #13

Well, when I tried generating LODs, when I added extra buffers for LODs it did not work for some reason...

-------------------------

