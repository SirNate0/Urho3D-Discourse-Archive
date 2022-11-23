gulaghad | 2017-01-02 01:04:02 UTC | #1

Hello,
I am new to Urho3d. When I modify the DynamicGeometry example to use multiple vertex buffers instead of single interleaved one, I get an ERROR: Stream index out of bounds.

Here is what I am doing. DynamicGeometry.cpp (whole file): [url]http://pastebin.com/NnG2Ef1Y[/url]
[pastebin]ZfdH8guW[/pastebin]

-------------------------

cadaver | 2017-01-02 01:04:02 UTC | #2

You need to call SetNumVertexBuffers() on the Geometry first.

-------------------------

