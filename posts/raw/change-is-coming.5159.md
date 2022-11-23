Leith | 2019-05-18 08:46:31 UTC | #1

To quote the boss man : "What artgolf1000 writes is very true. Urho is mature in the sense that it has its way of doing things, and also quality / ease-of-use expectations are fairly high due to its history, which makes changing it in a large way challenging or undesirable. This is kind of unfortunate for its continued development."

Boss man also indicated to me that I was free to tear up and rebuild anything that stood in my way.
I do hope the machine does not stand against progress.

The more I work with Urho, the more small corners I see that could use polish, I am yet to meet a single frost giant. But change is inevitable.

-------------------------

JTippetts | 2019-05-18 23:16:01 UTC | #2

Only change I really care to see is a Vulkan rendering back end. Maybe see the EASTL fork go core, but that's not really a huge deal. But if the rendering back ends can't keep up with progress, Urho3D will die.

Edit: Also, the editor is a frequent pain point. The rbfx fork might be a good draw of inspiration here. Honestly, if rbfx hadn't dropped Lua and AngelScript in favor of C# scripting, I would probably consider moving to that fork. But they did drop them, so... alas. Still, might be worth seeing if the editor work could be brought back here.

-------------------------

Leith | 2019-05-19 05:44:18 UTC | #3

Vulkan support is coming - it has to.
I expect no end to this game of playing catch up with the latest rendering api.

I feel your pain regarding C# - can we get our grubby hands on an older version of rbfx and refork from there?

Urho is exceptionally well-written, in terms of code quality, compared to many engines I have worked with. Most of the codebase is well-reasoned and well tested, but there are many areas in the engine where improvements can be made. There is also a lot of resistance to change, which is natural for two reasons.

Firstly, we're all hard-wired to fear and resist change when we are already in the comfort zone.
Secondly, change creates work... if I make a little change in the Urho source, it could mean making changes to a bunch of dependent samples, and it can break projects outside of that arena.

The fluttering of the wings of a butterfly can cause a tsunami on the other side of the world.

This is all true, but it's still no excuse for complacency, when we know we can do better.

[quote]But if the rendering back ends can’t keep up with progress, Urho3D will die.[/quote]
Yes, as in nature, if you are alive, you can be in one of three states - growing, stagnating, or decaying. Which state best represents Urho right now?

-------------------------

Modanung | 2019-05-19 20:19:46 UTC | #4

Despite the common anxiety about Urho going beyond undead I would like to note there still seems to be a steady stream of *new* people coming to the forums and an increasing amount of discussions on engine development happening lately. But that could just be spring. :)

-------------------------

rku | 2019-05-19 15:35:56 UTC | #5

[quote="Leith, post:3, topic:5159"]
can we get our grubby hands on an older version of rbfx and refork from there?
[/quote]

You cant, because removing AS/lua was pretty much first thing i did :trolleybus:

-------------------------

S.L.C | 2019-05-19 16:10:14 UTC | #6

I'd better fork the engine as it is because it'll get nasty from here on. Seems everyone wants to rip it apart and put a little bit of themselves in there.

-------------------------

weitjong | 2019-05-19 16:36:33 UTC | #7

Not if I can help it 😉 however, I don’t want to hold it back too. We can get dev branch for free in GitHub.

-------------------------

QBkGames | 2019-05-20 08:53:30 UTC | #8

From what I read around the Net, Vulkan would not make all that much difference to performance in most cases unless the entire engine is multi-threaded which allows you to send render commands from multiple threads.

What I think would make a significant difference to the engine presentability is a more modern lighting solution with Global Illumination and a good SSAO shader.

-------------------------

Modanung | 2019-05-20 11:14:59 UTC | #9

[quote="S.L.C, post:6, topic:5159, full:true"]
I’d better fork the engine as it is because it’ll get nasty from here on. Seems everyone wants to rip it apart and put a little bit of themselves in there.
[/quote]
I know the feeling but I'm comforted by the knowledge that there seems to be a sense of direction. This is a prerequisite for things to go somewhere. When the directions fail to align this commonly results in mitosis (not cell death).

-------------------------

guk_alex | 2019-05-20 13:01:50 UTC | #10

Multi-threading support is only one of the advantages of Vulkan, but not only. There're also decreased driver overhead and the lack of the context-switch architecture (if you want to dig deep you can achieve the similar performance with advanced OpenGL techniques know as zero-driver-overhead). And you are right that non of this matters if engine itself couldn't reach its own potential even without this modern graphics stuff.

-------------------------

S.L.C | 2019-05-20 15:36:04 UTC | #11

tl;dr A careful selection of choices and directions must be made in order to avoid the common pitfalls for a game engine in this state .

