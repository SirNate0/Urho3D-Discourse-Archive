UrhoIsTheBest | 2020-07-02 05:52:37 UTC | #1

I just read the [original paper](http://hhoppe.com/proj/geomclipmap/), also the [GPU modification](https://developer.nvidia.com/gpugems/gpugems2/part-i-geometric-complexity/chapter-2-terrain-rendering-using-gpu-based-geometry).
I was shocked by the amazing performance.
It uses 200k * 100k heightmap (40G compressed to 300M), stores it in video card memory. Very good frame rate even in 2004! 16 years ago! They used the whole US heightmap (1arc resolution, ~30meter).
[youtube video demo](https://www.youtube.com/watch?v=yoUQRT-Hmcc&feature=youtu.be)

That exactly meets my requirement for a large terrain game. 

I wonder if anyone has tried to implement that in Urho3D or in their project?
Is it easy to integrated with Urho3D?
I cannot wait to try it!

-------------------------

