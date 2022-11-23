GoogleBot42 | 2017-03-18 02:12:41 UTC | #1

So I am learning to write shaders in general and also learning the Urho3D way of doing them.

Looking at the shaders that Urho3D already has implemented helps a bit.  So I looked at TexturedUnlit.xml and Unlit.glsl and saw that it uses multiple passes in the fragment shader.

During the passes where it is not writing to gl_FragColor it is writing to gl_FragData at a few set positions in the array.

[code]
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
[/code]

So my question is what is gl_FragData being used for?  If I take out the other passes the shader seems to work just fine.  It does not seem to be read in later passes so I guess it is probably sending data back to urho3d for some purpose.  But I am just not sure.  Any help would be appreciated.  Thanks!

-------------------------

Eugene | 2017-03-18 02:12:16 UTC | #2

This is a question about GLSL, not Urho3D.

FragData is an array counterpart of FragColor. Outside both FragData and FragColor just fill corresponding pixels of corresponding render targets.

-------------------------

GoogleBot42 | 2017-01-08 09:01:58 UTC | #3

Alright.  What is the shader doing in the other passes?

-------------------------

1vanK | 2017-01-08 10:07:31 UTC | #4

It is "Multiple render Targets".

```
    #if defined(PREPASS)
        // Fill light pre-pass G-Buffer
        gl_FragData[0] = vec4(0.5, 0.5, 0.5, 1.0);
        gl_FragData[1] = vec4(EncodeDepth(vWorldPos.w), 0.0);
```
filled two textures that used in CoreData\RenderPaths\Prepass*.xml
```
    <command type="scenepass" pass="prepass" marktostencil="true" metadata="gbuffer">
        <output index="0" name="normal" />
        <output index="1" name="depth" />
    </command>
```

And
```
#elif defined(DEFERRED)
        gl_FragData[0] = vec4(GetFog(diffColor.rgb, fogFactor), diffColor.a);
        gl_FragData[1] = vec4(0.0, 0.0, 0.0, 0.0);
        gl_FragData[2] = vec4(0.5, 0.5, 0.5, 1.0);
        gl_FragData[3] = vec4(EncodeDepth(vWorldPos.w), 0.0);
    #else
```
filled 4 textures for  CoreData\RenderPaths\Deferred*.xml
```
    <command type="scenepass" pass="deferred" marktostencil="true" vertexlights="true" metadata="gbuffer">
        <output index="0" name="viewport" />
        <output index="1" name="albedo" />
        <output index="2" name="normal" />
        <output index="3" name="depth" />
    </command>
```

Defualt used Forward.xml and this code just ignored. You can delete this :)

-------------------------

1vanK | 2017-03-18 02:12:16 UTC | #5

[quote="GoogleBot42, post:3, topic:2685, full:true"]
Alright.  What is the shader doing in the other passes?
[/quote]

Urho3D used combination of defines for every passe for turn on and turn off fragments of code (Ubershader approach). So this code not exists for another passes except "prepass" and "deferred"

-------------------------

GoogleBot42 | 2017-01-08 19:41:27 UTC | #6

Huh, that is pretty cool!  Thanks 1vanK!  I will start to play with render paths a bit.  Fortunately, there is a page in the documentation on them.  I didn't even know about them before.

-------------------------

