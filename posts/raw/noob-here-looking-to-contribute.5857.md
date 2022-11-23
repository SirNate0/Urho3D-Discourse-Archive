shiv | 2020-02-01 08:03:50 UTC | #1

I recently start fiddling with Urho3D looking in into its code. I would like to contribute something useful in Urho3D specially in Graphics. What I believe, Urho3D does not have Vulkan/Metal support and I think it would be good opportunity for me to learn and contribute here. Although I had found on forum that there is support available for angle-->vulkan-->moltenvk, which I guess would be performance killer. 
What is your thought on this, or what are other items you can suggest?

-------------------------

rku | 2020-02-01 09:38:01 UTC | #2

These are complex topics that require lots of experience. Such first task would definitely be overwhelming and demotivating. Start small. Walk before you fly.

-------------------------

Modanung | 2020-02-01 12:58:12 UTC | #3

The issues on GitHub might provide some inspiration for things to work on:
https://github.com/urho3d/Urho3D/issues

Or maybe you could run by some existing [pull requests](https://github.com/urho3d/Urho3D/pulls)?

What experience do you have with graphics pipelines?

-------------------------

johnnycable | 2020-02-01 16:19:48 UTC | #4

[quote="shiv, post:1, topic:5857"]
angle–>vulkan–>moltenvk
[/quote]

thanks to @kakashidinho and @elix22  the port works fine. Surprising, it is quite fast.
Hence, the only possible improvement would be a direct, unencumbered Metal port.
But that would require a mastership in shading, beyond in-deep Urho3d knowledge...

Just to gain, then, some relative feature beyond opengles2... it's a lot of work for a couple of systems, ios and mac, whose games comes, for the former, mainly in 2d format, and, for the latter, mainly in poor shape, being mac os the worst video game platform you can find.

And, of course, you need to have a Mac...

-------------------------

shiv | 2020-02-02 05:26:34 UTC | #5

You are right its complex and I am also new to Urho3D. So I am learning it by going through available samples first later will focus on Vulkan port.

-------------------------

shiv | 2020-02-02 05:28:52 UTC | #6

Ok. So it seems metal port won't be that useful. So I guess Vulkan port would be more useful as its available on Windows, Android and Linux platforms.

-------------------------

kakashidinho | 2020-02-05 13:35:29 UTC | #7

If you want to add vulkan/metal renderer I think the whole rendering subsystem code needs to be refactored to incorporate “manually batching commands in a command buffer” style of vulkan/metal. The current subsystem of urho3d uses immediate style of dx11 and opengl.
Implementing vulkan in such a way that it adapts to existing immediate style will defeat the performance advantages of vulkan. It might be even slower than dx/gl renderer.
I might be wrong thought. That’s being said, I am also planning to add metal renderer to urho3d.

-------------------------

shiv | 2020-02-06 02:51:07 UTC | #8

Great to hear that you are planning to add metal renderer. You may be right about performance but  my first aim is to have a working vulkan sample with Urho3d, later will look at performance and refactoring, meanwhile if you have a plan idea or design I would like to have a look at that so we can align these two efforts.

-------------------------

kakashidinho | 2020-02-05 16:18:52 UTC | #9

Actually, I don't have any concrete idea yet. Currently I'm just looking at the existing renderers & shaders code to see what is the most feasible & elegant way to add metal. You are right that initially the performance might not be a concern yet, so direct vulkan implementation of Graphics subsystem could be the first step.
anw, the metal renderer addition might not be a trivial task after all. The existing HLSL & GLSL shader code are huge and there are many ifdef macros lurking around.
Nevertheless, adding metal/vulkan and refactoring could make the graphics subsystem more modern and open doors for more modern rendering technique to urho3d.

-------------------------

elix22 | 2020-02-05 18:26:23 UTC | #10

Just my 2 cents 
@kakashidinho 
Your current Angle-Metal implementation works great , 
All samples work perfectly well on all the devices I tested (except the **42_PBRMaterials**, which is understandable )  
It even outperformed vanilla GLES2 on some devices ,

https://discourse.urho3d.io/t/metal-moltenvk-support-for-ios-an-mac-devices/4845/58  

I am not trying to discourage you :)
As you said writing a pure Vulkan & Metal solution for Urho3D  would be a huge effort, I am sure you have the knowledge to tackle it however it will require an additional substantial amount of people with vast knowledge on this topic  which I am afraid are currently not part of this community .

-------------------------

kakashidinho | 2020-02-06 01:47:16 UTC | #11

I'm just saying a possibility. It might not happen or not very soon. I concur that the addition of metal could be huge and tedious change. Not to mention it could just be a close replicate of what Angle-metal has done initially.
Actually, I'm thinking of adding Forward+ rendering mode to Urho3d (well it might not be important for some, but could be a fun thing to do). But it requires compute shader. Angle-metal will not support compute at current stage. Nevertheless, I think i will start with dx11 and opengl compute shader addition to urho3d first. Though opengl on mac doesn't have compute shader capability.
The alternative way to add compute shader to mac is using angle-metal and and adding compute shader to it in a non-OpenGL-specification conformant way. I'm not sure it is an ugly design or not.

