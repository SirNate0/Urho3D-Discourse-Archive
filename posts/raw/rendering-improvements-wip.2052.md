dragonCASTjosh | 2017-01-02 01:12:35 UTC | #1

I have recently picked up work on improving the renderer, currently none of these changes are public but in the future they will likely be merged with the master branch of Uhro. All feedback is welcome as i want this to be the best it can.

[b]Current features include:[/b]
  [ul]  [li]Physically based inverse square light falloff
    [/li][li]Pre-filtered IBL(currently handled externally)[/li][/ul]

[b]Upcoming features:[/b]
[ul][li]Screen space reflections[/li]
[li]Screen space soft shadows[/li]
[li]Area lighting[/li]
[li]Ambient occusion[/li]
[li]New water shader[/li]
[li]And more..[/li][/ul]


[b]Screenshots[/b]
[color=red]To correctly view images you will need to open then in a separate window[/color]

[i]Inverse square light falloff[/i]
This uses the technique shown in Epic's PBR paper for unreal to get a realistic falloff of light.
[spoiler][img]http://i.imgur.com/5B6b17v.png[/img][/spoiler]

[i]Pre-filtered IBL[/i]
This may be difficult to see the difference but take my word for it performance is massively increased. likely not viable for mobile due to file size limits. 
[spoiler][img]http://i.imgur.com/3hbrFd7.jpg[/img][/spoiler]

-------------------------

Victor | 2017-01-02 01:12:36 UTC | #2

Looks really good man! One request I'd really like to see happen are improvements to the water shader (or perhaps a new water shader for oceans). The current shader is really cool, although I had a hard time trying to convert this example into Urho: [shadertoy.com/view/Ms2SD1](https://www.shadertoy.com/view/Ms2SD1) (for oceans).

Now, this could be because I am still new to Urho so I don't quite understand how everything is hooked up, but that's my request. :smiley: Again, great job so far!

- Sorry if this was not a valid request/feedback.

-------------------------

dragonCASTjosh | 2017-01-02 01:12:36 UTC | #3

[quote="Victor"]Looks really good man! One request I'd really like to see happen are improvements to the water shader (or perhaps a new water shader for oceans). The current shader is really cool, although I had a hard time trying to convert this example into Urho: [shadertoy.com/view/Ms2SD1](https://www.shadertoy.com/view/Ms2SD1) (for oceans).

Now, this could be because I am still new to Urho so I don't quite understand how everything is hooked up, but that's my request. :smiley: Again, great job so far!

- Sorry if this was not a valid request/feedback.[/quote]

Ill see what i can do :slight_smile:

-------------------------

Victor | 2017-01-02 01:12:36 UTC | #4

[quote="dragonCASTjosh"]
Ill see what i can do :slight_smile:[/quote]

You rock dude!

-------------------------

sabotage3d | 2017-01-02 01:12:36 UTC | #5

Looks good. Are you doing energy conservation? As the specs and diffuse look a bit blown out. 
For example these are from Unity's PBR: 
Fully metalic: [url]http://i.imgur.com/uVYZhkc.png[/url]
Fully diffuse:  [url]http://i.imgur.com/BsqDs9E.png[/url]
And this is going from one to the other: [url]http://i.imgur.com/S12idNa.gif[/url]

-------------------------

dragonCASTjosh | 2017-01-02 01:12:37 UTC | #6

[quote="sabotage3d"]Looks good. Are you doing energy conservation? As the specs and diffuse look a bit blown out. 
For example these are from Unity's PBR: 
Fully metalic: [url]http://i.imgur.com/uVYZhkc.png[/url]
Fully diffuse:  [url]http://i.imgur.com/BsqDs9E.png[/url]
And this is going from one to the other: [url]http://i.imgur.com/S12idNa.gif[/url][/quote]

Energy conservation is something im looking into but i want to change some stuff with the BRDF first

-------------------------

Hevedy | 2017-01-02 01:12:37 UTC | #7

This is looking pretty good, good work!

By the way the other day i tested the Urho3D las master version and the new PBR + Blurred shadows have big FPS drops and low FPS compared to other game engines. Drop to 80FPS and I'm in 780GTX in UE4 I can run a scene like that probably at constant 140FPS *but I need to check that better. And the shadows got some problems with the corners got an transparent aura

-------------------------

dragonCASTjosh | 2017-01-02 01:12:37 UTC | #8

[quote="Hevedy"]This is looking pretty good, good work!

