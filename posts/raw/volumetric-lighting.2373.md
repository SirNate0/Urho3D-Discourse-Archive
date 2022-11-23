artgolf1000 | 2017-01-02 01:15:02 UTC | #1

Hi,

I have ported [url]http://www.alexandre-pestana.com/volumetric-lights/[/url] into 'forwardlights' command, it works, but still has some issues.
I have commented the second 'forwardlights' command now, it will override generated volumetric light QUAT unexpectedly.

Edit: The engine does not support multiply forward lighting passes, so I have to use the alpha channel to store the volumetric light value instead.

-------------------------

franck22000 | 2017-01-02 01:15:02 UTC | #2

Nice, do you have any screenshots or video to show ? 

Are you planning to do this for deferred renderpath ?

-------------------------

artgolf1000 | 2017-01-02 01:15:02 UTC | #3

I'll try deferred render-path tomorrow, no screenshots or videos yet.

-------------------------

artgolf1000 | 2017-01-02 01:15:02 UTC | #4

Figure it out! It works in both forward mode and deferred mode now!

It support multiple directional lights, point lights and spot lights casting shadows, but use only one light to cast shadow is recommended.

To test volumetric lighting effect, just replace the original files with the modified version, the volumetric lighting effect should appears.

The forward mode can run on mobile devices, if you use only one directional light to cast shadow, the performance is excellent, I notice no cpu increase.

This demo has one directional light behind a wall, light beams come through the windows, you can see the volumetric lighting effect when light direction changes.

Youtube: [url]https://youtu.be/ZkkazPduyW4[/url]
[video]https://youtu.be/ZkkazPduyW4[/video]

Forward.xml:
[code]<renderpath>
    <rendertarget name="fullscreen" sizedivisor="1 1" format="rgba" filter="true" />
    <command type="clear" color="0 0 0 0" depth="1.0" stencil="0" output="fullscreen" />
    <command type="scenepass" pass="base" vsdefines="VOLUMETRICLIGHT" psdefines="VOLUMETRICLIGHT" vertexlights="true" metadata="base" output="fullscreen" />
    <command type="forwardlights" pass="light" vsdefines="VOLUMETRICLIGHT" psdefines="VOLUMETRICLIGHT" output="fullscreen" />
    <rendertarget name="blurv" tag="Bloom" sizedivisor="4 4" format="rgb" filter="true" />
    <rendertarget name="blurh" tag="Bloom" sizedivisor="4 4" format="rgb" filter="true" />
    <command type="quad" tag="Bloom" vs="Bloom" ps="Bloom" psdefines="BRIGHT VOLUMETRICLIGHT" output="blurv">
        <parameter name="BloomThreshold" value="0.0" />
        <texture unit="diffuse" name="fullscreen" />
    </command>
    <command type="quad" tag="Bloom" vs="Bloom" ps="Bloom" psdefines="BLURH" output="blurh">
        <texture unit="diffuse" name="blurv" />
    </command>
    <command type="quad" tag="Bloom" vs="Bloom" ps="Bloom" psdefines="BLURV" output="blurv">
        <texture unit="diffuse" name="blurh" />
    </command>
    <command type="quad" tag="Bloom" vs="Bloom" ps="Bloom" psdefines="COMBINE" output="viewport">
        <parameter name="BloomMix" value="1.0 1.0" />
        <texture unit="diffuse" name="fullscreen" />
        <texture unit="normal" name="blurv" />
    </command>
    <command type="scenepass" pass="postopaque" />
    <command type="scenepass" pass="refract">
        <texture unit="environment" name="viewport" />
    </command>
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" />
    <command type="scenepass" pass="postalpha" sort="backtofront" />
</renderpath>
[/code]

