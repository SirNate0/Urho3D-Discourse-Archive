LiamM32 | 2017-07-12 08:26:34 UTC | #1

The Urho3D front page lists support for Direct3D11 and OpenGL 3.2.  So does Urho prioritize Direct3D?  The OpenGL version is behind.

I know that OGRE 1.10 supports OpenGL 3.x, and I believe that OGRE 2.1 is OpenGL 4.5.
But does Urho perform better than Ogre 1.10 on OpenGL despite this?  Howabout Ogre 2.0, or 2.1?

The reason I'm asking is because I'm trying to revive an abandoned open-source game project; [Lips of Suna](https://gitlab.com/electric-gecko/lipsofsuna).  It uses a custom game-engine with Ogre.  I have been putting work into getting it to work with OGRE 1.10 (previously it was 1.9).

It's a pain having to work with an abandoned game engine with zero support. I don't even think it's such a great engine anyway. [Someone on a forum](https://forum.freegamedev.net/viewtopic.php?f=65&t=7487) suggested the idea of porting it to Urho3D.  After the initial work, this would be beneficial to the project if Urho really is well-suited.  But I don't want to go through all the work of doing that just to get _worse_ performance.

I read that Urho 3D is "Greatly inspired by OGRE and Horde3D".  Does this mean that those two engines were used as a design reference?  Is it likely that the new improvements in OGRE will come to Urho?

-------------------------

Eugene | 2017-07-12 08:58:42 UTC | #2

[quote="LiamM32, post:1, topic:3340"]
But does Urho perform better than Ogre 1.10 on OpenGL despite this?  Howabout Ogre 2.0, or 2.1?
[/quote]

How does version of GAPI related to engine performance?

I can't compare these engines but I've _heard_ that Ogre has design defects that lead to bad performance.
It'd be interesting to listen to someone expereinced.

-------------------------

slapin | 2017-07-12 14:41:02 UTC | #3

I remember Lips of Suna and like it very much. There is so much potential in it (both "old" version and
"new" version). If you start work on it please PM me and I'd like to help (if my qualification and time permits,
but I would really like to).

-------------------------

S.L.C | 2017-07-12 19:24:05 UTC | #4

I've only briefly been interested with Ogre3D a way back. Before the latest 2.x adventure. And from what I could grasp, Ogre3D was nice for hello-world applications but as soon as you began to scale a bit, you would've hit the issues of an old game engine design. And not to mention that Ogre3D is just a rendering engine. And while people call it a game engine, I fail to see all the components of a game-engine without third-party (_possibly outdated/maintained or soon to be_) libraries. And the worst of all, most of those third-party libraries are likely to each use a different design and you'll have to deal with integrating them into your game and adjust your style to each. Unless you're a good game-developer or part of team of good game-developers (_and I mean really good_). The best you can do with the engine are hello-world games, or simple games that look like they were taken from the 10'th place of a game-jam.

Compiling Ogre3D is(was?) another fun story. I don't know how that goes lately but I remember it being a bit daunting for anyone new.

And to be honest, I don't even know what critical part of OpenGL 4.5 is Ogre3D using. Most likely for some fancy feature that you're not even using. Like tessellation and whatnot. Basically, that number slapped on the engine is more like "_hey, you can use this version of open GL if you want or need (<- probably not)_".

Now let's bring up the rude/unfiltered part of me: If you couldn't be arsed to try out the engine and judge for yourself whether it would be sufficient for your needs. I highly doubt you'll be able to move forward with your project other than making these topics (_with either engine_). And most importantly: This is not the bottleneck you're looking for.

I'm not a game-dev, or consider myself as one, but I see these kind of topics online all the time. And most of the time, the project in question never reached further than the topic itself. You may think this is an un-polite opinion, but I'm just trying to be honest with you.

-------------------------

slapin | 2017-07-13 08:20:28 UTC | #5

Also if one hypothetically have found best OSS engine he/she wants to use, they might find some
other surprises. The problem is that an engine is a set of things like APIs. To even start the game one have to create engine for game based on these APIs, so it will be engine for your game, not something
abstract. And this phase might get so complicated that people really get overwhelmed and stop there.
Commercial engine make this stage a bit easier, but still there is a lot of things to handle which shocks unprepared minds.

About Ogre - could you please point some particular Ogre shortcomings, which you remember,
I mean most outstanding ones?

-------------------------

rasteron | 2017-07-13 09:15:24 UTC | #6

Maybe try porting over each other examples, particularly the benchmarking types then I guess you'll get your results.

-------------------------

George1 | 2017-07-13 15:29:08 UTC | #7

To me, this engine win the performance test in terms of rendering speed vs Orge3D.

-------------------------

Alex-Doc | 2017-07-13 20:14:43 UTC | #8

My two cents: if you are unsure about the engine choice, you have to reconsider your project too.
It would be weird to see someone build a house basing on the material of which his hammer is made of.
Each single engine, both commercial and open, have issues, game development has issues and it's not the rendering pipeline that fixes them.