-------------------------

Sinoid | 2020-02-06 02:06:54 UTC | #12

I strongly recommend against poking at adding a Vulkan backend unless you've implemented several before.

Vulkan makes a lot of restrictions on what you can do while a render-pass is in-flight which won't go well for the way Urho3D handles the RenderPaths.

I use a similar system in my own renderer and it required an additional `stage` abstraction in order to force restraints regarding rather basic things like clearing buffers and there's tons of vkCommandBuffer queuing going on before they finally get submitted.

All despite using V-EZ. With raw Vulkan it would've been so much much worse.

https://gist.github.com/JSandusky/190cf1bd561e36ae9c41004414ea9563

The GLSL shaders in Urho3D aren't written with Vulkan in mind either. You'll have to rewrite them. If your shaders run in GL3.3 then they definitely don't run in Vulkan. Glorious set-space hell.

---

A reasonable (but still bonkers) contribution would be setting up the build scripts (or even an external project) to build the tools necessary to cross-compile HLSL -> GLSL / ESSL / Metal (maybe ShaderConductor, maybe something else). That's very viable and although still a lot of work you could start seeing the results fairly quickly (in days possibly) even though the task as a whole is very long (weeks to months).

If you aren't focused on Graphics then there's tons of things you could look at. Even alternative backends could be worthwhile like an FMODStudio backend choice for Audio. AMD's new FemFX could be interesting too.

-------------------------

shiv | 2020-02-06 03:20:45 UTC | #13

[quote="Sinoid, post:12, topic:5857"]
I strongly recommend against poking at adding a Vulkan backend unless you’ve implemented several before.
[/quote]

I understand your concern, but isn't it a chicken and egg problem? Before having worked on several one has to begin first.
I had seen other implementation where CommanBuffer like abstraction are in use for GL and DX backends as well, but before making any such decision I want to have one sample working with vulkan first. Possibly it may need a re-write to fit everything to gather but lets consider it later.

[quote="Sinoid, post:12, topic:5857"]
The GLSL shaders in Urho3D aren’t written with Vulkan in mind either.
[/quote]

So, I guess there is an elegant solution already exist and I am familiar with. Angle shader translator works fairly well to translate shader source from one version to another and one language to another.

[quote="Sinoid, post:12, topic:5857"]
If you aren’t focused on Graphics then there
[/quote]

I had several years of experience in graphics but noob to Urho3d and want to utilize that, so I will focus on graphics only for now.

-------------------------

Sinoid | 2020-02-06 03:44:31 UTC | #14

@shiv a better way for me to put is that I suspect that "*if you had to ask then you can't*". Most that could wouldn't bother asking, if you're not one of them then go ahead.

> So, I guess there is an elegant solution already exist and I am familiar with. Angle shader translator works fairly well to translate shader source from one version to another and one language to another.

No, Angle is not good. It's ESSL -> others. Can you even build it on Windows without Cygwin? Google loves Cygwin and it's not an acceptable dependency. Ignoring that ESSL is a joke language targeting platforms few can actually afford to target beyond toy projects.

MS ShaderConductor is a much better base. I know for a fact that it works as I use it to compile HLSL -> ESSL for GLES3, GLSL for GL3.3, GLSL for 4.3, and SPIR-V for Vulkan.

-------------------------

Sinoid | 2020-02-06 03:49:15 UTC | #15

[quote="shiv, post:13, topic:5857"]
I understand your concern, but isn’t it a chicken and egg problem? Before having worked on several one has to begin first.
[/quote]


Yes, but you should do several isolated Vulkan renderer's first. The code I github-gist'ed was my 5th Vulkan renderer and it is still freaking terrible despite using V-EZ.

There's no good in having new blood nuke itself.

-------------------------

shiv | 2020-02-06 07:32:05 UTC | #16

[quote="Sinoid, post:14, topic:5857"]
“ *if you had to ask then you can’t* ”.
[/quote]

I don't agree but it's ok to assume that.

[quote="Sinoid, post:14, topic:5857"]
No, Angle is not good. It’s ESSL -> others. Can you even build it on Windows without Cygwin? Google loves Cygwin and it’s not an acceptable dependency. Ignoring that ESSL is a joke language targeting platforms few can actually afford to target beyond toy projects.
[/quote]
I was talking about "ANGLE's Shader translator" only (which is one module in ANGLE), which is very powerful tool to translate shaders across multiple languages and versions. It is being used as shader validator/translator in chrome/firefox and other popularly used software. Also, ANGLE is no more a toy, its being used by QT, chrome, Firefox (Webgl on most of Windows is powered by it) and list may go on. And yes of course  you can build ANGLE without cygwin. MS ShaderConductor might be good option too btw it's new kid in town.

-------------------------

Modanung | 2020-02-06 11:30:30 UTC | #17

7 posts were split to a new topic: [Social hygienics](/t/social-hygienics/5876)

-------------------------

kakashidinho | 2020-02-06 08:21:40 UTC | #20

angle can be built on windows without cygwin. I contributed to angle project before. I mostly worked on metal backend implementation and used to test the vulkan backend on windows as reference but not much, so the windows situations might be changed from time to time that I'm not aware of.

