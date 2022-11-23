wicash | 2019-05-16 17:17:41 UTC | #1

Hello.
I'm wondering how I can create models and textures and import them. So far I tried importing the .mdl files from urho3D to edit them and export them back into urho3D, but I can't open them with Blender or another program.

-------------------------

JTippetts | 2019-05-16 17:40:54 UTC | #2

It's a one-way pipeline, unless you want to write a reverse-exporter. Create the model in Blender, export it to .mdl for use in Urho3D.

-------------------------

Leith | 2019-05-17 06:27:17 UTC | #3

Hi wicash, Welcome to the community! :slight_smile:

Urho3D has a tool called AssetImporter which you can use to convert FBX files into MDL files.
You can use it to import Scenes, Models and Animations from FBX into Urho3D .xml, .mdl and .ani format. It can also import materials and textures.

This means you can create your 3D assets in any modelling application that can export to FBX.
But as mentioned, this is a one-way pipeline, so be careful to keep the FBX input files, and/or the native files from the modelling app, for future editing and re-exporting.

It may take a few attempts to work out which "switches" you need to provide when you first start using AssetImporter, depending on things like the lighting requirements of your scene, but it's not too difficult to work out, and there's lots of help available here.

-------------------------

wicash | 2019-05-17 10:01:19 UTC | #4

Thanks for the help guys.
So let's say I create a scene and a few models and export them correctly. What approach should I take to make a "game level" out of it? Is the urho3D Editor a good choice to assemble a level?

-------------------------

Leith | 2019-05-17 11:18:16 UTC | #5

I would say yes, even though I don't use it.

I currently tend to create my scenes in code, and immediately save them to XML format. I can then choose to edit the XML files in the editor, or some other editor, and/or reload those XML files instead of creating the scene in code. It's a chicken and egg thing.

-------------------------

Modanung | 2019-05-17 14:28:10 UTC | #6

For exporting models from Blender I'd use [this exporter](https://github.com/reattiva/Urho3D-Blender).

Also, welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

jmiller | 2019-05-17 15:22:53 UTC | #7

Welcome!

There have been a few editors and content generators posted in  https://discourse.urho3d.io/c/showcase/code-exchange and elsewhere in the forum and more can be added to https://github.com/urho3d/Urho3D/wiki somewhere.

Two I know:
  https://discourse.urho3d.io/t/building-construction-edddy-a-block-based-map-editor-written-in-c/2486

  http://discourse.urho3d.io/t/terrain-editor/765

I use text editor a lot.
[Urho3D-Blender](https://github.com/reattiva/Urho3D-Blender) works well for me - models, detailed scene.
I use Urho editor sometimes to preview things and create prefabs.

-------------------------

wicash | 2019-05-17 20:24:44 UTC | #8

Thanks guys. :grin:

I've stumbled upon Edddy before. I'm not sure if this is the right place to ask this, but how can I install it? I got the files from [https://gitlab.com/luckeyproductions/Edddy](https://gitlab.com/luckeyproductions/Edddy) but I have no idea how to actually build the editor.

-------------------------

Modanung | 2019-05-17 20:33:41 UTC | #9

I wouldn't call Edddy quite production-ready yet, it's missing several essential features. :roll_eyes:
But if you'd like to compile it anyway, the easiest way would be to use QtCreator to open the PRO-file after adding Urho3D (pasted or sym-linked) to your Edddy folder.

-------------------------

wicash | 2019-05-18 14:13:53 UTC | #10

Thanks for the help. I checked out Edddy and JTippetts Terrain Editor. 
I have a few more things I'd like to ask:

1.)  How do I get anything to show up in U3D Terrain Editor at all? :confounded: Everything I see is this: [https://i.imgur.com/qWPJqDV.png](https://i.imgur.com/qWPJqDV.png)

2.) When I want to load terrain like in the mini vehicle game or the water example, do I always need a height map?

3.) When I create a landscape/terrain in Blender, what is the best way to get it into urho3D? Do I need to create a height map and export the textures individually?

