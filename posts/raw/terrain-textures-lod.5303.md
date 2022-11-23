suppagam | 2019-07-18 01:21:40 UTC | #1

I was testing out the terrain system in Urho3D and I was trying to find out how to do terrain texture LOD. The current terrain system has a geometry LOD that works pretty well, but the texture doesn't really change. So, let's say you have a very nice diffuse + normal on your terrain, and it looks great at a distance, but terrible up close. 

How is it possible to define the LOD for terrain textures? Kinda like what Enemy Territory Quake Wars did here:

https://www.beyond3d.com/images/articles/etqw/mega_road-big.jpg
https://www.beyond3d.com/images/articles/etqw/mega_shadow-big.jpg
https://wiki.splashdamage.com/index.php/An_Advanced_Terrain_and_Megatexture

Each layer seems to have a material, which has LOD levels.

-------------------------

Leith | 2019-07-18 05:01:55 UTC | #2

Here's their material setup - I don't see any mention of LOD, but there are a suspicious number of detail textures! We have the usual 4 detail textures, then a bunch of others that have some blending information, indicating that local detail decals are being used to provide extra detail where required..
<https://wiki.splashdamage.com/index.php/An_Advanced_Terrain_and_Megatexture#Setup_the_Material>

-------------------------

JTippetts1 | 2019-07-18 13:28:27 UTC | #4

You can use the material definition file to set up LoDs per https://urho3d.github.io/documentation/HEAD/_materials.html

This allows you to degrade technique quality based on distance. For the actual textures themselves, you can use an associated xml file to specify mipmap usage.

For more sophisticated techniques such as using smaller, highly detailed splats for up close, you will probably need to write a custom shader and possibly dig into the guts of the terrain class. Vanilla Terrain just isnt that sophisticated at the moment.

-------------------------

