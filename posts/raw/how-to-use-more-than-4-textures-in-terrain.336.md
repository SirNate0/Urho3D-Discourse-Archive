hualin | 2017-01-02 00:59:42 UTC | #1

Hi,
Currently, the terrain use weight texture to determine use which unit. this cause the terrain can use 3 units only. Is there a way to use more than 3 units texture?
And how to produce the correct weight texture for that?

-------------------------

reattiva | 2017-01-02 00:59:42 UTC | #2

Hello, never tried but if you need 4 textures you could modify the fragment shader in \Bin\CoreData\Shaders\GLSL-HLSL\TerrainBlend to use also the alpha channel.
If you need more you need more weights texture (one texture = 4 splat textures). Add these weights textures and your splat textures in Bin\Data\Materials\Terrain.xml, then again modify the shader TerrainBlend to use all of them. JMonkey has an example, you could start from there:
[code.google.com/p/jmonkeyengine ... hting.frag](https://code.google.com/p/jmonkeyengine/source/browse/trunk/engine/src/terrain/Common/MatDefs/Terrain/TerrainLighting.frag)

-------------------------

cadaver | 2017-01-02 00:59:43 UTC | #3

Also, if you don't need to care of mobile device compatibility (which often have max. 8 texture units) you can modify the engine's texture unit definitions so that there's more room for material texture units.

-------------------------

aster2013 | 2017-01-02 00:59:43 UTC | #4

It's better make terrain can use more then 4 textures, but every terrain patch only use 4 textures at most.

-------------------------