-------------------------

jmiller | 2019-05-18 16:15:12 UTC | #11

2.) It seems that without a height map, Terrain will use all zero heights. I admit I have not tested. ;)
  https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/Terrain.cpp#L895

3.) Many terrain editors will output a height map, and some, a weight map for blending the actual textures.. roughly as described in  https://wikipedia.org/wiki/Texture_splatting and https://wikipedia.org/wiki/Heightmap

Here some have posted ways to get a heightmap, and I link to one method generating from a mesh in Blender.
https://discourse.urho3d.io/t/free-terrain-editors/1790/4

-------------------------

wicash | 2019-05-18 17:04:48 UTC | #12

Thanks for the fast response. :grinning:
I managed to get a heigh map for the Terrain I created in Blender. 
Now I want to add my textures. Since the .xml files look like this

><material>
    <technique name="Techniques/TerrainBlend.xml" />
    <texture unit="0" name="Textures/TerrainWeights.dds" />
    <texture unit="1" name="Textures/TerrainDetail1.dds" />
    <texture unit="2" name="Textures/TerrainDetail2.dds" />
    <texture unit="3" name="Textures/TerrainDetail3.dds" />
    <parameter name="MatSpecColor" value="0.5 0.5 0.5 16" />
    <parameter name="DetailTiling" value="32 32" />
</material>
I figured I can just replace the TerrainDetail.dds files with my own. So far this works as well, but from what I see it seems like the texture units are placed randomly(?) Let's say I want to create a Terrain that has a small road in it and I want the road to have a specific texture. What would be the approach for doing this?

-------------------------

jmiller | 2019-05-18 17:53:12 UTC | #13

For blending the detail textures one will also need a corresponding [weight map](https://discourse.urho3d.io/search?q=weight+map). The U3D Terrain editor thread goes into some detail about those.

-------------------------

JTippetts | 2019-05-18 23:03:58 UTC | #14

Gotta admit, I haven't really worked on the terrain editor in quite some time, and it's never really been what you would call 'production ready'. Quite far from it. But if you can find anything in the log file to indicate what's going wrong, it might be helpful. Your screenshot shows that the terrain isn't being drawn, which is probably a shader compilation issue. I bounced quite a lot between GL and D3D11 when working on that thing, so at any given point in time one shader set or the other was completely broken, and I honestly can't say what condition it may have been in when I stopped working on it last.

I probably should push a notice to that repo about it's inactivity and brokenness.

-------------------------

Asimov500 | 2019-12-24 02:59:31 UTC | #15

Is there a tool for exporting from 3ds Max, or will Urho3D use obj models?

-------------------------

restless | 2019-12-24 13:21:54 UTC | #16

Have you tried AssetImporter?

 https://urho3d.github.io/documentation/1.7.1/_tools.html

Interesting how well does it work with .3ds format

-------------------------

Asimov500 | 2019-12-25 00:29:46 UTC | #17

I have not tried anything yet. Only just managed to get Urho3D compiled and working and not read any documentation yet. Most engines can work with FBX, or obj though, but not tried to put one of my own models into the engine yet though. Just thought I would ask the question. I have been modelling in 3d max for over 15 years now.

I will however be reading the documentation over the next few weeks to work out how to do stuff.

-------------------------

QBkGames | 2019-12-25 05:01:38 UTC | #18

The AssetImporter can convert FBX files to mdl files.

Note, however that the units/scaling may need some tweaking. When I export FBX from Blender I have to apply a scaling of 0.01 for the model to convert to Urho at the correct scale. And also the model might need to be centered on the origin otherwise it might export with an offset. These are the issues I've encountered exporting from Blender using FBX, may or may not apply to 3D Max.

-------------------------

Asimov500 | 2019-12-25 17:25:51 UTC | #19

Thanks for that. I always reset my coordinates to 0,0 because I am used to the Unity engine anyway. I think most engines expect that. I have used quite a lot of different engines, but this is my first time using Urho3D.

-------------------------

