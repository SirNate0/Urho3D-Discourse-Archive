Sunc | 2022-08-25 07:18:27 UTC | #1

I am doing PBR rendering with Urho3D, the workflow I took is just as the PBRMaterials sample.
Since sRGB texture format is used, the gamma correction postprocess is appended, everything looks alright except the sky box.
In the PBRMaterials sample, there are no texture configure files(xml) along with the sky box textures to mark them as sRGB enabled, which I think is a missing stuff.
And after I tried adding these xml files, things make no different to the rendering result, the sky box looks too much white if tonemap and autoexposure is disabled.
Any one help me.

-------------------------

