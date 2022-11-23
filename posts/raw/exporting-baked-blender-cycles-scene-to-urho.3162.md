darkirk | 2017-05-26 02:39:48 UTC | #1

I just saw this nice Blender technique: https://www.youtube.com/watch?v=sB09T--_ZvU

And i would love to know how it would be possible to export that scene to Urho. Which built-in material supports that? Also, how big can the scene be?

-------------------------

rasteron | 2017-05-25 23:22:23 UTC | #2

Hey darkirk,

You can check out my Blender Simple Lightmap Export example if you're new to exporting scenes or models with lightmaps. This is using reattiva's exporter addon: https://github.com/reattiva/Urho3D-Blender

https://discourse.urho3d.io/t/blender-simple-lightmap-export/3065

-------------------------

darkirk | 2017-05-26 15:41:53 UTC | #3

Thanks for the help! I have a few questions about your technique:

* Do you assign the lightmap texture to each and every model in the scene? 
* Does it blend well with realtime soft shadows for physics-enabled objects? Such as boxes, doors, etc.
* How big can the lightmap texture be? 4096? 8192?
* How big can the scene be? Is there a limitation?
* Is it possible to use multiple lightmap textures to account for a bigger scene? Or should i just split scenes into different models in Blender?

-------------------------

Lumak | 2017-05-26 23:05:42 UTC | #4

Have you looked at Atomic Game Engine, specifically the AtomicGlow, https://discourse.atomicgameengine.com/t/atomic-glow-work-in-progress/281 

I haven't played with it but it seems to be coming along very nicely:

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/0ea9e658ad04184854e9c93a5881e6750fca9e89.png'>

-------------------------

darkirk | 2017-05-26 23:03:35 UTC | #5

Is it like a paid engine? On top of Urho?

-------------------------

Lumak | 2017-05-26 23:06:44 UTC | #6

It used to be a paid model but Josh did away with that about a year ago and it's now MIT license.  And yes, core is Urho3D.

-------------------------

rasteron | 2017-05-27 01:49:43 UTC | #7

* That depends on your setup. If you want to optimize your scene then you can use some type of texture atlasing.
* You can match the shadow color with your baked lighting (I posted an old experiment on this, see link below) and maybe use/write some custom shaders so they blend well and not overlap.
* This depends on your target platform and how much detail you want for your scene.
* Big enough I guess and you can do away with some optimization like LOD, billboarding, etc.
* Of course and again this depends on your setup. Probably merge your static models and use less lightmaps as possible.

https://discourse.urho3d.io/t/static-dynamic-shadows/1660

-------------------------

darkirk | 2017-05-27 14:41:45 UTC | #8

Since the scene is all one big mesh, can i apply frustum culling on submeshes? What about LODing?

-------------------------

rasteron | 2017-05-28 12:55:13 UTC | #9

I'm not quite sure and it would be better if you just try it out. Here's also a link to the rendering doc.

https://urho3d.github.io/documentation/1.5/_rendering.html

> Note that many more optimization opportunities are possible at the content level, for example using geometry & material LOD, grouping many static objects into one object for less draw calls, minimizing the amount of subgeometries (submeshes) per object for less draw calls, using texture atlases to avoid render state changes, using compressed (and smaller) textures, and setting maximum draw distances for objects, lights and shadows.

-------------------------

darkirk | 2017-05-30 17:12:53 UTC | #10

Thank you so much for the attention. :)

-------------------------

