daokoder | 2021-06-10 13:22:04 UTC | #1

I am adding procedurally generated caves to my game. But I found it tricky to render them properly. By default, they are only as dark as the ambient color and shadow color when the sun light is on outside the caves.

I read from the documentation that negative lights could be used to make caves dark. But in arbitrarily generated caves, I don't know if it is possible to place negative lights properly to achieve a reasonable effect. Does anyone know how to do this properly with negative lights?

Alternatively, I am considering to use zones inside caves, such that zones near the cave entrances will have lighter ambient color, and zones away from the entrances will have darker ambient color. Then I will also modify the shaders such that shadow colors are properly darkened according to the zone ambient colors. This way I am more or less sure it can produce acceptable results.

But I am curious if there is a better way. Does anyone know how other games (such as Minecraft) handle such problem? Thanks!

-------------------------

Eugene | 2021-06-10 14:03:30 UTC | #2

[quote="daokoder, post:1, topic:6886"]
Does anyone know how to do this properly with negative lights?
[/quote]
I don't consider "negative lights" as sane tool due to the enormous cost and inferior result. May be ok-ish tool to make a couple of blob shadows at the floor or some fancy color-bleeding visual effect, nothing more.

[quote="daokoder, post:1, topic:6886"]
Alternatively, I am considering to use zones inside caves, such that zones near the cave entrances will have lighter ambient color, and zones away from the entrances will have darker ambient color
[/quote]
It will work and will give you ok-ish results. There are "gradient zones" which support automatic linear blending between _two_ zones. The disadvantage is light popping due to discrete zone transitions. Also, zones are boxes, and you may need a lot of padding between interior and exterior. I.e. you cannot make round interior with thin walls: you will have zone bleeding either in or out.

[quote="daokoder, post:1, topic:6886"]
Does anyone know how other games (such as Minecraft) handle such problem?
[/quote]
Minecraft does simplified raytracing and volume tracing on CPU and just bakes lighting into voxel geometry. If you are okay with Minecraft quality of lighting (lack of actual sharp shadows, minor updates only), you can implement it on your own. Basically, flood fill light into your level and keep it in voxels and geometry. Update lighting for dynamic objects on CPU as well.

[quote="daokoder, post:1, topic:6886"]
But I am curious if there is a better way
[/quote]
Global Illumination is tricky. You can try to implement realtime GI, if you target high-end PC only. I think I saw Urho sample with realtime voxel GI somewhere on this forum.

I really like terrahedral interpolation for GI (like Unity does for static ligthing), but it is semi-static: you need to rebuild lookup structure every time you update light probes positions. It would be okay if you generate map only once or change it rarely.

Terrahedral interpolation allows you to smoothly interpolate in almost* arbitrary point cloud of sample points, which can be used for ambient lighting, fog intensity, and whatever else.

-------------------------

daokoder | 2021-06-10 15:41:44 UTC | #3

Thank you very much! This is a really good and informative reply.

[quote="Eugene, post:2, topic:6886, full:true"]
I don't consider "negative lights" as sane tool due to the enormous cost and inferior result. May be ok-ish tool to make a couple of blob shadows at the floor or some fancy color-bleeding visual effect, nothing more.
[/quote]

OK, I will forget about using "negative lights" for this.

[quote="Eugene, post:2, topic:6886, full:true"]
It will work and will give you ok-ish results. There are "gradient zones" which support automatic linear blending between _two_ zones. The disadvantage is light popping due to discrete zone transitions. Also, zones are boxes, and you may need a lot of padding between interior and exterior. I.e. you cannot make round interior with thin walls: you will have zone bleeding either in or out.
[/quote]

Zone bleeding won't be a problem, thin walls can be avoided in my game. I don't know how visible light popping will be, if it can be reduced to a not-very-obvious level, I consider it acceptable.

[quote="Eugene, post:2, topic:6886, full:true"]
Minecraft does simplified raytracing and volume tracing on CPU and just bakes lighting into voxel geometry. If you are okay with Minecraft quality of lighting (lack of actual sharp shadows, minor updates only), you can implement it on your own. Basically, flood fill light into your level and keep it in voxels and geometry. Update lighting for dynamic objects on CPU as well.
[/quote]

I think my game is a lot more sophisticated than Minecraft, I not sure doing all this on CPU would be a good idea in my game. But it's nice to know how Minecraft does it.

[quote="Eugene, post:2, topic:6886, full:true"]
Global Illumination is tricky. You can try to implement realtime GI, if you target high-end PC only. I think I saw Urho sample with realtime voxel GI somewhere on this forum.
[/quote]

I guess GI is the standard way to this. But I am afraid I don't enough time to implement an advanced technique such as realtime GI now. My game update has been long overdue, I am actually trying to find a quick solution, otherwise, I will have to postpone the cave feature to future updates. 

