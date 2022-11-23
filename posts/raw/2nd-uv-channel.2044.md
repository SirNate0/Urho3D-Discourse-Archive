Ecco | 2017-01-02 01:12:31 UTC | #1

..hi guys..im new here, so apart from my greetings to everyone, i have also some question, if you dont mind me asking..i went trough all samples included with Urho3d, and im very much impressed how easy is to use system (VS2010)..lighting/material system seems to be very nice to work with..however, i noticed that, there is no samples about use of 2nd uv channel or more, for sake of lightmap or GI map (almost all modern games uses this with dynamic lights)..having said this, is there any tutorial, or sample which introduces mix between baked and dynamic lighting ??
Thank you very much..

-------------------------

rasteron | 2017-01-02 01:12:31 UTC | #2

Hey Ecco, Welcome to the forums :slight_smile:

This question has been a FAQ and already been discussed on other threads. If you're familiar with Blender then you can do this with just a few simple steps:

1) Setup your already lightmapped scene so that the model/mesh contains two (2) UV maps with the 2nd UV named _UV2
2) Download and Install [url=https://github.com/reattiva/Urho3D-Blender]reattiva's Blender exporte[/url]r and toggle the section where it says UV2. 
3) Export and maybe do some adjustments in Urho3D Editor for checking.

Snippet from the exporter guide

[quote]
To export UV you need an UV map, you can see the list in the Data page of the current selected object.
The Urho MDL format supports two sets of UV coordinates. You can specify what maps to use by appending "_UV1" or
"_UV2" to the layer name. These suffixes can be used together but also alone, if they are missing the first used
layer will be chosen.
If the exporter reports some "Invalid UV" this means that some triangles of the mesh are mapped in the UV map to
triangles with an area null or too small. You need to increase the area in the UV map, you can set the option
'Select vertices with errors' to find these triangles.[/quote]

Hope that helps

-------------------------

Ecco | 2017-01-02 01:12:31 UTC | #3

..thank you very much..I am not using Blender, but 3dsmax..creation of lightmap in 3dsmax is not a problem..so, as I can see, i have to be sure that naming convention for UV layers must be set on specific way in order to work? I will take a look and play and come back if there are issues.. :slight_smile:

-------------------------

rasteron | 2017-01-02 01:12:31 UTC | #4

Sure thing. Yes, but I'm not sure exporting from Max is a complete process. I can only find the OgreExporter here: [github.com/urho3d/Urho3D/tree/m ... reImporter](https://github.com/urho3d/Urho3D/tree/master/Source/Tools/OgreImporter).

I don't know if this tool retains UV2 mapping but the sure way is to export as FBX (2013) to Blender and use reattiva's exporter.

-------------------------

Dave82 | 2017-01-02 01:12:32 UTC | #5

[quote="Ecco"]..hi guys..im new here, so apart from my greetings to everyone, i have also some question, if you dont mind me asking..i went trough all samples included with Urho3d, and im very much impressed how easy is to use system (VS2010)..lighting/material system seems to be very nice to work with..however, i noticed that, there is no samples about use of 2nd uv channel or more, for sake of lightmap or GI map (almost all modern games uses this with dynamic lights)..having said this, is there any tutorial, or sample which introduces mix between baked and dynamic lighting ??
Thank you very much..[/quote]


Hi ! The easiest way is download the Panda X exporter and export your models in .x format.I tested it with Urho and works fine.
The other solution is (Longer but more powerful) is to write your own exporter in maxscript.A basic exporter can be written in no time.Just follow the structure of Urho's mdl format.
[url]http://urho3d.github.io/documentation/1.4/_file_formats.html[/url]

-------------------------

