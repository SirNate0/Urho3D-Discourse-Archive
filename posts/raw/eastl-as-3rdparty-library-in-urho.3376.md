Eugene | 2017-07-22 18:34:44 UTC | #1

Urho have a lot of "bicycle" things.
We cannot just drop things like Urho.Container, but we can stop writing even more garbage code.
So, I suggest to include EASTL as part of 3rdparties available for internal and external usage.

Pros:

- Stop re-re-re-implementing things when some algo or specific container is needed. No more garbage like `Urho::LowerBound`-s (shame on me) or maybe even `Urho::Sort`

- More functionality for C++devs who dislike STL or want fast containers/compilation.

There shall be the same restriction as for other 3rdparties like Bullet: Urho shall not use EASTL types and things in interface. So, Urho containers will be used for public API and EASTL will be used to simplify some algos or internally store data in exotic containers.

-------------------------

1vanK | 2017-07-22 21:04:15 UTC | #2

Did you compare it with Urho?

-------------------------

Eugene | 2017-07-22 21:25:55 UTC | #3

I reviewed it, at least. What are you interested in?

-------------------------

1vanK | 2017-07-22 22:10:17 UTC | #4

I mean comparison of performance

-------------------------

Eugene | 2017-07-22 22:24:06 UTC | #5

I didn't think in that way, actually. There is too little common between Urho.Container and EASTL.

Urho.Container is few simple containers and algorithms needed for the Engine. EASTL is dozens of different containers, hundreds of algorithms and traits for almost every possible task.

I doubt that there is important performance difference between e.g. `eastl::hash_map` and `Urho3D::HashMap`. And since we cannot get rid of Urho.Container completely, there is no sence to replace Urho containers in Engine internals with EASTL ones and complain about performance.

-------------------------

rku | 2019-04-17 12:03:39 UTC | #6

I started integrating EASTL into [rbfx](https://github.com/rokups/rbfx/commit/71a1ba528d46cbca0edbacbf2feb29e429996bd6). There are more benefits than meets the eye too.

* Compatibility with stdlib. This is important.
* Swig already has code written to wrap stdlib containers and adapting them will be easy. This will relieve some C# maintenance burden.
* Can easily adapt other libs to use same classes. For example `fmt` could use same string implementation. This will be most likely just swapping some includes in `fmt`.
* Allocator customization. Instead of using separate allocator per container we could benefit from some memory pooling.

-------------------------

rku | 2019-05-01 12:11:06 UTC | #7

I am done with initial migration. Had to patch EASTL in the process, adding some convenience functions we are all used to. Smart pointers also needed a bit of love to allow us constructing `eastl::shared_ptr<>` from plain `T*` instead of having to explicitly use `ptr->shared_from_this()`. It all appears to be working fine.

-------------------------

