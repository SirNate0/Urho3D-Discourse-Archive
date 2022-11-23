kannsokusha | 2021-04-14 04:02:15 UTC | #1

When I use 3d ui,  the render texture's rgba has been multiply by alpha. Are there any options? or is an issue?
![1|636x499, 50%](upload://d8h6Icdi847L0Rwtudsvi2PGXcF.png) ![2|636x499, 50%](upload://mLYxgkSlBXSnq8Z3yIzWsNEg6eb.png)

-------------------------

SirNate0 | 2021-04-14 04:14:54 UTC | #2

Isn't that the expected behavior? What else would you expect alpha to do?

-------------------------

kannsokusha | 2021-04-14 04:18:24 UTC | #3

Left image is UI, right is 3D UI, I think their color should be same.

-------------------------

SirNate0 | 2021-04-14 04:59:18 UTC | #4

I see. I thought they were just two different values of alpha. In that case hopefully someone else has a better idea of how to fix it. Maybe the 3D UI drawable is setting the color to the value with alpha in it or something like that?

-------------------------

Modanung | 2021-04-14 06:56:52 UTC | #5

What's does the material you're using in 3D look like internally?

-------------------------

Eugene | 2021-04-14 08:43:37 UTC | #6

TL;DR: Write your own UI shader.

This issue is deep and I don’t see any easy fix.
The issue stems from the fact that alpha is used in two different ways on rendering. First, it’s the input for alpha blending, controlled by BlendMode. Second, alpha is written to alpha channel of output texture unconditionally. Output alpha channel is never used during alpha blending, but it’s used e.g. during deferred rendering.

So you basically want to write output alpha in some cases (deferred rendering), but don’t want to do it in other cases (UI rendering). But Urho doesn’t expose alpha combination API, so you have no choice but to write alpha. Which may have side effects if you later render this texture with shader that cares about alpha.

-------------------------

kannsokusha | 2021-04-14 12:37:38 UTC | #7

Continuing the discussion from [Problem with alpha in 3D UI](https://discourse.urho3d.io/t/problem-with-alpha-in-3d-ui/6807/6):

Thanks @Eugene , @Modanung , @SirNate0 . I can use custom shader to make it look right. But I think it is magic. :slightly_smiling_face:
The original shader: Unlit.glsl

    gl_FragColor = vec4(GetFog(diffColor.rgb, fogFactor), diffColor.a);

New shader :UnlitFor3DUI.glsl

    gl_FragColor = vec4(GetFog(diffColor.rgb, fogFactor), diffColor.a) / sqrt(diffColor.a);

-------------------------

