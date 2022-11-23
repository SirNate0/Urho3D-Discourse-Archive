Bananaft | 2017-07-17 20:48:22 UTC | #1

Lately I was playing with raymarching and 3d-fractals. I came up with the method to optimize raymarching and implemented it in Urho. I also added volumetric light scattering for point and spot lights. Taking from this demo: [blog.mmacklin.com/2010/05/29/in-scattering-demo/](http://blog.mmacklin.com/2010/05/29/in-scattering-demo/) and using some ugly hackery to make it work with finite attenuation lights (it uses inverse square fore light attenuation ).

Requires modern GPU.

[b]Screenshots and download:[/b]
[bananaft.itch.io/yedomaglobula](https://bananaft.itch.io/yedomaglobula)

Follow me: [https://twitter.com/Bananaft](https://twitter.com/Bananaft)
<img src="https://pbs.twimg.com/media/CxGTKmZXAAArA7w.jpg">
<img src="https://pbs.twimg.com/media/C5iHAUnWAAAY5AC.jpg">

-------------------------

theak472009 | 2017-01-02 01:15:13 UTC | #2

Looks freaking amazing man. Reminds me of those ShaderToy fractal demos.
Any chance to get the C++ source code or is it all done in shader code?
Edit: Found the code in Angelscript.

-------------------------

ghidra | 2017-01-02 01:15:14 UTC | #3

super cool.
The lights look great. Are you also building collision objects for that character to stand on?

I did some similar work a while ago.. but I never took it as far as you have:
[topic1682.html](http://discourse.urho3d.io/t/fractal-shader/1619/1)

-------------------------

dakilla | 2017-01-02 01:15:14 UTC | #4

nice, I love fractals

-------------------------

Lumak | 2017-01-02 01:15:15 UTC | #5

I like the lighting effect.  Awesome demo.

-------------------------

Bananaft | 2017-01-02 01:15:15 UTC | #6

Thank you all for feedback. So it actually works :slight_smile:. Forgot to ask, I really want to know what hardware you have and what performance you are getting?

[quote="theak472009"] Reminds me of those ShaderToy fractal demos.[/quote]
My go to source.

[quote="theak472009"]
Any chance to get the C++ source code or is it all done in shader code?
[/quote]

With this project I've made my first baby steps in C++. Whole raymarching thing is purely glsl and renderpath.xml. But I had to disable Z-culling for light volumes, to make them work with raymarching result. Also I passed couple additional  shader parameters for light scattering of spotlights. That's like 5-6 lines changed.

[quote="ghidra"]Are you also building collision objects for that character to stand on?[/quote]
No, I just placed him there :slight_smile:. I haven't tried collisions yet, but I will. Mesh is not an option, I have to calculate SDF for collisions either on GPU or CPU, both ways seems terrible. CPU will require to write code twice, keep it same, and may still give different results (in theory). GPU has problems with bringing information back to CPU to update objects.

-------------------------

vivienneanthony | 2017-01-02 01:15:16 UTC | #7

I wonder if a Linux version can be built. :-/

-------------------------

dakilla | 2017-01-02 01:15:17 UTC | #8

just put the linux binary player in the folder and run it.
it works partially, I experimented somes bugs...

-------------------------

Bananaft | 2017-01-02 01:15:17 UTC | #9

[url=https://github.com/urho3d/Urho3D/compare/master...Bananaft:master]Here is my fork and all the changes.[/url]

-------------------------

franck22000 | 2017-01-02 01:15:17 UTC | #10

Very nice demo ! 

Do you think you could make a pull request in Urho3D master branch for adding this volumetric effect support to point and spot lights ? That would be awesome.

-------------------------

Bananaft | 2017-03-05 22:50:01 UTC | #11

Hi, sorry for long reply.

I never did a pull requests, might use an assistance, and my coding style is a bit savage.

Also, it works easily only with deferred lighting, other modes will need an additional light volumes pass, witch is not cool.
Plus, this light scattering should somehow interact with fog, and trying to resolve this will rise many complicated questions.

-------------------------

Bananaft | 2017-04-15 22:04:03 UTC | #12

The new version features four different fractals, smoother lights scattering, cubemap sky and colored ambient occlusion, and some more minor tweaks.

https://bananaft.itch.io/yedomaglobula

-------------------------

Modanung | 2017-04-16 13:17:33 UTC | #13

So cool...
Unfortunately the misspelling of a certain resource prevents me from pouring the submarine some _tea_.

-------------------------

Bananaft | 2017-04-17 16:55:34 UTC | #14

What do you mean? Is there an error, it won't load or something?

-------------------------

Modanung | 2017-04-17 17:16:06 UTC | #15

Yea, it's looking for a Teapot where there only is a TeaPot.

-------------------------

Bananaft | 2017-04-18 10:22:23 UTC | #16

So you've built Linux binary from my brunch? How does it work? What GPU do you have?

-------------------------

Modanung | 2017-04-18 11:44:10 UTC | #17

I ran the game.as with a natively built Urho3D player. It's a simple naming issue fixed by changing line 234 of game.as from:
```
tpObject.model = cache.GetResource("Model","Models/Teapot.mdl");
```
to:
```
tpObject.model = cache.GetResource("Model", "Models/TeaPot.mdl");
```
...damned alternative spellings. ;P

-------------------------

Bananaft | 2018-04-29 21:00:08 UTC | #18

New video.
https://www.youtube.com/watch?v=FU-8j4sr3LY

-------------------------

Eugene | 2018-04-30 11:34:32 UTC | #19

Fractals are goddamn amazing. How the physics is implemented?

-------------------------

Bananaft | 2018-04-30 13:17:35 UTC | #20

Everything has to be sphere approximated. Character controller uses 2 spheres. Submarine uses 3. It's calculated with pixel shader. I use small 16bit textures to pass data to and from GPU. Position and radius is sent to GPU, distance and normal(estimated with given radius) are sent back. It is not very accurate, but with signed distance you can do soft collisions

-------------------------

johnnycable | 2018-04-30 19:52:42 UTC | #21

Nice. What kind of monsters are going to put in there?

-------------------------

Bananaft | 2018-05-01 21:07:32 UTC | #22

don't know yet. Will see. It won't be a shooting gallery though.

-------------------------

johnnycable | 2018-05-02 09:35:23 UTC | #23

What about _the dreaded [l-system](https://en.wikipedia.org/wiki/L-system) monster_?

![06|583x500](upload://lczCBrtVZHCFTgDEDCZaoOMDnNC.jpg)
_(the monster in a rare shot)_

The foul creature is renowned to live in such abysses like the ones you depicted. It feeds on unfortunate travelers looking for uncommon sources.
It is made of crystal/rocky (ehr, boxes is this shot) formations which can take the shape of many things like, obviously, different fractals kind.
You only need a formula, a fractal shape (which you substitute for the boxes), a auto-generated skeleton for movement, placement in sentive context.

![27|489x500](upload://mwpXk4G7N38ZFpYqDvF1bzhj4iY.png)
(_matrices paths for object substitution and skeletonizing_)

Easy creation with Sverchok generative design in Blender:
![48|679x500](upload://1Om2Td5YPDYrBlp8p6gFFw3Puwb.png)
just substitute Box for whatever

[get the blend](https://drive.google.com/open?id=1z2cw7wBgDu-GXQuJ1JvtSccjcPChDECf)

A heightened study on the subject: [LTM notes by Elfnor](http://elfnor.com/generative-art-sverchok-node-update.html)

-------------------------

Bananaft | 2018-10-02 14:06:59 UTC | #24

I wrote a devlog-story. It is mostly about graphics features and visuals.
https://medium.com/@bananaft/my-journey-into-fractals-d25ebc6c4dc2

-------------------------

Bananaft | 2018-10-02 17:34:07 UTC | #26

Thank you. My plan is to first try it at small platform like itch or humblewidget and then move to big ones.

-------------------------

Bananaft | 2019-10-02 16:24:28 UTC | #27

New build is available.
https://bananaft.itch.io/yedomaglobula

-------------------------

