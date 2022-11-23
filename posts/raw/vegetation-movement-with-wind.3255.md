darkirk | 2017-06-15 20:15:03 UTC | #1

Anyone has any idea on how do to something like this in Urho?

https://www.youtube.com/watch?v=_2sx6JPdlmw

-------------------------

Victor | 2017-06-15 20:46:21 UTC | #2

Hey there!

Both Lumak and Eugene have excellent examples here:

https://discourse.urho3d.io/t/10-000-grass-nodes/2394?source_topic_id=2894

https://discourse.urho3d.io/t/procedural-vegetation/2168

I hope those are helpful :)

-------------------------

darkirk | 2017-06-15 22:27:15 UTC | #3

Lumak seems to be manipulating the vertices directly: https://github.com/Lumak/Urho3D-Geom-Replication/blob/master/Source/Samples/62_GeomReplicator/StaticScene.cpp#L265

Wouldn't that be more efficient as a vertex shader?

-------------------------

Lumak | 2017-06-15 22:38:58 UTC | #4

You're probably right and you'd be better off using Eugene's procedural vegetation for your needs. My repo, as the title implies, focuses on geom replication as to avoid creating each grass per node, but can be used for trees, rocks, boxes, w/e you need.  This came about after watching someone's youtube vid of implementing thousands of grass nodes which ran... can't remember, maybe 15 fps.

-------------------------

darkirk | 2017-06-16 01:09:22 UTC | #5

But why? I mean, i'm not looking for procedural generation. I'm creating my vegetation assets by hand and i just want to add the wind effect to them.

-------------------------

Lumak | 2017-06-16 01:35:37 UTC | #6

It'll be sweet if you can write a shader for the wind effect. I'm looking forward to it :)

-------------------------

darkirk | 2017-06-16 01:53:12 UTC | #7

Unfortunately, my shader-writing skills go as far as UE4's material editor allows me. :(

-------------------------

Eugene | 2017-06-16 06:52:50 UTC | #8

I used procedural generation because wind shader requires additional vertex information.
You may try to rewrite my shader or you may generate these vertex data in addition to your geometry.

-------------------------

Alex-Doc | 2017-06-16 07:56:14 UTC | #9

I'm also planning to add wind in my game too (in a later moment).
I would use the vertex colors to map the displacement weight for the wind, as it seems to happen in here: https://developer.nvidia.com/gpugems/GPUGems3/gpugems3_ch16.html

@Eugene can you please tell me which additional vertex data you used?

-------------------------

Eugene | 2017-06-16 08:49:20 UTC | #10

Huh, let me recall...

Wind system was partially stolen from Unity.
The wind consists of the following parts:

1. Main wind controls tree bending caused by wind.
  `main_wind = main_magnitude + oscillation_magnitude * wave_function(time * oscillation_frequency)`
2. Turbulence controls branches waving up-down.
3. Foliage waving is somehow computed... 

Then, vertex parameters:

1. Base magnitude controls the influence of main wind. Magnitude is zero at the ground.
2. Turbulence magnitude and frequency control the influence of turbulence wind. Magnitude is zero at the trunk.
3. Foliage oscillation magnitude and frequency control the intensity of leaves trembling. Magnitude is zero at the branch.
4. True normal of geometry used to wave leaves. If you don't use normal hacks for better foliage shading, you may just use normals instead.

-------------------------

rasteron | 2017-06-16 09:48:15 UTC | #11

[quote="darkirk, post:5, topic:3255, full:true"]
But why? I mean, i'm not looking for procedural generation. I'm creating my vegetation assets by hand and i just want to add the wind effect to them.
[/quote]

If you just need basic wind effect on your vegetation, there's already one example available that comes with the default materials and options in shader (Vegetation.glsl/hlsl), which should be enough, unless you're looking for something else or better.

https://github.com/urho3d/Urho3D/blob/master/bin/Data/Materials/MushroomWind.xml

-------------------------

darkirk | 2017-06-16 13:43:58 UTC | #12

I'm using CryEngine's technique for painting wind effect strength on vertexes: http://docs.cryengine.com/display/SDKDOC2/Detail+Bending

I' m going to try to modify the mushroom to read that info when applying wind. Thanks for the tip.

-------------------------

sampad1370 | 2017-06-19 11:46:18 UTC | #13

Hi @darkirk
Are you solve your problem?
I interested to know what result!
thanks you.

-------------------------

darkirk | 2017-06-19 13:55:33 UTC | #14

Nope. I'm still learning about shaders and how to read vertex data such as colors painted in Blender. If i have some real progress, i'll post here.

-------------------------

sampad1370 | 2017-06-19 23:13:19 UTC | #15

Thank you @darkirk
I hope you get fast and good progress in those topic...
best regards.

-------------------------

