Lumak | 2017-12-07 21:11:38 UTC | #1

Early Merry Christmas, repo: https://github.com/Lumak/Urho3D-Lightmap

-------------------------

Lumak | 2017-12-02 05:41:39 UTC | #2

Update the roomScene.xml to make the baked texture seamless.

-------------------------

Dave82 | 2017-12-02 05:44:34 UTC | #3

Looks great ! is there a way to bake some indirect lighting too ? Like AO and GI ? If yes or there's EVEN a plan to implement it i will switch to this right away !

-------------------------

Lumak | 2017-12-02 06:19:58 UTC | #4

Direct lighting only:
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/4/4c5f489dda92ddbe97a6cc7be26f5b589e16cb24.png[/img]
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/d/d31b4cb94eccf721d37e4a990b29f20eb3db3608.png[/img]

press **F5** to start the light process and once complete, technique is changed to xxLightMap and the results should look like this with indirect lighting... unless I forgot to check something in.
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/4/4f0377a807b8d2c968ae765148b0e9002d049f98.png[/img]
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/f/fea1dbea8cbcef81f0f9ded98efa72a726fb3e46.png[/img]

-------------------------

dakilla | 2017-12-02 10:45:22 UTC | #5

Nice work, thanks for sharing ;)

-------------------------

Lumak | 2017-12-02 22:03:32 UTC | #6

I managed to write bake indirect lighting code and capture, but what's captured is not what I expect. It looks like just a larger version of the lightmap instead of direct+indirect+shadows.  Is that what you expect?

It might help you understand if I posted some images.

edit: nvm, indirect baked texture = diffuse texture + indirect lighting.  The lightmap is just indirect lighting, no texture. Anyway, indirect process is in the repo.

direct bake
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/a/a6fd6181789aec7a734b5f14255b02fcfa3ffafc.png[/img]

lightmap
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/a/a95414bbb52ab0a5bb9ba008966227944f70a717.png[/img]

indirect bake
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/e/edaadf298ec7b7374cb5c52571b93f27eda8ac2a.png[/img]

-------------------------

Lumak | 2017-12-02 20:48:55 UTC | #7

Updated repo w/ bake indirect and misc. cleanup.

-------------------------

Lumak | 2017-12-04 18:07:10 UTC | #8

I wrote some test code to process solidangle color averaging in the background thread to reduce the overall build time for larger indirect lighting textures sizes, 128x128 and 256x256, and these are the kind of numbers that I'm getting in the **lightmap.log** file.
[code]
-------------128x128---------
[Mon Dec  4 09:13:25 2017] INFO: node7: indirect completion = 20.78 sec.
[Mon Dec  4 09:13:25 2017] INFO: node9: indirect completion = 20.79 sec.
[Mon Dec  4 09:13:25 2017] INFO: node10: indirect completion = 20.81 sec.
[Mon Dec  4 09:13:37 2017] INFO: node5: indirect completion = 33.39 sec.
[Mon Dec  4 09:14:04 2017] INFO: node8: indirect completion = 60.55 sec.
[Mon Dec  4 09:14:24 2017] INFO: node6: indirect completion = 80.01 sec.

-------------256x256---------
[Mon Dec  4 09:17:26 2017] INFO: node7: indirect completion = 81.61 sec.
[Mon Dec  4 09:17:26 2017] INFO: node9: indirect completion = 81.65 sec.
[Mon Dec  4 09:17:26 2017] INFO: node10: indirect completion = 81.69 sec.
[Mon Dec  4 09:18:13 2017] INFO: node5: indirect completion = 128.24 sec.
[Mon Dec  4 09:20:08 2017] INFO: node8: indirect completion = 243.74 sec.
[Mon Dec  4 09:21:21 2017] INFO: node6: indirect completion = 316.35 sec.

[/code]

You can specify the size at line 258 in LightmapCreator.cpp:
[code]
lightmap->BeginIndirectLighting(outputPath_, 256);
[/code]

Detail images:
lightmap
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/0/06ded3ad6bd1dff7f023a637e1b13e969e38aa55.png[/img]
baked indirect
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/8/8d6225f2bec8bd3e4c1c6854f239e51a0cf5d009.png[/img]