However, I am very interested to support realtime GI in my game when time permits in the future. For the realtime voxel GI, are you referring to this one:
[https://discourse.urho3d.io/t/voxel-cone-tracing-university-project/2457](https://discourse.urho3d.io/t/voxel-cone-tracing-university-project/2457)?

[quote="Eugene, post:2, topic:6886, full:true"]
I really like terrahedral interpolation for GI (like Unity does for static ligthing), but it is semi-static: you need to rebuild lookup structure every time you update light probes positions. It would be okay if you generate map only once or change it rarely.

Terrahedral interpolation allows you to smoothly interpolate in almost* arbitrary point cloud of sample points, which can be used for ambient lighting, fog intensity, and whatever else.
[/quote]

It sounds like a very interesting technique, I will keep it in mind for future reference.

-------------------------

Eugene | 2021-06-10 20:59:54 UTC | #4

[quote="daokoder, post:3, topic:6886"]
I don’t know how visible light popping will be, if it can be reduced to a not-very-obvious level, I consider it acceptable.
[/quote]
As long as you have at most 2 adjacent zones, you can easily (almost) avoid light popping via gradient zones. It may be not trivial how to achieve this in arbitrary generated worlds. You will have to have clear separation between outdoor, indoor, and transition regions.

Or you can forget about transitions and leave light popping as is, some games got away with it.

[quote="daokoder, post:3, topic:6886"]
However, I am very interested to support realtime GI in my game when time permits in the future. For the realtime voxel GI, are you referring to this one:
[/quote]
[This topic](https://discourse.urho3d.io/t/rasterized-voxel-based-global-illumination/2115), but I didn't find it really useful. This is just a prototype, 10% of work done.

[quote="daokoder, post:3, topic:6886"]
It sounds like a very interesting technique, I will keep it in mind for future reference.
[/quote]
[This is the article](https://ubm-twvideo01.s3.amazonaws.com/o1/vault/gdc2012/slides/Programming%20Track/Cupisz_Robert_Light_Probe_Interpolation.pdf). [This is my implementation](https://github.com/rokups/rbfx/blob/master/Source/Urho3D/Math/TetrahedralMesh.cpp).

-------------------------

daokoder | 2021-06-11 15:37:24 UTC | #5

[quote="Eugene, post:4, topic:6886, full:true"]
As long as you have at most 2 adjacent zones, you can easily (almost) avoid light popping via gradient zones. It may be not trivial how to achieve this in arbitrary generated worlds. You will have to have clear separation between outdoor, indoor, and transition regions.

Or you can forget about transitions and leave light popping as is, some games got away with it.
[/quote]

Right, such issues should not be much a problem for certain games. Now I am also considering the option of baking similar information into the geometry, it could be simpler and less problematic.

[quote="Eugene, post:4, topic:6886, full:true"]
[This topic](https://discourse.urho3d.io/t/rasterized-voxel-based-global-illumination/2115), but I didn't find it really useful. This is just a prototype, 10% of work done.
[/quote]

OK, this looks more like it. When I searched for it on the forum yesterday, I didn't notice I was searching only in this category and could only find something marginally matching to what you were referring to. It does look very interesting, could very well suit my game, but unfortunately it is still incomplete and no longer in active development.

[quote="Eugene, post:4, topic:6886, full:true"]
[This is the article](https://ubm-twvideo01.s3.amazonaws.com/o1/vault/gdc2012/slides/Programming%20Track/Cupisz_Robert_Light_Probe_Interpolation.pdf). [This is my implementation](https://github.com/rokups/rbfx/blob/master/Source/Urho3D/Math/TetrahedralMesh.cpp).
[/quote]

Cool, you already implemented this :+1:. Curious, I couldn't find out how light probe data is computed in your implementation. I could be looking at the wrong places since I am quite new to the technique. I would be very interested to use it my game if it is easy enough to adapt :grinning:

-------------------------

Eugene | 2021-06-11 17:02:22 UTC | #6

[quote="daokoder, post:5, topic:6886"]
I couldn’t find out how light probe data is computed in your implementation.
[/quote]
File that I referenced is just a generic data structure for interpolation in point cloud.
How do you make this point cloud is up to you.

I have implemented raytracer for baking light probes from scene geometry and lights using Embree SDK, but it won't be easy to adapt in your project, *especially* if you want it in post-deployment time (=on player's machine instead of developer's one).

You may want to implement/take interpolation structure and fill light probes in less accurate and more robust way, i.e. by some heuristic algo in the code that generates your game world.

Note that tetrahedral interpolation can work in real-time only on "small" objects. Cave walls itself cannot use it for lighting. You will have more luck with baking cave walls ambient into vertex data (coarse but simple) or into lightmap textures (more details, may not worth the trouble).

-------------------------

daokoder | 2021-06-11 18:04:11 UTC | #7

[quote="Eugene, post:6, topic:6886, full:true"]
File that I referenced is just a generic data structure for interpolation in point cloud.
How do you make this point cloud is up to you.

I have implemented raytracer for baking light probes from scene geometry and lights using Embree SDK, but it won't be easy to adapt in your project, *especially* if you want it in post-deployment time (=on player's machine instead of developer's one).
[/quote]

I also briefly looked into the project that contains that file, I noticed it included some other source files related to the feature, so I began to wonder if your implementation covered everything I need. Good to know that is not the case.


[quote="Eugene, post:6, topic:6886, full:true"]
You may want to implement/take interpolation structure and fill light probes in less accurate and more robust way, i.e. by some heuristic algo in the code that generates your game world.

Note that tetrahedral interpolation can work in real-time only on "small" objects. Cave walls itself cannot use it for lighting. You will have more luck with baking cave walls ambient into vertex data (coarse but simple) or into lightmap textures (more details, may not worth the trouble).
[/quote]

OK, I will try to figure out how to do these in my game. It seems every approach will take quite a while to implement, so I think I will postpone the cave feature at the moment, and focus on finishing other parts of the current update.

I will resume the cave feature for another big update. Thank you very much for all your advices, they are very helpful.

-------------------------

