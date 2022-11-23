najak3d | 2020-09-25 02:07:10 UTC | #1

I'm new to Urho3D.  I am trying to grab some sample models from the internet, and then using AssetImporter to bring them into the Sample project for rendering.

My stopper is this -- the materials that reference a texture are referencing them in the base "Textures/" folder.   This is messy.  Just as "NinjaSnowWar" sample model has it's textures and materials all stored in  like-named subfolder, that's how I want my Imports to be created.

For example, I have imported a "Falcon.mdl", which has a dozen Materials and Textures.  I want the materials to be located under "Materials/Falcon/{materialname}.xml"  and Textures to be located under "Textures/Falcon/{texturename}.jpg"

I do not see any options for AssetImporter which permit me to force this type of folder structure.  What to do?

-------------------------

Modanung | 2020-09-25 07:35:10 UTC | #2

1: You put it ina...

[![](https://upload.wikimedia.org/wikipedia/commons/0/0c/Blender_logo_no_text.svg)](https://www.blender.org/)

-------------------------

najak3d | 2020-09-25 14:00:59 UTC | #3

Thanks for the response Modanung.  Thanks for the clue; I see we have an Urho3D exporter for Blender, which I assume eliminates our need to use AssetImporter. 

https://github.com/reattiva/Urho3D-Blender/tree/2_80


So the recommended model workflow is this: (???)
1. Import model into Blender.
2. Export from Blender using the latest Urho exporter, direct to MDL format.

And does this method permit you to put put the MDL's Material references into subfolders?

-------------------------

najak3d | 2020-09-25 15:33:03 UTC | #4

Moving forward, I've downloaded Blender 2.9 just now, and installed the Blender-Urho plugin, and enabled it.   So far, so good.

But now I can't see how to actually use it.  I've read the tutorial, which is for Blender 2.7.  I can't find the 'Free Style' area as mentioned in this tutorial.  I've spent 15 minutes looking for "the render tab in the Free Style area", with no luck.   If I try "File => Export", Urho is not listed as an option.

https://urho3d.fandom.com/wiki/Blender_to_Urho3D_Guide?file=Blender_model_in_urho3d-0.jpg

I do see how the Urho Exporter permits you to set the "Default Materials subpath" which defaults to "Materials".   So I assume (once I get this working) that for each model I want to export, I'll need to modify these default subpaths to be "Materials/{ModelName}"... and do the same for Textures as well.

But I can't do anything yet, because I can't find the method for doing the "Export".  Got hints?

![image|690x396](upload://amyXWx6qMxZHkYmwGRbhgtjyuQc.png)

-------------------------

najak3d | 2020-09-25 16:38:46 UTC | #5

So I downloaded Blender 2.79b, instead.  And here I installed the Urho Exporter, and it reports a syntax error (shown below).  So I'm stuck here again.

![image|690x321](upload://99WVXSUzbdnCv0JAzwxq7erGmkz.png) 

The Blender site gives you a choice between 2.79 or 2.90.   Version 2.80 is not an option for download.

I'm stuck.

-------------------------

SirNate0 | 2020-09-25 18:43:16 UTC | #6

There are other download options, I think, they're just a bit harder to get to. For example: https://www.blender.org/download/releases/2-83/
Or this link, which is actually to download that version) https://www.blender.org/download/lts/

In regards to Blender 2.90, it's possible the 2.8 version of the exporter would work with it, though I've certainly not tried it so I couldn't really say. I also can't guarantee that the exporter works with the 2.83-lts version, as I don't think I have that one installed. Perhaps someone else can say more definitively.

-------------------------

najak3d | 2020-09-25 20:42:34 UTC | #7

SirNate - thank you.  OK done.  I now have 2.83.6 installed, and the Urho Exporter installed just fine (same as it did for 2.90).  The problem now is that I cannot locate the UI option for Exporting a model.

How do I find that option in Blender?   Here's my screenshot.  Where is this elusive "Export to Urho" option?

![image|657x500](upload://kklS8eWORBUSZpDJaJYqUgftlG5.jpeg)

-------------------------

SirNate0 | 2020-09-26 00:43:09 UTC | #8

It should be under the Render tab (which I also find a bit counter-intuitive, though I don't really have a better suggestion).![image|437x500](upload://oQ9nwzoe2MD4vzZ2ueIbngLG1x5.png)

-------------------------

najak3d | 2020-09-26 03:49:16 UTC | #9

Perfect!  Thanks for the screenshot, I found it.  Now I can export to Urho format!  Hooray.

New show-stopper now --  AssetImporter created from this ONE MDL file output, with a half-dozen materials.  The issue with AssetImporter, is that it forced all of those materials to be in the "Materials/" subfolder, which is a no-go for us.  

And so we turned to Blender to fix that issue.  But when I do the export via Blender, I end up with a half-dozen MDL files and NO Materials!   This is even worse.

Is there some magic statement that I can use to ensure this combination of parts is Exported as a single MDL, with textures?   (same as the AssetImporter did for me)

Note, I used the "Selection Box" technique to select all parts, and then tapped "Export Urho" -- which then resulted in 6 MDL files, instead of 1.

![image|644x187](upload://lIZE2OYn7SGsCb96T52d3PfArh7.png)

What we want is : One MDL, and Materials/Textures that are in associated Subfolders called "{modelName}/".

-------------------------

SirNate0 | 2020-09-26 08:12:03 UTC | #10

In regards to the one model, I'm pretty sure you can just join/merge them in blender before exploring (if memory serves it's some modifier key+J when all of them are selected, though there may have been more steps required). In regards to the materials there are some issues with the 2.8 version of the exporter and materials. I haven't worked out exactly how to make it work yet (it worked fine for me in 2.7 blender, but I haven't done enough with 2.8 to worry about it yet), though perhaps some of the others have a way to do it.

Honestly, though, I think it could be simpler for you to just modify the Asset Importer source to have it look in subdirectories created based on some parameter you add. It did sound like file names were the only issue you had. Though I've only used the blender exporter, so maybe it's harder to do that than I'm imagining...

-------------------------

najak3d | 2020-09-26 08:15:20 UTC | #11

For now, we're probably just going to use the AssetImporter, as you suggested, and we're setting the Materials manually in code, run-time.  It's awkward, but will get the job done.

I would have expected AssetImporter for models to use the "{modelName}/" subdirectory by default, so that you don't end up with naming conflicts and a muddled mess of so many files in a single folder.

We're not at the point of planning to edit the AssetImporter/etc.  We just want to be users of this tool for now.  We are C# programmers, not C++, and are using UrhoSharp for our application.

-------------------------

