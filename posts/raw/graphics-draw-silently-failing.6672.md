SirNate0 | 2021-01-23 06:20:09 UTC | #1

The various `Graphics::Draw(...)` calls all seem to start with something along the line of an if check ensuring the state is acceptable and possibly a compiler define check (example below). If the conditions are not met, Draw just silently returns, making it impossible to tell if the call succeeded from both the calling code (e.g. a boolean success state return) and from the log. 
```
#if !defined(GL_ES_VERSION_2_0) || defined(__EMSCRIPTEN__)
    if (!indexCount || !indexBuffer_ || !indexBuffer_->GetGPUObjectName() || !instancingSupport_)
        return;
```
This ended up making it a ~3 hour process to figure out why the ImGui integration was failing to draw on an Emscripten build, rather than a ~3 minute process. As such, I was wondering if adding at least a log message would be acceptable, something like 
```
#if !defined(GL_ES_VERSION_2_0) || defined(__EMSCRIPTEN__)
    if (!indexCount || !indexBuffer_ || !indexBuffer_->GetGPUObjectName() || !instancingSupport_)
    {
        URHO3D_LOGERROR("Invalid call to Graphics::DrawInstanced(PrimitiveType type, unsigned indexStart, unsigned indexCount, unsigned minVertex, unsigned vertexCount,
    unsigned instanceCount)");
        return;
    }
...

#else
    URHO3D_LOGERROR("Unsupported draw call Graphics::DrawInstanced(PrimitiveType type, unsigned indexStart, unsigned indexCount, unsigned minVertex, unsigned vertexCount,
    unsigned instanceCount)");
#endif
```

Does this sound like a good idea? The main exception I can think of is that a call to Draw with 0 indices could be viewed as succeeding by doing nothing, so that case should possibly be excluded from logging the error.

-------------------------

Eugene | 2021-01-23 17:57:46 UTC | #2

[quote="SirNate0, post:1, topic:6672"]
As such, I was wondering if adding at least a log message would be acceptable
[/quote]
The downside -- huge amount of errors will overflow logs and it may hide more inportant errors in the begining. "No logging in render loop" policy has its reasons. I dunno what's better.

-------------------------

JSandusky | 2021-01-23 22:31:52 UTC | #3

> Resized scratch buffer to size X

Great Destroyer of logs.

-------------------------

WangKai | 2021-01-24 04:35:53 UTC | #4

When there is something we submit but not rendered, we can use graphics debugger to investigate.

-------------------------

SirNate0 | 2021-01-24 05:12:58 UTC | #5

I don't think I've ever used a graphics debugger, but I also haven't done any significant work on shaders for a few years. Would it work in this case though, as Urho never calls the graphics API to have it draw? And would it work for all the platforms (e.g. Web)?

-------------------------

JSandusky | 2021-01-24 09:12:06 UTC | #6

Won't help in this case (as you said, it's not even being called) and HTML5/WebGL debugging is a mess anyways.

Graphics debugger is more useful for understanding how the high-level is acting, how the vertex-shader is transforming things, and what the graphics state is at different times (like finding sticky state or confirming viewports are reasonable in shadow-atlasing).

Serious question is why this is even being hit at all. There are valid draw cases for unindexed draws with null vertex buffers (merge-instancing), but none for indexed draws with invalid index buffers. I assume it's the instance support bool failing? Even though WebGL2 should have that ... isn't that like mandatory to claim WebGL2 support? Bug in feature detection maybe or Mozilla browser being Mozilla (AKA: crap)?

-------------------------

vmost | 2021-01-24 13:16:44 UTC | #7

Could you add a static variable, and only log the first e.g. 5 instances of failures? Then add a log message "Exceeded log limit, these errors won't be logged again..."

-------------------------

SirNate0 | 2021-01-24 14:04:25 UTC | #8

[quote="JSandusky, post:6, topic:6672"]
Serious question is why this is even being hit at all.
[/quote]

To clarify, this check is not one I actually had fail. It was `void Draw(PrimitiveType type, unsigned indexStart, unsigned indexCount, unsigned baseVertexIndex, unsigned minVertex, unsigned vertexCount)` due to a lack of GL3 support (I'm assuming this actually means GL ES 3, but the variable/function doesn't specify). I just provided the other as an example of the `#ifdef`.

-------------------------

