slapin | 2017-03-18 02:31:46 UTC | #1

Hi, all!

I have graph of intersections and line segments. I want to make 3D mesh of roads out of it.
While segments are quite simple (can generate a few triangles forming quads) I try to make
intersection shapes. I can take direction vectors of roads from each intersection and use 2D normals to left and right to
get all needed points, but I need to sort them and generate triangular mesh out of result. Any ideas?
I did this before using various algorithms, but these are slow and error-prone. Is there some reliable way to
do this>

-------------------------

SirNate0 | 2017-03-20 19:41:19 UTC | #2

Are all intersections guaranteed to be at a node, or can they occur coincidentally at the middle of line segments?

-------------------------

slapin | 2017-03-21 05:57:16 UTC | #3

well, they're guaranteed to be at node, otherwise it ia a graph generation bug.

-------------------------

