lheller | 2019-03-06 08:26:08 UTC | #1

Hi!

Is it possible somehow add a spot light inside a sphere and make the sphere act like a light source?

Edit: Point light! :wink:

-------------------------

I3DB | 2020-04-27 07:16:27 UTC | #4

It seems to me it should work putting a point light inside a sphere. But I'm a beginner and don't know.

You can use emissive material and bloom and bloomhdr to make the effect more dramatic and noticed.

I sure wish people would answer questions instead of going off on tangents unrelated to the question. It makes this board useful for those to come in the future who are trying to solve problems. Movie comments make me want to look elsewhere and not on this board.

Here's an example, note the DiffEmissive. This is with a lit material and light outside the sphere.
![PNG|544x500](upload://pBBLHQNdQRgeXnUNItLXi8By6Qa.jpeg)

Also [check out the billboards sample and the use of lights](https://urho3d.github.io/samples/07_Billboards.html).

-------------------------

Modanung | 2019-03-05 22:34:52 UTC | #5

@lheller Do you mean area lights or would a light mask (or even near clip) be enough?

-------------------------

Dave82 | 2019-03-05 22:34:32 UTC | #6

Create a node and add a StaticModel and a Light component to it. For the staticModel use Sphere.mdl resource and that's about it.

-------------------------

Leith | 2019-03-06 08:01:16 UTC | #7

Why would you put a spotlight (which has Direction) inside a sphere, then try to model a spherical light, when a point light represents a light with "all" directions (a spherical light)?
Are you looking for a spherical light which is more intense in a particular direction?
I'm confused :)

If I'm right about your wanting to model a spherical light which is more intense in some direction, you could try combining some basic lighting models - first try mixing a directional light with a spherical light, and if it's not good enough, try mixing a spotlight, and a spherical light, connected to the same parent node (so having the same world position).

-------------------------

lheller | 2019-03-06 08:21:50 UTC | #8

What I want to reach is to create something like a star (a celestial object).
As we know, star is a light emitting object.

Anyway, the below works well without any light (UrhoSharp code):

    var sphere = StarNode.GetOrCreateComponent<Sphere>();
    var material = Material.FromColor(Color.White);
    material.CullMode = CullMode.None;
    material.LineAntiAlias = true;
    material.SetTechnique(0u, CoreAssets.Techniques.NoTextureVColAddAlpha);
    sphere.SetMaterial(material);

Anybody a solution with point light?

-------------------------

lheller | 2019-03-06 08:24:41 UTC | #9

Hello, yep, point light is what I want here.
But see my "solution" without any light.

-------------------------

Leith | 2019-03-06 09:42:21 UTC | #10

I like pictures - even bad ones - pictures are more clear, generally, than a thousand words - please show me what you see, and just after that, describe again what your goal is, I will try to do it in my project just to make sure it works before i reply.

-------------------------

lheller | 2019-03-06 10:19:47 UTC | #12

My goal is something like this:
![image|690x447](upload://1aU78f9RTSdhkjAIXrXrXjr0PA5.jpeg) 

I am developing a planetarium application where I also want to simulate the star [magnitude](https://en.wikipedia.org/wiki/Magnitude_(astronomy)).
The idea is to render small spheres with point light inside where the light range/brightness is set based on star magnitude value.

-------------------------

Leith | 2019-03-06 10:47:52 UTC | #13

stop using spotlights, switch to point lights, you'll be fine, and I'm here to help

-------------------------

guk_alex | 2019-03-06 11:18:28 UTC | #14

Question regarding these lights: do you need these starts to light some objects near it (planets and so on)? Or do you only need the starts only?
If you do not need to light any object by these starts and you just want this bloom effect around the spheres than you don't need any light source inside the spheres (and you will save a lot of performance) -  only special material is required for these starts and bloom post-processing effect.

-------------------------

lheller | 2019-03-06 11:23:05 UTC | #15

I already switched to point lights.
But now I think @guk_alex suggested a better solution.

-------------------------

lheller | 2019-03-06 11:25:00 UTC | #16

Hello @guk_alex 

No, I don't need to light near objects.

Can u pls give a short example only with one sphere and such material and that bloom effect?

-------------------------

Leith | 2019-03-06 11:25:29 UTC | #17

many hands, make light work

-------------------------

guk_alex | 2019-03-06 11:33:07 UTC | #18

I3DB mention it here: https://discourse.urho3d.io/t/sphere-as-light-source/5000/4?u=guk_alex
Material you looking for is DiffEmissive. And the effect is Bloom or BloomHDR.

-------------------------

Modanung | 2019-03-06 14:04:42 UTC | #19

If your stars remain without texture you might as well use [billboards](https://github.com/urho3d/Urho3D/tree/master/Source/Samples/07_Billboards) instead of spheres for maximum performance.

-------------------------

lheller | 2019-03-06 14:18:46 UTC | #20

@Modanung 
OK, but how to make one billboard component look like a sphere (or at least a circle) ?

-------------------------

Modanung | 2019-03-06 17:26:22 UTC | #21

Simply assign a material with a circle as texture - which can be made in a few clicks using [GIMP](https://gimp.org) - and some unlit or additive _Diff_ technique to the billboards.

-------------------------

lheller | 2019-05-17 13:24:47 UTC | #22

@Modanung

Did it, and used DiffAdd technique for billboardset's material.
But unfortunately only some of the circles are glowing. Like on the screenshot. 
![image|690x447](upload://yhMaDuYzA9CWtx8nVNP9SGqFx7D.png) 

I need all the circles glowing.
Any idea?

-------------------------

Modanung | 2019-05-17 20:38:04 UTC | #23

Maybe you could incorporate the glow into the circle image? Or use two billboards per star, one unlit opaque and one additive.

-------------------------

lheller | 2019-05-20 20:20:08 UTC | #24

@Modanung

Two billboards per star finally solved the problem: All circles are glowing!

But now there is another question (problem?): I need various colors for circles, in other words for each billboard in billboardset. Is it possible to do this for the same billboardset?

-------------------------

Modanung | 2019-05-20 20:28:28 UTC | #25

Yes, this is perfectly possible by using vertex colors. Simply set the billboards' `color_`s and then `Commit()`. Make sure your textures are in grisaille - since it will be *multiplied* with the vertex color - and the materials' techniques should be VCol ones.

-------------------------

lheller | 2019-05-21 08:17:36 UTC | #26

@Modanung

Thanks for help, now everything works as expected!

![image|690x447](upload://82DR4Wz90zUIKwc8cmwAt5rQelt.jpeg)

-------------------------

GoldenThumbs | 2020-01-23 19:42:21 UTC | #27

This solution seems really inefficient to me. Do the stars *need* to additivly blend for some reason? Why not just use alpha scissoring and an emissive texture? Sorry to necro an old thread BTW, but this seems like a really silly solution, unless there is a particular reason it needs to be done like this.

-------------------------

GoldenThumbs | 2020-01-23 19:46:12 UTC | #28

Heck, you just need one texture used in both albedo and emssive and to use the DiffEmissive technique, though ideally it's an unlit technique which has a strength float to multiply the diffuse color by. Actually shouldn't be hard to make. I'll do it RN.

-------------------------

lheller | 2020-01-23 19:58:47 UTC | #29

Hi!

Please if you can provide an example code (and also a texture),  I would appreciate it.

BR,

Ladislav

-------------------------

GoldenThumbs | 2020-01-23 19:59:12 UTC | #30

Already working on it lol.

-------------------------

lheller | 2020-01-23 20:00:22 UTC | #31

What I need is to make stars glowing like on the above screenshot.

-------------------------

GoldenThumbs | 2020-01-23 20:01:02 UTC | #32

And you are using HDR, right?

-------------------------

lheller | 2020-01-23 20:02:31 UTC | #33

Using BloomHDR, yes.

-------------------------

GoldenThumbs | 2020-01-23 20:03:01 UTC | #34

Ok, good. That means I'm right about this then. Next post will be a video of what I do.

-------------------------

GoldenThumbs | 2020-01-23 20:10:13 UTC | #35

Ok, breaking my promise, but I remember there being a bug with a few of the post effects, including both bloom variants (LDR & HDR) where the naming of some of the uniforms was messed up in the post effect XML. Is this fixed currently? If not I'll just fix it myself (it's honestly a pretty simple issue to remedy) but if it is fixed I want to make sure the build of the engine I'm using has these fixes. @Modanung You'd probably know.

-------------------------

lheller | 2020-01-23 20:14:24 UTC | #36

Anyway, you are still welcome to post a super efficient and fast way to produce glowing stars like on the above screenshot :blush: 
BTW you also think, the BillboardSet is the best way ?

-------------------------

GoldenThumbs | 2020-01-23 20:17:24 UTC | #37

Yes. Instead of rendering a sphere which has, at least 8 tris, a billboard is a quad which is 2 tris. I've done some experimenting in another engine with shading a billboard to make it look like a 3D object.![SPHERE|683x500](upload://vxYRAYVrvXO6lkOn99Eh3tQ5rwD.png)

-------------------------

GoldenThumbs | 2020-01-23 20:21:22 UTC | #39

I found the issue on github, it's not fixed. https://github.com/urho3d/Urho3D/issues/2542

-------------------------

Modanung | 2020-01-23 23:05:02 UTC | #40

@GoldenThumbs Maybe you could review the PR?
https://github.com/urho3d/Urho3D/pull/2546

-------------------------

GoldenThumbs | 2020-01-24 03:28:05 UTC | #41

https://www.youtube.com/watch?v=gOG2Vy-66gY so this is what I got to before I fell asleep, but I'm going to try to make the bloom look better.

-------------------------

GoldenThumbs | 2020-01-24 04:00:24 UTC | #42

Ok, so all the shader stuff I did seems to be pointless. You get the same result with the bloom even if values above 1 are used. HDR stuff doesn't seem to effect BloomHDR, from what I can see at least... So, in conclusion, just use an unlit material. That's it. I'd still use "ALPHAMASK" in the pixel defines, unless you want some gradient effect with alpha.

-------------------------

GoldenThumbs | 2020-01-26 11:10:28 UTC | #43

This does kind of lead to a question... Why use bloom at all? Why not just use a circular gradient with an unlit material and alpha blending? ![grad_sphere|500x500](upload://9xMTuweL2LNpC0hBnpzemw5MakQ.png)

CORRECTION! Turns out HDR Rendering was turned off in my test, I turned it on and everything worked like it should. https://github.com/GoldenThumbs/Urho3d_HDR_Glow/tree/master/CoreData/Shaders

-------------------------

lheller | 2020-04-27 19:39:45 UTC | #44

If anybody is interested, how I did, then here are the steps:

1. Loaded the material from image (Circle.png).
2. Set technique for material to **DiffVColAddAlpha**.
3. Generated an array of positions for circles (billboard in the set).
3. Create a billboard set with number off billboards **two times** as many as the required visible circles.
4. Iterated through the array of positions and set the current position for (2n)th billboard and at the same iteration also set the same position for (2n+1)th billboard. In other words, at the same position there are always two billboards from billboardset. 
5. Set size and color for current billboard and enabled it.
6. Commit.
7. Added **BloomHDR** postprocess effect.

Example animated 3D starfield with glowing stars:
https://youtu.be/kaD0aVXVObA

-------------------------

pldeschamps | 2021-01-17 20:20:28 UTC | #45

[quote="lheller, post:44, topic:5000"]
Set technique for material to **DiffVColAddAlpha** .
[/quote]

Thank you, this is what I was missing to give different colors to each Billbord item.

-------------------------

