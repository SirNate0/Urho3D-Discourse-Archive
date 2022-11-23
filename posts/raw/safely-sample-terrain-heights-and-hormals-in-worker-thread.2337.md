Eugene | 2017-01-02 01:14:49 UTC | #1

subj.
It is const op, so theoretically it can be safe, unless.. unless what? What could happen with Terrain that ruin anything?

PS: Why does BillboardSet::UpdateBufferSize calls geometry_->SetVertexBuffer(0, vertexBuffer_) on every resize?
I can't undertand why since it is plain assignment.

-------------------------

cadaver | 2017-01-02 01:14:49 UTC | #2

If the main thread destroys the terrain from under you or changes its size, in that case you're screwed, otherwise should be safe.

The BillboardSet code is likely a leftover from a time when re-setting the vertex buffer actually updated some internals in the geometry (in case vertex format changed), now it is unnecessary. Feel free to remove.

-------------------------

Eugene | 2017-01-02 01:14:50 UTC | #3

Would it be okay to hold shared pointer on Terrain in other component?

Update:
Can I somehow destroy object if some work items (maybe executing right now) need this object EXCEPT completing all work items?
Just infinite loop like WorkQueue::Complete, no other ways?

-------------------------

cadaver | 2017-01-02 01:14:51 UTC | #4

Note the Urho shared pointers are not threadsafe. Holding a shared pointer in another component's main thread code is OK though, but will not protect against modification of the Terrain component, ie. terrain resize.

There are presently no mechanisms to synchronize dependency on objects when the work queue tasks are being executed. If you look how Urho itself uses the queue presently, it's limited to the render update, during which the scene is assumed to not be modified.

-------------------------

Eugene | 2017-01-02 01:14:51 UTC | #5

It is true that I'll need some manual guarantees on terrain immutability, I can deal with it.
However, I need some way to guaranteely stop some work item.

Will code like this work as I expect?
With obviuos precondition that work item was added and wasn't completed/removed.
It looks like I missed something...
[code]
/// Remove a work item if possible, otherwise complete executing. Return true if item was completed.
bool WorkQueue::DiscardWorkItem(SharedPtr<WorkItem> item)
{
    if (RemoveWorkItem(item))
        return false;
    Resume();
    while (!item->completed_)
    {
    }
    item->sendEvent_ = false;
    return true;
}
[/code]

-------------------------

cadaver | 2017-01-02 01:14:52 UTC | #6

If it's OK for you to poll in the main thread until it has completed that should work.

-------------------------

