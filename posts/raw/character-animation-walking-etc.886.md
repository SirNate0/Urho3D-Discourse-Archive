vivienneanthony | 2017-01-02 01:03:48 UTC | #1

Hello,

How do I go about taking a imported mesh from Makehuman to Blender.  Then making some type of animation like walking and exporting it to Urho3D.

I will like to bring some character to life and I additionally have to do the same to clothing.

Vivienne

-------------------------

Mike | 2017-01-02 01:03:48 UTC | #2

Currently typical workflow would be:
- export to mhx format from MH [url]http://www.makehuman.org/doc/node/load_save_and_export.html[/url]
- import mhx file into blender [url]http://www.makehuman.org/doc/node/mhblendertools_mhx_importer_basic_usage.html[/url]
- import mocap (motion capture) file using MakeWalk [url]http://www.makehuman.org/doc/node/mhblendertools_makewalk_basic_workflow.html[/url]
- or create animations from scratch by posing the bones and inserting keyframes (you can enable rigify option when importing the mhx to generate a rig)

-------------------------

TikariSakari | 2017-01-02 01:03:48 UTC | #3

For the part of importing character from blender to urho. I have noticed that when I've tried making my own models, the least glitched way has been using [url]https://github.com/reattiva/Urho3D-Blender[/url] exporter in blender. FBX-format almost always comes out glitched when using IK-rigs, Collada might come out correctly, but most success out of those 3 I have had with the blender exporter and also with collada, I haven't figured out how to import more than one animation per saving, so if you have several animations it is quite a pain to export everything. The animations being glitchy has something to do with bone rolls I think, but regardless of how much I tried the animations almost always come out incorrectly if using fbx-format in blender.

I have been using this [url]http://www.open3mod.com/[/url] for trying to view the files out of blender to see if they work. Usually, although not always, what you see in that software is what you get when you are using assetimporter in urho.

As for exporting whole scenes from blender, I feel like going the route of collada has been most succesful for me.

-------------------------

