umen | 2017-01-02 00:58:50 UTC | #1

sorry for newbee questions , but there are some stuff ( simple ) that i don't understand .
the info in the example sources are very informative and i can learn allot and it is cool , the info in the new wiki is good but very high level 
for example i didn't found any where in the wiki or searching the forum what should i do when i like to :
1. model simple mesh and animate it  , what should i consider except low poly 
2.export it from blender (using Urho3D-Blender ) what is the right way ? what should i consider when exporting 
3.convert it to what ? how ?  what is preferred method / way ?

say i have all this info , i should know how to load it to the scene from the comments in the source .

4.what the editor can help me with the animated model , why  should i use it ? ( i have no idea what is level editor . 
but really the first 3 basic steps are missing or i just missed here something and can't connected the information bits .
thanks for your help !

-------------------------

rasteron | 2017-01-02 00:58:50 UTC | #2

Hi Umen, 

For me as a noob back then, learning how the engine importer works took some time and tests to figure things out. Start simple and make some simple changes to existing samples and/or code.

1. Max bone is 64 per submesh. [goo.gl/G70TWq](http://goo.gl/G70TWq). Animations can be setup or tweaked from code or script.
2. Learn from one of the examples. I think a good rigged and textured model from any supported formats will work. See SourceAssets folder as they consist of Blender and Ogre XML mesh files
3. Your models will be converted to native Urho format .MDL for mesh and .ANI for animation. More here [urho3d.github.io/documentation/a00041.html](http://urho3d.github.io/documentation/a00041.html)
4. like any 3d engines, Blender or any 3d software should do with Assimp file format support (since the engine supports it). The list of file formats here: [assimp.sourceforge.net/main_feat ... rmats.html](http://assimp.sourceforge.net/main_features_formats.html)

Here's a sample I did with the editor. The right zombie model (no armature) is a FBX format file imported directly using the Editor (File -> Import Model) and the sample ninja model as an Animated Model node (loaded, but usually this is done by script or code)

[img]http://i.imgur.com/UBTUMAj.jpg[/img]


You can also check out and search the old google forums ([groups.google.com/forum/#!forum/urho3d](https://groups.google.com/forum/#!forum/urho3d)) as there are many post there that has some good info on learning the basics. :wink:

Good luck and have fun!

-------------------------

umen | 2017-01-02 00:58:50 UTC | #3

Thanks for your answer , 
One more thing can i export from blender directlly in FXB format and then load to the 
Editor and then export it to engine format ? 
Also what is the true use of the editor ? 
How can it help me?

-------------------------

cadaver | 2017-01-02 00:58:51 UTC | #4

The editor has various purposes depending on how you count and there's no right or wrong way to use it, but whatever suits you:

1) Edit & compose scenes
2) Serve as an easy frontend for importing content (invokes AssetImporter tool)
3) Serve as an example of making an editor. It could be estimated that a full professional grade editor would take n times more effort (which is not realistic with current resources)
4) Test or prototype functionality, like scripts, physics, or engine features

-------------------------

umen | 2017-01-02 00:58:51 UTC | #5

Thanks for the answers!
bean playing with the editor i think i got the general idea of it comparing the Physics.xml i created with my test scene. 
i have suggestion for the editor tell me if it help ( its great help in other frameworks like Qt GUI editor and UML creation apps ) 
what about option to generate skeleton code or complete scene code out of the Editor created scene 
this will be big time saver and helper for prototyping and testing even skeleton for levels in games . 
i have allot of experience in Qt GUI editor and i know this option helps allot .

p.s 
quick question , in the editor how do i change the Far Clip / near Clip lens of the camera White  colour its hardly seen . 
Thanks

-------------------------

cadaver | 2017-01-02 00:58:51 UTC | #6

Yes, I know the mechanism how Qt creator can generate code from UI layouts.

In my opinion this is not the right direction for 3D or game scenes, particularly when they start to have large amount of objects (100+). The sample applications generate scene objects in code just because they're simple examples and they're teaching about the engine functions at the same time. In a real game project both the scenes/levels and the objects that are being spawned mid-game ("object prefabs") should rather be loaded from file data; Urho supports either XML or binary format. The NinjaSnowWar example demonstrates this.

-------------------------

umen | 2017-01-02 00:58:51 UTC | #7

I see , thanks for the answer

-------------------------

Mike | 2017-01-02 00:58:51 UTC | #8

I think examples should be more clear and simple if we were using prefabs/scenes.
We should demonstrate creation by code only in the first ones and quickly move to prefabs and scenes so that we could focus on the "meat" rather than spending most of the code to build the scene, distracting us from what is to be demonstrated.

-------------------------

cadaver | 2017-01-02 00:58:51 UTC | #9

It depends. Something like displaying the stone box or mushroom for the nth time could as well use a prefab, but when you're explaining things like Rigidbody settings it's IMO more pedagogical to set up the values in code, so that you know what the important values to change are. If you just look at eg. Rigidbody in the editor for the first time you may be overwhelmed because of all the attributes.

-------------------------

Mike | 2017-01-02 00:58:51 UTC | #10

Yes, each time something is demonstrated for the first time or needs obvious tweaking we should still rely on code, what I mean is that we should mix prefabs and code in a selective way.

-------------------------

