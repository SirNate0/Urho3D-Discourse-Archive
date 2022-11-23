Lumak | 2017-01-02 01:14:34 UTC | #1

If you look at the water glsl, the final fragcolor in PS() is:  
    gl_FragColor = vec4(GetFog(finalColor, GetFogFactor(vEyeVec.w)), 1.0);

where alpha = 1.0. 

How is the water transparent?

-------------------------

1vanK | 2017-01-02 01:14:34 UTC | #2

Water is not transparent. Shader mix two textures: rendered scene from main camera (refractColor) and rendered scene from reflection camera (reflectColor).

You can write for test
[code]
gl_FragColor = vec4(1.0);[/code]

-------------------------

Lumak | 2017-01-02 01:14:34 UTC | #3

Below is a pic from urho3d wikia page. There is reflection, but you can also see through the water and see the terrain.

I did figure out how to make my ocean shader use alpha. The water shader is still a mystery how the transparency happens.

[img]http://vignette2.wikia.nocookie.net/urho3d/images/2/23/23_Water.png/revision/latest?cb=20150215143404[/img]

-------------------------

1vanK | 2017-01-02 01:14:35 UTC | #4

[quote="Lumak"]but you can also see through the water and see the terrain.
[/quote]

it is texture on water plane

-------------------------

Lumak | 2017-01-02 01:14:35 UTC | #5

Thanks, didn't see that. It makes sense now.

-------------------------

