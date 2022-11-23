vivienneanthony | 2017-01-02 00:59:58 UTC | #1

Hello,

Please don't mind any typos or incorrect terminology.

1) Terrain Textures

[[b]b]Question[/b]
Is it possible to do a plane texturing that still uses the tilemap for sizing. Then textures are placed randomly in a location and rotation in the weighted areas. So textures don't look repeated and more nature.
[/b]
2) Rendering Quality using Nvidia(Cuda) or Amd
Is there a way to implement a feature to detect video card being a nvidia(cuda), amd(not sure of the format) and i'm assuming directx for win/pc and opengl for linux. I'm not sure about Macintosh. So the graphics can be pushed even higher

3) Muiltiple resource path in the Editor

4) Some sort of database connectivity utilizing SQLITE or any connection of ODBC
Meaning instead of loading individual MDL it can be stored in a db file like "models" or "textures"

Just questions.

Vivienne

PS. I highlighted the most important one.

-------------------------

friesencr | 2017-01-02 00:59:58 UTC | #2

Multiple resource paths are possible in several ways.

The editor uses the Urho3DPlayer which has commandline configuration of resource paths
[code]
-p <paths>   Resource path(s) to use, separated by semicolons
[/code]
[urho3d.github.io/documentation/a00002.html](http://urho3d.github.io/documentation/a00002.html)

Opening a scene file will add a temporary resource path based on the location of the scene file.  It assumes the urho convention (assuming the path is in the Scene folder) where it will add a directory about the scene file as a resource path.

You can also symlink folders in the Extra folder.  Every folder in the Extra folder will get automatically added as a resource folder.

-------------------------

vivienneanthony | 2017-01-02 00:59:59 UTC | #3

[quote="friesencr"]Multiple resource paths are possible in several ways.

The editor uses the Urho3DPlayer which has commandline configuration of resource paths
[code]
-p <paths>   Resource path(s) to use, separated by semicolons
[/code]
[urho3d.github.io/documentation/a00002.html](http://urho3d.github.io/documentation/a00002.html)

Opening a scene file will add a temporary resource path based on the location of the scene file.  It assumes the urho convention (assuming the path is in the Scene folder) where it will add a directory about the scene file as a resource path.

You can also symlink folders in the Extra folder.  Every folder in the Extra folder will get automatically added as a resource folder.[/quote]

I figured that. I'll check it out.

I'm just figuring out creating a not-movable but collidable wall. I setup the mass to be 100 but i think it might need to be much higher. (Actually. Fixed. I went through the documentation).

-------------------------

