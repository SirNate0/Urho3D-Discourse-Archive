throwawayerino | 2019-07-27 17:35:37 UTC | #1

I'm passing references to an image and don't want to have copies around
And if it is stored in memory, how could I release them?

-------------------------

Dave82 | 2019-07-27 18:06:55 UTC | #2

Resources in urho are reference counted. This means resources which reference count reaches 0 are automatically deleted. When you load a resource in resourcecache it's reference counter is increased by 1 when you use this resource somewhere in the scene the ref count increases each time you're refering to the resource. To remove unused resources call 
Cache->removeUnusedResources()

This will remove all resources with ref count of 1 (referenced only in resource cache)

-------------------------

Modanung | 2019-07-27 19:26:51 UTC | #3

You can also use `GetTempResource`. This will _not_ store the resource in the cache.

-------------------------

