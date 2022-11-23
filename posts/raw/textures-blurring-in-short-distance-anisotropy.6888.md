evolgames | 2021-06-11 03:11:20 UTC | #1

In the screenshot I have simple 1x1x1 Cubes (about 3 in the shot) with a repeating grid texture on them. I can't seem to figure out how to get rid of this blurring. I'm not sure if it is a mip map, anisotropy, or texture filtering. I don't mind it, but it's happening way too soon for the proximity of the camera. At a farther distance, this is fine. How can I get crisper textures up close? I don't currently have any fancy renderpaths. I tried setting the texture to filter_nearest as well as adjusting Anisotropy. Is this a mip map thing? 

![Screenshot_2021-06-10_22-42-12|690x388, 75%](upload://fmC1TK0Ku4Lbp1Pq5HKfN70hzGz.png)

-------------------------

SirNate0 | 2021-06-11 03:36:15 UTC | #2

I think it's probably a mip mapping issue since the line seems to get thicker when it gets more faded. You could try forcing it to use the lowest mip map level, or try a thicker line in the base texture, maybe with a gradient on the edge so any averaging becomes less noticable at distance.

-------------------------

evolgames | 2021-06-11 03:59:53 UTC | #3

Oh okay. Well the materials has a 
single simple PNG texture so no mip mapping is set. Is Urho auto-generating them? I recall some automipmap export function in Gimp. Maybe that'll help

-------------------------

weitjong | 2021-06-11 04:31:33 UTC | #4

Have you tried to disable the mipmap? You can create a matching xml file at the same resource folder where your PNG is being loaded from, and specify extra instructions there. See example usage in the UI.png and UI.xml from the Urho3D project provided texture folder.

-------------------------

Eugene | 2021-06-11 09:25:34 UTC | #5

[quote="evolgames, post:1, topic:6888"]
I’m not sure if it is a mip map, anisotropy, or texture filtering
[/quote]
TL;DR: Increase anisotropy until you like how it looks.

Both trilinear texture filtering (filtering between different mips) and anisotropy contribute to this behaviour.

If you have anisotropy off (anisotropy=1), rasterizer will always pick smallest mip level. I.e. if you squish 1024x1024 texture vertically 4 times (via scale, or due to projection), rasterizer will use 256x256 mip level. It introduces unnecessary blur along largest axis (x axis in your case). Rasterizer **has** to pick smallest mip level because otherwise there will be noise on the smallest axis (y axis in your case).
So, if you disable mips or mip filtering, you will get less blur and more noise.

If you want to have less blur without having any noise, you have to increate anisotropy level. In the example above, rasterizer will work as if sampling 1024x256 texture (if anisotropy=4): rasterizer will remove noise without any unwanted blur. It will cost you some performace of course.

-------------------------

evolgames | 2021-06-11 14:33:29 UTC | #6

Ok so here's what it looks like with this texture xml:
```
<texture>
    <filter mode="nearestanisotropic" anisotropy="4" />
    <mipmap enable="false" />
    <quality high="2" />
</texture>
```
![Screenshot_2021-06-11_10-08-05|690x388, 100%](upload://1we1cyvkra7wUQliBLZyzGJaQkU.png)

and with mipmaps enabled
![Screenshot_2021-06-11_10-08-49|690x388](upload://uqeQNMLI0HwyEhHFXZe0rjZxjrH.png)

I see what you mean about noise. I should note that no textures are squeezed or stretched, all are on 1x1x1 cubes. Looks like switching from trilinear to nearestanisotropic was what made the most difference in my case.

-------------------------

Eugene | 2021-06-11 16:42:57 UTC | #7

[quote="evolgames, post:6, topic:6888"]
that no textures are squeezed or stretched, all are on 1x1x1 cubes.
[/quote]
I mean that if you look tangentially at the surface, it becomes squeezed in screen space.

All blur related to non-uniform texture scaling can only be solved by anisotropic filtering of some kind.

-------------------------

evolgames | 2021-06-11 17:05:18 UTC | #8

Oh okay that makes sense. Well, it looks better. I'll continue playing around with it. Thanks everyone

-------------------------

Modanung | 2021-06-11 20:02:57 UTC | #9

As it is now, it would be pretty easy to replace the texture with a custom shader.

-------------------------

evolgames | 2021-06-11 22:01:04 UTC | #10

Wouldn't that be more expensive? I plan on all blocks being able to have custom colors.

-------------------------

Modanung | 2021-06-12 00:33:53 UTC | #11

I think it would be somewhat cheaper actually, depending on the implementation and how you measure.
If all that varies is the colour, you could use the diffuse or vertex colours for that.

-------------------------

evolgames | 2021-06-12 01:06:40 UTC | #12

Well that's interesting. I'm terrible at shader code though. This would be really useful to quickly get non-dull cubes in any game.

-------------------------

Modanung | 2021-06-12 08:41:36 UTC | #13

My experience with this is limited as well, but sufficient to imagine how one might achieve this result.
I'll PM, as this is getting somewhat off-topic.

-------------------------

