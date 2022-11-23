rogerdv | 2017-01-02 01:03:02 UTC | #1

I see that Urho3D inherits resource directory structure from Ogre3D, but I see a little problem with that: if I had dozens of meshes, the Textures, Materials and Models directories tend to become crowded. Is it possible to adopt a more distributed structure like this?

Data
  Vegetation
    Tree1.mdl
    Tree1.jpg
    Tree1.xml
    ****
  Buildings
    ***
  Terrain
    terrain-texture1.dds
   ***

-------------------------

Mike | 2017-01-02 01:03:03 UTC | #2

You are free to adopt custom data structure inside the 'Data' folder for your own assets.

-------------------------

friesencr | 2017-01-02 01:03:03 UTC | #3

I did something similar for our game.  Each character gets a folder with its resources.

-> data
--> characters
---> robot_dude
---> battle_bus
--> tilesets
---> spaceship


I tended to prefer barfing every resource type into that folder without sub folders further.  Textures work better in blender with the models being in the same folder as the model.  there is also the weirdness of image packing in blender.  It isn't a matter of can.  Urho has no restrictions on what organization you have.  The editor has some default path locations that don't work well if you don't use the defaults.  That is one of the reasons I made the resource browser as it lets you slice your pie in different ways.

-------------------------

JulyForToday | 2017-01-02 01:03:04 UTC | #4

I have a related question. Is it possible for the path references inside of xml files be relative?

So say I have a scene. The default set up is for my "scene_name.xml" to be inside of the Data/Scene folder, and the file would look something like this:
[code]
		<component type="Skybox" id="13">
			<attribute name="Model" value="Model;Models/Box.mdl" />
			<attribute name="Material" value="Material;Materials/skybox.xml" />
		</component>
[/code]

The models and materials are assumed to be in the root Data folder.

I want to have a structure like this:

Data/Places/place01/materials/
Data/Places/place01/models/
Data/Places/place01/textures/
Data/Places/place01/place01_scene_name.xml

To make this work I need to set the paths like this:
[code]
		<component type="Skybox" id="13">
			<attribute name="Model" value="Places/place01/models/Box.mdl" />
			<attribute name="Material" value="Places/place01/materials/skybox.xml" />
		</component>
[/code]

But I would like to do is have it relative to the scene file's path, so I could have this instead:

[code]
		<component type="Skybox" id="13">
			<attribute name="Model" value="models/Box.mdl" />
			<attribute name="Material" value="materials/skybox.xml" />
		</component>
[/code]

Which looks like the default, except I want some way to tell urho I mean the model and material folders inside Data/Places/place01/ instead of just Data/
Would something like this also be possible with all the other xml files? Having materials reference textures, prefabs/objects referencing other resources, relative to where the file containing the paths is on disk.
The reason I'd want this is in the case I want to move things around, things are much less likely to break. If I were to rename place01 to differentplace02, everything inside my example would break.

Not sure if it is possible, but it sure would be nice to have relative paths like that.

And I'm only asking if Urho itself can do this. I know the editor doesn't work this way, and would mess things up. Thankfully, the editor is straight forward to change.

-------------------------

cadaver | 2017-01-02 01:03:05 UTC | #5

You can make that work by adding a resource path to your scene base folder when you switch to that scene, then remove that path when you switch to another scene. Not convinced that Urho should do that automatically. I know there's some logic in the 2D animation resources to use relative paths, but that is more to ensure that data saved from external editors (eg. Spriter) works out of the box.

-------------------------

JulyForToday | 2017-01-02 01:03:05 UTC | #6

I suppose I would use the ResourceCache to set a resource path?

For the project I have in mind, which is small scale, this could work.

But I imagine you could only have that one base path (otherwise you'd have conflicts), so it would only be usable with one scene (at a time), and not so much for other resource types.

Personally, I was hoping for something along the lines of Blender, where you can specify an external data path relative to the scene file.
[code]Assuming your blender file lives here:
D:\Game\Projects\SomeProject\Scene\waterscene.blend

Instead of referencing the texture like this:
D:\Game\Projects\SomeProject\Scene\Textures\watertexture.png

You add the // prefix like this:
//Textures\watertexture.png
[/code]
Now you can rename or move the Scene folder with it's contents wherever you want, and the references in the blend file don't break.

So, for example, I would want to do something like this in Urho:
[code]
Data\Scene\waterscene.xml
Data\Material\watermaterial.xml
Data\Textures\watertexture.png

Data\Scenes\WaterScene\waterscene.xml (relative path for material: //materials\watermaterial.xml)
Data\Scenes\WaterScene\materials\watermaterial.xml (relative path for texure: //..\texures\watertexure.png)
Data\Scenes\WaterScene\textures\watertexture.png
[/code]

Then I could rename the WaterScene folder, or move it into a nested folder or different folder. I guess this sort of thing is not that big a deal for scenes, as much as prefabs/objects, where it would be really useful. And also for setting up a structure conducive for modding. From the perspective of a larger project with many assets, where you'd most likely want to arrange things like OP, and things are liable to get shuffled around a little, and also from the perspective of modding a finished game, having hardcoded paths inside of resources can really be a pain.

I understand if this is something Urho can't do at the moment, or if it wouldn't be possible given the engine's design. I just wanted to ask if it was possible, since it's a rather (imho) desirable feature/ability.

Edit: forgot the elipse in the texture's relative path

-------------------------

JulyForToday | 2017-01-02 01:05:58 UTC | #7

Bump.
Wanted to see if anyone had new input on this issue.

-------------------------

t.artikov | 2017-01-02 01:08:14 UTC | #8

I agree with JulyForToday.
It would be nice for me if resources refer to each other by relative paths.

-------------------------

