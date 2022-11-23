TheComet | 2017-01-02 01:10:03 UTC | #1

Hey guys

I created this model in blender:

[img]http://i.imgur.com/r1SdMXg.jpg[/img]

It has a diffuse map and a normal map:

[img]http://i.imgur.com/7KGC0Q4.png[/img]

I imported it into Urho3D's editor, created a new material "Hound.xml" and used the technique "DiffNormal" from the CoreData folder. There are two things I noticed.

1) The preview in the material editor is showing the correct result, but the model remains very dark. What am I doing wrong?
2) The teeth, tongue, and eyes are white. They are submeshes, but all submeshes are UV-mapped to the same single image. Why is the body rendering with textures but the other submeshes not?

[img]http://i.imgur.com/0iRoUWq.jpg[/img]

-------------------------

Mike | 2017-01-02 01:10:03 UTC | #2

Check "Material list" in the export settings. Currently your material slots are empty.

-------------------------

1vanK | 2017-01-02 01:10:03 UTC | #3

Enable "Tangent" in exporter

-------------------------

TheComet | 2017-01-02 01:10:03 UTC | #4

Generating tangents solved my first issue, thanks! Now I just need to figure out why the teeth and tongue are still white. Any ideas?

[img]http://i.imgur.com/L59mMwE.jpg[/img]

-------------------------

1vanK | 2017-01-02 01:10:03 UTC | #5

[quote="TheComet"]Generating tangents solved my first issue, thanks! Now I just need to figure out why the teeth and tongue are still white. Any ideas?



enable "material text list" in exporter

-------------------------

TheComet | 2017-01-02 01:10:03 UTC | #6

I'm exporting as [b].dae[/b] from blender and using AssetImporter to convert to [b].mdl[/b], so that option isn't available as far as I can see.

-------------------------

1vanK | 2017-01-02 01:10:03 UTC | #7

[quote="TheComet"]I'm exporting as [b].dae[/b] from blender and using AssetImporter to convert to [b].mdl[/b], so that option isn't available as far as I can see.[/quote]

just use blender exporter [github.com/reattiva/Urho3D-Blender](https://github.com/reattiva/Urho3D-Blender)

-------------------------

TheComet | 2017-01-02 01:10:03 UTC | #8

I never got that to work. I have it installed and enabled as an AddOn (also clicked save user settings):

[img]http://i.imgur.com/aWYjEED.jpg[/img]

But it doesn't show up as an option:

[img]http://i.imgur.com/HFt61HL.jpg[/img]

-------------------------

codingmonkey | 2017-01-02 01:10:04 UTC | #9

placement for this plugin
[url=http://savepic.net/7686683.htm][img]http://savepic.net/7686683m.png[/img][/url]

-------------------------

TheComet | 2017-01-02 01:10:04 UTC | #10

Cool, thanks for the help guys!

[img]http://i.imgur.com/2Dt5hrp.jpg[/img]

-------------------------

