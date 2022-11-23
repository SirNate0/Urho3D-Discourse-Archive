Leith | 2019-02-23 07:03:10 UTC | #1

I've got a model that appears to be 100x too large, due to assimp's FBX importer assuming scale is in centimeters. Today I added code to our AssetImporter tool - first I tried to read the unit scale factor from the fbx file prior to import, but it appears there is no such meta-property in my FBX file - so I added a new option to apply a user-defined scale factor during import (eg -sc 0.01) and enabled the appropriate import flag, but it seemed to make no difference!
[code]
            PrintLine("Applying Unit Scale Factor: "+String(GlobalScale));
            aiSetImportPropertyFloat(aiprops, AI_CONFIG_GLOBAL_SCALE_FACTOR_KEY, GlobalScale);
            flags |= aiProcess_GlobalScale;

            scene_ = aiImportFileExWithProperties(GetNativePath(inFile).CString(), flags, nullptr, aiprops);
[/code]

In frustration, I turned back to Blender. Here is the workflow I found to work for me:
In a new scene, I first import my FBX model, with import scale of 1.
Now I set Units to Metric, and Unit Scale to 0.01 - at this point, my model visibly shrinks in Blender's 3D view by 100 times.
Next, I export the model, with export scale of 1, and "!EXPERIMENTAL: Apply Transform" enabled.
Finally, I run the exported FBX through AssetImporter.
The result is a model that looks correct in Urho3D with no scaling applied at runtime, which ought to make my life a bit easier, as they now comply with the scale of the models used in the samples.
Any animations that I had previously imported, back when I had a scale issue, required no changes - they "just worked" with the scaled-down model (though I think I have no translate keys...)

I just thought this information might be useful for future reference, as it took me a few attempts to get the settings right in Blender.

-------------------------

Modanung | 2019-02-23 08:14:57 UTC | #2

The exporter also has a _Scale_ option.  

Btw, after scaling an _object_ in Blender its scale should be applied using **Ctrl+A S** before exporting.

-------------------------

Leith | 2019-02-24 04:25:02 UTC | #3

I'm still having trouble with baking scale into the geometry - Blender is insisting on injecting a root node (called "Armature") that contains scale.
This is bad for me, specifically because Urho3D's CollisiionShape class applies WORLD scale to rigidbodies attached to an armature:
[quote]
        case SHAPE_CAPSULE:
            shape_ = new btCapsuleShape(size_.x_ * 0.5f, Max(size_.y_ - size_.x_, 0.0f));
            shape_->setLocalScaling(ToBtVector3(cachedWorldScale_));
[/quote]

Personally, I think we're doing it wrong - collision shapes should be querying their parent node for its LOCAL scale, so that any scaling applied to the model is not inherited by collision shapes.
I believe that Bullet called it "local scale" for a good reason - it implies that scale inheritance won't be a problem when attaching (physics objects defined in local space coordinates) to a node hierarchy.
I understand it's not quite trivial to modify CollisionShape.cpp to respect local scale, but at the same time, I don't believe that such a change would break anything in any of our existing samples.

Yes, baking scale to the geometry will solve this problem, but it still makes me wonder why we're applying world scale to physics shapes, which are defined in local space! I personally think we should only be applying localspace scale to collision shapes, ie, the local scale of the immediate parent node (which is typically unit scale, regardless of what scale we applied at the root of the model).

-------------------------

TrevorCash | 2019-02-24 04:23:56 UTC | #4

In my newton integration, collision shape scale is by default scaled by the node's scale. But can be turned off via a call to SetInheritNodeScale(bool enable = false);  in addition to this control, the collision shape also has its own localscale, offset, and rotation parameters.

-------------------------

Leith | 2019-02-24 04:33:29 UTC | #5

I absolutely agree - at the very least we could provide a SetWorldScale method in CollisionShape that can be called on an existing, attached object, to counteract the existing logic.
Personally, I'd rather deal with the issue in CollisionShape class, than have to run various models through the Blender / Maya Gauntlet - we SHOULD be able to diffuse bad art with good code, and not require the art to naturally conform to our expectations.

-------------------------

Leith | 2019-02-24 04:40:07 UTC | #6

Thanks for the heads up about applying scale to geom - I'm still not happy with my workflow, I think there could be a small PR in this for a method in CollisionShape that gives us access to set the local scale on a collision object to whatever we want. This would allow us to attach physics objects defined in local coords to a scaled model, then correct the scale on the attached shapes as a post step, and has minimal impact on the existing logic in CollisionShape class.
I'd rather describe the scale of my model at runtime via xml, than rely on metadata that may not exist, or deal with the art scale piecemeal as part of my workflow.

-------------------------

Valdar | 2019-02-24 06:30:39 UTC | #7


Just FYI, Blender doesn't require you to have an Armature root, though in most cases you would want one (a rigged character for example). If you have simple static geometry that already has an armature, you can select the geometric item in Outliner, go to the object tab, and clear the "Parent" box. That will move the item from being a child of the armature to a root level object. As Modanung mentioned, you may need to apply scale, as well as rotation and location before removing it from the parent.

-------------------------

