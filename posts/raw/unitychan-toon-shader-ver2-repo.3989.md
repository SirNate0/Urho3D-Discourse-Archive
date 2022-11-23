Lumak | 2018-02-04 23:19:39 UTC | #1

Anyone interested in Unity Chan toon shader tech, here's the repo - https://github.com/Lumak/UnityChanToonShaderVer2

I briefly looked over the English manual but haven't done anything with it because I'm a novice graphics programmer.

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/5/566f43aac8403ac81c1aeae1725e03613eb7b99f.jpg[/img]

-------------------------

Lumak | 2018-02-04 19:36:49 UTC | #2

Let me add that I at least created a scene to view the model in the editor :slight_smile:.

-------------------------

Lumak | 2018-02-04 19:50:28 UTC | #3

I'd like to request @1vanK and @rasteron to take a look and give their opinion on the tech. if possible.

-------------------------

1vanK | 2018-02-05 08:31:10 UTC | #4

I've already posted a similar shader on old forum https://discourse.urho3d.io/t/toon-shader-wip/1564/11 (without outline) but when the forum moved the pictures were lost. Also somewhere on the computer I had a modified version, but I have a real dump here, I'll post it when I find it

EDIT: http://dropmefiles.com/1fZer

-------------------------

1vanK | 2018-02-05 09:15:24 UTC | #5

Some notes to understand how it works:
default diffuse shader - smooth gradient from 0 to 1
```
dot(normal, lightDir) // [-1, 1]
// should be  clamped to [0, 1] 
// return max(dot(normal, lightDir), 0.0);
```
toon shader - hard gradient taked from texture:
```
float NdotL = dot(normal, lightDir) * 0.5 + 0.5; // [-1, 1] to [0, 1]
return texture2D(sEnvMap, vec2(NdotL, 0.0)).r;
```
![ToonRamp|256x16](upload://w8knOS454UYvb2v1Uc2QLQ4HPz4.jpg)

-------------------------

1vanK | 2018-02-05 09:10:57 UTC | #6

 https://github.com/Lumak/UnityChanToonShaderVer2/blob/master/Assets/Toon/Shader/UCTS_Outline.cginc

It seems shader use scaling along normal method for outline: https://discourse.urho3d.io/t/outline-v2/1766/19?u=1vank
and scale value taked from texture https://github.com/Lumak/UnityChanToonShaderVer2/blob/master/Assets/Toon/Textures/utc_all2_outlinesmpler.png

-------------------------

rasteron | 2018-02-05 11:57:26 UTC | #7

Hey Mak, I'm not that quite familiar with cg/hlsl, so perhaps someone with more cg/hlsl knowledge can port this over and yes 1vank's version looks similar.

Having a quick look at the files, it seems there are other effects going on there other than toon and also uses Sobel filters.

https://github.com/Lumak/UnityChanToonShaderVer2/blob/master/Assets/Standard%20Assets/Effects/ImageEffects/Shaders/EdgeDetectNormals.shader

cheers.

-------------------------

Lumak | 2018-02-05 17:10:47 UTC | #8

@1vanK, @rasteron thanks for your feedback. There's a lot of information to digest. I just opened this in Unity editor ver 5.6.5f1 and it re-imported the project saying something about previous save was an older version  and I can see the both toon shader versions working.  That's gonna be a big help.

-------------------------

Sinoid | 2018-02-07 12:15:05 UTC | #9

Sobel is just two 3x3 kernels put together.

You just need a depth buffer to process:

    #define SOBEL_STEP_SIZE ???
    #define SAMPLE_SOBEL(NAME, X, Y) float NAME = texture2D(sDepthBuffer, vec2(coord.x + X*SOBEL_STEP_SIZE, coord.y + Y*SOBEL_STEP_SIZE));
    SAMPLE_SOBEL(l, -1.0, 0.0);
    SAMPLE_SOBEL(r, 1.0, 0.0);
    SAMPLE_SOBEL(t, 0.0, -1.0);
    SAMPLE_SOBEL(b, 0.0, 1.0);
    SAMPLE_SOBEL(tl, -1.0, -1.0);
    SAMPLE_SOBEL(tr, 1.0, -1.0);
    SAMPLE_SOBEL(bl, -1.0, 1.0);
    SAMPLE_SOBEL(br, 1.0, 1.0);

    float dX = tr + 2 * r + br - tl - 2 * l - bl;
    float dY = bl + 2 * b + br - tl - 2 * t - tr;
    float sobelEdge = 1.0 - (dX * dY); // 1.0 - N for black edges, N for white

-------------------------

