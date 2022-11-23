slapin | 2017-06-27 22:50:53 UTC | #1

Hi, all!

I have full scene with a set of different objects animated together.
Like 3 characters dancing and cubes rotating around them, everything made in Blender (no much
relevance, just as an example), exported as FBX or DAE. Blend is also available. I want this scene
to work in Urho as I see it in Blender. What is the process to
do this? Scenes can be different and have more stuff in them, I want to know some kind of generic workflow/approach to them.

-------------------------

johnnycable | 2017-06-28 12:44:06 UTC | #2

[quote="slapin, post:1, topic:3291"]
I want this scene
to work in Urho as I see it in Blender.
[/quote]

Those are big words... they're different enough.
What's wrong with reattiva exporter?

-------------------------

slapin | 2017-06-28 15:29:27 UTC | #3

> What's wrong with reattiva exporter?

It can't export scenes. BTW, I can't get your "big words" point. Elaborate?

-------------------------

johnnycable | 2017-06-28 16:05:40 UTC | #4

Blender render gives you the classical 3d pipeline (dx9). Cycles gives st like PBR. Anyway I doubt you can get blender cycles shaders to work with urho by simply exporting... not sure anyway. didn't tried for now. "Big words" means you don't probably get wysiwyg...
"No scenes" means you're trying to export things like skyboxes? If I'm not mistaken asset importer does import scenes...

-------------------------

slapin | 2017-06-28 16:07:23 UTC | #5

Well, I did not mean that by "exactly" more like "geometrically" i.e. lets put materials aside for now.

-------------------------

slapin | 2017-06-28 16:09:10 UTC | #6

AssetImporter can't blender. I can do static scenes using Collada export, but I'm more interested in animated scenes.
Any ideas?

-------------------------

johnnycable | 2017-06-28 17:48:33 UTC | #7

With Collada you can do animated ones too... mean you don't need blender...

-------------------------

lezak | 2017-06-28 19:11:51 UTC | #8

[quote="slapin, post:3, topic:3291"]
It can't export scenes.
[/quote]
Actually it can - You need to check "Export Urho prefabs" and there will be option "scene prefab". You just need to make sure that every thing is set up correctly, for example if You're using export UV option, all models should have UVs. 
[quote="slapin, post:6, topic:3291"]
AssetImporter can't blender.
[/quote]

Once again - it can, To import *.blend file You need to use 'scene' command (or You can use "import scene" in editor). It may not be the best solution, since all models will be imported as static, with no physics etc. (but with materials) also You'll have to rotate whole scene in blender (blender - urho up axis mismatch). Because of that I wouldn't recomend it to import ready scenes, but it's verry useful to import large number of models at once.

-------------------------

slapin | 2017-06-29 09:42:00 UTC | #10

Well, it looks like you did not use the tools yourself, so you don't really know.

1. You can't export actual scene using exporter - you can only  export a model. That means
if you have some stuff around model at some positions, these will not be kept.

2. AssetImporter doesn't support .blend files. Not ones from Blender 2.7.x at least.

-------------------------

slapin | 2017-06-29 09:43:15 UTC | #11

Also, please don't pollute this topic with half-assed answers.

-------------------------

slapin | 2017-06-29 10:56:09 UTC | #13

OK. Please don't pollute THE topic. Or I will create new one.

Half-assed = recommendations which are not tested in practice.
Note that unlike most of the audience (it seems) I actually use engine and all its tools
and ask questions only on grey topics which either not documented, not obvious, hard to discover
OR unexplored field. Providing answers from Google search result (or other search engine) is pointless
as I have already read them and tried them. If you don't have time to test your suggested solution, please
don't suggest it. It just wastes everyone's time and increases frustration. Each time you do this
a flock of newborn kitties is eaten by neighbour's dog. Trust me.

So if I ask question I want to get practical answer, not theoretical. If you did some similar stuff or are interested to do some research, or have some practical hints, I'm really interested. If you thought I can't use search so do that for me - please don't.

-------------------------

slapin | 2017-06-29 11:06:32 UTC | #15

Recommendation for use of Blender to Urho exporter for scenes.
It doesn't support it.
https://github.com/reattiva/Urho3D-Blender/issues/66

Use of Collada export only works for static scenes.

Also I know I can do everything manually. I basically ask how it is done by actual people
who actually have this problem. This is workflow question, not a question about export tools.

