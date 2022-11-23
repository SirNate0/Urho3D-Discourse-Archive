Liichi | 2017-02-16 23:23:52 UTC | #1

Hi, i exported some trees from blender to my scene, but i have some problems with lights.
I don't know if i did something worng during exporting or it's an Urho3D bug.
Video: https://vid.me/asiI
Anyone know how fix it?
Thanks.

-------------------------

Eugene | 2017-02-16 23:25:39 UTC | #2

I had similar problem when my Zone component was too small.

-------------------------

Liichi | 2017-02-16 23:39:28 UTC | #3

I changed the zone bounds to 1000 but it still happens :confused:

-------------------------

hdunderscore | 2017-02-16 23:54:30 UTC | #4

Does the bounding box look correct? Does changing light range change the distance of the popping effect? Are the normals exported?

Looks like there is some z-fighting when you rotated the camera, that seems strange too.

-------------------------

Liichi | 2017-02-17 01:05:34 UTC | #5

Does the bounding box look correct? Yes
Does changing light range change the distance of the popping effect? Yes
Are the normals exported? Yes i think, i follow the same steps to export all models of scene.
I noticed that if I use Diff.xml instead of VegetationDiff.xml the light works correctly.
It seems a VegetationDiff.xml bug. :/

-------------------------

Liichi | 2017-02-17 01:19:51 UTC | #6

I found the problem, I was using a material only with the technique VegetationDiff.xml, when i add a new technique Diff.xml to the material the problem disappeared. :slight_smile:
It's an issue or an noob error?

-------------------------

1vanK | 2017-02-17 07:18:21 UTC | #7

Pls show your material (xml file)

-------------------------

szamq | 2017-02-17 08:19:34 UTC | #8

What are your setup of near and far in camera? It looks like you set some large amount like 1000000 to far parameter.

Edit: Ah ok you already solved the issue:)

-------------------------

Liichi | 2017-02-17 16:28:29 UTC | #9

[quote="1vanK, post:7, topic:2800, full:true"]
Pls show your material (xml file)
[/quote]

http://pastebin.com/t8KmqBgV

Working material:
http://pastebin.com/JahVsMYm

-------------------------

1vanK | 2017-02-17 17:52:40 UTC | #10

material should contain only one technique with same lod

EDIT: https://urho3d.github.io/documentation/HEAD/_materials.html

-------------------------

Liichi | 2017-02-17 18:19:41 UTC | #11

Apparently, the second material only worked because Diff.xml was overwriting VegetationDiff.xml
Is there something wrong with the first material? (which only contains VegetationDiff.xml)

-------------------------

1vanK | 2017-02-17 20:34:01 UTC | #12

Vegetation should animate vertices of model, but I do not see it on video. So need more info about exporting settings

-------------------------

Liichi | 2017-02-19 15:53:57 UTC | #13

I realized that VegetationUnlit.xml works :confused: 
I tried to export using .blend, .dae, .fbx formats but none worked.
I also tried using the urho plugin but i get the same problem.

-------------------------

hdunderscore | 2017-02-20 01:42:07 UTC | #14

Well I think I have spotted a typo or error in vegetation shader. Simple test, turn off dynamic instancing-- does the issue still occur?

-------------------------

Liichi | 2017-02-19 23:29:42 UTC | #15

[quote="hdunderscore, post:14, topic:2800, full:true"]
Well I think I have spotted a typo or error in vegetation shader. Simple test, turn off dynamic instancing-- does the issue still occur?
[/quote]

No, everything works well (:

-------------------------

hdunderscore | 2017-02-20 00:46:08 UTC | #16

Offending line is: 
https://github.com/urho3d/Urho3D/blob/master/bin/CoreData/Shaders/HLSL/Vegetation.hlsl#L98

if anyone wants to confirm. Replacing cModel with modelMatrix seems to work.

-------------------------

Liichi | 2017-02-21 01:46:53 UTC | #17

Works for me, ty :D
I think you should commit.

-------------------------

