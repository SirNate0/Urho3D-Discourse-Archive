najak3d | 2022-02-14 05:17:28 UTC | #1

Most of the visual Apps I work on are "map related" and so are 2.5D in nature, like RTS or Google Earth style interfaces.

The annoying convention conflict is between the Lt/Lg coordinate system which is essentially a Vector2 with XY.. X is Longitude (East-West), and Y is Latitude (North-South) on the map.

But in the 3D renderer, we're using Vector3, but here.. Z aligns to Latitude, not Y. Instead Y is now "Altitude". (i.e. UP)

So our code is riddled with conversion from Vector2.XY to Vector3.XZ.... and are constantly assigning Y to Z and Z to Y as we convert back and forth between the conventions.

So begs the question -- should we just make the 3D renderer *also* use Y as North-South, and let Z be UP???

But I think this is likely a bad idea, because then it alters the meaning of "Yaw/Pitch/Roll" -- as I think "Yaw" in most 3D game engines is tied to rotating about the Y-Axis. So if we changed Z to up... then we'd have to change over to using "Roll" instead of "Yaw" to control the "bearing" of an entity (NSEW horizontal direction/angle). And "Roll" would be weird for this.

Then there is the issue of most objects -- Roll tends to mean "rotation along the Frontal axis" (like for an aircraft).

And so my tentative conclusion is that "It's best to keep Y as UP", as the confusion of XY = XZ for positional placement is easier than changing the conventional meaning of Yaw vs Roll.

-------------------------

najak3d | 2022-02-14 05:17:47 UTC | #2

One solution that we have employed to reduce the current XY to XZ pain is to create a new struct called something like LocXZ which is equivalent to Vector2, but uses "Z" instead of "Y", and then have implicit conversion defined to/from Vector2. But nearly all of our code uses the LocXZ. We also make it transform "to" Vector3 implicitly (but not the reverse, since you shouldn't ever implicitly drop information, as you might imagine the potential horrors that could arise).

I think that might be what we stick with, as we're still in infancy of a new project. Before deciding this for certain, I wanted to gather thoughts from others.

-------------------------

Eugene | 2022-02-14 07:51:31 UTC | #3

IMO it isn’t worth the pain.
Whenever you find a place in Urho code or a code snippet that relies on implied Y=up, you will be on your own to deal with it, and if it’s in the engine,  you should be ready to patch the engine itself.

-------------------------

najak3d | 2022-02-14 07:26:53 UTC | #4

I've mostly come to that conclusion myself, but before settling on it, wanted to triangulate with a few others.    I've already created our own "Location" struct, that has XZ members, instead of XY.

-------------------------

