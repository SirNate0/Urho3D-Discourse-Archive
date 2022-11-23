Tinimini | 2017-01-02 01:05:04 UTC | #1

Still playing around with custom geometry (or actually raw vertex & index buffers), but I can't seem to get the colors defined for my vertices to show up. All my geometries end up white no matter what color I've defined for the vertices. Which material am I supposed to use to get coloring to work?

-------------------------

cadaver | 2017-01-02 01:05:04 UTC | #2

If you're using the LitSolid shader, you need the VERTEXCOLOR define in both the vertex & pixel shader. Techniques which have VCol in their name have this.

However there wasn't a pure replace blend version of these yet. I just committed DiffVCol.xml & NoTextureVCol.xml techniques to master branch, which you should be able to use.

-------------------------

Tinimini | 2017-01-02 01:05:04 UTC | #3

Ok, thanks. I grabbed those techniques and I'll try those out. Can you give me an example how to use them? I need to define a material with those techniques, right? Sorry for the noob questions, but I'm pretty new at this 3D programming stuff.
I'm getting the following warnings when I build with my project with those techniques included:
[code]
[Fri May  8 12:01:14 2015] WARNING: Shader LitSolid(DIRLIGHT NOUV PERPIXEL VERTEXCOLOR) does not use the define NOUV
[Fri May  8 12:01:14 2015] WARNING: Shader LitSolid(DIRLIGHT NOUV PERPIXEL VERTEXCOLOR) does not use the define VERTEXCOLOR
[Fri May  8 12:01:14 2015] DEBUG: Compiled vertex shader LitSolid(DIRLIGHT NOUV PERPIXEL VERTEXCOLOR)
[Fri May  8 12:01:14 2015] WARNING: Shader LitSolid(AMBIENT DIRLIGHT PERPIXEL VERTEXCOLOR) does not use the define VERTEXCOLOR
[/code]

-------------------------

Tinimini | 2017-01-02 01:05:05 UTC | #4

Oh, and just wanted to say that I'm thoroughly enjoying my time with Urho3D. As I said, I'm pretty new to all this 3D programming stuff and it's been almost 20 years since I last wrote a line of C++, but having a blast so far.
Here's a screenshot of what I've been able to hack together so far (yes, one more voxel/cube/minecraft inspired thing).

[img]http://i.imgur.com/g1XXlba.jpg[/img]

-------------------------

cadaver | 2017-01-02 01:05:05 UTC | #5

Take some material as a base, like Mushroom.xml. Either edit the technique reference with a text editor, or use the editor's Material editor window to pick a new technique with the file selector.

However now that you mention those warnings, it appears that the LitSolid shader actually has never supported vertex colors though the techniques exist, so this is a bug which still needs to be fixed. It seems that so far vertex colors have only been used in unlit materials.

-------------------------

Tinimini | 2017-01-02 01:05:05 UTC | #6

Ah, that explains it. I got it working using NoTextureVCol technique. See screenshot.

[img]http://i.imgur.com/h7utBAM.png[/img]

-------------------------

Tinimini | 2017-01-02 01:05:05 UTC | #7

Got the lit version working also. Never having written shaders, I just took a look at how Unlit.glsl was done and I copied the stuff I thought was necessary. Here's the changed LitSolid.glsl. Just added the parts with #ifdef VERTEXCOLOR to it
[code]
#include "Uniforms.glsl"
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
#ifdef VERTEXCOLOR
    varying vec4 vColor;
#endif
varying vec3 vNormal;
varying vec4 vWorldPos;
#ifdef PERPIXEL
    #ifdef SHADOW
        varying vec4 vShadowPos[NUMCASCADES];
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
                vShadowPos[i] = GetShadowPos(i, projWorldPos);
        #endif

        #ifdef SPOTLIGHT
            // Spotlight projection: transform from world space to projector texture coordinates
            vSpotPos =  projWorldPos * cLightMatrices[0];
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
            vTexCoord2 = iTexCoord2;
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
    #ifdef VERTEXCOLOR
        vColor = iColor;
    #endif
}

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

    #ifdef VERTEXCOLOR
        diffColor *= vColor;
    #endif

    #if defined(PERPIXEL)
        // Per-pixel forward lighting
        vec3 lightColor;
        vec3 lightDir;
        vec3 finalColor;

        float diff = GetDiffuse(normal, vWorldPos.xyz, lightDir);

        #ifdef SHADOW
            diff *= GetShadow(vShadowPos, vWorldPos.w);
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
            finalColor += cAmbientColor * diffColor.rgb;
            finalColor += cMatEmissiveColor;
            gl_FragColor = vec4(GetFog(finalColor, fogFactor), diffColor.a);
        #else
            gl_FragColor = vec4(GetLitFog(finalColor, fogFactor), diffColor.a);
        #endif
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
            finalColor += texture2D(sEmissiveMap, vTexCoord2).rgb * cAmbientColor * diffColor.rgb;
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

        gl_FragData[0] = vec4(GetFog(finalColor, fogFactor), 1.0);
        gl_FragData[1] = fogFactor * vec4(diffColor.rgb, specIntensity);
        gl_FragData[2] = vec4(normal * 0.5 + 0.5, specPower);
        gl_FragData[3] = vec4(EncodeDepth(vWorldPos.w), 0.0);
    #else
        // Ambient & per-vertex lighting
        vec3 finalColor = vVertexLight * diffColor.rgb;
        #ifdef AO
            // If using AO, the vertex light ambient is black, calculate occluded ambient here
            finalColor += texture2D(sEmissiveMap, vTexCoord2).rgb * cAmbientColor * diffColor.rgb;
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

Seems to work:

[img]http://i.imgur.com/Cb5I5Xc.png[/img]

-------------------------

Tinimini | 2017-01-02 01:05:05 UTC | #8

By the way, if I want to write my own shaders, I suppose I need a new technique with that shader. But do these techniques and shaders need to be in the coredata folder, or is there a way to have my custom shaders and techniques in the Data folder in my own subfolder? Like I have my materials and textures etc.

-------------------------

GoogleBot42 | 2017-01-02 01:05:05 UTC | #9

They can be in the data folder too.  The two folders are simply resource directories that urho3d needs to run.  You can add your own directory with this command.
[code]GetSubsystem<ResourceCache>()->AddResourceDir("../../Assets");[/code]
So this would add a resource directory called Assets located two folders up.  If I have a folder located in "Textures" inside of this folder and a file called "Test.png" inside of this "Textures" folder I can load the texture with:
[code]cache->GetResource<Texture2D>("Textures/Test.png")[/code]
This even works if there are conflicting directories.  CoreData and Data and the added assets directory all have a "Textures" folder.  Urho3D just looks in each of these folders for a file called "Test.png"  I am not sure how Urho3D deals with conflicting files with the same name in the same sub-directory.

-------------------------

cadaver | 2017-01-02 01:05:05 UTC | #10

The VERTEXCOLOR shader change was also committed in the master branch.

In case of multiple resource directories having same file, the resource directory add order (priority) decides which gets loaded.

-------------------------

Tinimini | 2017-01-02 01:05:05 UTC | #11

Nice, thank you very much. I must say that this is a very helpful and friendly community you got here!

-------------------------

