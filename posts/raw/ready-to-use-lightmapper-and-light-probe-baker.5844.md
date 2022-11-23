Eugene | 2020-02-02 09:45:19 UTC | #1

I have just finished major feature update for Urho3D Rebel Fork aka rbfx and it will be available in rbfx master branch in the nearest future.

*Disclaimer:* I know some people may not be very happy that I'm doing it in rbfx instead of main Urho repository. However, this project was extremely hard on its own, and implementing it in vanilla would have taken much more effort. Feel free to port my work to main Urho repository if you feel like doing it, you will have my support. Porting would be tedious, but totally doable. Currently the code is incompatible with Urho3D master and therefore I don't post this in Code Exchange category.

As you could have guessed, this is integrated lightmapper in Urho (well, almost Urho), something I wanted to get for years. It may be buggy, but it is _not_ some proof-of-concept or sample, this is feature-complete and ready-to-use functional.

![image|674x500](upload://f6i9VpHxHta2Qf1vDclHXQgZifp.jpeg) 

It was inspired by unfinished Atomic Glow, but it shares literally zero lines of code with original work of Josh.

Features:

* Integrated with Urho3D rendering pipeline. The only manual work you have to do in order to bake lightmaps is to specify **LIGHTMAP** shader defines for both pixel and vertex shaders and enable "Bake Lightmaps" for the object. The rest is automatic.

* Supported fully baked lights (both direct and indirect lighting are baked) and baked indirect only. Dynamic lights work as usual. This list may be extended in the future.

* Supported materials and textures. Objects with Emission actually light nearby objects, and objects with transparency cast semi-transparent colored shadows.

* There is integrated utility for automatic lightmap UV generation.

* Supported lightmaps for `StaticModel` with or without LODs and `Terrain`

* Supported lighting of dynamic objects using light probes based on spherical harmonics. If you put light probes in the scene, dynamic objects will receive baked lighting. Note: Zone ambient lighting is applied dynamically on top of baked lighting from light probes.

* Supported environmental lighting from `Zone` fog color or `Skybox`.

* Supported physical smooth shadows if non-zero `Light` radius is set. It is treated as ray spread angle in case of directional light.

* Lightmaps are filtered and seams are stitched.

* Supported per-object resolution scale. Objects with zero "Scale in Lightmap" will contribute to baked lightmaps of other objects, but will not have lightmaps for itself.

* Baked lighting works (or should work) on any platform, but the baking itself is available on Desktop only. If you bake large scenes or use high quality settings, bake in Release. Debug is much slower.

Here is live sample that you can try (doesn't work on mobiles)
There is no dynamic lighting in this scene, everything is pre-computed.
(link may be out-of-date, I'm not going to maintain it forever)
https://eugeneko.github.io/
Baking of this scene took only 11 seconds, so I think I have decent performance.
Note color bleeding from bright objects due to bounced indirect light.
Note changing lighting on the character (the only dynamic object in the scene). Character model is quite dark, maybe I'll disable textures in this sample for more expressive lighting.

Code is merged into master branch of rbfx:
 https://github.com/rokups/rbfx

More screenshots:
![image|669x500](upload://AcNiSzkX53IjxpXorPHjm5f0bW4.jpeg)
![image|668x500](upload://rwZfXD2UZE8RUtF6SqYyyQG6RTK.jpeg) 
![image|671x500](upload://mGR28wTEXU2y4JzVjAqReELWp7u.jpeg) 
![image|668x500](upload://sWqWgoBNhicR0UqT6lZYNitRwC0.jpeg)

-------------------------

Eugene | 2020-01-27 19:48:38 UTC | #2

To prove than this can be used with real scenes, here is baked light for Sponza scene.
All parameters except brightness multipliers are default, quality is high.

Note that baked direct light looks slightly different due to missing gamma correction in Urho shaders.

Only indirect light is baked, 129 seconds to bake in background.
![image|690x406](upload://4P1ygs6nVL2eZixLkKTEzjZudZm.jpeg)

Direct and indirect baked, 127 seconds to bake in background.
![image|690x408](upload://drpR87T1Y6hIEWCYfYrGnGTL99n.jpeg) 

Same, but another camera position. I really like lighting on the banner.
Banner cloth model is hardest for automatic UV generation and it has terrible lightmap UVs with tons of seams, so it's a kind of stress test.
![image|690x408](upload://yGIV5gSPRo3wCI174E8w34yE8ax.jpeg)

Just look at lightmap UVs for banner :laughing:
![image|500x500](upload://nusOynSJihWH3zBzimrsgFwnYdN.jpeg) 
That's why the best UV is one made by artist.

Just as reminder, the best result you can get with simple dynamic lighting is this:
![image|690x405](upload://uVXCseyTBlxgDQL0lXZzlU2vx7J.jpeg)

-------------------------

Lumak | 2020-01-28 01:29:15 UTC | #3

Oh, wow, this looks awesome! Good job, Eugene!

-------------------------

restless | 2020-01-29 12:07:17 UTC | #4

Looks nice and makes me want to try the rbfx even more. Would be very interesting to know performance impact. Like, for example FPS in the Sponza with GLOW system versus simple dynamic lighting.

Thanks for publishing this and keep up good work!

-------------------------

Eugene | 2020-01-29 14:47:54 UTC | #5

Okay, about performance. There are several aspects, so plain FPS comparison won't help here.

1) Lightmaps. They are basically emission textures.
Baked lighting on static objects is rendered as simple textured scene without any lighting. I'd consider it almost zero runtime cost, especially when lightmap textures are relatively small.

2) Light probe sampling. It is done only for dynamic objects. Interpolation is relatively fast (one matrix multiplication per rendered batch). Extrapolation is more expensive, but you could avoid it by careful placement of light probes. Both has amortized constant complexity. However, light probe sampling complexity for spawned or warped object for the first frame grows as `O(N^(1/3))` with number of light probes in the Scene. This part might be optimized in the future, it's not that hard.

3) Now the most painful part. Spherical Harmonics support in Urho renderer pipeline. I have to propagate Spherical Harmonics (27 floats) thru the whole renderer, from `View.cpp` to `Graphics`. Yes, it degrades performance a bit. It can be mitigated by disabling SH in build options. However, you will lose all light gradients from light probes and get only average uniform lighting on the object, just like with `Zone`-s.

The most notable degradation is 25% FPS drop in Debug mode of HugeObjectCount sample even without any light probes placed. This is unavoidable price of spherical harmonics support. I will try to reduce this price in future refactoring. Disable SH in build options if you aren't ready to pay for it.

Unfortunately, Urho renderer pipeline is now very rigid, and I cannot get true "don't pay if don't use" thing.

Still, I believe that high quality global illumination for smaller number of objects is better than no global illumination for more objects.

-------------------------

WangKai | 2020-01-30 16:15:10 UTC | #6

Amazing! This is huge!

-------------------------

Sinoid | 2020-02-06 02:28:16 UTC | #7

@Eugene I know this is nasty, but it would be useful to be able to generate the tetmeshes for a scene from Zone volumes using the zone configurations. Perhaps zone-centroids as absolute values and their corners marked and then determined as SH accumulations along those vectors? I admit I only understand how to do this as a Laplace diffusion and have no idea what this really means regarding SH.

That'd nip any proc-gen concerns in the bud since Zones can be proc-gen'd as well.

---

Great work though, having written a lightmapper myself and dabbled in probes and SH I know how significant this is. From what I've seen it's awesome.

-------------------------

Eugene | 2020-02-06 06:18:56 UTC | #8

I have a dream of retiring Zones, you know, or at least leaving them as Editor-only tool. They add quite a lot of complexity in the renderer and in shaders and they don’t offer anything special — Zones are just crippled un-smooth version of light probe mesh. Or maybe they have use cases I’m not aware of?
Can we somehow replace these use cases too?

-------------------------

