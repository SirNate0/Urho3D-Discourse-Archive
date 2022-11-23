JeriX | 2017-01-02 01:00:11 UTC | #1

Is there any chance developers would implement basic support of WP platform in future?

-------------------------

cadaver | 2017-01-02 01:00:11 UTC | #2

SDL does support WinRT nowadays, so it's not an impossibility, but it would be a large undertaking, as it practically needs implementing a D3D11 renderer first.

-------------------------

thebluefish | 2017-01-02 01:00:15 UTC | #3

A DX11 renderer would be nice to have at some point, especially if we can take advantage of the many new features not present in DX9. The way the project is organized so far, it wouldn't be too disruptive to begin adding support for it. Though we would need someone familiar enough with DX11 to make something solid.

-------------------------

JeriX | 2017-01-02 01:00:15 UTC | #4

I've had some experience with dx11 in wp8: I think it's just some wrapper about dx9 hardware with disabled features of dx11 and enabled complexity of dx11 :angry:

-------------------------

cadaver | 2017-01-02 01:00:16 UTC | #5

There are at least two ways to go implementing a D3D11 renderer.

1) The API & compatibility-disrupting, efficient way. We change our whole low-level rendering API to benefit from D3D11 concepts, like the immutable state objects. Materials use uniform buffer objects instead of individual uniforms. OpenGL2 and D3D9 backends are rewritten to emulate D3D11 concepts. This breaks Urho programs which rely on the old low-level rendering API.

2) The minimal hack way: we write a D3D11 backend which emulates D3D9/OpenGL2 concepts like the individual renderstates and individual uniforms, and maps them to D3D11 concepts. This will not break compatibility, but it doesn't realize D3D11's full potential for performance gains.

Also, unless some magic is performed, D3D11 requires writing a third version of every shader. One possibility would be to ditch D3D9 at that point in which case we'd be back to just two versions: GLSL and D3D11 HLSL.

EDIT: somewhat related to the discussion at hand, I've started an experimental toy engine project which will explore modern graphics API's, different scene representation (basically merging the concept of "child node" and "component" into one, as well as unifying scene and UI) and radical lack of reliance on 3rd party libraries. I'm not quite up to the rendering part yet, but I'll start from D3D11. With some luck the knowledge gained from this will benefit Urho3D as well, and can in time be "transplanted" back:

[code.google.com/p/turso3d](http://code.google.com/p/turso3d)

-------------------------

thebluefish | 2017-01-02 01:00:16 UTC | #6

That toy project sounds like a great way to test concepts. I love how you specify multithreading in your "to do" list for the project, that's something that Urho3D could definitely use.

I propose a different way of implementing D3D11: Separate the Graphics subsystem. We can keep the original Graphics subsystem for OpenGL/D3D9 support, then add a Graphics_D3D11 subsystem which utilizes all the new awesome stuff that D3D11 has to offer. That way we don't need to ensure compatible between the various graphics modes.

I say this because the entire concept of implementing D3D11 being coupled with the implementation of OpenGL or D3D9 runs in the opposite direction of the existing Component-based structure.

-------------------------

cadaver | 2017-01-02 01:00:16 UTC | #7

The thing is, however, that a lot of classes in Urho rely on the Graphics subsystem API. Materials, the high-level view rendering, even UI. Having a different Graphics for D3D11 would mean also creating two versions of these classes, or a lot of #ifdef blocks inside them, and the differences could likely leak to the outside API, for example Material class exposing individual uniforms vs. constant buffers.

-------------------------

thebluefish | 2017-01-02 01:00:16 UTC | #8

Material class is part of the Graphics subsystem, there should be no problem separating it. UI is one of those things that will probably either need several #ifdef blocks or its own separate UI_D3D11 subsystem.

It sounds to me like it's time for some potential refactoring. It seems that the entire point of the subsystem-based approach is so that developers can mix-and-match just the systems they need. If we're going to run into these problems because some systems are too tightly coupled, then we need to decouple them and rethink our approach.

-------------------------

JeriX | 2017-01-02 01:00:16 UTC | #9

Maybe there is a small point to try to use [url=https://github.com/MSOpenTech/angle]ANGLE WP8 port[/url]? Just for basic support for this platform?

-------------------------

cadaver | 2017-01-02 01:00:16 UTC | #10

I don't think there's a refactoring possibility that can help to avoid coupling to Graphics, if we want to keep the idea that you write multiple rendering backends, but only need to write the higher-level rendering (meshes, lights, materials, UI) once. Compare to Ogre's RenderSystem interface, to which all Ogre's higher level classes talk to. The optional subsystems (Physics, Navigation, Network, Script...) on the other hand are very easy to keep decoupled. However, there may be a possibility to do adjustments to the Graphics API that accounts for both the old API's and new, for example make a SetShaders() call that accepts geometry / hull shader pointers, but practically those will always be null on OGL2 / D3D9.

Yes, ANGLE would be the fastest shortcut. Though considering that a phone is always slower than a PC, running extra code to function as a realtime graphics API call translator doesn't sound like it would get stellar performance.

-------------------------

cadaver | 2017-01-02 01:02:28 UTC | #11

In the Turso3D engine ([code.google.com/p/turso3d](http://code.google.com/p/turso3d)) I've now basically completed a D3D11 renderer. From this experience it should be doable to also implement D3D11 rendering in Urho. There are many options how to proceed but keeping the old Graphics API just as it is should result in reasonable performance, though obviously without any D3D11 extra features. Basically we'd create D3D11 state objects on the fly as needed from the Urho renderstates.

However, in Turso I wrote shaders from scratch using the SM4 profile, while in Urho it wouldn't be nice to have to write shaders three times (D3D11, D3D9, OpenGL). If we want to retain Urho as a viable engine for old Windows computers, dropping D3D9 means only choice is OpenGL, which may potentially have very bad drivers. SM2 could be dropped at any time though.

-------------------------

codingmonkey | 2017-01-02 01:02:28 UTC | #12

>From this experience it should be doable to also implement D3D11 rendering in Urho
cool! yes it's time )

>dropping D3D9 
it's nice idea (I always was interested only in open gl), but mb better make option for this then you build urho3d (use dx9 or dx11 )

-------------------------

weitjong | 2017-01-02 01:02:28 UTC | #13

Yes, I think there was a discussion topic quite sometime ago about supporting the "plugins" mechanism similar to Ogre's RenderSystem.

-------------------------

boberfly | 2017-01-02 01:02:29 UTC | #14

Very cool Cadaver! I like the design of Turso3D's graphics, serialising render states like this lends itself well to a Mantle/DX12 or GL-next approach, from seeing the NV_command_list extension. The multiple shaders situation is still painful though, not really sold on bgfx's approach or Unreal4's non-free HLSL cross-compiler either.

I think DX9 is still viable for all those Windows XP machines in China, it all depends what state the OpenGL driver is for these said machines, the Intel driver especially. Nvidia would expose stable enough drivers with perhaps GL3 or GL4 even.

[store.steampowered.com/hwsurvey](http://store.steampowered.com/hwsurvey)
[stats.unity3d.com/pc/](http://stats.unity3d.com/pc/)

From memory I don't think China is listed in the steam hardware survey (one of their steam dev days mentioned this that DOTA2 was deployed outside of steam in China). The Unity3D stats are more reflective of this, having the unsupported Windows XP at 39.1% (!)

-------------------------

franck22000 | 2017-01-02 01:02:30 UTC | #15

Hello Cadaver, 

I think you could drop DX9 support and keep OpenGL but maybe switch to OpenGL 3.x ? 

OpenGL support need to be keeped of course :slight_smile:

-------------------------

friesencr | 2017-01-02 01:02:31 UTC | #16

[quote="cadaver"]In the Turso3D engine ([code.google.com/p/turso3d](http://code.google.com/p/turso3d)) I've now basically completed a D3D11 renderer. From this experience it should be doable to also implement D3D11 rendering in Urho. There are many options how to proceed but keeping the old Graphics API just as it is should result in reasonable performance, though obviously without any D3D11 extra features. Basically we'd create D3D11 state objects on the fly as needed from the Urho renderstates.

However, in Turso I wrote shaders from scratch using the SM4 profile, while in Urho it wouldn't be nice to have to write shaders three times (D3D11, D3D9, OpenGL). If we want to retain Urho as a viable engine for old Windows computers, dropping D3D9 means only choice is OpenGL, which may potentially have very bad drivers. SM2 could be dropped at any time though.[/quote]

I am personally sick of transpilers from work.  Given all of the possibilities though the transpiler option, bgfx shaderc + glsl optimizer isn't a bad one.  There is also the angle approach for old intel hardware.  If we had opengl/dx11 and angle for old windows intel cards it would open up things like nanovg.

I would like to hear your more on what you learned from writing another renderer.  Did you find any oportunities for optimizations for urho cpu side?  The legendary, tyrannical king among fish will be more fierce then ever!

-------------------------

hdunderscore | 2017-01-02 01:02:31 UTC | #17

I see the earlier comments about dx11 indicate that maybe it could get messy as far as graphics classes are concerned-- but otherwise I think having duplicate shaders wouldn't be too big of an issue as we already have the dx9 shaders ready. Future shader additions is extra work on contributors, but there's nothing that requires an engine-user to write shaders/offer every graphics API option.

From an overall value perspective, I think having dx9-level support is a plus on Urho's side. Dx11 would be a great addition too.

The original topic is about getting windows phone support, so I'm not sure if it's on the table-- but would tessellation and geometry shaders be on the table with this proposed change?

-------------------------

cadaver | 2017-01-02 01:02:31 UTC | #18

D3D11 is a prerequisite for Windows Phone support. Obviously it would need work elsewhere too, but the render API is probably the biggest hurdle. Realistically speaking it will need a contributor who is interested and has hardware, to finalize the work once D3D11 support is in place, and also to keep maintaining the port.

By adopting newer rendering API's things like geometry shaders and tessellation become possible, that said I don't have experience of them so that too will probably require someone who has an idea of how they should be used and what the API should look like, but they should be easy enough to contribute once the newer API itself is in place.

For optimization: I did find some opportunities, for example simplifying the Drawable virtual function interface for updating objects in frustum, ensuring that we don't go through all the visible objects unnecessary times, and updating render state settings only just before the draw call, from a cached state that the Graphics class stores. Nothing major though, as Urho is already fairly good in its CPU & API use effectiveness.

-------------------------

boberfly | 2017-01-02 01:02:32 UTC | #19

I'd like to help with GL4/DX11 code where possible. When do you plan on integrating Turso3D things to Urho3D Cadaver? Or would you perhaps reshape Urho3D to be more in line with modern hardware and treat DX9/GL2 as a fallback?

But yeah it would just be some experiments on the side from me due to lack of time, OpenSubdiv is a nice codebase to look and see how they do tessellation in a practical way (despite the massive draw call overhead). This reminds me I got Oculus on the backburner once I get my DK2 back again too...

-------------------------

cadaver | 2017-01-02 01:02:32 UTC | #20

I will not commit to any firm promises but it looks like I'll be working on it during the first half of 2015. Will still need to make some final experiments related to shader language and perhaps implementing a quick & dirty fallback D3D9 renderer in Turso to see what it would look like before I start gutting Urho.

With current perspective it looks like the only major change would be the use of constant buffers. In Turso I have a pretty heavy-handed approach where I assume nothing of the uniforms, and actually require users (as well as the high-level rendering system) to craft properly ordered constant buffers. I'm not sure if this is the way to go, as it would make Urho somewhat less friendly to use. The alternative is to have the shader tell its constant buffer layout, and go always through that layout mapping when updating uniforms (like before). This seems to also be the approach used by bgfx.

Other things like tessellation, geometry shaders would be just additions that don't disrupt the existing API.

-------------------------

weitjong | 2017-01-02 01:02:36 UTC | #21

[quote="cadaver"]I will not commit to any firm promises but it looks like I'll be working on it during the first half of 2015. Will still need to make some final experiments related to shader language and perhaps implementing a quick & dirty fallback D3D9 renderer in Turso to see what it would look like before I start gutting Urho.[/quote]
It looks like Urho3D v2.0 is in the pipeline. I am looking forward to it.

-------------------------

rogerdv | 2017-01-02 01:02:36 UTC | #22

Ill admit that having OpenGL 2/DX9 is good to keep compatibility with old PCs, but I wouldnt mind if you upgrade Urho to Opengl 3 and Dx 11. Having tessellation is a must in today's engines.

-------------------------

devrich | 2017-01-02 01:02:37 UTC | #23

[quote="rogerdv"]Ill admit that having OpenGL 2/DX9 is good to keep compatibility with old PCs, but I wouldnt mind if you upgrade Urho to Opengl 3 and Dx 11. Having tessellation is a must in today's engines.[/quote]

I believe OpenGL 4.3 is when they started allowing tessellation shaders.  As a side note; AMD in Dec 2014 released propritary Linux drivers that make Radeon cards even as old as 5000 HD series line support OpenGL 4.4 and OpenCL 2.0 ( in case anyone working on linux has a Radeon card )

I +1 for OpenGL 4.3+ support  :smiley:

-------------------------

rogerdv | 2017-01-02 01:02:37 UTC | #24

Accroding to wikipedia, 4.0 supports tessellation via ARB_tessellation_shader. Anyway, Im not an expert in graphics. But if team decides to support Dx11 and OpenGL 3, I vote. And for an integrated editor too. And for free beers and girls.

-------------------------

devrich | 2017-01-02 01:02:38 UTC | #25

[quote="rogerdv"]...And for an integrated editor too...[/quote]

Do you mean a C++ Editor or ?

-------------------------

rogerdv | 2017-01-02 01:02:38 UTC | #26

Scene editor. Like Unity3d, or Unreal.

-------------------------

thebluefish | 2017-01-02 01:02:40 UTC | #27

While Urho3D does take some cues from Unity, I think one strong point that Urho3D has is its flexibility. The main issue with an integrated scene editor is that the more powerful you make it, the more specific it becomes. An open-source scene editor is definitely worth looking into, and [I have a simple, barebones demo here]([post4200.html#p4200](http://discourse.urho3d.io/t/a-simple-editor-in-c/730/2)).

Consider detailing what features you want in a scene editor that the current scene editor does not have.

-------------------------

rogerdv | 2017-01-02 01:02:40 UTC | #28

I dont see how Unity3d or Unreal are specific. They have been used to create all kind of games.

-------------------------

codingmonkey | 2017-01-02 01:02:40 UTC | #29

>Unity... have been used to create all kind of games.
and even if you gonna make your RTS or like "Total War" game with biggest map and many little objects, and with many details ?)

-------------------------

cadaver | 2017-01-02 01:02:41 UTC | #30

On the subject of an integrated or more advanced editor: note that Unity and Unreal both have much larger development teams. It is unrealistic to expect the same from Urho3D, at least from the core team.

IMO the included editor is somewhere halfway between a production-usable editor, and an example that says "hey, you can code an editor using the Urho3D runtime."

The idea of an external open source project for an Urho3D editor is excellent. It would be its team's call to which degree they'd support eg. integrated "test-in-editor". This requires some kind of higher level concept and structure (= more limitations) for the game code, that Urho3D itself doesn't define, as it's more like a library with a collection of subsystems that you can use like you wish.

-------------------------

amerkoleci | 2017-01-02 01:03:28 UTC | #31

I've tried the latest turso3d repo and its very good, I found HEAP MEMORY DETECTION when parsing json that has an array of values,
I saw your using your own JSON parser, can you give a look?

Thanks

-------------------------

cadaver | 2017-01-02 01:03:29 UTC | #32

You mean heap corruption? If you have a (short) reproduction case you could submit it to the turso3d project as an issue. Though the project is not really meant for public consumption or support yet.

-------------------------

amerkoleci | 2017-01-02 01:03:29 UTC | #33

Yeap, Try to parse something like this:
[code]
{
	"data" : ["one", "two", "three"]
}
[/code]

-------------------------

cadaver | 2017-01-02 01:03:29 UTC | #34

I tried parsing that from a file and calling MSVC debug heap check before and after. (VS2013 32bit and 64bit debug builds). No corruption detected in that case. I'm going to need more information (the code you used, compiler, build type.)

-------------------------

amerkoleci | 2017-01-02 01:03:29 UTC | #35

I'm using Vs 2013 and platform is Windows, seams that the copy constructor is causing problem, I'll prepare some simple stuff to showcase the issue.

-------------------------

amerkoleci | 2017-01-02 01:03:30 UTC | #36

With the upon json i'm getting:
HEAP CORRUPTION DETECTED: after Normal block (#960) at 0x007F7AB8.
CRT detected that application wrote to memory after end of heap buffer.

Memory allocated:
Vector.cpp(23)

-------------------------

cadaver | 2017-01-02 01:03:31 UTC | #37

You didn't put any example code in that post, neither I do see anything in the turso3d project's issues. If you're not going to share the code you're using to interact with the JSON classes I most probably cannot help you, with just the debug message you've given.

-------------------------

devrich | 2017-01-02 01:03:31 UTC | #38

[quote="amerkoleci"]With the upon json i'm getting:
HEAP CORRUPTION DETECTED: after Normal block (#960) at 0x007F7AB8.
CRT detected that application wrote to memory after end of heap buffer.

Memory allocated:
Vector.cpp(23)[/quote]


It may not even be Urho3D causing the issue; try looking here [url]http://stackoverflow.com/questions/19203604/heap-corruption-detected-after-normal-block[/url]

If you wrote something somewhere that overrides somehting in Vector.cpp from line 1 ~ 23 ( for example redefining the Vector class Urho3D uses )  then that may be the problem.

but as cadaver said; without the source code that's generating those errors then there is no way to actually narrow down the problem for you _other-than-guessing_ as I just did.

I hope that link i found helps as it's the closest thing I could find on your issue.

-------------------------

cadaver | 2017-01-02 01:03:31 UTC | #39

Note that we're talking about Turso3D codebase so this is actually off-topic strictly speaking. Urho itself doesn't have those same JSON classes. (Though the low-level container classes like Vector are extremely similar in the two.)

-------------------------

amerkoleci | 2017-01-02 01:03:31 UTC | #40

The issue was related to my changes, I've made some changes with String class that caused the issue, sorry for the inconvenience.

-------------------------

cadaver | 2017-01-02 01:04:18 UTC | #41

The pull request related to D3D11 & GL3 functionality is now online. [github.com/urho3d/Urho3D/pull/680](https://github.com/urho3d/Urho3D/pull/680) 

Feel free to test and comment.

-------------------------

codingmonkey | 2017-01-02 01:04:18 UTC | #42

It's not yet merged into master, but i'm check render-refactor brunch and it's compile fine on vc2013 without any errors.
But in Cmake setup window i'm not found any opengl 3.2 force option, It's used automatically when we choose GL-renderer ?
I'm already looked into new dx11 shaders code. they almost exact same as dx9 in most cases. And in this case i'm curious is they still have the same problem with VFT or not ? On old GL-renderer VFT works fine. after some hack to add engine-ability to create RGB(A)16F textures from RGB(A).

In previous shaders we could remap sampler with add number to the end of sampler name
example: sSomeSuperMap3 = use texture unit 3 (in material inspector)
is this still works for dx11 shaders? or now we have new rules to create or remap own samplers?

the newer SamplerState: they need to be configured by engine or in shader code ?
Sorry for noobiest questions, but i'm not worked with dx11 before.

And of course thank for all's of this :slight_smile: Supporting the DX11-Renderer is great step for engine.

-------------------------

cadaver | 2017-01-02 01:04:18 UTC | #43

GL3 <-> GL2 choice is dynamic during runtime, so it doesn't need a CMake option.

I haven't touched vertex texture fetch at all, actually D3D11 could set the same textures for both VS & PS so it would work like OpenGL. D3D9 is the problematic one in that respect.

The shaders do some macro trickery to work with both D3D9 / D3D11 and GL2 / GL3. Making custom samplers and assigning them to texture units works exactly like before (on D3D you choose the register, on OpenGL you postfix the unit number to the sampler name)

D3D11 sampler states are automatically created from the texture parameters, matching OpenGL & D3D9 functionality. In shader you just have to refer to the texture unit and sampler. The convention is that both the texture and sampler for a given texture unit must go to the same numbered register, so for example

[code]
Texture2D tDiffMap : register(t0);
SamplerState sDiffMap : register(s0);
[/code]

-------------------------

codingmonkey | 2017-01-02 01:04:18 UTC | #44

>on D3D you choose the register, on OpenGL you postfix the unit number to the sampler name
Oh yes, i'm just mixed these things that DX uses registers for samplers and GL don't needed this. I'm in last time just work with GL-render and forgot about this.

>so for example
I got it. thanks

-------------------------

TikariSakari | 2017-01-02 01:04:18 UTC | #45

[quote="cadaver"]The pull request related to D3D11 & GL3 functionality is now online. [github.com/urho3d/Urho3D/pull/680](https://github.com/urho3d/Urho3D/pull/680) 

Feel free to test and comment.[/quote]

I probably did something wrong, but I tried to compile it with linux and the 3d looks kinda distorted.

Here is a picture of the ninja wars:
[url]http://i.imgur.com/JGDaHkn.png[/url]

Basically it looks kinda like fish eye I guess?

On my android everything seemed to be working.

I guess this doesn't support opengles 3.0 on android tho?

-------------------------

friesencr | 2017-01-02 01:04:18 UTC | #46

[quote="TikariSakari"][quote="cadaver"]The pull request related to D3D11 & GL3 functionality is now online. [github.com/urho3d/Urho3D/pull/680](https://github.com/urho3d/Urho3D/pull/680) 

Feel free to test and comment.[/quote]

I probably did something wrong, but I tried to compile it with linux and the 3d looks kinda distorted.

Here is a picture of the ninja wars:
[url]http://i.imgur.com/JGDaHkn.png[/url]

Basically it looks kinda like fish eye I guess?

On my android everything seemed to be working.

I guess this doesn't support opengles 3.0 on android tho?[/quote]

What graphics do you have? Intel, AMD, or NVIDIA?  And what driver are you using? open source or proprietary?

-------------------------

hdunderscore | 2017-01-02 01:04:18 UTC | #47

Did you replace the old shaders with the new ones?

-------------------------

TikariSakari | 2017-01-02 01:04:18 UTC | #48

[quote="hd_"]Did you replace the old shaders with the new ones?[/quote]

ah, it was still linking the old glsl shader files. After changing the shaders to new ones, it seems to come up correctly.

-------------------------

cadaver | 2017-01-02 01:04:19 UTC | #49

GLES 3.0 support is not in; I have no hardware to test so likely someone else will have to contribute it.

-------------------------

codingmonkey | 2017-01-02 01:04:19 UTC | #50

I'm doing some tests of my FH on DX11 Renderer
and I have a little problem with my skysphere - is not visible now :frowning:
my skysphere is an simple sphere model with vertexes format: pos(vec3) + uv(vec2)
it use simple flat texture RGB (2028*2048) (not cube map)
my own shader for it (it work very well on dx9)
and for dx11 I do some fixes:
change tex2d to  Sample2D
add OUTPOSITION to oPos in VS
add  OUTCOLOR0 to oColor in PS

[code]#include "Uniforms.hlsl"
#include "Samplers.hlsl"
#include "Transform.hlsl"

void VS( float4 iPos : POSITION, 
         float2 iTexCoord: TEXCOORD0,
         out float4 oPos : OUTPOSITION,
         out float2 oTexCoord : TEXCOORD0)
{
    float4x3 modelMatrix = iModelMatrix;
    float3 worldPos = GetWorldPos(modelMatrix);
    oPos = GetClipPos(worldPos);
    
    oPos.z = oPos.w;
    oTexCoord = iTexCoord;
}

void PS(float2 iTexCoord : TEXCOORD0,
    out float4 oColor : OUTCOLOR0)
{
    oColor = cMatDiffColor * Sample2D(DiffMap, iTexCoord);
}
[/code]

maybe there is something else that I forgot to change ?

-------------------------

cadaver | 2017-01-02 01:04:19 UTC | #51

Try putting the OUTPOSITION last, and check the log that you're not getting an input layout creation error. Input layout refuses to create on D3D11 if the shader is accessing vertex elements that are not present in the vertex data.

-------------------------

TikariSakari | 2017-01-02 01:04:19 UTC | #52

I noticed quite a performance drop on linux mint for my setup. I am using Ati radeon hd 5870 + amd x6 t1050 processor. I am using these drivers: 
[url]http://support.amd.com/en-us/kb-articles/Pages/AMDCatalystOmegaLINReleaseNotes.aspx[/url]

I tried restarting computer in case it makes a difference, but there was none. I am using custom outline shader, but even if I disable it, it doesn't really make much impact on fps.

It looks like there is huge difference in light rendering for some reason. I tried using those remove specular, etc from the hud, but it had almost no impact either.

I am using same code base for both, so if something would needed to be changed with the light system or something else, that would explain the difference.

Old gl2, 140fps:
[url]http://i.imgur.com/La1rGVy.png[/url]

Gl3, ~40fps:
[url]http://i.imgur.com/svPupdh.png[/url]

For why the house is less visible in the gl2, I was testing out day-night cycle, where I rotate the node that has directional light attached to it in update method. Maybe this could be something that slows down gl3, when I adjust the lights rotation on every frame, or I am doing it in wrong place.

The code is as simple as this:
[code]
    lightRot_ += dt * 10.0f;
    while( lightRot_ > 360.0f )
        lightRot_ -= 360.0f;

    lightNode_->SetRotation(Quaternion(lightRot_, 0.0f, 0.0f));
[/code]

Maybe there is better lighting system with gl3 than gl2, which would cause the drop in frame amount, or possibly the linux doesn't hw accelerate gl3 for my gpu.

-------------------------

cadaver | 2017-01-02 01:04:19 UTC | #53

It's possible your driver falls back into some degree of software mode for GL3. It's hard to predict though when that will happen. You can use the -gl2 commandline switch or the "ForceGL2" engine startup option to force always to use GL2.

-------------------------

codingmonkey | 2017-01-02 01:04:19 UTC | #54

[code]#include "Uniforms.hlsl"
#include "Samplers.hlsl"
#include "Transform.hlsl"

void VS(float4 iPos : POSITION, 
        float2 iTexCoord: TEXCOORD0,
        out float2 oTexCoord : TEXCOORD0, 
        out float4 oPos : OUTPOSITION)
{
    float4x3 modelMatrix = iModelMatrix;
    float3 worldPos = GetWorldPos(modelMatrix);
    oPos = GetClipPos(worldPos);
    
    oPos.z = oPos.w;
    oTexCoord = iTexCoord;
}

void PS(float2 iTexCoord : TEXCOORD0, 
        out float4 oColor : OUTCOLOR0)
{
    oColor = cMatDiffColor * Sample2D(DiffMap, iTexCoord);
}[/code]

Yes, making the OUTPOSITION as last - helps, now SphereSky  is visible. Thanks
i don't remember but in dx9 shader this order (of outputs) is also been important or not ?

-------------------------

cadaver | 2017-01-02 01:04:19 UTC | #55

It's a D3D11 only phenomenon. It's rather odd that it happens, particularly when the shader compiler doesn't warn of it in any way. Has also happened if the interpolators have been in "wrong" order. Possibly the preferred way on D3D11 is to define your shader inputs and outputs as structs, for example like seen in [github.com/cadaver/turso3d/blob ... Diffuse.vs](https://github.com/cadaver/turso3d/blob/master/Bin/Data/Diffuse.vs)

-------------------------

codingmonkey | 2017-01-02 01:04:19 UTC | #56

> Possibly the preferred way on D3D11 is to define your shader inputs and outputs 
Probably
i trying to use this structs but fail. Got an error something about mul (bla bla...) and few time about not defined cModel (from cbuffer). Anyway is the custom output of VS or PS is supported by engine parser ? i think that the using input/output parameters is enough for me.

after the sky problem has been solved.
I still have an other problem with bot's laser fx.
There is using std tech DiffAddAlpha.xml with one diffuse texture. And it absolutely invisible now, but in material inspector in preview it looked very well. i guess that it's again some problem with input data (geometry) for shader. Now i'm try to figure out that wrong with it.

Well now laserFx is visible
[url=http://savepic.su/5478352.htm][img]http://savepic.su/5478352m.png[/img][/url]
I'm change the Unlit.hlsl with modifying an input parameters - add to VS input iNormal because model have a normals, when I doing export I choose options: pos + normal + uv.
But there have some errors in console.

-------------------------

cadaver | 2017-01-02 01:04:20 UTC | #57

I'm not completely sure what you're asking, but the COMPILEVS & COMPILEPS macros are defined depending on the shader being compiled from the shared source file, so you can use that to mask away code or definitions that would produce errors in the "other" shader. Other than that, you're free to feed whatever HLSL you want into the compiler and Urho is simply doing some things in its own way in the inbuilt shaders to ensure that the same shaders work for D3D9 & D3D11 with minimal changes. But if you wanted, you could rewrite the shaders in full D3D11 style.

-------------------------

codingmonkey | 2017-01-02 01:04:20 UTC | #58

>but the COMPILEVS & COMPILEPS macros are defined depending on the shader being compiled from the shared source file, so you can use that to mask away code or definitions that would produce errors in the "other" shader
I know, but cbuffer with cModel was defineted in VS and in VS I'm got an error with cModel undefinited )

I solved previous problem with console errors.
1. copy Shader / Unlit.hlsl
2. name copy as Shader / UnlitWithNormalsInGeometry.hlsl :slight_smile:
3. add iNormal to VS  input parameters
4. copy Tech / DiffAddAlpha.xml and name copy as DifAddAlphaGwN.xml (+GeometryWithNormals)
5. open DiffAddAlphaGwN.xml and change unlit to UnlitWithNormalsInGeometry
6. change the tech for laser materials with this new tech

-------------------------

NiteLordz | 2017-01-02 01:04:20 UTC | #59

AngelScripy does not run on the Windows Phone device as well. It will run on the emulator, as it compiles with the x86 but the arm version does not support native calling on WP. I have been working with the author of AngelScript, but we are currently stuck.

-------------------------