By the way the other day i tested the Urho3D las master version and the new PBR + Blurred shadows have big FPS drops and low FPS compared to other game engines. Drop to 80FPS and I'm in 780GTX in UE4 I can run a scene like that probably at constant 140FPS *but I need to check that better. And the shadows got some problems with the corners got an transparent aura[/quote]

The current problem with PBR within Urho is all the calculations are handled at runtime, engines like unreal approximate this into a texture that they load into a shader, the second feature currently listed as complete is doing this calculation prior to even shipping the engine so that performance is as high as possible for everyone.

as for shadows im looking to a screen space solution similar to unreal contact shadows thats planned for 4.13. it will allow high quality shadows on even the smallest object in the scene

-------------------------

hdunderscore | 2017-01-02 01:12:37 UTC | #9

Good to see you working on these things, thanks !

-------------------------

dragonCASTjosh | 2017-01-02 01:12:37 UTC | #10

[quote="hd_"]Good to see you working on these things, thanks ![/quote]
still having the issues you pointed out to me a while ago where dds files from cmftStudio are not being imported by Urho. Im having to result to CubeMapGen but results are very inconstant.

-------------------------

dragonCASTjosh | 2017-01-02 01:12:38 UTC | #11

I think after alot of tweeking i got the IBL system just right in terms of quality. The only downside is the amount of work needed in filtering and converting the textures extrenally
[spoiler][img]http://i.imgur.com/WBAUKwU.jpg[/img][/spoiler]

-------------------------

Hevedy | 2017-01-02 01:12:38 UTC | #12

Looking good.

I'm testing the scene with a tree model to test the shadows and the quality and I'm into problems with the shader of the tree (first problem there is missing diff+normal+mask in PBR) second problem the bark of the tree looks like if the don't are affected at all by PBR. And then I got a secondary problem with the leaves cause looks black in some parts, I will manage to send you the model tomorrow.

*As you can see the bark of the tree have a orange color at sides but not sure why is like if was metal or something.

[spoiler][img]https://dl.dropboxusercontent.com/u/28070491/URho3D/Forums/Screenshot_Wed_Jun__1_21_46_02_2016.png[/img][/spoiler]

-------------------------

dragonCASTjosh | 2017-01-02 01:12:38 UTC | #13

[quote="Hevedy"]Looking good.

I'm testing the scene with a tree model to test the shadows and the quality and I'm into problems with the shader of the tree (first problem there is missing diff+normal+mask in PBR) second problem the bark of the tree looks like if the don't are affected at all by PBR. And then I got a secondary problem with the leaves cause looks black in some parts, I will manage to send you the model tomorrow.

*As you can see the bark of the tree have a orange color at sides but not sure why is like if was metal or something.

[spoiler][img]https://dl.dropboxusercontent.com/u/28070491/URho3D/Forums/Screenshot_Wed_Jun__1_21_46_02_2016.png[/img][/spoiler][/quote]

For now I recommend waiting till i commit the new changes. I think you will like the results :slight_smile:

-------------------------

dragonCASTjosh | 2017-01-02 01:12:59 UTC | #14

I have created a performance test using the D3D11 build of the new PBR solution, can people please test and provide me the average and max tick rate of the renderer. this can be viewed by pressing F2.
Download : [url]https://drive.google.com/file/d/0B7EwsKWU8ATkclZnM0NhUEIyU1E/view[/url]

-------------------------

NiteLordz | 2017-01-02 01:12:59 UTC | #15

Launched, ran around a few seconds, and here is the RunFrame stat liine

RunFrame: 198 - 5.038 - 5.786 - 5.038 - 997.589

-------------------------

dragonCASTjosh | 2017-01-02 01:12:59 UTC | #16

[quote="NiteLordz"]Launched, ran around a few seconds, and here is the RunFrame stat liine

RunFrame: 198 - 5.038 - 5.786 - 5.038 - 997.589[/quote]

Can you tell me the render frame and your hardware, because the RunFrame can be affected by external things, also hardware would help me understand how well its performing

-------------------------

franck22000 | 2017-01-02 01:12:59 UTC | #17

Here is my performance report (I have a NVidia GTX 760): 

[img]http://i.imgur.com/tYkbKgF.png[/img]

Very nice work ! Is it some screen space reflections on the floor in the front of the door ? :slight_smile:

-------------------------

dragonCASTjosh | 2017-01-02 01:12:59 UTC | #18

[quote="franck22000"]Very nice work ! Is it some screen space reflections on the floor in the front of the door ? [/quote]
Nope not done SSR yet that is just cubemaps and lighting :slight_smile: also those results looks extremely nice 1MS on the renderer at the max