Deferred.xml:
[code]<renderpath>
    <rendertarget name="albedo" sizedivisor="1 1" format="rgba" />
    <rendertarget name="normal" sizedivisor="1 1" format="rgba" />
    <rendertarget name="depth" sizedivisor="1 1" format="lineardepth" />
    <rendertarget name="fullscreen" sizedivisor="1 1" format="rgba" filter="true" />
    <command type="clear" color="0 0 0 0" depth="1.0" stencil="0" output="fullscreen" />
    <command type="scenepass" pass="deferred" vsdefines="VOLUMETRICLIGHT" psdefines="VOLUMETRICLIGHT" marktostencil="true" vertexlights="true" metadata="gbuffer">
        <output index="0" name="fullscreen" />
        <output index="1" name="albedo" />
        <output index="2" name="normal" />
        <output index="3" name="depth" />
    </command>
    <command type="lightvolumes" vs="DeferredLight" ps="DeferredLight" vsdefines="VOLUMETRICLIGHT" psdefines="VOLUMETRICLIGHT" output="fullscreen">
        <texture unit="albedo" name="albedo" />
        <texture unit="normal" name="normal" />
        <texture unit="depth" name="depth" />
    </command>
    <rendertarget name="blurv" tag="Bloom" sizedivisor="4 4" format="rgb" filter="true" />
    <rendertarget name="blurh" tag="Bloom" sizedivisor="4 4" format="rgb" filter="true" />
    <command type="quad" tag="Bloom" vs="Bloom" ps="Bloom" psdefines="BRIGHT VOLUMETRICLIGHT" output="blurv">
        <parameter name="BloomThreshold" value="0.0" />
        <texture unit="diffuse" name="fullscreen" />
    </command>
    <command type="quad" tag="Bloom" vs="Bloom" ps="Bloom" psdefines="BLURH" output="blurh">
        <texture unit="diffuse" name="blurv" />
    </command>
    <command type="quad" tag="Bloom" vs="Bloom" ps="Bloom" psdefines="BLURV" output="blurv">
        <texture unit="diffuse" name="blurh" />
    </command>
    <command type="quad" tag="Bloom" vs="Bloom" ps="Bloom" psdefines="COMBINE" output="viewport">
        <parameter name="BloomMix" value="1.0 1.0" />
        <texture unit="diffuse" name="fullscreen" />
        <texture unit="normal" name="blurv" />
    </command>
    <command type="scenepass" pass="postopaque" />
    <command type="scenepass" pass="refract">
        <texture unit="environment" name="viewport" />
    </command>
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" />
    <command type="scenepass" pass="postalpha" sort="backtofront" />
</renderpath>
[/code]

Bloom.glsl:
[code]#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"

varying vec2 vTexCoord;
varying vec2 vScreenPos;

#ifdef COMPILEPS
uniform float cBloomThreshold;
uniform vec2 cBloomMix;
uniform vec2 cBlurHInvSize;
#endif

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    vTexCoord = GetQuadTexCoord(gl_Position);
    vScreenPos = GetScreenPosPreDiv(gl_Position);
}

void PS()
{
#ifdef BRIGHT
    #ifndef VOLUMETRICLIGHT
        vec3 rgb = texture2D(sDiffMap, vScreenPos).rgb;
    #else
        vec3 rgb = texture2D(sDiffMap, vScreenPos).aaa;
    #endif
    gl_FragColor = vec4((rgb - vec3(cBloomThreshold, cBloomThreshold, cBloomThreshold)) / (1.0 - cBloomThreshold), 1.0);
#endif
    
#ifdef BLURH
    vec3 rgb = texture2D(sDiffMap, vTexCoord + vec2(-2.0, 0.0) * cBlurHInvSize).rgb * 0.1;
    rgb += texture2D(sDiffMap, vTexCoord + vec2(-1.0, 0.0) * cBlurHInvSize).rgb * 0.25;
    rgb += texture2D(sDiffMap, vTexCoord + vec2(0.0, 0.0) * cBlurHInvSize).rgb * 0.3;
    rgb += texture2D(sDiffMap, vTexCoord + vec2(1.0, 0.0) * cBlurHInvSize).rgb * 0.25;
    rgb += texture2D(sDiffMap, vTexCoord + vec2(2.0, 0.0) * cBlurHInvSize).rgb * 0.1;
    gl_FragColor = vec4(rgb, 1.0);
#endif
    
#ifdef BLURV
    vec3 rgb = texture2D(sDiffMap, vTexCoord + vec2(0.0, -2.0) * cBlurHInvSize).rgb * 0.1;
    rgb += texture2D(sDiffMap, vTexCoord + vec2(0.0, -1.0) * cBlurHInvSize).rgb * 0.25;
    rgb += texture2D(sDiffMap, vTexCoord + vec2(0.0, 0.0) * cBlurHInvSize).rgb * 0.3;
    rgb += texture2D(sDiffMap, vTexCoord + vec2(0.0, 1.0) * cBlurHInvSize).rgb * 0.25;
    rgb += texture2D(sDiffMap, vTexCoord + vec2(0.0, 2.0) * cBlurHInvSize).rgb * 0.1;
    gl_FragColor = vec4(rgb, 1.0);
#endif
    
#ifdef COMBINE
    vec3 original = texture2D(sDiffMap, vScreenPos).rgb * cBloomMix.x;
    vec3 bloom = texture2D(sNormalMap, vTexCoord).rgb  * cBloomMix.y;
    // Prevent oversaturation
    original *= max(vec3(1.0) - bloom, vec3(0.0));
    gl_FragColor = vec4(original + bloom, 1.0);
#endif
}
[/code]

