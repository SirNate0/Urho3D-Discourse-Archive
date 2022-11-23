evolgames | 2020-09-02 22:17:04 UTC | #1

Simple discussion question with perhaps a complex answer. I'm just curious how u3d is able to run so much smoother and faster than other engines/applications/games.
The more I use it the more I understand it. And the more I understand it the more I like it. It just works. I don't know much about low-level graphics rendering and all that. I know just know some of the basics.

I'm getting a new laptop tomorrow (with a discrete gpu). Long story short I've been on a bottom-of-the-barrel laptop for the last 3 years (good one broke) with only integrated graphics. However, the silver lining is being forced to learn efficiency. I'm continually impressed with just how much I can do with urho that I can't even dream of otherwise. I can hardly load a unity sample at all whereas I can make a 3d urho game and 1000 trees doesn't put a dent in my 60fps, on top of a huge terrain, navmesh, bloom and npcs. I can't play regular 3d games but I can make them?

What's going on here? Is there a benchmark of 3d engines that explains this? Or is it just that scenes in urho are initially and inherently lightweight? Or are the majority of games/engines just being lazy because the hardware can take it? Or is it because urho uses .mdl binary models? This is really interesting to me, and I'm sure I would have overlooked/not noticed urho's speed if I had a better computer. I'd like to read up and understand this more. Someone point me in the right direction here.

-------------------------

Lys0gen | 2020-09-03 00:03:16 UTC | #2

Modern computers, yes even mediocre laptops from a couple of years ago, are incredibly fast. And yes, Urho3D is comparatively lightweight while Unity is incredibly bloated. Unity carries a lot of baggage which most devs don't even need for their specific project (though if you do, it is of course useful that you don't have to code it yourself) but that comes at a cost.

That said, I'm not sure if your benchmarks are equal. Rendering the same tree model 1000 times is probably much faster than just 50 different models (due to batching). Don't know if you put unity to the same test there.

Personally, I'm far more impressed by 90s/early 2000 games... I'll never understand how games like Morrowind ran smoothly on my 800 Mhz CPU with 256 mb RAM.

-------------------------

evolgames | 2020-09-03 00:33:00 UTC | #3

Hmm, makes sense to me.
Yeah I didn't do any equal testing between the two. More just personal realizations. It's clear though that Urho is far faster. Maybe I'll do a little test of both of them and compare framerates of the same static scene with a skybox, light, character controller, etc. I recall godot being faster than unity but also slower than Urho. I do feel that with Urho my scenes only have the bare minimum of what I need.

I think a lot of indie devs/games must be unnecessarily overbloated, then. I don't know what's being left out here feature/bloatwise, but whatever it is I haven't noticed. I'm picking on Unity here but it is a little ridiculous that every 2d unity web player game is nearly unplayable meanwhile I can do the urho physics stress test web sample no problem. I guess the devs don't strip things down, or there isn't an easy way to...

Oh yeah, those old games had some impressive feats. I guess they had to push things to the absolute limits. Apparently games like crash bandicoot hacked the playstation for more memory or something weird like that. I guess none of those older games had fancy lighting or did much raycasting, either.

-------------------------

jmiller | 2020-09-03 05:15:16 UTC | #4

Makes sense. And I gather that valuable experience from other engines were applied in Urho's design and over its evolution, with performance a consistent goal (I thought it is also noteworthy how well the docs point out quality-performance choices :) ) with fast shadows implementations, shaders profiled, community attention and tweaks over years, and others can go into a lot more detail there.
 :tropical_fish:

-------------------------

UrhoIsTheBest | 2020-09-03 06:36:25 UTC | #5

Did you run unity game from the editor or compiled binary? I think those editors are super bloated too.

