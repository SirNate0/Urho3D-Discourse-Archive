Florastamine | 2018-03-04 16:17:46 UTC | #1

I have a mini-game for my game in which the player has to paint a lot of decals. The decals are randomly chosen from a pool of images. Problem is, a `DecalSet` can only hold a single decal material, and that left me creating a lot of `DecalSet` components whenever I want to paint a decal, because the decals are different and not using that same single material. Performance considerably dropped down.

0 decal:
![image|690x387](upload://vKontUSTAZugFLPSNErRHrWB5iA.png)

50+ decals, the time spent during `Render/Present` increased a lot:
![image|690x387](upload://bydh2uxLu8Bn4EUQdWVn43zBE1t.png)

Is there any workaround? I know I can customize `DecalSet` into something else, i.e. `LightDecalSet` which optimizes for only one decal, but I'd like to know what I've been missing. 

Thank you!

-------------------------

Eugene | 2018-03-04 17:06:30 UTC | #2

Maybe back them into the atlas?
Do you _really_ need multiple materials, or just multiple textures?

-------------------------

Sinoid | 2018-03-04 17:19:28 UTC | #3

Or use a texture array if it's just the textures you care about and tweak the shader so you can use [UDIM](https://www.fxguide.com/featured/udim-uv-mapping/) or your own convention.

Arrays are less hassle than texture atlases but do require all decals be the same resolution.

-------------------------

Florastamine | 2018-03-05 13:49:12 UTC | #4

Thank you both @Sinoid, @Eugene for your suggestions.

@Eugene
[quote]Do you really need multiple materials, or just multiple textures?[/quote]
Yes, what I really want is multiple textures. But I totally forgot about using atlases, thank you! So I packed up all my textures with `SpritePacker` and manually specifying UV coords during `DecalSet::AddDecal()` to only paint what I need. That works wonderfully, and I don't have to deal with having to create a crazy amount of `DecalSet` anymore.
![image|412x500](upload://6pTTEqUYCYIMRL9xnpHT2lc31sx.png)

It surely performs better than the last time, scoring 70+ fps with 90 decals, performance loss is minimal:
![image|690x387](upload://qG1ZV4Zuti4LwhsEKgjgGBrHo0I.png)

@Sinoid I digged the documentation and it seems like Urho has some sort of support for texture arrays (`Texture2DArray`), but I'm pretty confused on how to use it. Was it the texture array thingy you were talking about?

-------------------------

Eugene | 2018-03-05 14:07:16 UTC | #5

[quote="Florastamine, post:4, topic:4074"]
but I’m pretty confused on how to use it
[/quote]

1. Make texture array resource combined of all needed textures.

2. Make custom shader that is able to sample these textures according to some ID

3. Somehow pass this ID along with decal into DecalSet

Pros:

- No edge bleeding issues

Cons:

- Harder to maintain
- Same texture size for each texture

-------------------------

Florastamine | 2018-03-05 14:21:39 UTC | #6

Alrighty then, I guess I won't be touching that anytime soon, I suck so hard at shaders XD. The atlas solution works great atm and that's just fine by me.

-------------------------