1. I know about blender exporter and its limitations.
2. I know about buggy Blender Collada exporter and its limitations and that I can use AssetImporter on that and recombine scene manually in script. This is a lot of manual labor.
3. I know about buggy Blender FBX exporter and its limitations and that I can use AssetImporter on that and recombine scene manually in script. This is a lot of manual labor.

Please do not suggest tools without explanations.

And yes, I don't believe you who have this task actually do this. I think somebody written some scripts OR
uses some crafty methods. So I want to know about these.

-------------------------

johnnycable | 2017-06-29 14:23:37 UTC | #16

Looks like it works.

The very basic blender scene:

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/bdb7c8e1e80f0ac458618698a50b31e4895c21e6.png" width="686" height="500">

The very easy setup:

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/494be8a404076a694be7201034465a25727a7fa4.png" width="440" height="410">

the urho reattiva plugin export options:

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/b353e1d19dc2d6945b0b46f06edaa529ecb240b3.png" width="330" height="500">
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/0656e96097481345a8a330ca37c65e8cbb17aa20.png" width="393" height="500">

the obtained objects in file system:

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/bf4911af2dc87b8f3b7457aec5cd57e8079d4ed5.png" width="690" height="136">
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/478c74d5a8a2a5c0cc3b5dbef666d953f7041ae4.png" width="690" height="140">

the final result in the editor:

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/81a74f82cfaa5752cc12cd76ff1e0b6cdb726faa.png" width="690" height="379">

Anyway, some times ago I tried to import miku hatsune and failed... :disappointed:
what a shame... must've been the physics...
but I will try again...

-------------------------

slapin | 2017-06-29 15:15:10 UTC | #17

By doing this you exported all objects with origin set to 0 and geometry offset. You can check this in editor.
You could also check the bug I linked here. Please think constructively - I have already passed all this.

-------------------------

slapin | 2017-06-29 15:39:49 UTC | #19

*facepalm* *facepalm* *facepalm*

Please check the result and see what you got.

-------------------------

slapin | 2017-06-29 15:44:36 UTC | #20

Also hint for stubborn - check python code for position XML values in scene/prefab output. Look hard.
After the result, please come back. I hope that torment is enough for you. Sometimes I wonder if people can read at all. I made short post, so even tl;dr'ers will be happy, explained things, added links to bugs, but still nothing... :(

-------------------------

slapin | 2017-06-29 15:51:18 UTC | #22

Detention for you:

1. Export to Collada. Import via AssetImporter. Look at scene in Editor. Check object origins.
2. Export via Blender exporter. Load into editor. Check object origins and placements. Compare with 1.
Provide results.

To be sure, by object origin I mean 0 in object-local coordinates, which is set in Blender.
Closely related to actual object POSITION.

Don't try to invent anything, I know what it can and can't do and how it does that.

-------------------------

slapin | 2017-06-29 15:53:07 UTC | #24

Even just comparing xml data visually for scenes aquired via collada or Blender exportive should give you hint.

-------------------------

johnnycable | 2017-06-29 16:04:08 UTC | #25

I guess @slapin is right here. I'm trying by switching various options in the exporter, but one thing is for sure: if I use the options as I did above (export scene prefabs only), and I open the scene in the editor, the scene is imported as a node with all object correctly placed as i put them in blender - anyway, node position in the attribute inspector of every object is zero. And that is no good. @Modanung, what you did exactly? Can you share your process?
While I'm looking that if I export one collective scene, the editor asks me to import as a prefab when I open the scene - I do, still the situation is as above - all object with zero position but set correctly - and the scene node alone instead has its own position with correct displacement in the attributes inspector...
Needless to say that setting position to local in the exporter gets all object to zero position in the editor... :neutral_face:
How does this work?

-------------------------

johnnycable | 2017-06-29 16:34:31 UTC | #26

Anyway that could be only a bug in the editor... I have to try to open the scene from code and check objects positions...

-------------------------

slapin | 2017-06-29 16:36:48 UTC | #28

Look at scene/prefab xml using text editor. (If you don't know the format, look at scenes from examples or
export scene using Collada and use AssetImporter, and compare to what you get).

-------------------------

johnnycable | 2017-06-29 17:22:32 UTC | #29

I did. No sign of position. That probably means is hardcoded into exported mdls. No luck there, it's binary.
HATE binary...
Haven't tried with asset importer yet...

-------------------------

johnnycable | 2017-06-29 18:25:20 UTC | #30

