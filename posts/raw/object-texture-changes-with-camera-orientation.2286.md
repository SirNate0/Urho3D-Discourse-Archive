zedraken | 2017-01-02 01:14:31 UTC | #1

Hi there,

I am experiencing a quite strange behavior.
I have a textured object displayed in my 3D space, and depending on the camera orientation that I can change by moving around the mouse (yaw and pitch angles), sometimes the texture on my object is modified and replaced by the texture of another object which has normally nothing to deal with my first object. 
When I return to the original camera orientation, the right texture comes back.
Quite strange.
I have the same behavior with the camera zoom. The right texture is displayed (or not) depending on the camera zoom value.
Does anyone experience such issue ? 
Is it a normal behavior on Urho3D and did I forget to configure something ?

Thanks in advance for your answers that can help me understanding what is going on.

Charles

-------------------------

Lumak | 2017-01-02 01:14:31 UTC | #2

I often notice this behavior when I forget to generate tangents for models with bump map.
The -t option in the AssetImporter generates tangents.

-------------------------

zedraken | 2017-01-02 01:14:32 UTC | #3

Thanks for the tip. I will check that.
For information, under Blender, I export my object to a object.x file using the x exporter. Do you think that a specific option shall be checked (or unchecked) ?
After that step, I use "AssetImporter model..." to convert the object.x file into a object.mdl file that I directly use under Urho3D. I also request the creation of one object.txt file that contains the list of materials (list of .xml files).

Charles

-------------------------

jmiller | 2017-01-02 01:14:32 UTC | #4

Somewhat unrelated:
You are probably aware of this plugin, which has given me excellent results: [github.com/reattiva/Urho3D-Blender](https://github.com/reattiva/Urho3D-Blender)

-------------------------

zedraken | 2017-01-02 01:14:32 UTC | #5

Thanks for the link to the plugin. I successfully installed it in my Blender 2.77 and as you said, I see an Urho3D export panel (I had to carefully search for it since it is not accessible through the usual menu File->Export).
I will now give it a try. Maybe it will help me to solve my issue.

-------------------------

Lumak | 2017-01-02 01:14:32 UTC | #6

Urho3D Blender exporter is a good recommendation. It's a good tool, more versatile, and you can directly export to mdl file w/o having to export to an intermediate file then process it through AssetImporter.

-------------------------

zedraken | 2017-01-02 01:14:32 UTC | #7

Finally, using the Blender exporter, I?can get rid of the problem I had. I also noticed that it can appear again if I render the object by selecting the ambient occlusion technique.
Anyway, the exporter seems to work fine after having understood the details of the available options.
Thanks !

-------------------------

