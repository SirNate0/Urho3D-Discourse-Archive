mohamed.chit | 2022-04-29 12:59:26 UTC | #1

It is believed that default C++ memory allocation to be slow, using new/delete without adding any implementation would have some penalties on performance.
We would like to use our custom memory allocators to use them to allocate Urho3d objects, is that possible? I see in Urho3d (RefCounted.cpp), it is hard coded (delete this).

I am not sure if it is possible to overload the new/delete operators (as far as I know, it should be done within the class declaration).
Doesn't Urho3d define an interface for Memory/Object allocation ?

how is it possible to use a custom memory allocater.

RefCounted instance at constructor does allocate "new RefCount()", that looks very expensive, doesn't that effect on Urho3d performance!

it would be great to have some advice, hint about this.

regards

-------------------------

SirNate0 | 2022-04-29 17:45:29 UTC | #2

[quote="mohamed.chit, post:1, topic:7245"]
Doesn’t Urho3d define an interface for Memory/Object allocation ?
[/quote]

As far as I'm aware it does not. BUT...


[quote="mohamed.chit, post:1, topic:7245"]
it should be done within the class declaration
[/quote]

which you are free to edit since you have the source code. If you wanted it to apply to all classes derived from Urho3D::Object you could probably put it in the URHO3D_OBJECT macro.

Though it would surprise me if you got much of a performance enhancement from these changes, unless you are creating/destroying thousands (millions?) of objects every frame. (I'm no expert and I've never tried myself, so feel free to experiment, I would welcome a more concrete benchmark over my speculation).

-------------------------

1vanK | 2022-04-29 18:16:09 UTC | #3

At the moment, I believe that the bottleneck is a sending of messages, which is used quite heavily inside the engine.You can use `99_Benchmark.exe` > `Molecules` for test. In addition, we need a possibility of multiple handlers for each event: <https://github.com/urho3d/Urho3D/issues/2907>. PR are welcome

-------------------------

vmost | 2022-04-29 23:01:14 UTC | #4

You could check out [this discussion](https://discourse.urho3d.io/t/faster-allocations-with-pmr/7122) I started.

-------------------------

