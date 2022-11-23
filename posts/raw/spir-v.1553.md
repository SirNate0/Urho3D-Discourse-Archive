dragonCASTjosh | 2017-01-02 01:08:28 UTC | #1

Today i looked on the Khronos website to check the state of Vulkan and SPIR-V and to my surprise found that there has been some big additions to the SPIR-V page including the Tools and LLVM  needed to develop with the language. This could solve the current limitation with Urho's shader (some community additions are only in 1 language). I dont have the time and experience to implement such a feature although id be willing to give it a shot with help.

[url]https://www.khronos.org/spir[/url]

-------------------------

Bananaft | 2017-01-02 01:08:28 UTC | #2

What limitations you are talking about?

-------------------------

dragonCASTjosh | 2017-01-02 01:08:28 UTC | #3

[quote="Bananaft"]What limitations you are talking about?[/quote]
There are a lot of shaders on the forums are only in a single shader language.

-------------------------

bvanevery | 2017-01-02 01:08:52 UTC | #4

I don't think having a common intermediate language solves a single shader [i]source code[/i] problem.  Who says that robust disassemblers (? term) from SPIR-V to GLSL and HLSL are going to be provided?  I seriously doubt HLSL would be provided at this point, and for all I know GLSL --> SPIR-V might be a one way trip at present.  Do you have some details from Khronos to suggest otherwise?

Then there's the problem of adoption.  Microsoft has already shipped DX12.  Apple is pursuing Metal.  Why are they going to get in the sack with SPIR-V?  See that thing on the chart that says "100% Khronos defined" ?  Well I bet NVIDIA, ATI, Apple, and MS have something negative to say about that.  It would be nice if the tendency in industry went more towards cooperation, but presently we're going through an "API split" era, so I wouldn't bank on it.

Meanwhile as far as source code problems, I've seen some HLSL --> GLSL translating tools out there, but not really GLSL --> HLSL.  I haven't looked hard, it was just my initial stab at the problem the other week.  But failure to come up with such things quickly, and blog entries that say "it doesn't exist" are worrisome.

-------------------------

bvanevery | 2020-03-09 21:05:31 UTC | #5

More than 4 years go by.  Microsoft open sourced its HLSL compiler.  Khronos added a Spir-V backend.  Khronos says [they can now render HLSL on Vulkan](https://www.khronos.org/blog/hlsl-first-class-vulkan-shading-language).  No idea how well any of it works in the real world, but it seems a Windows-centric developer could just use HLSL and blow off worrying about Spir-V.  Related is Microsoft's [ShaderConductor](https://github.com/Microsoft/ShaderConductor), which can convert HLSL to GLSL.

No idea about GLSL --> HLSL.  These strategic developments, indicate that I clearly shouldn't care.  HLSL is deemed important enough by industry, for me to stick with it.  Someone else can do homework on whether it's viable to worry about things from the GLSL side.  Looks like HLSL can go everywhere... that Vulkan can go, of course.  Which isn't so many places right now, in the real world.

NVIDIA made some DirectX Ray Tracing thingy back in 2018 with Microsoft.  Now they have [added ray tracing support to DXC's Spir-V backend](https://devblogs.nvidia.com/bringing-hlsl-ray-tracing-to-vulkan/).

-------------------------

