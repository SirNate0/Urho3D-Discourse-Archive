akilarandil | 2017-02-18 16:52:00 UTC | #1

Hi all,

I Want t convert an FBX file to MDL to use it on my Urho app. I used two techniques.

1. Used the plugin that is provided to be used on Blender
2. Exported the file as SMD and created a QC file and compiled it to MDL using Crowbar.

When running the app,
the first one gave an error saying the model doesn't have any bones.
the second one gave an error saying the mdl file is not supported.

I have a demo at the end of this week and I would really appreciate if anyone can help me with this.

-------------------------

1vanK | 2017-02-18 19:16:01 UTC | #2

1) show your export settings
2) try AssetImporter instead Blender

-------------------------

hdunderscore | 2017-02-18 21:56:17 UTC | #3

It's important to point out that Urhos mdl format is not the well known mdl format from some other engine. There is a Urho3D blender export plugin, available here: 
https://github.com/reattiva/Urho3D-Blender

or as mentioned, you can use Urho3Ds AssetImporter (either directly by reading the following documentation or importing via the editor).
https://urho3d.github.io/documentation/HEAD/_tools.html

-------------------------

akilarandil | 2017-02-19 04:42:54 UTC | #4

I used AssetImporter as well but it said that it doesn't recognize the file format MDL to be converted

-------------------------

hdunderscore | 2017-02-19 06:01:35 UTC | #5

Try converting your original fbx file instead.

-------------------------

akilarandil | 2017-02-20 04:06:50 UTC | #6

assimp export: no output format specified and I failed to guess it

This is all i'm getting when using it

-------------------------

akilarandil | 2017-02-20 04:09:12 UTC | #7

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/98d3fd3e30f38ff56c8faf62bb48aa6353d2cb8e.png" width="690" height="400">

-------------------------

akilarandil | 2017-02-20 04:09:45 UTC | #8

AssertImporter would give the following error.

assimp export: no output format specified and I failed to guess it

-------------------------

1vanK | 2017-02-20 04:13:45 UTC | #9

> the first one gave an error saying the model doesn't have any bones.

enable skeletons in exports settings :cold_sweat:

-------------------------

akilarandil | 2017-02-20 04:19:21 UTC | #10

What are the sub settings i should use?

1. Derigify
2. Only deform bones
3. Only visible bones
4. Use skinning for parent bones

-------------------------

1vanK | 2017-02-20 04:21:13 UTC | #11

Obviously, depending on the scene

-------------------------

1vanK | 2017-02-20 04:30:50 UTC | #12

Pls read help: https://github.com/reattiva/Urho3D-Blender/blob/master/guide.txt
Also you can move mouse to elements in Blender and read tooltips

-------------------------

akilarandil | 2017-02-20 04:44:57 UTC | #13

After exporting I would get this

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/13ae83d7a69d7f780eaf3097af9de38b41afe658.PNG" width="506" height="500">

-------------------------

hdunderscore | 2017-02-20 04:59:59 UTC | #14

That's good progress. Check the overwrite option, and the file should export. Those warnings probably indicate an issue you may need to subsequently fix.

-------------------------

1vanK | 2017-02-20 05:08:55 UTC | #15

Apply - Ctrl+A
Origin - button on left panel
Derigify found 0 bones - may be you do NOT USE rigify?
File already exists - enable file overwrite

-------------------------

akilarandil | 2017-02-20 05:50:24 UTC | #16

Okay so It exported without any errors now. When accessing the bones in Visual Studio i get this error.
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/52fc7baf9779f22088041551070bf985a24ff113.png" width="689" height="256">


This is the converted MDL file
https://drive.google.com/file/d/0B6T_CCmOec0FTjVhbWN2Nmd1ZzQ/view?usp=sharing

This is the FBX file.
https://drive.google.com/file/d/0B6T_CCmOec0Fd216aFhUNzJLeVU/view?usp=sharing

-------------------------

akilarandil | 2017-02-20 05:48:41 UTC | #17

This is the export settings for the conversion. 
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/1db52be2e9da81b57c68343d8a16b00c77347c61.png" width="690" height="388">

-------------------------

1vanK | 2017-02-20 05:57:16 UTC | #18

bone not founded. It is all that can be said on the basis of the provided information

-------------------------

akilarandil | 2017-02-20 13:23:22 UTC | #19

I fixed it. Had problems with the naming conventions.It's working now, Sorry for the inconvenience caused. And thank you very much for the support. Urho3D FTW!

-------------------------

