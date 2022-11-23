HaeferlKaffee | 2018-08-09 23:54:58 UTC | #1

Is there a way to render to a different resolution than the viewport? e.g. 1920x1080 viewport and window, but 192x108 raster size

-------------------------

Eugene | 2018-08-10 06:14:23 UTC | #2

Rendertargets could have arbitrary sizes specified in RenderPath
https://urho3d.github.io/documentation/HEAD/_render_paths.html

-------------------------

HaeferlKaffee | 2018-08-11 00:15:16 UTC | #3

The problem with that is that I don't think it's possible to edit the output of the base renderpaths. They don't output to rendertargets seemingly

-------------------------

Bananaft | 2018-08-13 08:03:52 UTC | #4

https://github.com/urho3d/Urho3D/blob/master/bin/Data/PostProcess/BloomHDR.xml
Check BloomHDR as an example. It creates rendertargests of smaller size and stretches them back to fullscreen.

there is also a quick but dirty way to set this up: render everything to texture then diplay it as UI billboard.

-------------------------

