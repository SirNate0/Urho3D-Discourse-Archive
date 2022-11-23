rico.decho | 2017-04-21 14:49:19 UTC | #1

I need to implement this feature for my game, for its integrated level editor.

I'm planning to use Thekla's Atlas Generation Tool and  Ands' Lightmapper C++ libraries, which are exactly what I need.

1st question : is this feature already implemented in Urho3d, and I've missed it ?

2nd question : if not, is this already planned, or has somebody already started to do it ?

3nd question : if not, can somebody give me clues on how to use these two libraries within Urho3D, as I'm new to Urho3D and I'm a not a graphics programmer, so I would need some advices...

Links:

https://github.com/ands/lightmapper
https://github.com/Thekla/thekla_atlas

-------------------------

Enhex | 2017-04-21 16:25:29 UTC | #2

1. It isn't implemented in Urho, tho there's support for doing it.

2. Few people did lightmapping using different approaches.

3. The simplest approach is to bake lightmaps inside Blender, tho it requires you to have fairly small scene since blender doesn't handle multiple texture files. Blender also doesn't handle "lumels" - maintaining consistent lightmap world pixel size.
If you're going to use the lightmapper lib you could try to find and use some offline renderer that can do light bouncing (global illumination) to get good results. I wouldn't recommend using Urho's renderer for this task.

-------------------------

Mike | 2017-04-21 17:23:53 UTC | #3

You can have a look at [Atomic](http://discourse.urho3d.io/t/atomic-game-engine-mit-urho3d-fork/643/105)

-------------------------

rico.decho | 2017-04-22 10:37:11 UTC | #4

Thanks, that's exactly what I need !!

This is for a rudimentary in-game level editor, so the Blender solution is not possible, but Embree + Thekla Atlas should be fine. 

At least now I have some sample code to learn from, so thanks again :)

-------------------------

oschakravarthi | 2019-04-26 05:35:26 UTC | #5

Hi @rico.decho,

Could you find out any solution for baking lightmaps offline programatically?

Thanks in advance.

-------------------------

green-zone | 2019-04-26 07:20:26 UTC | #6

https://discourse.urho3d.io/search?q=lightmap

Atomic-Glow lightmapper port for Urho3D
Only direct lighting is ported:
https://github.com/eugeneko/Urho3D/tree/atomic-glow
Other:
https://github.com/Lumak/Urho3D-Lightmap
Or:
https://www.youtube.com/watch?v=3rZB1otdQqI

-------------------------

