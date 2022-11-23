Dave82 | 2017-10-15 22:29:16 UTC | #1

I'm trying to figure out some things about the Dynamic navigation mesh.
1. It seems that FIndPath() have 3 result choices.Either it returns an empty path or an array with 2 elements or a full path.The problem is i never get an invalid (empty) path when i should.I always have at least 2 ponts as a result , A starting point and the closest point to destination.Even if there is no physical connection between two separate nav meshes the enemies keep walking to the closest point to the player.Is there any way to check there is a valid mesh connection between the navigation meshes ? 

2.Is there a way to take a radius into account while searching for a path ? I want enemies to keep certain distance from the edge of the navmesh,

To be honest CrowdAgents are a bit limited and are probably intended for general purpose and after testing it i couldn't get the desired result.All i want is finding a path on a simple planar navmesh and handle gravity and collision avoidance in my own algorythm.

-------------------------

Eugene | 2017-10-16 08:49:56 UTC | #2

[quote="Dave82, post:1, topic:3661"]
Is there any way to check there is a valid mesh connection between the navigation meshes ?
[/quote]
Is it enough to just check the distance between expected and actual destination?

[quote="Dave82, post:1, topic:3661"]
Is there a way to take a radius into account while searching for a path ?
[/quote]
AFAIK, navigation meshes doesn't provide built-in support of non-point actors. So the simplest way is to use several meshes with different radiuses.

[quote="Dave82, post:1, topic:3661"]
To be honest CrowdAgents are a bit limited and are probably intended for general purpose
[/quote]
You could avoid using CrowdAgents at all, but dynamic collision avoidance may be quite hard to implement. Do you need it?

-------------------------

Dave82 | 2017-10-16 12:41:11 UTC | #3

[quote="Eugene, post:2, topic:3661"]
Is it enough to just check the distance between expected and actual destination?
[/quote]

Well the expected and actual distance most of the time could be the same.Let's say player and enemy is standing next to a thin wall (one from each side) then FindPath() always returns the closest point to the player (destination) which is closest point to the wall on the enemy's side. This ends up in a very stupid result.If the player walks alongisde the wall the enemies keep following them on the other side of the wall no matter if there's no physical path between the two separate rooms.
In this situation the distance between the player and enemy is more or less equal if they standing next to each other on the same side of the wall , so checking the distance will fail. 

[quote="Eugene, post:2, topic:3661"]
 You could avoid using CrowdAgents at all, but dynamic collision avoidance may be quite hard to implement. Do you need it?
[/quote]

No i don't need it at all.Levels in old resident evil , silent hill games, etc are all static.Very rarely there is a fake dynamic element (Player pushes away a crate to obtain a door , explosion destroys a path so it's not walkable afterwards ,can be easily solved by using a different navmesh each time)

[quote="Eugene, post:2, topic:3661"]
"AFAIK, navigation meshes doesn’t provide built-in support of non-point actors. So the simplest way is to use several meshes with different radiuses."
[/quote]

In theory i have a solution using the GetDistanceToWall() i will try it the next weekend.

-------------------------

Eugene | 2017-10-16 12:48:12 UTC | #4

[quote="Dave82, post:3, topic:3661"]
Well the expected and actual distance most of the time could be the same
[/quote]

I am talking about distance between destination point passed to FindPath and actual path end in output array. If the difference is big, consider this path as non-satisfying and drop it.

[quote="Dave82, post:3, topic:3661"]
No i don’t need it at all.Levels in old resident evil , silent hill games, etc are all static.Very rarely there is a fake dynamic element
[/quote]
Well, other enemies are dynamic obstacles too. If you don't want enemies to trhough each other, you should somehow handle it. The better quality you want, the more complicated algo you need. `CrowdAgent` is generic-purpuse solution to make nice actor interaction with pushing and avoiding.

-------------------------

