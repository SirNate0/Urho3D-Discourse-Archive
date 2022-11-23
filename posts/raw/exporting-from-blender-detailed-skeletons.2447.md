slapin | 2017-01-02 01:15:26 UTC | #1

Hi all!

As everybody knows, general character skeleton can contain lots of bones.
For example each hand is 20 bones each, head rig, hair rig, clothes rig, feet
are all quite detailed, and if we shortcut by reducing number of animatable fingers, etc. this is easily noticeable
by player. While many people say that "your player have too much time to notice things in your game" and
"you don't ever need so many bones" are pure bullshit and lack of eyesight. We generally don't make graphics for blind people,
and what other thing player do except watching out animations, even heavy on fight? Also to notice, not all genres contain fight
even.
So as I justified the need for > 20 bones ([i]sorry for including the above part, but I really tired of explaining obvious things each time I ask about this problem[/i]), how do we handle the problem? The actual skeletons can contain many bones,
the problem is bone-per-mesh value should not be > 20. First I thought it was per [i]VertexBuffer[/i] value, so I tried to cheat
using different materials, so having material groups split mesh, but that doesn't work at all.

What works is actually [b]splitting mesh[/b]. So if we split-out dense areas (hands, feet, head, ...) we're fine. And yes, that works.
But there is problem - visible seam, which happens because normal smoothing in Blender is disrupted by splitting.
The fixing probably can be done in script code if splits are done in places, where normals end-up quite close even after split,
i.e. when we split not at wrist but spilt forearm in half. This way we can detect same vertices throughout the meshes and averaging their normals (making them the same). [b]This is slow, though, and all the data is known at export time.[/b].

So the question is - why not autosplit the mesh in exporter? This should be easy enough. Also I think this can be done
by loader, too, or by engine tools. We know all bone groups, so we can split mesh by bone groups and then join closest in 20
counts. That would let me avoid doing routine work in Blender then slow work in script.
Doesn't it sound like a good idea? Where to go with it?

-------------------------

rasteron | 2017-01-02 01:15:29 UTC | #2

This looks like a feature request with Blender Urho3D exporter. You can just post an issue to reattiva's repo and make the request..

[github.com/reattiva/Urho3D-Blender/issues](https://github.com/reattiva/Urho3D-Blender/issues)

-------------------------

