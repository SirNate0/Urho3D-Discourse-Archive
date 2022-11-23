ricab | 2018-02-13 19:33:46 UTC | #1

Is there any kind of [ScopeGuard](https://stackoverflow.com/questions/10270328/the-simplest-and-neatest-c11-scopeguard) or [ScopeExit](http://www.boost.org/doc/libs/1_66_0/libs/scope_exit/doc/html/index.html) available in Urho3D?

Here is a use case:
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Resource/Image.cpp#L976

There is a leak there (coverity 126870): `FreeImageData(pixelDataIn);` should be called on this exit path. While it could be called directly, a scope guard would be preferable, as it would avoid the duplicate function call and cover all possible [even future] exit branches.

Alternatively, Urho's smart pointers could support custom deleters, but that would be more work.

-------------------------

weitjong | 2018-02-14 12:31:19 UTC | #2

Alas, our SharedPtr is not a generic container. It can only contain Urho’s own refcounted object. Eugene has a PR which proposes a more generic container ala non-refcounted. But I don’t think it has ctor that takes a high-level function or lambda as deleter (yet). So at the moment, just do with what we got first, fixing it the old fashion way.

-------------------------

ricab | 2018-03-02 17:41:16 UTC | #3

It's been a while and just want to clarify that I'm currently unable to progress with any coverity issues because the service is down. It has been so since Feb 20 according to their [twitter page](https://twitter.com/coverityscan) :confused:

-------------------------

weitjong | 2018-03-02 18:14:37 UTC | #4

Yes. It takes unusual long for them to fix the SSL server certificate issue or whatever. We are forced to temporarily remove the coverity scan badge from our README page as the result.

-------------------------

