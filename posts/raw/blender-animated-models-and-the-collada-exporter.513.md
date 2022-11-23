rogerdv | 2017-01-02 01:01:01 UTC | #1

During my tests with Torque3D, I found that Blender DAE exporter has a bug: it only exports the active animation (or action, dont know the exact term). The workaround was to export the same model several times, one for each animation, and use Shape editor to configure the final mesh and its animations in Torque. Is there some similar approach in Urho to solve this problem?

-------------------------

codingmonkey | 2017-01-02 01:01:01 UTC | #2

have you pressed the button  - F (fake_user) in Action editor for each animation ? this means  - "save this datablock if even it has no users" 
by default at the same time only one animation have a user as armature.
I had a similar problem when importing animated character as a proxy object from other blend file, i guess that all animations should be marked as - "fake user" before it can be saved or exported )

-------------------------

rogerdv | 2017-01-02 01:01:01 UTC | #3

Got a similar reply in BlenderArtists forum, but never found a way to find the animations in the panel. I know they are there, because when I used Ogre exporter it generated correctly all the sequences, but cant find them. Anyway, at least now I know that we have a solution.

-------------------------

rogerdv | 2017-01-02 01:01:01 UTC | #4

Got it, one disadvantage of small dispalys is that you cant see many things in Blender that are hidden beyoin screen borders. but now the importer cant read the file:

[code]Reading file /home/roger/projects/urho-test/Bin/Data/human.dae
Could not open or parse input file /home/roger/projects/urho-test/Bin/Data/human.dae
[/code]

-------------------------

cadaver | 2017-01-02 01:01:01 UTC | #5

You can try verbose mode logging with the -v switch in AssetImporter. It's an Assimp bug, likely.

-------------------------

rogerdv | 2017-01-02 01:01:01 UTC | #6

Well, it is totally unrelated to animations:
[code]Reading file /home/roger/projects/urho-test/Bin/Data/human.dae
Info,  T0: Load /home/roger/projects/urho-test/Bin/Data/human.dae
Debug, T0: Assimp 3.1.131947607 amd64 gcc noboost singlethreaded
Info,  T0: Found a matching importer for this file format
Info,  T0: Import root directory is '/home/roger/projects/urho-test/Bin/Data/'
Debug, T0: Collada schema version is 1.4.n
Warn,  T0: Collada: No material specified for subgroup <> in geometry <armature_HumanBody_002-skin>.
Error, T0: Collada: Unable to resolve effect texture entry "human_jpg_001-sampler", ended up at ID "human_jpg_001".
Could not open or parse input file /home/roger/projects/urho-test/Bin/Data/human.dae[/code]

-------------------------

codingmonkey | 2017-01-02 01:01:01 UTC | #7

And if you take your file (human.dae) and open it in blender, and then exporting with this plugin [github.com/reattiva/Urho3D-Blender](https://github.com/reattiva/Urho3D-Blender)

-------------------------

rogerdv | 2017-01-02 01:01:01 UTC | #8

Exporter works, but geometry is deformed.
[url=http://s249.photobucket.com/user/rogerdv/media/Screenshot_Fri_Oct_31_13_44_24_2014.png.html][img]http://i249.photobucket.com/albums/gg237/rogerdv/Screenshot_Fri_Oct_31_13_44_24_2014.png[/img][/url]

-------------------------

codingmonkey | 2017-01-02 01:01:01 UTC | #9

it looks as if not all vertices have correct weight or not attached to bones

-------------------------

friesencr | 2017-01-02 01:01:01 UTC | #10

This looks like blender's crappy weight issue.  They fixed fbx but I think dae is still buggered.  My suggestion is to try fbx and see if it fixes your issue.

-------------------------

rogerdv | 2017-01-02 01:01:02 UTC | #11

I have tested the model with Unity in fbx format, using Blender 2.71: it imports perfectly. Does the assimp vbersion included in Urho already supports fbx format? Will try that.

-------------------------

rogerdv | 2017-01-02 01:01:02 UTC | #12

Negative for fbx, binary version is too recent for assimp, ascii version doesnt loads.

-------------------------

friesencr | 2017-01-02 01:01:02 UTC | #13

Are you running Urho3d master or stable?

-------------------------

rogerdv | 2017-01-02 01:01:02 UTC | #14

Im running master, I update every day from github.

-------------------------

codingmonkey | 2017-01-02 01:01:03 UTC | #15

[quote]Exporter works, but geometry is deformed.[/quote]
ok, today i am try to export my simple character with two action and it's works fine. 
and to solve your problem maybe this helps
 
[github.com/reattiva/Urho3D-Blen ... /guide.txt](https://github.com/reattiva/Urho3D-Blender/blob/master/guide.txt)
[quote]144  Weights 
145 ========= 
146 Issues with weights ('element mask' errors reported in the List of errors when 'Select vertices with errors' is enabled) 
147 might show up when: 
148   - some vertices are not weighted (skinning issue) 
149   Fix: redo the skinning for the vertices at fault 
150   - 'Vertex Groups' and bones are mismatching. This can occur when: 
151       - a bone has been deleted and its 'Vertex Group' has not been reassigned to remaining bones. This is a skinning issue. 
152       Fix: reassign 'Vertex Group' (in Properties > Object Data), manually or using Set Parent To Armature Deform With Automatic Weight. 
153       - a vertex is weighted exclusively to bones that have been removed from export (using one of the 'Skeletons' suboptions). 
154       Fix: 
155           - choose another 'Skeletons' suboption or modify Armature layer visibility to include more bones at export. 
156           - reassign 'Vertex Group' (in Properties > Object Data) so that each vertex is weighted to at least one remaining bone. 
 [/quote]

-------------------------

friesencr | 2017-01-02 01:01:03 UTC | #16

There is a normal checklist, which I have partially forgotten because I haven?t been working on my game in some time, that I try to follow.  No ngons, all quads,  no more than 3 weights / bone.

-------------------------

