Synex | 2017-09-15 19:13:55 UTC | #1

Hey guys, just to let you know the Box2D constraints sample hosted at [https://urho3d.github.io/samples/32_Urho2DConstraints.html](https://urho3d.github.io/samples/32_Urho2DConstraints.html) doesn't work correctly.

Tested on Firefox *(55.0.3 (32-bit))* and Chrome *(Version 60.0.3112.113 (Official Build) (64-bit))*, I am unable to drag the footballs around and test the constraints. Keyboard input seems to work so I unsure why mouse input wouldn't work. 

I would investigate further, but I don't have much time on my hands but I thought its worth mentioning.

In the meantime can anyone else confirm this issue?

-------------------------

Eugene | 2017-09-15 19:08:23 UTC | #2

Chrome 60.0. Confirmed. Emscripten is such a pain...

-------------------------

weitjong | 2017-09-16 05:59:17 UTC | #3

I think the problem is with the sample or the engine itself and has nothing to do with the compiler toolchain or the viability of the Web platform. In general all our samples were originally written just for native desktop platform. Over time when we added additional support for the other platforms, Rasperry-PI, Web, tvOS, you name it, we didn't retrofit them one by one to ensure each sample works as intended. Contribution is welcome.

-------------------------

