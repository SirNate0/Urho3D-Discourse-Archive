feltech | 2018-03-19 23:10:39 UTC | #1

Hey all,

I want to create a simple space sim/trading game (yes, another one, but wait, there's a catch!)...  I want to fully physically simulate all AI ships in the universe - even those far from the player.  The idea is to use extremely simple geometry, so that 1000s of bodies can be simulated at real-time rates.

The problem I'm trying to wrap my head around is the floating point accuracy issue.  Even with double-precision at 1cm resolution you only get approx 0.01 light years (approx 16 sig figs in a double, with cm resolution, is 10^14 m = 0.01 light years).

Reading around these, and other, forums, it seems the way to solve this is a hierarchical coordinate system, i.e. chunking or tiling the world.  Unfortunately, as far as I can tell Bullet is just not set up for this at all.

I have a couple of ideas, e.g. an entirely separate physics world per tile; or re-centring entities relative to their local tile with a "broadphase" plugin to exclude all entities not on that tile. 

The main thing I'm struggling to wrap my head around is how to handle movement and collision detection across (i.e. on the edge between) world chunks/tiles.  I'm fairly sure this is a solved problem, but I can't find any specific information about it on the web.

Anyone got any ideas?

-------------------------

Bananaft | 2018-03-20 19:31:16 UTC | #2

How many light years will comply? :slight_smile: 

Start small, try to get maximum performance from single bullet physics world, like one tiny solar system or asteroid field. It will provide you good learning and you will be able to grow your universe from there.

-------------------------

feltech | 2018-03-21 13:39:35 UTC | #3

I think that the problem of tiling the world needs to be tackled from the start, since it affects the internals of the engine.

I've had some more thoughts on this. I propose that all entities have a real-valued position relative to their current tile.  As far as Bullet is concerned, they would all inhabit the same small region of space. 

Then, we have a (pre-)broadphase that will filter down to entities in a single tile.  There is already similar functionality in Bullet via the collision object mask, but it has insufficient bits for this purpose.  Hopefully it will require limited modification to support tile coordinates, rather than a bitmask, though.  Or perhaps it will be more performant to roll something new.

The real trick, as I mentioned in my previous post, is what to do at the edges between tiles.  I think in that case we need to get deeper into Bullet's collision detection to re-centre the origin at the midpoint between two tiles, and compare pairs of entities across the tiles. 

That is, in a separate pass, use a list of pairs of inhabited tiles that neighbour one-another. Then, check pairs of entities (AABB overlap and the rest) across the divide, with the origin centred at the midpoint between the two tiles.

I've only got passing familiarity with some of Bullet's collision detection code, and very little familiarity with the collision response code, so I'm not sure how viable this is.

Anyone got any comments/suggestions/alternatives on this idea?

-------------------------

Bananaft | 2018-03-21 21:19:52 UTC | #4

Yeah, one more thing. Given, you have so enormously huge open spaces, spaceships will probably fly around on ridiculous speeds. And that means they will fly through everything and each other, as each frame they will move a great distance, even continuous collision detection won't cover that. Sweep test may work alright but only for collision with static geometry.

>collision detection across (i.e. on the edge between) world chunks/tiles.

proxy-collider that checks collisions in adjacent chunk and passes impulses to real object.

-------------------------

Leith | 2019-01-02 09:11:20 UTC | #5

Just a thought - The scene octree could be modified to be aligned more closely to Bullet's spatial tree, this could mean regions of the octree could be considered as separate physics worlds, with well-defined volume boundaries. This could be an extension of the existing octree, rather than a whole new work, so it would not need to disrupt standard visibility testing etc.

-------------------------

I3DB | 2019-01-02 20:57:40 UTC | #6

You could maintain a physics world size of a reasonable space size, and translate each area of interest into that space, while maintaining it's normal position outside your physics world space for viewing.

So in effect you have two locations for each and every object. It's translated location for physics world processing, and it's visible location.

But if you take a look at the Feature Sample 'Physics Stress Test' you'll get an idea of the number of objects tracked before things go awry.

-------------------------

