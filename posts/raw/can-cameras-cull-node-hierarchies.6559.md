najak3d | 2020-11-21 20:11:00 UTC | #1

I saw the "SetViewMask()" function for Drawables, as a way of filtering out content from a Camera.

Note that we have multiple cameras in the scene, rendering to multiple Viewports....  and we have this concept of "Layer Visibility" and each layer can have 1000's of renderables.

So in short, we want an efficient way to manage Visibility per Camera, other than having each camera sift through 1000's of renderables that it's not going to render.

It would be much nicer to have this "ViewMask" set at the Node level, that way the Camera Culling Logic would be extremely efficient -- it would see the Node's Mask - and then not bother sifting through the content of this Node, if the mask doesn't match.  Now we've just got one comparison to make, per Layer, rather than 1000's!...

Any ideas on how to make this more efficient for Urho to manage?

-------------------------

JSandusky | 2020-11-22 01:27:47 UTC | #2

Nodes aren't stored in the octree, only the drawables themselves.

You can bunch them up into `StaticModelGroup` components which will treat them as one whole but you'll have to measure if you actually gain anything from it for how your objects are laid out.

If occlusion culling is on then the `OccludedFrustumOctreeQuery` is used cull entire octants if they're occluded. If you can, setup good occluders. Even without marking occludees you'll gain from octant culling.

---

If you really really wanted to aggregate a mask for each Octant then you'd have to tag octants as they're dirty and then visit every dirty octant and all of its drawables to update the mask ... and then walk the tree OR'ing the masks together since you need to merge those masks upwards. That's kind of silly.

If messing with octants you'd probably win more by marking their "latest dirty frame" and using that to cache shadowmaps for reuse since shadowmaps have considerable cost in both view-setup and rendering.

-------------------------

Eugene | 2020-11-22 17:23:02 UTC | #3

[quote="najak3d, post:1, topic:6559"]
It would be much nicer to have this “ViewMask” set at the Node level, that way the Camera Culling Logic would be extremely efficient – it would see the Node’s Mask - and then not bother sifting through the content of this Node
[/quote]
Urho has exactly one `Octree` per `Scene`, and `Node` hierarchy is not stored there.
So, at the time of culling you literally don't have any information about node hierarchy and you *cannot add it* because it contradicts current data layout.
The only way would be to group all stuff into one `Drawable` (e.g. `StaticModelGroup` or something custom), but you will lose an ability of partial culling. You either render whole `Drawable` or nothing.

-------------------------

najak3d | 2020-11-22 17:26:02 UTC | #4

Thank you JSandusky and Eugene -- both of you alluded to the same answer -- "StaticModelGroup", which seems to be the right answer for me -- I could at least group things in close proximity into these groups, and that would reduce overhead of the entire scene (at least the culling logic).  And would also mostly solve my issued.   Instead of having to use the ViewMask to cull 1000's of renderables, we'd only be culling dozens, likely.    And that suffices for sure.

I selected Eugene's solution, because it more succinctly describes the solution we're going to choose.

-------------------------