DeferredLight.glsl:
[code]#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"
#include "Lighting.glsl"

#ifdef DIRLIGHT
    varying vec2 vScreenPos;
#else
    varying vec4 vScreenPos;
#endif
varying vec3 vFarRay;
#ifdef ORTHO
    varying vec3 vNearRay;
#endif

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    #ifdef DIRLIGHT
        vScreenPos = GetScreenPosPreDiv(gl_Position);
        vFarRay = GetFarRay(gl_Position);
        #ifdef ORTHO
            vNearRay = GetNearRay(gl_Position);
        #endif
    #else
        vScreenPos = GetScreenPos(gl_Position);
        vFarRay = GetFarRay(gl_Position) * gl_Position.w;
        #ifdef ORTHO
            vNearRay = GetNearRay(gl_Position) * gl_Position.w;
        #endif
    #endif
}


#ifdef SHADOW
    #ifdef VOLUMETRICLIGHT
        float ComputeScattering(float lightDotView)
        {
            const float G_SCATTERING = 0.5;
            const float PI = 3.14159265358979323846;
            float result = 1.0 - G_SCATTERING * G_SCATTERING;
            result /= (4.0 * PI * pow(1.0 + G_SCATTERING * G_SCATTERING - (2.0 * G_SCATTERING) * lightDotView, 1.5));
            return result;
        }

        float rand(highp vec2 co){
            return fract(sin(dot(co.xy ,vec2(12.9898,78.233))) * 43758.5453);
        }
    #endif
#endif

