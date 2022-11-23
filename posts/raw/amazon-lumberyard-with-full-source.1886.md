Lumak | 2017-01-02 01:11:06 UTC | #1

This is news to me. I had no idea it came with full source. here's the 1st person shooter sample based on CryEngine gameSDK [url=https://aws.amazon.com/lumberyard/downloads/]Lumberyard link[/url].

-------------------------

Shylon | 2017-01-02 01:11:06 UTC | #2

It is not really new news, PERSONAL VIEW, Lumberyard is really good engine and is going to be successful, but I like Urho3d more (lightweight, MIT, and growing community), also Honestly I do not like to bound to their license, I am using Unreal Engine 4 for Arch-Vis, but never using it for game, I tried other engines but after more than 1 year I finally chose Urho3d ( I tested few times ago), I am sure Urho3d also will be successful, I like coding beside my professional 3d works because I think it is better than playing Chess and keeps the brain active.

-------------------------

dragonCASTjosh | 2017-01-02 01:11:06 UTC | #3

the news that got me today is along the same kind of lines: [url]http://80.lv/articles/pay-what-you-want-for-cryengine/[/url] Cryengine V is pay what you want and includes new UI, could change the engine market at a AAA level

-------------------------

hdunderscore | 2017-01-02 01:11:06 UTC | #4

Options are always great to have, and I hope those engines find success so that we have a variety of up-to-date engines to choose from in the future.

I personally like the lightweight + open nature of Urho. We might not have all the bells and whistles, but what we do have works really well and allows for quick iteration and prototyping.

-------------------------

dragonCASTjosh | 2017-01-02 01:11:06 UTC | #5

We also have an amazing community. and what i like best about Urho is i can learn how how to implement features like the AAA companies for example my PBR work without worrying about the core engine. same goes for any other area of engine development.

-------------------------

jenge | 2017-01-02 01:11:06 UTC | #6

This is cool and would have been unheard of 5 years ago.  Though, I'm pretty sure that the free EULA will cover games only.  One thing to keep in mind is that most of Unity's money isn't coming directly from game developer licensees.  It is coming from ads, gambling usage, serious apps, defense contracts, etc.  Another thing, if they are remotely successful, this won't be "pay what you want" for long.  If anything, Crytek has shown a propensity for changing its EULA  :confused:   

The games we make I want to have a shelf life and so need to be able to build them.  The more complicated your tech/build the harder maintenance becomes... and this is also why I don't believe in binary solutions.  Good luck upgrading your project to the latest Unity every couple years, or maintaining your own version of Unreal or CryEngine, gah!

-------------------------

Lumak | 2017-01-02 01:11:06 UTC | #7

My intent was to see what tech I could learn from CryEngine and adapt somethings to Urho3D for personal use. I glanced through the folders and saw some interesting things, such as:
-global illumination
-spherical harmonics w/ doc
-HLSL cross compiler from GLSL (which I didn't know it's already on github).
-animation editor
-level editor
-terrain/editor

Way too many goodies to mention. It's definitely rich with a lot of resources to learn from.

-------------------------

dragonCASTjosh | 2017-01-02 01:11:07 UTC | #8

CE5 also has some new goodies one of them being Screen Space shadows. due to there website being down at the moment i cant test it but its listed in the docs and sounds a good idea

-------------------------

rasteron | 2017-01-02 01:11:07 UTC | #9

[quote="dragonCASTjosh"]the news that got me today is along the same kind of lines: [url]http://80.lv/articles/pay-what-you-want-for-cryengine/[/url] Cryengine V is pay what you want and includes new UI, could change the engine market at a AAA level[/quote]

wow, just got this news earlier too. This is quite interesting.

-------------------------

weitjong | 2017-01-02 01:11:07 UTC | #10

Full source code? Now this I need to see.  Thanks for the links.

-------------------------

codingmonkey | 2017-01-02 01:11:08 UTC | #11

nice feature I think 
[gamedev.amazon.com/forums/artic ... ation.html](https://gamedev.amazon.com/forums/articles/4737/modular-behavior-tree-editor-xml-serialization.html)

-------------------------

cadaver | 2017-01-02 01:11:08 UTC | #12

Downloaded the Lumberyard source yesterday, didn't have time to look indepth, but to be honest its structure didn't impress at least immediately. Naturally it's packed with features, but getting to understand it would take quite a bit of effort.

Still have the CryEngine V to check, and how much it's different, once their site starts working and actually gives me a password restore :slight_smile: (EDIT: that's no longer the problem, now just need the launcher to start working and downloading the engine)

