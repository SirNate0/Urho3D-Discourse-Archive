evolgames | 2021-04-13 04:46:46 UTC | #1

Is there a known issue with using materials on a torus?
Basically, I made a torus in blender and no matter what I tried I could not get a material applied to it. I did a simple diffuse color .XML file and it would flicker between that and the default color. Some of the faces of the torus (flat shaded) would be the correct color and others not. Rotation in game would flicker this. Sometimes I'd get it jumping between random colors. I have a color palette method I use with UVs and trying that did the same thing. The only thing that fixed it was adding a more primitive mesh along with the object in blender. So, it was a torus and cube as one object. Then everything worked as expected. The solution is kind of dumb but I just hid a tiny cube inside the torus. Just wondering if anyone else ran into this? Why would this happen? Godot didn't do this. Is Urho assuming something about the normals of the torus? I tried recalculation and different UV unwrapping. But in the end none of that worked nor is necessary if a cube is within the same object. So weird.

-------------------------

Nerrik | 2021-04-13 09:13:36 UTC | #2

When you use Normalmaps you have to precalculate the tangents with the Assetimporter
"Assetimporter model obj.obj mdl.mdl -t"

or maybe you have some z-fighting https://discourse.urho3d.io/t/solved-z-fighting/2081

-------------------------

SirNate0 | 2021-04-13 14:20:23 UTC | #3

Is your material set up correctly (has a texture if the technique expects one, uses the correct technique, etc.)? When you added the cube, did it perhaps change the material? And/or did you change whether you included the normals or something like that?

-------------------------

evolgames | 2021-04-13 17:29:45 UTC | #4

Yeah I tried both with and without textures, using the most simple materials possible. Also tried generating them in code. All of the methods worked for every other object in my game, too. The only thing that changed to the model was adding a cube to it. The cube's material was the same as the torus, and urho set the combined object to a simple diffuse color perfectly afterward. Maybe asset importer is reading the model differently. Though I tried fbx, obj, and dae. I'm going to try @Nerrik  's suggestion and make some steps for reproduction.

-------------------------

Modanung | 2021-04-13 18:05:19 UTC | #5

Does the same problem occur when using the torus that comes with the engine?
And could you share the glitching blend/model you're using?

Also, OpenGL or DirectX?

-------------------------

evolgames | 2021-04-14 00:29:56 UTC | #6

Thanks for the replies guys. @Nerrik -t didn't seem to work. I think something is going on with the parent node. This is a child node of a raycast vehicle and it seems the problem is not the model but this setup somehow. This is getting confusing.
If I use a fresh torus unmodified from blender and child it to the raycast vehicle node, the color will change randomly with rotation. If it is childed to the scene_ then nothing is wrong with the material.
Same thing happens with the Urho torus, and goes away if it's parent is the scene_ node and not the raycast vehicle. Same thing happens with cubes and combinations of the two. So it seems like the problem is not the model. This is opengl.

-------------------------

SirNate0 | 2021-04-14 02:31:44 UTC | #7

Does the raycast vehicle change the color of its children or anything like that?

-------------------------

evolgames | 2021-04-14 04:00:16 UTC | #8

No no it's just the raycast sample set up with some variable tweaks and different models. adding the steering wheel as a child made sense but I'm not sure why that would do this.

-------------------------

SirNate0 | 2021-04-14 04:05:03 UTC | #9

Are you getting any warnings about resources not being found in the log? Is the torus only a single geometry (in Urho, not in blender)?

-------------------------

evolgames | 2021-04-14 04:16:45 UTC | #10

Nope. I tried a little test by editing the 46_RaycastVehicleDemo sample to add the following:

```
	local obj = node:CreateChild()
	obj:SetPosition(Vector3(0,1,0))
	local staticModel = obj:CreateComponent("StaticModel")
	staticModel.model = cache:GetResource("Model", "Models/Box.mdl")
	staticModel:SetMaterial(cache:GetResource("Material", "Materials/Black.xml"))
```

which is where I run into the problem in my project. However, this works fine (node being the self.node for the vehicle script). Something my car does is the hull is currently having its materials applied via MaterialList, if that matters? I mean, it's not really an issue since from here I can simply parent the steering wheel (and other separate parts) elsewhere, but I don't know, maybe I'm doing something unproper.

Yes, the torus was single geometry. Childing Urho's box.mdl like above causes the issues in my project same as the torus.

-------------------------

