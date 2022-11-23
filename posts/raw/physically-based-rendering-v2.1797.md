dragonCASTjosh | 2017-01-02 01:10:13 UTC | #1

[i][b]Overview[/b][/i]
Since Sonoid finished working on PBR he passed the torch to me and provided me rights to change and redistribute the code as i feel fit. Since i took on the project i made some small changes, the first change i made was to allow PBR to work alongside the legacy renderer in Forward Rendering. The second change i made was to change the diffuse model to be Burley because i personally prefer it over Lambert. 

Results:
[video]https://youtu.be/6qfIHsG_MSU[/video]

Images:
[spoiler][img]http://i.imgur.com/5Rb6Rx4.jpg[/img]
[img]http://i.imgur.com/o4FC6XB.jpg[/img]
[img]http://i.imgur.com/TrIa6qu.jpg[/img][/spoiler]


[i][b]How to use[/b][/i]
When you create a material you will need to use one of the PBR render techniques located in CoreData/Techniques/PBR

If the selected technique uses diffuse then you will need to input a albedo texture into the diffuse channel. Albedo is similar to diffuse although it does not contain any lighting data.
if the selected technique uses normal then you will need to input a traditional normal map into the normal channel.
if the selected technique uses Metallic /roughness then you will need to input a PBR properties map into the specular channel. The PBR properties map contains Roughness in the red color channel and  Metallic in the green color channel.
if the selected technique uses emissive then you will need to input a emissive texture into the emissive channel.

For additional control over the material you can add  Roughness and Metallic as material parameters, from these values you can adjust the PBR properties  map or set default values for material without a PBR properties map 
[img]http://i.imgur.com/b6stkrb.png[/img]

[i][b]Effect[/b][/i]
Both the Roughness and Metallic values affect the overall look of the material. The effect each value has on the material is shown in the images below, these images where taken from the Material Test scene included in PBR repository.

Roughneses:
[spoiler][img]http://i.imgur.com/Mr9Tscs.png[/img][/spoiler]

Metalic:
[spoiler][img]http://i.imgur.com/dNLuu8G.png[/img][/spoiler]


Area Lighting is still in development although sphere lights are currently supported. The image below demonstrates sphere lights as demonstrated on the Material Test scene.

Sphere Light
[spoiler][img]http://i.imgur.com/ajUkyxO.png[/img][/spoiler]

[i][b]Download[/b][/i]

Currently the download will not work on OpenGL Deferred Renderers due to know issue (without a fix currently)
[url]https://github.com/dragonCASTjosh/Urho3D[/url]

-------------------------

codingmonkey | 2017-01-02 01:10:13 UTC | #2

Great work! Thanks for sharing this.

-------------------------

dragonCASTjosh | 2017-01-02 01:10:14 UTC | #3

[quote="codingmonkey"]Great work! Thanks for sharing this.[/quote]

Thanks for the support :slight_smile: 

I wanted to implement the IBL system demonstrated in the Unreal 4 PBR notes but it caused massive performance problems for my 970. you can enable it in the repo by changing iblColor in the LitSolid.hlsl to [code]float3 iblColor = ApproximateSpecularIBL(specColor, roughness, normal, -toCamera)[/code]

and the number of samples in the Lighting to 1024
[code]float3 PrefilterEnvMap(float Roughness, float3 R)
		{
			float3 N = R;
			float3 V = R;

			float3 PrefilteredColor = 0;
			const uint NumSamples = 1024;

			float TotalWeight = 0.0000001f;

			for (uint i = 0; i < NumSamples; i++)
			{
				float2 Xi = Hammersley(i * 2 + 0, NumSamples);
				float3 H = ImportanceSampleGGX(Xi, Roughness, N);
				float3 L = 2 * dot(V, H) * H - V;
				float NoL = saturate(dot(N, L));
				if (NoL > 0)
				{
					PrefilteredColor += SampleCubeLOD(ZoneCubeMap, float4(L, 0)).rgb * NoL;
					TotalWeight += NoL;
				}
			}
			return PrefilteredColor / TotalWeight;
		}[/code]

Anybody is welcome to make PR to the repo especially if they help with performance of the Unreal PBR as it looks a lot better

-------------------------

practicing01 | 2017-01-02 01:10:14 UTC | #4

Congratulations to all the parties involved! I hope to be able to use pbr on mobile/linux some day.

-------------------------

dragonCASTjosh | 2017-01-02 01:10:14 UTC | #5

[quote="practicing01"]Congratulations to all the parties involved! I hope to be able to use pbr on mobile/linux some day.[/quote]

OpenGL support should be done within a few days

-------------------------

weitjong | 2017-01-02 01:10:14 UTC | #6

[quote="dragonCASTjosh"][quote="practicing01"]Congratulations to all the parties involved! I hope to be able to use pbr on mobile/linux some day.[/quote]

OpenGL support should be done within a few days[/quote]

I am looking forward to it. Thanks for sharing it.

EDIT
I just clone the repo and I have a few questions:
[ul][li] It seems that there are no changes whatsoever to the Urho3D engine code. Is it really true?[/li]
[li] I understand that sinoid has transfer the copyright to you for all his work (IANAL, so sorry if I use a wrong term here). My question is, now under which license are you releasing your combined work? Please say MIT or even better Urho3D license (MIT) :wink:. Using Urho3D license makes it easier for us to pull the good bits over into upstream Urho3D project as there should be no copyright issue then in copying the code over pro-actively. [/li][/ul]

-------------------------

1vanK | 2017-01-02 01:10:15 UTC | #7

[quote="weitjong"]
It seems that there are no changes whatsoever to the Urho3D engine code. Is it really true?
[/quote]

Yes, it's only shaders. You can see fork from the original repo [github.com/souxiaosou/UrhoPBRCoreData](https://github.com/souxiaosou/UrhoPBRCoreData) . It's containt detailed comments, like
[code]        /// Smith GGX Visibility
        ///     nDotL: dot-prod of surface normal and light direction
        ///     nDotV: dot-prod of surface normal and view direction
        ///     roughness: surface roughness
        float SmithGGXVisibility(in float nDotL, in float nDotV, in float roughness)
        {
            float rough2 = roughness * roughness;
            float gSmithV = nDotV + sqrt(nDotV * (nDotV - nDotV * rough2) + rough2);
            float gSmithL = nDotL + sqrt(nDotL * (nDotL - nDotL * rough2) + rough2);
            return 1.0 / (gSmithV * gSmithL);
        } [/code]
