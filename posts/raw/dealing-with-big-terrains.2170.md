namic | 2017-01-02 01:13:38 UTC | #1

I've been using World Machine to create large terrains in Urho3D, but now i'm starting to have problems. Due to the large amount of entities in the "world", it's starting to hurt FPS. Also, this is just my first terrain tile. World Machine allows me to create a huge infinite terrain and export heightmaps of tiles. So, i have a few questions:

[ul]
[li]How can i load those tiles properly in Urho3d? Today, i have a range from the center of the tile, and if the player leaves that range, i load the nearest tile. For each tile, i have a list of the adjacent ones and their direction. [/li]
[li]How can i improve the performance when navigating within a single tile? Isn't terrain culling automatic? [/li][/ul]

-------------------------

jmiller | 2017-01-02 01:13:38 UTC | #2

Hi namic,

The profiler and DebugHud can show specifically where performance issues are:
[github.com/urho3d/Urho3D/wiki/D ... -Profiling](https://github.com/urho3d/Urho3D/wiki/DebugHud-and-Profiling)



Here are two threads on the general topic that might be useful:
[topic1395.html](http://discourse.urho3d.io/t/managing-large-scenes/1346/1) - Managing large scenes
[topic1957.html](http://discourse.urho3d.io/t/question-super-large-worlds/1870/1) - [Question] Super large worlds?

-------------------------

