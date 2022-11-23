Sunc | 2022-03-11 11:36:48 UTC | #1

Obviously GPU rasterization makes better performance to fetch the depth buffer，so what is the reason to do it by CPU?

-------------------------

Sunc | 2022-03-11 12:07:22 UTC | #2

As I considered a while, I guess the main reason is the cost of fetching GPU render buffer.
Although morden devices support hardware depth reading, but software rasterization makes the best device compability.
And if reduce the mesh quantity threshold, CPU does'nt get overwhelmed.

-------------------------

Eugene | 2022-03-11 13:31:35 UTC | #3

[quote="Sunc, post:2, topic:7216"]
As I considered a while, I guess the main reason is the cost of fetching GPU render buffer.
[/quote]
Also, GPU depth buffer is outdated by 1 frame, so you need more complex algos.
Also, it was written by the time of DX9, I am not sure how good is DX9 at depth fetching to CPU

-------------------------

JSandusky | 2022-03-13 02:39:16 UTC | #4

[quote="Sunc, post:2, topic:7216"]
As I considered a while, I guess the main reason is the cost of fetching GPU render buffer.
[/quote]

It's less *cost* so much that a blocking readback will stall, and still be a frame late. Reading back isn't particularly expensive if you can wait 2-3 frames while you let the map await fail while not touching the resource in question.

Hardware occlusion queries are a management headache and since the OcclusionBuffer is also used to cull entire octants of the octree (huge win) the query management would probably be out of control in scale.

Pros and cons all around.

-------------------------

