dragonCASTjosh | 2017-01-02 01:06:50 UTC | #1

Within the Urho community I have noticed allot of projects in shaders that only support 1 language and personally after spending a while working on HLSL I lose the motivation to write it again. There are a few solutions to this problems.

[b]Solution 1[/b]
Write a custom shader language that performs an offline compile to the target language, this solution would be a big undertaking but I feel there would be the benefit of optimisations for all shaders.

[b]Solution 2[/b]
Use a cross compiller to convert between languages. I noticed there have Mojo in our 3rd party list but from my understanding it doesn't have support for d3d11 or gl3. Therefore I'd recommend [url]https://github.com/James-Jones/HLSLCrossCompiler[/url] as it supports all languages used in the engine.

[b]Solution 3[/b]
Shader macros, this would involve making a shader in all languages that will change the default methods and variables we use to be the same in all languages. For example change GLSL vec3 and HLSL float3 to UFloat3.

-------------------------

codingmonkey | 2017-01-02 01:06:51 UTC | #2

You just need once choice the right gapi at stat of doing you game project. 
This allow to you avoid in future jumping from one gapi to other and rewrite all specific stuff for it.

if You need only Win use dx11-renderer
if You need cross-platform you must choice gl-renderer

> benefit of optimisations for all shaders
only manual writing and adjustments in native shader language gives this benefits. and not some common language its may only slow down shaders for both.

>I noticed there have Mojo in our 3rd party list but from my understanding it doesn't have support for d3d11 or gl3.
and it's great because it's have some problems with order of uniform store or something like this, earlier I have problem with it on dx9 renderer.

>For example change GLSL vec3 and HLSL float3 to UFloat3.
it's looked little weird, my choice better use vec3 on glsl and float3 on hlsl

-------------------------

cadaver | 2017-01-02 01:06:51 UTC | #3

I agree that some solution for this would be preferable.

However I don't think we can settle for a solution that requires HLSL bytecode as the input, as non-Windows users don't have access to the Microsoft HLSL compiler.

-------------------------

rasteron | 2017-01-02 01:06:51 UTC | #4

I totally agree with the guys here and yes, it is really getting prominent with GLSL here. For me, it's the cross platform nature and some shaders might work with GL ES as well (with some tweaking).  :wink: 

The HLSLCrossCompiler you have pointed out looks interesting though..

-------------------------

dragonCASTjosh | 2017-01-02 01:06:51 UTC | #5

[quote="codingmonkey"]
You just need once choice the right gapi at stat of doing you game project. 
This allow to you avoid in future jumping from one gapi to other and rewrite all specific stuff for it.

if You need only Win use dx11-renderer
if You need cross-platform you must choice gl-renderer
[/quote]
When developing features for Urho in general for example if i want to make PBR(I know PBR already exists) for Urho and then release it to the public then id have to ensure it works on dx11 and gl.  

[quote="codingmonkey"]
> benefit of optimisations for all shaders
only manual writing and adjustments in native shader language gives this benefits. and not some common language its may only slow down shaders for both.
[/quote]
By optimisation i mean language specific features.

[quote="cadaver"]
I agree that some solution for this would be preferable.

However I don't think we can settle for a solution that requires HLSL bytecode as the input, as non-Windows users don't have access to the Microsoft HLSL compiler.[/quote]
That's a point i didn't consider, maybe Solution 1 or 2  are the best to pick from, i wouldn't mind giving a custom shader language a shot but I'm not sure how to approach it.

-------------------------

cadaver | 2017-01-02 01:06:51 UTC | #6

You touch a larger point, contributing to Urho3D (on a level that is acceptable to be merged to the master) is hard.

Shaders or techniques, need to verify that all render API's work.
For scripting, need to make bindings for both AS & Lua.
Need to ensure components replicate & serialize right.

Unfortunately I don't see easy ways to make that easier :slight_smile: Probably my "ideal game/rendering library" would actually have a much smaller scope to make it more accessible to devs and to keep maintenance sane(r), but of course for Urho it's too late to change, it has grown and one has to live with it.

-------------------------

codingmonkey | 2017-01-02 01:06:51 UTC | #7

>custom shader language 
I don't think so, that custom shader language are good idea, this is thing for thing, the better way if urho3d will have just shader factory/editor for example as blender material nodes and build native shader for both glsl/hlsl shader language.

[img]https://mango.blender.org/wp-content/uploads/2012/04/splashbot_nodes-540x234.png[/img]

