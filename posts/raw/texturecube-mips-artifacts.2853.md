Bananaft | 2017-03-05 23:24:11 UTC | #1

1) I'm looking into PBRLitSolid.glsl and can't figure out how it changes the blurriness of Cubemap texture on materials with different roughness. I thought, it should select a particular mip level, but according to shader code it does not:
> finalColor += cMatEnvMapColor * textureCube(sEnvCubeMap, reflect(vReflectionVec, normal)).rgb;

2) I'm getting artifacts while trying to draw blurred cubemap. In deferred lighting mode I have a quad pass which reads normal and draws sky reflections into framebuffer.
>    vec3 reflcol = textureCube(sEnvCubeMap,normal,16.).rgb;

What I'm getting looks like biggest MIP is leaking:

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/a7b4c57b9263a876953a7a2902ec58052ba11171.png" width="690" height="365">

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/ba249da79d99a481c3d1131c21bd3eb1567c82f6.png" width="690" height="365">

-------------------------

1vanK | 2017-03-06 07:54:22 UTC | #2

```
        #ifdef ENVCUBEMAP
            finalColor += cMatEnvMapColor * textureCube(sEnvCubeMap, reflect(vReflectionVec, normal)).rgb;
        #endif
```

It has no direct relationship to the PBR (just identical part from default shaders, rudiment).

You need ImageBasedLighting() function

-------------------------

1vanK | 2017-03-06 05:33:15 UTC | #3

[quote="Bananaft, post:1, topic:2853"]
textureCube(sEnvCubeMap,normal,16.).rgb;
[/quote]

May be in texture only 10 miplevels?

-------------------------

Bananaft | 2017-03-06 07:53:09 UTC | #4

Thank you for pointing me in the right direction! In IBL.glsl it's textureLod not textureCube, and textureLod works perfectly.

> May be in texture only 10 miplevels?

Actually 8 :), and artifacts are visible on all of them, I just slapped higher number to make it more visible.

-------------------------

