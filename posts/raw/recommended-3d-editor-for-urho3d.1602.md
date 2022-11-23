DragonSpark | 2017-01-02 01:08:49 UTC | #1

Hello all,

I am a developer looking into creating an application based on Urho3D.  I am also thinking about learning how to create 3D models, and I am curious on what everyone here uses, and what the recommendation is for a beginning developer to use to create models for Urho3D (for a proof of concept, doesn't have to be fancy, obviously).

Thank you for any suggestions,
Michael

-------------------------

Calinou | 2017-01-02 01:08:49 UTC | #2

[url=http://blender.org/]Blender[/url] or [url=http://www.wings3d.com/]Wings 3D[/url].

-------------------------

bukkits | 2017-01-02 01:08:54 UTC | #3

Er... definitely Blender, not Wings3D.

I'm not even sure if Wings3D is alive anymore, but Blender is a far more complete and capable package with extensive documentation and community support.


EDIT:

CG Cookie is a good source for getting started with blender. Be aware that many tutorials on the internet for any 3D software is filled with bad advice and technique, but these are pretty solid. 

[cgcookie.com/learn-blender/](https://cgcookie.com/learn-blender/)

-------------------------

codingmonkey | 2017-01-02 01:08:54 UTC | #4

Any 3d editor what support export to any format what supported by AssetImporter
3dmax -> fbx- > AssetImporter -> mdl
maya -> fbx - > AssetImporter -> mdl
blender -> mdl

-------------------------

boberfly | 2017-01-02 01:08:58 UTC | #5

Highly recommend Blender also, especially if you don't want to pay for an expensive 3D application. It's perfectly capable of doing what the expensive apps can do, especially if you're doing real-time stuff.

I personally use Maya and successfully modelled/rigged/animated and exported an FBX file into Urho3D a few years ago, as I know Maya inside-out far more than Blender, especially at the time. There's an 'LT' version which is geared towards indie developers but I've not used this version of Maya before.

(This is coming from a professional 3D artist/TD).

Hope this helps!

-------------------------

Dave82 | 2017-01-02 01:09:01 UTC | #6

Blender is a good choice and among all commercial software i prefer 3ds max. You can use it as a modeller/level designer tool , and with maxscript you can turn it into a extremely powerful scene/placement editor so you can use it as an "all in one" tool.

-------------------------

Modanung | 2017-08-30 10:56:11 UTC | #7

[Blender](http://blender.org/), with [exporter](https://github.com/reattiva/Urho3D-Blender).

-------------------------

greenhouse | 2017-01-02 01:09:18 UTC | #8

Can I use Blender+exporter as a complete scene (2D/3D) creation tool or it's only can be done with Urho's Editor?

-------------------------

rasteron | 2017-01-02 01:09:19 UTC | #9

[quote="greenhouse"]Can I use Blender+exporter as a complete scene (2D/3D) creation tool or it's only can be done with Urho's Editor?[/quote]

You can check out the Urho3D Blender exporter panel and verify this, but afaik you can only export staticshapes and prefabs with it. I would suggest looking into the included [b]AssetImporter[/b] tool as it can read blend files and has an export as scene option.

[code]
Usage: AssetImporter <command> <input file> <output file> [options]
See http://assimp.sourceforge.net/main_features_formats.html for input formats

Commands:
model      Output a model
scene      Output a scene
node       Output a node and its children (prefab)
dump       Dump scene node structure. No output file is generated
lod        Combine several Urho3D models as LOD levels of the output model
           Syntax: lod <dist0> <mdl0> <dist1 <mdl1> ... <output file>[/code]

-------------------------

thebluefish | 2017-01-02 01:09:25 UTC | #10

[quote="codingmonkey"]Any 3d editor what support export to any format what supported by AssetImporter
3dmax -> fbx- > AssetImporter -> mdl
maya -> fbx - > AssetImporter -> mdl
blender -> mdl[/quote]

Can recommend this workflow for both 3DS Max and Maya. They work well for myself and an artist working with me.

-------------------------

globus | 2017-01-02 01:09:25 UTC | #11

[autodesk.eu/store](http://www.autodesk.eu/store)
3DMax ~   246,00 ? - 6.045,45 ?
Maya ~     246,00 ? - 6.045,45 ?

Blender - [b]FREE[/b]

-------------------------

abhijeet | 2017-08-30 06:39:28 UTC | #12

I am very new to all this 3d stuff, trying to build something with Urho3d for Xamarin forms 

I have .mdl files & I am able to render it on UrhoSurface, I want to provide texture to it (Styling)

Can anyone guide me on this ?

-------------------------