Tried with asset importer... works.
All the blender scene imported, light, zone, models, everything.
Just one thing: position inverted z = -z, y = -y.
:cry:
it that's confirmed, there's no other way short of creating a manual importer :persevere:
but i'm going to look at it tomorrow.

-------------------------

slapin | 2017-06-30 10:22:13 UTC | #31

IIRC there was some settings to make -Z +Y facing scene in exporter. But that is actually not what I point in discussion.

**TL;DR'ers, skip the following paragraph please, your brain might explode**
Ideally I want to have some kind of animation-ready setup, which collada/fbx export do not provide but
it looks not too complicated to implement. While I can do this for Torque3D, for example,
somehow this doesn't work for Urho - i.e. I want to setup global animation for scene and have this one exported. So that everything is transformed over time just after loading scene/spawning prefab. This might work for close interaction animations (fighting) or cutscenes (at least). At very least that would reduce needed work to set such things up...

-------------------------

johnnycable | 2017-06-30 19:51:59 UTC | #32

@slapin , @Modanung

[quote="johnnycable, post:30, topic:3291"]
Tried with asset importer... works.
All the blender scene imported, light, zone, models, everything.
Just one thing: position inverted z = -z, y = -y.
:cry:
it that's confirmed, there's no other way short of creating a manual importer :persevere:
but i'm going to look at it tomorrow.
[/quote]

What exactly happens it Z position ONLY is negated. Everything gets -Z. I exported a plane in 0,0,0 and it's got 0,0,-0...
AND everything is rotated 90° ccw around y...
The problem is in the scene xml file and not in the editor.

	<node id="3">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="Plane" />
		<attribute name="Tags" />
		<attribute name="Position" value="0 0 -0" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="2 2 1" />
		<attribute name="Variables" />
		<component type="StaticModel" id="5">
			<attribute name="Model" value="Model;Models/Plane.mdl" />
			<attribute name="Material" value="Material;Materials/DefaultMaterial.xml"/>
		</component>
	</node>

So it's probably st in the exporter... I'm on 1.6 stable on osx. Going to test head.

-------------------------

johnnycable | 2017-07-04 17:17:23 UTC | #33

More on Reattiva.

the very simple scene:

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/a9b722d4dfa9e2eeab6eb5344930cdafb2ba30de.png" width="681" height="500">

the setup:

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/a8050efc97ae3123d554f8ec586a734bbd6f701b.png" width="265" height="500">
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/5d23a334e77a78d6c578b822cdb535672b7b21fa.png" width="187" height="500">

the scene loaded in example 38_SceneAndUILoad with:

