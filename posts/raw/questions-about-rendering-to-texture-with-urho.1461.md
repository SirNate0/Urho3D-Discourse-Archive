Enhex | 2017-01-02 01:07:52 UTC | #1

Is it possible to render to texture once?
Is it possible to render to only part of a texture, to create atlases?

I want to render images once in real time and save them to atlases to be used by billboards.

-------------------------

codingmonkey | 2017-01-02 01:07:52 UTC | #2

hi
you can attach texture2d to Viewport, get RenderSurface and set manual update (for once render)

RenderSurface->SetUpdateMode(RenderSurfaceUpdateMode mode);

enum RenderSurfaceUpdateMode
{
    SURFACE_MANUALUPDATE = 0,
    SURFACE_UPDATEVISIBLE,
    SURFACE_UPDATEALWAYS
};

>Is it possible to render to only part of a texture, to create atlases?
it tricky say and find way how make this, but you may try
0. create hi-res RT (atlas)
1. create low-res rendertarget
2. render model into in low-res rendertarget
3. bind hi-res RT and use your own CustomCopyFramebuffer shader + ScissorsTest(or discard pixels by texCoords) to copy from low-res render target into selected place into Atlas.

-------------------------

