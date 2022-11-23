Sasha7b9o | 2017-01-02 01:08:07 UTC | #1

Call [code]    Ray ray(position, direction);
    PODVector<RayQueryResult> results;
    RayOctreeQuery query(results, ray, Urho3D::RAY_TRIANGLE, 0.5f, Urho3D::DRAWABLE_GEOMETRY, VIEW_MASK_FOR_MISSILE);[/code]
for the big vector of elements from different threads. If a thread one (created from main thread), that everything works well. At thw and more threads in a random time there is a mistake:
in
[code]void Octant::GetDrawablesInternal(RayOctreeQuery& query) const
...
    Drawable* drawable = *start++;[/code]
drawable - invalid pointer 0xcccccc... .

Perhaps, a mistake at me, but I do all manipulations with a scene and nodes in the main thread in event E_UPDATE or E_POSTUPDATE.

Update/
As it appeared, the mistake is shown and at one thread, which is carried out in parallel with the main thread.

-------------------------

cadaver | 2017-01-02 01:08:08 UTC | #2

There is possibility of errors at least if there are custom drawables that implement non-threadsafe code in response to bounding box operations. The standard 3D drawables like StaticModel should be safe, however the threaded Raycast code is not entered every time so there could well be actual bugs.

Also, because there's possibility of extra delay due to worker thread spin-up time, I believe it's better to just remove the threading code from Octree.

-------------------------