I'm ok with change. And as long as there is one direction (*not the band*). However, I have a feeling there will be (*is?*) more than one direction going on, and it will end up a freak-show. Basically a Frankenstein engine with bits from all over the places that tries to cover just about everything under the sun to satisfy everyone but failing to do what it was actually meant to do.

But those are just my thoughts. I'm quite curious how it'll actually end up.

I don't think i have enough fingers for every engine where the author retired and everyone began to volunteer and start working on new features and exciting new stuff. However, by the end of it all that remained was an engine without purpose and features no one cared about or maintained or sometimes even completed. At which point you could label it `yet another game engine that no one cares`.

Like I said. I'm ok with change. But change(*s?*) without purpose or direction for the sake of not looking stagnant will not yield a favorable result.

My problem with game engines nowadays (*at least most of them*) is that they focus too much on the graphics side. I mean, is that all a game is about? Looking good?

When you actually begin to do the logic of said games you soon realize you entered a nightmare. A clusterf* of nonsense that can't be evolved beyond a `Hello World` project. Basically, they lack the tools to build the logic of your game and aid you in getting a prototype without a ton of work.

How come no one here is offering to improve the GUI? Add better components. Everything boils down to graphics. Might as well just call it a rendering engine.

Which is why no successful game has ever use an open source engine. There are a few exceptions, I know. But they are too few for the plethora of games and free open source game engines out there.

I honestly have no right to complain about any of these. I don't contribute much. I play with ideas from time to time as a hobby. And what I've mentioned are basically observations I've made in time (*my opinions*).

-------------------------

Modanung | 2019-05-20 18:22:26 UTC | #12

For me it comes down to this:
> Urho3D is a free lightweight, cross-platform 2D and 3D game engine implemented in C++ and released under the MIT license.

When I read that line for the first time I *knew* I had found what I was looking for. That is what *defines* Urho3D, in my view. Meaning any decisions clearly diverging from that definition should be implemented as forks or extensions. The _lightweight_ part can be somewhat hard to define. But to me it means anything too specialized should not be a part of the core repo. This should not stop the community from creating, *indexing* and co-developing awesome extras which would otherwise clutter core development.

@S.L.C Indeed, the industry tends to use industry standards or in-house/project-specific engines. Do _id Tech_ engines count as open source game engines in your view? And I don't think that many other engines out there match the *exact* definition mentioned earlier.

-------------------------

Modanung | 2019-05-20 21:24:16 UTC | #13

Concerning forks I'd furthermore like to cite the Urho scriptures...
[details="Sermon"]
> Flash of the knife, on top of a pizza box
Divide the fish into two
Eyes and mouth slowly open and close
Even after the mutilation
>
>Unceremoniously into trash
But the spirit remains to haunt
Fear for the day when it returns from the dead
And traps you into a net
>
> -----
> *...and concerning commercial forks...*
>
>Evil shark
Eat my heart
So if I die I may respawn

[/details]

-------------------------

JTippetts | 2019-05-20 22:11:40 UTC | #14

:rofl: Nice and to the point.

-------------------------

QBkGames | 2019-05-21 02:17:29 UTC | #15

[quote="S.L.C, post:11, topic:5159"]
How come no one here is offering to improve the GUI? Add better components. Everything boils down to graphics. Might as well just call it a rendering engine.
[/quote]

In terms of fulfilling it's scope of "lightweight all purpose engine", I think Urho is quite complete and usable. The GUI is quite decent and usable, in what way should be improved? Also what better components could be added? You can always improve on things for sure (I'm thinking physics), but what we have is reasonably functional.

To me, the only area in which Urho is falling a bit behind the rest of the engine world is on the graphics side, so that should be the focus of improvements. I definitely agree that a good graphics does not equate a good game, however when you try to go commercial, you find that people do judge a book by its cover and a game by its graphics, so the game needs to look presentable, and having primitive lighting starts to get noticeable.

-------------------------

Leith | 2019-05-22 05:22:42 UTC | #16

Not everything boils down to graphics.
There's a lot of stuff missing from Urho - today I found that DecalSet has no AutoRemove implemented. Recently, I found that btPairCachingGhostShape is not supported. Also today, I found that the number of Collision Mask bits in the Editor is not sufficient for me (I have about 12 of the available 16 bits defined, while the editor provides eight checkboxes for eight bits). These are just a few small examples off the top of my head, but not a day goes by that I don't notice something else.

Without suggesting that we should be adding new components at all, there is a lot of small things that can and should be addressed, and in most cases are unlikely to break existing code.

-------------------------

JTippetts | 2019-05-22 22:56:57 UTC | #17

Those kinds of issues, though, won't 'kill' the engine. A couple tiny pull requests will fix them, and users of Urho3D in the past have usually been pretty good about finding and fixing such things. However, eventually graphics backend stagnation *will* kill it. See Apple's push to deprecate OpenGL. Eventually, the engine has to follow where the standards go, and right now Urho3D is already behind (no D3D12 support, no Metal support, no Vulkan support). It's not critical yet, but there should be a plan in place to address it. From what I understand, this will be a pretty challenging task. I would take it on, but it is quite outside of my area of expertise.

