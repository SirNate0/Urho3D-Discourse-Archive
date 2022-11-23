davemurphy | 2018-02-09 16:57:52 UTC | #1

In the engine is it possible to animate an AnimatedModel without having a skeleton attached? I have no need to modify these animations in the engine, just play them back.

For example, if I wanted an artist to create an animation for an ‘exploded view’ of a machine, what is the best way for them to create that animation and import it into Urho3D? I know that they can create a root node for the model and then create a child bone for every machine component in the machine (with 100% vertex weights), but a skeletal animation seems like the wrong tool for this.

In Blender I can create a scene with a few objects, transform them, and give them keyframes for the animation, all with no bones and not morphing the shapes. When I export these animations into mdl and ani files, the animation contains the keyframes but can’t be played back because my objects have no bones to assign as the root bone of the animation. Animations in the blend file can be played in Unity, so does Unity basically create a one bone per object automatically on blend file import, or is the animation played another way?

Thanks.

-------------------------

Lumak | 2018-02-09 21:27:34 UTC | #2

Something like this? https://discourse.urho3d.io/t/my-untitled-game-progress-videos/3327/5?u=lumak

The turret in the pic is imported using a "node" option in AssetImporter to maintain a hierarchy order and I take it apart in game.

-------------------------

Sinoid | 2018-02-09 21:32:34 UTC | #3

Edit: didn't know about the stuff Modanung referenced, that looks ideal.

---

There's AttributeAnimation and ObjectAnimation (a collection of attribute-animations) which can animate most attributes. I don't believe the Assimp based converter has support for exporting those.

They can be loaded from Xml/Json files [see source,
 ObjectAnimation.h](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Scene/ObjectAnimation.h), example 30_LightAnimation shows how to set them up in code.

The simplest way to do that would be to use [Reattiva's Blender exporter](https://github.com/reattiva/Urho3D-Blender) and use the [Prefab mode](https://github.com/reattiva/Urho3D-Blender/blob/master/guide.txt#L281) such that each part is a separate object. You would have to add the capability in Python for the exporter to output ObjectAnimation.xml/json for each object track in Blender.

The process for getting the key info should be the same as for the bones.

> Animations in the blend file can be played in Unity, so does Unity basically create a one bone per object automatically on blend file import, or is the animation played another way?

They have a similar (though slightly more robust, IIRC there's no blending/mixing still) object/attribute animation system so they probably just load Blender's object-keys into that.

-------------------------

davemurphy | 2018-02-12 18:48:49 UTC | #5

Thanks @Sinoid, I'll take a look at extending the Blender exporter.

It looks like the @Modanung post has been deleted, can you give an overview if you remember?

-------------------------

Modanung | 2018-02-12 19:45:53 UTC | #6

It kind of felt like a double mention...
https://discourse.urho3d.io/t/export-animated-node-transforms-to-urho3d/1067

-------------------------