But in general I'm with hd_ ; Urho doesn't have the most amount of or most modern features, but what is there is a solid base for building more.

-------------------------

yushli | 2017-01-02 01:11:08 UTC | #13

I will stick to Urho3D as long as Cadaver acts actively as the lead dev on this project. Urho3D is elegant, nice coding style, rock solid design and performance. Thank you for implementing such a great engine, with MIT licence and still keep working on improving it.

-------------------------

yushli | 2017-01-02 01:11:09 UTC | #14

And let's not forget that Urho3D has such as nice build system. All major platforms can be targeted with the same code base and literally just one command. And, being constantly improving on.

-------------------------

Shylon | 2017-01-02 01:11:09 UTC | #15

As you mentioned about build, I removed Lumberyard a week ago, 1 of reason was, if you to create a new project, you should open the visual studio then build game and ENGINE, after long building, i had error opening project, I removed the engine instantly, :slight_smile:, now I tests my Urho3d project with QtCreator (cmake) and Mingw_64 5.3, easy and nice without needing of Visual Studio (I do not like it). I did test Urho3d on Ubuntu Studio before and I will on Ubuntu Studio 16.04 LTS too.

-------------------------

Hevedy | 2017-01-02 01:11:13 UTC | #16

[quote="cadaver"]
Still have the CryEngine V to check, and how much it's different, once their site starts working and actually gives me a password restore :slight_smile: (EDIT: that's no longer the problem, now just need the launcher to start working and downloading the engine)
[/quote]

No idea how you made that I can't even login.  :laughing: 

[quote="cadaver"]
But in general I'm with hd_ ; Urho doesn't have the most amount of or most modern features, but what is there is a solid base for building more.
[/quote]

Yeah, but a boost in the visual part should be something cool.
In the second side, if you guys add visual effects to 2D samples and the fluids plugin for Box2D Urho will win so much, the other AAA engines got pretty bad 2D support and that is a good side to get new users.

-------------------------

thebluefish | 2017-01-02 01:11:14 UTC | #17

[quote="Hevedy"]In the second side, if you guys add visual effects to 2D samples and the fluids plugin for Box2D Urho will win so much, the other AAA engines got pretty bad 2D support and that is a good side to get new users.[/quote]

To be blunt with it, I honestly think the entire 2D side needs some significant overhaul to even be competitive with other AAA engines currently.

-------------------------

boberfly | 2017-01-02 01:11:18 UTC | #18

Yeah Lumberyard is very large, the renderer back-end wasn't much fun to read (GL support is essentially shoe-horning a DX11 wrapper over it), the UI is Windows-only. Urho3D is much nicer to read, but I come from Horde3D's codebase where I learned C/C++...

CryEngine V sounds a lot better (curious to know if their new UI is Qt...?)

I'm curious about Nitrous engine's design though, too bad it's closed:
[youtu.be/xXyZ4YaktyU?t=3256](https://youtu.be/xXyZ4YaktyU?t=3256)

Sounds like it is using the 'actor' model for async communication with different systems, maybe along the lines of this:
[theron-library.com/](http://www.theron-library.com/)

If I had the time/motivation/skillset, a cool toy engine could be made with this (or at least learning the concepts so it works well with your codebase), perhaps also implementing everything into job tasks with pure functions and AoS/SoA structs pumped through code written in ISPC. I think though you'd really need to rewrite some reliant middleware, or perhaps adapt it to this system somehow. I think for any codebase, starting with Urho3D's core & build system would be a very wise decision. I think also decoupling the development pipeline and the runtime as another cool way to go, like just doing XML stuff in the development phase and then transforming this to a binary format which is just directly mapped to a struct. The tool pipeline can be just Qt+Python and as procedural as possible. :slight_smile:

-------------------------

Hevedy | 2017-01-02 01:11:18 UTC | #19

[quote="boberfly"]
CryEngine V sounds a lot better (curious to know if their new UI is Qt...?)
[/quote]

The launcher at least is Qt, but not sure the engine.

*I think the engine is Qt Too.

-------------------------

Lumak | 2017-01-02 01:11:23 UTC | #20

I downloaded the CryEngine V for free. CryEngine has runtime global illumination using spherical harmonics, and found this doc when researching SH lighting, [url=http://www.research.scea.com/gdc2003/spherical-harmonic-lighting.pdf]Sony R&D SH Lighting[/url]. It might be interesting to implement...

-------------------------

