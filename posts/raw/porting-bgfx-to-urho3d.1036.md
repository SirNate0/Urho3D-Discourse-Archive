sabotage3d | 2017-01-02 01:04:58 UTC | #1

Hi ,
I am thinking of porting bgfx to Urho3D as an extension or replacement of the existing rendering engine. 
Is there currently any easy way of adapting third party rendering library in Urho3D, like passing geometry, lights, cameras ?
They have a long feature list that can even surpass Unreal Engine in some areas .

It as it has been used in a few mobile commercials games and they look quite good . 

[github.com/bkaradzic/bgfx](https://github.com/bkaradzic/bgfx)

[youtube.com/watch?v=viYQyuzNctE#t=13](https://www.youtube.com/watch?v=viYQyuzNctE#t=13)

[youtube.com/watch?v=PoAMDzuEJ3I](https://www.youtube.com/watch?v=PoAMDzuEJ3I)

-------------------------

thebluefish | 2017-01-02 01:04:58 UTC | #2

Look at how the existing Render subsystem is implemented. OGL, DX9, and DX11 all define their own Renderer subsystem that gets switched between at compile time. You could implement your bgfx renderer similarly.

Alternatively define your own bgfx subsystem, initialize the engine with no Renderer subsystem, and then wire everything appropriately.

Alternatively keep everything the same, but implement you bgfx subsystem that renders to a render texture. Then draw it similarly to the UI subsystem, on top of the existing Renderer, etc...

-------------------------

GoogleBot42 | 2017-01-02 01:04:58 UTC | #3

I can't believe I haven't heard of this before.  :confused:  It is very cool!  I would like to see this be ported to the engine.  If it is possible, I do wonder how it would perform in comparison to the subsystems already finished.

-------------------------

boberfly | 2017-01-02 01:04:59 UTC | #4

I debated whether or not to do this awhile ago. After the renderer refactor I don't think it is really worth doing. For one, the bgfx-specific submission-based renderer where it sorts everything for you using hash keys would be doubling up the work Urho3D already does when arranging and sorting batches so you'd disable it like you would when drawing GUIs with bgfx. Unless you replace all of Urho3D::Graphics and how it submits calls to how bgfx expects and not just make a bgfx toggle next to DX9/11/GL. You'd also need to make yet another set of shaders for it, albeit ones which would work in both GL and DX.

Bgfx has the option to render in another thread so that's something interesting to see if it would speed things up with Urho3D, but it might behave oddly with Urho3D's threaded culling, but I'm just speculating. Also the planned DX12/Vulkan backends that Urho could support 'for free' once bgfx gets patched.

Urho would probably benefit more from just adding a compute shader abstraction like bgfx has to make it on-par with bgfx imo.

Funny story, the Dogbyte game was once using Horde3D that used some of my GL ES 2.0 porting efforts to render it, before they changed to bgfx... :smiley:

-------------------------

cadaver | 2017-01-02 01:05:00 UTC | #5

I'm not sure if bgfx handles well the large amount of shader permutations that Urho generates. If I understand right, you pass an "ubershader" similar to Urho's shaders to its shader compiler, then it spits out the permutations as separate files. In Urho there may easily be thousands of permutations of a single shader, though most of them never get used, so it would rather need to be able to invoke the compiler at runtime on demand, or have the compiler built-in to the renderer. Also, it has a fixed drawcall limit per frame due to the drawcall sorting scheme. It was something quite high (32768?) but nevertheless it's something I'd personally feel uneasy about.

Other than that, it's your usual API agnostic low-level graphics solution, outside of the drawcall submission queue and the compute shader support the low-level operations are very similar to Urho's existing graphics subsystem.

-------------------------

sabotage3d | 2017-01-02 01:05:00 UTC | #6

I have feeling that it might get slower than the native Urho3D rendering subsystem which kind of kills it for me. Also I think feature-wise Urho3d is not that far away. For something in the future if they support more Rendering APIs it might make more sense. I wonder how the guys from Dogbyte balanced the graphics so well on mobile.

-------------------------

bkaradzic | 2017-01-02 01:05:00 UTC | #7

Hi guys, I noticed traffic to my GItHub project is coming from here and joined forum to clarify a few things.

Default bgfx limit is 64K, but it's configurable if you need more or less (if you want to save memory). Limits do exist on GPU, CPU, memory, etc. It's not like renderer without explicit limit are just unbound and can do whatever, more likely limit is there you just don't know what is it.

There is performance comparison with different renderers and platforms, see 17-drawstress table:
[github.com/bkaradzic/bgfx#17-drawstress](https://github.com/bkaradzic/bgfx#17-drawstress)

This test specifically stresses bgfx submission loop. There is num^3 cubes, updating their model matrix while trying to maintain 60Hz. You can try recreating similar example with Urho3D and comparing it with bgfx. Benefit of switching Urho3D to bgfx is that you have to stop worrying about renderer and focus on other things like user usability, editors, effects, etc.

-------------------------

boberfly | 2017-01-02 01:05:00 UTC | #8

Hi Branimir welcome to the forums! I'm that annoying guy who added the 'Add Vulkan Support' to bgfx's issue tracker... :slight_smile:

We do have an object count stress test but it's more or less mirroring the Ogre3D one:
[github.com/urho3d/Urho3D/tree/m ... bjectCount](https://github.com/urho3d/Urho3D/tree/master/Source/Samples/20_HugeObjectCount)

Maybe one that copies bgfx could be made to see the differences like you said.

Cheers

-------------------------

cadaver | 2017-01-02 01:05:00 UTC | #9

Welcome!

The object stress test in Urho tests also culling, light interactions, scene render queue management and automatic instancing, which the bgfx drawstress-test doesn't. To perform a more equal test one needs to use the Urho Graphics class directly for the low-level interface, something like this (not exactly same, but it performs a number of drawcalls in different positions using the same state. The setting of the material color and viewproj matrix are actually redundant, when the shaders are kept same.)

[code]
    Model* mod = GetSubsystem<ResourceCache>()->GetResource<Model>("Models/Box.mdl");
    if (mod)
    {
        ShaderVariation* noTextureVS = graphics_->GetShader(VS, "Basic");
        ShaderVariation* noTexturePS = graphics_->GetShader(PS, "Basic");

        int num = 200;

        for (int x = -num; x < num; ++x)
        {
            for (int y = -num; y < num; ++y)
            {
                Matrix3x4 pos(Vector3(x*0.007f, y*0.007f, 0.5f), Quaternion::IDENTITY, 0.005f);
                graphics_->SetShaders(noTextureVS, noTexturePS);
                graphics_->SetShaderParameter(VSP_VIEWPROJ, Matrix4::IDENTITY);
                graphics_->SetShaderParameter(PSP_MATDIFFCOLOR, Color::RED);
                graphics_->SetShaderParameter(VSP_MODEL, pos);
                graphics_->SetBlendMode(BLEND_REPLACE);
                graphics_->SetDepthTest(CMP_ALWAYS);
                graphics_->SetDepthWrite(false);
                graphics_->SetColorWrite(true);

                mod->GetGeometry(0, 0)->Draw(graphics_);
            }
        }
    }
[/code]

I tested both drawstress & this code snippet, both using D3D9, and the performance figures were nearly equal. Which is as I suspected, as in the end both bgfx & Urho Graphics class will be talking to the graphics API using a minimal amount of API calls. This leads me to believe that migrating to bgfx would not offer either significantly worse or significantly better performance.

-------------------------

rku | 2017-09-23 08:27:29 UTC | #10

With @cadaver resigning maybe this matter is worth revisiting? Even if bgfx does not offer immediate performance gains it still provides free support for new rendering APIs, some of which we will definitely not see ever implemented in Urho3D as it is now. bgfx port (or even full migration) could relieve some maintenance stress.

-------------------------

Eugene | 2017-09-23 08:34:37 UTC | #11

Maybe. I heard about some problems with bgfx, but I've never tried it.

-------------------------

rku | 2017-09-23 08:38:17 UTC | #12

Could you elaborate? @bkaradzic is very helpful  and they might just get addressed. Besides i would like to point out that i am willing to help too. As far as i am capable anyway.

-------------------------

cadaver | 2017-09-23 12:04:20 UTC | #13

My suggestion now is that you should have some kind of game plan how you're going to benefit from it, and how you're going to change the high-level rendering to accomodate. E.g. doing clustered forward lighting, using compute shaders? Otherwise it's just a lot of work, and it'll be hard to keep the existing featureset 100%.

Preferably you shouldn't be compiling new shaders during runtime at all (ie. know all used permutations beforehand), but that's kind of hard with the level of configurability the renderpath and materials / techniques offer.

However, I think you should be bold in taking Urho rendering to new directions, as if you ask enough users you will no doubt end up with an impossible featureset (e.g. function on low-end mobiles, keep all existing features..) At some point it may be better to just break compatibility majorly, if the benefits are clear enough.

-------------------------

bkaradzic | 2017-09-24 01:45:33 UTC | #14

There is already Urho3D to bgfx port going on here:
https://github.com/jamesmintram/Urho3D/tree/JM-NoopGraphics

[quote="Eugene, post:11, topic:1036, full:true"]
Maybe. I heard about some problems with bgfx, but I’ve never tried it.
[/quote]

Need more info... :)

[quote="cadaver, post:13, topic:1036"]
My suggestion now is that you should have some kind of game plan how you’re going to benefit from it, and how you’re going to change the high-level rendering to accomodate. E.g. doing clustered forward lighting, using compute shaders? Otherwise it’s just a lot of work, and it’ll be hard to keep the existing featureset 100%.
[/quote]

Benefits of porting to bgfx are not just about high-level features. There is benefit of having identical feature set while using common shader language so that adding new, and maintaining existing features is not difficult. Also by just switching to bgfx, Urho3D will get new rendering backends, and that part of maintenance will be offloaded elsewhere.

I actually recommend first straight port to achieve 1:1 feature set, as if bgfx is just another rendering backend (next to existing ones) in Urho3D. Once that's complete old rendering backends can be dropped, and all state tracking, sorting, and then in 2nd step other stuff that bgfx internally supports can be removed from higher level scene code in Urho3D. Once bgfx is fully integrated people should investigate about adding more advanced stuff.

The reason why I think it's not good idea to start port + add bunch of new features is that engine might end up in rump state, where port is not fully functional, but new features are not completely added either. So in that state might not be appealing to anyone.

Anyhow if anyone is interested to help with this port just let join effort in that repo above.

-------------------------

yushli1 | 2017-09-24 02:27:34 UTC | #15

Don't do that porting inside the main Urho3D repo. If ported, Urho3D is no longer Urho3D. If this port is desirable, please do so in other repo, any other repo.

-------------------------

bkaradzic | 2017-09-24 03:14:45 UTC | #16

[quote="yushli1, post:15, topic:1036, full:true"]
Don’t do that porting inside the main Urho3D repo. If ported, Urho3D is no longer Urho3D. If this port is desirable, please do so in other repo, any other repo.
[/quote]

That port is not in main repo, it's done by someone from AtomicEngine community for their purpose (their focus is more shipping games than building an engine). As for Urho3D, it's whatever Urho3D community wants. bgfx is intentionally designed as renderer-only in hope that not having other parts of engine will be more appealing for engine creators to use it. Idea was like people are using 3rdParty libs for physics, sound, navigation/AI, networking, windowing/input, etc. but there is nothing like that for rendering. From my point of view, Urho3D using bgfx or not, there is no change...

-------------------------

rku | 2017-09-24 06:54:16 UTC | #17

[quote="yushli1, post:15, topic:1036, full:true"]
Don’t do that porting inside the main Urho3D repo. If ported, Urho3D is no longer Urho3D. If this port is desirable, please do so in other repo, any other repo.
[/quote]

This is absurd and suggesting that is suggesting engine to stagnate because noone is going to write backend for dx12, noone is going to write backend for metal, noone is going to write backend for vulkan. Not to mention bgfx solving write-once shader problem..

-------------------------

weitjong | 2017-09-24 08:41:40 UTC | #18

IMHO, being done elsewhere first does not exclude us to pull the good bits in later, if the license permits it and if it turns out to be really that good where we may be decide to trade it off with Urho backward API compatibility. For one time we could be just the "recipient" of other people hard work and experiment. I have my doubt it will happen anytime soon though as it looks like the porting work has just began a few days ago.

-------------------------

yushli1 | 2017-09-24 09:34:08 UTC | #19

This is not absurd and this is not suggesting engine to stagnate. keep Urho3D what makes it is Urh3D, then add to it, not try to make it another one. If dx12 is to be supported, do so in Urho3D's style, If vulkan is to be supported, do so in Urho3D's style. Do not drag it to another structure with other design desicions. This kind of backend should be carried out in other repo. What in Urho3D's main repo, should be adapted to Urho3D first. Urho3D can bring over the good bits of course. But keep Urho3D what makes it Urho3D is essential.

-------------------------

yushli1 | 2017-09-24 09:40:55 UTC | #20

BTW, If you are so eager to help Urho3D, why not begin to port useful rendering features from Atomic Engine to urho3D engine, instead of arguing about porting to a completely different rendering backend?

-------------------------

Eugene | 2017-09-24 09:48:54 UTC | #21

> keep Urho3D what makes it is Urh3D

Why do you think that outsourcing physics, networking, navigation and scripting _is_ Urho way and outsourcing renderer is _not_ Urho way?

-------------------------

cadaver | 2017-09-24 18:07:52 UTC | #22

There are some parts of the rendering, like reusing the same shadow map over and over in between light accumulation passes, that will not map well to bgfx's views, or require a bit of ugly hackery. Since it incurs repeated rendertarget switches, it's probably not a good idea to do at all, and worth dropping. Also, since bgfx seems to have 256 view id limit, you cannot do "unlimited" lights that way anyway, though it's probably not realistic to have > 256 shadowed lights in a scene, it's just that the current Urho rendering allows you to do that (and tank your framerate)

-------------------------

Eugene | 2017-09-24 11:56:41 UTC | #23

[quote="cadaver, post:22, topic:1036"]
There are some parts of the rendering, like reusing the same shadow map over and over in between light accumulation passes, that will not map well to bgfx’s views
[/quote]

Thanks! I heard about exactly this, but didn't manage to recall.

-------------------------

yushli1 | 2017-09-24 13:22:02 UTC | #24

Because rendering is the core of a game engine. And the design and structure of it determines the characteristic of that engine.

-------------------------

Eugene | 2017-09-24 13:49:15 UTC | #25

[quote="yushli1, post:24, topic:1036"]
Because rendering is the core of a game engine.
[/quote]

Scene graph, editor and public API is the core of the engine.
Built-in shaders and assets is the basis of the engine appearance.
Renderer backend is neither first nor second. It's just an implementation detail that you never notice unless you are developer.

-------------------------

yushli1 | 2017-09-24 15:14:59 UTC | #26

A game engine is chosen by its user first by the quality of graphics it can render, or its first impression. then its performance, then its code style, then its structure and API usage. Not the other way around. In that sense, pulling the rendering techniques from other engine, and integrate it seamlessly with Urho3D is prefered than ,say, improving its public API. This is also the hard part that few people are willing or qualitified to do so to improve Urho3D right now.

-------------------------

dragonCASTjosh | 2017-09-25 09:48:13 UTC | #27

BGFX is simply a abstraction layer not an engine, it does not change Urhos feature set and it wouldn't be to difficult to port the current shaders over, the changes will only be the same as changing from DirectX to OpenGL at first, it just opens some doors to us such as having new rendering API's and hardware specific fixes that would require a dedicated team to keep on top of. Using it doesnt make Urho any less Urho.

-------------------------

weiyuemin | 2020-06-28 08:14:33 UTC | #28

[quote="bkaradzic, post:14, topic:1036"]
Urho3D to bgfx port
[/quote]

curious about the Urho3D to bgfx porting. jamesmintram's port seemed not complete

-------------------------

Eugene | 2020-06-29 08:11:44 UTC | #29

Time passed, and I changed my mind on the subject.

Porting Urho to bgfx is not really viable option -- among all other things, it inflicts major performance penalty on batching. I don't remember exact numbers, but HugeObjectCount was _times_ slower.

Abstraction level of bgfx is so high so it simply doesn't allow the amount of control that Urho requires.
Sure, you can build _new_ engine around bgfx so it doesn't suffer from limitations _too much_. But proting Urho? I don't believe this is possible.

-------------------------

weiyuemin | 2020-06-30 12:59:56 UTC | #30

do you have a branch that work on the porting, maybe I can continue work on it? (as you said HugeObjectCount was times slower, I guess you had a branch that tries the porting..)

-------------------------

Eugene | 2020-06-30 13:13:54 UTC | #31

Here’s the branch I tested and even fixed sometimes. I don’t remember exact version or configuration I tested, tho.
https://github.com/boberfly/Urho3D/tree/feature/bgfx

-------------------------

weiyuemin | 2020-06-30 15:15:03 UTC | #32

just tried this branch, found the sample HugeObjectCount is about 20% slower than the original Urho at cc25bef60ec57fc409dae1b3f07539e73e18aad3 when both using D3D11 renderer.

So maybe there is some other problems in this branch that leads the slowness?

when using BGFX renderer, compilation failed. I'll continue try it tomorrow.

-------------------------

Eugene | 2020-06-30 15:22:54 UTC | #33

I might have tested it with disabled instancing back then.
Can you try it this way as well?

-------------------------

weiyuemin | 2020-07-01 03:37:14 UTC | #34

my test results yesterday is not that exact. Actually no 20% slower problem.

Today I checkout an unmodified Urho at cc25bef60ec57fc409dae1b3f07539e73e18aad3 and tested HugeObjectCount again on my i7 9700k + rtx 2070s (release build, SPACE pressd to rotate these cubes after starting the sample):

with instance d3d11: fps26
no instance d3d11:  fps23
with instance gl: fps25
no instance gl:  fps21

and boberfly's feature/bgfx branch:
with instance d3d11: fps24-25
no instance d3d11: fps22

fps almost the same. but a little difference: on boberfly's feature/bgfx, when f2 pressed only a little text is displayed. when using original Urho, when f2 pressed there are many lines of text displayed (DEBUGHUD_SHOW_ALL)

on my modified Urho: (I think main difference is I modified debughud to only show fps)
with instance gl: fps29
no instance gl: fps27

-------------------------

Eugene | 2020-07-01 06:20:18 UTC | #35

When you make BGFX compile, can you check it too?
I remember huge perf difference between non-instanced BGFX and non-instanced... pretty much everything.

-------------------------

rbnpontes | 2020-07-02 02:57:38 UTC | #36

Please continue this great job, I think there will be a great contribution to the community

-------------------------

weiyuemin | 2020-07-02 10:00:37 UTC | #37

I make bgfx renderer compiled by commenting out all URHO3D_D3D11 like things in cmake files. (otherwise URHO3D_D3D11 and URHO3D_BGFX will both be defined and leads to compile error)

but it can't run correctly.

My cmake arguments: -DURHO3D_BGFX=1 -DURHO3D_SAMPLES=1 -DURHO3D_SYSTEMUI=1
(is there anything wrong with these arguments?)

will continue try this when i'm free

-------------------------

weiyuemin | 2020-07-03 12:40:39 UTC | #38

bgfx renderer result: fps 15.5  (instance is default off)

compared to d3d11, indeed slower.

-------------------------

weiyuemin | 2020-07-03 13:29:54 UTC | #39

when using d3d11 renderer, there's difference if you press or not press space (to rotate the cubes):

not rotate the cubes: fps 37
rotate the cubes: fps22    (both non-instance)

when using bgfx renderer, there's no difference if you press or not press space (to rotate the cubes).
both fps 15.5

seemed some dirty mechanism broken on bgfx renderer

-------------------------

Eugene | 2020-07-03 14:10:26 UTC | #40

Batching performance penalty is not caused by any bug (as far as my understanding goes), it is just how BGFX is implemented. It’s not broken, it’s deliberately made to be slower for sake of implementation simplicity.

-------------------------

brokensoul | 2020-11-19 11:12:08 UTC | #41

What you guys think about Magnum(https://github.com/mosra/magnum) or Diligent (https://github.com/DiligentGraphics/DiligentEngine) ? Instead of bgfx

-------------------------

Eugene | 2020-11-19 11:51:03 UTC | #42

They don’t have feature parity with current Urho renderer, so I don’t think it will ever get to main repo even if someone implemented it

-------------------------

dertom | 2020-11-19 19:17:36 UTC | #43

To name another candidate: 
https://github.com/ConfettiFX/The-Forge

-------------------------

Dave82 | 2020-11-20 13:08:07 UTC | #44

Wow this one looks really interesting and most feature rich so far. Did anyone tried it yet  ?

-------------------------

SirNate0 | 2020-11-20 15:51:07 UTC | #45

It certainly seems interesting, though I don't think I'll like their code style:
https://github.com/ConfettiFX/The-Forge/issues/177

-------------------------

1vanK | 2020-11-20 23:16:22 UTC | #46

13 posts were split to a new topic: [C vs c++ (again)](/t/c-vs-c-again/6555)

-------------------------

JSandusky | 2020-11-21 03:26:07 UTC | #47

> It certainly seems interesting, though I don’t think I’ll like their code style:

Meh, it grows on you.

[quote="Dave82, post:44, topic:1036, full:true"]
Wow this one looks really interesting and most feature rich so far. Did anyone tried it yet ?
[/quote]

I use it currently. It works and it's not demonstrably slower than the equivalent raw API code, which doesn't sound like much but that is a lot to ask for. I don't care for the shader-tool suggested and just use shader-conductor.

-------------------------

JSandusky | 2020-11-22 02:47:03 UTC | #48

Should add that I would never consider ***porting*** Urho3D to The-Forge. If someone were to try such a thing it'd make more sense to be a 'Graphics2' option that excluded legacy 'Graphics' and UI, becoming a project choice and doesn't discard legacy targets or mess with anyone else too much.

Common functionality would get moved out into mostly purely calculative functions (OcclusionBuffer works anywhere, skinning matrix math doesn't change, etc) and the new stuff be render-graph based with a much more raw API direct to The-Forge (you still have to handle transitions/barriers in The-Forge). 

Using that clean split makes it more sensible to be hugging modern methods like indirect-draws, GPU cluster/triangle culling, splitting large batch-pumps into jobs for threaded cmd-lists, compute skinning, and opens up async rendering without creating a gigantic mess in Graphics.

Sounds like a lot of work, but it's not that bad. Compute skinning greatly simplifies shader and rendering complexity by effectively reducing everything to "static-draws" after the prep-work has been done. UI is the headache, to interop-layer or to not and do something else is the question.

Maybe 140hrs to get to a "proof" stage without UI, assuming graphics was the only beef one had. (I dropped Urho for custom because of physics+audio+state more so than what I could do with graphics, SDL not handling windows spatial is a serious deal breaker).

-------------------------

WangKai | 2022-10-23 12:35:16 UTC | #49

Any progress on this direction?
This port will allow Urho3D running on more graphics API, e.g. Vulkan, Metal.
Bgfx has been improving.

-------------------------

Eugene | 2022-10-27 10:20:03 UTC | #50

AFAIK there was an attempt, but bgfx API was too limited at the time to offer comparable performance.

-------------------------

WangKai | 2022-10-28 02:03:43 UTC | #51

It's a good path to me, as long as the third party library is good enough, no matter what it is. It's better than dying.

-------------------------

Eugene | 2022-10-28 09:41:31 UTC | #52

[quote="WangKai, post:51, topic:1036"]
It’s better than dying.
[/quote]
To be honest, Urho is dying *not* because of missing Vulkan API.
bgfx not gonna help here.

-------------------------

1vanK | 2022-10-29 22:06:06 UTC | #53

Let's be honest, nobody will ever use Urho3D to make AAA games. The niche of our engine is indie games. Therefore, an advanced graphics engine is not needed here. An indi developer simply won't have the money to create quality content with PBR textures, normal maps, hair physics and other features of expensive games. Our movement will move towards more 2D support. I have some drafts, but for now I'm busy restructuring the engine. Unfortunately it took longer than I thought. From this point of view, Urho3D is more alive than, for example, rbfx, which moving in the wrong direction.

-------------------------

hunkalloc | 2022-10-31 19:12:45 UTC | #54

> The niche of our engine is indie games. Therefore, an advanced graphics engine is not needed here.

This depends heavily on what you consider "advanced". There are a lot of features on a graphics engine that help indies be more productive and be more efficient. Take imposters, for example, or lightmapping. Or terrain texture blending. 

> An indi developer simply won’t have the money to create quality content with PBR textures, normal maps, hair physics and other features of expensive games

That's simply not true. I'm an indie artist and I can afford to create quality content because that is my jam. A Substance subscription is cheap, and there are plenty of open-source tools out there capable of producing PBR content. In fact, most of them do so because it is the industry standard. Not supporting PBR alienates a huge part of the indie developer userbase.

> From this point of view, Urho3D is more alive than, for example, rbfx, which moving in the wrong direction.
rbfx is adding features that makes developers, regardless of their background, more productive. I can move my assets into the engine more easily. The built-in editor is a god send for an artist like me. And lightmapping saves me from having to deal with a complicated Blender-based workflow. 

Urho is supposed to be a general purpose, complete, game engine. I don't think all perspectives are being considered here.

-------------------------

hunkalloc | 2022-10-31 19:18:16 UTC | #55

Just look at the Most Popular add-ons for Unity on their marketplace. It's all stuff created to make indie devs more productive with less resources: https://assetstore.unity.com/?category=tools&orderBy=1

Terrain and sky generators, so we can prototype and get worlds faster. IK, so we don't have to animate every single situation out there. An improved inspector, to make debugging easier and iterations faster. Lightmapping, again. A*/Basic AI. 

Those are tools have help indie be competitive with AAA. Just because features are "advanced", doesn't mean that they are not useful. 16xMSAA and realtime global GI? Yeah, maybe not useful, but I think not all perspectives are being considered here. Productivity is key.

-------------------------

1vanK | 2022-10-31 19:22:22 UTC | #56

I have other things to do than engage in useless arguments. If you are such a cool artist, then help the project by creating a beautiful demo to attract people.

-------------------------

amerkoleci | 2022-10-31 20:12:41 UTC | #57

I have been following all changes you've made and make 0 sense to me, adding alias, switching from uint to int, at what scope? There used to be a strong community behind urho but I would never use Urho at current state, too sad authors like @cadaver totally ignored all commits you did by totally broking urho.

Don't take me wrong, is not hate speech but really.

Seriously, reconsider your priorities and stop thinking about which direction is rbfx going.

-------------------------

1vanK | 2022-10-31 20:13:15 UTC | #58

Remind me how much money you paid me to do what you want and not what I want?

-------------------------

amerkoleci | 2022-10-31 20:17:07 UTC | #59

What kind of answer is this? By 10 years old kid or what? 

You're changing a years of open source effort done by other people without having respect for their time/effort.
 
Grew up dude!

-------------------------

1vanK | 2022-10-31 20:17:50 UTC | #60

Do you have some kind of fetish about children? <https://discourse.urho3d.io/t/moving-urho3d-github-io-to-urho3d-io/6861/19>

-------------------------

1vanK | 2022-10-31 20:18:49 UTC | #61

I don't really respect you. Because your contribution to the engine is zero, but why did you get that your opinion matters.

-------------------------

amerkoleci | 2022-10-31 20:25:02 UTC | #62

Lol, very mature from you.

Keep up this way!

-------------------------

rku | 2022-11-03 07:35:20 UTC | #63

[quote="1vanK, post:53, topic:1036"]
From this point of view, Urho3D is more alive than, for example, rbfx, which moving in the wrong direction.
[/quote]

You are confident. It is a race then.

-------------------------

1vanK | 2022-11-03 09:33:27 UTC | #64

![1_dx9|566x361](upload://pPxAQrCL9ICPkEAWsuJ3t3nyEtZ.png)

-------------------------

niansa | 2022-11-03 11:45:57 UTC | #65

Where is cubemapping, a half-decent editor and all? And where is the community??

@1vanK Seriously, did you ever contribute to the engine? You only ever degraded it with stupid commits. Signed iterators and shit **can** cause serious issues.
All you are doing is abusing your powers. And censoring opinions like these by suspending forum accounts.
I and many others here kindly ask you to restore the engine into a workable state and step back from your position. The engine went downhill ever since you started "contributing", after the last engine release.

-------------------------

1vanK | 2022-11-03 12:59:14 UTC | #66

I don't see anyone else wanting to do the engine. If you don't like my changes, I have a great option for you: https://github.com/urho3d/Urho3D/releases/tag/1.8

-------------------------

1vanK | 2022-11-03 13:01:43 UTC | #67

[quote="niansa, post:65, topic:1036"]
Signed iterators and shit **can** cause serious issues.
[/quote]

Where were you when this option was offered?

-------------------------

1vanK | 2022-11-03 13:30:40 UTC | #68

[quote="niansa, post:65, topic:1036"]
Where is cubemapping, a half-decent editor and all?
[/quote]

Why do you think someone else should do it? Start doing, come back with the result.

-------------------------

dragonCASTjosh | 2022-11-05 08:52:39 UTC | #69

Iv been quit on this forum and engine for a long time since my PBR changes. And its attitudes yours that pushed me away. You say you dont see anyone making meaningful changes but then whever a good idea is purposed its shot down. In my case i was willing to spend the time modernizing the rendering in a way that doesnt effect indie devs at all but it was all rejected in favor of doing backwards changes that reduce the quality of the engine. If you want people to work on the engine you need to support them and incubate the ideas. 
Things got so bad for me here that i just went and built my own engine for my projects because i didnt want to deal with stupid arguments. Its a shame Urho could been in godots position if there was a respectful and forward-looking community was allowed to exist

-------------------------

1vanK | 2022-11-05 11:11:39 UTC | #70

Why should I support or incubate someone. I'm not a nursery nanny. We have a lot of code in the engine that was added in a half-baked state and then abandoned by the developer. And someone else needs to  maintenance him (IK for example). I'm not saying that my code is perfect, but at least I feel responsible for my code. It is unlikely that someone will be able to maintenance my binding generator. But why should I maintain all other code? At the moment I don't even know if our engine compiles on MacOS because I don't use that system. I have written about this several times. If you don't need it, then why should I need it?

-------------------------

1vanK | 2022-11-05 11:19:56 UTC | #71

[quote="dragonCASTjosh, post:69, topic:1036"]
it was all rejected in favor of doing backwards changes that reduce the quality of the engine
[/quote]

I've never been a fan of backwards compatibility. A game engine is not an ordinary library. On the contrary, the engine often changes for a particular game. Therefore, it is not a problem to have a separate version of the engine for each of your games.

-------------------------

1vanK | 2022-11-05 12:46:30 UTC | #72

To be honest, I tried to understand from your messages who exactly rejected your proposals and which ones? Could you clarify?

Latest posts:<https://discourse.urho3d.io/t/stealing-panda3ds-render-pipeline/4778/30?u=1vank> <https://discourse.urho3d.io/t/stealing-panda3ds-render-pipeline/4778/36?u=1vank>

-------------------------

1vanK | 2022-11-05 13:33:19 UTC | #73

[quote="rku, post:10, topic:1036, full:true"]
With @cadaver resigning maybe this matter is worth revisiting? Even if bgfx does not offer immediate performance gains it still provides free support for new rendering APIs, some of which we will definitely not see ever implemented in Urho3D as it is now. bgfx port (or even full migration) could relieve some maintenance stress.
[/quote]

[quote="rku, post:17, topic:1036"]
This is absurd and suggesting that is suggesting engine to stagnate because noone is going to write backend for dx12, noone is going to write backend for metal, noone is going to write backend for vulkan. Not to mention bgfx solving write-once shader problem…
[/quote]

Sounds reasonable, why is brgfx not integrated to rbfx after 5+ years?

-------------------------

SirNate0 | 2022-11-05 13:53:09 UTC | #74

[quote="1vanK, post:71, topic:1036"]
On the contrary, the engine often changes for a particular game. Therefore, it is not a problem to have a separate version of the engine for each of your games.
[/quote]

You may like this, but I do not. I would rather have only one version of the engine rather than half a dozen. Or at least have changes that break the code using engine be infrequent and quick to fix. For the most part I think Urho has done this well in the past. I'm less sure of now with the sweeping changes to integer types and scripting that have been happening - maybe it's still fine, but it looks like too much for me to be willing to even try at the moment. At some point I'll get to it, but probably after I finish my current project in returning to one of my older ones.

---

[quote="1vanK, post:67, topic:1036, full:true"]
[quote="niansa, post:65, topic:1036"]
Signed iterators ... **can** cause serious issues.
[/quote]

Where were you when this option was offered?
[/quote]

Speaking for me, I was on the forum. I think I only saw the stuff on GitHub about it a few weeks late, after the discussion and work for it had largely been finished. I don't check GitHub as often as the forum (once a month vs once a day), and wrongly expected large changes like that would be discussed in the developer talk section. I don't entirely mind the change, especially if we put it into Urho 2.0 rather than 1.9. I'm less sure of how I feel about all the typedefs (i32, etc.) but I can see some of the advantages as well, and they don't require any changes to my code.

-------------------------

1vanK | 2022-11-05 15:05:36 UTC | #75

[quote="SirNate0, post:74, topic:1036"]
You may like this, but I do not. I would rather have only one version of the engine rather than half a dozen.
[/quote]

It's abstract. None of the engines can provide all the functionality you need for your particular game. For example, I added an additional window to the editor for quick insertion of objects I needed when creating level. Should it be in the engine repository? Or I needed to significantly change the button class to get the effect of a smooth color change, since at the moment an object cannot have several event handlers for same event at the same time. Should I push this to the repository? 

After all, if there have been changes in the repository that break backwards compatibility, then you don't have to upgrade. You can continue to develop the current game on the old engine, and start a new project on the latest version of the engine.

-------------------------

rku | 2022-11-05 15:26:54 UTC | #76

You want to go down the route of measuring our.. features? rbfx has a totally new renderer and we plan on switching to Diligent for a common graphics backend. Should i list other features rbfx had and urho never will?

-------------------------

1vanK | 2022-11-05 15:48:59 UTC | #77

Was it the answer to my question?

-------------------------

1vanK | 2022-11-05 15:54:24 UTC | #78

Maybe it was like being rude. It's just that there are those who want to integrate bgfx into the engine, but you probably studied this issue and sewed on the conclusion that this is a bad idea. I would like to know about this reason.

-------------------------

1vanK | 2022-11-05 16:01:45 UTC | #79

[quote="rku, post:76, topic:1036"]
You want to go down the route of measuring our… features?
[/quote]

I'm afraid you will lose. For example, we have the console, the scripting language, the editor.

-------------------------

Eugene | 2022-11-05 17:07:11 UTC | #80

[quote="1vanK, post:73, topic:1036"]
Sounds reasonable, why is brgfx not integrated to rbfx after 5+ years?
[/quote]
The serious answer is that bgfx was tried and found lacking (I don't have Urho bgfx branch link, sorry).
It's just way too limited. It may be good enough if you build entire new renderer/engine around it, but it's too restricting for Urho3D. I think that sokol, nvrhi, nri, Diligent or TheForge offer much better API for migrating existing engine, than bgfx.

-------------------------

rku | 2022-11-05 17:19:30 UTC | #81

https://github.com/boberfly/urho3d/tree/feature/bgfx

-------------------------

1vanK | 2022-11-06 00:42:31 UTC | #82

![1_dx9|690x102](upload://fl18mrKFsuQaag9tJcS7R2v9XQT.png)

xD

-------------------------

SoNewBee | 2022-11-06 12:46:56 UTC | #83

really？
finally we add bgfx support？🤩

-------------------------

SoNewBee | 2022-11-06 12:48:20 UTC | #84

hahahaha
that's really funny

-------------------------

SoNewBee | 2022-11-07 01:10:53 UTC | #85

So how about we select Diligent？

-------------------------

George1 | 2022-11-07 16:27:55 UTC | #86

Too many branches, resulting in not many users.  
It is better to stick to 1 branch and accept all the code changes and make it version 2 :).
Let people manage their own changes.

It will make the engine more lively, but coding quality may go down :).

-------------------------

1vanK | 2022-11-07 18:42:36 UTC | #87

[quote="George1, post:86, topic:1036"]
Let people manage their own changes.
[/quote]

Nobody wants to do anything <https://github.com/Urho3D-CE/Urho3D>

-------------------------

George1 | 2022-11-08 08:43:44 UTC | #88

Thanks, I think people shouldn't complain then.  It's already there for contribution.

-------------------------

rku | 2022-11-08 08:55:26 UTC | #89

Because:
- It is hidden
- It is a bad idea
- @George1 has no idea what he is talking about

-------------------------

1vanK | 2022-11-08 08:57:44 UTC | #90

It's not hidden <https://discourse.urho3d.io/t/urho3d-community-edition/6513>

-------------------------

George1 | 2022-11-08 09:16:46 UTC | #91

You can import your whole branch in there and manage it?  This way you don't have issue with quality of code.

But it needs advertisement on the main page.

-------------------------

rku | 2022-11-08 09:53:44 UTC | #92

Of course it is hidden. It does not belong to Urho3D organization on github and is in no way involved in official workflow of contributions. As far as everyone is concerned it is just a sandbox of some third party. Even if a contributor knows of that project and it's purpose - why would they waste their time contributing their code into junkyard instead of main project? Only ones contributing to CE would be ones who are unable to write good-enough code to be accepted to the main repo. Although bar seems to go down enough for that to no longer be a limitation.

-------------------------

1vanK | 2022-11-08 10:56:14 UTC | #93

[quote="rku, post:92, topic:1036"]
It does not belong to Urho3D organization on github
[/quote]

There is a technical reason for this, it is not possible to fork a repository to the same organization.

[quote="rku, post:92, topic:1036"]
Even if a contributor knows of that project and it’s purpose - why would they waste their time contributing their code into junkyard instead of main project? Only ones contributing to CE would be ones who are unable to write good-enough code to be accepted to the main repo. Although bar seems to go down enough for that to no longer be a limitation.
[/quote]

I first thought about rbfx.

-------------------------

