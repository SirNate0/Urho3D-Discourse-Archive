SirNate0 | 2020-04-03 22:28:15 UTC | #1

This is a thread for me to ask assorted questions about Filesystem related functions (such as GetInternalPath, AddTrailingSlash, etc.) and their usages while working on adding a `Path` class to Urho instead of just `String` and a handful of functions.

To start things off, why is `GetInternalPath` used here and not `ResourceCache::SanitateResourceName`?
```
void AnimationController::FindAnimation(const String& name, unsigned& index, AnimationState*& state) const
{
    StringHash nameHash(GetInternalPath(name));
...
```

-------------------------

Modanung | 2020-04-04 21:24:52 UTC | #2

I think this may mainly be an optimization; `SanitateResourceName` is more complex and `FindAnimation` is called by almost *all* of `AnimationController`'s member functions.

-------------------------

SirNate0 | 2020-04-04 21:45:23 UTC | #3

Seems plausible. If that's the case, though, I think we should probably not call GetInternalPath and just require the user to pass a proper (internal, trimmed) string. I don't plan on doing either option, that's just my thoughts on the matter.

-------------------------

Modanung | 2020-04-04 22:37:02 UTC | #4

Another option would be to add `#ifdef _WIN32` either within `GetInternalPath` or anywhere the function is used. I expect this would *not* cause problems since `GetNativePath` also assumes no modification to the string are required when operating outside of bat country (aka Windows).

-------------------------

