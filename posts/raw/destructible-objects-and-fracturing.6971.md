evolgames | 2021-08-15 07:04:26 UTC | #1

Was able to make these really nice looking destructible blocks today. Found a fairly quick way to do so that wasn't tedious.
https://youtu.be/omkTRy9J-0s

-------------------------

SirNate0 | 2021-08-15 16:09:36 UTC | #2

How did you do it? A Voronoi fracture of a convex hull? i.e. like this:

https://youtu.be/0_qVjLGuT6E

-------------------------

evolgames | 2021-08-15 17:11:41 UTC | #3

Not exactly. I'm using cell fractured pieces from a cube but all randomly placed and chosen. They won't fit to the same cube again, but they look like they do.

I did:

1. annotation pen (on surface) in blender, scribbled around, then did a cell fracture of annotations to make a bunch of pieces out of it
2. Alt + G set all selected pieces to origin
3. Used a script to batch export all of them at once 
4. Batch renamed them to 1.fbx, 2.fbx, etc
5. Used a simple bash script I made to batch convert to mdl with Asset Importer. This was easier because the filenames could be the ${i} in the script's loop
6. Simple loop to load all mdl's to a table when I might need them
7. On node collision (above a force threshold) I remove the cube, and insert an appropriate number of randomly chosen/placed pieces in its place
8. Lastly, I apply a force that is both a little random and influenced by the impacting body

I think this is great because it's always different and looks fairly real. For my purposes, the whole block can break on impact. I don't need partial fractures or anything. What's nice is I can easily add a ton more pieces without any tedious exporting, importing, or anything like that. I'm going to make a separate list of random tiny pieces and sprinkle those around the exact collision point to make a little extra fancy dust and realism.

Here's the blender batch export script I'm using:
```
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
# <pep8 compliant>

bl_info = {
    "name": "Batch export FBX files",
    "author": "brockmann",
    "version": (0, 1, 0),
    "blender": (2, 80, 0),
    "location": "File > Import-Export",
    "description": "Batch Export Objects in Selection to FBX",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Import-Export"}


import bpy
import os

from bpy_extras.io_utils import ExportHelper

from bpy.props import (BoolProperty,
                       FloatProperty,
                       StringProperty,
                       EnumProperty,
                       CollectionProperty
                       )


class Batch_FBX_Export(bpy.types.Operator, ExportHelper):
    """Batch export objects to fbx files"""
    bl_idname = "export_scene.batch_fbx"
    bl_label = "Batch export FBX"
    bl_options = {'PRESET', 'UNDO'}

    # ExportHelper mixin class uses this
    filename_ext = ".fbx"

    filter_glob = StringProperty(
            default="*.fbx",
            options={'HIDDEN'},
            )

    # List of operator properties, the attributes will be assigned
    # to the class instance from the operator setting before calling.

    # context group
    use_selection_setting: BoolProperty(
            name="Selection Only",
            description="Export selected objects only",
            default=True,
            )

    use_mesh_modifiers_setting: BoolProperty(
            name="Apply Modifiers",
            description="Apply modifiers (preview resolution)",
            default=True,
            )
    axis_forward_setting: EnumProperty(
            name="Forward",
            items=(('X', "X Forward", ""),
                   ('Y', "Y Forward", ""),
                   ('Z', "Z Forward", ""),
                   ('-X', "-X Forward", ""),
                   ('-Y', "-Y Forward", ""),
                   ('-Z', "-Z Forward", ""),
                   ),
            default='-Z',
            )
    axis_up_setting: EnumProperty(
            name="Up",
            items=(('X', "X Up", ""),
                   ('Y', "Y Up", ""),
                   ('Z', "Z Up", ""),
                   ('-X', "-X Up", ""),
                   ('-Y', "-Y Up", ""),
                   ('-Z', "-Z Up", ""),
                   ),
            default='Y',
            )
    global_scale_setting: FloatProperty(
            name="Scale",
            min=0.01, max=1000.0,
            default=1.0,
            )

    def execute(self, context):                

        # get the folder
        folder_path = os.path.dirname(self.filepath)

        # get objects selected in the viewport
        viewport_selection = context.selected_objects

        # get export objects
        obj_export_list = viewport_selection
        if self.use_selection_setting == False:
            obj_export_list = [i for i in context.scene.objects]

        # deselect all objects
        bpy.ops.object.select_all(action='DESELECT')

        for item in obj_export_list:
            item.select_set(True)
            if item.type == 'MESH':
                file_path = os.path.join(folder_path, "{}.fbx".format(item.name))

                # FBX settings
                bpy.ops.export_scene.fbx(
                        filepath=file_path, 
                        use_selection=self.use_selection_setting, 
                        use_active_collection=False, 
                        global_scale=self.global_scale_setting, 
                        apply_unit_scale=True, 
                        apply_scale_options='FBX_SCALE_NONE', 
                        bake_space_transform=False, 
                        object_types={'EMPTY', 'CAMERA', 'LIGHT', 'ARMATURE', 'MESH', 'OTHER'}, 
                        use_mesh_modifiers=self.use_mesh_modifiers_setting, 
                        use_mesh_modifiers_render=True, 
                        mesh_smooth_type='OFF', 
                        use_subsurf=False, 
                        use_mesh_edges=False, 
                        use_tspace=False, 
                        use_custom_props=False, 
                        add_leaf_bones=True, primary_bone_axis='Y', 
                        secondary_bone_axis='X', 
                        use_armature_deform_only=False, 
                        armature_nodetype='NULL', 
                        bake_anim=True, 
                        bake_anim_use_all_bones=True, 
                        bake_anim_use_nla_strips=True, 
                        bake_anim_use_all_actions=True, 
                        bake_anim_force_startend_keying=True, 
                        bake_anim_step=1, 
                        bake_anim_simplify_factor=1, 
                        path_mode='AUTO', 
                        embed_textures=False, 
                        batch_mode='OFF', 
                        use_batch_own_dir=True, 
                        use_metadata=True, 
                        axis_forward=self.axis_forward_setting, 
                        axis_up=self.axis_up_setting
                        )

            item.select_set(False)

        # restore viewport selection
        for ob in viewport_selection:
            ob.select_set(True)

        return {'FINISHED'}


# Only needed if you want to add into a dynamic menu
def menu_func_import(self, context):
    self.layout.operator(Batch_FBX_Export.bl_idname, text="FBX Batch Export (.fbx)")


def register():
    bpy.utils.register_class(Batch_FBX_Export)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_import)


def unregister():
    bpy.utils.unregister_class(Batch_FBX_Export)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_import)


if __name__ == "__main__":
    register()

    # test call
    #bpy.ops.export_scene.batch_fbx('INVOKE_DEFAULT')
```

And a simple bash script
```
#!/bin/bash

for (( i=1;i<117;i++)); do

	/home/evol/BuildGame/bin/tool/./AssetImporter model /home/evol/${i}.fbx /home/evol/BuildGame/Data/Models/Fragments/${i}.mdl -nt -nm

done
```

-------------------------

lebrewer | 2021-08-18 15:37:32 UTC | #4

I've been using this with some success for bigger stuff: https://blendermarket.com/products/ossim/docs

-------------------------

lebrewer | 2021-08-18 15:38:27 UTC | #5

This one is also useful for body parts and less rocky stuff: https://blendermarket.com/products/noisy-cutter

-------------------------

evolgames | 2021-08-18 17:15:24 UTC | #6

Whoa I love the way the cuts look on wood! I'm going to try this with a crate object or something

-------------------------

