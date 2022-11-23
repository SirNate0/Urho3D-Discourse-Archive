Enhex | 2017-01-02 01:08:14 UTC | #1

Is there more space efficient way than a string to identify resources?

Would using a SharedPtr to the resource be safe if the resource gets reloaded?
Is SharedPtr needed, or raw/weak pointer would be enough?

Perhaps a verion of ResourceCache::GetResource() that uses StringHash name instead of String?

-------------------------

codingmonkey | 2017-01-02 01:08:15 UTC | #2

>gets reloaded?
I think what reloading it's internal operation (see: bool ResourceCache::ReloadResource(Resource* resource)) it "inspirited to move" by FileWatchers, and you have the same seriazible component (or whatever) with new update data by the same pointer as before. The pointer maybe as raw and also as shared...

>Perhaps a verion of ResourceCache::GetResource() that uses StringHash name instead of String?
resources actually already are stored by hashed names, this string name converts to StringHash little deeper
[code]
Resource* ResourceCache::GetResource(StringHash type, const String& nameIn, bool sendEventOnFailure)
{
    String name = SanitateResourceName(nameIn);

    if (!Thread::IsMainThread())
    {
        URHO3D_LOGERROR("Attempted to get resource " + name + " from outside the main thread");
        return 0;
    }

    // If empty name, return null pointer immediately
    if (name.Empty())
        return 0;

    StringHash nameHash(name);
[/code]

then it get <T> res like this:
const SharedPtr<Resource>& existing = FindResource(type, nameHash);

-------------------------

Enhex | 2017-01-02 01:08:15 UTC | #3

If pointers are safe in case of reloading, that means they're fit for purpose.
Thanks.

I did see that StringHash is used internally, but ResourceCaches doesn't have API to use it.

-------------------------

