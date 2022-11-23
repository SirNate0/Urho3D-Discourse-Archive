WangKai | 2020-11-15 14:51:46 UTC | #1

I found that the there is serious z-fighting on my Android phone. So I did a little investigation. 

It turned out that the format of the depth buffer created on my Android phone for Urho3D programs is **"D16"** while for OpenGL desktop / D3D11/D3D9, the default format of depth/stencil buffer is **"D24S8"**, which means on a physical mobile device, we are using 16bit depth vs 24bit normally on desktop! This surely causes a lot of issues.

I don't know the design and history of Urho3D's depth-buffer or detailed spec about EGL2.0, however, as a dirty quick test, by adding `SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 24); ` into `Graphics::SetScreenMode` of `OGLGraphics.cpp` makes the demo run normal:

```c++
#ifndef GL_ES_VERSION_2_0

        SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 24);

        SDL_GL_SetAttribute(SDL_GL_RED_SIZE, 8);

        SDL_GL_SetAttribute(SDL_GL_GREEN_SIZE, 8);

        SDL_GL_SetAttribute(SDL_GL_BLUE_SIZE, 8);

        if (externalWindow_)

            SDL_GL_SetAttribute(SDL_GL_ALPHA_SIZE, 8);

        else

            SDL_GL_SetAttribute(SDL_GL_ALPHA_SIZE, 0);

        SDL_GL_SetAttribute(SDL_GL_STENCIL_SIZE, 8);

        if (!forceGL2_)

        {

            SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, 3);

            SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, 2);

            SDL_GL_SetAttribute(SDL_GL_CONTEXT_PROFILE_MASK, SDL_GL_CONTEXT_PROFILE_CORE);

        }

        else

        {

            SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, 2);

            SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, 0);

            SDL_GL_SetAttribute(SDL_GL_CONTEXT_PROFILE_MASK, 0);

        }

#else

        SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, 2);

        SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, 0);

        SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 24); //<========= !!! Quick Test!!!

#endif
```

I think this will ask SDL to use eglChooseConfig to query a 24 bit depth size display for us.

Additionally, on my phone,  the following check passed, which means D24S8 is supported.
```c++
if (CheckExtension("GL_OES_packed_depth_stencil"))
        glesDepthStencilFormat = GL_DEPTH24_STENCIL8_OES;
```

Shall we check this failed before we decide not to call `SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 24);`?

-------------------------

WangKai | 2020-11-15 14:56:24 UTC | #2

I captuered the graphics trace of the app running my physical phone with RenderDoc.

This is the info I got when watching the original backbuffer:
![image|302x28](upload://zlqENcVdDQDTPDkWjRDMhIxxeHx.png) 

This is the info I got after the quick fix:
![image|368x34](upload://avqPGIUviEVGSMlMWFlDliA1fiV.png)

-------------------------

Eugene | 2020-11-15 15:03:47 UTC | #3

[quote="WangKai, post:1, topic:6526"]
Additionally, on my phone, the following check passed, which means D24S8 is supported.
[/quote]
There is an issue tho. `SDL_GL_DEPTH_SIZE` should be set **before** context creation, and extension check can be done only **after** context creation. So you cannot reliably check if you can actually set `SDL_GL_DEPTH_SIZE` to 24. I think the workaround was to create temporary context... But it will require certain work.

-------------------------

WangKai | 2020-11-15 15:16:10 UTC | #4

Thank for pointing out this Eugene,

I just checked SDL document https://wiki.libsdl.org/SDL_GL_SetAttribute
**"SDL_GL_DEPTH_SIZE - the minimum number of bits in the depth buffer; defaults to 16"**

This is truly an issue here. Any close faces look alright on desktop can potentially have z-fighting.
I'm still looking for a way to work around this. Edit: this explains why every Urho3D sample I saw on my phone is always flickering.

-------------------------

WangKai | 2020-11-15 17:16:00 UTC | #5

Another way is try both 24 bit and 16bit depth , this is great code -

https://github.com/gameplay3d/gameplay/blob/4de92c4c6f8047db5dcb7f0dee8541c7e7ea5a80/gameplay/src/PlatformAndroid.cpp#L241

-------------------------

Eugene | 2020-11-15 17:31:42 UTC | #6

Yep, we already do this stuff in Urho. Some kind of retry loop that tries several different context parameters. It checks multisampling now. I don't know how to expand this loop for depth buffer as well.

https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/OpenGL/OGLGraphics.cpp#L426-L456

-------------------------

WangKai | 2020-11-16 09:06:39 UTC | #7

Done.
https://github.com/SuperWangKai/Urho3D/commit/99566cf8bd2fbb0fc8df0f4dc60591f361d186f7

-------------------------

Eugene | 2020-11-16 09:33:13 UTC | #8

It's quite nasty approach tho. Would be even worse if we remember sRGB which should be tested in similar way (I don't know why it's not tested now).
Lemme check, maybe I'll find better way.

-------------------------

WangKai | 2020-11-16 10:40:03 UTC | #9

Please go ahead. 

From the current implementation in Urho OpenGL, it seems sRGB is not related to the code I changed.

Edit: sRGB of OGL seems not related to the context creation. If there are no more factors to extend the support, I think the code I'm current use should be OK.

-------------------------

Eugene | 2020-11-16 13:13:58 UTC | #10

I did a bit of googling, and apparently OpenGL doesn't let user query max allowed values easily.
I think your solution is good enough, we can always change it later.

I don't like infinite loops in old code, cleaned it up a bit:
https://github.com/urho3d/Urho3D/pull/2726 
I hope it's okay.

-------------------------

WangKai | 2020-11-17 09:59:15 UTC | #11

I like the change from `while` to `for`, makes simpler code  :)

-------------------------

