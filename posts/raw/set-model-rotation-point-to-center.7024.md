MtrnXf | 2021-10-29 12:17:03 UTC | #1

Hello there. Ich have a model of a window of a building which geometry center is not at the middle of the object but at the left-bottom. Additionally the model is too huge according to it's world (grid). So when rotating the model it's not turning around it's center but around point left-bottom like an egg. I tried to modify the model with "SetGeometryCenter(0,...)" method at runtime before adding it to the root node, but nothing changes.
Can you help me with some code to modify the model so that it rotates around its center? Huge thanks

[Link to Window.mdl](https://filehorst.de/d/eEHngial)

-------------------------

Eugene | 2021-10-29 12:39:32 UTC | #2

The easiest way to fix transforms is on the level of Scene.
E.g. if your model has wrong center, you:
1) Add root node where the center of your model _should_ be.
2) Add child node used for offset.
3) Add your model to child node.
4) Move child node used for offset so the center of the model is where you want it to be.
5) Rotate root node.

-------------------------

MtrnXf | 2021-10-29 21:43:02 UTC | #3

It works, thank you :grinning:

*//Root node for rotation*
Node rootNode = Scene.CreateChild("RootNode");
rootNode.Position = new Vector3(x: 0, y: 0, z: 0);

*//Child node with negative offset to emulate new center of the model*
Node childNode = rootNode.CreateChild("ChildNode");
childNode.Position = **new Vector3(x: -10, y: 0, z: 0);**

*//Model at child node*
StaticModel model = childNode.CreateComponent<StaticModel>();
model.Model = ResourceCache.GetModel("Window.mdl");


But at childNode.Position I have entered a fixed offset for x of -10 that works for my "Window.mdl". But how can I calculate the offset according to the size of the model?

Regards

-------------------------

Eugene | 2021-10-29 22:05:06 UTC | #4

[quote="MtrnXf, post:3, topic:7024"]
But how can I calculate the offset according to the size of the model?
[/quote]
Well, you have access to BoundingBox of the Model.
You can deduce from there.

-------------------------

MtrnXf | 2021-11-02 14:33:11 UTC | #5

It's working. Here is the code to center the model by moving the child node half the model size to the left:

childNode.Position = new Vector3(-1f * model.BoundingBox.HalfSize.X, 0, 0);

The thing is, I have a model of a window in "x3d" format which is used in the webbrowser. It has a texture (.jpg file), you can look through the glas of the window (half transparent) and the window has an open animation. I used AssetImporter_Win64.exe to convert the "x3d" to a "mdl"  (above file). The conversion is working, but after that the "mdl" has no transparency of the glas anymore (you can't look through the glas) and the texture is corrupt. The texture is not applied to the whole frame of the window anymore, only some parts. Do you have an hints on that?

(Would be nice if Urho could import .x3d or .gltf format, but I did not find any information on that.)

Thank you. Regards

-------------------------

Modanung | 2021-11-03 11:38:08 UTC | #6

Better even would be to correct your assets using e.g. Blender.

-------------------------

