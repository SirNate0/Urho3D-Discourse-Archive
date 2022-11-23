Modanung | 2019-01-17 13:54:32 UTC | #1

The indices of geometries/materials seem unrelated to the order in which they are listed in Blender. Is there a way to control their order? Not being able to predict this order is inconvenient.
I'm improving the random pilot/pedestrian generation code for [url=https://github.com/LucKeyProductions/heXon]heXon[/url]/[url=https://github.com/LucKeyProductions/OGTatt]OGTatt[/url].

-------------------------

codingmonkey | 2019-01-17 13:57:58 UTC | #2

did you try this sorting ?

![SortElements|398x469](upload://b2AvJdD6SKzmBhGUJadQGm1iSz6.png)

-------------------------

Modanung | 2019-01-17 13:58:39 UTC | #3

I was not aware of this option, I'll try that. Seems like sorting by material is what I would need. Awesome.
Thanks again!

EDIT: Yep, that's it! Cool; what a relief. :slight_smile:
heXon pilots are now saved to and loaded from a file.

EDIT2: This python script does the same for all selected objects:
```
import bpy

for ob in bpy.context.selected_objects:
    bpy.context.scene.objects.active = ob
    
    bpy.ops.object.mode_set(mode = 'EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.sort_elements(type='MATERIAL', elements={'FACE'})
    bpy.ops.object.mode_set(mode = 'OBJECT')
```

-------------------------