but it is obsolete, I think. It is a pity that these comments have been removed.

-------------------------

hdunderscore | 2017-01-02 01:10:15 UTC | #8

Just previewing the test scene, it seems to miss a bit of the punch of other PBR implementations. I couldn't guess why from the short test -- it could be as simple as poor environment map choice or may be something more. In my previous attempt with PBR I realised it's important to have simple tests and comparisons.

I can tell there is a lot of work put into this though, nice work so far !

[quote="weitjong"]It seems that there are no changes whatsoever to the Urho3D engine code. Is it really true?[/quote]
Most of the work is in the shaders, but a complete PBR implementation will need to touch on the engine source to at least provide some parameters for area lights.

-------------------------

dragonCASTjosh | 2017-01-02 01:10:15 UTC | #9

[quote="weitjong"]


I just clone the repo and I have a few questions:
[ul][li] It seems that there are no changes whatsoever to the Urho3D engine code. Is it really true?[/li]
[li] I understand that sinoid has transfer the copyright to you for all his work (IANAL, so sorry if I use a wrong term here). My question is, now under which license are you releasing your combined work? Please say MIT or even better Urho3D license (MIT) :wink:. Using Urho3D license makes it easier for us to pull the good bits over into upstream Urho3D project as there should be no copyright issue then in copying the code over pro-actively. [/li][/ul][/quote]

Currently there are no changes to Urho3D engine code and its possible to get away without any changes but to include features like Parallax Correction for cubemaps and Area Lighting there will need to be small changes to the engine.
For the licence sinoid provided me the source under MIT as is visible in the licence image found under the shader dir (only there temporally). Im not sure if MIT would allow me to changes the licence to Urho3D but if it did i would change it.



[quote="1vanK"]
but it is obsolete, I think. It is a pity that these comments have been removed.
[/quote]

The lack of comments is a temporary thing, I was planning on moving PBR to its own shader file and re-document.

[quote="hd_"]
Just previewing the test scene, it seems to miss a bit of the punch of other PBR implementations. I couldn't guess why from the short test -- it could be as simple as poor environment map choice or may be something more. In my previous attempt with PBR I realised it's important to have simple tests and comparisons.
[/quote]

The issue likely lies within the IBL solution that has been used. Currently i am using the Unreal 4 mobile IBL(same as sinoid implemented). I tried implementing more advanced IBL and it provided much better results although the performance of it currently is horrible  

Comparison
[spoiler]Current Rough Metallic
[img]http://i.imgur.com/Jycn6aR.jpg[/img]

More advanced IBL
[img]http://i.imgur.com/7Opjq6Q.jpg[/img]

Current Rough Non-Metallic
[img]http://i.imgur.com/13848FI.jpg[/img]

More advanced IBL
[img]http://i.imgur.com/eaNMWK3.jpg[/img][/spoiler]

-------------------------

weitjong | 2017-01-02 01:10:15 UTC | #10

[quote="dragonCASTjosh"]Currently there are no changes to Urho3D engine code and its possible to get away without any changes but to include features like Parallax Correction for cubemaps and Area Lighting there will need to be small changes to the engine.
For the licence sinoid provided me the source under MIT as is visible in the licence image found under the shader dir (only there temporally). Im not sure if MIT would allow me to changes the licence to Urho3D but if it did i would change it.[/quote]

