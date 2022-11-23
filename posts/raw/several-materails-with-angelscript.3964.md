berrymooor | 2018-01-26 11:22:45 UTC | #1

Hi, simple question:
if i implementing model with one material via AngelScript, it's look like this:

**jack.material = cache.GetResource("Material", "mat.xml");**

But how about models with several matarials? How attach second material of model for example?

-------------------------

Dave82 | 2018-01-25 17:25:03 UTC | #2

Use the set_materials method which accepts the index of the material.The number of materials should be equal to number of vertex buffers per model

[code]
jack.set_materials(0 ,  cache.GetResource(“Material”, “mat.xml”));
jack.set_materials(1 ,  cache.GetResource(“Material”, “mat2.xml”));
jack.set_materials(2 ,  cache.GetResource(“Material”, “mat3.xml”));
[/code]

-------------------------

Eugene | 2018-01-26 12:46:51 UTC | #3

`set_*` and `get_*` methods are internal property accessors.
Just use properties: `jack.materials[0]`

-------------------------

1vanK | 2018-01-25 19:34:35 UTC | #4

u can use ApplyMaterialList() for models with multiple materials (blender can generate this list)

-------------------------

Modanung | 2018-01-26 11:26:17 UTC | #5

https://discourse.urho3d.io/t/models-with-multiple-materials/3895/3?u=modanung

-------------------------