-------------------------

elix22 | 2019-05-23 06:45:21 UTC | #18

I did implement Vulkan & Metal backends .
Most of it is working very well  (you can try it ). 
There are still some issues that need to be fixed , like shadow support and some memory issues .
I don't have time now to continue working on it , I might continue working on it in a few months.
You are right ,  this is a challenging task and requires vast knowledge on SDL2, Urho3D , Angle , Vulkan , Metal.  

https://discourse.urho3d.io/t/metal-moltenvk-support-for-ios-an-mac-devices/4845

-------------------------

Leith | 2019-05-23 11:09:15 UTC | #19

Rendering tech is within my scope - I can certainly help with transition between rendering api, but right now I have no urgent need for widespread rendering support, so it's not on my priority list.

-------------------------

Leith | 2019-05-28 08:17:27 UTC | #20

Please try to find some time to continue your work - Apple pulling OpenGL support sort of increases the pressure to add vulkan support.

-------------------------

Leith | 2019-06-06 05:16:02 UTC | #22

I don't know which way is the right way forward.
But I like that someone other than me is thinking about it!

I'm not certain that I like the idea of stripping back everything to the bone.
We have a very clean design pattern, we should be able to do that conceptually and not actually break anything. Improved documentation would give more "bang for buck" than a restructure of the framework, and would facilitate future development.

There are places where fundamental paradigm shifts are needed.
One of them, is that multiple threads can issue render commands on modern graphics api - we're not bottlenecked to issue those from the thread that owns the render context.
I'm sure that there are others.

-------------------------

rku | 2019-06-06 11:43:31 UTC | #23

Reality check: change is not coming. Forget about it.

Look around. There is no clear project leader. There are few maintainers who keep project on life support, but at this point it is in vegetative state. No new development is happening. This forum is full of inexperienced people who keep talking about petty stuff like using panda3d pipeline and what not. They will not make Urho3D 2.0 happen. There may be a handful of skilled enough people that are interested in pushing project forward, but that will also not happen precisely because project is on life support and current maintainers only do life support. Nothing wrong with that, but it is what it is. Should new people come by and take over a project - well this is a huge responsibility that should not be taken lightly. And so nobody does that.

So instead of talking - get to work. Make a fork and put work into it. If your ideas are good - you will get followers and your project will become Urho3D 2.0 while Urho3D 1.7 will continue being LTS release forever.

-------------------------

Leith | 2019-06-06 12:19:41 UTC | #24

In our current state I can issue pull requests, but not many people see those,
If my ideas are good, and I shove PR, I have no guarantee that my work will see the light of day, or that it will be fairly judged by my peers. I know the only alternative is to fork, but I want to give back.
Can one person make positive change?

I would like to think so.

If we need a new project leader, let there be one for each field in the engine, some of those are mine. I will do what needs to be done, in one small part of the engine, and be a leader there, if that is what we need. I don't know what we need, but we need change. If we are not in a state of growth, then we are in a state of decay. I can help, and there are more like me who can too.

I specialize in graphics, physics and networking. I can do other stuff but those are my key areas.

-------------------------

Dave82 | 2019-06-06 13:51:07 UTC | #25

You  have to see the project from a game developer point of view too. Since urho is a game engine there are lot of people here who are not really interested in contributing to engine fixes and new features. They want to make a game and not fixing a game engine. Perhaps small pr's but nothing core stuff.
If i have to patch and add extra features to a game engine i would simply write my own general purpose engine

For now i'm happy with current features of urho3d since i'm making a game which doesn't require nexgen graphics...

-------------------------

cadaver | 2019-06-06 14:03:19 UTC | #26

IMHO, to ensure Urho's development to a "2.0" version you would need a person or a group in a "do or die" situation where they have no other choice but to develop the engine, so that they can make their project come true.

For example, I'm currently working on a Commodore64 game that is quite advanced and pushing boundaries. I know there's nowhere in the world I could get the engine code for that ready-made, so I have to make it myself. And then I have to make the editor(s) so that I can build the game content. Granted, they're not the best editors ever, and not flexible enough for the development of any C64 game, but good enough for my project.

But, in the realm of PC or mobile development, there's so many engines to choose from, or the wish to experiment on your own (ie. start / fork another engine project), so a "do or die" situation leading specifically to Urho's development is unlikely, as unfortunate as it is.

-------------------------

Leith | 2019-06-06 15:05:45 UTC | #27

