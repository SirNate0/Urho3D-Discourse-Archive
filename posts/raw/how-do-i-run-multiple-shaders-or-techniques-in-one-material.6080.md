throwawayerino | 2020-04-12 14:02:09 UTC | #1

I want to draw an outline around a mesh. I have a simple shader ready but can't seem to load it. Only the first technique in the material is being loaded.

-------------------------

jmiller | 2020-04-12 14:49:17 UTC | #2

It seems Techniques are selected by Renderer::SetMaterialQuality() and LOD distance:
  https://urho3d.github.io/documentation/HEAD/_materials.html

Our 'Outline shader' thread, with solutions modifying RenderPath:
  https://discourse.urho3d.io/t/outline-v2/1766

-------------------------

