1vanK | 2019-03-30 09:50:38 UTC | #1

https://www.youtube.com/watch?v=HrtpaTctthc

This method allow transparency without alpha pass

Shader LitSolid.glsl
```
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

    // ================= BEGIN ==========

    #if defined(SCREENDOOR) && !defined(ALPHAMASK)
        mat4 threshold = mat4
        (
            1.0 / 17.0,   9.0 / 17.0,   3.0 / 17.0,   11.0 / 17.0,
            13.0 / 17.0,  5.0 / 17.0,   15.0 / 17.0,  7.0 / 17.0,
            4.0 / 17.0,   12.0 / 17.0,  2.0 / 17.0,   10.0 / 17.0,
            16.0 / 17.0,  8.0 / 17.0,   14.0 / 17.0,  6.0 / 17.0
        );
        int x = int((gl_FragCoord.x + 1.0) * 0.5 / cGBufferInvSize.x);
        int y = int((gl_FragCoord.y + 1.0) * 0.5 / cGBufferInvSize.y);
        if (diffColor.a < threshold[x % 4][y % 4])
            discard;
    #endif
```

Material MushroomScreenDoorTransparency.xml
```
<material>
    <technique name="Techniques/Diff.xml" />
    <texture unit="diffuse" name="Textures/Mushroom.dds" />
    <parameter name="MatSpecColor" value="0.1 0.1 0.1 16" />
    
    <shader psdefines="SCREENDOOR"/>
    <parameter name="MatDiffColor" value="1.0 1.0 1.0 0.5" />
</material>
```

Reference: https://digitalrune.github.io/DigitalRune-Documentation/html/fa431d48-b457-4c70-a590-d44b0840ab1e.htm

-------------------------

1vanK | 2019-03-30 20:18:08 UTC | #2

Fixed version with more square pattern:

```
    #if defined(SCREENDOOR) && !defined(ALPHAMASK)
        mat4 threshold = mat4
        (
            1.0 / 17.0,   9.0 / 17.0,   3.0 / 17.0,   11.0 / 17.0,
            13.0 / 17.0,  5.0 / 17.0,   15.0 / 17.0,  7.0 / 17.0,
            4.0 / 17.0,   12.0 / 17.0,  2.0 / 17.0,   10.0 / 17.0,
            16.0 / 17.0,  8.0 / 17.0,   14.0 / 17.0,  6.0 / 17.0
        );
        int x = int(gl_FragCoord.x - 0.5);
        int y = int(gl_FragCoord.y - 0.5);
        if (diffColor.a < threshold[x % 4][y % 4])
            discard;
    #endif
```

-------------------------

smellymumbler | 2019-03-30 15:23:54 UTC | #3

That's so cool! Is that your game?

-------------------------

1vanK | 2019-03-30 18:05:20 UTC | #4

> That’s so cool! Is that your game?

no, just example of using

-------------------------

