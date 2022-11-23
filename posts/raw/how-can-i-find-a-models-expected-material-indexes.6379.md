evolgames | 2020-09-09 18:07:24 UTC | #1

So if I export a blender object (obj in this case. fbx works too), I can run it through asset importer to get the resulting .mdl + materials/textures. In my case, I'm not using textures. In Urho, I do the following to set the materials to the write index:
```
roadObject.model = cache:GetResource("Model", "Models/roadSeg.mdl")
roadObject:SetMaterial(3,cache:GetResource("Material", "Materials/Road.xml"))
roadObject:SetMaterial(4,cache:GetResource("Material", 
```
and so on and so on.

Some of the objects could have 20 indexes. The thing is, any change to the object reorders these. And they are seemingly randomly ordered. So I am playing a guessing game for each model to figure out where the materials go. This is strictly just flat-shaded color materials assigned in blender, no uv wrapping or anything.

Maybe this is just a blender thing...I took a look at the .obj and .mtl in a text editor but didn't see anything standing out. Is there a way to figure out the index expectation without guessing? I mean, it works, but there's got to be a simpler way.

-------------------------

Modanung | 2020-10-01 06:40:52 UTC | #2

In edit mode, select all faces and pick _Mesh_ -> _Sort Elements..._ -> _Material_.

-------------------------

evolgames | 2020-10-01 02:40:48 UTC | #3

Okay, totally forgot the Editor does this automatically. For anyone interested, the better solution is to copy what the Editor is doing, specifically in this file:
`/bin/Data/Scripts/Editor/EditorImport.as`

As you can then, with code, automatically load a model with the correct materials applied in the right indexes. I believe in one of the Jack samples, because he is simply 2 material textures, the technique is done how I did it in the OP. Since there are only two, it's trivial to guess. However, this doesn't mean it's the correct choice for every situation. It makes more sense to have an automated approach, which is what you'd get if you make your game in the editor itself. Consider multiple models with 20+ materials. Even if you know the corresponding indexes and names, it makes more sense to have this done automatically.

-------------------------

George1 | 2020-10-01 08:57:40 UTC | #4

You need to design your game so that the number of materials will be the same for a specific group of object types.   This way the code is always the same...   Just recognize the type and execute the code.
 Never have too many object groups.

-------------------------

Modanung | 2020-10-01 09:44:18 UTC | #5

You could also create `ModelName.txt` material lists.

-------------------------

