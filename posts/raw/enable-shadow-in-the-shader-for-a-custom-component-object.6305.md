UrhoIsTheBest | 2020-08-09 06:18:36 UTC | #1

Sorry there would be lots of questions since I am not familiar with the rendering pipeline of Urho3D.

**Context**
I have a custom component to support CDLOD terrain. The heightmaps are passed to GPU and used for vertex displacement in shader. Now I want to support **shadow** for this terrain object. There are two parts:
1. The terrain surface can receive shadows casted from other objects; 
2. The terrain (mountains, hills) can cast shadow on the terrain surface itself.

Let's focus on the (1) part first.
I did some research on the existing Urho3D shaders/techniques/materials, and did some quick demo tests. I found the minimal would be one base pass and one light pass, for example:
```
<technique vs="CdlodTerrainShadow" ps="CdlodTerrainShadow" >
    <pass name="base" />
    <pass name="light" depthtest="equal" depthwrite="false" blend="add" />
</technique>
``` 
Also, I need to define ```PERPIXEL``` and ```SHADOW``` mutation in the shaders, just copy from those examples and it will be very similar. My shaders look like this:
```
void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = (0.02 * iPos* modelMatrix).xyz;

    float morph_k = GetMorphK(worldPos);
    worldPos.xz = GetMorphVertex((iPos.xz - iTexCoord7.xz), worldPos.xz, morph_k);

    float height = GetHeight(worldPos.xz);
    worldPos.y = height;
    gl_Position = GetClipPos(worldPos);

    // normalized to 0 ~ 1
    float normalized_height = GetNormalizedHeight(worldPos.y);
    vColor = GetColorFromNormalizedHeight(normalized_height);

    // calculate normals
    vNormal = GetNormal(worldPos.xz, 0.02);

    vTexCoord = worldPos.xz;
    vHeight = normalized_height;

    #ifdef PERPIXEL
    vWorldPos = vec4(worldPos, GetDepth(gl_Position));
        // Per-pixel forward lighting
        vec4 projWorldPos = vec4(worldPos, 1.0);
        #ifdef SHADOW
            // Shadow projection: transform from world space to shadow space
            for (int i = 0; i < NUMCASCADES; i++)
                vShadowPos[i] = GetShadowPos(i, vNormal, projWorldPos);
        #endif
    #endif
}

void PS()
{
    vec4 grass = texture(sTextureTerrainDetail10, vTexCoord);
//    vec4 stone = texture(sTextureTerrainDetail12, vTexCoord);
//    float weight = max(dot(vNormal, vec3(0, 1, 0)), 0.0);
//    vec4 final_details = grass * (1.0 - weight) + stone * weight;
//
//    vec4 main_texture_color = texture(sTextureMap4, vTexCoord / (cMapSize + cExtraMapSize));
//    float weight2 = texture(sTextureTerrainWeight11, vTexCoord).r;
    #if defined(PERPIXEL)
        vec4 diffColor = vec4(1.0);

        // Get normal
        vec3 normal = normalize(vNormal);

        // Per-pixel forward lighting
        vec3 lightColor;
        vec3 lightDir;
        vec3 finalColor;

        float diff = GetDiffuse(normal, vWorldPos.xyz, lightDir);

        #ifdef SHADOW
            diff *= GetShadow(vShadowPos, vWorldPos.w);
        #endif

        lightColor = cLightColor.rgb;
        finalColor = diff * lightColor * diffColor.rgb;
        gl_FragColor = vec4(finalColor, diffColor.a);
    //    gl_FragColor = (main_texture_color * (1 - weight2) + final_details * weight2 ) * diff * 2.0;
    //    gl_FragColor = vec4(1,0,0,1) * diff;
    //    gl_FragColor = vColor * diff;
    #endif
}
```

**The shaders are super straightforward but the whole terrain renders nothing! And there is no shader compile error.**

I spent a lot of time to debug this and finally noticed if I comment out
```
 vec4 grass = texture(sTextureTerrainDetail10, vTexCoord);
```
It would work.

Then I noticed the **TextureUnit = 10** is for ```SHADOWMAP```, which might conflict with the rendering pipeline.
```
enum TextureUnit
{
    TU_DIFFUSE = 0,
    TU_ALBEDOBUFFER = 0,
    TU_NORMAL = 1,
    TU_NORMALBUFFER = 1,
    TU_SPECULAR = 2,
    TU_EMISSIVE = 3,
    TU_ENVIRONMENT = 4,
...
    TU_VOLUMEMAP = 5,
    TU_CUSTOM1 = 6,
    TU_CUSTOM2 = 7,
    TU_LIGHTRAMP = 8,
    TU_LIGHTSHAPE = 9,
    TU_SHADOWMAP = 10,
    TU_FACESELECT = 11,
    TU_INDIRECTION = 12,
    TU_DEPTHBUFFER = 13,
    TU_LIGHTBUFFER = 14,
    TU_ZONE = 15,
    MAX_MATERIAL_TEXTURE_UNITS = 8,
    MAX_TEXTURE_UNITS = 16
...
};
```

I also noticed if I use ```vColor``` in the PS, the terrain would be empty. Turns out the ```vColor``` is derived from a texture unit 9 I passed to shader.

