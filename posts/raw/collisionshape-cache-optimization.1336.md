Enhex | 2017-01-02 01:06:56 UTC | #1

First of all, I don't know if Urho already does something like this, if so please let me know.

Bullet's wiki says different rigid bodies can use the same collision shape. ([bulletphysics.org/mediawiki- ... ion_Shapes](http://www.bulletphysics.org/mediawiki-1.5.8/index.php/Collision_Shapes))

I'd like to suggest having a CollisionShape cache that stores unique shape instances, and when a user tries to create a collision shape, the cache will check if there's already an instance for it to use.
CollisionShape can have a "unique" flag to exclude it from caching, in cases where it's going to be modified after creation.
If the user tries to modify a shape it can automatically become unique. It will help to reduce complexity and prevent unexpected behavior for inexperienced users.
If the user wants to modify the shape and still cache it, he'll have to create the modified shape as a new shape to have it cached.

I argue that in the vast majority of the cases the user will use the same collision shape for every prefab type, creating redundant duplicates of the shape for every instance.
So caching shapes by default makes sense.

-------------------------

1vanK | 2017-01-02 01:06:56 UTC | #2

Is the shapes consume a lot of memory?

-------------------------

Enhex | 2017-01-02 01:06:57 UTC | #3

[quote="1vanK"]Is the shapes consume a lot of memory?[/quote]
I'm not worried about memory, it will only save few KBs, before the CPU will be a bottleneck.

I'm hoping it will help reduce cache misses.

-------------------------

codingmonkey | 2017-01-02 01:06:57 UTC | #4

PhysicsWorld have a some method with name: CleanupGeometryCache

[code]
void PhysicsWorld::CleanupGeometryCache()
{
    // Remove cached shapes whose only reference is the cache itself
    for (HashMap<Pair<Model*, unsigned>, SharedPtr<CollisionGeometryData> >::Iterator i = triMeshCache_.Begin();
         i != triMeshCache_.End();)
    {
        HashMap<Pair<Model*, unsigned>, SharedPtr<CollisionGeometryData> >::Iterator current = i++;
        if (current->second_.Refs() == 1)
            triMeshCache_.Erase(current);
    }
    for (HashMap<Pair<Model*, unsigned>, SharedPtr<CollisionGeometryData> >::Iterator i = convexCache_.Begin();
         i != convexCache_.End();)
    {
        HashMap<Pair<Model*, unsigned>, SharedPtr<CollisionGeometryData> >::Iterator current = i++;
        if (current->second_.Refs() == 1)
            convexCache_.Erase(current);
    }
}
[/code]

As you see there is something happening with cache 
and by this i guessing that cache are exist, at last some kind variant of it

-------------------------

Enhex | 2017-01-02 01:06:57 UTC | #5

Ok, good to know, saved me quite a lot of trouble in the future.

-------------------------

friesencr | 2017-01-02 01:06:57 UTC | #6

There is already a cache for using same models.  Saving the bvh results to a file is a room for improvement.  Great for terrains.

-------------------------

cadaver | 2017-01-02 01:06:59 UTC | #7

Primitive shapes (boxes etc.) aren't cached, because we'd still need to be prepared for unique scaling and size parameter. So it could only use the cached shape if the values match exactly, and maintaining the shape cache for all shapes would involve more complex code and some overhead (most likely a suitably keyed HashMap).

It will be interesting to know the results if you decide to test out primitive shape caching, but as of now it's not a high priority for the project itself.

-------------------------

Enhex | 2017-01-02 01:07:01 UTC | #8

I looked at how the cache works, using a hash map model pointer and LOD level pair.

Perhaps like a model object, there could be size & scale object for shapes that is defined once. It's just a pair/struct of 2 Vector3's.
Keeping an unordered set of unique shape descriptions will be the most optimal solution.
For repeated use of the same shape description, the user should be able to pass a reference to an existing shape description, so the pointer can be compared instead.

I think it could be just as efficient.

As for testing performance, I previously tried a quick hack which didn't work.
I might try to properly test it by implementing the above suggestion at the end of my current project (no premature optimization).

-------------------------