void PS()
{
    // If rendering a directional light quad, optimize out the w divide
    #ifdef DIRLIGHT
        #ifdef HWDEPTH
            float depth = ReconstructDepth(texture2D(sDepthBuffer, vScreenPos).r);
        #else
            float depth = DecodeDepth(texture2D(sDepthBuffer, vScreenPos).rgb);
        #endif
        #ifdef ORTHO
            vec3 worldPos = mix(vNearRay, vFarRay, depth);
        #else
            vec3 worldPos = vFarRay * depth;
        #endif
        vec4 albedoInput = texture2D(sAlbedoBuffer, vScreenPos);
        vec4 normalInput = texture2D(sNormalBuffer, vScreenPos);
    #else
        #ifdef HWDEPTH
            float depth = ReconstructDepth(texture2DProj(sDepthBuffer, vScreenPos).r);
        #else
            float depth = DecodeDepth(texture2DProj(sDepthBuffer, vScreenPos).rgb);
        #endif
        #ifdef ORTHO
            vec3 worldPos = mix(vNearRay, vFarRay, depth) / vScreenPos.w;
        #else
            vec3 worldPos = vFarRay * depth / vScreenPos.w;
        #endif
        vec4 albedoInput = texture2DProj(sAlbedoBuffer, vScreenPos);
        vec4 normalInput = texture2DProj(sNormalBuffer, vScreenPos);
    #endif

    // Position acquired via near/far ray is relative to camera. Bring position to world space
    vec3 eyeVec = -worldPos;
    worldPos += cCameraPosPS;
    
    vec3 normal = normalize(normalInput.rgb * 2.0 - 1.0);
    vec4 projWorldPos = vec4(worldPos, 1.0);
    vec3 lightColor;
    vec3 lightDir;
    
    float diff = GetDiffuse(normal, worldPos, lightDir);

    #ifdef SHADOW
        diff *= GetShadowDeferred(projWorldPos, normal, depth);
        #ifdef VOLUMETRICLIGHT
            highp vec3 rayDirection = normalize(worldPos-cCameraPosPS);
            float accumFog = 0.0;
            const int NB_STEPS = 15;
            #ifdef DIRLIGHT
                float ditherValue = rand(vScreenPos);
            #else
                float ditherValue = rand(vScreenPos.xy/vScreenPos.w);
            #endif
            for (int n = 0; n < NB_STEPS; n++) {
                highp vec4 projWorldPosSpace = vec4(cCameraPosPS+(float(n)+ditherValue)*(worldPos-cCameraPosPS)/float(NB_STEPS), 1.0);
                accumFog += GetShadowDeferred(projWorldPosSpace, vec3(0.0), float(n)*depth/float(NB_STEPS))*ComputeScattering(dot(rayDirection, lightDir));
            }
            accumFog /= float(NB_STEPS);
        #endif
    #endif
    
    #if defined(SPOTLIGHT)
        vec4 spotPos = projWorldPos * cLightMatricesPS[0];
        lightColor = spotPos.w > 0.0 ? texture2DProj(sLightSpotMap, spotPos).rgb * cLightColor.rgb : vec3(0.0);
    #elif defined(CUBEMASK)
        mat3 lightVecRot = mat3(cLightMatricesPS[0][0].xyz, cLightMatricesPS[0][1].xyz, cLightMatricesPS[0][2].xyz);
        lightColor = textureCube(sLightCubeMap, (worldPos - cLightPosPS.xyz) * lightVecRot).rgb * cLightColor.rgb;
    #else
        lightColor = cLightColor.rgb;
    #endif

    #ifdef SPECULAR
        float spec = GetSpecular(normal, eyeVec, lightDir, normalInput.a * 255.0);
        vec3 finalColor = diff * lightColor * (albedoInput.rgb + spec * cLightColor.a * albedoInput.aaa);
    #else
        vec3 finalColor = diff * lightColor * albedoInput.rgb;
    #endif

    float finalAlpha = 0.0;
    #ifdef SHADOW
        #ifdef VOLUMETRICLIGHT
            finalAlpha = accumFog;
        #endif
    #endif

    gl_FragColor = vec4(finalColor, finalAlpha);
}
[/code]

LitSolid.glsl:
[code]#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"
#include "Lighting.glsl"
#include "Fog.glsl"

#ifdef NORMALMAP
    varying vec4 vTexCoord;
    varying vec4 vTangent;
#else
    varying vec2 vTexCoord;
#endif
varying vec3 vNormal;
varying vec4 vWorldPos;
#ifdef VERTEXCOLOR
    varying vec4 vColor;
#endif
#ifdef PERPIXEL
    #ifdef SHADOW
        #ifndef GL_ES
            varying vec4 vShadowPos[NUMCASCADES];
            #ifdef VOLUMETRICLIGHT
                varying vec2 vScreenPos;
                varying vec4 vShadowPosCamera[NUMCASCADES];
                varying vec4 vShadowPosTarget[NUMCASCADES];
            #endif
        #else
            varying highp vec4 vShadowPos[NUMCASCADES];
            #ifdef VOLUMETRICLIGHT
                varying highp vec2 vScreenPos;
                varying highp vec4 vShadowPosCamera[NUMCASCADES];
                varying highp vec4 vShadowPosTarget[NUMCASCADES];
            #endif
        #endif
    #endif
    #ifdef SPOTLIGHT
        varying vec4 vSpotPos;
    #endif
    #ifdef POINTLIGHT
        varying vec3 vCubeMaskVec;
    #endif
#else
    varying vec3 vVertexLight;
    varying vec4 vScreenPos;
    #ifdef ENVCUBEMAP
        varying vec3 vReflectionVec;
    #endif
    #if defined(LIGHTMAP) || defined(AO)
        varying vec2 vTexCoord2;
    #endif
