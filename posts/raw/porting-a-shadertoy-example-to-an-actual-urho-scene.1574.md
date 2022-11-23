namic | 2017-01-02 01:08:35 UTC | #1

I'm trying to learn more about shaders and i started by trying to port this skydome shader into Urho3D: [shadertoy.com/view/4tf3RM](https://www.shadertoy.com/view/4tf3RM)

How do i return a fragColor to Urho3D?

-------------------------

codingmonkey | 2017-01-02 01:08:35 UTC | #2

There is two technics what use for sky
-DiffSkybox.xml
-DiffSkyplane.xml
You need copy one of them for example : new DiffShadertoySky.xml then look into this new copy on first line you will see
[code]<technique vs="Unlit" ps="Unlit" psdefines="DIFFMAP">[/code]
This tech use std unlit(glsl/hlsl) shader with one definition for pixel shader DIFFMAP.
you may change this name to UnlitShadertoy
finally you got something like this:
[code]<technique vs="UnlitShadertoy" ps="UnlitShadertoy" vsdefines="MYDEFINITIONFORVS"> psdefines="DIFFMAP MYDEFINITIONFORPS" [/code]

then you must go to CoreData\Shaders\GLSL(hlsl) and try to find Unlit.glsl copy it into UnlitShadertoy.glsl

Now you are free to modifying your own shader, also you have a tech what using it for rendering (DiffShadertoySky.xml)

>How do i return a fragColor to Urho3D?
well, at the end of shader file few places return color for different RenderPath types
but in generic, all RPs does this
gl_FragColor = vec4(GetFog(diffColor.rgb, fogFactor), diffColor.a);

I think you may keep your calculations just little upper then this end block 
[code]   #if defined(PREPASS)
        // Fill light pre-pass G-Buffer
        gl_FragData[0] = vec4(0.5, 0.5, 0.5, 1.0);
        gl_FragData[1] = vec4(EncodeDepth(vWorldPos.w), 0.0);
    #elif defined(DEFERRED)
        gl_FragData[0] = vec4(GetFog(diffColor.rgb, fogFactor), diffColor.a);
        gl_FragData[1] = vec4(0.0, 0.0, 0.0, 0.0);
        gl_FragData[2] = vec4(0.5, 0.5, 0.5, 1.0);
        gl_FragData[3] = vec4(EncodeDepth(vWorldPos.w), 0.0);
    #else
        #ifndef OUTMRT01 
            gl_FragColor = vec4(GetFog(diffColor.rgb, fogFactor), diffColor.a);
        #else
            gl_FragData[0] = vec4(GetFog(diffColor.rgb, fogFactor), diffColor.a);
            gl_FragData[1] = vec4(1.0, 1.0, 1.0, 1.0);
        #endif
    #endif [/code]

and final your color pass into diffColor

-------------------------