So 
**Question 1: Are all those texture unit already reserved for particular use, and we should NOT use them to pass our own textures? like I am doing here:**
```
<material>
    <technique name="Techniques/CdlodTerrain.xml" />
<!--    <technique name="Techniques/Diff.xml" />-->
    // unit [0, 3] are reserved for heightmap textures.
    <texture unit="0" name="" />
    <texture unit="1" name="" />
    <texture unit="2" name="" />
    <texture unit="3" name="" />
    // unit 4 is reserved for earth vegetation texture map.
    <texture unit="4" name="" />
    <texture unit="5" name="" />
    <texture unit="6" name="HeightMapsTest/DEM_print.png" />
    <texture unit="7" name="" />
    <texture unit="8" name="" />
    <texture unit="9" name="" />
<!--    <texture unit="10" name="Textures/TerrainDetail1.dds" />-->
<!--    <texture unit="10" name="TerrainTextures/forest.jpg" />-->
    <texture unit="10" name="Textures/StoneDiffuse.dds" />
    <texture unit="11" name="TerrainTextures/aerial_grass_rock_disp_1k.png" />
    <texture unit="12" name="Textures/StoneDiffuse.dds" />
    <parameter name="MyCameraPos" value = "0 0 0" />
    <parameter name="HeightMinMaxScale" value="0 0 0" />
    <parameter name="MapSize" value="1 1" />
    <parameter name="ExtraMapSize" value="1 1" />
</material>
```
**So we can only use 6 and 7? What if we have more textures?**

**Question 2: Should this generator a shader compile error?**


-----------------------------------------------------------------------------------------

Now the terrain can receive shadow casted from other objects, although I don't know how to pass more textures to the shader later.
![Screenshot_Sat_Aug__8_22_40_15_2020|690x459](upload://ikYyGLswgAojaEirIpXaBUVBTS6.jpeg) 
**Question 3: How to enable terrain cast shadow on itself?**
I set my terrain component (which is inherited from ```Urho3D::Drawable```)
```
  SetCastShadows(true);
```
I also added another ```pass```:
```
<technique vs="CdlodTerrainShadow" ps="CdlodTerrainShadow" >
    <pass name="base" />
    <pass name="light" depthtest="equal" depthwrite="false" blend="add" />
    <pass name="shadow" vs="Shadow" ps="Shadow" />
</technique>
```
Those exact setting would work on the native ```Urho3D::Terrain``` object, but it does not work on my terrain.
**What did I miss?**

----------------------------------------------------------------------------------------------

PS: 
I feel it's really hard for me to learn through the code given lack of detailed documentation & tutorials.
Especially, consider I am even a professional software engineer in one of those big name companies (though I am not a specialist in 3D rendering&gaming). So I guess it would be even harder for people who are self learning those stuff. 
I recently spent 1~2 weeks studying most the [LearnOpenGL Book](https://learnopengl.com/Introduction), which is a **GREAT** tutorial in every aspect. But I still lack the domain knowledge about all those **rendering pass**. I also finished an online 3D graphics course (just read through those slides, lectures).
I wish there would be more tutorials and detailed documentation about those topics, especially the Urho3D implementations. The official [documentation](https://urho3d.github.io/documentation/1.6/_render_paths.html) is still far from enough.
For example, for this light pass:
```
 <pass name="light" depthtest="equal" depthwrite="false" blend="add" />
```
Where is the source code to do the real work? where is the code to write shadow map? etc.

**Could someone provide more materials on 3D game engine rendering pipeline? How did you guys become an expert on those topics and know all the nitty details in Urho3D engine?**

-------------------------

Modanung | 2020-08-09 20:15:26 UTC | #2

4 posts were split to a new topic: [Mysterious profile](/t/mysterious-profile/6309)

-------------------------

kannsokusha | 2020-08-11 02:33:13 UTC | #5

I added a lot of texture units and wasted a lot of GPU memory. :sweat_smile:

    /// Texture units.
    enum TextureUnit
    {
        TU_DIFFUSE = 0,
        TU_ALBEDOBUFFER = 0,
        TU_NORMAL = 1,
        TU_NORMALBUFFER = 1,
        TU_METALLIC = 2,
        TU_ROUGHNESS = 3,
        TU_OCCLUSION = 4,
        TU_EMISSIVE = 5,
        TU_ENVIRONMENT = 6,
    #ifdef DESKTOP_GRAPHICS
        TU_VOLUMEMAP = 7,
        TU_LIGHTRAMP = 8,
        TU_LIGHTSHAPE = 9,
        TU_SHADOWMAP = 10,
        TU_FACESELECT = 11,
        TU_INDIRECTION = 12,
        TU_DEPTHBUFFER = 13,
        TU_LIGHTBUFFER = 14,
        TU_ZONE = 15,
        TU_RADIANCE = 16,
        TU_IRRANIANCE = 17,
        MAX_MATERIAL_TEXTURE_UNITS = 8,
        MAX_TEXTURE_UNITS = 18
    #else
        TU_LIGHTRAMP = 7,
        TU_LIGHTSHAPE = 8,
        TU_SHADOWMAP = 9,
        MAX_MATERIAL_TEXTURE_UNITS = 7,
        MAX_TEXTURE_UNITS = 10
    #endif
    };

-------------------------

weitjong | 2020-08-11 11:25:12 UTC | #7

Please start a fresh topic and keep it on topic.

-------------------------

weitjong | 2020-08-14 13:24:04 UTC | #9

Reopening the topic (as per requested by OP) after all offending posts being deleted.

-------------------------

UrhoIsTheBest | 2020-08-15 03:34:33 UTC | #10

That's not a scalable solution though, and it needs to modify source code and recompile. Also, are you using those extra textures the way as their semantic names? or whatever you want. My GPU only supports max 16 I think.

-------------------------

kannsokusha | 2020-08-17 03:08:34 UTC | #11

Yes，I using those as their semantic names. It's convenient for me to test my shader.

-------------------------