In this editor you have various logic bricks and connect they with lines to have a new shader.

-------------------------

dragonCASTjosh | 2017-01-02 01:06:51 UTC | #8

[quote="cadaver"]but of course for Urho it's too late to change[/quote]
I agree it may be to late to fix allot of the issues but i feel there is still improvements that can be made towards this. Although none of them are going to be small tasks to undertake. Shaders may be the easiest to fix currently. But you also brought up scripting and maybe a abstraction layer for registering functions to script could be made.

For Shaders an offline compiler may help for initial testing of shaders as it can point out any errors before you test in all API's. 

[quote="codingmonkey"]I don't think so, that custom shader language are good idea, this is thing for thing, the better way if urho3d will have just shader factory/editor for example as blender material nodes and build native shader for both glsl/hlsl shader language.[/quote]
This is a good implementation although we would still have duplicate shaders on the backend, this means that a visual editor will have to write everything twice and i feel this is not ideal for its performance.

-------------------------

cadaver | 2017-01-02 01:06:51 UTC | #9

Yes, naturally those kinds of improvements can be done (with effort).

What I mean that now it's too late to crop Urho's scope, ie. to actually remove features to make it easier to maintain and contribute to.

-------------------------

dragonCASTjosh | 2017-01-02 01:06:51 UTC | #10

[quote="cadaver"]What I mean that now it's too late to crop Urho's scope, ie. to actually remove features to make it easier to maintain and contribute to.[/quote]
Ah i see what you mean. the only way to remove that problem is a rewrite but i feel that its out of the question for now

-------------------------

cadaver | 2017-01-02 01:06:52 UTC | #11

After some thinking, I believe the engine should always load the graphics API's native shader language. Any homebrew parser or conversion utility will probably never account for all the cases and language features.

However an offline tool to make conversions from a common format to the native languages wouldn't be bad, and it would be optional. Proof-of-concept would be to use it on Urho's own shaders, which tend to be rather basic.

-------------------------

friesencr | 2017-01-02 01:06:52 UTC | #12

[quote="cadaver"]After some thinking, I believe the engine should always load the graphics API's native shader language. Any homebrew parser or conversion utility will probably never account for all the cases and language features.

However an offline tool to make conversions from a common format to the native languages wouldn't be bad, and it would be optional. Proof-of-concept would be to use it on Urho's own shaders, which tend to be rather basic.[/quote]

an offline tool could run other things like glsl optimizer without having to take on any runtime dependencies.

-------------------------

cadaver | 2017-01-02 01:06:52 UTC | #13

When I tested GLSL optimizer it seemed to strip away conditionals, which means it would have to be run separately on each shader permutation, and those are only known at runtime. If there's a way to run it without doing that, then it would fit perfectly.

-------------------------

dragonCASTjosh | 2017-01-02 01:06:53 UTC | #14

[quote="cadaver"]When I tested GLSL optimizer it seemed to strip away conditionals, which means it would have to be run separately on each shader permutation, and those are only known at runtime. If there's a way to run it without doing that, then it would fit perfectly.[/quote]

It looks like UE4 is taking a similar approach to this, they also used mesa glsl optimiser but then changed the input to accept hlsl: 
[url]https://docs.unrealengine.com/latest/INT/Programming/Rendering/ShaderDevelopment/HLSLCrossCompiler/index.html[/url]

I guess a similar approach for Urho may also work although to the sounds of things we may have to make a number of changes to the library.

-------------------------

dragonCASTjosh | 2017-01-02 01:06:53 UTC | #15

[quote="Sinoid"]
That was a joint effort by nVidia and Epic for UE4. They gave a talk about it at GDC, the recording is in the vault, it was an enormous project that was part of the even more enormous OpenGL porting nightmare they went through.
[/quote]
very true but from my understanding they where a d3d11 only engine at the time and most of the work was put into the engine itself and not as much with the shaders

[quote="Sinoid"]
A more realistic approach would be to start with BGFX's ShaderC and maul it into something more tolerable and not dependent on BGFX. It's at least relatively modern already, as opposed to hlsl2glsl or hlslparser. Also doable solo and able to nicely sit outside (or inside if later deemed worthy).[/quote]
BGFX's ShaderC looks very good,  it looks like it takes in hlsl and compiles to both glsl and hlsl but I'm not to sure. it also looks like a perfect setup for a visual editor like what codingmonkey suggested.

-------------------------

amerkoleci | 2017-01-02 01:06:54 UTC | #16

