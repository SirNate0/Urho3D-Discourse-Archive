namic | 2017-01-02 01:08:33 UTC | #1

We're migrating our UDK title to Urho3D in order to be completely free of licensing issues. Since the gameplay code is very simplistic, the really hard stuff involves migrating all of our art to the Urho3D pipeline and also adapting our materials to Urho3D ones. So far, terrains have been an issue. We use World Machine to build our terrains and export 4K maps to UDK: a heightmap, a diffuse and a splatmap. The diffuse on the entire terrain mesh allows us to have something similar to Megatexture terrain, with good amount of detail breaking up tiling and giving nice color variations. We then use the splatmap to create 4 material layers based on the RGBA values of the splatmap. Those material layers are normal UDK materials. Here's some more detail on the workflow: 

[udn.epicgames.com/Three/TerrainA ... tures.html](http://udn.epicgames.com/Three/TerrainAdvancedTextures.html)
[udn.epicgames.com/Three/LandscapeMaterials.html](http://udn.epicgames.com/Three/LandscapeMaterials.html)

Does Urho3D support this kind of workflow or has something similar? I would love to hear more about other teams using Urho3D, and specially, how they terrain workflow looks like. Thanks in advance for the attention, guys!  :wink:

-------------------------

codingmonkey | 2017-01-02 01:08:34 UTC | #2

maybe this will be helpful
[github.com/JTippetts/U3DTerrainEditor](https://github.com/JTippetts/U3DTerrainEditor)

-------------------------

namic | 2017-01-02 01:08:34 UTC | #3

Apparently, the shader used by that application has accepts a terrain texture with RGB for diffuse and A for height. It also supports 4 ~ 8 "weight" maps... are those colorized detail maps? I wasn't able to understand how they are used. If the terrain already has an RGB diffuse, why does it need a weight map? Shouldn't the weight map be just a grayscale texture being multiplied into the base diffuse? Seems to be an unnecessarily complex workflow.

-------------------------

JTippetts | 2017-01-02 01:08:34 UTC | #4

The shader used in my terrain editor actually functions similarly to the default Urho3D terrain shader, just with modifications. It has 2 blend textures (used as 8 greyscale channels) which are used as interpolants to blend from among the 8 tiling detail textures, which are held in a texture atlas. The height channel (alpha channel of the detail textures) is used as a further factor in the blending, to avoid 'smooth' gradient blends between terrains. Instead, 'lumpy' blends are done, where height differences can give a greater weight to a particular texture. This can, for example, make rocks protrude through grass and soil, rather than just smearing a direct linear blend between them. A later iteration of the shader introduces tri-planar mapping, which projects the detail textures onto the terrain along each of the 3 cardinal axes, and blend among the 3 using the terrain normal, to eliminate the stretching that comes from draping the detail textures like a blanket onto the terrain, projecting along the vertical axis only.

Essentially, the shader associates one channel from the 2 blend textures for each of the 8 terrain types. So, R from blend0 weights the first of the 8 detail terrain types (a dirt texture, in the application), G weights the second (a different variety of dirt), B weights the third (grass), and A weights the fourth (sand). Similarly for blend1 channels and the last 4 detail textures.

After the weight for a particular channel is obtained from the blend maps, a further modification is performed using the height (obtained from the detail texture's alpha channel). This height is typically the same displacement map used to generate the detail texture's normal map. It is used to offset the linear blend weight factor for the terrain type. Areas where the height of a particular detail texture is high end up being weighted more than areas where another detail texture is low height, if the weight factors are equivalent. This forces the 'lumps' of a detail texture to protrude through lower surrounding terrain, giving rise to the effect. [url=http://i.imgur.com/RtB0bNw.jpg]Image[/url]

There is no overall diffuse map to break up the tiling on a macro scale, unfortunately, so the terrains look quite repetitive from a distance. However, this can be mitigated somewhat due to having access to 8 different terrain types. In earlier versions, I did implement the technique described in the UDKTerrainAdvancedTextures document, of blending the terrain detail back into itself at a larger scale (the section titled [b]Multi-UV Mixing: Reducing tiling through scalar mixing[/b]), but with the 8 terrain types + tri-planar this becomes quite exceptionally heavyweight, and my potato is just too potato to handle it well.

Urho's materials system is not nearly as advanced as UDK, so while you can accomplish what you desire with Urho, be prepared to do a lot of the grunt work of shader writing yourself. The 'default' Urho terrain material is suitable for simple demos, but is not powerful.

-------------------------

namic | 2017-01-02 01:08:35 UTC | #5

Thank you for the great explanation, JTippetts. I feared that we would have to reinvent some wheels in the process.  :neutral_face:

-------------------------

