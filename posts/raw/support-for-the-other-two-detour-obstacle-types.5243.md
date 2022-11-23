Leith | 2019-06-21 04:31:57 UTC | #1

I noticed that our NavMesh implementation only supports one kind of "obstacle shape"... a vertical cylinder. While poking around in the Detour sourcecode, I noticed that two more kinds are supported: AABB, and OBB (ok, it can rotate in the Y axis).

OBB would be very useful to apply to DOORS, combined with a dynamic (tiled) navmesh, this would mean that a door being opened, or closed, or half open, will automatically block or allow access to AI agents in terms of their ability to pathfind. It's not a deal breaker, but it would be one less thing to deal with in terms of AI logic.

Would anyone else be interested in seeing the Obstacle class extended to be closer to CollisionShape - and supporting all three Detour obstacle shapes?

-------------------------

Modanung | 2019-06-21 20:08:32 UTC | #2

This sounds like something I could definitely use for several projects.

-------------------------

Leith | 2019-06-22 13:19:00 UTC | #3

I'll take that as a yes!

Old Fish did say that this implementation was only meant to serve as an example, but boy did he pick the right example! I mean, using the crowd agent, rather than the raw agent, with all its wonderful canned behaviors... Now we just need a bit more flesh back on those bones.

I need to restructure my codebase here - I will shadow my work, fork and pull down the lastest master, see what shakes, then push back a more complete obstacle class, following the pattern laid down by collisionshape... no suprises, but like i said, the detour aabb obstacle does not rotate, but might move, and the obb obstacle (say that ten times) can only rotate in the Y axis, like we would expect in most cases in an XZ plane based game, even in a true 3D world, the world UP vector at any moment, usually matters the most

-------------------------

Leith | 2019-06-23 07:41:07 UTC | #4

Since the existing code generates events when obstacles are added or removed, I have two choices.

I can submit a PR for an obstacle that breaks existing projects, but is optimal and operates just like collisionshape, or, I can define a bunch of new events.

I would like to hear from the wings, how I should approach a possible PR, and what conventions we have for this. I'm pretty sure there is no document describing procedures for PR.

-------------------------

Modanung | 2019-06-23 13:07:18 UTC | #5

I think optimal implementation has pretty much always outweighed backwards compatibility.

-------------------------

Leith | 2019-06-24 07:34:18 UTC | #6

That is the answer I wanted to hear...
Personally, I don't like to go around breaking stuff that works perfectly fine as it is...
However, to make an omelette, you have to break a few eggs.

Optimal it is then :slight_smile:

The new Obstacle class will have three dimensional extents, and will encode cylinders in exactly the same way as collisionshape (basically x is radius, y is height, and z is not used).
The event structures for adding and removing obstacles will be adjusted to reflect this.

-------------------------

Leith | 2019-07-31 05:09:57 UTC | #7

Attached is a proposed patch to support all three obstacle shape types.
It has not been properly tested - though I only expect the debugdrawing to be incorrect.
These changes don't appear to break existing code - at least the crowd navigation example still works perfectly.

Rather than introduce new classes and events, I chose to extend the existing Obstacle class and the related E_NAVIGATION_OBSTACLE_ADDED event.
Obstacle class attributes were extended to include obstacle type, plus a few other fields such as length and rotation angle. DynamicNavigationMesh::AddObstacle was adjusted to respect the new data.

Type 0 indicates vertical cylinder - our traditional obstacle shape.
Type 1 indicates an AABB - a box oriented to the world axes.
Type 2 indicates an OBB - a box that can rotate (in our case only around Y, a limitation of detour)

For the box types, the "radius" attribute is treated as "width", and the box dimensions are generally considered as axial half-widths.

Finally, there is an option to inherit Y orientation from the parent node, or not - this bool is set to true by default.

[EDIT]
I forgot to update the "RemoveObstacle" event, but for test purposes, it's probably not important.

<https://www.dropbox.com/s/kgewm0heyahxkw1/Navigation.zip?dl=0>

-------------------------

