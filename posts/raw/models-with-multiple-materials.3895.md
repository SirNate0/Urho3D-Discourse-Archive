Sean221 | 2017-12-29 16:55:56 UTC | #1

I have create a model in Blender and it has two materials attached to it. Ive exported it using reattiva exporter. 
The problem is that i cannot assign both of the materials to the object when i create it.

![ExporterSettings|150x500](upload://fdEY9mba1FhzoLuEFJMz6uLjVvS.PNG)

These are the settings im using

![BlenderGun|690x149](upload://uPGboNLKa5euCiwFGOIqpteWTlB.PNG)

This is what its supposed to look like

![InGame|690x167](upload://nVl7FLuXlNJbBltMEB0TBBGO1rp.PNG)

This is what it looks like in game


Finally here is the code im using to create the model

    	StaticModel* gunObject = gunNode->CreateComponent<StaticModel>();
    	gunObject->SetModel(cache->GetResource<Model>("Models/Gun.mdl"));
    	gunObject->SetMaterial(cache->GetResource<Material>("Materials/Base.xml"));
    	gunObject->SetMaterial(cache->GetResource<Material>("Materials/BarrelStuff.xml"));

-------------------------

Dave82 | 2017-12-29 17:48:07 UTC | #2

Use the overloaded method which takes both the index and the texture.

gunObject->SetModel(cache->GetResource<Model>("Models/Gun.mdl"));
gunObject->SetMaterial(0 , cache->GetResource<Material>("Materials/Base.xml"));
gunObject->SetMaterial(1 ,cache->GetResource<Material>("Materials/BarrelStuff.xml"));

-------------------------

Modanung | 2017-12-30 08:56:21 UTC | #3

And if the geometry id's don't match up with the material slots in Blender, sort the elements by material before export.

[details="Python script for sorting elements of all selected objects by material"]
```
import bpy
    
for ob in bpy.context.selected_objects:
    bpy.context.scene.objects.active = ob
    
    bpy.ops.object.mode_set(mode = 'EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.sort_elements(type='MATERIAL', elements={'FACE'})
    bpy.ops.object.mode_set(mode = 'OBJECT')
```
[/details]

For a single object you can find the menu option under _Mesh_ -> _Sort Elements_ -> _Material_ in Edit Mode.

-------------------------

1vanK | 2017-12-31 15:28:23 UTC | #4

use material list file

-------------------------

