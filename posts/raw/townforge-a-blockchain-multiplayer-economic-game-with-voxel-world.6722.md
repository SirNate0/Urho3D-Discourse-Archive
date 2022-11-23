townforge | 2021-02-18 21:59:21 UTC | #1

Hi,

Townforge is a blockchain based game, where you building structures and try and outcompete other players. The core is an economic game, where creating buildings costs money and you try to get more income from those buildings than you spent in the first place.

The expenses and income from those buildings are recorded on the chain, and are thus made in "real" money which can be exchanged between players (and mined as a normal blockchain). There is a builtin chat, decentralized marketplace, and a player may specialize in various ways to make a living in the game. 

There is a 3D world that goes with it, where players can optionally build freestyle models for their buildings, Minecraft style. The terrain is procedurally generated and practically infinite.

The game runs on Linux, Windows, and Mac.

Being based on a blockchain, this is an inherently multiplayer game, and it is currently in testnet (ie, beta) so any currency mined at the moment will be erased once the final mainnet starts. This makes it a great time to experiment to get acquainted with the game rules.

Here's a video of building a Pegasus statue in game: https://youtu.be/6DcvsUn99_k

And a screenshot:
![](https://i.imgur.com/LVWRQwU.png)

There's a website at https://townforge.net. A manual and a FAQ are there, they're good reads if you're interested.

-------------------------

1vanK | 2021-02-18 22:58:14 UTC | #2

I'm interested in the technical side of the game. How much did you have to change the engine and what exactly did you add to it? Perhaps there is something useful that we could add to the main repository.

-------------------------

townforge | 2021-02-19 00:07:40 UTC | #3

I changed a number of things. I PRed some of them (with varying success, given the changes are made to adapt the engine to my particular needs, so not always so generic). They're the ones PRed as moneromooo ^_^ A lot of the changes are for speeding up terrain generation, as it's created on the fly as the player moves around the infinite procedural terrain.

All my changes can be found in https://git.townforge.net/townforge/Urho3D/commits/branch/cc

-------------------------

evolgames | 2021-02-19 19:40:40 UTC | #4

How do you handle generating terrain on the fly?
Are you using heightmaps and modifying those or some other method?
Really cool concept!

-------------------------

townforge | 2021-02-19 20:58:44 UTC | #5

The (practically infinite) terrain is divided in 256x256 chunks. The displayed area is a 2N+1 x 2N+1 set of chunks, with N set by the player (the larger the N value, the farther you can see). The camera is kept in the center chunk. If it moves out of it the grid is moved to reset the camera in the center chunk, and new chunks are created at the missing edge to replenish the grid.

New chunks are procedurally created using a number of coordinate based deterministic noise functions, including simplex noise and similar. Various maps are created (height map, and various "resource" maps that dictate how good a given tile is at a given thing, like wood generation, ground stability, etc).

For the height map, I adapted code from "Realtime Procedural Terrain Generation" by Olsen. Since it's a blockchain game and all game actions have to abide by the consensus rules, everything has to be exactly deterministic and reproducible, so I changed the algorithm to cater for that, all based on coordinates.

If you create a new city, you control a seed which generates new maps, in an practically infinite way.

Graphically, this is using the Urho3D Terrain system, to which you can pass an image as height map. The resource maps use the texture to show resource suitability as a greyscale map.

-------------------------

evolgames | 2021-02-23 01:01:59 UTC | #6

Oh cool thanks so much for the explanation. I've been curious about techniques for this in Urho, and in general, for a while.

-------------------------

townforge | 2021-06-12 17:08:41 UTC | #7

In case anyone was interested, the game's now finished and launches on the 3rd of July :slight_smile: 

Here's a nice building made by one of the people who tried the test version:
![](https://townforge.net/images/main-item-voxels.jpeg)

-------------------------

throwawayerino | 2021-06-12 20:25:33 UTC | #8

Good luck on launch day!

-------------------------

