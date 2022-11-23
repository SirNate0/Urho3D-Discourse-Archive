Lumak | 2020-06-01 01:14:53 UTC | #1

Finally got around to making it work
right side view
[img]https://i.imgur.com/CU4Solo.png[/img]

Had to finagle TBN matrix to obtain a proper parallax occlusion.

Lighting normal correction
[img]https://i.imgur.com/d91oD68.png[/img]

-------------------------

Lumak | 2020-05-31 23:19:03 UTC | #2

Repo published - https://github.com/Lumak/Urho3D-ParallaxOcclusionMap

Let me know  if there's some files missing.

-------------------------

Lumak | 2020-06-01 00:55:21 UTC | #3

Updated the repo with lighting normal correction.

-------------------------

Miegamicis | 2020-06-01 06:34:40 UTC | #4

If there would be a "Hall of fame" section in the forums, your name would be at the top of it! Nice work! It's always awesome to see what you have prepared. :+1:

-------------------------

elix22 | 2020-06-01 06:45:56 UTC | #5

Very cool demo .
I made a small modification to pass GLSL compilation on Android
https://github.com/elix22/Urho3D/blob/master/bin/Data/Parallax/Shaders/GLSL/Parallax.glsl

-------------------------

lebrewer | 2020-06-01 17:48:32 UTC | #6

This is fantastic. Thanks a lot for the awesome work, @Lumak! :heart_eyes:

-------------------------

Lumak | 2020-06-02 00:13:01 UTC | #7

Glad ppl like this repo, I think this was something that's been over due by several years.

@elix22 Let me know what the change is or I can't take look at your changes in your fork.

-------------------------

elix22 | 2020-06-02 06:29:42 UTC | #8

It applies both for iOS and Android .
The change is  in **Parallax.glsl**

Add  at the top:

    #ifdef MOBILE_GRAPHICS
        precision mediump float;
    #else
        precision highp float;
    #endif

change from :

    const float minLayers = 8;
    const float maxLayers = 36;

change to :

    float minLayers = 8.0;
    float maxLayers = 36.0;

change from :

        if ( fDenominator == 0.0f )
        {
           fParallaxAmount = 0.0f;
        }	

change to :

        if ( fDenominator == 0.0 )
        {
           fParallaxAmount = 0.0;
        }

-------------------------

lebrewer | 2020-06-02 15:57:59 UTC | #9

can it work with terrains?

-------------------------

Lumak | 2020-06-04 04:19:25 UTC | #10

I couldn't just answered the question but had to try it. And the answer is, you can do parallax mapping on terrain with limitations. This is because detail textures requires displacement and normal map. If you were to do that with 1-weight map and 3-detail textures, that would mean you'll need total of 10 textures. That'll be problematic, however, you can do it with 2 detail textures. Texture detail list:
1-weight map
2-detailmap1 with displacement(heightmap) embedded in alpha channel
3-detailmap2 with displacement(heightmap) embedded in alpha channel
4-normalmap1 for detailmap1
5-normalmap2 for detailmap2

~~Very restrictive but do-able. Here's a test that I did.~~ Nope. this is not right.
conclusion: the very first image, which is edited out, has only normal map applied and no matter what I tried, parallax mapping fails due to varying normals, even if you fix the tangents and bitangents some parts of the terrain becomes distorted. So, parallax mapping will not work, but normal map will.

@elix22 thank you for that. I'll update the repo with your changes.

-------------------------

Lumak | 2020-06-05 14:50:12 UTC | #11

Updated the repo: bug fix for parallaxLength computation, added elix22's android changes, added saint images.
and another pic
[img]https://i.imgur.com/pQe6Rge.png[/img]

-------------------------

GoldenThumbs | 2020-06-05 20:21:03 UTC | #12

