Modanung | 2017-12-30 08:55:51 UTC | #1

I just found out how easy it is to create macros in Blender. Here's how:

https://vimeo.com/168983330

The python script below sorts the elements of all selected objects by material. This makes geometry indexes in Urho3D correspond with the object's list of materials in Blender. Without macros this would be quite tedious and time-consuming work if you need to do it for many objects.

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

-------------------------