Regarding the offline cross-compiler solution. The problem with urho3d shaders is that they contain too many #ifdef. So one glsl/hlsl shader code would be translated into multiple variations in spirv depending on preprocessor definitions (doesn't matter what cross-compiler used). I think the tedious part is knowing all needed variations beforehand in order to generate them.
If the vulkan renderer was to be implemented, a runtime hlsl-spirv translator could be an easier and less tedious choice. Since all needed variations will be known at runtime.

Anw, these are just my thoughts. You may have a better idea. Metal renderer (if it would ever be implemented) could benefit from an offline shader converter also, to reduce runtime shader loading/converting.

-------------------------

elix22 | 2020-02-06 12:52:17 UTC | #21

Right , Angle compiles fine on Windows without cygwin .
One can always try my Urho3D-Angle-Vulkan implementation on Windows 
**git clone -b angle-vulkan https://github.com/elix22/Urho3D.git**
**cmake_vs2017_vulkan.bat - will create an Visual Studio project using Angle on top of a  Vulkan backend**

-------------------------

bvanevery | 2020-02-21 02:42:48 UTC | #22

[quote="shiv, post:1, topic:5857"]
What I believe, Urho3D does not have Vulkan/Metal support and I think it would be good opportunity for me to learn and contribute here.
[/quote]

Do you do Windows?  If so, you could do DX12 instead.  Vulkan will never matter to Windows, there's no argument for it.  Whether you wished to work on DX12, Vulkan, or Metal, any of them will be "big heavy change" to Urho3D's method of operation.  Any solution would ultimately be common to all 3.  Windows cares about DX12.  Apple cares about Metal.  Only Linux cares about Vulkan, there's no other motive.  Well honestly I don't know what Android cares about.

Anyways, platform war.  You didn't specify one.  You don't have to solve all of them or engage in *perceived* portability.  Nobody cares about Vulkan except platforms where it will actually be used.  So if you happen to like Windows more than I would guess from your 1st post, thought I'd sanity check this.

What you can accomplish, is up to your skill.  *Big* project to do any of these.  Do 1.  Let someone else do others, *if* you even get so far as to do 1.

-------------------------

shiv | 2020-02-21 05:50:17 UTC | #23

Graphics vendors are investing in Vulkan so there is quite good support available on Windows. It could go like Opengl way, as in early years Opengl support was bad and broken on windows but now a days it's better. But yes, Microsoft does not intend to support Vulkan for now!

My aim is to write rendering layer such that it could be possible to implement multiple rendering backends with most of code re-use. So, I guess I have to invest time learning d3d12 too to take right design decisions. Indeed it's big project and as of now I don't even know I would be able to finish it or not! But I already took first step by diving into Urho3d's current rendering code.

-------------------------

bvanevery | 2020-02-21 09:09:26 UTC | #24

One thing the OpenGL open source crowd never really understood about Windows, is that deployment of drivers was everything on Windows.  Those cheesy Intel machines with bad OpenGL drivers, but quite passable DX10/11 drivers, were around for a *long time*.  And consumers don't just up and fix their drivers like some kind of Linux expert.  So you have real problems that due to Microsoft's strong arming, and previous weak investment from Intel before they decided they wanted to do otherwise, that like 10 years of a lot of computers were really lousy at OpenGL.

Actually I'm still using one right now as I write this!  12 year old business class laptop, that you can't even assume has OpenGL 2.0 on it.  It's always breaking OpenGL centric stuff if I try out, because a lot of code doesn't do appropriate "robust" checks for capabilities that old.  Perfectly good Intel DX 10.1 implementation on it though.

Given past history, I fully expect the same nightmare out of Vulkan, no matter what people think and believe or want to believe.  I'd be swayed by actual evidence of Vulkan games shipped that are working just fine without bugs on Windows, but I haven't looked into that.  I think Linux crowd generally speaking is kidding themselves about these Windows deployment issues, that they just cannot be taken seriously.

If you are a game developer, you want to do this kind of engine, and you want to make money on Windows, you do DX12.

-------------------------

Modanung | 2020-02-21 09:50:47 UTC | #25

Cross-platform solutions soften brand locks, threatening business models.

-------------------------

JTippetts | 2020-02-21 16:44:29 UTC | #26

If you're taking suggestions on where to focus your efforts, I'd like to throw in the suggestion of working on the web backend, or the GLES3 + WebGL2 stuff that @orefkov and @weitjong started on. The WebGL backend with Emscripten has a few small issues, related to input handling and canvas sizing, that need ironed out before it can be considered battle-ready. Urho3D would really fill an under-served niche (C++ engines for 3D WASM/WebGL games) if we could get that system into shape. It's 90% there, just needs a little bugfixing.  And WebGL2 support would be a nice future-proofing effort, even if it's not yet as widely supported as WebGL1.

-------------------------

johnnycable | 2020-02-21 16:49:37 UTC | #27

Subscribing to that. Win as DX, Apple has Metal, and the only platform for Vulkan is Linux. Scarce adoption, scarce support. It's going to take long, oh so long, before (and if) VK takes off...

-------------------------

