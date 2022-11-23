Eugene | 2020-02-10 18:31:40 UTC | #1

[quote="Modanung, post:15, topic:5913"]
The subjective validity of your statement also depends on what one considers to be “functional changes *in* Urho”. It is in the lightweight bare-bones nature of Urho for its functionality to expand in the peripherals.
[/quote]
Said it before. If you cannot implement some simple task without deep changes in the engine, it's not really "lightweight", it's "missing features". Or outright missing features, e.g. no networking in Web builds. I don't mean Urho cannot be used. It totally can and Urho community prove it. But it would be lie to say that Urho don't miss anything.

Also, only a person who never looked at Urho renderer code can call it "lightweight". It's complicated as hell. Ever looked at View.cpp/Batch.cpp?

-------------------------

cadaver | 2020-02-10 18:31:40 UTC | #2

[quote="Eugene, post:1, topic:5916"]
Also, only a person who never looked at Urho renderer code can call it “lightweight”. It’s complicated as hell. Ever looked at View.cpp/Batch.cpp?
[/quote]

Some things like the logic for pingponging postprocess buffers is definitely not clear or lightweight, instead it's just very hardcoded and there's an element of "magic" to it, which is not nice to have.

One thing which I pondered as a simpler replacement was having high-level helper operations (ie. collect visible objects, collect light interactions, render a collection of objects...) in the Renderer which could be used to make your custom render process in code, somewhat like Unity's Scriptable Render Pipelines are today. Back when I worked on it, Turso3D went a bit into this direction, but didn't get very far.

-------------------------

Eugene | 2020-02-10 18:31:40 UTC | #3

[quote="cadaver, post:2, topic:5916"]
One thing which I pondered as a simpler replacement was having high-level helper operations (ie. collect visible objects, collect light interactions, render a collection of objects…) in the Renderer which could be used to make your custom render process in code, somewhat like Unity’s Scriptable Render Pipelines are today
[/quote]
This sounds quite close to what I meant here:
[quote="Eugene, post:74, topic:5872"]
I have several ideas how to change renderer, but I will not make any plans or promises until I confirm they will work out well.
I want to try one radical approach, but it will require huge commitment of effort and therefore you will not get any updates in the nearest months about it.
[/quote]
Since you are here, maybe you can share some thoughts?

There are a lot of issues (or so I think) in the renderer.
Going from top to bottom:

0) Hard to extend and configure render paths, need an instance for each permutation. E.g. if I want to choose between sRGB and RGB with just a flag, or I want optional GBuffer layer for Deferred, I need to clone RP. We have it now with e.g. Forward/ForwardDepth
1) There is no per-view-per-drawable state, essentially making things like smooth LOD transitions very hard to implement in multi-view use cases.
2) Drawables store a lot of temporary View-specific data used only in rendering.
3) Vertex lights fall back into pixel lights (lolwat) instead of spherical harmonics (cannot really blame Urho because there were no SH back then, but still an issue)
4) Hardcoded vertex and pixel shader permutations, missing automatic shader defines. E.g. I want shader to automatically get defines like `PASS_LITBASE`, `TEXTURE_DIFFUSE` or `INPUT_NORMAL`. If we had it, there would be no need to have 100 techniques for each permutation.
5) Almost zero caching of computations done in View/Batch.cpp, even if result is the same for consequent frames.
6) Uniform Buffers are used in the way opposite to how they are supposed to be used. No wonder they are slower on OpenGL and are disabled there.

-------------------------

cadaver | 2020-02-10 18:31:40 UTC | #4

Not really other ideas, but I thought of the default shaders (ie. LitSolid) being quite monstrous and that it would have been nicer to have shader per purpose, like DiffuseTextured, NormalMappedTextured and possibly get rid of Techniques altogether at same time. Shaders could have then definitions (either automatically or manually) what requirements they have for textures / vertex input streams.

-------------------------

Eugene | 2020-02-11 08:43:29 UTC | #5

[quote="cadaver, post:4, topic:5916"]
but I thought of the default shaders (ie. LitSolid) being quite monstrous and that it would have been nicer to have shader per purpose, like DiffuseTextured, NormalMappedTextured and possibly get rid of Techniques altogether at same time
[/quote]
How would you avoid copy-paste in such shaders?
Even if you extract everything into functions... Well, we already extracted pretty much everything into functions. And LitSolid is still quite huge. Shall we split it, there would be a lot of repeating lines in all variations.

It's also not clear what configuration deserves separate shader and what configuration shall be just a define. How many variations should spawn from just LitSolid?

-------------------------

cadaver | 2020-02-11 11:40:30 UTC | #6

I think, using utility functions where possible.

However, I see how shaders are split more as a content choice, the engine shouldn't need to mandate it either way, just be able to configure whatever it wants out of the shader (like the light type or shadowing on/off). Ideally I always saw whatever Urho included just as an example shader, and the user writing their real shaders :)

Having deferred / forward embedded in same material or shader is also potentially cumbersome no matter how you look at it.

-------------------------

