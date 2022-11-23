bvanevery | 2017-01-02 01:08:48 UTC | #1

I'm still pretty much a shader noob.  My 3D background comes from the fixed function era.  I'm trying to figure out why [url=https://github.com/gawag/UrhoSampleProject]Urho Sample Project[/url] only runs at 10 FPS on my cheesy 2008 era Intel integrated business class laptop.  I know it's bad but I would not expect it to be [i]that [/i]bad, given that the demo does so little.  Just has a torch, some shadows, and a colored sphere with shiny reflective goop on it.  I added a Debug HUD to the project, basically cutting and pasting from Urho's samples.  Sorry I don't have that in GitHub yet either, I'm a Git noob too.  Anyways the readouts really don't look like they'd tell me a darned thing about shaders per se.  I see that Present is consuming a total of 800 ms, out of 1000 ms for RunFrame.  If it adds up to 1000 ms, sometimes it doesn't.  Anyways that proportion is pretty much correct regardless.  Lotsa time in Present.  I guess that HUD is telling me "hey dumbass, the shaders are gobbling up everything!" and I'm like, yeah, right, kinda figured.

What's your favorite approach for figuring out exactly what about a HLSL shader is gobbling up everything?

I've also got a line at the bottom, if that's helpful.
Tex:High Mat:High Spec:On Shadows:On Size:1024 Quality:16bit High Occlusion:On Instancing:On API:D3D11
Somehow amounts to, choke the crap out of crappy integrated GPU.

-------------------------

bvanevery | 2017-01-02 01:08:49 UTC | #2

Visual Studio 2015 has stuff built in to capture frame info about API side happenings.  Intel also has a standalone Graphics Monitor tool that does pretty much the same thing.  Neither are telling me what's going on in the HLSL shaders themselves though.  Guess I'll keep looking and learning.

-------------------------

Calinou | 2017-01-02 01:08:50 UTC | #3

Give [url=https://apitrace.github.io/]apitrace[/url] a try.

-------------------------

bvanevery | 2017-01-02 01:08:50 UTC | #4

[quote="Calinou"]Give [url=https://apitrace.github.io/]apitrace[/url] a try.[/quote]

Doesn't claim to inspect or profile DX11 so I think that's a no-go.  At least they have a nice feature matrix on their webpage.

-------------------------

bvanevery | 2017-01-02 01:08:55 UTC | #5

I've been checking out AMD and NVIDIA's websites.  All of these 3 old laptops I have are DX10 class HW, and strangely, I have AMD, NVIDIA, and Intel represented.  I guess I can test low end anything.   :smiley: 

AMD's current tools simply don't work with a "ATI Mobility Radeon HD 3400" class device.  I get nasty messages about no AMD GPU being found.  I did find an older discontinued tool that might work, but it wants a DX10 compiler.  Seems to be a similar story with an older NVIDIA tool, the DX10 orientation.  I think when DX11 came along they must have all dumped old stuff and rebranded with new stuff.  So there's a bit of a retro computing exercise going on here.  I'm a little concerned that a DX10 compiler won't produce the same output as a DX11 compiler, but maybe it's close enough to get the big picture of what's going on in a shader.  Although, there's the more specific issue that a "RV630LE" is not a listed device for the AMD tool.  Maybe that particular integrated circuit is in a support black hole that nobody cares about.  It seems I'll have to do further digging to learn about the performance characteristics of the GPUs I actually have.  2 are integrated business class parts and maybe nobody ever cared if they did HLSL well.  1 is an old dedicated NVIDIA card so maybe I'll have better luck with that.

NVIDIA wants to put me in a "cone of silence" for their latest greatest tool, and that's rubbing me the wrong way.  Joining their developer program is required to get the tool.  Their program agreement has a bunch of crap about NVIDIA owning any feedback I give them, and that all that feedback has to remain confidential.  I believe there were additional confidentiality terms, and I got bored of reading their agreement.  Don't think I'm willing to be pwned by NVIDIA.  I did a preliminary look to see if there was some other (illegal) source of the tool available, but no luck.  I guess it's not sexy to pirate something available for free, let alone a mere developer tool.  But a NVIDIA cult of information control isn't sexy either.  Screw them.  At least this is educational about who's offering what, and conditioning the marketplace in what way.  When I finally buy a new laptop I'll be remembering this sort of thing.

I find that the discontinued AMD GPU ShaderAnalyzer 1.59 has some bugs, one of which may make it useless in practice.  The 1st is it doesn't believe various DirectX dlls are available on the system when they actually are, even though Windows 7 was a supposedly supported platform.  I solved that by adding C:\Windows\SysWOW64 in the Options..Include Paths.  The 2nd is it doesn't seem to respect #include "whatever.hlsl", which makes it pretty darned useless in the real world.  I've seen bugs about that in other tools as recently as April 2015, so who knows what was going on back then.  Seems difficult to look back in their archives, maybe they've purged old posts about tools they don't want to talk about.  Don't know if <> or absolute paths would fix it.  Don't care, I really don't feel like going to heroics with code to use a bad old tool.  I will find something else.

-------------------------