I am exactly in the same situation as you. I have a 2014 personal macbook that I've been coding for the past few years. I use another macbook for work too, haven't touched any high end PC with reasonable GPU for quite some years.
When I started looking for a game engine for my personal hobby, I tried many things out there. Unity is usable but very laggy when the project gets large. Unreal cannot even start because it says my macbook < hardware minimal. I used godot for a while too, but could not get used to the editor and script language there. I am too old that I cannot work with a coding editor without vim support. I've been dreaming to see a lightweight game engine that I can just use CLion to write code and compile/run to see the game. I don't need any mouse drag/click in those editors (I don't even use mouse actually, only one for testing the game). I just want pure coding environment that I can configure into my comfort zone.

Also I am sick of most of current AAA games that put too much efforts on visual effect while not much improvement in game playing. I don't remember any recent games that I played more than a few hours. All my good memory about games are from early days. I would focus mainly on game play for my game and would only need basic visual. For indie project, artist is too expensive anyway.

And Urho3D is the only choice for me.

-------------------------

Eugene | 2020-09-03 09:34:10 UTC | #6

[quote="evolgames, post:1, topic:6366"]
What’s going on here? Is there a benchmark of 3d engines that explains this? Or is it just that scenes in urho are initially and inherently lightweight? Or are the majority of games/engines just being lazy because the hardware can take it?
[/quote]
My best bet is that Urho is faster because it's doing less, both in terms of computation and abstraction.
It's kind of obvious, when you think about it. The more things the engine performs, the slower it works.

Urho has very simple default shaders, Unity has much more complicated default shaders.
Urho has rough navigation over simplified navmesh, Unity supports height mesh for precise positioning.
If I remember things right, Urho has default PCF shadow quality 2x2, Unity has default PCF quality 5x5. Better shadows, costs more.
The same scene with default settings is bound to be faster in Urho than in Unity due to different amount of computations required.

Abstraction costs are also important. If you want to renderer 100k simply-lit cubes, plain OpenGL will do _much_ faster than any engine. However, if you want some flexibility of settings, you have to pay some performance for higher level of abstraction.
Unity has more built-in features than Urho and it supports more GAPIs, therefore it requires higher level of abstraction and inflicts bigger penalty on performance.
Urho is 100% native (if we ignore optional scripts), Unity can be compiled for all platforms at once thanks to C# scripts, and this abstraction is also paid by performance of user logic.

-------------------------

evolgames | 2020-09-03 16:57:24 UTC | #7

Oh I just ran one of the Unity samples through their editor vs the urho lua samples. I don't use Urho's editor anyway, but it's definitely snappier.

I totally get that perspective. There's plenty of older, objectively good games without the new, almost gimmicky, graphics. It's been years since I've actually played a game like I used to. The most I'll do is retro multiplayer with my brothers, which is more of a social event than a video game hobby (playing C&C and Halo 2). I'm just not interested in the new things coming out, which I'm not sure is an age thing or just that I prefer the older games/nostalgia. Maybe a little of both. Making them is much more fun and productive, though. I would say that for new games, indie games are more engaging, possibly because they don't stick to any formulaic scripts and you can end up with really unique and imaginative gameplay.

I think everyone has their habits and ideal setup. Urho's editor looks really easy to use but I just feel more comfortable scripting everything, even if it doesn't really make sense to. I just use a text editor (geany) and set a keyboard macro to run the current project as is (no compiling). The nice thing about a more minimal engine is using only what you need. And in most of our cases (I suppose), we aren't interested in AAA effects/features anyway. Also, it's interesting that AAA is considered always better by the masses whereas I see it as restaurant quality meals vs. homemade food (indie). You might have more things going on but you can't replace charm.

@Eugene ahh okay! I appreciate the specifics. That's really interesting. Well, what we get with Urho is plenty and "good enough" for me. I get why a serious studio would want a more established engine, especially for distribution. I wonder if I'll ever reach a point where I need any of the extra stuff.

-------------------------

George1 | 2020-09-04 04:57:40 UTC | #8

From my experience when I started, which was a few years ago.
I have tested Unity, Irrlicht, Ogre3d etc.  
Urho3d was the fastest when handling large number of objects.

Not sure how optimized other engines are today.

-------------------------

Modanung | 2020-09-04 08:27:30 UTC | #9

[quote="evolgames, post:1, topic:6366"]
What makes Urho3d so much faster?
[/quote]

@cadaver did. :slightly_smiling_face:

-------------------------

QBkGames | 2020-09-08 02:00:46 UTC | #10

As Eugene said, Urho3D would be fastest (especially on older hardware) because it is more lightweight and has simpler shaders and architecture (which is also incredibly useful for people trying to understand how an engine works). 

However, once Unity finishes implementing their new Jobs based ECS (Entity Component System), it could end up being the fastest engine on Earth. They did a demo 2-3 years ago where they showed 100000 entities on screen at the same time running at 60 fps (probably on high-end HW, but still impressive). 

Also, the new version of Ogre3D (2.1 or so) is also based on a similar design, therefore it might now be much faster than Urho3D (though I haven't tested it to know for sure). The major problem with Ogre3D is that it's not an engine, it's just a rendering library, whereas Urho3D has all the features you need to complete a game (if you don't need very sophisticated graphics that is).

-------------------------

evolgames | 2020-09-08 19:27:40 UTC | #11

Well I guess that makes Urho a good choice for me for the foreseeable future. At this level the lightweight shaders work great for me. If I ever start up a studio with employees, I suppose a AAA approach would make more sense, especially to get a more polished look with fancy effects. Last I remember, Unity was thinking of or has implemented Vulkan, which I know to be faster than opengl.
Again, I don't know much about lower level stuff but from what I understand Urho exclusively uses opengl, and has yet to take advantage of Vulkan? Might be interesting for the future. At the moment my graphics doesn't support it anyway. I did play around with it on a different machine and it was pretty cool to see in action.

-------------------------