About technical part, I moved from Torque3D (released, finished, 3+ years project) to Urho3D and the performances of Urho3D are really way better than Torque3D's. I've never really considered Ogre due to the need of a game engine and not just rendering.

On the practical side, I'd do as suggested above: try porting the demos and see how it goes.

Personally, I'd chose Urho3D over Ogre in any case, since Ogre would require me to do extra work which is already up, running and long tested by others (read as Audio, Physics, Navigation ...).

-------------------------

LiamM32 | 2017-07-15 01:47:20 UTC | #9

[quote="slapin, post:3, topic:3340, full:true"]
I remember Lips of Suna and like it very much. There is so much potential in it (both "old" version and
"new" version). If you start work on it please PM me and I'd like to help (if my qualification and time permits,
but I would really like to).
[/quote]
Thank you.  I am very glad to hear that, as so far I've been on my own with Lips of Suna.  I have gotten some advice on the [forum](https://forum.freegamedev.net/viewforum.php?f=25&sid=8c18189c8c0ebbff74661c6322c630b8), but no one else has bothered to edit the code themselves so far.  I am very inexperienced in C++ and programming in general, so this makes things very difficult for me.

I would PM you, but it looks like I can't.  I probably need to make more posts first.

Because I am so inexperienced in programming, I unfortunately don't even know where to start with porting it to the new engine.  It would be very, _very_ nice if you could start the task on your own.  I will try to assist where I can, but because of my limited skills I will probably end-up being more of a "director".  What I did so far was within reach for me, because I was pretty much just replacing deprecated OGRE functions with the recommended replacement.

There are multiple phases I have in mind for what should happen to Lips of Suna.  After changing the engine, the next step is to rewrite the Lua codebase in a better-suited language and in an easier coding style, while also taking the opportunity to make some functional improvements.

I don't know exactly how it would look to complete the "first phase" of the project, which is to change the engine.  Should we just get the older Lips of Suna 0.5.0 working with Urho3D (as Urho3D does support LuaJIT), and then start the next phase once that's done?  How do you think it should play-out?

I have more ideas regarding the direction Lips of Suna should go in, which I should sometime post the details of.

-------------------------

Alan | 2017-07-15 18:28:46 UTC | #10

[quote="LiamM32, post:9, topic:3340"]
I am very inexperienced in C++ and programming in general, so this makes things very difficult for me.
[/quote]
Why don't you go with something you're more familiar with? Unless you use a very limited engine with proprietary/exclusive scripting, some of your skills will be usable in other frameworks/engines. In the end it's useful knowledge overall and it's much faster to start with something you're familiar with and then go lower level than to struggle with something low level without understanding much of it.
That being said overall Urho code is very easy to understand compared to other engines out there.

-------------------------

LiamM32 | 2017-07-17 20:51:35 UTC | #11

[quote="Alan, post:10, topic:3340, full:true"]
Why don't you go with something you're more familiar with?
[/quote]
You don't understand.  There _isn't_ anything that I'm more familiar with.  The only exceptions are Game Maker (which I used to use many years ago, but only for simple 2D games), and Unity3D (which I did in a short programming class, but I can't use it for this, and don't really like it anyway).  The only programming that I can do comfortably is Arduino.

You clearly didn't see the full weight of what I meant when I said "very inexperienced in C++ and programming in general".


About what I mentioned above; Instead of a two-step process of porting Lips of Suna's current codebase and then rewriting the Lua in Angelscript, would it be better to just start writing it with Urho from scratch, using the old codebase as a design reference?

-------------------------

LiamM32 | 2017-07-17 23:20:46 UTC | #12

[quote="S.L.C, post:4, topic:3340, full:true"]
Compiling Ogre3D is(was?) another fun story. I don't know how that goes lately but I remember it being a bit daunting for anyone new.
[/quote]
Yeah, I had trouble.  I don't think I even managed to do it.
[quote="S.L.C, post:4, topic:3340, full:true"]
And to be honest, I don't even know what critical part of OpenGL 4.5 is Ogre3D using. Most likely for some fancy feature that you're not even using. Like tessellation and whatnot. Basically, that number slapped on the engine is more like "_hey, you can use this version of open GL if you want or need (<- probably not)_".
[/quote]
Actually, I believe that they're using it for the AZDO techniques possible with OpenGL 4.5.

Tesselation might be a nice feature to have at some point, actually.  At-least I want to have different _Level of Detail_ models that can be swapped out based on distance.

-------------------------

Eugene | 2017-07-17 21:32:36 UTC | #13

[quote="LiamM32, post:12, topic:3340"]
Tesselation might be a nice feature to have at some point, actually
[/quote]
Tesselation is overestimated, IMO. It may work nice for e.g. terrains, but for generic drawables it's less poverfull. You still need low-level lods for optimization, and only the best-quality-LOD can be aditionally tuned with tesselation (if you have AAA-level content, of course)

-------------------------

