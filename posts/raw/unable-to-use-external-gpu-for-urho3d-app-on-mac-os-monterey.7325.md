daokoder | 2022-09-13 12:54:01 UTC | #1

Hello! I recently upgraded my macbook pro from Mojave to Monterey. Everything work fine for me except some minor issues. But one thing bugs me the most is the strange problem I encountered when trying to use an external GPU to run an Urho3D application.

The problem is that, if I configure an app bundle to prefer the external GPU (AMD Radeon RX 580), the app will run using a software renderer!

![Urho3D_Using_SoftwareRenderer_for_ExternalGPU|690x394](upload://dDoM4ztGkBMRCd8txjSTiu8Ujkd.jpeg)

This is very weird! I have spent more than one day trying to solve the problem without success. Anyone knows how this happens or how to fix it? Thanks a lot!

-------------------------

SirNate0 | 2022-09-13 20:31:02 UTC | #2

I'm not at all sure, but I wonder based on this list if Apple always give that string for the graphics adapter?

https://feedback.wildfiregames.com/report/opengl/feature/GL_MAX_3D_TEXTURE_SIZE

Or maybe not. Not sure. But here's some info about storing multiple GPUs or switching GPUs in an application. I'm not sure how you're trying to run on the external GPU, or what Urho is doing on a Mac, but it might be helpful for figuring out what is happening. Unfortunately I don't have a Mac, so I can't really help you any more than this.

https://developer.apple.com/library/archive/qa/qa1734/_index.html

-------------------------

daokoder | 2022-09-14 07:07:26 UTC | #3

Thank you for trying to help.

> I’m not at all sure, but I wonder based on this list if Apple always give that string for the graphics adapter?

No, it gives the right vendor and card information for the integrated GPU (and for the external GPU as well before the system upgrade). And it was actually using a software renderer with an extremely poor performance.

>  I’m not sure how you’re trying to run on the external GPU, or what Urho is doing on a Mac, but it might be helpful for figuring out what is happening.

Among a few laptops I am using for developing and testing, only Macbook Pro that has a sufficiently powerful CPU. I am trying to use it to test and record some videos for my game, but its GPU is too poor, so I have to use an external GPU for this.

Luckily, by looking through SDL source code and Apple's online documentation for OpenGL, I just found a solution, by adding the following line in Graphics::SetMode() to enforce the using of hardware accelerated drivers:
```
SDL_GL_SetAttribute(SDL_GL_ACCELERATED_VISUAL, 1);
```
Now it can ignore Apple's software renderer and use the external GPU properly as before.

-------------------------

