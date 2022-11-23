NessEngine | 2019-03-16 20:45:54 UTC | #1

Hi all,
Is it possible to set multiple materials on the same geometry (of a static model) during runtime from code?
Or maybe there's a better way to do what I want - multiple textures on the same plane with different UV, color, depth bias and other material-related properties. Any ideas?

Must happen from code, as materials are generated at runtime..

Thanks!

-------------------------

Modanung | 2019-03-17 08:51:29 UTC | #2

You something like Quake III's multi-textures? I think you'd have to write a custom shader for that.
[quote="Leith, post:7, topic:5036"]
...you can use an existing multi-texture blending shader, such as the terrain shader...
[/quote]

...or use multiple geometries (or models) on the same location.

-------------------------

NessEngine | 2019-03-16 21:18:07 UTC | #3

[quote="Modanung, post:2, topic:5036"]
…or different geometries (or models) on the same location.
[/quote]

Thanks! Since its a simple geometry it wouldn't be that bad, but how do I avoid the z-fighting? For some reason even with depth bias I'm seeing flickering (or maybe I just didn't use depth bias properly?)

-------------------------

Modanung | 2019-03-16 21:25:28 UTC | #4

Depth bias is exactly what should prevent that. What values are you using? Negative values bring a surface towards the camera - as it were - and should be pretty small: Generally below 10<sup>-5</sup>.

-------------------------

NessEngine | 2019-03-16 21:27:42 UTC | #5

That's what I'm trying :) Specifically -0.000025. I'll try to play with values a bit more to make it work.
Thanks!

-------------------------

Modanung | 2019-03-16 21:31:47 UTC | #6

The cursor's material in Edddy uses `<depthbias constant="-0.0000023"/>`.

-------------------------

Leith | 2019-03-17 04:00:58 UTC | #7

Are you certain you require separate UVs per material? This requires that the vertex geometry supply multiple UV sets.
If you can use a fixed set of textures that share a common uv per vertex, then you can use an existing multi-texture blending shader, such as the terrain shader, and apply it to any geometry that provides for at least one uv.

-------------------------

Leith | 2019-03-18 09:05:28 UTC | #8

Blending shaders avoid all z-fighting, by choosing a texel from one of N input textures, and blending the inputs in some additive way to the output pixel. There is no z-fighting in that use-case. And, there is no overdraw. Multiple objects at the same position and rotation is likely to cause z-fighting, when a slightly more sophisticated shader can do it.

-------------------------

NessEngine | 2019-03-21 19:25:18 UTC | #9

Hi sorry for not replying I just saw your reply.
Unfortunately I do need different UVs so I can't use your suggestion. Thanks though! :)

I ended up using layers and getting depth bias to work.

-------------------------

