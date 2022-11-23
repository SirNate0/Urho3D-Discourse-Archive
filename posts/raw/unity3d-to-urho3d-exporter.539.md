arealperson | 2017-01-02 01:01:15 UTC | #1

Hi,

I'm looking for the "Unity3D to Urho3D exporter" as shown on the Urho3D main page.
Is this available yet ? I cant seem to find it.

I would like to export some of my Unity scenes to start converting them to Urho3D.

Thanks,

-------------------------

lexx | 2017-01-02 01:01:15 UTC | #2

I think he made it to his firm, so it is not open source project and I dont think it is not available anywhere. 
But somebody correct if im wrong.

But, check this link:
[forum.unity3d.com/threads/export ... er.122907/](http://forum.unity3d.com/threads/exporting-from-unity-to-blender.122907/)

Blender can export .fbx file which you can convert to urho3d format.
(maybe converter converts .obj files too, I dont remember)
And converter is urho3d_dir/Bin/AssetImporter.exe

AssetImporter:
  model  parameter; from dae/fbx/etc  to model, no instances, only 1 model file
  scene  parameter; creates  .scene file and multiple .mdl files

-------------------------

Stinkfist | 2017-01-02 01:01:15 UTC | #3

The description of the demo video ( [youtube.com/watch?v=m3ehQwfbjGg](https://www.youtube.com/watch?v=m3ehQwfbjGg) ) at least states that the guy was working on an open source game engine. Who knows, maybe he/the company publishes this when it's more finished?

-------------------------

jenge | 2017-01-02 01:01:15 UTC | #4

Hello,

I was writing this stuff last year for a game project we were working on.  Urho3D was lacking 2D at  the time and thus the cocos2d-x integration.  The exporter was designed for some preprocess tooling and isn't general purpose.

- Josh

-------------------------

