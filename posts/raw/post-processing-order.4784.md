GodMan | 2018-12-31 13:48:58 UTC | #1

I've read on the forums that the AutoExposure, and bloom need to be in a certain order for the results to be render correctly. Is this correct? I get a little color washing if anyone has seen my post under the projects thread. It's not bad, but look a little off to me.

    	graphics->SetSRGB(true);
    	renderer->SetHDRRendering(true);

    	effectRenderPath->Append(cache->GetResource<XMLFile>("PostProcess/AutoExposure.xml"));
    	effectRenderPath->Append(cache->GetResource<XMLFile>("PostProcess/BloomHDR.xml"));
    	effectRenderPath->Append(cache->GetResource<XMLFile>("PostProcess/Tonemap.xml"));
    	effectRenderPath->Append(cache->GetResource<XMLFile>("PostProcess/FXAA2.xml"));

    	effectRenderPath->SetEnabled("BloomHDR", true);
    	effectRenderPath->SetEnabled("FXAA2", true);
    	effectRenderPath->SetShaderParameter("BloomHDRMix", Vector2(exposure, 2.0f));

-------------------------

GodMan | 2018-12-31 23:17:05 UTC | #2

So no one knows if AutoExposure should come before or after BloomHDR?

-------------------------

Modanung | 2019-01-01 14:03:37 UTC | #3

No, everyone's hung over from new year's eve.

Also, happy new year! :confetti_ball: :slightly_smiling_face:

-------------------------

GodMan | 2019-01-01 15:11:32 UTC | #4

LOL, I figured that was it. :stuck_out_tongue:

I tried searching the docs, and the forums, but did not find anything.

-------------------------

1vanK | 2019-01-02 10:12:29 UTC | #5

 https://discourse.urho3d.io/t/some-questions-on-hdr-and-srgb/1207/7

-------------------------

GodMan | 2019-01-02 14:36:52 UTC | #6

Thanks. I did not find this on my initial search.

    	effectRenderPath->Append(cache->GetResource<XMLFile>("PostProcess/FXAA2.xml"));
    	effectRenderPath->Append(cache->GetResource<XMLFile>("PostProcess/AutoExposure.xml"));
    	effectRenderPath->Append(cache->GetResource<XMLFile>("PostProcess/BloomHDR.xml"));
    	effectRenderPath->Append(cache->GetResource<XMLFile>("PostProcess/Tonemap.xml"));

This is how I have it now.

-------------------------

