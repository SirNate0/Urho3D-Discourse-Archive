Eugene | 2017-01-02 01:15:43 UTC | #1

I'm trying to import this model
[3dwarehouse.sketchup.com/model. ... 994630e5c6](https://3dwarehouse.sketchup.com/model.html?id=69483ef386b6645fd12d2c994630e5c6)
with command
[code]AssetImporter.exe scene model.dae Scene.xml[/code]
But all materials are mixed up.
AI also somewhy cannot find textures.
What's wrong with me/model/AI?
Can somebody experienced help me?

Thank you.

-------------------------

Enhex | 2017-01-02 01:15:43 UTC | #2

Not sure exactly what's your problem, but if you want to use several materials for a single model, Blender's Urho exporter has an option to create materials list file that automatically set them up in the correct order when loaded with Urho.

-------------------------

