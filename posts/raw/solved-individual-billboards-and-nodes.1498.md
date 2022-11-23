Enhex | 2017-01-02 01:08:09 UTC | #1

Is there a way to attach to a node a Billboard from a BillboardSet?

I want to do this instead of using BillboardSet for each node, because I assume BillboardSet batches all its individual billboards for rendering, correct?

So if I want to attach individual billboards, the only way is to update their position & rotation manually on Update event?

Also, is there a reason to use BillboardSet for each node? Maybe occlusion culling?

-------------------------

cadaver | 2017-01-02 01:08:09 UTC | #2

You could subclass BillboardSet to do this. Presumably the API would end up somewhat similar to StaticModelGroup. Your component could subscribe as a listener to each node it's using to get the OnMarkedDirty() notifications when the node moves.

Note that the BillboardSet is culled as one unit, so if the nodes are far away from each other, its bounding box will be large and it'll be drawn if any of the billboards is in view.

-------------------------

