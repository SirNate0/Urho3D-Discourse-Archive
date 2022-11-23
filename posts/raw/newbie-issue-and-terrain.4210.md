fnadalt | 2018-05-02 12:25:14 UTC | #1

Hi! I'm trying to implement a large terrain. My idea is to build individual Terrains (chunks) from their own height maps, and stitch them together, unloading and loading accordingly while the player walks through the "chunks" of Terrain. The entire heighmap is chopped into several 128x128 pieces. Just for testing, I created a Terrain and its N/S/W/E chunks using SetNeighborss. Each individual Terrain component is only 96x96!!! I don't understand what's going on. If you want to check out: https://github.com/fnadalt/world. Thanks!

-------------------------

Bananaft | 2018-05-14 12:31:14 UTC | #2

Hi, wellcome to the forum!
I had similar problem:
[quote="cadaver, post:2, topic:1040, full:true"]
Terrain heightmap needs an odd number of points so that the mipmapping works properly while the patch edges remain in place. For example 129 x 129, 257 x 257.
[/quote]

-------------------------

