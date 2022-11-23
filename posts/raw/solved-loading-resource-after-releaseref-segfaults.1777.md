TheComet | 2017-01-02 01:10:03 UTC | #1

In a previous question of mine (see [url=http://discourse.urho3d.io/t/when-are-resources-deallocated/1717/1]this thread[/url]) I was told it was possible to call [b]cache->GetResource<XMLFile>("thingy.xml")->ReleaseRef();[/b]. It appears if you ReleaseRef() a resource after loading and using it, loading another resource of the same type will segfault.

[code]void App::Start()
{
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    for(int i = 0; i < 10; i++)
    {
        XMLFile* f = cache->GetResource<XMLFile>("UI/DefaultStyle.xml");
        f->GetRoot();     // segfaults for i=1, works at i=0
        f->ReleaseRef();
    }
}[/code]

Another, simpler example even:
[code]void App::Start()
{
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    for(int i = 0; i < 10; i++)
    {
        XMLFile* f = cache->GetResource<XMLFile>("UI/DefaultStyle.xml"); // segfaults for i=1, works at i=0
        f->ReleaseRef();
    }
}[/code]

In the first case, GetRoot() fails because [b]document_[/b] is NULL:
[code]XMLElement XMLFile::GetRoot(const String& name)
{
    pugi::xml_node root = document_->first_child(); // document_ is NULL.

    // SNIP
}[/code]

In the second case, GetResource() fails because refCount_ is pointing to garbage:
[code]void RefCounted::ReleaseRef()
{
    assert(refCount_->refs_ > 0); // refCount_ is 0x642f74656d6f002f (this is a garbage value)

    // SNIP
}[/code]

After some analysis, the reason is simple: ResourceCache isn't notified of the resource being destroyed when manually calling ReleaseRef() on it, which means ResourceCache will continue to hold an invalid pointer to the destroyed resource.

So what is the correct way of destroying a resource from the cache manually?

-------------------------

cadaver | 2017-01-02 01:10:05 UTC | #2

Calling ReleaseRef() manually when something is managed by shared pointers (such as the resource map of ResourceCache) is a bad idea, because it disturbs the pointers' automated refcount management.

The ResourceCache has the family of ReleaseResource() functions, please use these. In extreme situation use ResourceCache::GetAllResources() and const cast it as necessary so that you can modify the resource map directly.

-------------------------

Dave82 | 2017-01-02 01:10:05 UTC | #3

Also you can simply use the cache->GetTempResource() which won't store the resource in the cache but only in a smart pointer.So once it goes out of scope it will be deleted.

[code]void App::Start()
{
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    for(int i = 0; i < 10; i++)
    {
        SharedPtr<XMLFile> f = cache->GetTempResource<XMLFile>("UI/DefaultStyle.xml");
        // Do something with f 
       // f will be deleted once goes out of scope... nothing to release here
    }
}[/code]

[quote]It appears if you ReleaseRef() a resource after loading and using it, loading another resource of the same type will segfault.[/quote]

Well that's exacly what should happen if you releaseRef().You should ALWAYS Release those refs that were prevoiusly AddRef()'d.

[quote] XMLFile* f = cache->GetResource<XMLFile>("UI/DefaultStyle.xml");
f->ReleaseRef();[/quote]
This is wrong since the only ref is stored by the ResourceCache and you releasing it.

It was my fault...:slight_smile: in the other topic i didn't explaied Urho's ref counting very well.
So 

1. Call ReleaseRef() only if you AddRef() previously.
2. The easiest way to get rid of unused resources is call cache->RemoveAllResources(). This will remove all resources with refCount == 1 (referenced only by the cache , not used elesewhere)

-------------------------

