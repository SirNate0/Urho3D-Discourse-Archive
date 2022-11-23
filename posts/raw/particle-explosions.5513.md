suppagam | 2019-09-05 13:46:12 UTC | #1

I have started working with VFX in my game and, unfortunately, I have been hitting a couple of walls when it comes to particle systems in Urho. My particles always end up looking like the simple stuff in Unity:

![image|531x284](upload://ffr62wwm5Tcj2ljw75GzZ7mWwKy.jpeg) 

Does anyone have any examples of more elaborate systems in Urho?

Kinda like this: https://www.youtube.com/watch?v=c1yxdUGRr_o

-------------------------

codexhound | 2019-08-26 21:39:52 UTC | #2

I don't have concrete examples but for complicated systems you would need multiple emitters each with a different particle effect.

You could define a node : Node * particleSystemNode, and then attach multiple emitters to that node to accomplish this.

In that video example it seems he is using the unreal gui to accomplish the same. You can see he is using multiple emitters. To enable the system, enable the node. Maybe someone with more knowledge of the code base could answer whether it would be good to have a dedicated particle system class that does stuff like this for you or there is a better way of doing this.

-------------------------

Leith | 2019-08-27 11:39:56 UTC | #3

The only major limitation I see in Urho3D particles right now, is that they can't interact in the physical world. There is no way to enable physics sphere collisions, etc.

-------------------------

Modanung | 2019-08-27 13:32:22 UTC | #4

What would be a great addition is curves that define the progression of values for a single particle. I think this might not - or hardly - require modifying Urho's particle system, but rather a more advanced editor.

-------------------------

Leith | 2019-08-27 13:33:57 UTC | #5

I have had thoughts about curves recently too, our support exists, but its not great, I could use curves to modify the position of an agent moving across a navmesh offmesh link, but theres no easy way. We should support a range of basic curves, to support lerping in many forms

-------------------------

Leith | 2019-08-27 13:35:08 UTC | #6

In my case, I was thinking of portions of a great circle, but it could be just catmull rom

-------------------------

Valdar | 2019-08-27 15:10:05 UTC | #7

Have you checked out Dakilla's Github implementaion of Spark? Not sure if it's what you need, but maybe be worth a look.
https://github.com/fredakilla/Urhox
https://github.com/fredakilla/spkgen

-------------------------

suppagam | 2019-08-27 15:48:31 UTC | #8

That definitely looks cool! I think I might be having a hard time translating the "node graph" experience that I have with particles to code. Also, "edit, compile, run" is not a good flow for tweaking particles. Do you guys know a way of auto-refreshing particles so I can tweak the values and see the changes in realtime?

Also: How can I do those curves in Urho's particle code?

As for suggestion on how to improve: a small sample showcasing every property of a particle XML would be awesome. What does what. I think that's the hardest thing, going through and understanding how they come together.

-------------------------

Modanung | 2019-08-27 21:19:56 UTC | #9

The thought I shared was with high uncertainty. The furthest I got with particles was for [heXon](https://luckeyproductions.itch.io/hexon), which does nothing too complex... but I imagine combining [`AttributeAnimation`](https://urho3d.github.io/documentation/HEAD/_attribute_animation.html)s and particles more interesting things should be possible.
You may also be interested in the [`AnimatedBillboardSet`](https://gitlab.com/luckeyproductions/heXon/blob/master/animatedbillboardset.cpp) that I made for heXon and [OG Tatt](https://gitlab.com/luckeyproductions/OGTatt).
To quickly create texture animation frame data you can use [`anido`](https://gitlab.com/snippets/1860709).

-------------------------

suppagam | 2019-08-27 21:47:00 UTC | #10

Help me understand anido. With it, I can make particles that read from particle texture spritesheets like these:

![image|660x480](upload://6quxkVgvTTagp644vIoZAKN5R5w.jpeg) 

And it will animate AND apply the particle effect?

-------------------------

Modanung | 2019-08-27 21:54:39 UTC | #11

```
frode@Anvil ~ $ anido 2 3 .5
<texanim uv="0.000 0.000 0.500 0.333" time="0.000" />
<texanim uv="0.500 0.000 1.000 0.333" time="0.500" />
<texanim uv="0.000 0.333 0.500 0.667" time="1.000" />
<texanim uv="0.500 0.333 1.000 0.667" time="1.500" />
<texanim uv="0.000 0.667 0.500 1.000" time="2.000" />
<texanim uv="0.500 0.667 1.000 1.000" time="2.500" />
```

That's what it does. :slightly_smiling_face:
```
Usage
anido columns rows interval
    or
anido columns rows width height interval
```

The width and height should be normalized (between 0 and 1).

-------------------------

suppagam | 2019-08-27 21:53:58 UTC | #12

Holy crap, the sky is the limit now. I found out about this tool: https://www.popcornfx.com/ and I can export as spritesheets and i'll just use those instead.

-------------------------

Modanung | 2019-08-27 22:26:06 UTC | #13

I replaced the enemy in heXon that appears most frequent - the Razor - with pre-rendered animated, normal & emission mapped billboards. Coincidentally @extobias did something similar contemporary. 
https://discourse.urho3d.io/t/random-projects-shots/2431/119

`anido`  grew inside the source of OG Tatt when I _really needed_ it for the hood fire:

https://gitlab.com/luckeyproductions/OGTatt/raw/master/Resources/Textures/Flame2.png

That's a pre-rendered Blender fire simulation edited to loop, btw.
I think I was missing the feature to change the pivot, that's how I explain the inefficient use of texture area.

-------------------------

suppagam | 2019-09-04 20:15:16 UTC | #14

I found out that I can also export normal maps and specular maps from my particle simulations. I'm still trying to find a way to render DiffSpecNormal particles, but that might look awesome!

-------------------------

Modanung | 2019-09-05 13:45:44 UTC | #15

[quote="suppagam, post:14, topic:5513"]
I’m still trying to find a way to render DiffSpecNormal particles
[/quote]
What ways did you try without succeeding?

-------------------------

