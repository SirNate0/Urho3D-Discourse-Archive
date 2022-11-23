smellymumbler | 2017-12-13 20:49:01 UTC | #1

Hey everyone! I've been trying to work with Urho's editor for a while now, and then i tried to write my own editor. I've realized that all this can be great for learning, but I really want to finish at least one project before i go back to trying to improve my own editor and learn more about 3D geometry manipulation.

In order to solve that, I've decided to build all the game levels and scenes with Blender, then export to Urho. Unfortunately, i have some questions about the way Urho handles prefabs and geometry instancing. Take this Unity plugin for example:

https://www.assetstore.unity3d.com/en/#!/content/100772

It bundles similar objects from the Blender scene into one and optimizes the scene in Unity. Is it possible to do the same with Urho? I have a bunch of models in Blender that i use as modules to build up my levels. Same model for wall, pillar, etc. Kinda like a tileset. But when i export my scene using the existing Urho export tools, i get a bunch of models and many drawcalls.

-------------------------

SirNate0 | 2017-12-13 22:13:51 UTC | #2

I think the group instancing stuff in the newer version of the Blender exporter might be asking the lines of what you want (see [here](https://discourse.urho3d.io/t/importing-complicated-scene-into-urho/3291/47))

-------------------------

