vivienneanthony | 2017-01-02 01:00:45 UTC | #1

Hello,
Have anyone used the Blender .fbx exporter for importing to the Urho3D editor? I'm trying to transfer between the two with the most minimum of labor.

The Steps
1. Create a blender scene or dummy scene then export in .FBX format with Z-Forward and Y-Up?
2/ Use Blender-Urho3d Exporter to transfer over models and texture
3. Reload and reset textures in the Urho3d editor

The problem I am having because of the various coordinates system being used the output from the 1st step always have some rotation in the Urho3D editor.
I don't think the output coordinates of step 1 and 2 match.
Vivienne

-------------------------

Mike | 2017-01-02 01:00:45 UTC | #2

Chris has written a detailed tutorial at [url]http://teamfriesen.com/blog/2013/09/07/finally.html[/url]  :wink:
Now, with Urho3D Blender add-on you can easily deal with orientation by setting the "Front view" option in the export panel and there is no need to export to FBX.

-------------------------