Is this just an adaption of the shader on [Learn OpenGL](https://learnopengl.com/Advanced-Lighting/Parallax-Mapping) or totally rewritten yourself? I mean, seeing as this is an established technique there's going to be a lot of similarities lol.

I also wrote an [Urho3D version of that shader](https://discourse.urho3d.io/t/parallax-mapping/4754) from Learn OpenGL awhile ago. Don't think I ever made a Github repo for it though. Anyway, it's nice seeing someone else trying this effect.

-------------------------

Lumak | 2020-06-06 12:31:08 UTC | #13

I had no idea about your work. I wish I had known about it; that would've save me the trouble writing one. The shader code in my work is from DirectX SDK, along with the textures.

-------------------------

elix22 | 2020-06-07 07:56:36 UTC | #14

@Lumak you missed a small change.
const int assignment into float will fail on some android devices 

```
float minLayers = 8;
float maxLayers = 36;
```

change to :

```
float minLayers = 8.0;
float maxLayers = 36.0;
```


For those that would like to try it on an Android device,
I generated an Android apk with all the samples , this one included.
https://drive.google.com/file/d/19_feFQS18ePSScwtw-7ynj5XWuFLEtoS/view?usp=sharing

-------------------------

Lumak | 2020-06-07 23:36:54 UTC | #15

@elix22 Alright, I'll make another update with those changes.

Ever since I've started on this project, I wondered about two things:
   1 - I was puzzled by why the tangent and bitangent vectors needed to be swapped and negated to construct the TBN matrix, i.e.
```
mat3 tbn = mat3(-vec3(vTexCoord.zw, vTangent.w), -vTangent.xyz, vNormal);
```
to make this work. 


 2  - why when the orientation of the face changed, the parallax offset got skewed.

I finally figured it out. Of all the primitive models that we have in Data/Models folder, the Plane.mdl is the only model with the incorrect tangents. I pre-dumped every model's tangent vectors and post-dumped them again after calling **GenerateTangents()** fn Plane.mdl currently stores bitangent vectors in tangent vector data.

The second problem -- I've looked over the DirectX sample over and over again and didn't see where I made a bad copy or translated HLSL incorrectly. Just another puzzle I couldn't figure out. Then after looking at the Learn OpenGL version of the shader that @GoldenThumbs pointed out, I realize the transpose() could be inherent in the HLSL but needed to explicitly applied in GLSL. And sure enough, that solved the problem.

These two problems fixes the following problems:
1-- cube parallax occlusion 
[img]https://i.imgur.com/GDBtwgI.png[/img]

2-- terrain parallax occlusion
[img]https://i.imgur.com/NzRibEz.jpg[/img]

I have these test codes in several folders. I'll collect them and add them to the repo in a day or two.

-------------------------

GoldenThumbs | 2020-06-08 01:23:07 UTC | #16

Glad I could help! Also, ay I ask where you got that terrain shader? Is this the @JTippetts terrain shader (with some modifications made by you for the POM)?

-------------------------

Lumak | 2020-06-08 01:36:30 UTC | #17

Repo updated, as I don't think I'll have the time to update it after today.

@GoldenThumbs It's a modified version of the default TerrainBlend shader that comes with Urho3D.

-------------------------

GoldenThumbs | 2020-06-08 02:43:16 UTC | #18

By the way I found that [issue with the plane model](https://discourse.urho3d.io/t/whats-with-normal-maps/5364/4?u=goldenthumbs) a while ago. Should have been fixed by now given how there's no benefit to having a default model with faulty tangents and the fix is very easy.

Edit: could one do a PR for art assets? I might just do it myself.

-------------------------

elix22 | 2020-06-08 09:26:49 UTC | #19

@Lumak thanks for the demo.

Small note, transpose is not supported on mobile devices 
I added local **transpose(in mat3 inMatrix)**  implementation on my side 

https://github.com/elix22/Urho3D/blob/master/bin/Data/Parallax/Shaders/GLSL/LitSolidParallax.glsl


Also updated the Android APK
https://drive.google.com/file/d/19_feFQS18ePSScwtw-7ynj5XWuFLEtoS/view?usp=sharing

-------------------------

Lumak | 2020-06-09 15:22:58 UTC | #20

@elix22 Thanks, again. Added that function to repo.

@GoldenThumbs Typical procedure is to make the changes to SourceAssets/ *.blend files and that'll generate the *.mdl files.  Maybe @1vanK can investigate what's wrong with the Plane.blend file to see why it's generating erroneous tangents.

-------------------------

1vanK | 2020-06-10 01:06:59 UTC | #21

*.blend have tangents but *.mdl was changed later: https://github.com/urho3d/Urho3D/commit/16eea3949961fe6798b2ed63ea1b72d19eceac4b

Can you test this file https://dropmefiles.com/KThBy

-------------------------

Lumak | 2020-06-10 01:36:54 UTC | #22

The one from your dropmefiles.com works perfectly. The updated one -- 16eea3949961fe6798b2ed63ea1b72d19eceac4b, didn't work properly.

-------------------------

coldev | 2020-06-10 18:59:43 UTC | #23

nice assets , thanks :grin:

-------------------------

Modanung | 2020-06-22 23:07:01 UTC | #24

Maybe try it with some [Texture Haven](https://texturehaven.com/textures/) assets and PBR?

-------------------------

