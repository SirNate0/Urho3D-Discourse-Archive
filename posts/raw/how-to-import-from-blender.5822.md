pldeschamps | 2020-01-23 12:36:12 UTC | #1

Hello,
My purpose is to make a planetarium. I want the user to see stars and to click on a star to select it and get informations.
I made a 3D scene with blender and python scripting: I made 500 white filled circles around a sphere (the 500 stars are at the good position, facing the center). The light and the camera are in the center of the scene. I can render it in Blender.

Next, I need to import the objects in my Urho3D project.

These are few questions :

1. the Blender Urho3D addon seems not to work with Blender 2.8. Right?
I need to use Assetimport to convert my scene.
2. Can I convert a full node with all the circles in it. assimp does not propose me Urho3D export command. How should I do? Is there any step by step documentation?
3. what should I get? a xml file? 500 xml files? a mdl file?

I made python scripting in blender to draw the sky.
4. would it be a better (faster or easier) solution to draw the sky in urho editor with angelscript?

Thank you for your help and your advices

-------------------------

JTippetts | 2020-01-23 12:36:05 UTC | #2

reattiva's [exporter](https://github.com/reattiva/Urho3D-Blender/tree/2_80) has a branch named 2_80. Clone the repo and switch to that branch (or just visit that link, and choose download ZIP, then follow the README instructions to install the addon in Blender) . The exporter worked the last time I tried it with Blender 2.8.

-------------------------

throwawayerino | 2020-01-18 18:25:51 UTC | #3

There's also AssetImporter.exe if you build it with Urho3D, where you can pass it a collada file or a blend (?) and get an mdl + Textures, animations, etc.

-------------------------

pldeschamps | 2020-01-18 20:29:02 UTC | #4

Great, it works!
So I exported 7 selected circles as 7 .mdl files. (I can't attach any picture at this time :frowning: 
Is it possible to export one mdl file with all the 500 circles as children nodes?
Will the user be able, from a urho3d project, to select one circle among the 500 circles mdl unic file?

-------------------------

pldeschamps | 2020-01-18 21:32:20 UTC | #5

So I ticked the "Merge objects" box and exported a 134 Ko .mdl file. I guess I made it.
I will try to render it in a urho3d project and see if the user can select one circle and if I can get the name of the object clicked...

-------------------------

Modanung | 2020-01-18 23:15:43 UTC | #6

The exporter also has the option to export an XML scene file, which may be useful.

-------------------------

pldeschamps | 2020-01-22 06:08:32 UTC | #7

Thank you for your answers.
I was able to see my model in a urho3D project. But I can't see the Materials (the color of the disks).
I tried to export the materials but I get this error:

> Traceback (most recent call last):
  File "C:\Users\pierre-louis\AppData\Roaming\Blender Foundation\Blender\2.81\scripts\addons\Urho3D-Blender-2_80\__init__.py", line 937, in invoke
    return self.execute(context)
  File "C:\Users\pierre-louis\AppData\Roaming\Blender Foundation\Blender\2.81\scripts\addons\Urho3D-Blender-2_80\__init__.py", line 933, in execute
    ExecuteAddon(context)
  File "C:\Users\pierre-louis\AppData\Roaming\Blender Foundation\Blender\2.81\scripts\addons\Urho3D-Blender-2_80\__init__.py", line 1600, in ExecuteAddon
    ExecuteUrhoExport(context)
  File "C:\Users\pierre-louis\AppData\Roaming\Blender Foundation\Blender\2.81\scripts\addons\Urho3D-Blender-2_80\__init__.py", line 1473, in ExecuteUrhoExport
    Scan(context, tDataList, settings.errorsMem, tOptions)
  File "C:\Users\pierre-louis\AppData\Roaming\Blender Foundation\Blender\2.81\scripts\addons\Urho3D-Blender-2_80\decompose.py", line 2500, in Scan
    DecomposeMesh(scene, obj, tData, tOptions, errorsMem)
  File "C:\Users\pierre-louis\AppData\Roaming\Blender Foundation\Blender\2.81\scripts\addons\Urho3D-Blender-2_80\decompose.py", line 1938, in DecomposeMesh
    DecomposeMaterial(mesh, material, tMaterial)
  File "C:\Users\pierre-louis\AppData\Roaming\Blender Foundation\Blender\2.81\scripts\addons\Urho3D-Blender-2_80\decompose.py", line 1724, in DecomposeMaterial
    tMaterial.twoSided = mesh.show_double_sided
AttributeError: 'Mesh' object has no attribute 'show_double_sided'

-------------------------

1vanK | 2020-01-22 13:40:25 UTC | #8

Exporting materials from Blender 2.8 not implemented yet, becouse in Blender 2.8 internal rederer was removed. You can still use Blender 2.7. Currently I am experimenting with convertig Urho's shaders to Cycles one to one (Unlit and Solid) but I can’t say when I public something

![Urho blender 2.8|690x401](upload://1AVX9Iz9eH4fruvDngV140qNTu0.png)

-------------------------

pldeschamps | 2020-01-23 01:54:05 UTC | #9

@1vanK no worries, there is no hurry.
I guess I can add materials in my urho project, after I have imported the model or in urho editor...

-------------------------

1vanK | 2020-01-26 14:13:22 UTC | #10

Some progress

https://www.youtube.com/watch?v=hxEMVUjbf9U

UPD:
 https://github.com/1vanK/Urho3D-Blender/tree/2_80
data.blend + textures for testing

It is a surprise for me, but custom shaders work not only in Cycle, but also in Eevee

-------------------------