And you have to ask, is it worth creating a higher res image for indirect bake. And the answer is no.
There are obvious detail difference in the lightmap images from 64x64 to 256x256, but the diff of baked indirect images aren't all that different.
diff image online w/ fuzz 1%
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/4/474a28078abe20476a178f9af7a26d3be63e93a2.png[/img]

-------------------------

Lumak | 2017-12-04 19:49:25 UTC | #9

Really no difference when comparing the default size at 64x64.
[code]
-------------64x64---------
[Mon Dec  4 11:28:45 2017] INFO: node7: indirect completion = 5.37 sec.
[Mon Dec  4 11:28:45 2017] INFO: node9: indirect completion = 5.37 sec.
[Mon Dec  4 11:28:45 2017] INFO: node10: indirect completion = 5.38 sec.
[Mon Dec  4 11:28:49 2017] INFO: node5: indirect completion = 9.14 sec.
[Mon Dec  4 11:28:54 2017] INFO: node8: indirect completion = 14.90 sec.
[Mon Dec  4 11:29:00 2017] INFO: node6: indirect completion = 20.73 sec.
total time = 20.73 sec.
--- threaded
[Mon Dec  4 11:30:11 2017] INFO: node7: indirect completion = 5.38 sec.
[Mon Dec  4 11:30:11 2017] INFO: node9: indirect completion = 5.39 sec.
[Mon Dec  4 11:30:11 2017] INFO: node10: indirect completion = 5.40 sec.
[Mon Dec  4 11:30:14 2017] INFO: node5: indirect completion = 9.07 sec.
[Mon Dec  4 11:30:20 2017] INFO: node8: indirect completion = 14.76 sec.
[Mon Dec  4 11:30:26 2017] INFO: node6: indirect completion = 20.49 sec.
total time = 20.49 sec.

[/code]
You can save about a minute when creating 256x256 image threaded, but as mentioned previously, it's not worth it. And for this reason, I won't be checking in my threaded test code to the repo.

-------------------------

Lumak | 2017-12-04 23:24:46 UTC | #10

I was very skeptical about the diff'd images, and looking through my code, I realized I was calling **lightmap->SetSavefile(false);** early on to skip updating my baked files.


**True diff images:**

**64v128**
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/3/37a467d0bb6c3c0faef00492ebc5eca2195709b1.png[/img]

**128v256**
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/2/2f38bb047266d804df613133861ff0a4364aad09.png[/img]

-------------------------

Lumak | 2017-12-05 17:55:43 UTC | #11

Repo updated w/ solid angle color computation threaded option, and more importantly the indirect render texture is now fixed to 64x64.

-------------------------

Lumak | 2017-12-06 22:05:40 UTC | #12

Repo updated: runs 4x faster. The default scene setup now completes in **~5 secs.**

-------------------------

coldev | 2017-12-08 16:16:08 UTC | #13

Thanks 4 share.. nice christmas gift   :grinning:

-------------------------

Lumak | 2017-12-08 17:43:16 UTC | #14

You're welcome :slight_smile: 

Repo updated: refactored lightmap.cpp and created texturebake.cpp. This is the last update I'll make this year.

-------------------------

smellymumbler | 2017-12-08 17:48:14 UTC | #15

I'm curious: any chance this can be used with external tools such as Mitsuba or Eevee? 

Doing lighting correctly is something extremely difficult and this project could benefit from being a modular way of integrating renderers, instead of trying to render things itself. That's just my two cents, of course! Amazing effort. Learning a lot from your code, Lumak. You rock.

-------------------------

Lumak | 2017-12-08 19:46:36 UTC | #16

I'm not aware of Eevee but have studies Mitsuba about a couple of years ago.  Mitsuba does generate **perfect** lighting images but it does this by screen space raycasts, and there are variations of raycast options, does it on the CPU, and is really slow.

My implementation is based on **Hugo Elias's Radiosity.** Except, I haven't implemented the skipping of pixels, evaluate, and interpolate part, but brute force pixel processing. And I also use hemisphere instead of hemicube that everyone who's ever implemented Hugo's method that I've seen are so keen to believe that is the best option.