rku | 2020-02-21 17:07:35 UTC | #28

Android future is vk and it won't take long. Vk is best xplat option really.

-------------------------

shiv | 2020-02-21 17:11:10 UTC | #29

I agree. Also, Android is just another Linux.

-------------------------

shiv | 2020-02-21 17:13:10 UTC | #30

I had not yet got chance to play around with webgl. I guess WebGL 1 should have been working fine, as I saw a few examples on website. What other benefit WebGL 2 will bring besides future proofing?

-------------------------

JTippetts | 2020-02-21 17:24:08 UTC | #31

WebGL is almost there, but there are some issues still, even with the official samples. For one, buttons and checkboxes receive double input events on mobile browsers. For another, I sometimes get disappearing modifier keys if I run an application in an iframe; ie, It won't detect if Ctrl or Shift is held if I run my game in an iframe. I have yet to test if that issue shows up in the official samples.

-------------------------

bvanevery | 2020-02-21 21:58:38 UTC | #32

[quote="Modanung, post:25, topic:5857, full:true"]
Cross-platform solutions soften brand locks, threatening business models.
[/quote]

I *wish* that were true in 3D.  It isn't.

In 1996 to 1998 I optimized OpenGL device drivers for Digital Equipment Corporation workstations on Windows NT.  We had the DEC Alpha CPU, the fastest in the world at the time, and still the best CPU RISC architecture I've seen to this day.  I was a super elite assembly coder jock, as good as anyone in the world on this specific chip.  We had a strategic alliance with Microsoft.  We were trying to kneecap Silicon Graphics, then the 900 lb. gorilla of the 3d graphics workstation and rendering farm world.  Integraph was doing the heavy lifting with their "cheap" Intel based workstations, but we were doing our part too.  And in not that many years, we all won.  SGI died, slain, a titan falling hard into the dirt.  They had additional screw-ups, like hemorrhaging the 3d engineers that formed NVIDIA and 3dfx Interactive.  They were anti-commodity and anti-Intel, they wanted to sell their own MIPS processors, and that hubris ultimately killed them.  The world was changing to a commodified marketplace and they simply wouldn't get with the times or make appropriate investments in **consumer grade OpenGL**.

In this environment, Microsoft the proprietary overlord, foisted DirectX on us.  First versions were *very bad*.  They bought this company called Rendermophics and just ripped the lid off their cheesy implementation, to produce DX 3.x.  I forget the exact version number or letter, but I want to say 3.0a.  Us jocks had *huge* fights on Usenet about the stupidity of all of this.  Had to do with immediate vs. retained mode models of API, with very bad consequences to performance of the HW of the period.  These Rendermorphics people were complete amateurs and couldn't HW their way out of a paper bag.  I think they were London based; Microsoft summoned them to Redmond and decapitated them.

Microsoft got busy and produced DX5, the first *decent* version of it.  OpenGL had a real proprietary threat aimed right at it.  It was now incumbent upon the OpenGL ARB, the consortium of vendors that worked out the standard, to *act*, to meet the threat.  Because of their competing business interests, they mostly proved unable to do so.  A proprietary company has a much easier time *executing* a strategy, than a bunch of companies trying to cooperate with each other.

The consumer PC did *not* get OpenGL investments from the ARB vendors, because they were mostly Unix workstation guys.  And then Microsoft *kneecapped* OpenGL on their platform.  We worked closely with the Microsoft team in Redmond, we were only 2 miles away in Bellevue.  Internally they decided at some point, *no future investments* in OpenGL.  We were allies and under NDA, so we couldn't talk about it.  Microsoft would hold developer conferences and *flat out lie* to people about what was going to happen to OpenGL.  It was going to die, it was being killed as they spoke, and they told everyone the opposite.  To get the most distance over people while slicing the knife into the jugular.  I hope I held my grimaces back sufficiently in public, when they were saying all of this, as I knew my duty to DEC.

It torpedoed our efforts in the DEC Commodity Graphics group to provide cheap OpenGL implementations on Windows NT.  We worked closely with Microsoft and were reliant on their codebase to make our own stuff work cost effectively.  When they cancelled, we were in a serious bind.  So serious that ultimately I quit my job and moved on.  We could have tried to do heroics and make totally our own codebase, but our boss didn't think we could do it in time and be market relevant.  He may have been right.  We will never know.  We were crippled by Microsoft, and then internal politics threatening the DEC Alpha itself, finished us off.  Compaq sought to buy DEC.  Within 6 months after I left, our Commodity Graphics group was no more, and my peers were out finding new jobs.

A few years down the road, SGI imploded and Khronos emerged.  They seemed to have few real resources for development.  They had one last chance to save OpenGL, with their release of 3.0.  I forget the details now, but somehow they did a rather bad job with it.  They couldn't execute or stay relevant.  And so finally, Microsoft's long campaign of terror against it, bore its final fruit and it drifted unrecoverably towards death.

