TheSHEEEP | 2017-01-02 01:13:31 UTC | #1

Hey there,

I'd like to know what approach you'd suggest when using Urho3D for the following case:

I want to display a large (truly large, think hundreds, possibly up to 1000) amount of animated 3D units at the same time.
Now, I know of two methods to achieve that, at least in principle.

1) Using sprites. I know I wrote 3D before, but sprites would work just as well when available in multiple directions. Heroes Of Annihilated Empires used that approach and had a really unique style that I liked very much:
[video]https://youtu.be/NAoMWOT2eXo?list=PLhG6bWwiy1v5I9fQ-gxohI8ffVCVI96D3&t=65[/video]
For that to work, sprites obviously have to be put into the 3D scene with correct clipping and at least alpha testing. 
I figure something like that could work using BillboardSets, no? Or maybe sprites directly?

2) Hardware instancing. I know that Urho3D automatically does hardware instancing, but does that apply to animations as well? I know hardware instancing with animations is possible (I think Ogre has a demo on that?), but afaik it is a different beast than non-animated hardware instancing.
So, is this actually supported in Urho3D?

-------------------------

cadaver | 2017-01-02 01:13:31 UTC | #2

Skinned instancing is not supported, so you'd need to modify the engine for that, or create your custom skinned model component. One idea would be to write the skin matrices to a texture and read from it in the vertex shader, however I haven't tried that in practice.

Though in my tests 1000 animated models using unmodified Urho isn't a huge stretch, so the instancing is not necessarily a must for that. Using the SkeletalAnimation sample bumped to 1000 models I got a little over 100 FPS with a fairly beefy CPU & GPU. 1000 drawcalls in general isn't much. The Jack models in SkeletalAnimation are actually 2 drawcalls each, head and body, so if you can use just one geometry/material per model you'd be in even better position. The CPU time to update the animation for all models may even end up dominating the load. Urho does already have a distance-based animation LOD built in, which makes the animation not update every frame for far-away models. You can adjust the severity of the optimization, or also turn it off it you really want all animations to update every frame.

-------------------------

TheSHEEEP | 2017-01-02 01:13:32 UTC | #3

Interesting thought. 
I'll try modifying the sample, too, to see those effects.
Of course, in a real game, there will be more going on than just animated meshes :wink:

Then again, we already kind of established I will do the gameplay on another thread, so it might just be enough.
I need to try it.

What about the massed animated sprites in the 3D world, though?
Wouldn't that be even better, performance wise, even if I have to calculate the exact animation playing for each component?
Even if 1000 models would work on top GPU & CPU, I cannot take that for granted and would like to support mid-range PCs as well.
Let's assume 1000 units, consisting of 20 different units, each with 8 directions of animation. 
If we assume a perfect distribution of all different units & directions, then we would have between 160 (if all equal ones were at the same animation page) and 1000 (if all were on different animation pages) draw calls, with a MUCH lesser triangle count.
Of course, I am hoping that animated sprites use the same draw call if on the same animation page, which might be wrong - not exactly an optimization I'd take as guaranteed :wink:

Again, I'd need to test that, too, of course, but if you say "No! That's a stupid idea!" I would save myself the time :slight_smile:

-------------------------

cadaver | 2017-01-02 01:13:32 UTC | #4

Sprites will be much cheaper than actual skinned models, yes.

The Urho2D sprite batcher is pretty well optimized and should do drawcall combining for sprites sharing the same material / texture. Alternately, if you find Urho2D classes hard to use in a 3D world you can emulate the same with BillboardSet; in that case I recommend to have one billboardset per material for most efficiency.

-------------------------

TheSHEEEP | 2017-01-02 01:13:32 UTC | #5

Did a few tests by changing the demo code:
When I use the 24_Urho2DSprite and pump the amount of coins up to 1000, I don't even see a difference. The FPS max out at 200 FPS (the limit, I guess?).
When I use the 33_Urho2DSpriterAnimation and create 1000 randomly placed little devils (using a random animation), the FPS becomes ~80 (my current machine is just a very mediocre laptop, at best). But I guess that is understandable, given that the devil is much bigger :slight_smile:

I also upped the Billboard sample up to 20 nodes * 50 billboards and the FPS became 130+.
Of course, the Billboard is not animated, and from a small look, I'm not sure if a BillboardSet can actually have animated sprites (other than color animation/rotation, etc.).
So I am guessing that BillboardSet per does not really do what I would need (animated sprites), at least out of the box.

Is there any downside to using Urho2DSprite (AnimatedSprite2D) in a 3D world?
I guess I only have to make sure that the Sprites always face the camera, but that sounds doable.

-------------------------

cadaver | 2017-01-02 01:13:33 UTC | #6

You can rotate the sprites' scene nodes, you'll just have to do that manually after the camera position/rotation is known for the frame.

-------------------------

TheSHEEEP | 2017-01-02 01:13:33 UTC | #7

Excellent, thanks for your help :slight_smile:

-------------------------

