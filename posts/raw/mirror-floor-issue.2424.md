artgolf1000 | 2017-06-29 08:00:21 UTC | #1

Hi,

I want the wood floor has some mirror effect, so I modified the water sample to get a mirror floor.

I use default forward render path, it works great on macOS, the mixture effect of the original wood texture color and the reflection texture color appears.

But it has an issue on iOS device, it seems that the enviroment texture passed to the shader is black, the wood is black, only the reflection texture color appears.

Is it a bug?

Thanks.

Edit: I had enabled multi-sample feature before, when I disabled multi-sample, it works! :smiley: 

C++
[code]...
waterMat->SetTexture(TU_EMISSIVE, renderTexture);
[/code]

Floor.xml
[code]<material>
    <technique name="Techniques/DiffReflection.xml" quality="0" loddistance="0" />
    <texture unit="diffuse" name="Textures/Wood.jpg" />
    <parameter name="UOffset" value="10 0 0 0" />
    <parameter name="VOffset" value="0 2 0 0" />
    <parameter name="FresnelPower" value="16" />
</material>[/code]

DiffReflection.xml
[code]<technique vs="LitSolid" ps="LitSolid" psdefines="DIFFMAP">
    <pass name="base" />
    <pass name="litbase" psdefines="AMBIENT" />
    <pass name="light" depthtest="equal" depthwrite="false" blend="add" />
    <pass name="prepass" psdefines="PREPASS" />
    <pass name="material" psdefines="MATERIAL" depthtest="equal" depthwrite="false" />
    <pass name="deferred" psdefines="DEFERRED" />
    <pass name="depth" vs="Depth" ps="Depth" />
    <pass name="shadow" vs="Shadow" ps="Shadow" />
    <pass name="refract" vs="Mirror" ps="Mirror" />
</technique>
[/code]

Mirror.glsl
[code]#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"
#include "Fog.glsl"

#ifndef GL_ES
varying vec4 vScreenPos;
varying vec2 vReflectUV;
varying vec4 vEyeVec;
#else
varying highp vec4 vScreenPos;
varying highp vec2 vReflectUV;
varying highp vec4 vEyeVec;
#endif
varying vec3 vNormal;

#ifdef COMPILEPS
uniform float cFresnelPower;
#endif

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    vScreenPos = GetScreenPos(gl_Position);
    // GetQuadTexCoord() returns a vec2 that is OK for quad rendering; multiply it with output W
    // coordinate to make it work with arbitrary meshes such as the water plane (perform divide in pixel shader)
    // Also because the quadTexCoord is based on the clip position, and Y is flipped when rendering to a texture
    // on OpenGL, must flip again to cancel it out
    vReflectUV = GetQuadTexCoord(gl_Position);
    vReflectUV.y = 1.0 - vReflectUV.y;
    vReflectUV *= gl_Position.w;
    vNormal = GetWorldNormal(modelMatrix);
    vEyeVec = vec4(cCameraPos - worldPos, GetDepth(gl_Position));
}

void PS()
{
    vec2 refractUV = vScreenPos.xy / vScreenPos.w;
    vec2 reflectUV = vReflectUV.xy / vScreenPos.w;

    float fresnel = pow(1.0 - clamp(dot(normalize(vEyeVec.xyz), vNormal), 0.0, 1.0), cFresnelPower);
    vec3 refractColor = texture2D(sEnvMap, refractUV).rgb;
    vec3 reflectColor = texture2D(sEmissiveMap, reflectUV).rgb;
    vec3 finalColor = mix(refractColor, reflectColor, fresnel);

    gl_FragColor = vec4(GetFog(finalColor, GetFogFactor(vEyeVec.w)), 1.0);
}
[/code]

-------------------------

artgolf1000 | 2017-06-29 08:00:13 UTC | #2

After disabled multi-sample feature on iOS device, the issue disappears.

Finally, I figure out an solution, it supports multi-sample feature on iOS devices.

Floor.xml
[code]<material>
    <!-- The water example will assign the reflection texture to the emissive unit -->
    <!-- The engine will automatically assign the refraction (viewport) texture to the environment unit during refract pass -->
    <technique name="Techniques/DiffReflection.xml" quality="0" loddistance="0" />
    <texture unit="diffuse" name="Textures/Wood.jpg" />
    <parameter name="UOffset" value="4 0 0 0" />
    <parameter name="VOffset" value="0 4 0 0" />
    <parameter name="MatDiffColor" value="1 1 1 1" />
    <parameter name="MatSpecColor" value="0.5 0.5 0.5 16" />
    <parameter name="FresnelPower" value="20" />
</material>[/code]

DiffReflection.xml
[code]<technique vs="LitSolid" ps="LitSolid" psdefines="DIFFMAP">
    <pass name="base" />
    <pass name="litbase" psdefines="AMBIENT" />
    <pass name="light" depthtest="equal" depthwrite="false" blend="add" />
    <pass name="prepass" psdefines="PREPASS" />
    <pass name="material" psdefines="MATERIAL" depthtest="equal" depthwrite="false" />
    <pass name="deferred" psdefines="DEFERRED" />
    <pass name="depth" vs="Depth" ps="Depth" />
    <pass name="shadow" vs="Shadow" ps="Shadow" />
    <pass name="refract" vs="Mirror" ps="Mirror" depthtest="equal" depthwrite="false" blend="alpha" />
</technique>
[/code]

Mirror.glsl
[code]#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"
#include "Fog.glsl"

#ifndef GL_ES
varying vec4 vScreenPos;
varying vec2 vReflectUV;
varying vec4 vEyeVec;
#else
varying highp vec4 vScreenPos;
varying highp vec2 vReflectUV;
varying highp vec4 vEyeVec;
#endif
varying vec3 vNormal;

#ifdef COMPILEPS
uniform float cFresnelPower;
#endif

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    vScreenPos = GetScreenPos(gl_Position);
    // GetQuadTexCoord() returns a vec2 that is OK for quad rendering; multiply it with output W
    // coordinate to make it work with arbitrary meshes such as the water plane (perform divide in pixel shader)
    // Also because the quadTexCoord is based on the clip position, and Y is flipped when rendering to a texture
    // on OpenGL, must flip again to cancel it out
    vReflectUV = GetQuadTexCoord(gl_Position);
    vReflectUV.y = 1.0 - vReflectUV.y;
    vReflectUV *= gl_Position.w;
    vNormal = GetWorldNormal(modelMatrix);
    vEyeVec = vec4(cCameraPos - worldPos, GetDepth(gl_Position));
}

void PS()
{
    vec2 reflectUV = vReflectUV.xy / vScreenPos.w;
    float fresnel = pow(1.0 - clamp(dot(normalize(vEyeVec.xyz), vNormal), 0.0, 1.0), cFresnelPower);
    vec3 reflectColor = texture2D(sEmissiveMap, reflectUV).rgb;
    gl_FragColor = vec4(GetFog(reflectColor, GetFogFactor(vEyeVec.w)), fresnel);
}
[/code]

-------------------------