The moral of this story is that when a proprietary vendor dominates an OS platform, they *will* win.  They can make crippling decisions to control their platform.  Nowadays you don't just have Microsoft playing this game, you *also* have Apple playing this game with Metal.  Apple historically had very tepid support for OpenGL, they grumbled a lot and dragged their feet about implementations.  If Apple had decided to back Vulkan to modernize, then it could have had a chance.  But they didn't, they decided to dominate everything with Metal.  It's their corporate DNA to do so, they also are doing Swift instead of Objective C now.  Lock you into their ecosphere by any and all available means.  I already know exactly how this plays out, having seen it during the Windows monopoly era.

Now it is possible, that DX12, Metal, and Vulkan are all *so* similar, compared to historical differences between DirectX and OpenGL, that the engineering side of things is not really a problem.  I don't know, I haven't kept up, I don't write device drivers anymore.  So maybe if you could snap your fingers and produce the needed support *right now*, everyone could be happy with Vulkan everywhere.

The problem is, all Apple *or* Microsoft has to do to wreck that, is just change something.  They control the destiny, not Khronos.  And although I might be prepared to believe that Microsoft is more looking towards open source and open standards nowadays, I do *not* believe that about Apple *at all*.  They *will* ruin this show, to the best of their ability to do so.

In the real world, chasing platforms around is a substantial driver investment.  Expect Vulkan to lag, because $$$$ business arguments have to be made to pay engineers to do all the gruntwork.

-------------------------

johnnycable | 2020-02-22 14:58:28 UTC | #33

Do not miss the market point. 3D on a phone is a punishing experience. Apple and Android are mainly 2D platforms for gaming. 3D stands really on something more immersive, desktop, AR...
Anyway a standard is a standard and maybe Android will be able to push it along alone...

-------------------------

Modanung | 2020-02-22 15:37:24 UTC | #34

[quote="bvanevery, post:32, topic:5857"]
I *wish* that were true in 3D. It isn’t.
[/quote]

In my view, your expansion only confirms my earlier statement.

-------------------------

bvanevery | 2020-02-22 18:40:33 UTC | #35

Microsoft does "Veni, Vidi, Vici!" with DirectX, killing OpenGL.  How do you figure that confirms what you believe?  3D APIs are inexorably linked to HW platforms and OSes.