#endif

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    vNormal = GetWorldNormal(modelMatrix);
    vWorldPos = vec4(worldPos, GetDepth(gl_Position));

    #ifdef VERTEXCOLOR
        vColor = iColor;
    #endif

    #ifdef NORMALMAP
        vec3 tangent = GetWorldTangent(modelMatrix);
        vec3 bitangent = cross(tangent, vNormal) * iTangent.w;
        vTexCoord = vec4(GetTexCoord(iTexCoord), bitangent.xy);
        vTangent = vec4(tangent, bitangent.z);
    #else
        vTexCoord = GetTexCoord(iTexCoord);
    #endif

    #ifdef PERPIXEL
        // Per-pixel forward lighting
        vec4 projWorldPos = vec4(worldPos, 1.0);

        #ifdef SHADOW
            // Shadow projection: transform from world space to shadow space
            for (int i = 0; i < NUMCASCADES; i++)
                vShadowPos[i] = GetShadowPos(i, vNormal, projWorldPos);
            #ifdef VOLUMETRICLIGHT
                // Shadow projection: transform from world space to shadow space
                for (int i = 0; i < NUMCASCADES; i++)
                    vShadowPosCamera[i] = GetShadowPos(i, vec3(0), vec4(cCameraPos, 1.0));
                // Shadow projection: transform from world space to shadow space
                for (int i = 0; i < NUMCASCADES; i++)
                    vShadowPosTarget[i] = GetShadowPos(i, vec3(0), projWorldPos);
                vScreenPos = GetScreenPosPreDiv(gl_Position);
            #endif
        #endif

        #ifdef SPOTLIGHT
            // Spotlight projection: transform from world space to projector texture coordinates
            vSpotPos = projWorldPos * cLightMatrices[0];
        #endif
    
        #ifdef POINTLIGHT
            vCubeMaskVec = (worldPos - cLightPos.xyz) * mat3(cLightMatrices[0][0].xyz, cLightMatrices[0][1].xyz, cLightMatrices[0][2].xyz);
        #endif
    #else
        // Ambient & per-vertex lighting
        #if defined(LIGHTMAP) || defined(AO)
            // If using lightmap, disregard zone ambient light
            // If using AO, calculate ambient in the PS
            vVertexLight = vec3(0.0, 0.0, 0.0);
            vTexCoord2 = iTexCoord1;
        #else
            vVertexLight = GetAmbient(GetZonePos(worldPos));
        #endif
        
        #ifdef NUMVERTEXLIGHTS
            for (int i = 0; i < NUMVERTEXLIGHTS; ++i)
                vVertexLight += GetVertexLight(i, worldPos, vNormal) * cVertexLights[i * 3].rgb;
        #endif
        
        vScreenPos = GetScreenPos(gl_Position);

        #ifdef ENVCUBEMAP
            vReflectionVec = worldPos - cCameraPos;
        #endif
    #endif
}

#ifdef SHADOW
    #ifdef VOLUMETRICLIGHT
        float ComputeScattering(float lightDotView)
        {
            const float G_SCATTERING = 0.5;
            const float PI = 3.14159265358979323846;
            float result = 1.0 - G_SCATTERING * G_SCATTERING;
            result /= (4.0 * PI * pow(1.0 + G_SCATTERING * G_SCATTERING - (2.0 * G_SCATTERING) * lightDotView, 1.5));
            return result;
        }

        float rand(highp vec2 co){
            return fract(sin(dot(co.xy ,vec2(12.9898,78.233))) * 43758.5453);
        }
    #endif
#endif

