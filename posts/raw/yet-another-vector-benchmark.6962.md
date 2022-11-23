1vanK | 2021-08-10 17:51:47 UTC | #1

Urho3D::Vector vs Urho3D::PODVector vs std::vector

<https://github.com/1vanK/Urho3DContainersBenchmark>

Result: <https://github.com/1vanK/Urho3DContainersBenchmark/blob/master/vector_result.txt> Lower values are better.

Some conclusions:
* Debug version of `std::vector` is very slow, but release version is fast (perhabs some bounds checks)
* `Urho3D::Vector` the slowest (release version)
* It seems `std::vector` have some optimizations for POD types, but `Urho3D::PODVector` is faster
* Mingw is faster than Visual Studio
* 64 bit is faster than 32 bit

-------------------------

vmost | 2021-08-10 17:58:31 UTC | #2

Interesting that `std::vector::iterator` is slower than `operator[]`. I thought they were equivalent (naively).

Nvm was looking at debug. It is only slower for `std::vector<int>` in release test for MinGW 32-bit (with a flipped speed relationship in VStudio...).

-------------------------

Eugene | 2021-08-11 06:51:19 UTC | #3

[quote="1vanK, post:1, topic:6962"]
Some conclusions
[/quote]
I must point out issues with this benchmarking (which may or may not substantially affect the result, I don't know):

- In Push tests you may be measuring performance of memory allocator (which is probably not what you want)

- I don't 100% trust hand-made benchmarking systems. [Benchmarking libraries](https://quick-bench.com/) exist out there for a reason. Sometimes it matters, sometimes it doesn't :man_shrugging: 

- Resulting numbers are not really helpful without error margin. I have significant fluctuations (5-10%) between runs when I run these benchmarks locally. Which means that `vector_result.txt` is meaningless (or even harmful/misleading) on its own.

Having said that, I have run your benchmarks locally and I _think_ these conclusions are correct.

-------------------------

1vanK | 2021-08-11 06:59:39 UTC | #4

In any case, the difference between implementations is minimal, so we can replace Vector and PODVector with std::vector.

-------------------------

rku | 2021-08-11 09:11:55 UTC | #5

GCC/Clang on linux/macos + older msvc version tests would be good. msvc only recently made debug performance of containers not stupid.

This would make rbfx maintenance easier so regardless, please do it :)

-------------------------

SirNate0 | 2021-08-11 10:36:21 UTC | #6

More importantly, this would make integration with many 3rd party libraries (for geometry processing, for example) much easier, and allow the use of the STL algorithms, and make a lot of the Stack Overflow answers applicable with the vectors without changing all of the function names. I am in favor of the change.

-------------------------

vmost | 2021-08-11 10:39:00 UTC | #7

I am also in favor (fwiw). I have been using the STL in my own project as much as possible already :D.

-------------------------

SirNate0 | 2021-08-24 20:05:01 UTC | #8

If anyone is interested in it actually happening, I've started work on switching over to std::vector on this branch. There seem to be some issues with the AngelScript bindings at present, and I'm not sure when I'll get to them as this is a lower-priority project for me.

https://github.com/SirNate0/Urho3D/tree/switch-to-stl-vector

For this, I've opted to change the other container's method names to also match the standard library (so they use `size()` instead of `Size()`, for example).

-------------------------

glebedev | 2021-08-25 12:35:52 UTC | #9

Is it possible to include eastl to the test?

-------------------------

1vanK | 2021-08-31 07:10:25 UTC | #10

Added (txts with results in root of repo)

-------------------------

