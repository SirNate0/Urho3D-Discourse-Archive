smellymumbler | 2017-04-19 06:24:43 UTC | #1

So, i'm currently using a set of modular meshes to build my game levels. Instead of using the Urho3D editor, i'm using Blender because i want to leverage Cycles to bake a high-resolution lightmap for the level. Unfortunately, I can't find a way of using the baked lightmap texture for my level inside Urho.

How are you guys doing this? Is there any sample laying around?

-------------------------

rasteron | 2017-04-17 23:34:50 UTC | #2

Just name the second uv map which will be your lightmap(s) to `_UV2`, then export with reattiva's Blender exporter and set the technique to DiffLightMap.xml, that's all there is to it.

Note: the exporter will set the lightmap technique but just in case..

-------------------------

smellymumbler | 2017-04-18 14:36:24 UTC | #3

I didn't know this exporter, i was exporting COLLADA from Blender and then using Urho's tools. Thanks a lot! I'm going to leave the link here for other people: https://github.com/reattiva/Urho3D-Blender

Does the PBR pipeline support this lightmapping technique? I'm also curious about the object itself: if i need to use the same object in another level, can i safely bake another map, put it in UV2, and call it a day? So i can have modular meshes loaded separately, but a single diffuse for lightmap that i can switch at will?

-------------------------

Sinoid | 2017-04-19 00:11:48 UTC | #4

> Does the PBR pipeline support this lightmapping technique?

Technically "yes." accurately, no.

Baking for PBR is more involved as you need to capture the directional component for specular response apart from just the diffuse response, the application of the lightmap then needs to go through its paces so the two are balanced correctly.

If Filmic Blender also applies to Blender's baking and not just final renders then it's probably doable from cycles with some math misery so the blender and R/T render sides are happy, as long as the desired method is simple (HL2-RadNorm or Amb+Dir).

> I'm also curious about the object itself: if i need to use the same object in another level, can i safely bake another map, put it in UV2, and call it a day?

Yes. Though batching isn't set up with lightmapping in mind, and it's not really possible without a set in stone "this is how lightmaps shall be."

-------------------------

rasteron | 2017-04-19 00:12:21 UTC | #5

Sure thing, as for mixing lightmaps with other materials or techniques like PBR, apparently you can only do the standard diffuse thing and with alpha clip (i.e. lightmapped trees/vegetation). Maybe post a feature request for it. would be nice to have a lightmap + normal map technique first though..

> if i need to use the same object in another level, can i safely bake another map, put it in UV2, and call it a day? So i can have modular meshes loaded separately, but a single diffuse for lightmap that i can switch at will?

seems no problem with that if you are just switching texture or material by code or scene settings.

-------------------------

smellymumbler | 2017-04-19 01:32:21 UTC | #6

Oh, so i can only bake lightmaps for models that have simple diffuse-based materials? No specular, normal, etc? 

That's a bummer. :(

-------------------------

Sinoid | 2017-04-19 01:53:58 UTC | #7

@rasteron
> Maybe post a feature request for it. would be nice to have a lightmap + normal map technique first though..

There's little difference between lightmaps that work with normal maps and those that work with PBR, they both have the same issue of needing some information about the directions of the incoming light.

> Oh, so i can only bake lightmaps for models that have simple diffuse-based materials? No specular, normal, etc?

In PBR the lightmap is applied in a fashion similar to Zone color. You can use it, but it is not ideal - it will still probably be better than no lightmap. 

The lightmap contribution will appear like the surface is 100% rough, and will not have a specular highlight for any angle of view. For the most part the rest of PBR will overpower the lightmap, but if the lightmap is intended to be the primary light-source it won't work.

-------------------------

rasteron | 2017-04-19 07:24:21 UTC | #8

@Sinoid ah good to know as it seems to be the case.

[quote="smellymumbler, post:6, topic:3021"]
Oh, so i can only bake lightmaps for models that have simple diffuse-based materials? No specular, normal, etc? 

That's a bummer. :frowning:
[/quote]

I see there are some references and maybe a few tutorials out there if you did some search, so let's just say the engine is capable but the technique is missing. ;)

-------------------------

smellymumbler | 2017-04-19 23:33:53 UTC | #9

Thank you! Unfortunately, i'm not that good with graphics. Guess i'll just ignore lightmaps for now. :D

-------------------------

