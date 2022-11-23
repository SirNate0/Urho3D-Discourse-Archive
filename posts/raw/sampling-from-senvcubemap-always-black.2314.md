TheComet | 2017-01-02 01:14:40 UTC | #1

I'm trying to implement reflection for arbitrary surfaces, and I figured sEnvCubeMap would be the correct way to do this.

Here is my technique:
[code]<technique vs="RefractionReflection_VS" ps="RefractionReflection_PS" >
    <pass name="refract" />
</technique>[/code]

Pixel shader:
[code]#include "Uniforms.glsl"
#include "Samplers.glsl"

const float bumpyness = 0.0;
const float refractFactor = 0.9;

varying vec3 vPosition_worldSpace;
varying vec3 vNormal_worldSpace;
varying vec3 vTangent_worldSpace;
varying vec3 vEyeDirection_worldSpace;
varying vec2 vTexCoord;
varying vec3 vProjection;

void PS()
{
    vec3 eyeDirection_worldSpace = normalize(vEyeDirection_worldSpace);
    vec3 normal_textureSpace = normalize(texture2D(sNormalMap, vTexCoord).rgb * 2 - 1);

    mat3 invTBN = mat3(
        normalize(vTangent_worldSpace),
        normalize(cross(vTangent_worldSpace, vNormal_worldSpace)),
        normalize(vNormal_worldSpace)
    );

    vec3 normal_worldSpace = invTBN * normal_textureSpace;
    vec3 reflect_worldSpace = reflect(-eyeDirection_worldSpace, normal_worldSpace);
    vec3 reflectColor = textureCube(sEnvCubeMap, reflect_worldSpace).rgb;

    gl_FragColor = vec4(reflectColor, 1);
}[/code]

Result:
[img]http://i.imgur.com/1iqsPc2.png[/img]

And just to show that my reflect_worldSpace vector is correct, here I output it directly with [b]gl_FragColor = vec4(reflect_worldSpace, 1);[/b]:
[img]http://i.imgur.com/34RvS1J.png[/img]

-------------------------

NiteLordz | 2017-01-02 01:14:42 UTC | #2

I'm currently working on the same thing, you having any luck with it?

i am looking at how the water sample works, and not having any luck as of yet.

-------------------------

jmiller | 2017-01-02 01:14:43 UTC | #3

I just thought I should mention: There is an issue with GL_TEXTURE_CUBE_MAP_SEAMLESS that results in software fallback and rendering black on some hardware (including GeForce 9800GT and some older in the line that otherwise support OpenGL 3.2). It's 'wontfix' but a simple fix is described.
[github.com/urho3d/Urho3D/issues/1380](https://github.com/urho3d/Urho3D/issues/1380)

But if TextureCube otherwise renders for you, disregard.

-------------------------

