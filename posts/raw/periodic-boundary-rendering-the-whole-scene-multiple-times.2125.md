feltech | 2017-01-02 01:13:17 UTC | #1

Hello all.  I'm trying to create a world with a periodic boundary, that is, you go off one side and come back on the other.

To do this (in 3D) I need to draw the whole scene 8 times and put them next to each other, to form a larger scene "cube".  I'm hoping it's just the rendered portion that needs cloning, not the physics objects.

I've tried `Node::Clone()` but I don't see any cloned node in the scene, and it looks like `Clone` is just for replicating across a network anyway?

Perhaps there is a way to do it with the `Renderer` or `Viewport`?

Any hints much appreciated!

-------------------------

cadaver | 2017-01-02 01:13:17 UTC | #2

The engine doesn't support rendering the same node in multiple positions, so unless you make engine changes for this, you need to have an actual copy of the "world tile" in your scene, at least with the drawable components.

Node::Clone() should work, it's not intended for net replication. After cloning, call SetPosition() on the clone node and you should see it in a different position.

-------------------------

feltech | 2017-01-02 01:13:17 UTC | #3

Thanks for the hint.  I found out why nothing was showing up when I did a `Clone`. 

The basic problem is that `Clone` expects the cloned `Component`'s `Model` to have come from the `ResourceCache` (see `StaticModel::SetMaterialsAttr`).  However, my `Model`s are custom and created at run time, so are not in the `ResourceCache`.  Hence the cloned `Component` has no `Model` and doesn't render (and I get an error  log "Material index out of bounds", since it's trying to clone a `Material` onto a non-existent `Model`).

Adding my models to the `ResourceCache` via `AddManualResource` gets me something on screen to play with.  It doesn't get me all the way to a periodic environment, but at least I'm making progress  :wink: .

-------------------------

cadaver | 2017-01-02 01:13:17 UTC | #4

Yes, the resources are indeed necessary to be named and in cache as the cloning doesn't operate with pointers, but through the generic attribute serialization. Cool that you figured it out!

-------------------------

