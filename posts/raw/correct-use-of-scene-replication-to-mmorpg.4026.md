dev4fun | 2018-02-17 23:47:21 UTC | #1

Hey guys, Im doing a MMORPG using Urho3D and im have some doubts about it. My game will have different maps on ur world. Each map its a static model... For start the scene replication, I thought to make a scene on server for each map, this way, player will receive just what its inside on your current map. What I would like to know its:

1. That's its a good way to do scene replication?
2. What I should to do if I want the player have the possibility to move between maps? Example: Im on City, and walking I want to go to the hunt/leveling up map
3. About above question, what way I could "stream" the neighbor scene/map? Because of the maps should be like a bridge, I want to see where Im going/ another side of bridge

Exemplifying:
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/0/0e509e9176e4614edfc2620578a774f46bd6caa1.jpg'>

_Look that all maps are connected, it isn't a big map, and yes a lot of maps connected each other_

I hope that someone can give me a light about it, because I was a bit confused after see the real way that scene replication works..

Thanks.

-------------------------

Enhex | 2018-02-19 11:49:33 UTC | #2

Check out the networking interest management:
https://urho3d.github.io/documentation/HEAD/_network.html#Network_InterestManagement

You can use "distance factor" and "minimum priority" to automatically lower the update rate and exclude far nodes.

-------------------------

