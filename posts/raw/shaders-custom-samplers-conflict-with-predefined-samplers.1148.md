krstefan42 | 2017-01-02 01:05:43 UTC | #1

I'm trying to add a parallax mapping option to the litSolid shader, and I need to add an additional sampler for the height/displacement map. In the docs it says:

[i]In GLSL shaders it is important that the samplers are assigned to the correct texture units. If you are using sampler names that are not predefined in the engine like sDiffMap, just make sure there is a number somewhere in the sampler's name and it will be interpreted as the texture unit. For example the terrain shader uses texture units 0-3 in the following way:[/i]

But If I add a sampler2D "sDispMap0" to the shader, and then in the material set <texture unit="0" name ="Textures/StoneFloorDisplacement.jpg" />, and then set the built-in diffuse texture afterwards, the diffuse texture overrides the displacement texture. The diffuse texture must be set to always use texture unit 0. Probably if I used a higher-numbered texture unit, I could avoid any conflicts. But on OpenGL ES you only get 8 texture units, I believe. I could also stash the height map in the alpha channel of the specular map. What do you think the best route is?

-------------------------

cadaver | 2017-01-02 01:05:43 UTC | #2

Choose the texture unit for your custom sampler according to what inbuilt samplers you also need. Eg. if you don't need normal map (probably not a realistic assumption), you could use 1. On OpenGL ES it's rather crowded, as units 5-7 are needed for light attenuation and shadows, and cannot be used.

-------------------------