void PS()
{
    // Get material diffuse albedo
    #ifdef DIFFMAP
        vec4 diffInput = texture2D(sDiffMap, vTexCoord.xy);
        #ifdef ALPHAMASK
            if (diffInput.a < 0.5)
                discard;
        #endif
        vec4 diffColor = cMatDiffColor * diffInput;
    #else
        vec4 diffColor = cMatDiffColor;
    #endif

    #ifdef VERTEXCOLOR
        diffColor *= vColor;
    #endif
    
    // Get material specular albedo
    #ifdef SPECMAP
        vec3 specColor = cMatSpecColor.rgb * texture2D(sSpecMap, vTexCoord.xy).rgb;
    #else
        vec3 specColor = cMatSpecColor.rgb;
    #endif

    // Get normal
    #ifdef NORMALMAP
        mat3 tbn = mat3(vTangent.xyz, vec3(vTexCoord.zw, vTangent.w), vNormal);
        vec3 normal = normalize(tbn * DecodeNormal(texture2D(sNormalMap, vTexCoord.xy)));
    #else
        vec3 normal = normalize(vNormal);
    #endif

    // Get fog factor
    #ifdef HEIGHTFOG
        float fogFactor = GetHeightFogFactor(vWorldPos.w, vWorldPos.y);
    #else
        float fogFactor = GetFogFactor(vWorldPos.w);
    #endif

    #if defined(PERPIXEL)
        // Per-pixel forward lighting
        vec3 lightColor;
        vec3 lightDir;
        vec3 finalColor;

        float diff = GetDiffuse(normal, vWorldPos.xyz, lightDir);

        #ifdef SHADOW
            diff *= GetShadow(vShadowPos, vWorldPos.w);
            #ifdef VOLUMETRICLIGHT
                highp vec3 rayDirection = normalize(vWorldPos.xyz-cCameraPosPS);
                float accumFog = 0.0;
                const int NB_STEPS = 15;
                float ditherValue = rand(vScreenPos);
                for (int n = 0; n < NB_STEPS; n++) {
                    highp vec4 vShadowPosSpace[NUMCASCADES];
                    for (int i = 0; i < NUMCASCADES; i++) {
                        vShadowPosSpace[i] = vShadowPosCamera[i]+(float(n)+ditherValue)*(vShadowPosTarget[i]-vShadowPosCamera[i])/float(NB_STEPS);
                    }
                    accumFog += GetShadow(vShadowPosSpace, float(n)*vWorldPos.w/float(NB_STEPS))*ComputeScattering(dot(rayDirection, lightDir));
                }
                accumFog /= float(NB_STEPS);
            #endif
        #endif
    
        #if defined(SPOTLIGHT)
            lightColor = vSpotPos.w > 0.0 ? texture2DProj(sLightSpotMap, vSpotPos).rgb * cLightColor.rgb : vec3(0.0, 0.0, 0.0);
        #elif defined(CUBEMASK)
            lightColor = textureCube(sLightCubeMap, vCubeMaskVec).rgb * cLightColor.rgb;
        #else
            lightColor = cLightColor.rgb;
        #endif
    
        #ifdef SPECULAR
            float spec = GetSpecular(normal, cCameraPosPS - vWorldPos.xyz, lightDir, cMatSpecColor.a);
            finalColor = diff * lightColor * (diffColor.rgb + spec * specColor * cLightColor.a);
        #else
            finalColor = diff * lightColor * diffColor.rgb;
        #endif

        #ifdef AMBIENT
            finalColor += cAmbientColor.rgb * diffColor.rgb;
            finalColor += cMatEmissiveColor;
            finalColor = GetFog(finalColor, fogFactor);
        #else
            finalColor = GetLitFog(finalColor, fogFactor);
        #endif
    
        #ifndef VOLUMETRICLIGHT
            float finalAlpha = diffColor.a;
        #else
            float finalAlpha = 0.0;
        #endif
    
        #ifdef SHADOW
            #ifdef VOLUMETRICLIGHT
                finalAlpha = accumFog;
            #endif
        #endif
        gl_FragColor = vec4(finalColor, finalAlpha);
    #elif defined(PREPASS)
        // Fill light pre-pass G-Buffer
        float specPower = cMatSpecColor.a / 255.0;

        gl_FragData[0] = vec4(normal * 0.5 + 0.5, specPower);
        gl_FragData[1] = vec4(EncodeDepth(vWorldPos.w), 0.0);
    #elif defined(DEFERRED)
        // Fill deferred G-buffer
        float specIntensity = specColor.g;
        float specPower = cMatSpecColor.a / 255.0;

        vec3 finalColor = vVertexLight * diffColor.rgb;
        #ifdef AO
            // If using AO, the vertex light ambient is black, calculate occluded ambient here
            finalColor += texture2D(sEmissiveMap, vTexCoord2).rgb * cAmbientColor.rgb * diffColor.rgb;
        #endif

        #ifdef ENVCUBEMAP
            finalColor += cMatEnvMapColor * textureCube(sEnvCubeMap, reflect(vReflectionVec, normal)).rgb;
        #endif
        #ifdef LIGHTMAP
            finalColor += texture2D(sEmissiveMap, vTexCoord2).rgb * diffColor.rgb;
        #endif
        #ifdef EMISSIVEMAP
            finalColor += cMatEmissiveColor * texture2D(sEmissiveMap, vTexCoord.xy).rgb;
        #else
            finalColor += cMatEmissiveColor;
        #endif

        #ifndef VOLUMETRICLIGHT
            gl_FragData[0] = vec4(GetFog(finalColor, fogFactor), 1.0);
        #else
            gl_FragData[0] = vec4(GetFog(finalColor, fogFactor), 0.0);
        #endif
        gl_FragData[1] = fogFactor * vec4(diffColor.rgb, specIntensity);
        gl_FragData[2] = vec4(normal * 0.5 + 0.5, specPower);
        gl_FragData[3] = vec4(EncodeDepth(vWorldPos.w), 0.0);
    #else
        // Ambient & per-vertex lighting
        vec3 finalColor = vVertexLight * diffColor.rgb;
        #ifdef AO
            // If using AO, the vertex light ambient is black, calculate occluded ambient here
            finalColor += texture2D(sEmissiveMap, vTexCoord2).rgb * cAmbientColor.rgb * diffColor.rgb;
        #endif
        
        #ifdef MATERIAL
            // Add light pre-pass accumulation result
            // Lights are accumulated at half intensity. Bring back to full intensity now
            vec4 lightInput = 2.0 * texture2DProj(sLightBuffer, vScreenPos);
            vec3 lightSpecColor = lightInput.a * lightInput.rgb / max(GetIntensity(lightInput.rgb), 0.001);

            finalColor += lightInput.rgb * diffColor.rgb + lightSpecColor * specColor;
        #endif

        #ifdef ENVCUBEMAP
            finalColor += cMatEnvMapColor * textureCube(sEnvCubeMap, reflect(vReflectionVec, normal)).rgb;
        #endif
        #ifdef LIGHTMAP
            finalColor += texture2D(sEmissiveMap, vTexCoord2).rgb * diffColor.rgb;
        #endif
        #ifdef EMISSIVEMAP
            finalColor += cMatEmissiveColor * texture2D(sEmissiveMap, vTexCoord.xy).rgb;
        #else
            finalColor += cMatEmissiveColor;
        #endif

        gl_FragColor = vec4(GetFog(finalColor, fogFactor), diffColor.a);
    #endif
}
[/code]

-------------------------

franck22000 | 2017-01-02 01:15:02 UTC | #5

Excellent, looking forward to see if you are able to port it for deferred rendering.

-------------------------

artgolf1000 | 2017-01-02 01:15:03 UTC | #6

The deferred mode is ready, it support both forward lighting mode and deferred lighting mode now!

I have to use the alpha channel to store volumetric lighting value, it may cause alpha lighting incorrect, if this happens, put 'vsexcludes="VOLUMETRICLIGHT"' and 'psexcludes="VOLUMETRICLIGHT"' to the litalpha and light pass, such as 'DiffAlpha.xml', it should solve the issue.

I can not figure out how to let lighting pass support multiple render target at present.

-------------------------

dragonCASTjosh | 2017-01-02 01:15:04 UTC | #7

Does it support the PBR render path? because i think it would look amazing alongside PBR

-------------------------

artgolf1000 | 2017-01-02 01:15:04 UTC | #8

I am not familiar with PBR, you may look into DeferredLight.glsl, I guess it not difficult to port to PBR.

-------------------------

dragonCASTjosh | 2017-01-02 01:15:06 UTC | #9

as long as it doesnt make changes to the diffuse or specular then i dont see it causing a problem to implement

-------------------------

