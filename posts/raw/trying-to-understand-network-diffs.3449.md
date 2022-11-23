TheComet | 2017-08-15 09:22:03 UTC | #1

For the game I'm writing, I have a 2D tilemap where each tile stores a list of properties (claimer ID, timeout period, etc.) and I'm wondering what the best method is to synchronize this over the network.

Each tile can potentially update at any point in the game, so obviously I don't want to send the entire tilemap whenever this happens, just the tiles that have changed.

If I do a thing where I have an object that implements ```Serializable``` and it writes the entire tilemap using the Load() and Save() methods, will the network code be smart enough to generate a good diff from that? Or will it just send the entire tilemap?

-------------------------

cadaver | 2017-08-15 09:39:45 UTC | #2

The network code works on attribute level. If an attribute has changed, it will send it over whole. Serializable's Load() & Save() are actually not being called in network serialization, so you can't rely on them.

Doing what you want might be possibly done best using custom messages.

-------------------------

TheSHEEEP | 2017-08-15 09:45:12 UTC | #3

Not sure what you are doing, but at least in RTS games, the solution is determinism.
Everything must happen in exactly the same way for all players. Which is very much doable (even for RNG if you use same seeds) - but you have to plan for it and design your code accordingly.

And if everything happens in the same way, all data you need to send around is user input.

Of course, that completely circumvents any (or most) need of any Serializable for most game objects, reducing the data sent to an absolute minimum.

Personally, I find that approach easier than having to worry about attribute weight of every single object. Plus, your code gets leaner as all your game objects have one less layer to worry about. You "just" have to make sure your simulation is "airtight". But YMMV ;)

-------------------------

TheComet | 2017-08-15 10:45:46 UTC | #4

Ideally this would be the way to go, agreed. However, my game uses physics simulations to interact with the tiles, and Bullet is inherently non-deterministic.

@cadavar I'll look into custom messages, because I think there is an opportunity here to define a clean "API" to interact with the tilemap.

-------------------------

TheSHEEEP | 2017-08-15 11:04:29 UTC | #5

[quote="TheComet, post:4, topic:3449, full:true"]
Ideally this would be the way to go, agreed. However, my game uses physics simulations to interact with the tiles, and Bullet is inherently non-deterministic.
[/quote]

Yeah, that is the largest drawback of Bullet. If you really need to use physics for game logic, I don't even know if there is a deterministic physics engine...
I don't think that is easily doable due to floating point shenanigans.

-------------------------

Eugene | 2017-08-15 11:08:51 UTC | #6

[quote="TheSHEEEP, post:5, topic:3449"]
Yeah, that is the largest drawback of Bullet. If you really need to use physics for game logic, I don’t even know if there is a deterministic physics engine…
[/quote]

I heard about non-production fixed-point physics engines...

-------------------------

DrAlta | 2017-08-15 12:29:17 UTC | #7

For Deterministic physics engines there is the proprietary DPhysics for Unity and The Open Source [Boulette Physiques](https://github.com/yoanlcq/boulette-physiques)  Both appear to be 2D.  Newton Dynamics is as deterministic as floats allow if single threaded.

-------------------------

