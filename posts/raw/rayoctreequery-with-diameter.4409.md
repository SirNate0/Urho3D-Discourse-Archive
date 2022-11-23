capelenglish | 2018-07-26 11:55:57 UTC | #1

I'm using RayOctreeQuery to determine if a mouse-click hits an object. This works fine except when it's close to the edge of the object. I need the ray to have a diameter, in other words, the bullet diameter. If my bullet has a diameter of 3, then I need to detect a hit that is 1.5 from the edge of the object. Is there any way to accomplish this in Urho3D?

-------------------------

SirNate0 | 2018-07-26 12:31:20 UTC | #2

You could try a physics sphere cast. Other than that I think you're stuck with just doing a set of raycasts in a circle to approximate it.

-------------------------

