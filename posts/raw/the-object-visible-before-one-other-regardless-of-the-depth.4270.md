Marcin | 2018-05-29 08:13:30 UTC | #1

Hi,
I would like to have one object (StaticModel) always visible over one chosen another object (regardless of depth), something like using technique 'NoTextureOverlay', but my object should be rendered normally in relation to all other models (with depth test, etc...). Please, let me know how to do it?
Thanks in advance

-------------------------

Eugene | 2018-05-29 09:32:51 UTC | #2

It's quite tricky request because it contradicts usual rendering pipeline.
It's possible with stencil tricks, but this is really hard way.
What's the target hardware and how much objects you want to draw this way?

-------------------------

Marcin | 2018-05-29 10:00:16 UTC | #3

Thanks for your answer, I was hoping that there is some simple way to do this...
I want to draw only one object this way. Target platform: PC with Windows.

-------------------------

Eugene | 2018-05-29 10:59:36 UTC | #4

The problem is that you need depht test enabled to draw any non-convex object, so you need depth test on for both objects. On the other hand, you don't want these objects to interfere with each other...

If you use forward lighting for these objects, the problem become even more severe.

Possible solution (no forward lighting) is:

1. Draw object _below_, depth test on, depth write on.
2. Redraw the object _below_ with custom shader that sets depth to 1. depth test on, depth write on, depth function equal.
3. Draw object _above_, depth test on, depth write on.
4. Draw object _below_ again, depth test on, depth write on, _color write off_.

In the result you will get object _below_, overlapping object _above_ and valid depth for both objects.

-------------------------

TheComet | 2018-05-29 13:57:48 UTC | #5

This might be of interest: https://discourse.urho3d.io/t/how-to-control-render-order/1240

-------------------------

