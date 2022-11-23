OakenBow | 2017-01-02 01:15:43 UTC | #1

Essentially, I'm trying to make a Terraria-style 2D block game. The way I'm currently trying to organize it is a region of 4*4 chunks of 32*32 blocks each, giving each region 2^14 blocks (which I might end up changing to 4*4 * 64*64). I'm going to use a node for each region/chunk, but was wondering if it's more efficient to give each block its own node or try to somehow make a new texture for the chunk (current idea is a 2D array of ints) each time it's modified (sorta like how 3D voxels have to regenerate the mesh each time). I'm mainly asking because if each region has 16,384 nodes (or  65,536 with larger chunks) in it for terrain alone, node and sprite counts are going to spike rather quickly.

-------------------------

szamq | 2017-01-02 01:15:43 UTC | #2

The node approach is overkill and useless, node contains information like position rotation and scale which you already know about each block.
You need to make an array or something better, that will merge surrounding blocks with same material into one (quadtree?)

-------------------------

