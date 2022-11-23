nergal | 2017-12-01 15:11:13 UTC | #1

I've developed a very basic physics-"engine" for some blocks in my game (required a less accurate one compared to bullet). However, it calculates positions on CPU. Is there a way to instead use the GPU to both increase performance AND number of objects used (boxes)?

I'm guessing that it's somehow possible using shaders, but I'm not sure. If so, are there any good tutorials/examples for using custom shaders with Urho3d?

Thanks!

-------------------------

Eugene | 2017-12-01 15:36:53 UTC | #2

[quote="nergal, post:1, topic:3808"]
I’m guessing that it’s somehow possible using shaders, but I’m not sure. If so, are there any good tutorials/examples for using custom shaders with Urho3d?
[/quote]

There is no good routine for GPU computations in Urho for now.

Urho definetely need compute shaders support, and I hope they'll be implemented at some point after BGFX backend implementation.

-------------------------

Bananaft | 2017-12-03 10:10:10 UTC | #3

I did GPU collision check for my fractal exploration game. It works on pixel shader. But my case is specific and I guess, this approach can't be used in general case. Also, I still use Bullet alongside.

https://twitter.com/i/moments/937261051007160320

What was the results of your optimization experiments? Did you got any meaningful boost?

https://discourse.urho3d.io/t/optimise-physics/3711

-------------------------

nergal | 2017-12-03 10:20:03 UTC | #4

I managed to get around 1000 blocks with bullet, but I had to tweak so that it looked a bit strange using layers. But I created my own physics engine in the end to allow me for a lot of more blocks. But instead I make the physics much less accurate. But for my project I just want to get debris shattered before I add it to the voxel-world itself.

I wish it were possible to configure bullet within urho3d in some easy manner. I've used bullet with ThreeJS for WebGL and it was possible to modify attributes for the bullet engine to optimise usage.

-------------------------

weitjong | 2017-12-03 12:18:10 UTC | #5

We do not use Bullet provided CMake build scripts so all the original configurable build options got lost as the result. In theory it should be possible to integrate its build scripts with our build system, if we really want to. We have successfully done that with SDL some time back. Contribution is welcome.

-------------------------

