suppagam | 2019-07-18 01:26:40 UTC | #1

Does anyone know how rendering grass blades on specific parts of a terrain texture would work in Urho? 

http://i.imgur.com/d9IndGQ.jpg

I imagine it would need a mask texture, of course, but how do I read the mask and instantiate the objects on those areas? Is there a `SetDetailLayer` equivalent for Urho's terrain object?

-------------------------

guk_alex | 2019-07-18 08:00:54 UTC | #2

I can imagine that it could be done via particles with the grass intensity being described as some sort of heat-map.

-------------------------

JTippetts | 2019-07-18 11:37:39 UTC | #3

You could use your weight map texture for a mask. The TerrainBlend texture uses a weight map to describe how to splat the terrain textures, so you could just load a copy of that texture CPU-side, and query pixels directly to determine where to instance your grass.

-------------------------

suppagam | 2019-07-18 13:46:59 UTC | #4

Thanks! But how do you read the mask black vs. white pixels in Urho? And what object do I instantiate? Do I have to create my own object with quads, or is there a built-in way of doing grass efficiently?

-------------------------

JTippetts1 | 2019-07-18 15:21:14 UTC | #5

There is no built in way of doing grass, outside of the usual static meshes and mesh groups. You can go off into the weeds with shell/fur rendering, volume rendering, etc... but that will all take a bit of custom development and probably a few hours spent reading theses and siggraph papers. I did a brief experiment with a scheme that uses a static mesh of billboards constantly centered on the player (thread: https://discourse.urho3d.io/t/grass-vegetation-mapping/4623 repo: https://github.com/JTippetts/Urho3DGrassTest ) with mixed results. With a bit of artistic finesse it could maybe be made to work.

As far as querying the weight map, that is a simple matter of loading the map into an image and sampling a pixel directly. The map will have one color component mapped to your grass base texture, so you can just test that component vs some threshold and enable/disable grass at that spot depending on the result.

-------------------------

suppagam | 2019-07-18 16:17:17 UTC | #6

Oh, I'm not really looking into fancy modern ways of doing grass with shaders and stuff. I just thought there was a built-in efficient way of slapping tons of billboard quads with a texture on my terrains as a layer. Like this: http://docs.garagegames.com/torque-3d/official/content/documentation/World%20Editor/Tutorials/CreatingFoliage.html

Thanks for the link, I'll definitely learn from your implementation. Thank you! 

As for the sampling, I think I have to phrase my question a little better: With Urho, once I read the mask and know what is closer to 0 or 1 and therefore how much grass I want, how do I get the transform (X, Y, Z) where to create my quad?

-------------------------

Lumak | 2019-07-18 16:42:32 UTC | #7

I think this is what you're looking for -- Vector3 Terrain::HeightMapToWorld(const IntVector2& pixelPosition) const
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/Terrain.cpp#L636

-------------------------

suppagam | 2019-07-18 17:41:20 UTC | #8

Thank you! Super useful.

-------------------------

jmiller | 2019-07-20 02:27:25 UTC | #9

Over the years we have also accumulated a variety of threads with still valid advice and samples related to [vegetation](https://discourse.urho3d.io/search?q=vegetation), [grass](https://discourse.urho3d.io/search?q=grass), and such.

-------------------------

