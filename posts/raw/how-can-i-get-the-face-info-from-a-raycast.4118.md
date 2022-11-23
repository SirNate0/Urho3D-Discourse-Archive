Pihozamo | 2018-03-24 01:21:24 UTC | #1

I would like to know if it's possible to get the face (triangle, quad, ...) info from a raycast collision result. 

What I'm doing right now is getting the collision position from the raycast result and calculating the distance from all the geometry vertexes so I can get the nearest point, however I feel like there is a better way.

Looking at the documentation for the RayQueryResult class it seems that there's no info about the intercepted face, only the whole Geometry, in this case the drawable_ variable.

So if I could get the intercepted face info I could just filter it down to that face's vertexes. 

Thank you.

-------------------------

Sinoid | 2018-03-24 02:35:53 UTC | #2

**A:**

Add an `unsigned subObjectElementIndex_` to RayQueryResult that defaults to `M_MAX_UNSIGNED`. Update `Ray::HitDistance` to be able to output the index in the index buffer of the first triangle vertex (the index of the index, not the index of the vertex). Make relevant changes to `Geometry` to bubble that up and use it in `StaticModel::ProcessRayQuery`, recording the index whenever the distance checks pass.

Then fix all the places that are unhappy about adding the extra parameter to Ray::HitDistance, fix scripting bindings, etc.

The rest of RayQueryResult already contains what you need to get in order to get the vertex and index data as well as vertex data description for pulling out the vertex attributes you care about for your *whatever-it-means-here-triangle*.

---

**B:**

Roll a bespoke / copy-pasta of Ray::HitDistance to use after first successful cast to cast again and capture out more data.

---

**C:**

Tweak Ray::HitDistance to accept an *output-count* and thus treat the input pointers as the start of an array, where the first element is the hit position, and the next N are the element data that was used for the triangle of the hit.  Then somehow bubble that mess of information back up and hope you don't end up ever having more types of triangles you need to get.

-------------------------

ghidra | 2018-03-27 16:56:28 UTC | #3

is this in the wiki? this should be in the wiki ;)

-------------------------

SirNate0 | 2019-07-13 21:26:45 UTC | #4

So has anyone actually made a solution to this?

-------------------------

Leith | 2019-07-14 06:48:52 UTC | #5

I don't know, but since I have some experience with both physics and graphics raycasting I could add it to my todo list? I would definitely like to say that we can always provide more information from collision queries than we already do. I think its an area where we can do better. I personally should know this, it's a beginner thing in directx to pick triangles

-------------------------

Leith | 2019-07-15 14:46:10 UTC | #6

I just poked around a bit - Urho3D::RayQueryResult does not tell us which triangle we hit - however it does tell us the exact UV coordinates of the hitpoint (which indicates that yes we COULD have returned that extra information...)

In another time, I had to use barycentric coordinates to determine the UV of the hit point (terrain painting, coming soon!) - given there is no internal acceleration structure for hit queries in the Model class, and assuming that all UVs are "unique" (subject to interpretation of the definition), I reckon the fastest way to determine which triangle was hit is to check every triangle in the model, to find out if we can map the UV hit coordinate back to a barycentric coordinate within that triangle. In the case of unique UVs, there will be only one hit result (and so a chance to terminate our search early). In the case of shared UVs, we have to do a second test to figure out which hit result is closest, and/or sort the results by distance.

-------------------------