-------------------------

NiteLordz | 2017-01-02 01:13:00 UTC | #19

NVidia Quadro K2200

[img]https://s31.postimg.org/sywuzqhgr/Untitled.png[/img]

-------------------------

cadaver | 2017-01-02 01:13:00 UTC | #20

Seems to be hitting the 200 fps limiter, you can retry with -nolimit

-------------------------

dragonCASTjosh | 2017-01-02 01:13:00 UTC | #21

that's looks to be around mobile graphics card in terms of specs and I'm happy with the performance

-------------------------

dragonCASTjosh | 2017-01-02 01:13:00 UTC | #22

[quote="cadaver"]Seems to be hitting the 200 fps limiter, you can retry with -nolimit[/quote]
i consider that a good thing as it means PBR is not causing any performance issues

-------------------------

codingmonkey | 2017-01-02 01:13:01 UTC | #23

good work! I'm testing your demo and I have these debug info with -nolimit
[url=http://savepic.ru/10251683.htm][img]http://savepic.ru/10251683m.png[/img][/url]

-------------------------

1vanK | 2017-01-02 01:13:09 UTC | #24

Look forward to OpenGL version :)

-------------------------

dwlcj | 2017-01-02 01:13:09 UTC | #25

Hello dragonCASTjosh,Maybe When will add SSR feature?

-------------------------

rasteron | 2017-01-02 01:13:09 UTC | #26

Another thing to consider is mobile rendering performance with defacto standard shaders, ie. lighting with minimal or no shadows, some effects like bloom, hdr, etc.

-------------------------

dragonCASTjosh | 2017-01-02 01:13:09 UTC | #27

[quote="1vanK"]Look forward to OpenGL version :slight_smile:[/quote]
I am finishing up with the DirectX version but im happy to let someone work on a GL port of it whilst im working :slight_smile: else you may be waiting a short while

[quote="dwlcj"]Hello dragonCASTjosh,Maybe When will add SSR feature?[/quote]
I have looked into SSR and other advanced features although it will require allot of learning on my part

[quote="rasteron"]Another thing to consider is mobile rendering performance with defacto standard shaders, ie. lighting with minimal or no shadows, some effects like bloom, hdr, etc.[/quote]
The new solution should have minimal performance difference over traditional rendering as alot of the IBL is done offline. I even believe the performance is fast enough to replace the default renderer as all traditional materials should be supported on the new PBR system

-------------------------

rasteron | 2017-01-02 01:13:10 UTC | #28