Actually I have a lot of experience in the c64 area, including how to code reset resistance and border removal, and i would love to teach what i know
The C64 is a good example, mostly because there was little to no docs, and mainly because the internet was new, and not many of us had made their own modem and connected to a BBS
To be clear, the z80 had nothing for me, but I learned the difference between irq and nmi quickly on the c64
Also, hi and good to see you, old fish

-------------------------

Modanung | 2019-06-06 21:51:40 UTC | #28

Every advantage has its downsides. Arrested engine development also means little change in the API, which - if you can shake the fear of possible future problems - *can* actually be experienced as pleasant in the development of applications.

@rku You moved pretty quick with **rbfx**, how do you maintain your pessimism concerning Urho3D?

-------------------------

rku | 2019-06-07 06:07:49 UTC | #29

@Modanung i already detailed my reasons. @cadaver synthesized it even better. At the moment noone particularly **needs** Urho3D-the-project to go forward. Many people **would like** it to progress but they do not really **need** it to happen. And so we are where we are.

-------------------------

NinjaPangolin | 2019-06-07 08:48:27 UTC | #30

Allow me to voice my opinion as an rather non-active user who finds the engine to be really neat and nice to work with.

There are two things that Urho lacks that prevents it from gaining popularity and subsequently more people willing to put time and effort into improving and developing it. The first problem is that the engine is rather obscure and not very well known. I think it'd be nice to push it more in various services such as reddit.com/r/gamedev and reddit.com/r/cpp. We need blog post describing all the cool things we can do with the engine. We need some tutorials and showcases. As of now it's kind of difficult to dive into more advanced parts of the engine - the documentation and wiki pages are rather sparse and one needs to get his hands dirty by looking through the code and forum archives to find solutions to problems he had. One of the reason engines such as Unity are so popular is that there's million and one tutorials showing how to do things. These make people want to try experimenting themselves. How about Urho? Let's say I'd like to write my custom shader. The only tutorial-like example I can find in the web is this old post http://nervegass.blogspot.com/2014/12/urho-shaders-edge-detection.html. The documentation says "study techniques code". Now that's not something a beginner developer want to hear.

The second thing that could help Urho is an actual successful game. But that's rather difficult thing to achieve so I'd stick to creating a better introductory materials to lure the newcomers. And then maybe one of them will manage to create something that will make people more interested in the engine itself.

-------------------------

UNDEFINED-BEHAVIOR | 2019-06-07 21:56:29 UTC | #31

So it's already de facto LTS huh :thinking:

@NinjaPangolin 

>not very well known

Not so sure about that. 
Quick search for "GameEngine" and a couple dozen will come up.
But If one is really looking for an engine that's: 

* Cross platform including web and mobiles
* Is FOSS
* Reasonably close to the metal
* Strong 3D
* Most feature rich.
* Looking to mod the engine and build their own thing on.

The only project that hit all the bullet points are this one IMO
Really if ANY of the above doesn't, there's a better choice out there and they won't even consider this engine in the first place.

-------------------------

George1 | 2019-06-08 00:58:35 UTC | #32

Hi rku,
Your progress is great.
The only drawback with your current fork is that cmake does not work out of the box.
It has two dependencies. 
The sn.exe and and nuget to restore json file on windows visual studio.

-------------------------

Zaroio | 2019-06-08 01:12:22 UTC | #33

It needs a better editor, A good editor, and a good gui, could bring more people. I guess. Something like godot. Also, how about a discord server?

-------------------------

UNDEFINED-BEHAVIOR | 2019-06-08 06:31:27 UTC | #34

With c# features OFF it works as is over here.

-------------------------

Leith | 2019-06-08 06:33:42 UTC | #35

I have been posting about some of the issues I have found, and some solutions were proposed. Not PR, but on the record and searchable. That is more useful, to me, than PR.

-------------------------

George1 | 2019-06-08 13:11:50 UTC | #36

[quote="Leith, post:35, topic:5159"]
he record and search
[/quote]

Thanks I know. But I want to use C# without those manual setting.
  
Rku, give us the the wait for event feature in your coop task system.  The one similar to what aster2013 provided for lua script :). 

https://discourse.urho3d.io/t/lua-coroutine-extension/112

Good to see more progress on that fork.

Event should work immediately at the current time frame.

regards.

-------------------------

rku | 2019-06-08 13:58:20 UTC | #37

A fair point. You need mono+msbuild on unixes or .net framework 4.7.1 on windows. Since C# is very much experimental i disabled it by default so now it should build out of the box on desktops.

[quote="George1, post:36, topic:5159"]
Thanks I know. But I want to use C# without those manual setting.
[/quote]
If you aim to be a developer you have to develop. You have to set up your environment right as engine depends on external components.

[quote="George1, post:36, topic:5159"]
Rku, give us the the wait for event feature in your coop task system. The one similar to what aster2013 provided for lua script :).
[/quote]
Not sure what that would be.

We are moving into offtopic now so we should stop :]

-------------------------

