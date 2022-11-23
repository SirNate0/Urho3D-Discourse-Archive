dragonCASTjosh | 2017-01-02 01:10:46 UTC | #1

Im trying to add a new buffer into the G-Buffer to handle specular color and roughness. But they way its set up is confusing me a little as OpenGL outputs gl_fragcolor[2] as the normalbuffer, the normal buffer is in sampler slot 2. but gl_fragcolor[3] is the depthbuffer and the depthbuffer is resisted as sampler 13. Similar scenario for DirectX so any help would be appreciated.

-------------------------

codingmonkey | 2017-01-02 01:10:47 UTC | #2

Hi, so why you do not use this scenario ? 
[img]https://habrastorage.org/files/f34/422/ef5/f34422ef554f49a3979f85c4cd9ac35c.jpg[/img]
[habrahabr.ru/company/mailru/blog/248873/](https://habrahabr.ru/company/mailru/blog/248873/)

in comments folks talked about what depth(hw) actually no real render target (so it do not use MRT output I think) (except additional user's linear sw depth 16f/32f), so actually on this picture only used 3 - RTT = 96bit per pixel
HDR - are lighting buffer for GI and self-illuminated objects
also they talked what, additional G-buffer RTTs produce move overdraw for objects in separated passes. So, they keep g-buffer as possibly tiny.

-------------------------

dragonCASTjosh | 2017-01-02 01:10:47 UTC | #3

[quote="codingmonkey"]Hi, so why you do not use this scenario ? 
[img]https://habrastorage.org/files/f34/422/ef5/f34422ef554f49a3979f85c4cd9ac35c.jpg[/img]
[habrahabr.ru/company/mailru/blog/248873/](https://habrahabr.ru/company/mailru/blog/248873/)

in comments folks talked about what depth(hw) actually no real render target (so it do not use MRT output I think) (except additional user's linear sw depth 16f/32f), so actually on this picture only used 3 - RTT = 96bit per pixel
HDR - are lighting buffer for GI and self-illuminated objects
also they talked what, additional G-buffer RTTs produce move overdraw for objects in separated passes. So, they keep g-buffer as possibly tiny.[/quote]

My current issue is that the specular is an RGB colour value so there is not enough space in the current buffers. But if depth is not a real RTT then id have to add a buffer before it and move depth to the end although this is just a guess at the moment.

-------------------------

codingmonkey | 2017-01-02 01:10:47 UTC | #4

>My current issue is that the specular is an RGB colour value so there is not enough space in the current buffers
This leads to a natural question, can we just save F0 instead RGB values ?

-------------------------

dragonCASTjosh | 2017-01-02 01:10:47 UTC | #5

[quote="codingmonkey"]>My current issue is that the specular is an RGB colour value so there is not enough space in the current buffers
This leads to a natural question, can we just save F0 instead RGB values ?[/quote]

it represents a color, and its not ideal to recalculate this value.

[code]    #ifdef PBR
		
        #ifdef SPECMAP // SPECULAR
            float4 specSample = Sample2D(SpecGlossMap, iTexCoord.xy);
            float3 specColor = specSample.rgb;

            #ifdef ROUGHNESS
                float roughness = max(0.04, specSample.a);
            #else
                float roughness = max(0.04, 1.0 - specSample.a);
                roughness *= roughness;
            #endif            

			roughness += cRoughness;
             roughness = pow(roughness, 2);
            specColor *= cMatSpecColor.rgb; // mix in externally defined color

        #elif METALIC // METALNESS
            float4 roughMetalSrc = Sample2D(RoughMetalFresnel, iTexCoord.xy);

            #ifdef ROUGHNESS
                float roughness = max(0.04, roughMetalSrc.r);
            #else
                float roughness = max(0.04, 1.0 - roughMetalSrc.r);
                roughness *= roughness;
            #endif

			roughness += cRoughness;
             roughness = pow(roughness, 2);
            float metalness = clamp(roughMetalSrc.g + cMetalic, 0.0, 1.0);
            
            float3 specColor = max(diffColor.rgb * metalness, float3(0.08, 0.08, 0.08));
            specColor *= cMatSpecColor.rgb;
            diffColor.rgb = diffColor.rgb - diffColor.rgb * metalness; // Modulate down the diffuse
		#else
			float roughness = cRoughness;
            roughness *= roughness;
			float metalness = cMetalic;

            metalness = clamp(metalness, 0.01, 1.0);
		 
			float3 specColor = max(diffColor.rgb * metalness, float3(0.08, 0.08, 0.08));
			specColor *= cMatSpecColor.rgb;
			diffColor.rgb = diffColor.rgb - diffColor.rgb * metalness; // Modulate down the diffuse
        #endif[/code]

-------------------------

codingmonkey | 2017-01-02 01:10:47 UTC | #6

S?bastien wrote in his topic what: 
[quote]Specular texture is now rather constant and gloss is high-resolution [b]monochrome[/b]. For advanced materials, a high-resolution specular texture can be authored [1].[/quote]
[seblagarde.wordpress.com/2011/0 ... ting-mode/](https://seblagarde.wordpress.com/2011/08/17/feeding-a-physical-based-lighting-mode/)

monochrome - means 8bit in low budget case, or no? )

Actually i'm do not know how they use this F0 on second rendering steps and got colored spec. 
But I guess what using of monochrome Specular it's world standard of PBR )

-------------------------

dragonCASTjosh | 2017-01-02 01:10:47 UTC | #7

[quote="codingmonkey"]S?bastien wrote in his topic what: 
[quote]Specular texture is now rather constant and gloss is high-resolution [b]monochrome[/b]. For advanced materials, a high-resolution specular texture can be authored [1].[/quote]
[seblagarde.wordpress.com/2011/0 ... ting-mode/](https://seblagarde.wordpress.com/2011/08/17/feeding-a-physical-based-lighting-mode/)

monochrome - means 8bit in low budget case, or no? )

Actually i'm do not know how they use this F0 on second rendering steps and got colored spec. 
But I guess what using of monochrome Specular it's world standard of PBR )[/quote]

They are using a Spec/Gloss workflow although what worked on is mainly a Metal/Rough workflow and converting the spec to monochrome would make it a greyscale value, in a real world representation it should be all thats need but Urho3d allow for control over the specular color so this can not be the case.

refer to page 16 table3: [url]http://www.frostbite.com/wp-content/uploads/2014/11/course_notes_moving_frostbite_to_pbr.pdf[/url]

-------------------------

codingmonkey | 2017-01-02 01:10:47 UTC | #8

>They are using a Spec/Gloss workflow although what worked on is mainly a Metal/Rough workflow and converting the spec to monochrome 
Oh, thank for clarify. I do not figure out a lot with this PBR  rendering and so on... so actually I can't help you a lot with this.

[spoiler]find slides: [slideshare.net/makeevsergey/ ... 14finalv21](http://www.slideshare.net/makeevsergey/skyforge-rendering-techkri14finalv21)
slide 72 show spec F0[/spoiler]

-------------------------

dragonCASTjosh | 2017-01-02 01:10:47 UTC | #9

[quote="codingmonkey"]
so actually I can't help you a lot with this.[/quote]

Thats ok, i just need to add a new buffer into urho3d and ill be good :slight_smile:

-------------------------

cadaver | 2017-01-02 01:10:50 UTC | #10

D3D9 limits maximum rendertargets to 4, in which case there is no room for an added RT, unless hardware depth is used, which not all GPU's support.

It's OK to change the D3D11 & GL rendering code to support more than 4 though, but please don't touch the original deferred renderpath, which shouldn't use any more RTs due to efficiency concerns. It's OK if you make separate renderpath and lighting shaders for PBR.

-------------------------

dragonCASTjosh | 2017-01-02 01:10:50 UTC | #11

[quote="cadaver"]D3D9 limits maximum rendertargets to 4, in which case there is no room for an added RT, unless hardware depth is used, which not all GPU's support.

It's OK to change the D3D11 & GL rendering code to support more than 4 though, but please don't touch the original deferred renderpath, which shouldn't use any more RTs due to efficiency concerns. It's OK if you make separate renderpath and lighting shaders for PBR.[/quote]

So far i have managed to integrate PBR alongside the Forward renderer without changing its original functionality. i plan to do the same for deferred, since its the case you dont approve of additional RT's i will look into recalculating the specular color.

-------------------------

cadaver | 2017-01-02 01:10:50 UTC | #12

It wouldn't be a problem to add RTs if you create a separate PBR deferred renderpath. Actually there would probably be two: PBR deferred non-hardware depth (with extra linear depth RT), and PBR deferred hardware depth (no depth RT needed)

-------------------------

dragonCASTjosh | 2017-01-02 01:10:50 UTC | #13

[quote="cadaver"]It wouldn't be a problem to add RTs if you create a separate PBR deferred renderpath. Actually there would probably be two: PBR deferred non-hardware depth (with extra linear depth RT), and PBR deferred hardware depth (no depth RT needed)[/quote]

ill do some testing, but the main reasons i was avoiding adding an extra render path is PBR materials will look extreamly broken on none PBR paths, and this could confuse people who are new to the engine.

-------------------------

cadaver | 2017-01-02 01:10:50 UTC | #14

There are probably hundreds of ways to shoot yourself in the foot or get confused in a 3D engine (starting even from simple things like camera near and far clip) so I wouldn't personally use that as a reason to limit myself or do a lesser implementation of some effect.

That said, so far the renderpaths have aimed at producing the same output, so naturally it's cleaner if no extra ones are added.

-------------------------

dragonCASTjosh | 2017-01-02 01:10:50 UTC | #15

[quote="cadaver"]There are probably hundreds of ways to shoot yourself in the foot or get confused in a 3D engine (starting even from simple things like camera near and far clip) so I wouldn't personally use that as a reason to limit myself or do a lesser implementation of some effect.

That said, so far the renderpaths have aimed at producing the same output, so naturally it's cleaner if no extra ones are added.[/quote]

I personally dont think it would lesser the effect if i dont implement the renderpath, the worst case of not doing so would likely be less then 1 ms additional render time on a standard game scene. So i believe keeping it cleaner may be a better option in this scenario especially with dx9 limitations.

-------------------------

