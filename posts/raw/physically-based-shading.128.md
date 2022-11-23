iFire | 2017-01-02 00:58:15 UTC | #1

I'm trying to implement physically based shading for Urho3d and its deferred shader.

Physically based shading uses the Cook Torrance shading model. I'm implementing [url=http://blog.selfshadow.com/publications/s2013-shading-course/karis/s2013_pbs_epic_notes_v2.pdf]Epic's Model[/url]

This is a log.

Material textures required:
Base Color (RGB):

Roughness (Greyscale):

Metallic (Greyscale):

if metallic ==  1.0 (White) (is metal)
    specular = albedbo
else if metallic == 0.0 (Black) (is dialect)
    diffuse = albedo
    fixed reflectance value (linear: 0.04 sRGB: 0.06)
else 
    reflectivity from albedo
    diffuse = albedo * metallic

Cavity (Greyscale):
s.diffuseLight *= cav *diffuseCavityStrength
s.specularLight *= cav * specularCavityStrength

Normal Map:
Use Urho's xGxR.

Shaders are in Bin\CoreData\Shaders\.

ShaderVariation* Graphics::GetShader(ShaderType type, const char* name, const char* defines) const;

DeferredLight.glsl is deferred lighting.

Can someone explain how the shaders in Urho3d work?

-------------------------

iFire | 2017-01-02 00:58:15 UTC | #2

Reserved space.

-------------------------

cadaver | 2017-01-02 00:58:15 UTC | #3

This is the relevant documentation in the doxygen docs. It's not that much or detailed; practically you just have to dive into the existing shader code to figure it out.

Materials:
[urho3d.github.io/documentation/a00021.html](http://urho3d.github.io/documentation/a00021.html)

Shaders:
[urho3d.github.io/documentation/a00022.html](http://urho3d.github.io/documentation/a00022.html)

-------------------------

iFire | 2017-01-02 00:58:16 UTC | #4

I think I'll have to add Roughness, Metalness and Cavity to <texture unit="diffuse|normal|specular|emissive|environment" . Is it defined in the c++?

-------------------------

cadaver | 2017-01-02 00:58:16 UTC | #5

Extra material parameters for shaders can be defined fully data-driven, you don't have to touch C++. Though you might want to setup defaults in the Material class if you like.

For example the terrain shader code (CoreData/Shaders/HLSL/TerrainBlend.hlsl) defines a float2 uniform constant like this (these need to be prefixed with 'c')

[code]
uniform float2 cDetailTiling;
[/code]

A value for it is assigned in the Data/Materials/Terrain.xml:

[code]
    <parameter name="DetailTiling" value="32 32" />
[/code]

-------------------------