Thanks for the prompt reply. Again, IANAL. Urho3D license is MIT license. The only difference is that it declares the work/material/code is copyrighted by Urho3D project. If anyone submitting a PR to us then you must have read and agree to the T&C to release them under MIT license with the copyright statement "Copyright (c) 2008-2016 the Urho3D project" (see [urho3d.github.io/documentation/H ... klist.html](http://urho3d.github.io/documentation/HEAD/_contribution_checklist.html)). Basically, what I am asking is whether we have your permission to "copy" the combined work into Urho3D project and thus they would adhere to the above term. We do not steal other ppl code  :wink:  and claim them as ours. Alternatively, we can just wait passively until you send us PR when/if you decide to merge your work to upstream Urho3D project.

-------------------------

Modanung | 2017-01-02 01:10:15 UTC | #11

Looking great. :slight_smile:

-------------------------

dragonCASTjosh | 2017-01-02 01:10:15 UTC | #12

[quote="weitjong"][quote="dragonCASTjosh"]Currently there are no changes to Urho3D engine code and its possible to get away without any changes but to include features like Parallax Correction for cubemaps and Area Lighting there will need to be small changes to the engine.
For the licence sinoid provided me the source under MIT as is visible in the licence image found under the shader dir (only there temporally). Im not sure if MIT would allow me to changes the licence to Urho3D but if it did i would change it.[/quote]

Thanks for the prompt reply. Again, IANAL. Urho3D license is MIT license. The only difference is that it declares the work/material/code is copyrighted by Urho3D project. If anyone submitting a PR to us then you must have read and agree to the T&C to release them under MIT license with the copyright statement "Copyright (c) 2008-2016 the Urho3D project" (see [urho3d.github.io/documentation/H ... klist.html](http://urho3d.github.io/documentation/HEAD/_contribution_checklist.html)). Basically, what I am asking is whether we have your permission to "copy" the combined work into Urho3D project and thus they would adhere to the above term. We do not steal other ppl code  :wink:  and claim them as ours. Alternatively, we can just wait passively until you send us PR when/if you decide to merge your work to upstream Urho3D project.[/quote]

Your free to implement it into Urho3D, i was going to make a pull request once i got the OpenGL version and and cleaned up the code a little. But you are free to merge it when you feel its ready :slight_smile:

-------------------------

weitjong | 2017-01-02 01:10:16 UTC | #13

[quote="dragonCASTjosh"]Your free to implement it into Urho3D, i was going to make a pull request once i got the OpenGL version and and cleaned up the code a little. But you are free to merge it when you feel its ready :slight_smile:[/quote]
Thanks in advance for that. I am not necessary saying I am the best person to do it nor stating the readiness of the combined work, but I think everyone here will be definitely happy to see it merged eventually.

-------------------------

dragonCASTjosh | 2017-01-02 01:10:36 UTC | #14

I updated the Repo to support OpenGL Forward Rendering so now everyone should be able to access it :slight_smile: . As for the GL deferred renderer i ran into some issues to do with YCoCg that Sinod originally implemented as way to boost performance and compress the Albedo and Specular into a single RGBA color buffer. If anyone wants to help with fixing it, everything should be on the Repo, if i cant find a fix within the next few weeks i may look into removing the functionality from all renderers and add extra buffers for what is needed

-------------------------

dragonCASTjosh | 2017-01-02 01:10:41 UTC | #15

Made some advancements today, nothing public yet but i wanted to provide a short development screenshot of area lighting. In my private build area lighting is only supported on Point lights although i am looking to branch it out to other light sources and even one up unreal and include none spherical area lights :slight_smile: 

[img]http://i.imgur.com/H3gEGz8.jpg[/img]
[img]http://i.imgur.com/tC3CBjB.jpg[/img]

-------------------------

weitjong | 2017-01-02 01:10:41 UTC | #16

Awesome. Will definitely look at the OpenGL implementation once I have concluded the SDL 2.0.4 upgrade.

-------------------------

dragonCASTjosh | 2017-01-02 01:10:42 UTC | #17

@weitjong How do you think its best to implement the front end of Area Lighting, in my head currently i have new lighting types or multiple new options on existing lights.

-------------------------

gawag | 2017-01-02 01:10:44 UTC | #18

Hm I just read this thread and was thinking about the environment maps and also about mirrors for a while. I also found this lecture about the topics: [inf.ed.ac.uk/teaching/course ... 9_2013.pdf](http://www.inf.ed.ac.uk/teaching/courses/cg/lectures/cg9_2013.pdf)
The environment maps used in the samples here (yeah just samples but still) look pretty fake as they don't show the actual scene at all.
I remember the Half Life 2 engine from Garrys Mod and they did environment maps by pre-rendering images in the level editor at various coordinates scattered throughout the map (a 3D raster). This looked pretty bad as well because the maps jumped when the object moved around and was closer to a different map and also the maps did not reflect the actual scene at all (dynamic objects/lights).

Raytracing is still way to slow but what about this:
Could a camera with a FOV of 90 be used to dynamically create cubemaps used as environment maps? Could there be like a wandering camera that calculates a (new) cubemap for one object every six frame (one cubemap side each frame, so if you have 10 objects with an environment map every one gets updated all 60 frames)? Could that special camera render all 6 sides in one "frame" (sub-frame if you want)? 

Or could some mirror technique (like the Urho water sample) be used to get environment data?

-------------------------

dragonCASTjosh | 2017-01-02 01:10:44 UTC | #19

[quote="gawag"]Could a camera with a FOV of 90 be used to dynamically create cubemaps used as environment maps? Could there be like a wandering camera that calculates a (new) cubemap for one object every six frame (one cubemap side each frame, so if you have 10 objects with an environment map every one gets updated all 60 frames)? Could that special camera render all 6 sides in one "frame" (sub-frame if you want)? [/quote]

Creating dynamic cubemaps without 6 rendertextures per cubemap would become very costly very quick, and after filtering the cubemap for the majority of materials you would find it was not worth the cost. A better solution would be SSR where you do a screen space raytreace to capture the reflections, there are multiple methods of doing SSR but my preferred result is the one used by Frostbite 3 as it does not create a noisy texture like UE4 does under certain scenarios. 

Results: [url]http://www.frostbite.com/wp-content/uploads/2015/08/Stochastic-Screen-Space-Reflections.mp4[/url]
Paper: [url]http://www.frostbite.com/2015/08/stochastic-screen-space-reflections/[/url]

-------------------------

gawag | 2017-01-02 01:10:44 UTC | #20

[quote="dragonCASTjosh"][quote="gawag"]Could a camera with a FOV of 90 be used to dynamically create cubemaps used as environment maps? Could there be like a wandering camera that calculates a (new) cubemap for one object every six frame (one cubemap side each frame, so if you have 10 objects with an environment map every one gets updated all 60 frames)? Could that special camera render all 6 sides in one "frame" (sub-frame if you want)? [/quote]

Creating dynamic cubemaps without 6 rendertextures per cubemap would become very costly very quick, and after filtering the cubemap for the majority of materials you would find it was not worth the cost. A better solution would be SSR where you do a screen space raytreace to capture the reflections, there are multiple methods of doing SSR but my preferred result is the one used by Frostbite 3 as it does not create a noisy texture like UE4 does under certain scenarios. 

Results: [url]http://www.frostbite.com/wp-content/uploads/2015/08/Stochastic-Screen-Space-Reflections.mp4[/url]
Paper: [url]http://www.frostbite.com/2015/08/stochastic-screen-space-reflections/[/url][/quote]
:open_mouth: 
Wow that's awesome! I want that!  :smiley: 
I have no idea how to do that.  :frowning: 

I get the ideas behind that but how to do the raytracing? Is it done on the CPU? Or is the whole scene somehow moved to the graphics card to calculate there?
Are mirrors in principle also done like that?
I some games there is glass that partly mirrors, is partly transparent and is partly "bending" the viewing angle somehow. Is the bending similar?
I had no idea that such a thing is possible.

Edit: Added to wishlist [github.com/urho3d/Urho3D/wiki/urho3d-wishlist](https://github.com/urho3d/Urho3D/wiki/urho3d-wishlist)

Edit2: Ah it seems to be not a real ray trace but a "depth buffer scan": [casual-effects.blogspot.de/2014/ ... acing.html](http://casual-effects.blogspot.de/2014/08/screen-space-ray-tracing.html)
"...Games march 3D rays across the height field defined by a depth buffer to create very approximate screen-space reflections...."

-------------------------

dragonCASTjosh | 2017-01-02 01:10:44 UTC | #21

[quote="gawag"]I get the ideas behind that but how to do the raytracing? Is it done on the CPU? Or is the whole scene somehow moved to the graphics card to calculate there?
Are mirrors in principle also done like that?[/quote]

The raytracing is done on the GPU in the post processing pass therefore it had details of the final rendered scene.
Mirrors tend to be render target therefore they have a dedicated camera that renders to the mirror, think of it like CCTV and a monitor, glass can be done this way although it would be slow so it tends to use the cubemap as SSR can only reflect whats visible.

-------------------------

gawag | 2017-01-02 01:10:44 UTC | #22

Just added an "Edit2" to my last post. Found that out already. Interesting idea though.
So SSR and PBR are post processing effects and not material effects, I see.

So if one want to render stuff not directly visible to the camera (like a mirror) one has to use something like the water in Urho does? I guess one could also do something like the portals in Portal with that.

Maybe I should make a new thread but how to read the depth buffer? Is there even one? That would be also good to make a depth blur effect but as I tried that there seemed to be no depth information.

-------------------------

dragonCASTjosh | 2017-01-02 01:10:44 UTC | #23

[quote="gawag"]
So SSR and PBR are post processing effects and not material effects, I see.
[/quote]

I wouldnt say PBR is an effect and its not post provessing. PBR is a material system itself, it takes observable world values to allow artists to accurately create materials. It also allows for better plastic materials.

-------------------------

boberfly | 2017-01-02 01:10:44 UTC | #24

Great stuff!!!

I'd get rid of the YCoCg stuff, unless it's easily #ifdef'd in and out as an optional optimisation.

I'll see if I can get some stuff set up that tests this against a production renderer with similar shaders so that it can be calibrated and to see if the approximations are accurate enough. Maybe like using Appleseed+Gaffer (yet another unfinished project of mine is IECoreUrho support for Cortex/Gaffer).

-------------------------

dragonCASTjosh | 2017-01-02 01:10:44 UTC | #25

[quote="boberfly"]Great stuff!!!

I'd get rid of the YCoCg stuff, unless it's easily #ifdef'd in and out as an optional optimisation.

I'll see if I can get some stuff set up that tests this against a production renderer with similar shaders so that it can be calibrated and to see if the approximations are accurate enough. Maybe like using Appleseed+Gaffer (yet another unfinished project of mine is IECoreUrho support for Cortex/Gaffer).[/quote]

I was planning to remove YCoCg at this point as it is only causing problems and i dont think it makes much of a difference at this point as developers can pick forward rendering. 


Also just uploaded a video on youtube demonstrating PBR with a wide variety of materials from algorithmic share. 
[video]https://youtu.be/6qfIHsG_MSU[/video]

-------------------------

boberfly | 2017-01-02 01:10:45 UTC | #26

Very nice. I recognise that HDRI also... :slight_smile:

-------------------------

dragonCASTjosh | 2017-01-02 01:10:45 UTC | #27

[quote="boberfly"]Very nice. I recognise that HDRI also... :slight_smile:[/quote]

thanks, and the HDRI is from a public library of them :slight_smile:

In other news i feel like PBR is getting very close to a point where it is free for the master branch. All that remains is cleaning up deferred render path and Tube Lighting and it will match Unreals PBR feature set. I will look into square area lighting as there has been points where i have needed in the past on projects.

Oh and i also need to remove all the crap i added to the repo for testing like the 30+ materials that i got from algorithmic share

-------------------------

thebluefish | 2017-01-02 01:10:46 UTC | #28

[quote="dragonCASTjosh"]Oh and i also need to remove all the crap i added to the repo for testing like the 30+ materials that i got from algorithmic share[/quote]

This has helped me a few times when I've accidentally pushed sensitive data to a public branch: [help.github.com/articles/remove-sensitive-data/](https://help.github.com/articles/remove-sensitive-data/)

Who knows if you need to be that extreme, but sometimes it's easier to clean it out than worry about potential licensing violations.

-------------------------

dragonCASTjosh | 2017-01-02 01:10:46 UTC | #29

[quote="thebluefish"]

This has helped me a few times when I've accidentally pushed sensitive data to a public branch: [help.github.com/articles/remove-sensitive-data/](https://help.github.com/articles/remove-sensitive-data/)

Who knows if you need to be that extreme, but sometimes it's easier to clean it out than worry about potential licensing violations.[/quote]

Thanks, although i dont think its that bad, from what i can tell the materials are free to use and distribute, the only issue i have is that i made changes to default urho3d maps and materials for testing and i have to undo these changes and make a demo level

-------------------------

Dave82 | 2017-01-02 01:10:47 UTC | #30

THIS is absolutely awesome !  :open_mouth: 
Is this going to be officially added to Urho ?

-------------------------

dragonCASTjosh | 2017-01-02 01:10:47 UTC | #31

[quote="Dave82"]THIS is absolutely awesome !  :open_mouth: 
Is this going to be officially added to Urho ?[/quote]

Thanks :slight_smile: and i do plan to merge it when its ready.

-------------------------

Lumak | 2017-01-02 01:10:48 UTC | #32

You've come a long way with this project, Josh.  Awesome job! 
I really liked the demo video.

-------------------------

dragonCASTjosh | 2017-01-02 01:10:48 UTC | #33

[quote="Lumak"]You've come a long way with this project, Josh.  Awesome job! 
I really liked the demo video.[/quote]

Thanks and iv had alot of fun with it so far. There is still a little more work to do before i feel its ready but i think its in a very usable state and that alone makes me happy.

-------------------------

dragonCASTjosh | 2017-01-02 01:10:51 UTC | #34

Updated First post to include more up to date images. Also added sphere lighting to the repository. This leads into my current issue of hitting a brick wall with tube lights, i will continue to work towards implementing it but for now it is not my priority so may not be included any time soon, for now i will focus on fixing deferred render paths to achieve identical results to forward render paths without compromising legacy Urho3D rendering.

-------------------------

dragonCASTjosh | 2017-01-02 01:11:14 UTC | #35

PBR is fully usable, before i consider merging the core PBR work can people please give me performance results from a wide verity of platforms.

-------------------------

Shylon | 2017-01-02 01:11:15 UTC | #36

THANK you so MUCH :slight_smile:
is this link to download ?

[url]https://github.com/dragonCASTjosh/Urho3D[/url]

-------------------------

dragonCASTjosh | 2017-01-02 01:11:15 UTC | #37

yea that is the download link :slight_smile:

Edit: just commited sample program that can be used for performance testing.

-------------------------

Hevedy | 2017-01-02 01:11:15 UTC | #38

Downloaded and compiled but at run the scene all is empty just the skybox and text, and at open in editor the nodes are here but no mesh or material and at try to select manual material return shader errors o_O

-------------------------

dragonCASTjosh | 2017-01-02 01:11:15 UTC | #39

send me a screne shot of the error

-------------------------

dragonCASTjosh | 2017-01-02 01:11:15 UTC | #40

Try the latest commit

-------------------------

1vanK | 2017-01-02 01:11:15 UTC | #41

How to change brightness of ambient light when used Zone Texture?

I have very sharp border when I use directional light 
[url=http://savepic.ru/8993512.htm][img]http://savepic.ru/8993512m.png[/img][/url]
Is it normal?

-------------------------

Shylon | 2017-01-02 01:11:15 UTC | #42

I wonder, is there any capture mechanism for zone to capture or render to texture in its field?

-------------------------

dragonCASTjosh | 2017-01-02 01:11:15 UTC | #43

[quote="1vanK"]How to change brightness of ambient light when used Zone Texture?

I have very sharp border when I use directional light 
[url=http://savepic.ru/8993512.htm][img]http://savepic.ru/8993512m.png[/img][/url]
Is it normal?[/quote]

you can change the ambient light in the Zone options, the option your looking for is ambient color.
As doe the sharp transition, i beleive its a side affect of when i changed diffuse, not sure what the cause it at the moment but ill change the diffuse back to Lambert for now.

-------------------------

1vanK | 2017-01-02 01:11:15 UTC | #44

[quote="dragonCASTjosh"]
you can change the ambient light in the Zone options, the option your looking for is ambient color.
[/quote]

not working for glossy material (like Copper)

-------------------------

dragonCASTjosh | 2017-01-02 01:11:15 UTC | #45

[quote="1vanK"]
not working for glossy material (like Copper)[/quote]

Likely due to how it has been implemented, you can brighten metallic materials by increasing the defuse color in the material editor

-------------------------

1vanK | 2017-01-02 01:11:15 UTC | #46

May be implement multiplication Zone Texture * Ambient color?

-------------------------

dragonCASTjosh | 2017-01-02 01:11:15 UTC | #47

[quote="1vanK"]May be implement multiplication Zone Texture * Ambient color?[/quote]
I dont think thats the cause, it looks to be the metallic value is cancelling out any colour changes as there should be 0 diffuse on a metallic material, therefore boosting the diffuse means that the little bit of diffuse lefts from artefacts is amplified so you can see the color changes

-------------------------

1vanK | 2017-01-02 01:11:15 UTC | #48

But material reflected environment (take value from texture), so it this place we can increase brightness this texture

-------------------------

codingmonkey | 2017-01-02 01:11:16 UTC | #49

On first my trying I build engine with gl renderer. 
So with it, I got crashing of driver when I trying to assign material onto spheres from PBR folder (one by one).
then I rebuild engine with dx11. 
Also see some buggy behavior (long material loading, you probably use ultra-res textures?). 
Editor was opened and freeze, once.

this is log from PBRMaterials.bat (dx11)
[url=http://savepic.net/7918765.htm][img]http://savepic.net/7918765m.png[/img][/url]

only work if open PBRScene Scene and assign materials.
also need find zone in scene and assign to it cubemap textures\cubemaps\6.xml, otherwise IBL not working I guess
[url=http://savepic.net/7929007.htm][img]http://savepic.net/7929007m.png[/img][/url]

-------------------------

dragonCASTjosh | 2017-01-02 01:11:16 UTC | #50

[quote="1vanK"]But material reflected environment (take value from texture), so it this place we can increase brightness this texture[/quote]
The problem with directly multiplying the reflection is that is will affect offset by the metallic value during a lighting pass, therefore the none metallics become brighter and metallics are darker until you increese the ambient till the point of the none metallics being white

-------------------------

dragonCASTjosh | 2017-01-02 01:11:16 UTC | #51

[quote="codingmonkey"]So with it, I got crashing of driver when I trying to assign material onto spheres from PBR folder (one by one).
then I rebuild engine with dx11. 
Also see some buggy behavior (long material loading, you probably use ultra-res textures?). [/quote]

This is likely entirly down to the high resolution images i use at the moment, hopefully the comunity provides some lower resolution images.

[quote="codingmonkey"]only work if open PBRScene Scene and assign materials.
also need find zone in scene and assign to it cubemap textures\cubemaps\6.xml, otherwise IBL not working I guess[/quote]

That scene hasn't been used in a few weeks so im supprised it worked at all

-------------------------

1vanK | 2017-01-02 01:11:16 UTC | #52

Anyway it looks very cool, but probably it requires more powerful hardware than my old notebook xD

-------------------------

dragonCASTjosh | 2017-01-02 01:11:16 UTC | #53

[quote="1vanK"]Anyway it looks very cool, but probably it requires more powerful hardware than my old notebook xD[/quote]
probably because all the textures are 4096x4096 :slight_smile: try make a new scene and use the PBR... materials for example PBR00M,xml these do not include textures

-------------------------

dragonCASTjosh | 2017-01-02 01:11:16 UTC | #54

I cant seam to replicate the errors with the demo script, so im not sure if i can make a fix at the moment.

-------------------------

1vanK | 2017-01-02 01:11:16 UTC | #55

I think need way to configure count of samples. I decrease IMPORTANCE_SAMPLES to 4 and prefomance improved dramatically without noticeable deterioration in the quality

-------------------------

dragonCASTjosh | 2017-01-02 01:11:16 UTC | #56

[quote="1vanK"]I think need way to configure count of samples. I decrease IMPORTANCE_SAMPLES to 4 and prefomance improved dramatically without noticeable deterioration in the quality[/quote]
it will likely be a feature at some point but im looking for the best way to do it, any ideas.

-------------------------

1vanK | 2017-01-02 01:11:16 UTC | #57

Just send this value to shader as parameter from material and clamp(2, 16) in shader

-------------------------

dragonCASTjosh | 2017-01-02 01:11:16 UTC | #58

[quote="1vanK"]Just send this value to shader as parameter from material and clamp(2, 16) in shader[/quote]
i didnt consider doing that, i mostly looked into passing is a a define from the render path or material

-------------------------

1vanK | 2017-01-02 01:11:16 UTC | #59

Ideally, this parameter should send engine, that the player can adjust the quality of all materials

-------------------------

1vanK | 2017-01-02 01:11:17 UTC | #60

Like (view.cpp)


[code]void View::SetGlobalShaderParameters()
{
    graphics_->SetShaderParameter(VSP_DELTATIME, frame_.timeStep_);
    graphics_->SetShaderParameter(PSP_DELTATIME, frame_.timeStep_);

    if (scene_)
    {
        float elapsedTime = scene_->GetElapsedTime();
        graphics_->SetShaderParameter(VSP_ELAPSEDTIME, elapsedTime);
        graphics_->SetShaderParameter(PSP_ELAPSEDTIME, elapsedTime);
    }
}

void View::SetCameraShaderParameters(Camera* camera, bool setProjection)
{
    if (!camera)
        return;

    Matrix3x4 cameraEffectiveTransform = camera->GetEffectiveWorldTransform();

    graphics_->SetShaderParameter(VSP_CAMERAPOS, cameraEffectiveTransform.Translation());
    graphics_->SetShaderParameter(VSP_CAMERAROT, cameraEffectiveTransform.RotationMatrix());
    graphics_->SetShaderParameter(PSP_CAMERAPOS, cameraEffectiveTransform.Translation());

    float nearClip = camera->GetNearClip();
    float farClip = camera->GetFarClip();
    graphics_->SetShaderParameter(VSP_NEARCLIP, nearClip);
    graphics_->SetShaderParameter(VSP_FARCLIP, farClip);
    graphics_->SetShaderParameter(PSP_NEARCLIP, nearClip);
    graphics_->SetShaderParameter(PSP_FARCLIP, farClip);
[/code]

-------------------------

dragonCASTjosh | 2017-01-02 01:11:17 UTC | #61

[quote="1vanK"]Ideally, this parameter should send engine, that the player can adjust the quality of all materials[/quote]
ill look into that tomorrow :slight_smile: bug fixing for tonight.

also new commit to fix problem with area lights still rendering.

-------------------------

hdunderscore | 2017-01-02 01:11:17 UTC | #62

I am unable to even test the latest changes via the MaterialTest.xml, my PC locks up on the attempt. I guess it's the 4k textures, but not sure.

In my opinion the IBL should be using pre-filtered cubemaps rather than the method being used at the moment. You might see tools using the realtime method employed in these shaders (Substance Designer 4.5+ accepts unfiltered hdr panoramas), but a game engine that will be displaying a full scene worth of assets needs a more efficient way.

-------------------------

sabotage3d | 2017-01-02 01:11:17 UTC | #63

In some cases pre-filtered cubemaps won't work but it might be good option for more diffusive materials. Both UE4 and Unity have a roughness or metalness parameter to control the bluriness of the environment. From fully diffusive to fully reflective.

-------------------------

dragonCASTjosh | 2017-01-02 01:11:17 UTC | #64

[quote="hd_"]I am unable to even test the latest changes via the MaterialTest.xml, my PC locks up on the attempt. I guess it's the 4k textures, but not sure.

In my opinion the IBL should be using pre-filtered cubemaps rather than the method being used at the moment. You might see tools using the realtime method employed in these shaders (Substance Designer 4.5+ accepts unfiltered hdr panoramas), but a game engine that will be displaying a full scene worth of assets needs a more efficient way.[/quote]

Game engines looks to be moving towards sampling the cubemaps, and in our case it may be better as people are not going to want to capture a cubemap then put it through an external program, and an internal sampler would be a fair bit of work. and what is causing the scene not to load? because im not able to replicate many of the issues.

-------------------------

hdunderscore | 2017-01-02 01:11:17 UTC | #65

I don't believe that, do you have a source? Unity and UE4 have tools to bake lighting, so it might not take extra effort from the developer, but it's still performing the optimisation.

-------------------------

dragonCASTjosh | 2017-01-02 01:11:17 UTC | #66

Epic is performing sampling on the GPU, these samples only apply on Cubemaps/Hemisphere maps captured from within the engine   

[code]float3 DiffuseIBL( uint2 Random, float3 DiffuseColor, float Roughness, float3 N, float3 V )
{
	N = normalize( N );
	V = normalize( V );

	float3 DiffuseLighting = 0;
	
	float NoV = saturate( dot( N, V ) );

	const uint NumSamples = 32;
	for( uint i = 0; i < NumSamples; i++ )
	{
		float2 E = Hammersley( i, NumSamples, Random );
		float3 L = TangentToWorld( CosineSampleHemisphere( E ).xyz, N );
		float3 H = normalize(V + L);

		float NoL = saturate( dot( N, L ) );
		float NoH = saturate( dot( N, H ) );
		float VoH = saturate( dot( V, H ) );

		if( NoL > 0 )
		{
			float3 SampleColor = AmbientCubemap.SampleLevel( AmbientCubemapSampler, L, 0 ).rgb;

			float FD90 = ( 0.5 + 2 * VoH * VoH ) * Roughness;
			//float FD90 = 0.5 + 2 * VoH * VoH * Roughness;
			float FdV = 1 + (FD90 - 1) * pow( 1 - NoV, 5 );
			float FdL = 1 + (FD90 - 1) * pow( 1 - NoL, 5 );

#if 1
			// lambert = DiffuseColor * NoL / PI
			// pdf = NoL / PI
			DiffuseLighting += SampleColor * DiffuseColor * FdV * FdL * ( 1 - 0.3333 * Roughness );
#else
			DiffuseLighting += SampleColor * DiffuseColor;
#endif
		}
	}

	return DiffuseLighting / NumSamples;
}

float3 SpecularIBL( uint2 Random, float3 SpecularColor, float Roughness, float3 N, float3 V )
{
	float3 SpecularLighting = 0;

	const uint NumSamples = 32;
	for( uint i = 0; i < NumSamples; i++ )
	{
		float2 E = Hammersley( i, NumSamples, Random );
		float3 H = TangentToWorld( ImportanceSampleGGX( E, Roughness ).xyz, N );
		float3 L = 2 * dot( V, H ) * H - V;

		float NoV = saturate( dot( N, V ) );
		float NoL = saturate( dot( N, L ) );
		float NoH = saturate( dot( N, H ) );
		float VoH = saturate( dot( V, H ) );
		
		if( NoL > 0 )
		{
			float3 SampleColor = AmbientCubemap.SampleLevel( AmbientCubemapSampler, L, 0 ).rgb;

			float Vis = Vis_SmithJointApprox( Roughness, NoV, NoL );
			float Fc = pow( 1 - VoH, 5 );
			float3 F = (1 - Fc) * SpecularColor + Fc;

			// Incident light = SampleColor * NoL
			// Microfacet specular = D*G*F / (4*NoL*NoV) = D*Vis*F
			// pdf = D * NoH / (4 * VoH)
			SpecularLighting += SampleColor * F * ( NoL * Vis * (4 * VoH / NoH) );
		}
	}

	return SpecularLighting / NumSamples;
}
[/code]

source: [url]https://github.com/EpicGames/UnrealEngine/blob/97c8d3ef55e869e17ef149903eae2a33101381c9/Engine/Shaders/PostProcessAmbient.usf[/url]

-------------------------

hdunderscore | 2017-01-02 01:11:17 UTC | #67

I couldn't find where those two shader functions were actually used in the engine, link?

-------------------------

theak472009 | 2017-01-02 01:11:18 UTC | #68

I don't get what your goal is with the PBR Sinoid added. I am just curious as to why you are trying to change it? The original version works perfectly well. I am pretty sure it's a work in progress but what is the reason for comparing the albedoInput.a (metallic) with Magic Number -50 in DeferrredLight pixel shader? Some comments would be nice.

-------------------------

dragonCASTjosh | 2017-01-02 01:11:18 UTC | #69

[quote="hd_"]I couldn't find where those two shader functions were actually used in the engine, link?[/quote]
I dont know UE4 enough to find the implementation but from the looks of it they use it in post processing.

[quote="theak472009"]I don't get what your goal is with the PBR Sinoid added. I am just curious as to why you are trying to change it? The original version works perfectly well. I am pretty sure it's a work in progress but what is the reason for comparing the albedoInput.a (metallic) with Magic Number -50 in DeferrredLight pixel shader? Some comments would be nice.[/quote]

Alot of the work i did was heading towards where Sinoid was going. Any changes i made where for rendering quality. As for the DeferredLight shader that was used for rendering experiments and shouldnt be used, if you want to use PBR in a deferred render path then you should used PBRdeferred. I currently removed comments to keep with the style of urho shaders but i will add them back once everything is fully stable.

-------------------------

dragonCASTjosh | 2017-01-02 01:11:21 UTC | #70

After some more testing i recomend using D3D11 if you wish to use PBR as D3D9 has major stutters for some reason. Gl seams ok from testing

-------------------------

dragonCASTjosh | 2017-01-02 01:11:25 UTC | #71

I believe if we have an example scene with reasonable resolution textures then it would be ready to be merged with the master. the 4K textures are a drain for most systems

-------------------------

dragonCASTjosh | 2017-01-02 01:11:38 UTC | #72

The major part of PBR is now a pull request :slight_smile: it includes an example that does not use 4K textures and the slowest part of the demo is the 2 emissive textures but that shouldnt be a problem.

-------------------------

weitjong | 2017-01-02 01:11:38 UTC | #73

Thank you.

-------------------------

vivienneanthony | 2017-01-02 01:11:41 UTC | #74

Hi,

Did PBR get pulled into the release of Urho3D? I can't pull the newest version without ad-hocing nanodbc til the whole VS2015 is fixed. So, What do I need to use the PBR? I'm assuming copying the shader, technique, and sample materials.

Vivienne

-------------------------

dragonCASTjosh | 2017-01-02 01:11:41 UTC | #75

[quote="vivienneanthony"]Hi,

Did PBR get pulled into the release of Urho3D? I can't pull the newest version without ad-hocing nanodbc til the whole VS2015 is fixed. So, What do I need to use the PBR? I'm assuming copying the shader, technique, and sample materials.

Vivienne[/quote]

PBR is not yet merged as there are still some small fixes, as for what you need everything is there for you, just ensure you are using a PBR technique. There are a handful of example materials included

-------------------------

vivienneanthony | 2017-01-02 01:11:42 UTC | #76

[quote="dragonCASTjosh"][quote="vivienneanthony"]Hi,

Did PBR get pulled into the release of Urho3D? I can't pull the newest version without ad-hocing nanodbc til the whole VS2015 is fixed. So, What do I need to use the PBR? I'm assuming copying the shader, technique, and sample materials.

Vivienne[/quote]

PBR is not yet merged as there are still some small fixes, as for what you need everything is there for you, just ensure you are using a PBR technique. There are a handful of example materials included[/quote]

Ah. Okay.

I attempted to modify the Urho3D similiarly.  Most of it worked.

I have this messaged when I load a material. I looked for "environmentSpecular" in  your files but it's not there so I'm not certain why that is showing up also.

[code][Mon Apr  4 09:11:05 2016] ERROR: Failed to compile pixel shader PBRLitSolid(IBL PBR):
0(1394) : error C7011: implicit cast from "vec4" to "vec3"
[Mon Apr  4 09:11:05 2016] ERROR: Failed to compile pixel shader PBRLitSolid(DIRLIGHT IBL PBR PERPIXEL):
0(1128) : error C1008: undefined variable "environmentSpecular"
[Mon Apr  4 09:11:05 2016] ERROR: Failed to compile pixel shader PBRLitSolid(IBL PBR PERPIXEL POINTLIGHT):
0(1128) : error C1008: undefined variable "environmentSpecular"
[/code]

Leaving this as a result.

[i.imgur.com/vdXMxmO.png](http://i.imgur.com/vdXMxmO.png)

Vivienne

-------------------------

dragonCASTjosh | 2017-01-02 01:11:43 UTC | #77

[quote="vivienneanthony"]I have this messaged when I load a material. I looked for "environmentSpecular" in your files but it's not there so I'm not certain why that is showing up also.[/quote]
This is a known issue with OpenGL at the moment, im working on fixing the issues tonight.

-------------------------

vivienneanthony | 2017-01-02 01:11:43 UTC | #78

[quote="dragonCASTjosh"][quote="vivienneanthony"]I have this messaged when I load a material. I looked for "environmentSpecular" in your files but it's not there so I'm not certain why that is showing up also.[/quote]
This is a known issue with OpenGL at the moment, im working on fixing the issues tonight.[/quote]

Ah. Ok. Im going see whats throwing the implicit vec4 to vec3 error then.

-------------------------

dragonCASTjosh | 2017-01-02 01:11:43 UTC | #79

[quote="vivienneanthony"]

Ah. Ok. Im going see whats throwing the implicit vec4 to vec3 error then.[/quote]

that would be helpful, as for the other error you can solve it by changing the return of ImageBasedLighting located in IBL.glsl into cube

-------------------------

dragonCASTjosh | 2017-01-02 01:11:43 UTC | #80

Fixed OpenGL implementation, enjoy :slight_smile:

-------------------------

vivienneanthony | 2019-03-07 07:48:47 UTC | #81

[quote="dragonCASTjosh"]Fixed OpenGL implementation, enjoy :slight_smile:[/quote]

Cool. 

https://www.youtube.com/watch?v=6p66wzV8-ps

I have to figure out what causes the dot in the first part in the lobby but the second half is checking out the materials and seeing how light affect it.

Vivienne

-------------------------

dragonCASTjosh | 2019-03-07 07:49:00 UTC | #82

Nice results although i noticed you wasnt using a Zone with a Zone texture, PBR iuses Image Based Lighting, this will correct the lighting color to the scene and add reflections to materials that need it. Zones in Urho have the ability to capture the scene from in editor so the reflections are of the area it is within. but overall nice video

-------------------------

Enhex | 2017-01-02 01:11:56 UTC | #83

Nice work. I tried it and found some problems which I posted about here:
[topic2058.html](http://discourse.urho3d.io/t/pbr-problems/1969/1)

-------------------------

namic | 2017-01-02 01:12:05 UTC | #84

Was this merged? What's missing for PBR? Any docs on it?

-------------------------

hdunderscore | 2017-01-02 01:12:05 UTC | #85

It was merged. The docs are lacking, but if you are familiar with PBR from other engines and materials in Urho, then it's simple enough. When making a material, pick one of the PBR techniques. I've only tested the metalness/roughness workflow, so in that case in the specular texture you feed a roughness (red) /metalness (green) texture. Then you use zones in Urho to provide a zone texture for image based lighting. There is an example scene you can open in the editor to see how it was done.

-------------------------

dragonCASTjosh | 2017-01-02 01:12:06 UTC | #86

Currently there is only Metalic/Roughness workflow, im currently working on improving the whole system then i will work on docs

-------------------------

JedTheKrampus | 2017-01-02 01:12:08 UTC | #87

Have you considered using cmft (look it up on Github because I can't post links) to prefilter cubemaps for each zone rather than importance sampling the cubemap?

-------------------------

dragonCASTjosh | 2017-01-02 01:12:08 UTC | #88

[quote="JedTheKrampus"]Have you considered using cmft (look it up on Github because I can't post links) to prefilter cubemaps for each zone rather than importance sampling the cubemap?[/quote]
it was a consideration but file size limits on mobile would impact its ability to be used, engines like unreal get around this by implementing a simplified sampling system on the shader.

-------------------------

hdunderscore | 2017-01-02 01:12:09 UTC | #89

Using cmft to prefilter the cubemaps is a good way to go, and supporting it in the workflow would be nice. From my previous tests, urho has trouble reading the outputs of cmft directly though.

-------------------------

sabotage3d | 2017-01-02 01:12:12 UTC | #90

What is the current state of the PBR area lights? I stumbled upon this page it looks quite promising and there is working code as well: [url]https://eheitzresearch.wordpress.com/415-2/[/url]

-------------------------

hdunderscore | 2017-01-02 01:12:12 UTC | #91

I don't believe anyone is working or at least close to an implementation yet. Open to all contributions :smiley:

-------------------------

dragonCASTjosh | 2017-01-02 01:12:12 UTC | #92

i was looking into it but im low on time so feel free to take over with the feature :slight_smile:

-------------------------

namic | 2017-01-02 01:12:22 UTC | #93

Does this implementation support parallax mapping?

-------------------------

1vanK | 2017-01-02 01:12:23 UTC | #94

[quote="namic"]Does this implementation support parallax mapping?[/quote]

if I am not mistaken, there is no. But you can see it [post10188.html](http://discourse.urho3d.io/t/parallax-mapping-opengl-only-for-now/1158/7)

-------------------------

namic | 2017-01-02 01:12:23 UTC | #95

Yes, but how can they work together?

-------------------------

1vanK | 2017-01-02 01:12:23 UTC | #96

[quote="namic"]Yes, but how can they work together?[/quote]

through editing shaders xD

-------------------------

Lumak | 2017-01-02 01:12:42 UTC | #97

I finally downloaded 1.5 yesterday, built it, and ran some samples.  And I was surprised to see the PBR demo! I ran it and it looks amazing! Thank you, josh!

-------------------------

dragonCASTjosh | 2017-01-02 01:12:42 UTC | #98

[quote="Lumak"]I finally downloaded 1.5 yesterday, built it, and ran some samples.  And I was surprised to see the PBR demo! I ran it and it looks amazing! Thank you, josh![/quote]
I have improvement in the works, higher quality and much better performance.

-------------------------

yushli | 2017-01-02 01:12:42 UTC | #99

better quality and much better performance. Well, eager to see it show up in main branch...

-------------------------

sabotage3d | 2017-01-02 01:12:43 UTC | #100

Is the PBR currently compatible with mobile or it needs to be optimized?

-------------------------

