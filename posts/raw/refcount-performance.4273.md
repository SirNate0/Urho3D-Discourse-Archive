TheComet | 2018-05-31 10:46:05 UTC | #1

I have some thoughts on how reference counting is implemented.

As of now, for every object in Urho3D that inherits from `RefCounted` (so nearly everything in the engine and most of the stuff in a user's application) there will be two calls to malloc. One to allocate the object and another for allocating the `RefCount` object: https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Container/RefCounted.cpp#L33

The question here is: Is calling malloc twice having any impact on performance? Or are there other things that outweigh the cost of allocating?

If this is a concern, then I have two ideas. The first is to inline `refs_` and `weakRefs_` into RefCounted and get rid of `RefCount` entirely. In order for weakrefs to still work, the conditions for when the object is destructed and freed would have to be modified: Call the destructor when `refs_` reaches zero, free the memory when `weakRefs_` reaches zero. This has the advantage of only having a single malloc call and the refcounts are located close to the object itself which makes the cache more coherent. The disadvantage is the additional delete logic, having to overload operator new, and the object remains allocated as long as there are weak references pointing to it.

Another idea might be to have a memory pool for `RefCount` objects. This would improve allocation speed but the refcount would be located far away from the object in memory, which is bad news for the cache whenever you modify the refcounts.

I'd like to hear your thoughts. Maybe this whole thing is also not an issue.

-------------------------

Eugene | 2018-05-31 16:43:20 UTC | #2

[quote="TheComet, post:1, topic:4273"]
The first is to inline `refs_` and `weakRefs_` into RefCounted and get rid of `RefCount` entirely. In order for weakrefs to still work, the conditions for when the object is destructed and freed would have to be modified: Call the destructor when `refs_` reaches zero, free the memory when `weakRefs_` reaches zero.
[/quote]

Once you called dtor, you are not allowed to read or modify any part of the object.
/>

[quote="TheComet, post:1, topic:4273"]
Another idea might be to have a memory pool for `RefCount` objects.
[/quote]

Once you have global pool for something, you must care about threading. So it should be thread-local pool. Not so easy, questionable performance.

-------------------------

S.L.C | 2018-05-31 17:41:17 UTC | #3

Either way you go there's something to be lost. Threading issues with memory pools, memory issues with moving it into the same class.

And if you try to do it like a shared pointer thing where you store the counter and instance in the same structure to be near each-other, you end up "leaking" memory because if there's still a weak reference you can't release the counter and thus you can't release the memory for the actual instance. Not to mention that you get a few inconveniences.

Either way it gets nasty. That's why `shared_ptr` and similar smart pointers use a similar counter that is allocated separately. And `ReferenceCounted` is no different than that.

If you do have a memory allocator that can allocate the counter  near the instance, you could just overwrite the `new` operator to replace the default behavior. Should reduce the number of changes to be made to existing code.

-------------------------

TheComet | 2018-05-31 23:27:57 UTC | #4

[quote="Eugene, post:2, topic:4273"]
Once you called dtor, you are not allowed to read or modify any part of the object.
[/quote]

Good point. Maybe it's possible to do as @S.L.C said, somehow allocate RefCount near the object being refcounted. Or perhaps even allocating a larger block of memory to fit both and constructing them next to each other?

[quote="S.L.C, post:3, topic:4273"]
And if you try to do it like a shared pointer thing where you store the counter and instance in the same structure to be near each-other, you end up “leaking” memory because if there’s still a weak reference you can’t release the counter and thus you can’t release the memory for the actual instance.
[/quote]

In the grand scheme of things, this probably won't matter too much for two reasons: 1) weak references aren't *that* common and 2) the refcounted objects all have a relatively small memory footprint. I can't think of any single Urho class that requires over, say, 1kB of memory when allocated.

I'm just thinking out loud here. I'll have to actually do some measurements.

-------------------------

Eugene | 2018-06-01 00:28:07 UTC | #5

[quote="TheComet, post:1, topic:4273"]
Or are there other things that outweigh the cost of allocating?
[/quote]
You know, we have 50% single-threaded rendering with constant memory reallocation for per-batch instancing buffers...

Every time I see yet another thread about optimizing refcnt, or optimizing string copies, or complains about probably slow new attributes, I want to say “Sweet summer child...”

-------------------------

orefkov | 2018-06-01 06:29:34 UTC | #6

Imho, by optimizing refcount allocation in 100 times, common programm performance increased by 0.01%
Do you have profiled tests telling that It is bottleneck for engine?

-------------------------

1vanK | 2018-12-10 14:51:49 UTC | #8

[quote="orefkov, post:6, topic:4273, full:true"]
Imho, by optimizing refcount allocation in 100 times, common programm performance increased by 0.01%
Do you have profiled tests telling that It is bottleneck for engine?
[/quote]

memory fragmentation is problem also

-------------------------

cosar | 2018-12-10 18:41:00 UTC | #9

I think cache misses and memory fragmentation can lead to performance issues and should not be neglected. On top of that, proper profiling on core mechanics is hard to achieve, so it's very difficult to asses the impact.
There might be another way that will avoid double allocation and non-contiguous memory, and without detaching the destructor from the deallocation.
Instead of a weak reference counter, we can have a weak reference double linked list (weak_ptr containing node information), with the head kept in RefCounted. The penalty is a tail insert at weak reference creation, a node removal at breaking the weak reference, and a list traversal at object destruction (when strong refs go to zero) to invalidate existing weak refs.
The assumption is that weak references are used just occasionally to break circular dependencies and that most objects don't have weak refs to them.

-------------------------

1vanK | 2018-12-10 22:08:36 UTC | #10

Actually after using std::make_shared() memory is freed only after all weak_refs is deleted, so we can do the same and just move refcounters into objects

-------------------------

cosar | 2018-12-10 23:06:40 UTC | #11

That's what TheComet's first proposal was (and the easiest to implement). If delayed memory freeing is not an issue, then this looks like the best approach.

-------------------------