> void SceneAndUILoad::CreateScene()
> {
>     ResourceCache* cache = GetSubsystem<ResourceCache>();

>     scene_ = new Scene(context_);

>     // Load scene content prepared in the editor (XML format). GetFile() returns an open file from the resource system
>     // which scene.LoadXML() will read
>     SharedPtr<File> file = cache->GetFile("TestScene/TestScene.xml");
>     scene_->LoadXML(*file);

running the exe shows every object crammed at position 0,0,0:

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/ba1c31b8c90682c7057bed8dda5ff6bcf983a8f4.jpg" width="690" height="431">

When loaded in the editor, objects are in correct position but with zero position values...

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/c7ad3acc751b86f933d2dc99e8ee028569d32780.png" width="690" height="431">

So it is beginning to look like Urho Reattiva exporter for blender doesn't work.

-------------------------

johnnycable | 2017-07-04 17:24:38 UTC | #34

As a side note...
HEAD is the same
Asset Importer shows similar problem. Asset position is correct, reference system is exchanged, suzanne doesn't export correctly and the pyramid shows wrong geometry... :no_mouth:
the blend file (rename in TestScene.blend)
<a class="attachment" href="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/ff567c5f1f388ac89b9d03c3f83e63940052b396.csv">TestScene.csv</a> (600.0 KB)
Urho3d 1.6, Os X 10.12.3, Blender 2.77

-------------------------

Modanung | 2017-07-04 18:29:30 UTC | #35

With these settings, the only thing that doesn't seem to work is rotation and scaling.

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/dafb27c2c81c5d9518f167b5b1828a0194cb1272.png" width="690" height="441">

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/b7974559bdeab52eb632f8d88b3498cf03b936fe.png" width="690" height="456">

-------------------------

johnnycable | 2017-07-04 20:14:58 UTC | #36

wait... I don't have those options in my reattiva plugin. "Save node position", "rigidbody mass". Where is it from?

-------------------------

Modanung | 2017-07-04 21:41:02 UTC | #37

Those options appear when you enable _Export Urho Prefabs_.

-------------------------

lezak | 2017-07-04 22:00:02 UTC | #38

For such  a simple scene directly importing .blend file works fine (assetimporter or import scene in editor) , all You need to do is place 3d cursor at 0,0,0 and rotate whole scene around it by -90 on x axis (and of course remember to apply rotation and scale - in attached blend file suzanne don't have rotation applied). Just keep in mind that it will import everything as static model. 
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/b71e496485c3893286257a9c584647d20e3c2762.png" width="690" height="356">

-------------------------

rasteron | 2017-07-04 23:08:49 UTC | #39


The settings should be **Front View = Back**
https://github.com/reattiva/Urho3D-Blender/commit/dda553d1c1259f53497e68e116392b0f0e690087

and in Blender, you still have to set **Apply Visual Transform (CTRL+A)**

@lezak
green arrow is `Up` on Urho, not the same with Blender :slight_smile: No need to rotate the whole scene, just apply visual transform..

@Modanung
Using the latest, I also don't see the `Use Gravity` and other sub options there even when you toggle Export Urho Prefabs, are you using a custom or older version?

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/54c141d5b7163a7b30b096187d28218bfb522a40.png'>
-
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/fa5ff5e89ba23d895b8449d77766866ade4ffcb7.png'>

-------------------------

Modanung | 2017-07-05 00:09:58 UTC | #40

[quote="rasteron, post:39, topic:3291"]
are you using a custom or older version?
[/quote]

Apparently, yes. I seem to have both 0.5 and 0.6 installed, and 0.5 was activated.

-------------------------

rasteron | 2017-07-05 02:48:45 UTC | #41

Ok got it thanks :slight_smile:

-------------------------

johnnycable | 2017-07-06 16:02:44 UTC | #42

@rasteron  did as you said, but to no avail. The issue opened by @slapin  is confirmed in https://github.com/reattiva/Urho3D-Blender/issues/66 where they explain exporting scenes was not foreseen in the beginning... it's in the way but not ready yet.
Meanwhile exporting into the editor gives some results, but with a different coord system...
@Modanung could you share the v.5 version plugin? I'm not able to find it anywhere...
Thank you

-------------------------

Mike | 2017-07-06 18:29:31 UTC | #43

Experimental version should be available tomorrow  :stuck_out_tongue:
I'm currently doing some cleaning and finishing documentation :face_with_monocle:

-------------------------

rasteron | 2017-07-06 21:12:12 UTC | #44


Version 0.5 starts [here](https://github.com/reattiva/Urho3D-Blender/tree/c7f586ce38704fa515e8005be19ed2f2cb3d27d4) but it looks like @Modanung has a specific commit version.

-------------------------

rasteron | 2017-07-07 00:26:28 UTC | #45

Actually, did some more quick export tests just recently and I don't see any problem with the exporter and it is applying the positions properly. I do have to note that the **Apply Visual Transform** setting is just a specific case since I usually export single mesh lightmapped scenes for mobile testing, you can discard that part and try again. You still need to set **Front = Back** btw.

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/f5a91263df7580edaec68233387c0db4c218765e.jpg" width="690" height="388">

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/abf6f95aa63c6c6027d0e16b509a1a3f4757e1ab.jpg" width="690" height="250">

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/f94e119298840df58f976ef83911228272844eba.jpg" width="317" height="437">
.
Blender v2.77 64-bit, Exporter 0.6 ([9ead493](https://github.com/reattiva/Urho3D-Blender/tree/9ead493c92787e8014353244bda5fecbd285c6ce))

-------------------------

rasteron | 2017-07-06 23:28:06 UTC | #46

A more complete test with position, rotation and scale exported. All suzanne meshes scaled 2x, looking at ball and positioned 8 units away from center and at ground.

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/882ee1511a4bf30d4821e2ddd685d0b204bd8ee2.png" width="690" height="431">

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/ec374380089afa9ba304989fa41265db7fa747c3.jpg" width="690" height="297">

For the scaling part, values are correct but this should be done inside blender since you should apply the final **mesh** dimensions before export (apply visual transform, scale only).

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/5f653599353d0413e45fcdcdd801591a13790946.png" width="690" height="276">

-------------------------

Mike | 2017-07-07 09:26:06 UTC | #47

Experimental derivative available [here](https://github.com/Mike3D/Urho3D-Blender-Mod).
Please read the 2 supplied guides thoroughly to grasp the new features.

-------------------------

rasteron | 2017-07-07 09:28:37 UTC | #48

This is awesome Mike, will check it out :+1:

-------------------------

Mike | 2017-07-07 09:43:11 UTC | #49

For those who want to stick to vanilla exporter, the 'Transform objects' option (as seen in Modanung screenshot) has been added by Reattiva on june 3rd. So if you don't have this option available, you are encouraged to upgrade your exporter (currently only Front-view = 'Front (-Y +Z)' supported).

-------------------------

johnnycable | 2017-07-07 13:30:45 UTC | #50

Thank you, I'll try asap.

-------------------------

johnnycable | 2017-07-10 12:03:36 UTC | #51

So here it is, in blender:

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/2441160c90e3d2b44c119a2861aeeb72165e5da0.png" width="690" height="422">

and the editor:

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/b7ccd641e786de8c51786608f1dcad4a3fe10d60.png" width="690" height="363">

exported with the new plugins, thanks to @Mike. Back (+Y+Z) chosen (the one with the asterisk :stuck_out_tongue:)  position is correct now. Rotation is different in sign, anyway orientation is correct; changing the sign rotate the items wrong. I don't know if this is correct...
I tried using the new scene exporter with the momo project inside the zip. I only obtained partial results, but probably I messed up something... procedure should be: first open and export the momo asset.blend, then open and export the momo scene.blend, right? 
In the editor I've got some scenery correctly but some other wrong. I'll try that again later.
Thank you to all of you guys for the help.

-------------------------

slapin | 2017-07-10 12:53:16 UTC | #52

@Mike thank you so much for feature.

Now, while you're at this could you please add bone Z-facer (with animations)?
It looks like Urho heavily depends and assumes that bones face Z axis (Y axis in blender),
but animated models I have here do have different rolling scheme, so direct bone control
never works properly... It is possible to sort of fix this by using helper Nodes with known direction
attached to bones, but it looks like nobody actually cares about actual bone roll. Somehow other engines
like UE4 and Unity cope with this automatically, but for Urho some magic have to be added...

-------------------------

Mike | 2017-07-10 19:08:12 UTC | #53

I always export my armatures with bone roll set to +Y Axis, this makes life easier in Urho.

I think we'd better, focus on motion retargeting in Urho, which could benefit the whole community.

-------------------------

slapin | 2017-07-10 20:40:41 UTC | #54

Well, the main problem is that if you get your models from animator already with animations and you simply can't rework them, that will be show stopper now. And changing bone roll in exporter would really help many people (I think).

-------------------------

slapin | 2017-07-10 20:42:21 UTC | #55

BTW what you mean by motion retargeting - engine feature or exporter feature?
Could you elaborate a bit more?

-------------------------

Mike | 2017-07-11 05:44:49 UTC | #56

I mean something like [this](https://www.evl.uic.edu/sjames/mocap/motionviewer.html). Retargeting a mocap or ani file to any skeleton in Urho,

-------------------------

slapin | 2017-07-12 03:41:33 UTC | #57

Well, Blender already contains quite good set of tools both for retargeting and mocap handling.
Or do you mean something different?

-------------------------

Mike | 2017-07-12 05:48:36 UTC | #58

Then why don't you simply retarget your animations to a +Y Axis armature ?

-------------------------

slapin | 2017-07-12 07:17:50 UTC | #59

I'm not really animator, retargetting is heavy work.
For roll fixing there is no need to do full-blown retargetting - it is easiest to do during export and can be done automatically.
Fixing the roll is just calculation of proper inverse transformation and applicating it to each bone fixed for each animation frame.
BTW, some export optimizations are needed beforehand, as it is extremely slow now (I suggested some ways before, like
limiting amount of steps wrapping some loops around).

-------------------------

artgolf1000 | 2017-12-14 00:05:39 UTC | #60

I have never exported a whole scene, for the Blender exporter had been designed to export models.

There is another limitation in the exporter: It can export all 'Shape Keys', but it will not export any keyframes of these 'Shape Keys'.

The official exporter(AssetImporter version) does not export any 'Shape Keys' at all.
 
In short, if you want to support vertex morph, you need to write your own code to load keyframes of 'Shape Keys', and implement your own shape key sub-system.

-------------------------

