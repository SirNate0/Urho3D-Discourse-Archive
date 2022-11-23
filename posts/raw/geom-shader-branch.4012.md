Sinoid | 2018-02-13 08:51:45 UTC | #1

Rather than try to update my old GS stuff I've started over (I wasn't very happy with it back then anyways). In this implementation, I've opted that the VS and GS must always use the same constants (sort of moot in GL), though it's a minor change if it has to change - but I don't see the point until a case arises that it has to be. Realistically the VS->Hull->GS->Domain all need the same info.

[Branch is here](https://github.com/JSandusky/Urho3D/tree/GeometryShaders). Both OpenGL and DX11 are there and it's more or less done, just requires doing something *real* like particle expansion to make sure it holds up in practice and a bit more aggregating shaders together instead of separate listings (so Hull/Domain aren't more mess).

---

Clone+perturb cube test (*GSTest.___* in the branch):

HLSL:

![image|690x368](upload://iVO51Qd4towoj30V4Yu3lmRkwzo.jpg)

GLSL (different because I bumbled maxvertex ct in HLSL):

![image|690x368](upload://1TMw7K0xYoWI43diNME43kwwbZ6.png)

-------------------------

Sinoid | 2018-02-14 07:39:59 UTC | #2

Tessellation is pretty much there, I didn't get a chance to test it today but it's at the point where it has to be tried out before anything remaining can really be identified.

On GLES and D3D9 the bulk of the GS/TCS/TES code is #ifdef'ed out. It only remains in sparse places like `Graphics` where it doesn't add any meaningful bloat and in function signatures where the parameters are checked and errors logged (*"Tessellation not supported by this GL context"*, etc). The #ifdef'ing does go against coding conventions in some places but that's a tradeoff to keep the preprocessor blocks at a minimum instead of scattered all around (everything about GS/TCS/TES in one place instead of where it *should* be).

OpenGL core profiles are now checked and the api named appropriately for 3.3 (GS), 4.0 (TCS/TES), and 4.3 (compute/ssbo). 

Likewise for DX11 with feature levels checked for whether geometry shaders are supported (10_0+) as well as hull/domain/compute shaders (11_0+). If feature level 11_0 or greater is detected then shaders will compile targeting shader-model 5 instead of shader-model 4 as this includes structured buffer support and other things needed for DX11 compute in the future.

For naming I've settled on using the OpenGL naming scheme of TCS and TES while using the platform specific names in logged messages (ie. *"Failed to compile hull shader"* on DX11), my reasoning being that error googling will be easier when the correct term is right there.

-------------------------

Sinoid | 2018-02-15 11:25:36 UTC | #3

Tessellation works on DX11 now (6, 3 tess levels):

![image|690x368](upload://uQXaOx3njlyf1CZkqOAmBnF6pw4.png)

A bit buggy (a botched tess-shader eats the next draw too) and I need to clean up some mess in forcing patch topology. If you try to render with hull/domain shader bound and not using a patch topology ... not only the GPU goes down, Windows goes down with it (at least on both my 980 and Intel HD).

Prettier geometry shader (because tess isn't very pretty):

![image|690x374](upload://9JA2nRp9euFM1raKATBEhRUVJpN.png)

A couple of bug-fixes to do but so far so good.

-------------------------

Eugene | 2018-02-15 11:45:50 UTC | #4

Great!
BTW, what do you think about BGFX renderer?

-------------------------

Sinoid | 2018-02-15 15:13:02 UTC | #5

Do you mean BGFX in general or a BGFX renderer for Urho?

**In general:**

I got to work with it recently (both as-is and in a gutted form with all the *bx* stripped away). It was being used as one of several controls to measure performance against so I had to port all of rendering to BGFX.

I loved the struct basis rather than parameter heavy functions, I totally duped that in my own framework as it gives such a nice DirectX style feel that's really natural. I'll avoid badmouthing it, but it sits in this strange indeterminate place where it's neither low-level nor high-level ... which isn't a place a 3rd party API should ever be.

Except the shading *language* - that thing is a crime against humanity and is probably accelerating the heat-death of the universe. That thing made me angry enough to start a shading language project out of spite.

**In Urho:**

It doesn't bring anything to the table beyond *"well, don't have to maintain a mid-level renderer anymore"*. Switching to BGFX isn't going to make the work going on in `View`, `Renderer`, or script bindings any simpler. It's not going to rectify the issues with insignificant material changes constituting a new batch, provide materials/techniques, etc ... solving problems is still work.

In Urho3D the Direct3D11 specific code is 5,320 lines, Direct3D9 is 5,116, and OpenGL is 5,774 ... sure there's probably more elsewhere wrapped in preprocessor blocks but it's still barely anything (that's with counting { and } only lines to boot).

The inflated perception of the renderer as a large beast is probably made worse with shaders existing in this nebulous state of *"they're examples"* but actually massive catch-all programs - imparting a draconian feel that is stuffy compared to looking at trivial BGFX shaders that do 5%. Stack on some technique, texture, and material XML and the pain begins.

The *missing* renderers are also really a non-issue IMO. If they were that desirable someone would've already done it. Vulkan has been around for 2 years now, *"no vulkan"* grumbles really don't hold water ... and again, BGFX doesn't help there, or with DX12 either (rubbish implementation).

-------------------------

Eugene | 2018-02-15 15:52:10 UTC | #6

Thanks for answer!
[quote="Sinoid, post:5, topic:4012"]
Do you mean BGFX in general or a BGFX renderer for Urho?
[/quote]
I meant both.

[quote="Sinoid, post:5, topic:4012"]
but it sits in this strange indeterminate place where it’s neither low-level nor high-level
[/quote]
I noticed it too. AFAIK it's needed for fine optimization of things for different platforms..
I dislike how BGFX handles uniforms, but I'm afraid it would be other issues if BGFX would be just command player w/o this sorting and grouping.

[quote="Sinoid, post:5, topic:4012"]
Except the shading language - that thing is a crime against humanity and is probably accelerating the heat-death of the universe. That thing made me angry enough to start a shading language project out of spite.
[/quote]
Y? Generic SL is probably most important thing in renderer (except compute shaders) that Urho misses.

-------------------------

Sinoid | 2018-02-16 01:26:44 UTC | #7

[quote="Eugene, post:6, topic:4012"]
Y? Generic SL is probably most important thing in renderer (except compute shaders) that Urho misses.
[/quote]

For that reason. It brings nothing else to the table except working in multiple places (at the cost of being a limited subset) and is just another macro/substitution setup. In contrast CG brings CGFX as an option, is an actual defined language - HLSL brought FX (which though deprecated will probably never die), etc.

I'm admittedly a bad person for comment on that as I don't see 2 or even 4 shading languages as serious of a problem as settling on a LCD set of common functionality/patterns. 

Who is the shading language really even for? The shaders should face the programmer, the properties of the shader should face the designer.

I've pretty much gone entirely visual anymore, doing something similar to the TFX system in Destiny [ARR slides](http://advances.realtimerendering.com/destiny/gdc_2017/index.html). Has been pretty trivial, except for the *linking*, tying the disparate ends together is super-duper hard hard-coding land. Miserable land of  no winning there.

-------------------------

Sinoid | 2018-02-26 04:53:44 UTC | #8

Tessellation now works in OpenGL:

![image|690x368](upload://z8jGY5g8XgvNuKpc6DRdrhGg6f.png)

I didn't push a shader because while it only took a few minutes to wrap it up I gutted the daylights of the OGL shaders as I was troubleshooting, so my shader became too much of a hairy ball of #line statements and other assorted nastiness.

Using tessellation on OGL requirs setting the #version number in shaders to a target that supports the necessary constructs (ie. gl_InvocationID undefined error means the version is too low).

**To Do**
- Up until now GLSL versioning hasn't really been an issue
    - need to sort something out, ie. 400 but not 410 supported, 410 but not 400, etc
- ~~Patch primitive types~~
    - If tessellation is active geometry must be rendered as patches (GL will silently fail, DX will seize the system)
    - Currently I override as a 3-point patch if tessellation shaders are bound, I expect to leave that as default and add a PATCH_QUAD_LIST primitive that can be used explicitly where quads are desired (like terrain), higher primitives are off into a land of 
    - Higher than quads is off into "*very specialized use case, you must know what you're doing if you want it*" land
- ~~Considerations for stream-output~~
    - That's an entire project in itself, it's viable just a large scope endeavor
- Reference shaders (probably just for working with the LitSolid shaders)
    - ~~Unlit Particle~~
    - Lit Particle
    - Lit Solid
- ~~Billboard set particle expansion in GS option~~
- ~~Support GS/HS/DS on renderpath quad commands~~

Commentary welcomed on the points above as well as the branch.

I won't be touching it for a while as this is a good empty weekend for me to sit down and write  a DirectX12 renderer ... so I'll probably come back to this in a week once I have that working.

-------------------------

Egorbo | 2018-02-20 16:21:49 UTC | #9

Amazing, looking forward to seeing GS in the main branch :slight_smile:

-------------------------

Sinoid | 2019-05-23 13:20:03 UTC | #10

Wrapping up particles this evening. Implemented as adding a *"Generate Points"* option to BillboardSet that will have it generate a POINT_LIST instead of a triangle list with the size/UV coordinates packed as XY=min, ZW=max.

Two *Disco* instances, one using regular quads and the other emitting as points that are expanded in geometry shader:

![image](upload://p99z1nIMDmHF6JO1OC1kaZuIzfU.png)

Applicable to everything using UnlitParticle shaders, I'll get to LitParticle later. 

Nothing auto-magical, still requires setting a material and technique as usual:

    <technique vs="UnlitParticle" ps="UnlitParticle" gs="UnlitParticle" 
        vsdefines="VERTEXCOLOR" gsdefines="VERTEXCOLOR" psdefines="DIFFMAP VERTEXCOLOR ADDITIVE">
        <pass name="alpha" depthwrite="false" blend="add" />
    </technique>

... so pretty much the same to use.

-------------------------

Sinoid | 2018-03-06 19:18:30 UTC | #11

General status:

- DX11 cbuffers actually work now (I botched that so hard)
- Techniques set support flags for GS and tessellation requirements so technique selection can bypass unsupported techniques
    - Of course it can't do anything about supported primitives (quad-patches, points for expansion, etc)
- Lighting shader permutations are generated ... no idea WTF I was thinking omitting those
    - Particles are now 1:1 identical for both Unlit and Lit, I'll push those shaders later after some cleanup

Here's some happy GS particles verifying the whole pipe is healthy:

![LitGSParticle|690x355](upload://jdWQNZOEClUMZBV1QDT2MgNCq60.gif)

Probably a week out before I'll submit a PR.

- Remaining
    - Documentation updates
        - I've been lagging on that
    - Two tessellation example materials derived from UnlitSolid
        - A simple phong subdivision
        - Displacement mapping
- Definitely won't be doing (at least for the foreseeable future)
    - GS expansion for beams, the smorgasbord of options is way too huge to even go there
    - LitSolid tessellation 
        - lighting is pain and LitSolid shaders are long past nuts

Although point expanded billboards create an awkward loop of "*here's this trait in a component that I can only use based on specific material properties, which come from the particle effect resource I give the emitter, that material also has to use a technique whose shaders are configured to work with a particular input ... okay*" - I'm at a loss for what to do about it that isn't either draconian or just shifting that brittleness elsewhere.

-------------------------

Sinoid | 2018-03-13 18:51:06 UTC | #12

Pushed phong-tessellation shaders for both HLSL and GLSL, shader is **Tess_Unlit**. Material located in `Materials/Demo/Tess_Distance_Kachujin.xml`. Should probably rename that folder to *UsageDemos* or something that is a little clearer that indicates that contents are just *"this is an example of how you use this stuff"* and not a first-class-citizen demo.

They use a `TessParams` float4 for controlling the traits.

- X: maximum tessellation level (clamped at a max of 16 so accidents don't result in murder)
- Y: distance at which tessellation begins (outside of that is always as-is)
- Z: offset adjustment to shift the distance, so you don't have to get right on top of it to hit the
 max
- W: phong smoothing power, 0.3 - 0.7 is sane - beyond 1.0 and *stairs* get introduced

The #defines `TESS_PHONG` activates the phong-smoothing and `TESS_FIXED` disables the distance levels, in which case it uses the maximum tess-level at all times.

The shader only performs backface culling, the information required for frustum or behind-camera culling isn't currently passed off to shaders.

Untessellated:

![Urho3D_editor_-_Untitled_2018-03-11_16-33-21|690x368](upload://o1gEp2GxOImrl6CYPmJOuIhRV6a.jpg)

Tessellated (just one extra level) at 0.3 smoothing power:

![Urho3D_editor_-_Untitled_2018-03-11_16-34-07|690x368](upload://nKIwz4Ge78a5MAeZ5Ex8Mp9EKms.jpg)

Obviously normals have to be identical across seams so models that aren't, like the Ninja, are crack-city.

-------------------------

franck22000 | 2018-03-29 20:53:37 UTC | #13

Hello Jonathan,

Any ETA for the PR to be ready ? Im very interested by this :) 

Keep up your good work. Your work is very usefull for the Urho community.

-------------------------

Sinoid | 2018-03-30 18:16:11 UTC | #14

[quote="franck22000, post:13, topic:4012"]
Any ETA for the PR to be ready ? Im very interested by this :slight_smile:
[/quote]

Probably towards the end of the weekend.

I doubt this will be a quick PR to get merged, I expect it could take a week or longer given the breadth of the changes.

-------------------------

Sinoid | 2018-03-31 21:09:22 UTC | #15

Particle shaders have been published:

https://github.com/JSandusky/Urho3D/commit/f1126f0b1010a85b5311a838e11aa8c555fb6d96

`GS_Burst` particle effect is setup to use geometry shader point-expansion. Setting up your own techniques for point-expansion requires adding a `POINTEXPAND` definition to the VS and GS defines, as well as specifying the LitParticle / UnlitParticle shaders for the GS stage.

The ParticleEmitter component also needs the new `Generate Points` attribute set so it'll use point emission mode.

Commentary welcome, particularly on how the GLSL split is handled. If anyone tries it out let me know if anything is broken.

-------------------------

Sinoid | 2018-04-07 03:51:16 UTC | #16

@weitjong @Eugene would you prefer the PR as is with many commits or would you prefer it collapsed down into one monolithic commit?

I don't have a problem with a *dead* PR for review purposes followed by collapsing it down for a final one. 

There was some swing. In particular, I originally avoided having GLES2/DX9 unaware of the additional shader stages, but supporting technique selection based on platform support and scripting forced me to reverse that.

I'm not strictly attached to the particle/BillboardSet changes, not going to cry if those have to be split off and put into a *to revisit* or such. Really just a solid proof of a complex case.

-------------------------

Eugene | 2018-04-07 06:39:48 UTC | #17

IMO 10-20-30 commits are fine to be merged as is. 
Aand anyway, let’s start here

-------------------------

weitjong | 2018-04-07 07:43:23 UTC | #18

Thanks in advance for the PR. If the commit messages are decent, i.e. you are comfortable to have them made public then they should be ok. Only on rare situation we are forced to request for squashing the commits. The choice is yours to make.

-------------------------

Sinoid | 2018-04-22 06:48:39 UTC | #19

Not going to move forward with this. I'll leave the fork up though.

The community is still a poisonous pit of OSS evangelism and I don't want to be a part of that. Like the RakNet stuff before, IDC what is done with it.

Most are incapable of using this stuff anyway, so it's just a headache if it were merged as they can't be bothered to turn on the debug layer to troubleshoot. Tesselation and GS do not tolerate incompetence, there's a lot of that around here.

-------------------------

rku | 2018-04-22 09:41:32 UTC | #20

I can not comment much on share in this thread as i have not looked through it, but it does look potentially useful and we are extremely thankful for your contribution.

[quote="Sinoid, post:19, topic:4012"]
a poisonous pit of OSS evangelism
[/quote]

This is mean.

I probably should not, but here we go...

This is OSS project. A colossal amount of work are given free to everyone (you included). Naturally it is expected for community members to contribute back. You do not have to however. There are plenty of closed projects showed off in showcase forum and noone bats an eye about closed projects. If you received unexpected responses triggering this reaction then maybe it was your failure in communication?

I have not noticed anything bad said towards yourself. All discussions in this forum are respectful. This is not the first time you have a temper outburst though. There were rage-deleted repositories and now there is name-calling. Considering that maybe you should conduct yourself in more respectful manner publicly. Noone wronged you here to deserve to be called "poisonous pit".

A word on incompetence claims: the less people know the more they *think* they know.

-------------------------

cosar | 2018-04-23 21:32:42 UTC | #21

What happened? Anything we can do to help?
I was looking forward for this branch to be merged. I'm not a contributor to this project because of time constrains, but so far the community was quite friendly. Maybe you can share with the rest of us what the issue is and we might be able to help somehow.

-------------------------

Eugene | 2018-04-24 12:02:32 UTC | #22

Just curious. Is there any TODO list related to this branch?

-------------------------

Sinoid | 2018-04-30 07:28:25 UTC | #23

@Eugene just a "does compile" check for RaspPi and Mobile. Otherwise it should be good. I did a few checks by faking a GLES target for checking some of the #ifdefs but those are at least a dozen commits behind.

The BillboardSet changes are ambiguous, I think they're safe to drop (they're technically safe to drop) as those changes pose problems for the Urho3D particle editor that doesn't give you access to the nodes/components of the preview for setting the switches involved in tripping the GPU expansion of particles.

I had expected it to take 2 - 4 weeks to get merged. It raises a lot questions, in places like the dubious AA handling in line drawing, etc.

**To be super-specific:** the final item pre-PR was just making sure at least a droid build worked. I fought with it for a few days but did surrender as I couldn't get CMake to do squat there

@rku unless I'm blind there's no name-calling up there (speaking of that I'd appreciate an admin giving me back my old name of 'Sinoid'). I went out of my way to point out that this is fairly advanced stuff and likely far outside of the capability of most.

*begin sarcasm - for your long-winded comment of existential nothing*

On the contrary, I want to know where you live because apparently, a person can live for free there with zero need to pay bills. Just doing zilly for fun. That, is name calling.

*end sarcasm*

I don't have a real beef with you, you flatly never listened to squat I said, so there really can't be a beef as you clearly had earplugs in the whole time. There was never a counter-voice to your extremism, so I opt for bail again rather than surrender - not going to do anything that helps splinter forks.

---

You basically have to use DX and **HAVE** to turn on the debug logging in the control panel if you so much as want to touch any of this. It's not faint of heart material, OpenGL has squat to help you through it - which makes it a big cluster-mess if RenderDoc fails to save your bacon - which it will fail.

You're probably completely unaware that DX requires perfect alignment of outputs to inputs and that semantics are generally meaningless aside from the VS input, you'll get to meet those woes the instant you touch GS/HS/DS. As I said, well outside of average capability.

-------------------------

