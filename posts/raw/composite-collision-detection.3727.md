QBkGames | 2017-11-11 09:49:27 UTC | #1

I'd like to have an object, for example a car, that conceptually is made up of a number of parts (e.g. wheels, doors, roof, bumper bars, hood, bonnet, etc). Physically it should behave as a single rigid body (maybe based on the Raycast Vehicle). However when colliding, I would like to know exactly which of it's parts was involved in the collision, so that I may change the mesh of that part to one that shows some damage and also I like to keep track of the damaged parts so that later on, when the player enters a garage they are given the option the replace/repair the damaged parts.

Ideally, I would have a node that has a single rigid body and multiple collision shapes, but I couldn't figure out how to determine which of the collision shapes was involved in the collision.

Any ideas? Thanks.

-------------------------

stark7 | 2017-11-12 21:03:35 UTC | #2

The raycast result gives you the mesh that was hit, the distance and the node it belongs to, it doesn't use the physics bodies.

-------------------------

QBkGames | 2017-11-13 04:16:17 UTC | #3

Thanks for the idea.
So, I should get the collision data from the physics world and use it to create an Octree raycast query to get the specific child node and mesh. A bit convoluted but could work.

-------------------------

Bananaft | 2017-11-13 08:48:04 UTC | #4

[quote="QBkGames, post:1, topic:3727"]
but I couldn’t figure out how to determine which of the collision shapes was involved in the collision.
[/quote]

Compound collision shape won't tell you which of it's parts is colliding.

I would recommend the following: Making your car collision a single convex shape to keep things fast and simple, then, when it detects collision, you take a position of collision point and check what part it belongs "by hand" by checking it's intersection with part's bounding boxes, or finding a closest part to a collision point.

-------------------------

SirNate0 | 2017-11-14 15:01:54 UTC | #5

Based off of some earlier searching, I'm pretty sure you can also make a few modifications to Bullet so that it will tell you which shape in the compound shape was hit.

If you want, I can try to find those links, but if you'd prefer not modifying the engine I'd go with the other solutions.

-------------------------

