davemurphy | 2018-07-20 14:39:01 UTC | #1

I'm trying to use raycast on models I've imported from the Blender mdl exporter. I've been having trouble with the Avocado model from the glTF 2.0 sample repository. The model is relatively small and I need to set it's scale to 30 to make it the size I want. The problem is when I RaycastSingle with RAY_TRIANGLE it won't hit the back of the avocado model, just the front part and the pit. When the model is scaled to 1 raycasts work fine. 

Has anyone else had an issue with raycasts not working on their own models when scaled? And Is this a problem with the model or are there limitations to the triangle raycast algorithm that I don't know about?

Here is the source model, you'll also need a Blender glTF importer.
https://github.com/KhronosGroup/glTF-Sample-Models/tree/master/2.0/Avocado
https://github.com/ksons/gltf-blender-importer

-------------------------

Eugene | 2018-07-24 14:32:07 UTC | #2

If you add `ret.direction_.Normalize();` just before `return ret;` in function `Ray::Transformed` in `Ray.cpp`, would it fix your problem?

-------------------------

davemurphy | 2018-07-24 14:32:15 UTC | #3

Thanks!

Normalizing the ray direction does fix the problem of the ray not hitting the mesh. However, it changes the position returned by the raycast to be in model space. In my case, I'm using uniform scaling, so the hit distance can be scaled by any component of the model's world scale.

According to the comment by Nathan Reed on [this StackOverflow answer](https://gamedev.stackexchange.com/questions/72440/the-correct-way-to-transform-a-ray-with-a-matrix), if you used non-uniform scales, the point returned by the raycast should be transformed back to world space.

DMGregory in comment to Nathan's answer also states that you can store the scale factor used to normalize the direction vector (invLen in Vector3::Normalize). Although I'm not sure the best way to propagate invLen up to StaticModel::ProcessRayQuery.

-------------------------