Please take in account that offline shader compilation would require shader permutation support too, immagine I have different number/types of lights in my scene, My material can have diffuse and normal map enabled in one scenario and in other only diffuse map enabled.

-------------------------

cadaver | 2017-01-02 01:06:54 UTC | #17

The way this should (IMO) be done is that the compilation preserves all #ifdefs present in the shader code. 

In the dark ages we used to be forced to enumerate the shader permutations beforehand, and indeed for example all HLSL permutations would be precompiled offline, but this was clumsy. Now, with HLSL, it compiles during runtime and writes the compiled permutations into binary files inside the shader cache directory for fast loading the next time, but this isn't mandatory, and on GLSL a similar mechanism isn't possible at all.

-------------------------

amerkoleci | 2017-01-02 01:07:11 UTC | #18

Right, compile or load from cache is the best approach, this is fine until you get in account compute shaders, D3DCompiler is very slow to compile them on runtime, I saw an example where it can take up to 1minutes or something.

-------------------------

boberfly | 2017-01-02 01:07:31 UTC | #19

I'm excited for SPIR-V taking off in a big way, and tools to convert this bytecode to GLSL or HLSL. Especially when someone could theoretically make an entirely new language, perhaps cython-like or have some node-based system perhaps.

But yeah, future-thinking here.

Also:
[url]https://github.com/google/shaderc[/url]

-------------------------

dragonCASTjosh | 2017-01-02 01:07:31 UTC | #20

From my understanding SPIR-V should already output GLSL Bytecode or at least something OpenGL can use. HLSL output from the sound of things shouldn't be hard for anyone with a good grasp on programming and shaders. As for a GLSL to SPIR-V converter i do believe that Khronos are realising on along with Vulkan and its part of the LunerG/Valve Vulkan SDK.

-------------------------

boberfly | 2017-01-02 01:07:32 UTC | #21

[quote="dragonCASTjosh"]From my understanding SPIR-V should already output GLSL Bytecode or at least something OpenGL can use. HLSL output from the sound of things shouldn't be hard for anyone with a good grasp on programming and shaders. As for a GLSL to SPIR-V converter i do believe that Khronos are realising on along with Vulkan and its part of the LunerG/Valve Vulkan SDK.[/quote]

So yep there's already glslang from Khronos which takes GLSL in and converts to SPIR-V. Google's shaderc uses it as a library with their own interface.

The closest thing I'd image happening is like this:
[url]http://cgit.freedesktop.org/~airlied/virglrenderer/tree/src/vrend_shader.c[/url]

This code is part of virgl (which is essentially a Gallium 'OpenGL' driver which supports multiple state trackers on top, and converts TGSI bytecode to GLSL). Just replace TGSI with SPIR-V and there you go, outputs probably human-unreadable GLSL.

On a side-note I'd very much like to see a virvulkan in future, use Gallium's plethora of state trackers (including the DX9 one) and run it on any Vulkan-capable driver. That would super-charge a whole back-catalogue of DX9-only games for SteamOS potentially....

-------------------------

Enhex | 2017-01-02 01:08:50 UTC | #22

With C++ expression templates can be used to generate either HLSL/GLSL from C++ code.
A library like Boost.Proto can be used to do it: [boost.org/doc/libs/1_59_0/do ... proto.html](http://www.boost.org/doc/libs/1_59_0/doc/html/proto.html)

That could be a really interesting project.
For an example check out VexCL library: [github.com/ddemidov/vexcl](https://github.com/ddemidov/vexcl)

-------------------------

rku | 2017-11-11 11:20:47 UTC | #23

bgfx actually uses shader macros to bridge gap between shader languages. Since languages are similar enough there isnt much that needs to be done through macros either. Every shader is supposed to include and use this: https://github.com/bkaradzic/bgfx/blob/master/src/bgfx_shader.sh

Is shaderc really required with bgfx? From quick look seems like it could be totally optional.

Considering bgfx port is under way, maybe adopting bgfx approach could be a good idea?

Edit: someone also pointed me to this: https://github.com/mellinoe/ShaderGen. It is not exactly production-ready, but interesting nevertheless.

-------------------------

Eugene | 2017-11-11 13:30:47 UTC | #24

[quote="dragonCASTjosh, post:1, topic:1326"]
Shader macros, this would involve making a shader in all languages that will change the default methods and variables we use to be the same in all languages
[/quote]
Matrix multiplication and array initialization would become a bit ugly, but marco should be fine.

-------------------------

