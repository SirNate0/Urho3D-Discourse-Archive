smellymumbler | 2017-04-26 03:54:08 UTC | #1

I've recently discovered WorldMachine [through this](https://www.youtube.com/watch?v=8uZGUsfjrbw) amazing tutorial and i was trying to reproduce the workflow with Urho. I successfully managed to import the heightmap and apply a single diffuse texture to the terrain. It looks great from a distance and i'll definitely used it to add more detail to the level. 

Unfortunately, it doesn't look very good at a close distance or using a first-person camera. The texture gets blurry and it is very hard to get any detail. Has anyone used WM with Urho before? How would you guys add more detail to the terrain?

-------------------------

rasteron | 2017-04-26 04:49:07 UTC | #2

You can generate [TerrainWeights](https://github.com/urho3d/Urho3D/blob/master/bin/Data/Textures/TerrainWeights.dds) using WorldMachine so you can add up to 3 diffuse texture variations like what you see in the terrain example. 

Try and check out the Basic Splatmap macro here:
http://www.world-machine.com/library/index.php?entry=73&focus=1

The default terrain shader only uses RGB channel or 3 diffuse textures so you can probably just ignore the alpha channel which looks like a slot for the erosion map there.

Hope that helps.

-------------------------

Victor | 2017-04-26 16:56:49 UTC | #3

Speaking of WorldMachine, I've used it for Urho for a while now, but I think http://www.quadspinner.com/GeoGlyph might be a better solution as WorldMachine seems to be a bit slow in their next release. The workflow should be mostly the same.

Sorry if that was a bit off-topic, but I thought I'd throw that in there for those looking to use WM.

-------------------------

smellymumbler | 2017-04-26 19:17:23 UTC | #4

@Victor, certainly not. Thanks for the link! I'll check this tool as well, it looks really good.

@rasteron, thanks for the tip. Is it possible to have 3 materials instead of 3 diffuses? That way i can use normals and also detail textures to make the whole thing less blurred.

-------------------------

Victor | 2017-04-26 20:20:08 UTC | #5

You could generate multiple splatmaps (SplatA, SplatB, ...) for a single terrain, and send those to your terrain shader. The shader could then use those splatmaps to paint textures onto your terrain. If you utilize the A channel, you could have 4 textures per splatmap. I hope that helps.

**Edit** 
Actually, I think I misunderstood the question. As far as I know, only 1 material for a terrain in Urho, but that shouldn't stop you from having a lot of detail on your terrain. I believe if you did use multiple splatmaps to paint your textures on the terrain, utilize TextureArray for the shader, that would help a great deal. It shouldn't effect defining a normalmap or even an AO map for your terrain. (http://urho3d.wikia.com/wiki/Terrain_Shader_with_normal,_specular_and_height_mapping)

-------------------------

smellymumbler | 2017-04-26 20:14:01 UTC | #6

But still, the terrain will only have one texture pass with those 3 channels. Or are they not related? Can i apply multiple materials on a same terrain, like a layer-based system?

-------------------------

rasteron | 2017-04-27 05:17:50 UTC | #7

[quote="smellymumbler, post:4, topic:3050"]
@rasteron, thanks for the tip. Is it possible to have 3 materials instead of 3 diffuses? That way i can use normals and also detail textures to make the whole thing less blurred.
[/quote]

No prob and as Victor mentioned, the default terrain only uses one material and these textures, though you're not limited to enhance and modify it by source or shaders. If you're going for the default route then the link resource (by gawag) that he posted also works in GLSL and desktop only, last time I tested.

-------------------------

smellymumbler | 2017-06-05 17:28:59 UTC | #8

I eventually went with this approach: https://kosmonautblog.wordpress.com/2017/06/04/terrain-rendering-overview-and-tricks/

I export multiple splatmaps from WorldMachine, covering all the layers of materials that i might have. And i render the terrain once per splatmap. I have 5 splatmaps now and it works great.

-------------------------