First Silicon Graphics had [IRIS GL](https://en.wikipedia.org/wiki/IRIS_GL) and their [IRIX](https://en.wikipedia.org/wiki/IRIX) version of Unix.  Then they release OpenGL in 1992, with the *full intent* of mostly dictating how OpenGL is going to be developed and used.  They make other Unix workstation vendors dependent upon them, especially with respect to their OpenGL Sample Implementation codebase.  Workstation vendors have some wiggle room in principle within this open standard, but in practice, OpenGL is designed to perform best on *SGI hardware*.  They control this world.

Meanwhile, many battles happen in Unix land for control.  You are right that cross-platform solutions soften brand locks here.  Eventually Linux comes along, creating a new low end option in the Unix market.

Here comes Microsoft!  They want to get into the expensive high end Workstation market.  They ship [Windows NT](https://en.wikipedia.org/wiki/Windows_NT) in 1993, same time as Linux and Java are getting off the ground.  CAD workstation seats are way too expensive back then, so Integraph allies with MS to make cheaper Intel CAD boxes.  DEC has the Alpha, and also [VMS](https://en.wikipedia.org/wiki/OpenVMS) which used to compete with Unix.  They have a Unix too, but they're a minor player in that market and not Unix loyalists.  They ally in the crusade to dethrone SGI, with both expensive and relatively cheap DEC Alpha Windows NT workstations.

MS wins!  "Veni, Vidi, Vici!" with Windows NT.  The only reason you are doing Unix today, is Linux and the FSF.  They saved the show.  If Linux had never happened, then you'd be using Windows today.  The FSF with Richard M. Stallman would have *never* gotten the job done.  Mr. Stallman can't execute in industry.  Linus Torvaldis can.  If he hadn't existed, you'd have needed someone else like him to come along, to save us from The Beast.

When Steve Jobs came back to rescue Apple, he brought the Mach kernel and NextStep based technology with him.  So if Linux didn't exist, Unix could have had a resurgence then.  But Mr. Jobs was a controlling asshole, as big an asshole about locking you in as Bill Gates ever was.  Jobs didn't even want you *opening your Mac case*.  He went to extraordinary lengths to tie the Apple user's hands.

Once Apple shipped the iPhone, they gained real power.  It made them tons of money and made them more important than Microsoft!  And now they want to take over the whole world, every single business and market they can get into.  They fight with Google, Amazon, and Facebook for control, but it's not *cross-platform* that loosens their grip.  They're Walled Garden all the way down, they don't believe in cross-platform.  Their grip is loosened by *fights in the consumer market*, for control.  They're not a monopoly, people do switch phones.

They are *never* going to make it easy to do Vulkan.  The minute someone gets something sorta workable together, they're gonna *change Metal*, to break it.  They'll do it at the API level, they'll do it at the device driver level.  Because *they can*, and they *want to*.  Just like MS wanted to do with DirectX vs. OpenGL once upon a time.  All the Apple execs can look back at history and confidently say, well that DX thing, it went really really well for Microsoft!  "Veni, Vidi, Vici!"

Why would Apple help Linux?  Someone said, rightly or wrongly, that Android is a Linux.  Well Google is one of Apple's arch-rivals.  *Of course* you do your best to kneecap your rivals.  They don't want mobile games on Android, they want mobile games on iPhone.

Those who don't study history, are doomed to repeat it.  I'm afraid that *young* FLOSS types, can be hopelessly naive in their ideology.  I'm not talking about you, Modanung.  I'm talking about the OP.  If he's going to pour all the effort into Vulkan, he should do it with eyes open about what's going to happen.

-------------------------

SirNate0 | 2020-02-22 19:00:01 UTC | #36

My 2 cents:

Personally I think Vulkan would be the best first choice as a modern graphics API. I think the case could be made for DX12, because Windows has by far the largest desktop share, but Android certainly dominates on mobile (and while 3D on mobile is certainly taxing on the device and possibly the developer, I think that is actually an opportunity for smaller developers while the AAA games focus mostly on Windows). Vulkan is also the only modern graphics API that does work on most all of the platforms Urho does.

I certainly don't think Metal is the way to go (at least as the first new graphics backend), as that only works for Apple products, and MoltenVK exists. Certainly, Apple could break Vulkan support, but for one I don't think it's in there interest to do so, since they're more of a services and hardware company than a software one (unlike old Microsoft), but if Metal were selected, the point stands that it will likely *never* work on any non-Apple platform.

-------------------------

kakashidinho | 2020-02-22 20:06:17 UTC | #37

I think just let OP decide what he wants to do. After all, this is just an open source project. Also, why not support as many graphics backend as we can. Though I think Vulkan is the most loved API by open source communities.

For OpenGL, its features have become a lot like D3D overtime. Its problem is that vendor implementations are often very buggy due to lack of interests and also the complexity required is huge. Modern API like Vulkan shifts a lot of burdens to developers so driver implementation has become much more simpler.

As for Metal, I really like it since it is a low overhead API but at the same time much simpler than Vulkan and D3D12. I feel like it is a middle ground between older APIs (D3D11/GL) and newer APIs (D3D12/VK).
I had a chance to talk to Metal team at Apple office recently. It seems they don't any hostile opinions of Vulkan. It's just that they decided to implement only Metal on their own since it is designed by them with their hardwares in mind and it is easier for them to implement only one API.
I agree that platform specific APIs are almost always the best choices for their respective platforms. Since they are designed for their specific platforms/hardwares.

And btw, I think on Android, OpenGL ES is going to be implemented on top of Vulkan internally anyway. I think recent release version allows user to choose Vulkan as GLES driver.

-------------------------

bvanevery | 2020-02-22 20:27:35 UTC | #38

[quote="kakashidinho, post:37, topic:5857"]
I had a chance to talk to Metal team at Apple office recently. It seems they don’t any hostile opinions of Vulkan.
[/quote]

OpenGL team at Microsoft wasn't hostile to DirectX either.  They were *engineers*, they didn't see things in terms of API takeovers.  But they were *not calling the shots* about business strategy.  Some suit higher up, tells them, "You are not working on OpenGL anymore.  Here's your new assignment in the DirectX working group.  You will move to new group and you will do what you're told.  If you don't like it, you can quit.  And you're under NDA, so you will *not* go blabbing to the rest of the world at the next developer conference.  In fact if you want to keep your job, you will stand up in front of the crowd and *lie to* them about what's happening.  These are our marching orders, take it or leave it."  Yes it was the head of the OpenGL development, who personally delivered the lies *on orders*.  In private, he apologized to us, knowing full well the impact.  His hands were tied.

You don't know anything about what Apple is going to do, *unless* some junior engineer was dumb enough to let something slip.  Even I wasn't that dumb, I knew my place.

[quote="SirNate0, post:36, topic:5857"]
Vulkan is also the only modern graphics API that does work on most all of the platforms Urho does.
[/quote]

Vulkan is never going to be plug and play across all platforms.  That's a developer's *fantasy*.  Reality is every platform supported will take some integration work to keep it functioning.  Every platform will have quirks, if it works at all.  So if you say an Android-centric effort is going to "work well" across all platforms Urho3D touches, well <cough cough> it isn't true.  It'll work well on Android, if you can even cover Android since there are an awful lot of versions of Android.  It's not going to somehow become the basis of Urho3D the engine, doing all this easy work in Vulkan, easy time everywhere.

When Urho3D finally gets into this "more direct" style of API, it will need some kind of unifying layer.  It doesn't matter whether someone starts with Vulkan, DX12, or Metal.  It doesn't matter what someone's theoretical preferences for "the best" API are.  What will matter, is someone doing the work on *one* platform.  They will *probably* fail at it, hard.  In the event that they don't, dust off whatever they've got, and try to make that unifying layer on a 2nd, 3rd, and 4th platform.  It will be a long work.  Doesn't matter which API is the starting point of such work.

I try to influence the OP to make their choice, not for *fantasy* reasons.  Like if they want to do whole hog Linux, know that they are doing that.  Or whole hog *Android*, know they are doing *that*, and that it's *not* Linux.  And that thinking they will get iOs or OSX "for free", is sheer fantasy.

-------------------------

Modanung | 2020-02-22 22:31:04 UTC | #39

[quote="bvanevery, post:35, topic:5857"]
How do you figure that confirms what you believe?
[/quote]

I meant to describe part of a dynamic. If Apple and Microsoft were not be interested in brand locking their victims they would have been more likely to unite their efforts.
Seeing a threat is not the same as losing a battle. Of course they *will* in the long run. :wink:

In my view it would be wise to focus on what the Khronos group has to offer.

-------------------------

bvanevery | 2020-02-22 22:58:13 UTC | #40

[quote="Modanung, post:39, topic:5857"]
I meant to describe part of a dynamic. If Apple and Microsoft were not be interested in brand locking their victims they would have been more likely to unite their efforts.
[/quote]

Total agreement here.

[quote="Modanung, post:39, topic:5857"]
In my view it would be wise to focus on what the Khronos group has to offer.
[/quote]
History shows that it's *hard* for different vendors to cooperate, even when an Existential Threat is facing them.  SGI, OpenGL ARB, *failed*.

Khronos is a *weak* follow-on from that.  Weaker than the OpenGL ARB ever was.  They don't have all that many development resources.  That's why they utterly failed at their [Longs Peak initial OpenGL 3.0](https://en.wikipedia.org/wiki/OpenGL#Longs_Peak_and_OpenGL_3.0) release.  They displayed incompetence, inability to execute in real industry.  We can hope that they are better at steering their ship now, but damage has been done, they lost a few years of ground to the competition.  It killed OpenGL, it affects uptake of Vulkan.

-------------------------

shiv | 2020-02-23 03:17:28 UTC | #41

I have gone through all posts and I believe that, lots of fellow members are in favor of Vulkan backend.
Also, d3d12 backend is promising for Windows but I believe for now d3d11 support is good enough and we can defer it.
As far as concerned about WebGl 2.0, I could not try it and nor I want to divert my focus. 
So, I will be focusing on Vulkan first as this could bring support for multiple platforms and it can boost Urho3D performance.

-------------------------

bvanevery | 2020-02-23 18:37:58 UTC | #42

I hope you get the results on Linux or Android you are looking for.

[quote="shiv, post:41, topic:5857"]
Also, d3d12 backend is promising for Windows but I believe for now d3d11 support is good enough and we can defer it.
[/quote]

DX11 is going to be around for awhile yet, because it's much less work for developers to deal with.  Hopefully you realize [the difference](https://en.wikipedia.org/wiki/Direct3D#Direct3D_12):

>**Direct3D 12** [[97]](https://en.wikipedia.org/wiki/Direct3D#cite_note-anandtech.com-97)[[99]](https://en.wikipedia.org/wiki/Direct3D#cite_note-redgamingtech.com-99)[[104]](https://en.wikipedia.org/wiki/Direct3D#cite_note-104)[[105]](https://en.wikipedia.org/wiki/Direct3D#cite_note-105)[[106]](https://en.wikipedia.org/wiki/Direct3D#cite_note-anand12-106)[[107]](https://en.wikipedia.org/wiki/Direct3D#cite_note-107) allows a lower level of hardware abstraction than earlier versions, enabling future games to significantly improve multithreaded scaling and decrease CPU utilization. This is achieved by better matching the Direct3D abstraction layer with the underlying hardware, by means of new features such as Indirect Drawing, descriptor tables, concise pipeline state objects, and draw call bundles. Reducing driver overhead is in fact the main attraction of Direct3D 12, similarly to AMD's [Mantle](https://en.wikipedia.org/wiki/Mantle_(API));[[106]](https://en.wikipedia.org/wiki/Direct3D#cite_note-anand12-106) in the words of its lead developer Max McMullen, the main goal of Direct3D 12 is to achieve "console-level efficiency" and improved CPU parallelism.[[108]](https://en.wikipedia.org/wiki/Direct3D#cite_note-108)[[109]](https://en.wikipedia.org/wiki/Direct3D#cite_note-109)[[110]](https://en.wikipedia.org/wiki/Direct3D#cite_note-110)

DX12 has a *very different* theory of operation than DX11, one that burdens the developer a great deal.  You will face the same kind of difference doing Vulkan instead of OpenGL.  Good luck!

-------------------------

Eugene | 2020-02-25 11:13:33 UTC | #43

[quote="kakashidinho, post:37, topic:5857"]
Also, why not support as many graphics backend as we can
[/quote]
I want to answer this.
Because the less code we have to maintain, the better.

If a person adds new backend, will this person sign a contract in blood to continue development of said backend until their death? I suppose no.

Therefore, when next person comes to add some important feature, said person will have to deal with even more backends.
Combinatory explosion of variations is already bad enough in Urho.
Urho doesn't have geom/tess shaders now, and the more backends you add, the less likely Urho will get these shaders.

-------------------------

bvanevery | 2020-02-25 20:31:12 UTC | #44

I mostly agree.

In $0 open source, people implement *what they want.*  What they are *personally* committed to.  So for instance if you *know* you want Metal, you will implement Metal.  Doesn't matter what others are doing, what others *might* want.  You are doing the work.  I *know* I want DirectX 11, that's why I'm here participating at all.  I know I want a scripting language and not just C++, so I work on those issues.

Outside of the *personal* commitment, nothing in the real world actually gets done.  $0 open source developers usually overestimate *their skill*, underestimate *the difficulty* of things, and often have no concept of their **limited shelf life** as a contributor.  Real life happens.  People get older.  People lose their time, end up needing real money for time spent.

Leads of projects step down.  Even big, famous, important leads, like the guy who did LuaJIT.  He was as important in the world of Lua, and even in the world of *virtual machines generally*, as it gets.  He wrote literally the fastest virtual machine in the world, for such a small language implementation not counting LLVM optimizer or whatever.  He did something others didn't think could be done.  Yet he's pretty much gone, pretty much back seat advisory role now.  Trying to pass the torch to someone else, and nobody's picking it up.

So if you're working on your Metal, you'd better *finish and ship* your Metal.  If you don't, then realistically, no one else will!  Or your Vulkan, whatever.

A leader has to make a good foundation, if anyone is going to maintain it in the future.  Otherwise it crumbles, bit rots, and dies.  Nobody likes looking at someone's half-finished, half-assed, broken code.  Nobody's getting paid to do it, so if it sucks, it gets ignored.

-------------------------

kakashidinho | 2020-02-26 02:28:36 UTC | #45

OK, I get your points. I was just asking that because many major engines out there support multiple graphics systems, hence why you want OP to implement a certain API. Maybe he just wants to improve his skills in different areas he need, and an open source project is a good opportunity. If he won't be able to finish it, it is not like it will be accepted into Urho either.

Btw, as much as we want to support cross platforms using the same code as much as possible. There will always be some differences and specific fast paths belong to certain APIs. For example, the traditional deferred rendering is not suitable for mobile GPUs even if the graphics APIs (GLES 3, vk, metal) supports doing so. On mobile, the deferred pass needs to be implemented differently on different graphics API in order to make it more efficient. MoltenVk won't solve this problem, its tessellation emulation is also a potential slow path since the way Metal's tessellation works is totally different from vk. But yeah, it is not very important for many people. Furthermore, at some points, maybe you should start removing legacy back-ends such as D3D9. Maintaining older graphics APIs are harder when the modern API design keeps going to a different direction .

Anw, I did have a thought of implementing metal in Urho in the past, I want to add something useful to Urho using what I'm good at (I suck at many other things). But still not sure whether it is worth the time and efforts or not, now maybe not. And if I was to do something, I would never leave it half finished before publishing either (and as mentioned Urho could just reject it).

-------------------------

George1 | 2020-02-26 02:53:03 UTC | #46

Hey Hoang I know you together with elix22 could do this in days :).

The thing is like you said, whether the implementation get accepted into core is another question.

-------------------------

johnnycable | 2020-02-26 16:26:26 UTC | #47

[quote="kakashidinho, post:45, topic:5857"]
Metal’s tessellation works is totally different from vk.
[/quote]

Ditto on this. Considering how mobile works, probably the best thing would be to separate 
into 2 different profiles: one for 3D/Desktop and another for 2D/mobile, probably...

-------------------------

SirNate0 | 2020-02-26 17:15:03 UTC | #48

As someone who personally dislikes most 2D mobile games, while I support a split in profiles, I think it would be better to just split it Desktop and Mobile, or if needed Desktop, Mobile 3D, and Mobile 2D (or High Quality, Medium/Low Quality, and 2D).

-------------------------

bvanevery | 2020-03-16 21:51:26 UTC | #49

I have been investigating Diligent Engine.  It already has a number of things Urho3D might like to have, such as Vulkan, DX12, C++17, and generally speaking "modern" attitudes towards the 3D engine problem.

Indeed, one might wonder, why not just go work on that project instead?  The big thing I've found lacking so far, is no obvious developer community or forum.  It may be open source, but it doesn't look like "contributions discussed or accepted" open source.

It also doesn't have any scripting language.  That doesn't strike me as a big difference though, because I won't ever use AngelScript.  If I did commit to Lua, it would have to be 5.4, and me implementing that support.  So from my standpoint, neither engine has scripting that I want.

Anyways, apropos of Vulkan rendering concerns, they have a blog entry about [resource state management](http://diligentgraphics.com/2018/12/09/resource-state-management/).  This is all really picky and involved.  It's very different from "old school" game programmer doesn't-have-to-care way of doing things.  If someone thinks they're going to do Vulkan or Metal or DX12 for Urho3D, they'd probably be wise to study an engine that's already been walking down that road for 5 years.

> ## Resource state management in Diligent Engine
> 
> The purpose of Diligent Engine is to provide efficient cross-platform low-level graphics API that is convenient to use, but at the same time is flexible enough to not limit the applications in expressing their intent. Before [version 2.4](https://github.com/DiligentGraphics/DiligentEngine/releases/tag/v2.4), the ability of application to control resource state transitions was very limited. Version 2.4 made resource state transitions explicit and introduced two ways to manage the states. The first one is fully automatic, where the engine internally keeps track of the state and performs necessary transitions. The second one is manual and completely driven by the application.

-------------------------

