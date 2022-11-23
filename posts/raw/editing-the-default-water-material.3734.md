davidpox | 2017-11-12 17:15:41 UTC | #1

Hi! I'm currently using the water sample (23) and I was wondering how I would go about changing the alpha of the water. I want water that is pretty grimy and not so transparent. Changing the MatDiffColor doesn't have any effects on the material. 

Any help is appreciated =)

-------------------------

Lumak | 2017-11-12 17:29:25 UTC | #2

Two changes:
1) in CoreData\Techniques\Water.xml, add
[code]
    <pass name="refract" blend="alpha" />
[/code]
2) in your shader:
glsl: change
[code]
    gl_FragColor = vec4(GetFog(finalColor, GetFogFactor(vEyeVec.w)), 1.0);
[/code]
to 
[code]
    gl_FragColor = vec4(GetFog(finalColor, GetFogFactor(vEyeVec.w)), yourMatAlpha);
[/code]

similar for hlsl.

-------------------------

davidpox | 2017-11-12 17:50:05 UTC | #3

Hmmm I just tried that but that only seems to change the... intensity of the colour. 

https://imgur.com/a/SU46k
First is Alpha to 0.5f
Second is to 1.0f

Doesn't seem to change the opacity of the water itself

-------------------------

1vanK | 2017-11-12 18:09:17 UTC | #4

in material "Materials\Water.xml"
```
    <parameter name="FresnelPower" value="100" />
    <parameter name="WaterTint" value="1.0 1.0 1.0" />
```
absolute transparent water

>  I was wondering how I would go about changing the alpha of the water

In this example water absolutely nontransparent. All that you see is just special texture on the plane.

-------------------------

Lumak | 2017-11-12 18:27:22 UTC | #5

Here's my test:
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/7/7efdeac79048a3ef9299f4403bceea3ff0c67a1d.jpg[/img]
It's hard to tell when the alpha=0.5, unless you have a unique texture on a model that's partially submerged in the water.

edit: Iet me take that back. Unless you're applying a diffTexture to the water, which is not the case for ex. 23, it'll be difficult to see the transparency effect.

-------------------------

davidpox | 2017-11-12 19:25:27 UTC | #6

So how would I go about recreating more realistic looking water? For example here: 
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/0/06f732975aae822e6bfcbf8891161660053e635c.jpg'>

This water is greenish, and you can't see to the bottom of the lake.

-------------------------

Lumak | 2017-11-12 22:16:06 UTC | #7

If just the opacity settings, you don't need alpha blend, so keep the coredata\techniques\water.xml the same and try the material below:
[code]
<material>
    <!-- The water example will assign the reflection texture to the diffuse unit -->
    <!-- The engine will automatically assign the refraction (viewport) texture to the environment unit during refract pass -->
    <technique name="Techniques/Water.xml" />
    <texture unit="normal" name="Textures/WaterNoise.dds" />
    <parameter name="NoiseSpeed" value="0.005 0.005" />
    <parameter name="NoiseTiling" value="80" />
    <parameter name="NoiseStrength" value="0.1" />
    <parameter name="FresnelPower" value="4" />
    <parameter name="WaterTint" value="0.3 0.4 0.3" />
</material>

[/code]

-------------------------