Using Urho3D's tech., indirect light processing is **blazing fast.** And the accuracy only depends on the lightmap/indirect light resolution that you choose.

Here's an example of the lightmap image created at 512x512 resolution:
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/5/5eaac9abb78c443c687d455019e1269d77da3647.png[/img]

I never realized how accurate **Hugo's** method was until I observed the cascading light and shadow at the top/left of the image and color bleeding.

-------------------------

Lumak | 2017-12-08 18:26:33 UTC | #17

That description above, I will have to use it on my github repo page.

-------------------------

smellymumbler | 2017-12-08 21:01:00 UTC | #18

I see. But isn't speed that much of a concern when you're baking lights? Or are you planning of generating lightmaps in realtime, similar to what Sauerbraten does?

-------------------------

Lumak | 2017-12-08 21:45:40 UTC | #19

Generating lightmaps at runtime to achieve static GI is exactly what's happening in my demo - just skip baking textures because you really don't need them, unless you're wanting to remove lights from the scene and render baked images as unlit.

Speed is a concern to me. I don't know about you but, I can remember a number of times when I've tried generating lightmaps in other engine/program and having to wait 40 mins. to see resulting lightmap textures with undesirable blemishes even for scenes strictly with box only type geometries.

What makes Mitsuba not work in this case is, it only does screen space processing. If you're wanting to only do screen space, there are plenty of shaders out there that can do SSGI, of course, w/o BRDF that Mitsuba applies in its process.

edit: had to rephrase.
edit2: sry, I don't know what a Sauerbraten is.

-------------------------

Lumak | 2017-12-08 21:59:42 UTC | #20

Let me also mention that there is a baked scene sample in Lightmap/bakedScene.xml which demonstrates rendering bakedIndirect as Unlit w/o any lights in the scene.

-------------------------

smellymumbler | 2017-12-08 22:02:16 UTC | #21

Now i understand what your goal is! I thought this was intended to be a lightmap baking tool, such as the ones included in UE and Unity. 

About embree: https://github.com/prideout/aobaker
About sauerbraten: http://sauerbraten.org/
http://sauerbraten.org/docs/editref.html

-------------------------

Lumak | 2017-12-08 22:12:16 UTC | #22

My original title for this thread was named "baking" something, so yeah, I really didn't describe what I've implemented exactly. And I'm not sure if "generator" describes it properly.

I've not seen nor tried UE and Unity lightmap baking tool to know if I generate something comparable. I wrote this and the lightprobe to replace a ton of lights that I had in a scene that I couldn't have in real time for mobile device.

-------------------------

Lumak | 2017-12-11 21:02:24 UTC | #23

Testing second light bounce in the demo. 
edit: i guess it'd help to have a reference of the 1st bounce

light bounce=1
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/f/f28b9e0dc6561193f02a3ffff2be372e9c947302.png[/img]
light bounce=2
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/9/994ed32ba18287dddb4a39c1b0618fdffd718932.png[/img]

-------------------------

Lumak | 2017-12-12 01:49:43 UTC | #24

Looking at the bounced light results had me look over my solid angle calculation again, and I believe there was an error.

edit: nope, it's mathematically correct.

-------------------------

Dave82 | 2017-12-12 03:18:46 UTC | #25

I don't know why but the indirect light doesn't feel and seem right.