Sounds good. In a related topic, pointing to this [url=https://github.com/urho3d/Urho3D/issues/1397]issue[/url] where you guys were proposing BGFX as the renderer, I think it would be a better choice moving forward but I see there's also a lot at stake on this matter. Just a thought.

Great job on the current PBR feature btw, looks good!

-------------------------

dwlcj | 2017-01-02 01:13:10 UTC | #29

I Found advanced RenderPipeline In Panda3D 
Features?
Physically Based Shading
Deferred Rendering

URl:[url]https://github.com/tobspr/RenderPipeline[/url]

-------------------------

sabotage3d | 2017-01-02 01:13:10 UTC | #30

The Panda3D PBR looks quite impressive for still frames. When I look at the Render Pipeline it looks all python based, sounds like bad performance.

-------------------------

dragonCASTjosh | 2017-01-02 01:13:10 UTC | #31

[quote="sabotage3d"]The Panda3D PBR looks quite impressive for still frames. When I look at the Render Pipeline it looks all python based, sounds like bad performance.[/quote]

Its performance is not to bad as there is a C++ backed.

[quote="dwlcj"]I Found advanced RenderPipeline In Panda3D [/quote]

I have been talking a fair bit the developer of RP to find faults and improvements with my PBR solution.

[quote="rasteron"]Sounds good. In a related topic, pointing to this issue where you guys were proposing BGFX as the renderer, I think it would be a better choice moving forward but I see there's also a lot at stake on this matter. Just a thought.[/quote]

My main reasoning behind it is because it would lower the requirements when working on the renderer without taking away developer control.




On a side note i looked into Ambient Occlusion but settled with the best solution being backed for this there will likely need to be a lightmap generator that also handles AO.

-------------------------

cadaver | 2017-01-02 01:13:11 UTC | #32

On subject of bgfx still: on the other hand if you find something it can't do or where there's a mismatch or annoyance for Urho usecase, it could be a lot harder to get those hypothetical changes approved in bgfx, instead of working within Urho's "inhouse" rendering code.

-------------------------

dragonCASTjosh | 2017-01-02 01:13:11 UTC | #33

[quote="cadaver"]On subject of bgfx still: on the other hand if you find something it can't do or where there's a mismatch or annoyance for Urho usecase, it could be a lot harder to get those hypothetical changes approved in bgfx, instead of working within Urho's "inhouse" rendering code.[/quote]

i think the main reason it keeps getting brought up is not because Urho's renderer is bad or slow, i think its because developer have to write features multiple times. for example for my PBR i had to write it once for DirectX forward, do a half write for Deferred, then i have to do a Port to GL forward then do the GL deferred, and its alot of rewriting the same feature

also do you have some kind of alert go off every time bgfx is mentioned  :smiley:

-------------------------

cadaver | 2017-01-02 01:13:11 UTC | #34

Well that's the shaders which you had to write multiple times.

No I don't have an alarm for bgfx, but now I'm actually expecting its author to appear in this thread :slight_smile:

-------------------------

dragonCASTjosh | 2017-01-02 01:13:11 UTC | #35

[quote="cadaver"]Well that's the shaders which you had to write multiple times.

No I don't have an alarm for bgfx, but now I'm actually expecting its author to appear in this thread :slight_smile:[/quote]

the simplest way to solve the shader issue is just write some preprocessor change the syntax of one of the languages but this is likely not a good long term solution. Vulkans spirv may be the best solution

-------------------------

rasteron | 2017-01-02 01:13:11 UTC | #36

To be quite honest, the current renderer works really well. The only thing that I haven't tested yet are the limits, quality and performance on an average android and other mobile devices.

I'm quite comfortable just using OpenGL/ES and GLSL, it's just a matter of preference I guess plus it works cross-platform with some tweaks.

-------------------------

dragonCASTjosh | 2017-01-02 01:13:12 UTC | #37

[quote="rasteron"]I'm quite comfortable just using OpenGL/ES and GLSL, it's just a matter of preference I guess plus it works cross-platform with some tweaks.[/quote]

This works on the game side features in shaders but when it comes to adding engine features like PBR i have to write it multiple times, it is just a little annoying as i have rebuilt my PBR system from scratch a few times and i have had to write dx at least 5 times and every time started porting to gl before i found improvements to my solution. if the shaders where unified i could just do the initial rewites and leave it at that

-------------------------

dragonCASTjosh | 2017-01-02 01:13:19 UTC | #38

PR submitted: [github.com/urho3d/Urho3D/pull/1477](https://github.com/urho3d/Urho3D/pull/1477)

-------------------------

sabotage3d | 2017-01-02 01:13:19 UTC | #39

Looks good, nice work.

-------------------------

dwlcj | 2017-01-02 01:13:19 UTC | #40

Very nice!

-------------------------

krstefan42 | 2017-01-02 01:13:42 UTC | #41

Nice work, always glad to see more modern features in Urho3D 's rendering.

[quote="dragonCASTjosh"][i]Pre-filtered IBL[/i]
This may be difficult to see the difference but take my word for it performance is massively increased. likely not viable for mobile due to file size limits.[/quote]
Why can't the pre-filtering be done at scene load time? It doesn't need to be super accurate. Heck you could almost just generate mip maps from the environment map, put on trilinear filtering, and call it a day. You could add a 1 pixel pre-pass blur to each mip to hide the pixels, or do a quick 3-tap blur filter in the final shader. Then mix the lower mips into the higher ones to better match a wide specular lobe.

[quote="dragonCASTjosh"]the simplest way to solve the shader issue is just write some preprocessor change the syntax of one of the languages but this is likely not a good long term solution. Vulkans spirv may be the best solution[/quote]
I've seen the preprocessor solution used in other code, and I think it works pretty well.

-------------------------

dragonCASTjosh | 2017-01-02 01:13:44 UTC | #42

[quote="krstefan42"]Why can't the pre-filtering be done at scene load time? It doesn't need to be super accurate. Heck you could almost just generate mip maps from the environment map, put on trilinear filtering, and call it a day. You could add a 1 pixel pre-pass blur to each mip to hide the pixels, or do a quick 3-tap blur filter in the final shader. Then mix the lower mips into the higher ones to better match a wide specular lobe.
[/quote]

the current solution is in mixing pre-filtering witha mobile friendly solution. the performance is on par with traditional pre-filtering but saves 2 samplers on the gpu as prefiltered also needs the roughness vs ndl image and irridiance map.

-------------------------

sabotage3d | 2017-01-02 01:13:53 UTC | #43

Might be cool to test against some of these PBR examples: [github.com/simongeilfus/Cinder-Experiments](https://github.com/simongeilfus/Cinder-Experiments)

-------------------------

theak472009 | 2017-01-02 01:14:06 UTC | #44

Did the guy just give up? Seems reasonable since there is not much to improve XD

-------------------------

dragonCASTjosh | 2017-01-02 01:14:07 UTC | #45

[quote="theak472009"]Did the guy just give up? Seems reasonable since there is not much to improve XD[/quote]

Im still working although a mix between lack of time and a lot of learning makes it hard. i pushed physically based light values not to long ago.

[quote="sabotage3d"]Might be cool to test against some of these PBR examples: [github.com/simongeilfus/Cinder-Experiments](https://github.com/simongeilfus/Cinder-Experiments)[/quote]

i actually looked through that whilst i was learning :slight_smile:+

-------------------------

dragonCASTjosh | 2017-01-02 01:14:12 UTC | #46

Improvements to sphere lights using the approach detailed in epic paper, with this method it should be possible to have large amounts of area lights within the scene although its limited to sphere and tube lighting only. I may look into doing other lights shapes later down the line.

Images: [url]http://imgur.com/a/69BFR[/url]

-------------------------

dwlcj | 2017-01-02 01:14:55 UTC | #47

DragonCASTjosh:
Rendering Improvements have new progress? Especially soft shadows.

-------------------------

dragonCASTjosh | 2017-01-02 01:14:55 UTC | #48

[quote="dwlcj"]DragonCASTjosh:
Rendering Improvements have new progress? Especially soft shadows.[/quote]

Not much just yet, I have been very busy with University, i also managed to lose a lot of work in a system crash so i have to rebuild the tubelight stuff. I have some local work to improve the mip sampling and the attenuation of lights under PBR. Alongside that i have put some time aside to try and work out what is wrong with variance shadow maps as in my personal testbed renderer they work perfectly and the implementation so far looks identical

-------------------------

dwlcj | 2017-01-02 01:14:56 UTC | #49

All Right?Thank you very much,dragonCASTjosh.
I Use Physically based Rendered in Urho3d.
[img]http://www.vestudio.cn/vesbbs/UploadFile/2016-10/201610247314498887.png[/img]
Missing a few things:
SSR or Ogre2.1 Parrallax Cubemap
Soft Shadow
AO
GI

-------------------------

dragonCASTjosh | 2017-01-02 01:14:56 UTC | #50

[quote="dwlcj"]All Right?Thank you very much,dragonCASTjosh.
I Use Physically based Rendered in Urho3d.

Missing a few things:
SSR or Ogre2.1 Parrallax Cubemap
Soft Shadow
AO
GI[/quote]

Awesome that someone is using the PBR stuff already :slight_smile: let me know if there us anything i can do to make it easier to use.

As for the missing features they are all on my roadmap, parallax mapping should be simple i know JSandusky had a text file explaining how to implement it in his original PBR implementation but i no longer have access to that. As for SSR im fairly new to graphics and have never touched tracing so it will be difficult to learn, same goes with GI. AO should be a little more simple and same with soft shadows

-------------------------

jmiller | 2017-01-02 01:14:57 UTC | #51

[quote="dragonCASTjosh"]Awesome that someone is using the PBR stuff already :slight_smile: let me know if there us anything i can do to make it easier to use.[/quote]

I have been using it all along (it's really easy) and could produce some very nice screenshots if circumstances would permit and I'd go to the effort. I will just say that it is well worth looking at.   :wink: 
Thanks for your ongoing work on PBR, plans sound good. Sorry to hear about system crash, I can certainly empathize and hope for speedy recovery.

-------------------------

dragonCASTjosh | 2017-01-02 01:14:57 UTC | #52

[quote="carnalis"]I have been using it all along (it's really easy) and could produce some very nice screenshots if circumstances would permit and I'd go to the effort. I will just say that it is well worth looking at.   
Thanks for your ongoing work on PBR, plans sound good. Sorry to hear about system crash, I can certainly empathize and hope for speedy recovery.[/quote]

Glad your enjoying it, and don't worry I didn't get sent to far back, I managed to get tube lighting reimplemented it on my branch for DirectX, I also found where I think the issue lies with variance shadows but I'm not sure whats wrong with it.

-------------------------

