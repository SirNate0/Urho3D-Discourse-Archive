magic.lixin | 2017-01-02 01:08:26 UTC | #1

here is my setup:

   RenderPath@ renderpath =  renderer.viewports[0].renderPath.Clone();
    renderpath.Load(cache.GetResource("XMLFile","RenderPaths/ForwardHWDepth.xml"));
    renderpath.Append(cache.GetResource("XMLFile","PostProcess/AutoExposure.xml"));
    renderpath.Append(cache.GetResource("XMLFile","PostProcess/BloomHDR.xml"));
    renderpath.Append(cache.GetResource("XMLFile","PostProcess/Tonemap.xml"));
    renderpath.Append(cache.GetResource("XMLFile","PostProcess/ColorCorrection.xml"));
    renderpath.SetEnabled("TonemapReinhardEq3", false);
    renderpath.SetEnabled("TonemapUncharted2", true);
    renderer.viewports[0].renderPath = renderpath;

  it`s too dark if enable tonemap.

  with tonemap:
   [img]http://i.imgur.com/a1POr2j.png[/img]

 without tonemap:
   [img]http://i.imgur.com/jJsFV2f.png[/img]

 am I doing something wrong ?

-------------------------

codingmonkey | 2017-01-02 01:08:26 UTC | #2

Probably you need tweak uniforms for tonemaping

world.camera.effectRenderPath->SetShaderParameter("TonemapMaxWhite", 1.8f);
world.camera.effectRenderPath->SetShaderParameter("TonemapExposureBias", 2.5f);

-------------------------

magic.lixin | 2017-01-02 01:08:27 UTC | #3

thanks, it looks brighter now.

-------------------------

