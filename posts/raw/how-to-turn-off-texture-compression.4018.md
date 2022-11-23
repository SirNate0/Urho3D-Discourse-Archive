ChunFengTsin | 2018-02-15 07:17:35 UTC | #1

Hello , every one!

I  I've succeeded in drawing chunks dynamic, but the texture is fuzzy.

Look this:

![2018-02-15%2014-09-07%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE|690x410](upload://xjsV9N5kYuWHdmMt7LDRVgiOnHK.jpg)

This is original texture:

![2018-02-15%2014-11-15%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE|690x268](upload://wj5fSnsHWpM8Fm9W6NiHsoorLfI.png)


   Here are  simple Material , Technique  and a Shader.

GrassMaterial:

    <material>
    <technique name="Techniques/GrassTech.xml" />
    <texture unit="diffuse" name="Textures/texture.png" />
    </material>


GrassTech:

    <technique vs="GrassSL" ps="GrassSL" psdefines="DIFFMAP" >
    <pass name="base" />
    <pass name="prepass" psdefines="PREPASS" />
    <pass name="material" />
    </technique>

GrassSL:

    #include "Uniforms.glsl"
    #include "Samplers.glsl"
    #include "Transform.glsl"
    #include "ScreenPos.glsl"
    #include "Fog.glsl"

    varying vec2 vTexCoord;
    varying vec4 vWorldPos;
    #ifdef VERTEXCOLOR
        varying vec4 vColor;
    #endif

    void VS()
    {
        mat4 modelMatrix = iModelMatrix;
        vec3 worldPos = GetWorldPos(modelMatrix);
        gl_Position = GetClipPos(worldPos);
        vTexCoord = GetTexCoord(iTexCoord);
        vWorldPos = vec4(worldPos, GetDepth(gl_Position));

        #ifdef VERTEXCOLOR
            vColor = iColor;
        #endif
    }

    void PS()
    {
        // Get material diffuse albedo
        #ifdef DIFFMAP
            vec4 diffColor = cMatDiffColor * texture2D(sDiffMap, vTexCoord);
            #ifdef ALPHAMASK
                if (diffColor.a < 0.5)
                    discard;
            #endif
        #else
            vec4 diffColor = cMatDiffColor;
        #endif

        #ifdef VERTEXCOLOR
            diffColor *= vColor;
        #endif

        // Get fog factor
        #ifdef HEIGHTFOG
            float fogFactor = GetHeightFogFactor(vWorldPos.w, vWorldPos.y);
        #else
            float fogFactor = GetFogFactor(vWorldPos.w);
        #endif

        #if defined(PREPASS)
            // Fill light pre-pass G-Buffer
            gl_FragData[0] = vec4(0.5, 0.5, 0.5, 1.0);
            gl_FragData[1] = vec4(EncodeDepth(vWorldPos.w), 0.0);
        #elif defined(DEFERRED)
            gl_FragData[0] = vec4(GetFog(diffColor.rgb, fogFactor), diffColor.a);
            gl_FragData[1] = vec4(0.0, 0.0, 0.0, 0.0);
            gl_FragData[2] = vec4(0.5, 0.5, 0.5, 1.0);
            gl_FragData[3] = vec4(EncodeDepth(vWorldPos.w), 0.0);
        #else
            gl_FragColor = vec4(GetFog(diffColor.rgb, fogFactor), diffColor.a);
        #endif
    }


so, I have two question:
 
1. How to show original texture on cube?

2. As you can see,  there is no shadow now , I want to calculate it manually, have not use Urho3D's Light.
that's like i calculate a value " shadowValue " (0< shadowValue < 1),
now I want to do this: 

    vec4 diffColor = cMatDiffColor * texture2D(sDiffMap, vTexCoord) * shadowValue ;

    is that right? 
    If OK, how I pass the shdowValue to Shader?

-------------------------

Sinoid | 2018-02-15 16:09:29 UTC | #2

**1)** That's not compression. It's filtering, you have to add an XML file for your texture to set it.

https://urho3d.github.io/documentation/1.7/_materials.html

Read the entire page. It answers both of these questions.

**2)** If you want the illusion of a global light then use something like:

`float shadowValue = clamp(dot(iNormal, -cFakeLightDirection), 0.4, 1.0);`

To add your own custom `cFakeLightDirection` you just add a uniform to the shader and then set in the XML using a `parameter` element. In the shader the name **MUST** start with **c** so `cFakeLightDirection` but in the material XMl/editor you set it as `FakeLightDirection`.

-------------------------

ChunFengTsin | 2018-02-15 09:11:43 UTC | #3

Thanks very much , I will try later.
But I also have a question about cMatDiffColor and sDiffMap , I can not find links about them in Document .
Can you offer me links , or give me a  simple explanation of them.

-------------------------

Sinoid | 2018-02-15 09:56:04 UTC | #4

Those are built-ins in the sample shaders. cMatDiffColor comes from `Uniforms.hlsl/glsl` and sDiffMap from `Samplers.hlsl/glsl`. Nothing magical there.

One is a uniform that comes from a material and the other a sampler.

-------------------------

ChunFengTsin | 2018-02-15 11:58:52 UTC | #5

En, Thanks , 
Today is  the new year's Eve of Chinese.
"May the five blessings come to you"

-------------------------