The red circles show some random artifacts and the whole area between the red cube and the pillars are too bright.Also where the pillars touch the ground doens't seem right either.There are some bright circle shaped artifacts around them.
![image|690x388](upload://9tJM17NWOiKQ7cQtvpkrjtywdzM.jpg)

-------------------------

Lumak | 2017-12-12 04:34:47 UTC | #26

Yeah, I've noticed some strange artifacts.

One that really boggles my mind is this one:
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/9/936ce021ffc029bb699b422426072eaddff4eee2.png[/img]

I've gone through the debug draw process of drawing every point and normal on every object in the scene and they're correctly positioned and points outward from where they should be.  Yet, how does a star cluster form on a sphere when irradiance of close or next neighbors should be gradient if not the same.

Math wise, I don't massage my irradiance value during computation. What you see is what's been calculated from what's returned from render texture.

-------------------------

Dave82 | 2017-12-12 06:07:45 UTC | #27

Is the same artifact happens if you increase the resolution ? It seems like an ultra low resolution lightmap issue

-------------------------

Lumak | 2017-12-12 13:13:40 UTC | #28

* fixed the problem with star cluster on the sphere. turns out the camera rotation need to be set using FromLookRotation() fn, otherwise, the rotation gets skewed
* fixes the partial lighting on the back wall - uv mapping was too close, new model provided. also provided a new uv mapped box model
* the light ring around the pillars fixed by setting mat cull and shadowcull to "none."  you can't set this for the room!

-------------------------

Dave82 | 2017-12-12 13:22:15 UTC | #29

That's good news.Any screen shots ?

-------------------------

Lumak | 2017-12-12 13:39:36 UTC | #30

images of fixes
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/4/4d0e885c81a0f6e64de2a0cd8798e3b951106ac9.png[/img]

-------------------------

godan | 2017-12-12 20:23:39 UTC | #31

Just playing around with this: where can I set the bounces? Or is that feature not in yet?

-------------------------

Lumak | 2017-12-12 21:40:37 UTC | #32

I've not put that in yet. Mathematically, the irradiance calculation is correct, but I it just looks too bright to me. I'll need to verify it with a second source and compare the results before I can check that in.

It's simple to implement.
1. reinit state in lightmapCreator to [code]LightMap_IndirectLightBegin;[/code]
2. reinit state in [code]Lightmap::BeginIndirectLighting[/code] to [code]State_IndirectLightBegin[/code]

-------------------------

Lumak | 2017-12-13 17:57:03 UTC | #33

Maya's second light bounce room image. I tried to dummy down the GI bake settings in Maya to mimic Hugo's radiosity: sampling at 4096 (base on 64x64 texture size), no bake shadow, etc., because Maya does have some pretty sophisticated settings you can setup.  And I probably don't have the shaders set correctly because I'm losing color on no-texture objects.

Baked images on 64x64 texture size.

Hugo:
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/5/590fc22409d3be4c4d97f4bb37032f0d7cba7bdd.png[/img]

Maya:
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/1/126007411d357803fd55886e3b3cc329125b7619.jpg[/img]

Summing the luma of generated second bounce images, Hugo's method accumulated ~19% more light than Maya.

-------------------------

Lumak | 2017-12-13 01:22:30 UTC | #34

If I multiply irradiance by 50% Luma and summed with 20% of the original color, I get:
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/d/d20671b499b0a38012dae03ecdff9ecaebe45934.png[/img]

-------------------------

Lumak | 2017-12-13 18:28:39 UTC | #35

Testing alternate approach by turning off all the lights in the scene and sampling light emitted from the lightmap in the first indirect light pass, results in the 2nd pass image below.

Total luma captured in the scene is 5% more than Maya. First, sampling was 19% more.  Of course you can always tone down color by replacing the percentage of the color with luma.

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/3/3b91955ecefa3eca47e0e9b9ad5d55c58bbdbe39.png[/img]

Posting Maya image again for easy comparison:
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/1/126007411d357803fd55886e3b3cc329125b7619.jpg[/img]

Luma, RGB remove.
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/5/59a1c93c891ca5aa5d03c8b85d66d069d30a8681.png[/img]

-------------------------

godan | 2017-12-13 18:17:37 UTC | #36

This looks a lot better IMO. Nice one!

-------------------------

smellymumbler | 2017-12-13 19:19:08 UTC | #37

Quick question: does this auto-unwrap my scene? Or i have to do that myself? That scene is a single object?

-------------------------

Lumak | 2017-12-13 20:12:27 UTC | #38

By
[quote]
does this auto-unwrap my scene?
[/quote]
I think you mean, does it uv unwrap. No, it doesn't do any uv unwrapping. Each model is expected to already have texCoord2.

The scene has 6 static models, each with its own texcoord2.

-------------------------

Lumak | 2017-12-14 05:33:20 UTC | #39

Repo updated: 2ndary light bounce and clean up.

Final comparison with Maya: Hugo's method results in **3.5% less light**.  And the default output is luma, no RGB. Set **lumaOutputColor_=false** in Lightmap.cpp for color.

-------------------------

Eugene | 2017-12-13 22:43:26 UTC | #40

What's the reason of these gradients lines on the columns? Looks like an artifact.

-------------------------

Lumak | 2017-12-14 05:33:45 UTC | #41

Ya, the pillars look like shit. It's the way it's uv mapped. It'd probably come out a lot better if **Thekla** uv mapper is used, but that's entirely a whole another project and I'm not touching that.

-------------------------

elix22 | 2017-12-14 03:52:12 UTC | #42

I have one word , beautiful.
Would be useful for low end mobile devices.
Once I will have some spare time will try it on more complex scene's

-------------------------

Lumak | 2017-12-16 00:47:52 UTC | #43

I will have another repo update before Christmas.  Update will include baking direct and indirect to produce a combined Unlit texture, so you can have it in a static environment.  

Final will include:
* for dynamic environment: lightmap.
* for static environment: unlit.
* removing direct baked images.

-------------------------

rasteron | 2017-12-16 01:23:44 UTC | #44

Looking great Lumak and awesome work :+1: Yes, I'm sure this will be great for mobile.

-------------------------

Lumak | 2017-12-17 16:51:38 UTC | #45

Repo updated with direct and indirect texture bake.  Before you start any lightmap process, check out the resulting baked texture by openging the bakedScene.xml in the editor.

-------------------------

elix22 | 2017-12-17 23:56:18 UTC | #46

The baked outcome looks great

-------------------------

smellymumbler | 2017-12-18 15:20:47 UTC | #47

Would this work with terrains?

-------------------------

Lumak | 2017-12-28 22:38:44 UTC | #48

@smellymumbler, no.

Repo updated with HLSL support.

-------------------------

Liichi | 2020-03-09 23:26:09 UTC | #49

Is there any reason not to merge this?

-------------------------

Eugene | 2020-03-10 13:24:32 UTC | #50

I think I can answer this, as a person who implemented lightmapper myself.

There's a huge difference between lightmapping sample and baked lighting support in the engine.

It took me 2 weeks to implement lightmap _generation_ from scratch (aka "sample"), and 2.5 _months_ to integrate baked lighting into the engine and polish most notable rough corners, so I get actually usable tool suitable for real scenes.

This is the reason why most of the samples (and Urho has a lot of the 3rd-party samples) are not merged into master in any form.

It's only 5-10% of work to implement sample. The rest 90-95% of work is to smoothly integrate sample functionality into the engine in actually re-usable and flexible form.

-------------------------

Liichi | 2020-03-11 13:49:16 UTC | #51

Oh, I thought that implementing lightmap generation was the hard part :(

-------------------------

Modanung | 2020-03-11 15:10:50 UTC | #52

It probably _is_ the part that requires most close-to-the-metal technical knowledge, but not what requires most lines of code. I think what @Eugene is saying is that making something work, is not the same as making it widely applicable in a way that is relatively easy to understand for others.

-------------------------

Eugene | 2020-03-11 15:22:42 UTC | #53

[quote="Modanung, post:52, topic:3812"]
It probably *is* the part that requires most close-to-the-metal technical knowledge, but not what requires most lines of code
[/quote]
So true.

The raytracting kernel of lightmapper requires certain technical knowledge and algorithms, so it may be hard to implement if one is not familiar with the area (like me 5 months ago).

On the other hand, this part is relatively simple from architectural point of view. Actual intergarion raises a lot of new questions and issues.

How lightmapper shall handle materials and models of the engine? What components are supported and how? What's performance on real scenes? Does lightmapper converge with increasing quality? How to run it in the background while scene is open in the Editor? How to handle dynamic objects? How to handle model LODs? How to integrate new changes into legacy shaders? How to make it as simple-to-use as possible? In perfect world, with one or two clicks in the Editor.

-------------------------

