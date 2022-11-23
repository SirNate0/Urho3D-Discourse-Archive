fanchenxinok | 2020-07-07 16:19:05 UTC | #1

hi all,
how to roll a texture 360 degree like a cyclinder without up and down surfaces as following image:
![untitled|405x414](upload://dBLhr4y7E7cHbzxjOcTgEsG20hN.png) 
i try to create a plane model then roll it 360 degree, but nothing change. 
// a roll plane
	Node* rollNode = scene_->CreateChild("RollPlane");
	rollNode->SetRotation(Quaternion(-90.0f, 0.0f, 0.0f));
    rollNode->SetScale(Vector3(4.0f, 2.0f, 2.0f));
    rollNode->SetPosition(Vector3(2.0f, 6.0f, 6.0f));
    auto* rollPlane = rollNode->CreateComponent<StaticModel>();
    rollPlane->SetModel(cache->GetResource<Model>("Models/Plane.mdl"));
    rollPlane->SetMaterial(cache->GetResource<Material>("Materials/rollMat.xml"));
	rollNode->Roll(360.0f); 

could anyone give me a hint, how to use Urho3D API to create it?
best regards!

-------------------------

jmiller | 2020-07-13 01:42:49 UTC | #2

Hi and welcome to the forum! :confetti_ball: 

Models/meshes are usually used by engines in final form. CustomGeometry is an option with Urho, as is programmatically creating indexed models, but both have disadvantages.

`Data/Models/Cylinder.mdl` seems closer to what you want, but it does have end caps.
One could:
Find or model a suitable cylinder with the [UV mapping](https://wikipedia.org/wiki/UV_mapping) you want. This can be done  with e.g. [Blender](https://www.blender.org/).
Export to Urho MDL. Urho comes with AssetImporter, and there are a couple Blender exporters linked from wiki, with one [Blender exporter](https://discourse.urho3d.io/t/blender-2-8-exporter-with-additonal-features-e-g-urho3d-materialnodes-and-components/5240) I have used recently.

:tropical_fish:

-------------------------

dertom | 2020-07-06 08:24:04 UTC | #3

Additional info, 'roll' means rotations around the X-axis.

[quote="fanchenxinok, post:1, topic:6246"]
rollNode->Roll(360.0f);
[/quote]

So what you did here was to rotate your model  360deg around x-axis which has obviously no effect.

-------------------------

fanchenxinok | 2020-07-06 10:05:08 UTC | #4

hi jmiller,
thanks for your reply, i will try.
best regards!

-------------------------

fanchenxinok | 2020-07-06 10:06:16 UTC | #5

hi dertom,
thanks for your reply.
best regards!

-------------------------

fanchenxinok | 2020-07-08 10:23:06 UTC | #6

hi jmiller,
i download urho3d-blender-exporter.zip, then i follow readme.md file in this package.
But encounter the following error:

* ->‘Install…’->[zip]/blender_addons/addon_blender_connect.zip and enable the checkbox

![捕获1](upload://sfUSTbqEX5ukYNSE5CbA5sg2qQp)

-------------------------

fanchenxinok | 2020-07-08 10:24:16 UTC | #7

also install "Urho3D-Blender.zip" addon encounter the following error:
->'Install...'->[zip]/blender_addons/Urho3D-Blender.zip and enable the checkbox:
![捕获2|690x172](upload://3syXwarfXkasmOqtKOufUekDjUU.png)

-------------------------

jmiller | 2020-07-08 18:51:10 UTC | #8

According to https://github.com/dertom95/Urho3D-Blender/wiki  you may also want to install https://github.com/dertom95/addon_blender_connect to enable the integrated Urho3D renderer. However, neither are necessary with the branches I use (master versions cloned directly to `addons/`).

-------------------------

fanchenxinok | 2020-07-09 01:52:24 UTC | #9

hi jmiller,
https://global.discourse-cdn.com/standard17/uploads/urho3d/original/2X/c/c6097f1b27e4aac213d5daa952d02f10bb7698c9.png
this error happened when install your addon_blender_connect package. 
i download the release package of urho3d-blender-exporter.zip from:
https://github.com/dertom95/Urho3D-Blender/releases/tag/0.1.2

i think it is the most recently release addon.

best regards

best regards!

-------------------------

fanchenxinok | 2020-07-09 02:17:29 UTC | #10

hi jmiller,

i modify _init_.py of addon_blender_connect from:
def register():
    **defRegister()**
    bpy.types.World.blender_connect_settings = bpy.props.PointerProperty(type=BlenderConnectSettings)

def unregister():
    **defUnregister()**
    del bpy.types.World.blender_connect_settings

to 


def register():
    **defRegister**
    bpy.types.World.blender_connect_settings = bpy.props.PointerProperty(type=BlenderConnectSettings)

def unregister():
    **defUnregister**
    del bpy.types.World.blender_connect_settings

the previous error fixed, but a new error happened:

Traceback (most recent call last):
  File "C:\Program Files\Blender Foundation\Blender 2.83\2.83\scripts\modules\addon_utils.py", line 382, in enable
    mod.register()
  File "C:\Users\Administrator\AppData\Roaming\Blender Foundation\Blender\2.83\scripts\addons\addon_blender_connect\__init__.py", line 35, in register
    bpy.types.World.blender_connect_settings = bpy.props.PointerProperty(type=BlenderConnectSettings)
NameError: name 'BlenderConnectSettings' is not defined

how can i fix it ?
best regards!

-------------------------

jmiller | 2020-07-09 02:39:57 UTC | #11

[quote="fanchenxinok, post:9, topic:6246"]
i think it is the most recently release addon.
[/quote]
Ah yes, good..

I am not familiar with this part of the setup, but looking again at https://github.com/dertom95/Urho3D-Blender/wiki .. maybe `pyzmq` addon was missed? The addon's thread and videos might also be useful.

-------------------------

dertom | 2020-07-13 01:42:49 UTC | #12

Yes, I guess @jmiller is right with his suggestion, that it is likely that you did not install pyzqm that this exporter uses. If you really want to use this exporter make sure to follow this instructions on that wiki link. I know, I know,... much hassle for installation.
You know that there is another blender-exporter which is much easier to install: https://github.com/1vanK/Urho3D-Blender/tree/2_80

-------------------------

