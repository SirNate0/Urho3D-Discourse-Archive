PsychoCircuitry | 2021-10-04 15:18:22 UTC | #1

So, I'm not sure how to go about extending the source to achieve this. I'm trying to implement a blocker search in the lighting shader for the shadow mapping, and my understanding is that I will need 2 sampler states, the traditional comparison state for analyzing depth and also a normal sampler state for reading the values to determine the blockers.

For the sake of api consistency (I'm assuming), the sampler states are created in the directx11 implementation per texture, 1 texture, 1 sampler state, bound equally to the 16 slots. I'm assuming to create a similar environment to dx9, where this was bundled together as the texture item.

Is there anyway I can create 2 states during the shadow pass, registering the 2nd state somewhere I will presume to be empty? I've tried various methods, and obviously I can get the sampler description created when a shadow texture is present, however when I attempt to interject the state somewhere along with original shadow sampler state using PSSetSamplers it always crashes urho. Thread attempting to read write a resource it doesn't have access to. It compiles tho.

I assume I can create an additional texture just for the state, which seems wasteful, since I just need an additional state. And the renderer already has a dummy color texture setup for certain scenarios, I could probably extend this out to work. But I'd rather not, if I don't have to.

I've tried accessing several of the other sampler state registers as well, but the ones I've tried give me an error of overlapping semantics not yet defined, I'm assuming they are not registered during that pass, which is why I think interjecting another sampler state in there should be possible.

Right now, I've scrapped the comparison state, and just perform a manual comparison in the shader with texture lookup, but I'd like the benefits of speed and texture filtering from the comparison state.

My use case doesn't need compatibility with the other graphics apis, so I've thought about redesigning the entire way the states are registered to be more directx 11-esque, creating a new state for every texture when probably a huge majority of them are identical seems a bit redundant. And then I can possibly unbind them from being locked state to texture.

But any ideas on how to move forward with this would be appreciated.

Thanks!

Edit: I managed to get the sampler state added and registered without crashing, altho I would wager its far from safely handled. It works for this specific use case. However now I'm seeing that any sampler state that isn't explicitly registered with the same texture unit as the as the texture itself does not work correctly in the shaders. I'm not sure what I'm not understanding here... I've set the sampler state descriptions to be identical for everything, hard coded values. However even with this, if I try to sample the diffuse texture with the normal map sampler state, I get nothing but black diffuse color. If I sample with the diffuse sampler state, it's correct. If i have the texture hold 2 sampler states, but set the 2nd to a register different from the tu index, same thing. There are no errors, it runs. I've tried removing the calls in implementation where it sets the sampler states to null pointers, I'm not sure this really does anything cuz the sampler state references are tied to the texture itself.

Any ideas?

-------------------------

PsychoCircuitry | 2021-10-03 03:04:40 UTC | #2

My last post was getting long, so updating here.

Here's what I've done now, I set every sampler state to NULL. DX11 has a default state if you assign the state as null. This renders ok as long as everything else is unchanged. If I change any of the sampler states from the default locations in shader tho, I get no texture... black or transparent. I've changed zero shader resources the "t" register slots, only the changing the state, but it discards the texture then...

I've wiped out all the macro defined functions Sample2D etc. And instead changed the shaders to the default dx11 functions ie texture.Sample(samplerstate, coords). I also changed the registration names of the sampler states. Totally unrelated to the texture registrations. I read somewhere that some shader compilers will rearrange and bind things differently as an optimization, but this shouldn't be the case with the native hlsl compiler, but tried anyway.

Somehow the shader resources and sampler states are being bound together. I didn't even think this was possible in dx11 hence the separate registrations. To remove the binding limitations of dx9, so shader resources and sampler states could be reused however without having to create a whole new resource for every change.

I'll keep researching. But if anyone has any ideas how the shader resources and sampler states might be locked together, I'd appreciate any insight. I'm no guru just a hobbyist lol.

Thanks,
-PsychoCircuitry

-------------------------

PsychoCircuitry | 2021-10-04 03:20:20 UTC | #3

Ok back into looking at the problem today. I'm now using renderdoc to debug. I've taken 2 captures, one with texture working, one without. Here's the analysis. The only change between the 2 captures. In litSolid.hlsl I've changed `tDiffMap.Sample(sDiffMap, iTexCoords.xy)` to `tDiffMap.Sample(sNormalMap, iTexCoords.xy)`. Theoretically this should make no difference because, when the devCon sets PS samplers I'm passing a 16 length array of null sampler states. All 16 slots are set to default sampler states.

Now renderdoc shows on the incorrect version, shader resource view for the diffuse texture is non existent! How is this possible? I've changed nothing with how the shader resource views are passed to the shaders.

I'll keep looking into it.

EDIT: another thing of note, if I swap the normal texture lookup for the diffuse sampler, instead of no resource view, I get totally no render data, the vertex buffer is never sent to the input assembler, at least renderdoc shows no data that any of these objects exist in the capture... I'm thoroughly stumped at this point.

I've set the srvs to be registered from 16 to 31, this makes no difference. What is baffling is that I'm not changing the source code between working and not working states. Everything renders correctly as long as I keep the urho locked indices for everything, even with the +16 offset in srv. Things go wacky only when I attempt to use a sampler state that's out of step with a srv. How can changing the sampler state cause a srv to become nonexistent? Or vertex buffer to suddenly disappear? None of this makes any sense with my limited dx knowledge. Looking for any ideas on where to go from here.

EDIT 2: did some exploring on renderdoc settings and enabled the dx11 debugger as well as captured all resources, instead of just used resources. Dx debugger says nothing, couple warnings about sampler states as null being set to default, 1 for the render target being null, in another post cadaver said this is because of the depth write only for the shadow map. The missing textures and or vertex buffers exist on the gpu, but are somehow not making it to the pipeline when I change the sampler state. The texture shows as a floating resource not bound to t0 but only when I change sampler state, it is bound when I use the s0 for sampling...

EDIT 3: OK, now this is just strange... I've managed to trick the shaders into working with another sampler state. It does not work after a fresh install, but if I keep swapping the t0, t1, s0, s1 registers, I can finally get it to render correctly with t0 sampling with s1. HOWEVER, materials with no normal map, use the DIFFUSE texture of another material with a normal map, or go black, it changes under different camera angles. I've made sure that the samplers_ array in impl_ are holding 0 pointers to anything in the textures... this is beyond weird. Mind you the hack for the states doesn't work on first run after fresh install, I have to keep switching the shader defined names of the registers until it clicks. I feel like this may be some sort of cached data issue, but I'm not caching shaders. They are compiled every run. What else could possibly be caching data to cause this? 

Still looking into it. Let me know if you have any ideas of what or where to look for the issue.

-------------------------

Eugene | 2021-10-04 15:11:29 UTC | #4

[quote="PsychoCircuitry, post:3, topic:7004"]
What else could possibly be caching data to cause this?
[/quote]
First of all, make sure that cache of compiled shaders is up to date, or you clear it manually before every run.

[quote="PsychoCircuitry, post:3, topic:7004"]
How can changing the sampler state cause a srv to become nonexistent?
[/quote]
Can you show what exactly you did to have 2 samplers? It's hard to debug code in browser, but it's even harder to debug words.

On the topic, I would say you create second fake texture with the sampler you want, and you just hack dx11 shaders to use it. I mean, like `tDiffMap.Sample(sNormalMap, iTexCoords.xy)`. It sucks, but I cannot come up with anything else.

You may need to patch DX11 backend so it doesn't ignore second texture as unused, e.g. by adding additional scan here:
![image|690x194](upload://qtNfbaBtaQz1FJCeE6CVa3v0Xyp.png)

-------------------------

PsychoCircuitry | 2021-10-04 15:20:45 UTC | #5

Thanks for your response, I was not even looking in the shader variation code yet.

I apologize for not giving more concrete examples of what I was altering in the backend code. It was lots of stuff and reversions (and butchering lol), between my posted updates. But I completely understand where you are coming from with helping debug with zero code. And again I'm sorry. I will keep that in mind with any future posts asking for specific code help.

Anyway your snippet from the shader variation code was exactly what I needed. Making sure useTextureUnits_ index is true for whatever sampler state I want to use in a shader, fixes the issue completely.

Now I can start thinking about how to go forward with my desired solution.

Thanks again,
-PsychoCircuitry

-------------------------

