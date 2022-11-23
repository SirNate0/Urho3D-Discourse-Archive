HappyWeasel | 2021-01-16 09:49:35 UTC | #1

Hi,

I understand Urho3d supports setting LODs per model. How does that affect an animated model? In my 3d application, I can bind the mesh to a rig and animate it. Exproting as fbx and getting into my urho code works fine. Do I have to repeat that process for every LOD ? (i.e. bind it to the rig, export as fbx, set as lod in the assetimporter - btw not sure how that works).. And what happens to the animation if I "zoom out", and the "LOD switches", will "the animation continue" .

Thanks for help/info. Maybe I just have some wrong concepts about how this is supposed to work. 
Greetings

-------------------------

Eugene | 2021-01-16 10:44:30 UTC | #2

All LODs share the same set of transforms, so animation works independently of LOD. All lods should be in one model file, too.
I don’t know how asset importing pipeline should work as I never tried it myself.

-------------------------

