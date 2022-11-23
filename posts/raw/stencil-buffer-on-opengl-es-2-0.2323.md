sabotage3d | 2017-01-02 01:14:45 UTC | #1

I am using Stencil buffer on Desktop and everything works fine when I switch to ES 2.0 on Android it stops working. Is there a way I can enable it?

-------------------------

cadaver | 2017-01-02 01:14:45 UTC | #2

Stencil functionality is currently totally disabled for OpenGL ES 2. I no longer remember what exact errors trying to use it led to, or was it just that it reduced performance. FBO rendering with stencil was also unavailable due to lack of a properly functioning packed depth+stencil format, and creating depth / stencil separately didn't work either from what I remember. Stencil not being supported is documented in the "API differences" section of the documentation.

You may want to try to undo the ifdefs related to stencil disable from OGLGraphics.cpp and see what happens.

-------------------------

sabotage3d | 2017-01-02 01:14:45 UTC | #3

Thanks cadaver. Is there a way I can set it with raw GL calls as it might be quicker than modifying the engine. There are some UI libraries and vector graphics libraries which are using the stencil buffer heavily. I just want to quickly check on a few mobile devices with Android if the stencil will work at all if not I will try to make it work without it.

-------------------------

cadaver | 2017-01-02 01:14:45 UTC | #4

You can use raw GL to test, but you need to modify the SDL OpenGL initialization in OGLGraphics.cpp to request a stencil buffer.

-------------------------

sabotage3d | 2017-01-02 01:14:45 UTC | #5

These two seems to be already enabled for GL_ES_VERSION_2_0
[code]SDL_GL_SetAttribute(SDL_GL_STENCIL_SIZE, 8);

glEnable(GL_STENCIL_TEST);[/code]
Is there anything else I need to set? 
Do I need this guy as well?
[code]glFramebufferRenderbuffer(GL_FRAMEBUFFER, GL_STENCIL_ATTACHMENT, GL_RENDERBUFFER, object);[/code]

-------------------------

cadaver | 2017-01-02 01:14:45 UTC | #6

Please check again, SDL_GL_SetAttribute(SDL_GL_STENCIL_SIZE, 8) should be ifdeffed out for GLES.

If you test to the backbuffer only, you don't need setting the stencil attachment. If you need stenciling when rendering to a texture, you may try enabling that, but like I said I remember having no luck with a suitable stencil format.

-------------------------

sabotage3d | 2017-01-02 01:14:47 UTC | #7

Yeah I have no luck as well. I anyone had any success with this please share your input.

-------------------------

sabotage3d | 2017-01-02 01:14:47 UTC | #8

I finally got it working. I was trying to set it outside of Urho3D but it works only if I do it inside the OGLGraphics. Can we please have it by default enabled I don't think it would do any harm?

[code]#else
        SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, 2);
        SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, 0);

        SDL_GL_SetAttribute(SDL_GL_STENCIL_SIZE, 8);
#endif[/code]

-------------------------

cadaver | 2017-01-02 01:14:48 UTC | #9

It's probably acceptable, will have to confirm later with actual hardware testing. I don't think I'll actually make the engine use stencil by itself (light stencil mask optimization) on OpenGL ES since it's a bit unsure territory, but for custom rendering it should be fine.

-------------------------

glebedev | 2021-02-16 13:12:36 UTC | #10

I know quite some time passed, but maybe you remember if stencil should be enabled for GL ES 3.0. Should it?

-------------------------

WangKai | 2021-02-17 03:24:45 UTC | #11

Reminds me of this - 
https://discourse.urho3d.io/t/depth-stencil-buffer-issue-on-gles-2-0/6526

-------------------------

WangKai | 2021-02-17 03:26:53 UTC | #12

And stencil on non-GLES 2.0 is already enabled by -
```
SDL_GL_SetAttribute(SDL_GL_STENCIL_SIZE, 8);
```

-------------------------

Eugene | 2021-02-17 05:56:12 UTC | #13

[quote="WangKai, post:12, topic:2323"]
And stencil on non-GLES 2.0 is already enabled by -
[/quote]
The issue is that GLES 3.0 _is_ GLES 2.0 too, therefore it has stencil disabled.

-------------------------

cadaver | 2021-02-17 11:18:42 UTC | #14

In my time I don't think I ever tried to enable GLES3 or test it personally, so it's best I don't comment inaccurately.

-------------------------

