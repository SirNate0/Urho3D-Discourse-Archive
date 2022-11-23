Leith | 2019-01-31 09:59:04 UTC | #1

i just had a tech discussion about lighting in horror games, i complained that standard lighting equations are not good in dark places, and proposed a negative light, or anti light, that can have 'anti colours'.

I see this useful in general - subtractive lighting can be used in dark scenes, but it is also useful for stained glass projections.

-------------------------

Dave82 | 2019-01-31 12:35:58 UTC | #2

If you want really good results , forget dynamic lights. You need extra calculations , GI , contrast  and desaturation shader to have a real horror atmosphere.To have tolerable results with dynamic lights you should first rewrite Lighting.hlsl (glsl) shader to have inverse square attenuation. BTW this is what i'm working on right now : (You can see the high contrast , specular highlights , baked GI , AO , which is impossible to do with simple dynamic lights)
![image|690x413](upload://1kLDoAlA5K2kO4y5LQJ0aWR8pE2.jpeg)

-------------------------

GodMan | 2019-01-31 19:10:58 UTC | #3

@Dave82 Looks good. I always wondered how to handle dark scenes.

-------------------------

Leith | 2019-02-02 15:41:03 UTC | #4

Instead of GI and baked lighting, we can turn up the ambient lighting, and use negative lights to darken the scene, we get dynamic light and shadow, best of both worlds - just an idea at this stage, but not a huge thing to make happen

-------------------------

Dave82 | 2019-02-03 03:14:48 UTC | #5

Too much work and won't be nearly as good as baked lightmaps. Not to mention to simulate real GI with this solution you'll need 30-40 lightsources in a scene.That scene will run 2 fps on android.
What we need is voxel cone tracing or something like this : 
https://www.youtube.com/watch?v=VOg_8ipCZLA

-------------------------

Modanung | 2019-02-06 08:28:55 UTC | #6

That looks quite noisy _through_ the codec.

-------------------------

Leith | 2019-02-03 12:56:40 UTC | #7

I respect your opinion, and will consider your words, but I am still leaning towards an experiment in subtractive lighting. I agree that baked GI looks great, but it tends not to mix well with dynamic lights. I'm feeling torn, as the trade-off is not all bad, I just don't like the bloom when we add dynamic lighting to a baked lit scene, and feel that negative lighting might offer an alternative to conventional lighting that has currently been overlooked. It could be as simple as adding a SIGN to our lights, telling the math in the shader to add or subtract based on the sign of the brightness.

-------------------------

Leith | 2019-02-06 05:46:38 UTC | #8

Yeah its a horrid codec, but I can see beyond the noise.

-------------------------

Leith | 2019-02-06 05:47:54 UTC | #9

I forgot to mention that regular lights could work in the same environment as dark lights, so we don't need a crapload of lights, we just need to place them and weight them carefully.

-------------------------

Dave82 | 2019-02-06 06:18:26 UTC | #10

I remember using this method back in 2006-2008 working on fps levels to simulate global illumination and bake lightmaps.

-------------------------

Modanung | 2019-02-06 08:04:45 UTC | #11

[quote="Leith, post:8, topic:4885, full:true"]
Yeah its a horrid codec, but I can see beyond the noise.
[/quote]

What I meant was the codec is so horrid it _hides the SSAO grain_, which is most visible around **~35s**.

-------------------------

Leith | 2019-02-08 06:23:34 UTC | #12

at 35s, the camera is behind a wall, outside of the lit area, so its pretty understandable, we're just getting ambient light there, no other lighting, direct or indirect
It would have helped if that wall had a hole in it, since I assume its in the same ambient zone.
We'd be able to see light pouring into that area, and be able to judge the lighting more fairly.

-------------------------

Modanung | 2019-02-08 09:12:49 UTC | #13

I meant the moment the camera goes back into the light. For about one or two seconds there's a heavy grain which seems familiar from Blender's Cycles when rendering with a low amount of samples.

![SSAOgrain|411x500](upload://73wtrwnBImIvomv8FOnh7CmAIow.png)

-------------------------

Dave82 | 2019-02-08 10:47:37 UTC | #14

And when he moves the light left/right you can see the light calculation is not instant ! There is some sort of interpolation between the current frame and the previous. It seems that he uses a technique of distributing the GPU intensive calculation into frames so he can have very high quality result on acceptable speed.
Interesting idea.

-------------------------

Leith | 2019-02-11 06:57:22 UTC | #15

Today I was informed that signed light intensity is perfectly ok - the dark lighting experiment is on, I just need to finish up my current work on animation blending first.
Conceptually, it means that ambient lighting should be raised from (20 percent?) to 50 percent, and we use both positive and negative lights in our scenes.

-------------------------

