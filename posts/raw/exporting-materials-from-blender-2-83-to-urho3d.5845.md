1vanK | 2020-05-13 09:33:29 UTC | #1

Need some tests before PR if anyone is interested in this: <https://github.com/1vanK/Urho3D-Blender/tree/2_80>

https://www.youtube.com/watch?v=O0h12-2Hnq0

Notes:
* Requires latest version of Blender 2.83 Alpha <https://builder.blender.org/download/>
* `Render Properties > Color Management > Display Device = None` to match colors Blender and Urho
* You need clone material from library to be able to edit material
* PBR materials not implemented yet
* If you wrote your own Urho's shaders, you can add own node trees to addon\data.blend and append expoter to addon\materials.py (syntax very easy)

Important:
You can not use any cycles material. You need clone and tune predefined materials wich corresponds to existed Urho’s shaders.

-------------------------

WangKai | 2020-01-30 16:22:04 UTC | #2

Cool feature! Obviously a lot of work.

-------------------------

johnnycable | 2020-01-31 16:53:34 UTC | #3

Can it work with 2.82 beta?

-------------------------

1vanK | 2020-01-31 17:06:20 UTC | #4

Theoretically yes, but I have not tested. This exporter uses new `compare` node https://wiki.blender.org/wiki/Reference/Release_Notes/2.82/Cycles

-------------------------

Avagrande | 2020-09-29 17:50:45 UTC | #5

I wrote something like this for my own exporter. It saves images too. 
It currently only supports 3 shader types, but I hope this helps anyone who might want to continue working on this. 
https://gist.github.com/Polynominal/2236e2b28d9114e35fcce50eb4dcff54

-------------------------

