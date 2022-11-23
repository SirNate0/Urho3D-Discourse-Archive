spenland | 2019-12-14 17:58:56 UTC | #1

I'm unable to use the blender exporter since I'm using 2.8, and I can't seem to get my uv and normal maps working. Well, I think the UV is working but the normal map is not. Here is my material file:

    <material>
	<technique name="Techniques/DiffNormal.xml" quality="1" />
	<technique name="Techniques/Diff.xml" quality="0"/>
	<texture unit="diffuse" name="Textures/water_plant_uv.png" />
	<texture unit="normal" name="Textures/water_plant_norm.png" />
    </material> 

Is there something I'm doing incorrectly?

-------------------------

spenland | 2019-12-14 18:07:16 UTC | #2

You know, if there is a version of 2.8 blender that works with the exporter, I'd be glad to use an older version and get the exporter working if it handles the making of the mdl and materials/textures. I just can't go back to 2.7 blender.

So if anyone knows a working version of blender that the exporter works with, that'd be good too.

-------------------------

jmiller | 2019-12-14 23:14:05 UTC | #3

```
<texture unit="diffuse" name="Textures/water_plant_uv.png" />
```

The texture name leads me to wonder. Typically, "Diffuse maps specify the surface color in the RGB channels."
  https://urho3d.github.io/documentation/HEAD/_materials.html

  https://discourse.urho3d.io/t/how-to-read-uv2/5344

@reattiva's 2.8 branch of Urho3D-Blender was working with normals IIRC from when I last used it early Blender 2.8?
  https://github.com/reattiva/Urho3D-Blender/tree/2_80

@dertom's exporter has been working with Blender 2.8, exports normals, but misses some functionality (check gh Issues)
  https://discourse.urho3d.io/t/blender-2-8-exporter-with-addional-features-e-g-urho3d-materialnodes-and-components/5240

-------------------------

spenland | 2019-12-15 17:55:13 UTC | #4

I got the exporter working although I kept getting " 'Mesh' has no attribute 'show_double_sided' " ….I thought since my mesh isn't double sided, I could just set that to false but when I do the resulting mdl file doesn't appear when I put it in my game.

Sooo.. if I export from Blender to get the materials and textures, then use the AssetImporter to convert an fbx to mdl and use all those files, I get a working object in my game But it looks nothing like my Blender file...same normal issue I think.

In Blender:
![in_blender|487x500](upload://z1EsYtY7xLS5lswNj33H6C8TTNK.png) 

<br/>

In Game:
![in_game|532x500](upload://iyqqAeXrawhJem6IqW9I85971J7.png) 

<br/>

I'm using only Textures now in blender, no Materials (I baked them to a diffuse image and a normal image)

-------------------------

jmiller | 2019-12-15 18:28:29 UTC | #5

[quote="spenland, post:4, topic:5764"]" ‘Mesh’ has no attribute ‘show_double_sided’ "[/quote]

I can't recall the exact cause, but think some web search or debugging the exporter can reveal it.

'Apply Modifiers' was broken by Blender 2.8 API changes for both @reattiva exporter and @dertom exporter, so you might try disabling that..

Also, Blender FBX import has usually given me good results.

-------------------------

