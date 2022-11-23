tbutton2005 | 2019-05-12 05:29:43 UTC | #1

hi. how to use pbr in urho3d?

-------------------------

jmiller | 2019-05-12 06:33:35 UTC | #2

Hi,

The 42_PBRMaterials sample demonstrates PBR. C++ version for reference:
  https://github.com/urho3d/Urho3D/tree/master/Source/Samples/42_PBRMaterials

Its scene file
  https://github.com/urho3d/Urho3D/blob/master/bin/Data/Scenes/PBRExample.xml
also references some resources in the `bin/AutoLoad` directory
  https://github.com/urho3d/Urho3D/tree/master/bin/Autoload/LargeData

Extended material definitions, roughness-metallic maps, HDR skybox maps..

There are a number of [PBR-related threads](https://discourse.urho3d.io/search?q=PBR), some with more [implementation details](https://discourse.urho3d.io/t/physically-based-rendering-v2/1797).

related docs (non-PBR-specific)
[materials](https://urho3d.github.io/documentation/HEAD/_materials.html)
[render path](https://urho3d.github.io/documentation/HEAD/_render_paths.html)

-------------------------

Leith | 2019-05-12 09:51:44 UTC | #3

Yeah I kind of avoided replying to this one, because there is a decent demo, but then I went and looked in the sourcecode for tutorial 42, and found it lacking in detail. There is almost nothing to learn from the sourcecode, and given that it is the flagship product for educating the public how to use it, I find it lacking, and mostly, in substance.

-------------------------

