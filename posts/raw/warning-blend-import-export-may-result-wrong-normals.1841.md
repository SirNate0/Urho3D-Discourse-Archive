Enhex | 2017-01-02 01:10:35 UTC | #1

AssImp .blend import and Urho3D-Blender export may result wrong normals.

A workaround is to export to .dae/.fbx and then import it with AssetImporter.

Direct .blend import/export, wrong normals:
[img]http://i.imgur.com/wadD2Fh.png[/img]

Workaround, correct normals:
[img]http://i.imgur.com/Ccpnmss.jpg[/img]

I tested it with this viewer: [assimp.org/main_viewer.html](http://www.assimp.org/main_viewer.html)
...to make sure it's a problem with Assimp and not something Urho3D does, and it still happens.
I opened an issue for Assimp:
[github.com/assimp/assimp/issues/816](https://github.com/assimp/assimp/issues/816)

Not sure if Urho3D-Blender uses Assimp, if not it also has this bug.

-------------------------

hdunderscore | 2017-01-02 01:10:35 UTC | #2

Are you using the auto-smooth option? If so, then in that case blender is using a new feature called split normals.

Try the branch in this issue: [github.com/reattiva/Urho3D-Blender/issues/45](https://github.com/reattiva/Urho3D-Blender/issues/45)

-------------------------

1vanK | 2017-01-02 01:10:35 UTC | #3

Maybe assimp and blender importer used differenet methods of triangulation. Try manually triangulation of model before baking of normal map

-------------------------

1vanK | 2017-01-02 01:10:35 UTC | #4

Also check "tagent" flag in exporter

-------------------------

Enhex | 2017-01-02 01:10:35 UTC | #5

[quote="hd_"]Are you using the auto-smooth option? If so, then in that case blender is using a new feature called split normals.

Try the branch in this issue: [github.com/reattiva/Urho3D-Blender/issues/45](https://github.com/reattiva/Urho3D-Blender/issues/45)[/quote]

I have Auto Smooth enabled and disabling it results the same error, so it should be the case.
I'll try the Urho3D-Blender branch.

1vanK - These aren't the problems.

EDIT:
split normals branch solved it.

-------------------------

