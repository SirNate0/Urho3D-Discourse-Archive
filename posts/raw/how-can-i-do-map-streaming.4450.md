tomarlo4 | 2018-08-09 23:00:16 UTC | #1

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/1/1060eb2a7e849a5893c7f861a6daf4071bfc6f46.jpeg'>

how can i do player's 3D area or map/texture load by streaming like this? like a distance of field rendering

to save ram and vram memory in big maps?
thx

-------------------------

Bananaft | 2018-08-16 19:18:31 UTC | #2

https://urho3d.github.io/documentation/1.5/_resources.html

There is asynchronous scene loading functionality. So you can load next location in background and switch to it on the fly.

-------------------------

S.L.C | 2018-08-16 23:48:28 UTC | #3

Is that a screenshot of Rage? IIRC that uses [id Tech 5](https://en.wikipedia.org/wiki/Id_Tech_5) engine with a revised implementation of [MegaTexture](https://en.wikipedia.org/wiki/Id_Tech_4#MegaTexture_rendering_technology) from id Tech 4. That feature seems very specific to that engine. But I'm pretty sure someone dug into it for the fun of finding out how it was implemented and most likely made a detailed blog post about it. Heck, probably even made a demo. People usually do these things because it is quite interesting. Just try a `megatexture implementation` search on google. You are bound to find some leads. Sure, you'll have to do some work too. Don't expect everything on a plate.

https://github.com/PhilCK/mega-texture

-------------------------

anders | 2018-08-17 12:17:05 UTC | #4

this involves LOD, sometimes lod and sync/async render, you would need to first ask how to use lod in urho3d and im curious about this too hahaha'

-------------------------

S.L.C | 2018-08-17 16:22:25 UTC | #5

With the [asset importer](https://urho3d.github.io/documentation/HEAD/_tools.html) tool. You basically tell it to combine several meshes into one file.

https://github.com/urho3d/Urho3D/blob/f8badde1ccec6fd9a7d6b06003c8220f59bb3c1e/Source/Tools/AssetImporter/AssetImporter.cpp#L271

-------------------------

Modanung | 2018-08-18 15:53:20 UTC | #6

Fortunately I made a short video a while back on how to do this using Blender. :)
https://discourse.urho3d.io/t/information-source-how-to-exporting-lods-with-blender/2083
The required Blender plug-in can be found [here](https://github.com/reattiva/Urho3D-Blender). I'm not sure how LODs combine with asynchronous loading, though. You might have to split up the model anyway in order to load different levels of detail in a specific order. I dunno.

-------------------------

lvoml-eternity | 2018-08-17 23:24:04 UTC | #7

"I’m not sure how LODs combine with asynchronous loading, though."
first async, after lod i suppose =S

borderlands have the same system

maybe its about distance too... distance of view or field, maybe?
(rendering by distance is possible? .-.)

a game i forget the name, u enter in a area and the textures load slow or just on time depending of ur HDD, when all is loaded, u go to a mission (that is a elevator), when u go to elevator, the door closes and while ure in the elevator the anterior area is "un-loaded" and the next area is loaded, when the next area appear by the other door in the elevator, textures load slow again, it repeat when u back
always saving memory

this is a good way to never lose performance =D

-------------------------

