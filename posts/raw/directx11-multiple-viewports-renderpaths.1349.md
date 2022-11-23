Bart | 2017-01-02 01:07:02 UTC | #1

Hi,
I noticed (maybe a bug?) strange behaviour:

[ul][b]Steps to reproduce[/b]
[*]I used main branch version 1.4.441[/*]
[*]Configure with 64bit, DX11 and Samples with "Visual Studio 12 2013" (happens also for 32bit)[/*]
[*]In sample 09_MultipleViewports, there is demonstration how to add and toggle shader effects for main viewport. If you try to apply the same renderpath to the secondary view (rearview mirror like) the secondary view goes black when an effect is enabled. Effect is correctly switched on for the main view[/*][/ul]

This works correctly for DX9. I tried adding a new RenderPath object for secondary viewport, still the same behaviour. With DX9, I could use single RenderPath object for 4 viewports, toggle efects on it and I affected all viewports without problems.

Am I missing something with DX11 or is this a bug?

Bloom ON:
[img]http://imageshack.com/a/img910/1043/Qwf3cZ.png[/img]

Bloom OFF:
[img]http://imageshack.com/a/img538/7049/snZ7YK.png[/img]

Changes in code (MultipleViewports.cpp):
[code]void MultipleViewports::SetupViewports()
{
    Graphics* graphics = GetSubsystem<Graphics>();
    Renderer* renderer = GetSubsystem<Renderer>();

    renderer->SetNumViewports(2);

    // Set up the front camera viewport
    SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraNode_->GetComponent<Camera>()));
    renderer->SetViewport(0, viewport);

    // Clone the default render path so that we do not interfere with the other viewport, then add
    // bloom and FXAA post process effects to the front viewport. Render path commands can be tagged
    // for example with the effect name to allow easy toggling on and off. We start with the effects
    // disabled.
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    SharedPtr<RenderPath> effectRenderPath = viewport->GetRenderPath()->Clone();
    effectRenderPath->Append(cache->GetResource<XMLFile>("PostProcess/Bloom.xml"));
    effectRenderPath->Append(cache->GetResource<XMLFile>("PostProcess/FXAA2.xml"));
    // Make the bloom mixing parameter more pronounced
    effectRenderPath->SetShaderParameter("BloomMix", Vector2(0.9f, 0.6f));
    effectRenderPath->SetEnabled("Bloom", false);
    effectRenderPath->SetEnabled("FXAA2", false);
    viewport->SetRenderPath(effectRenderPath);

    // Set up the rear camera viewport on top of the front view ("rear view mirror")
    // The viewport index must be greater in that case, otherwise the view would be left behind
    SharedPtr<Viewport> rearViewport(new Viewport(context_, scene_, rearCameraNode_->GetComponent<Camera>(),
        IntRect(graphics->GetWidth() * 2 / 3, 32, graphics->GetWidth() - 32, graphics->GetHeight() / 3)));
    renderer->SetViewport(1, rearViewport);
    rearViewport->SetRenderPath(effectRenderPath);                  ////// ONLY ADD THIS LINE  ///////
}[/code]

-------------------------

cadaver | 2017-01-02 01:07:02 UTC | #2

Bug confirmed. I suspect this is related to the viewport being less than screen-sized, in which case viewport clear on D3D11 doesn't happen in an usual way, but is emulated with shaders.

EDIT: problem is broken implementation of Graphics::ResolveToTexture() on D3D11. However D3D11 lacks StretchRect, so it must be worked around.

-------------------------

cadaver | 2017-01-02 01:07:02 UTC | #3

Should be fixed in the master branch. Note that this is not a perfect fix, as an antialiased less-than-fullscreen viewport on D3D11 will lose its antialiasing when it has postprocessing effects. However it should no longer output black.

-------------------------

Bart | 2017-01-02 01:07:04 UTC | #4

Thank you for this super quick fix!

Does this mean that FXAA2 and FXAA3 shaders will not produce antialiasing, or does your remark concerns some other (built-in) AA in D3D11? Will this probably be fixed for next official release? I would like to help, but I am afraid that my knowledge about this tricky area is basically zero..   :frowning: 

Thumbs up for supporting D3D11, it gives me more than 4x higher FPS than D3D9 on my box (workstation with nVidia Quadro K2200).

-------------------------

cadaver | 2017-01-02 01:07:04 UTC | #5

FXAA2/3 will always work. Hardware MSAA will not, unless the viewport covers the full window.

Likely this could be fixed with a copy (using shader + drawcall) to an intermediate texture, but this loses some performance.

-------------------------

cadaver | 2017-01-02 01:07:05 UTC | #6

Should now be properly fixed in the master branch. Multisampled screenshots already required a similar intermediate texture (but it was being discarded), so I now create a permanent intermediate texture on demand, resolve the whole screen, and then copy the smaller rect from the intermediate texture to target. This performs some unnecessary work, which possibly could be eliminated by sampling only the necessary area in a drawcall + shader, but at least works correctly.

-------------------------

Bart | 2017-01-02 01:07:12 UTC | #7

Thank you very much for your work on this engine!!

-------------------------

