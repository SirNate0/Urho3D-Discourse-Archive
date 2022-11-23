GodMan | 2017-11-21 23:48:51 UTC | #1

I have not been able to get my lightmapping material to work I suspect that AssetImporter may be destroying the 2nd uv set would someone mind uploading a .mdl file that they know has 2 texture coordinates.

-------------------------

Dave82 | 2017-11-20 22:16:11 UTC | #2

Just tell me what you exactly need and i will create it for you,A plane floor with few boxes on it is enough ?

-------------------------

GodMan | 2017-11-20 22:37:45 UTC | #3

That's fine or just a plane, that's what I'm doing now. The lightmap should show but nothing. So I need to test if Asset Importer is messing up the mesh.

-------------------------

rasteron | 2017-11-21 00:22:43 UTC | #4

For lightmaps or 2nd UV, you should try Blender exporter. Here's a sample blender file link ready for export:

https://discourse.urho3d.io/t/blender-simple-lightmap-export/3065

-------------------------

GodMan | 2017-11-21 00:43:08 UTC | #5

People telling users to use Blender makes no sense to me. 3ds max and Maya are much better and more well known. I have many years experience with 3ds max I'm not switching to blender just to export a mesh. Even Irrlicht supported common formats. This is what happens when you insist on using a custom model format and reinvent the wheel.

I'm just trying to make sure Asset Importer is not causing the issue here. So far I ran into some animation issues and fixed them when using Asset Importer I will be posting a tutorial for 3ds max users soon. 

I just need a .mdl file that has both UV coordinates for me to test with it does not matter what you guys exported it with.
Maybe a  lightmap material file also so I can make sure my material file is correct as I did not see any examples on the forums with any material files.

Thanks

-------------------------

stark7 | 2017-11-21 02:05:31 UTC | #6

[quote="GodMan, post:5, topic:3763"]
3ds max and Maya are much better and more well known. I have many years experience with 3ds max I’m not switching to blender just to export a mesh.
[/quote]

It will be worth it if you added blender under your belt.

-------------------------

Dave82 | 2017-11-21 17:58:17 UTC | #7

Well i have some bad news...It seems that AssetImporter just doesn't like meshes with 2 uv's... I tried .x , 3ds , fbx and even ogre mesh format but Assimp just ignores the 2nd uv set.l.I'm affraid i can't help you until i write a direct mdl exporter for 3ds max.

The weird thing i was able to export x with 2 uv sets and convert it to mdl.The lightmapped model in the post below is a panda .x file converted to mdl using Assimp and it worked perfectly before (3ds max 9 with Urho 1.4)
https://discourse.urho3d.io/t/problems-with-lightmaps-dynamic-lights/1073/9?u=dave82

EDIT : 
I can confirm that even if i use my lightmapped models (my own format) and export them to *obj the second UV map is lost.

-------------------------

GodMan | 2017-11-21 17:59:17 UTC | #8

I've downloaded 1.4 and built everything. I might try to convert my static models to .mdl format using 1.4 and see if this works.

-------------------------

Lumak | 2017-11-21 18:55:48 UTC | #9

@Dave82, I'm using 1.7 release and have 2nd uv working. I'd like to get others to also verify that works.

-------------------------

Eugene | 2017-11-21 19:07:34 UTC | #10

[quote="Dave82, post:7, topic:3763"]
I tried .x , 3ds , fbx and even ogre mesh format but Assimp just ignores the 2nd uv set
[/quote]

Please report an issue on GitHub tracker and attach model to test.

-------------------------

GodMan | 2017-11-21 19:19:23 UTC | #11

@Lumak Are you exporting with 3ds max. If so I've exported the static mesh from 3ds max 2015 and convert it with Asset Importer to .mdl and everything is okay except when I try to use a lightmap on UV channel 2 the lightmap never shows so I assume that the conversion process in Asset Importer is messing with the 2nd UV channel. I reimported my original fbx file in max to double check it and everything was okay with the model.

-------------------------

Lumak | 2017-11-21 23:48:36 UTC | #12

I'm using Maya LT 2016, and because of that I rely solely on assetimporter.

edit: I should mention that I work with .fbx files.
edit2: This might be more critical: choose export option to **FBX 2013**

-------------------------

GodMan | 2017-11-21 22:34:49 UTC | #13

I'll try what you suggest.

-------------------------

GodMan | 2017-11-21 22:53:11 UTC | #14

I'd like to report that everything is working fine now. I tried what @Lumak said and changed my .fbx exporter in 3ds max to 2013 instead of 2014 and everything worked fine my lightmap showed up this time so thanks great suggestion.

Oddly though I got no errors in the output from AssetImporter when using the 2014 exporter. 

Now I can go and try to add my directionl lightmap shader to urho3d that I made for Irrlicht 2 years ago.


Thanks for all the suggestions guys.

-------------------------

Lumak | 2017-11-21 23:05:58 UTC | #15

Glad it's solved. I'm curious, did you use 1.7 release or 1.4?

-------------------------

Dave82 | 2017-11-21 23:32:10 UTC | #16

@Eugene It won't be necessary since i'm still using 1.5

-------------------------

GodMan | 2017-11-22 00:02:38 UTC | #17

I'm using 1.7 but not the github master source I could not build the download from github so I downloaded the 1.7 zip from the website and everything built fine.

-------------------------

