jenge | 2017-01-17 18:52:11 UTC | #1

[b]UPDATE:[/b]  We've released the Atomic Game Engine [b]under the MIT license[/b] on GitHub, [url=https://github.com/AtomicGameEngine/AtomicGameEngine]github.com/AtomicGameEngine[/url]

Hello cadaver and team!

Firstly, I must say incredible work on Urho3D.  It is simply a joy for development.  Great job on the core, rendering, and integrating so many awesome FOSS projects! :slight_smile:

I've been hacking on Urho in my spare time for the last couple years.  I made a Unity3D exporter, a Quake2 Renderer, hacked up some emscripten support, and a bunch of other prototype-y things that never saw the light of day.

A month ago, I decided to fork and start the "Atomic Game Engine" project.  The focus of Atomic is to be able to use Javascript and C/C++ to ship games on Desktop, Mobile, and WebGL.

UPDATE: The Atomic Game Engine is now Open Source under the permissive MIT license!  :open_mouth: 

Atomic Game Engine 2016 Video Reel
https://www.youtube.com/watch?v=Jz54r17HN3A

[img]http://atomicgameengine.com/blog/images/RoboBeach.png[/img]
[img]http://atomicgameengine.com/blog/images/AndroidBuildSettings.png[/img]
[img]http://atomicgameengine.com/blog/images/Atomic_Roboman_Touch.gif[/img]
[img]http://atomicgameengine.com/blog/images/DevSnapshot2116.png[/img]

[b]Update: Game From Scratch Preview[/b]

https://www.youtube.com/watch?v=fRnEs15y-Us

Thanks again and looking forward to showing more progress, soon!  You can follow the project on Twitter: [url]https://twitter.com/AtomicGEngine[/url]

- Josh Engebretson
THUNDERBEAST GAMES, LLC

-------------------------

cadaver | 2017-01-02 01:01:51 UTC | #2

Thanks for sharing!

I would strongly suspect that some of the changes like Emscripten support do end back up in mainline Urho.

-------------------------

aster2013 | 2017-01-02 01:01:52 UTC | #3

Cool, it looks awesome. 
BTW: Can you share your sample code and assets? If you can, I want to add a Lua script game sample based on your code in Urho3D.

-------------------------

jenge | 2017-01-02 01:01:52 UTC | #4

@cadaver: That would be great.  I'll get the licensing sorted out soon (it'll be either MIT or Apache).

@aster2013:  Thanks! Yes, I pulled the assets from opengameart ([opengameart.org/content/space-ga ... k-extended](http://opengameart.org/content/space-game-art-pack-extended)) and the explosion is from an XNA example (which I think is also fine to redistribute).  The scripts use the first pass of our Javascript component model, so they are already due for a refactor.  You could probably do a more Urho-centric version of the game.  The most current scripts are in the editor repository, I need to make an examples/tutorials repo which is nothing but the example scripts.

-------------------------

jenge | 2017-01-17 18:52:30 UTC | #5

I published an update video on the progress this week.

https://www.youtube.com/watch?v=hOkPBdLj5vA

- Josh Engebretson
THUNDERBEAST GAMES, LLC

-------------------------

friesencr | 2017-01-02 01:02:00 UTC | #6

Looks awesome Josh!  I am really looking forward to see where throw your opinions.  Urho's lack of strong opinions on structure and lack of turn key components seem like a really great place to round of some our edges.  For instance we have had quite a few suggestions to create a trigger component in Urho.  We have always suggested that you can make your own prefab and thus don't supply a trigger.  Also the Nvidia Shield has a tegra 4 and not a 3.

-------------------------

jenge | 2017-01-02 01:02:00 UTC | #7

Thanks!

Ah yes, I have a Nexus here with a tegra 3, got it confused in the heat of recording video :slight_smile:  I really like the Shield, great piece of hardware!

- Josh

-------------------------

friesencr | 2017-01-02 01:02:00 UTC | #8

[quote="jenge"]Thanks!

Ah yes, I have a Nexus here with a tegra 3, got it confused in the heat of recording video :slight_smile:  I really like the Shield, great piece of hardware!

- Josh[/quote]

Yeah I love my Shield.  I got an early run and have some issues with thumb stick dead zones and the clicky dpad but other than that it is such a cool little device. The screen, speakers, and ergonomics trounce any other handheld.  I have an Ouya which has the Tegra 3 and the Tegra 3 struggles.  I can't wait for the Sheild Portable 2 with full gles 3 support.  Hello Dolphin!

-------------------------

buhb11 | 2017-01-02 01:02:10 UTC | #9

Hello,I`ve been tracking the progress of this engine,so far so good!But to be honest with you I cant wait one more day without testing it! Please make me a gift for this holidays and leave the page from github because I`m ready to start developing in it! Thanks  :unamused:

-------------------------

Hevedy | 2017-01-02 01:02:10 UTC | #10

[quote="jenge"]

I tried to keep the video brief and for a wider audience, so only touch on the open source aspect of the project.  I am in the process of setting up a blog to talk about the core tech, including Urho3D.  

The plan is for the runtime to be MIT, so it will also be available to fork, pull request, etc.  You can actually already find it in the Urho3D forks if you're interested.

Thanks again and looking forward to showing more progress, soon!  You can follow the project on Twitter: [url]https://twitter.com/AtomicGEngine[/url]
[/quote]

The tools & editor are private ?

-------------------------

lexx | 2017-01-02 01:02:13 UTC | #11

Im very interested in this project, good work.

[quote]
The focus of Atomic is to be able to use Javascript and C/C++ to ship games on Desktop, Mobile, and WebGL.
[/quote]
No angelscript support?  Angelscript for webgl?

-------------------------

jenge | 2017-01-02 01:02:13 UTC | #12

@buhb11:  Thanks, we're working hard on Atomic.  It will be available in 2015

@Hevedy:  Yes, the editor is a private repo

@lexx:  Angelscript uses assembly code which won't work compiled for the web.  We're focusing on Javascript and languages that compile to Javascript.

- Josh

-------------------------

buhb11 | 2017-01-02 01:02:15 UTC | #13

[quote="jenge"]@buhb11:  Thanks, we're working hard on Atomic.  It will be available in 2015

@Hevedy:  Yes, the editor is a private repo

@lexx:  Angelscript uses assembly code which won't work compiled for the web.  We're focusing on Javascript and languages that compile to Javascript.

- Josh[/quote]

I`m looking forward! But when you say ,,It will be available in 2015`` this means January 1 or :confused:

-------------------------

jenge | 2017-01-17 18:53:08 UTC | #14

# The Atomic Game Engine now has a website: [url]http://www.AtomicGameEngine.com[/url]

We've also published the latest engine progress video.  It features [b]2D platformer physics, 2D lights with shadows, and Javascript IDE improvements[/b]

https://www.youtube.com/watch?v=DZjkSYoZECU

- Josh

@buhbb1: I really don't have a better timeframe than 2015 at the moment, sorry.  You could sign up for the newsletter on the Atomc Game Engine site if you would like to receive updates

-------------------------

Hevedy | 2017-01-17 18:53:40 UTC | #15

[quote="jenge"]# The Atomic Game Engine now has a website: [url]http://www.AtomicGameEngine.com[/url]

We've also published the latest engine progress video.  It features [b]2D platformer physics, 2D lights with shadows, and Javascript IDE improvements[/b]

https://www.youtube.com/watch?v=DZjkSYoZECU
- Josh

@buhbb1: I really don't have a better timeframe than 2015 at the moment, sorry.  You could sign up for the newsletter on the Atomc Game Engine site if you would like to receive updates[/quote]

This is nice. I see the update via Twitter today, nice changes, and have 2D light! This is needed to implement in the Urho3D

-------------------------

sabotage3d | 2017-01-02 01:02:22 UTC | #16

Have you tested the engine under IOS 8 . I wonder if there are any problems ? 
Do you rely fully on vanilla SDL for compatibility between different platforms ?

-------------------------

buhb11 | 2017-01-02 01:02:23 UTC | #17

I have a question! How much time does it take to compile the editor and the engine itself?I`m asking this because I`m also contribuing to godot engine and there the compilation time takes somewhere around 3-6 min,which is not quite pleasent.

-------------------------

TiZ | 2017-01-02 01:02:25 UTC | #18

I don't remember you mentioning it in any of your videos, and your website only lists Windows and Mac as desktop targets.

Do you plan on supporting Linux, and not just as a deployment target, but for editing as well?

-------------------------

amerkoleci | 2017-01-02 01:02:28 UTC | #19

Did you used spidermonkey for Javascript embedding?

-------------------------

jenge | 2017-01-02 01:02:28 UTC | #20

@sabotage3d: I have not deployed to iOS yet, however as all other platforms including WebGL are running there most likely won't be any major issues.  The SDL in ThirdParty is used for all platforms other than WebGL, where an emscripten-ized SDL2 is used.

@buhb11:  Build times are well under a minute for everything on my Mac, this is entirely thanks to @weitjong's excellent build system

@TiZ: Yes, there isn't any reason Linux can't be supported for editing and deployment, other than lack of manpower at the moment.  

@amerkoleci:  Atomic uses Duktape for Javascript ([url]http://duktape.org[/url]), Spidermonkey is a huge dependency which would also complicate WebGL deployment

- Josh
[url]http://www.AtomicGameEngine.com[/url]

-------------------------

buhb11 | 2017-01-02 01:02:29 UTC | #21

This is a stupid question,but anyways...do you support directX?If not,everything is rendered using opengl 2.0 even for 2d?Thanks!

-------------------------

jenge | 2017-01-02 01:02:32 UTC | #22

Yes, the 2d lighting system (and 2d in general) will continue to support Direct3D9

- Josh
[url]http://www.AtomicGameEngine.com[/url]

-------------------------

amerkoleci | 2017-01-02 01:02:59 UTC | #23

I would like to know how do you script your logic from emscripte/html?
I don't think you expose the duktape scripting in javascript environment, that will be such pain, how do you manage that part?

-------------------------

jenge | 2017-01-02 01:02:59 UTC | #24

Hello,

The scripting is exactly as with the other platforms, the bindings are simply compiled to JS along with everything else.

Please use the Atomic Game Engine forums for questions regarding it.  They are available on the website.

Cheers,
- Josh
[url]http://www.AtomicGameEngine.com[/url]

-------------------------

j15r | 2017-01-02 01:03:52 UTC | #25

[quote]@aster2013:  Thanks! Yes, I pulled the assets from opengameart and the explosion is from an XNA example (which I think is also fine to redistribute).  The scripts use the first pass of our Javascript component model, so they are already due for a refactor.  You could probably do a more Urho-centric version of the game.  The most current scripts are in the editor repository, I need to make an examples/tutorials repo which is nothing but the example scripts.[/quote]

Looks beautiful! I do have one quick question about the assets -- are the modular interiors (or their precursor models and textures) shown in those demos actually from Open Game Art as well? I've had no luck finding anything similar, but the site's a bit hard to navigate, so that may just be pilot error on my part.

Thanks,
joel.

-------------------------

jenge | 2017-01-02 01:04:04 UTC | #26

@j15r:  The assets in the video were licensed and are not on open game art.

I will keep posts here to a minimum, though I wanted to mention that Atomic is in Early Access and currently available to download.  [b]Please use our forums for questions and discussion regarding Atomic.[/b]

Atomic has been a ton of work and I don't think I would have initiated the effort if not for the Urho3D base.  To say thanks:

[b]Any contributor to Urho3D as listed in the README.md, can receive Atomic Pro.[/b]  If you're interested, register for Standard (which is free) and then send an email to thunderbeastgames AT gmail DOT com with your name as it appears in the readme.  Also, if you want your name in the credits let us know in the email how you would like them to appear.

Cheers!
- Josh
[url]http://www.AtomicGameEngine.com[/url]

-------------------------

sabotage3d | 2017-01-02 01:04:04 UTC | #27

Looks cool are there any demos for the pro version with IOS and Android ?

-------------------------

jenge | 2017-01-17 18:54:04 UTC | #28

Hey all!

It has been 5 months since the initial release and I wanted to share some updates.  Here's an Atomic Editor video from this weekend which shows some progress on the workflow.  It feels great to be at a point where talking about some basics takes 30 min :slight_smile:

https://www.youtube.com/watch?v=XUPgj9Oh3dQ

A binary test build of the editor should be available within a couple weeks.

I also wanted to answer some perhaps common questions:

1)  Why did you choose Urho3D and why make Atomic?

I've been in  the game industry for 20 years and have developed and used many game engines in  that time.  For our games studio, I have always wanted to be able to compile our engine tech from source.  I've never been a fan of black box solutions like Flash & Unity.  Unreal is just massive and I am not a big fan of royalty arrangements.  So, I spent years looking into various FOSS libraries.  When I saw Urho3D a few years ago on Google Code, it clicked and I spent loads of free time having FUN playing with it.  I also did some real work, as with the first proof of concept Emscripten build, etc.  Late 2014, I decided that I wasn't getting any younger and it was time to stop "playing around" and really build something :slight_smile:  

TL;DR I want to make games, have very strong thoughts on the tech I want to make games with, and Urho3D provided an absolutely stellar starting point.

I put together a [url=http://atomicgameengine.com/why_atomic/]"Why Atomic?"[/url] on the website which covers why Atomic specifically.

2)  Why didn't you fork the Urho3D repository?

I would have preferred to fork as it would have simplified some things.  However, GitHub has significant usability issues on forked repos, not least of which being that they can't be searched.  I also needed the flexibility to change the structure (we've added/removed/and moved much stuff) which loses the benefits of being a fork.  Atomic and Urho3D also have quite different goals and features, for example AngelScript/Lua and the Scripting API module in general have been removed as we're focusing on JavaScript (huge thanks to Lasse for designing a modular system where this is not only possible but easy!). 

3)  Why isn't Atomic under a permissive license?

I love permissive licenses and maybe one day we'll be able to do this.  In the meantime, I went full-time on Atomic six months ago and have been funding the tech personally.  There are paid and free versions of the Atomic Game Engine.  I would also like to reiterate that anyone who has contributed to Urho3D in any way can receive a free license  to Atomic Pro (details above)

Whew!  In summary, I think Atomic is a great showcase for what can be built on top of Urho3D with some determination :slight_smile:  Thanks again to the Urho3D Project, Lasse, and contributors which have helped get a dream of mine off the ground, and at least walking at this point!

 - Josh
[url=http://www.AtomicGameEngine.com]http://www.AtomicGameEngine.com[/url]

-------------------------

christianclavet | 2017-01-02 01:06:23 UTC | #29

Hi, Been checking your progress, and your editor coming in really nice and solid! Your inspector should be used as inspiration on what the default URHO Editor Inspector window should behave!

-------------------------

jenge | 2017-01-02 01:06:44 UTC | #30

Hello! 

We published a new development digest today.  There's been a lot of work put into the editor and making the script component and prefab systems solid.

[atomicgameengine.com/blog/development-digest-3/](http://atomicgameengine.com/blog/development-digest-3/)

I also gave Urho3D a shout and hope that we help drive some traffic :slight_smile:

Thanks! 
- Josh

-------------------------

jenge | 2017-01-02 01:07:10 UTC | #31

Hello,

I am pleased to say that we've put the Atomic Runtime under the MIT license.  This is 100% of the code in user redistributable binaries and makes the runtime source license compatible with the Urho3D project :smiley:

Now, I can use Atomic to continue my Quake2 port, hah! [url=http://discourse.urho3d.io/t/idtech2-running-on-urho3d/217/1]idTech2 running on Urho3D[/url] 

- Josh
[url]http://www.atomicgameengine.com[/url]

-------------------------

thebluefish | 2017-01-02 01:07:13 UTC | #32

Very nice!

Now we can backport the JS stuff :wink:

I took a look at your TB integration, and I'm a bit confused as to why you still use Urho3D's batching when TB does the batching for you. [url=http://discourse.urho3d.io/t/turbo-badger-implementation/1364/1]I went ahead and posted my TB implementation[/url] so that you can take a look.

However I did go ahead and pull some of the input stuff from your implementation now that it's under MIT. My existing solution was.... not great xD

-------------------------

jenge | 2017-01-02 01:07:20 UTC | #33

Thanks for posting your TB implementation. I'll have a look, glad our implementation has been useful to you :slight_smile:

I initially had Urho's UI system and TB's working together, then moved Urho's UI to be a "System UI" which is a simple, consistently themed UI, for displaying debug dialogs, system messages, etc on device, web, in the editor etc.  The batching is a result of this process, though can probably be changed now.

- Josh

-------------------------

jenge | 2017-01-02 01:07:24 UTC | #34

We've been working on C# scripting. 

Atomic [b]C#[/b] running under the VS2015 Debugger :slight_smile:

[img]http://docs.atomicgameengine.com/forum_images/AtomicSharpVS_Small2.png[/img]

- Josh

-------------------------

boberfly | 2017-01-02 01:07:24 UTC | #35

Very cool move jenge!

Good to see C# support also. Any chance of a cython bind? :wink:

-------------------------

sabotage3d | 2017-01-02 01:07:24 UTC | #36

Is that windows only I am always confused with this C# stuff ?

-------------------------

jenge | 2017-01-02 01:07:29 UTC | #37

@boberfly:  We're sticking with JavaScript, C#, and C++, though you could probably use IronPython :open_mouth: 

@sabotage3d:  The C# support will initially be for desktop (Windows/OSX).  My primary development box is a Mac.

We pushed an update today with improved touch controls.  Urho's rendering system performs like a champ!

[img]http://docs.atomicgameengine.com/forum_images/ToonTownTouchUpdate.gif[/img]

- Josh

-------------------------

Hevedy | 2017-01-02 01:07:44 UTC | #38

[quote="sabotage3d"]Is that windows only I am always confused with this C# stuff ?[/quote]

C# now is open by Microsoft and you got the compilers sources and there are projects to support in others platforms in official way, the new VS 2015 got cross compiling and the new C# got an option to compile the apps as bin like C++ do.

-------------------------

jenge | 2017-01-02 01:08:16 UTC | #39

Hey all,  we pushed a new development snapshot with a slug of editor improvements:

+ Editing of multiple nodes/components simultaneously
+ New undo/redo system which handles multi-editing
+ Editor play mode window can now be resized and remembers position/size between plays
+ Editor snap settings
+ Remember component section states between node selects
+ New attribute widget data binding system
+ ResourceRefList inspector widget
+ UIListView improvements to handle multiple selection
+ Selection cut operation
+ New mainframe menu items and keyboard focus fixes
+ Numerous misc fixes (dragging nodes in hierarchy frame, etc)
+ JSON import type for editor
+ Improvements to WebSocket support

There's download information available in the forums [url=http://atomicgameengine.com/forum/#/discussion/154/dev-snapshot-multi-edit-editor-playmode-improvements]HERE[/url]

[img]http://docs.atomicgameengine.com/forum_images/atomic2mon.jpg[/img]

Cheers!
- Josh

-------------------------

1vanK | 2017-01-02 01:08:16 UTC | #40

I'm not good in licenses, but It will be a violation if someone will take the code from the Atomic and integrates it to Urho?

-------------------------

codder | 2017-01-02 01:08:16 UTC | #41

If you take the code from Atomic module which is based on Urho3D no, since its still MIT licensed as URHO3D.
I don't know for the editor but It have a different license.

Will be cool to integrate Light2D component in Urho3D :smiley:

-------------------------

jenge | 2017-01-02 01:08:16 UTC | #42

Yup, the entire runtime is MIT and should be clearly noted in the sources.  If something is useful, please do use it :slight_smile:

- Josh

-------------------------

1vanK | 2017-01-02 01:08:16 UTC | #43

[quote="jenge"]Yup, the entire runtime is MIT and should be clearly noted in the sources.  If something is useful, please do use it :)

- Josh[/quote]

What are the formalities to be observed? Just add the copyright to the beginning of the file, or it is necessary to mark each block of borrowed code? Or is the other way?

-------------------------

jenge | 2017-01-02 01:08:16 UTC | #44

@Sinoid: Hey! I took some inspiration from your cubemap generation stuff this morning, thanks! :slight_smile:

[img]http://docs.atomicgameengine.com/forum_images/CubeMapGen2.jpg[/img]

- Josh

-------------------------

codder | 2017-01-02 01:08:17 UTC | #45

Here:
[tldrlegal.com/l/mit](https://www.tldrlegal.com/l/mit)

And here:
[blog.jcoglan.com/2010/08/15/wha ... t-license/](https://blog.jcoglan.com/2010/08/15/what-i-mean-when-i-use-the-mit-license/)

So as far as I understand, if you plan to make a commit into Urho3D using parts of AGE their names should be included in contributors list as they made the original work but you can change the copyright lines in source files with no problem.

-------------------------

jenge | 2017-01-02 01:08:31 UTC | #46

Holy cow, I made two blog posts in two days.  Which is good since the last one was in August, been pretty busy!

Here's what we've been up to for the last bit: [b][url=http://atomicgameengine.com/blog/development-digest-4/]Atomic Development Digest #4[/url][/b] 

We're also offering free Atomic Pro Indie licenses to contributors, including all Third Party technology. [b]This of course includes Urho3D contributors[/b] :smiley: 

If you're a Urho3D contributor, big or small, see the announcement blog for details and then please keep contributing to make Urho3D even more awesome!

[b][url]http://atomicgameengine.com/blog/announcement-1/[/url][/b]

- Josh

-------------------------

rikorin | 2017-01-02 01:08:31 UTC | #47

Is this even OK? I'm asking not from a legal standpoint, it's about morals. Taking existing (great) engine and adding some features, then giving it another name and trying to sell. Funny that you don't want others to do the same to you, thus stating "The technology can be used for any lawful purpose other than creating a competing game engine." 
That's really sad, when a goal is revenue, not making good software.

-------------------------

cadaver | 2017-01-02 01:08:31 UTC | #48

Is Unity being immoral when they take Recast/Detour library and use it in a commercial engine?

I believe each potential customer can evaluate the value added, and choose the commercial option if they find the value to be good. Note that Atomic's runtime is licensed under MIT so PR's could be made back into Urho core.

Open source development is rarely done from purely altruistic reasons. The reason I began writing Urho3D was to increase my skill in graphics and game engine programming and therefore bring benefit to myself.

-------------------------

sabotage3d | 2017-01-02 01:08:31 UTC | #49

The question is did Urho3d had any PR's from Atomic Game Engine? Currently it looks like Urho3d contributions are used in Atomic Game Engine but not the reverse.

-------------------------

rikorin | 2017-01-02 01:08:31 UTC | #50

[quote="cadaver"]Is Unity being immoral when they take Recast/Detour library and use it in a commercial engine?[/quote]
Recast/Detour library was made specifically to be used in engines, so it's fine. The same way as it's perfectly fine to make a game using Urho3D and sell it. 
Well, I don't want to argue about it, I just shared my opinion on this. 
Shouldn't have done that.

-------------------------

cadaver | 2017-01-02 01:08:31 UTC | #51

No worries, I think it's valuable to have discussions and disagreeing viewpoints on the subject of open source & business morals, as long as the conversation remains polite.

Sabotage3d: good point, Josh has certainly made bugfix contributions to the Urho repo, but I don't think there's any major code from Atomic that has found its way in. From my POV I can safely say that I won't go hunting for code to import from the Atomic repo, simply because of lacking time, but that's not to say someone else couldn't do that. To a degree, the engine is a modified fork, so back-and-forth movement of code isn't necessarily trivial.

-------------------------

jenge | 2017-01-02 01:08:31 UTC | #52

Hey guys,

Atomic is a very different project than Urho3D.  I have great respect for Urho and, as acknowledged in this thread,  wouldn't have gone down the path of creating Atomic if not  for the Urho3D base.  I also contacted @cadaver on the frontend to make sure that, even though the code is MIT licensed, that there wasn't a problem "morally".   If there would have been a problem, philosophically speaking, we wouldn't have gone down this path.  There wasn't, instead we received some great advice, and so we did... 

Urho3D is MIT, the bulk of the code where we use it, the runtime, is MIT.  Urho3D is itself made up of quite a number of FOSS dependencies and we have added even more to the list.  The tooling license, which is not MIT though is full source, does have a very plain language "don't make a competing game engine" clause, as we want it clear that taking the Atomic Editor and running with it, is not desired and WE would have a problem with that...  

The only thing I personally feel weird about is having to rename the Urho3D namespace, when we started it was simply "Engine" and that worked great, if we had started with Urho3D that would also have been fine as I would have created an Atomic namespace alongside it.  Though, we had everything in the Engine namespace, so it made more sense to switch to Atomic namespace and stick with it :/

There are and will be a lot of people finding out about Urho3D through Atomic as we certainly do not hide the lineage.  It wasn't by accident that it is first on the "Friends of Atomic" list :slight_smile:  [url]http://atomicgameengine.com/about/[/url]

There's not much chance we'll make everyone happy about Atomic existing, but do understand that we're a tiny company of 2 people, one household, and have put all of our personal finances into getting Atomic off the ground.  We do want to make a living working on games and supporting Atomic, and have been publishing updates here the entire time. 

There's a full featured free version and we're also offering Atomic Pro for free to anyone who contributes to Atomic, Urho3D, or any of the third party technology used.  So, if you have written ANY code that is used in Atomic, you can use it for absolute free.  [url]http://atomicgameengine.com/blog/announcement-1/[/url]

- Josh

-------------------------

jenge | 2017-01-17 18:54:44 UTC | #53

Hi Guys! 

GameFromScratch.com has published the very first preview of the Atomic Game Engine:

[i]"Well if you are willing to work on an engine that is under development, there is certainly a lot here to like.  If you are looking for a Unity-esque editing experience, but with a much cleaner coding experience and access to the source code, certainly give Atomic a shot?"[/i]

The text preview is available here: [gamefromscratch.com/post/201 ... ngine.aspx](http://www.gamefromscratch.com/post/2015/12/22/A-Closer-Look-at-the-Atomic-Game-Engine.aspx)

There is also a [b]48 minute video[/b] version is available on YouTube:

https://www.youtube.com/watch?v=fRnEs15y-Us

In other news, we've been working on a high performance Chromium based WebView, which will be available soon... and MIT of course :slight_smile:

Here's a GIF of the current multi-tabbed browser example, will be adding a bit more UI to the example soon!

[img]http://docs.atomicgameengine.com/forum_images/MultiWebView.gif[/img]

- Josh

-------------------------

jenge | 2017-01-02 01:09:23 UTC | #54

I've been doing some UI work and really needed quick access to the awesome tb UI debugger.  This allows debugging UI layouts, event tracking, constraints, atlas generation, batching, etc.  It really helps debugging layouts and works in app UI including on device.

It is also really easy to bring up the debugger from script, by simply passing a parent widget for the window: 

[code]var view = new Atomic.UIView();
Atomic.UI.debugShowSettingsWindow(view);
[/code]

... and here is a look at debugging the Atomic Editor UI!

[img]http://docs.atomicgameengine.com/forum_images/UIDebugger_Small.png[/img]

- Josh

-------------------------

practicing01 | 2017-01-02 01:09:23 UTC | #55

Any plans for networking? I'd really like to see multiplayer project templates for an FPS and RTS.

-------------------------

jenge | 2017-01-02 01:09:24 UTC | #56

@practicing01:  We have pretty much done nothing with simulation networking to date.

Put together a quick 3D WebTexture example:

[img]http://docs.atomicgameengine.com/forum_images/WebView3D.gif[/img]

Here's the script:

[github.com/AtomicGameEngine/Ato ... Texture.js](https://github.com/AtomicGameEngine/AtomicExamples/blob/master/WebTexture/Resources/Components/WebTexture.js)

Need to add page interaction in 3DDDDDDD  :astonished: 

- Josh

-------------------------

Calinou | 2017-01-02 01:09:26 UTC | #57

Have you considered publishing the Atomic Game Engine under the GPL or LGPL, to allow free use by open source games? This engine quite interests me, but I want to develop a fully free game. This licensing model would allow you to still make money by selling licenses (licensing exceptions) for proprietary games, but users will be able to create fully FLOSS games.

Note that you will probably need to add a GPL exception to link to OpenSSL, if you want to do this.

Thanks in advance for considering this. :slight_smile:

-------------------------

jenge | 2017-01-02 01:09:26 UTC | #58

@Calinou:  Thanks, 100% of the code in deployed games is MIT (or BSD/Apache/etc) which is compatible with (L)GPL code and pretty much every other license out there.  I have considered "dual licensing" the editor code, however the (L)GPL wouldn't be my first choice as those licenses have a ton of baggage and are difficult to parse.  

The community edition of Atomic will continue to be full source and absolutely free.  We also offer [url=http://atomicgameengine.com/blog/announcement-1/]free Pro licenses to contributors[/url] including all third party technology used...

The current licensing seems to be working out pretty well, please note we have been working fulltime on Atomic for over a year now and have put all of our personal finances into the effort.

If you're primary concern is being fully FLOSS, end to end, I can wholeheartedly recommend Urho3D as the best choice around :slight_smile:

- Josh

-------------------------

jenge | 2017-01-02 01:09:29 UTC | #59

A couple of neat things with the new UIWebView, first playing a phaser.io example on a 3D web texture:

[img]http://docs.atomicgameengine.com/forum_images/WebTexture3DBreakout.gif[/img]

.. and TypeScript loaded in the new code editor (Ace/UIWebView), which supports themed syntax highlighting, code folding, autocomplete, basic linting, etc.  It also has support for pretty much every common language JavaScript, TypeScript, C#, etc 

[img]http://docs.atomicgameengine.com/forum_images/AtomicTS.png[/img]

- Josh

-------------------------

jenge | 2017-01-02 01:09:47 UTC | #60

Hello!

We pushed a new binary Dev Snapshot, here are some update notes:

+ High performance Chromium WebView with 2D, 3D, and UI support ([bitbucket.org/chromiumembedded/cef](https://bitbucket.org/chromiumembedded/cef))
+ New integrated JavaScript/TypeScript code editor based on Ace ([ace.c9.io](https://ace.c9.io))
+ New Water Shader, Multi-tab Web Browser, Atomic Drive-in, and Web Texture examples
+ Updated ToonTown example with dynamic physics, improved lighting, and object placement
+ Added scripting support for raycasting in 3D
+ Added UI Debugger to the Developer tools menu for debugging UI layout, batching, and event tracking
+ Support for mixing realtime shadows with lightmaps, currently D3D9/11 only (thanks @mattbenic)
+ Added Asset Database scan/force import to Developer Debug menu
+ Added TSLint to the build process (thanks @shaddockh)
+ Support for EngineConfig in Atomic Player (thanks @mattbenic)
+ Fixed issue with 0 size files in deployment (thanks @mattbenic)
+ Fixed issue with UIView and UITabContainer resizing
+ Fix for TMXLayer2D SharedPtr issue (thanks @rsredsq)
+ Build in parallel with multiple jobs when using xcodebuild
+ Mac and Windows Atomic Editor binaries are now code signed

[img]http://docs.atomicgameengine.com/forum_images/DevSnapshot2116.png[/img]

[b]3D WebView Scene Example[/b]
[img]http://docs.atomicgameengine.com/forum_images/AtomicDriveIn.gif[/img]

[b]Basic Water Shader Example[/b]
[img]http://docs.atomicgameengine.com/forum_images/WaterExample.gif[/img]

[b]Google Maps in the UIWebView Multi-tab browser example[/b]
[img]http://docs.atomicgameengine.com/forum_images/GoogleMapsWebView.gif[/img]

[b]Star Wars![/b]
[img]http://docs.atomicgameengine.com/forum_images/WebViewDevSnapshot.gif[/img]

Download information is available in our forum here: [atomicgameengine.com/forum/#/dis ... apshots/p1](http://atomicgameengine.com/forum/#/discussion/110/atomic-editor-development-snapshots/p1)

Cheers!
- Josh

-------------------------

jenge | 2017-01-02 01:09:54 UTC | #61

I blogged about the 20 year adventure leading to the Atomic Game Engine, 2016 Roadmap, and our plans for moving the technology forward:

[atomicgameengine.com/blog/future-of-atomic-1/](http://atomicgameengine.com/blog/future-of-atomic-1/)

 :smiley: 

- Josh

-------------------------

Bluemoon | 2017-01-02 01:09:54 UTC | #62

Wow... That was one inspiring adventure  :slight_smile: . The resolve to keep pushing on is really encouraging. Kudos

-------------------------

jenge | 2017-01-17 18:55:08 UTC | #63

Created a visualization of the Atomic master branch through March 10th, 2016

https://www.youtube.com/watch?v=orbr9CY_yKA

Super easy to do with [url=http://gource.io/]Gource[/url]

 :smiley:

-------------------------

jenge | 2017-01-17 18:55:47 UTC | #64

Good news everyone! 

### The Atomic Game Engine is now Open Source under the permissive MIT license! :open_mouth: 

We made a blog post with the announcement: [atomicgameengine.com/blog/announcement-2/](http://atomicgameengine.com/blog/announcement-2/)

[img]http://atomicgameengine.com/blog/images/RoboBeach.png[/img]
[img]http://atomicgameengine.com/blog/images/AndroidBuildSettings.png[/img]
[img]http://atomicgameengine.com/blog/images/Atomic_Roboman_Touch.gif[/img]
[img]http://atomicgameengine.com/blog/images/DevSnapshot2116.png[/img]

Cheers!
- Josh

-------------------------

rasteron | 2017-01-02 01:11:11 UTC | #65

Wow, hey nice congrats! :slight_smile:

-------------------------

Modanung | 2017-01-02 01:11:11 UTC | #66

Cool, thanks for opening up! :slight_smile:

-------------------------

hdunderscore | 2017-01-02 01:11:11 UTC | #67

Wow, that's big news ! Thanks !

I'm curious what the plan is-- maybe going for an asset store model?

-------------------------

gawag | 2017-01-02 01:11:11 UTC | #68

Cool.
How is AGE in relation to Urho? Has it developed into a different direction or is it like a current Urho with additional stuff?
What about the development? Are the developments of Urho and AGE going to keep totally separate or will there be some kind of exchanging or merging, which would mean a bigger team on one engine?
Has it conflicting goals or intentional different design decisions?

-------------------------

weitjong | 2017-01-02 01:11:11 UTC | #69

Well, the "core" of game engine which is Urho3D is MIT all these time, so that's not news. Open sourcing the editor part, however,  is a surprising but welcome news.

-------------------------

gawag | 2017-01-02 01:11:11 UTC | #70

[quote="weitjong"]Well, the "core" of game engine which is Urho3D is MIT all these time, so that's not news. Open sourcing the editor part, however,  is a surprising but welcome news.[/quote]

Oh so they didn't change Urho that much and primarily added an editor? Did they change Urho at all and is the editor like an external tool? Or just slightly modified? Could it be used as an alternative to the normal Urho editor?

-------------------------

weitjong | 2017-01-02 01:11:11 UTC | #71

[quote="gawag"][quote="weitjong"]Well, the "core" of game engine which is Urho3D is MIT all these time, so that's not news. Open sourcing the editor part, however,  is a surprising but welcome news.[/quote]

Oh so they didn't change Urho that much and primarily added an editor? Did they change Urho at all and is the editor like an external tool? Or just slightly modified? Could it be used as an alternative to the normal Urho editor?[/quote]
I didn't say that. I believe they do extend on what core Urho3D provides and keep them there. As I understand those code has been licensed under MIT as well in the past, so that not news to me. As for the editor, I have no idea so no comment.

-------------------------

gawag | 2017-01-02 01:11:12 UTC | #72

I've now read this whole thread, parts of their website and their story.
Seems like I've underestimated their success, they've sold over 3000 licenses and have quite some connections.
The forum is slower as the Urho one so I assume their community is smaller.
They made some changes to Urho and pushed it into a slightly different direction with a focus on Javascript and WebGL.
They try to make games under a "THUNDERBEAST GAMES" brand.

I'm wondering what happens now after making their engine and tools free? The prices are already gone and 3000+ sold licenses are not bad but for that price of somewhere between 60$ and 100$ (if I remember correctly) not enough to hold a whole company/team. They seem to be two people.
They seem to have a lot of plans but it also sounds a bit like trying to get money on other ways and maybe reduce their effort in AGE.
Oh they have this uWebKit Unity viewer for 95$: [uwebkit.com/store/](http://uwebkit.com/store/)
Maybe that and possible other things sell quite well.

So there's kinda a commercial project using Urho. Not a lot of manpower though but they seem to be really effective in getting stuff done.
Hm, so what could be done with this situation? I guess some things could be exchanged between both engines and others have to be kept separated due to the different goals.

I came to Urho3D by looking for a free software engine after more or less bad experience with Irrlicht, CrystalSpace and Ogre. I don't know how good Urho3D is currently in relation to all the other engines (as in Top 10, Top 5, or Top 3 or whatever) but it seems really good from a technical point of view as I've heard a lot. I read that Urho mostly lacks stuff like editors and other tools compared to the big commercial engines, with AGE there seems to be a step in that direction though.

Project "Let's catch up with the big engines like Unreal, CryEngine and Unity". :wink:

-------------------------

hdunderscore | 2017-01-02 01:11:12 UTC | #73

AGE has a quite a few changes compared to urho core, including javascript and C# bindings and chromium built in. I imagine with much of the hard work done in atomic, porting back to urho would be a smaller task than implementing them from scratch, but still no small task either way.

-------------------------

gawag | 2017-01-02 01:11:12 UTC | #74

[quote="hd_"]AGE has a quite a few changes compared to urho core, including javascript and C# bindings and chromium built in. I imagine with much of the hard work done in atomic, porting back to urho would be a smaller task than implementing them from scratch, but still no small task either way.[/quote]
Yeah the question is also: will AGE keep like a different engine or will it be more like optional extensions extending Urho? The Chromium build in looked really good for example, could that be a library?
AGE could be a bundle consisting of Urho and some extensions and an external editor or whatever. Like a Linux Distribution. Maybe a lot of what they added/changed could be made into extensions/libraries for Urho. So that the "AGE project" would be basically working on the normal Urho and their extensions and other stuff.
No idea how much they changed Urho and which parts could be relatively easily made extensions for Urho itself.
Merging the projects would be a big step forward.

-------------------------

weitjong | 2017-01-02 01:11:12 UTC | #75

I could be wrong but I recall the CEF3 work was being done by Enhex first. [topic1021.html](http://discourse.urho3d.io/t/cef3-web-browser-integration/993/1)

-------------------------

Shylon | 2017-01-02 01:11:12 UTC | #76

If The Atomic Game Engine team was focusing only on Urho3d then we had more complete Game Engine, if Panda3d, Ogre3d, Irrlich and .... (a very long list of free engines) team and contributes was focusing on one unit engine, then we had a very good community driven game engine, LIKE BLENDER (a good free 3d software), the main problem is everyone wants to build an engine, and halfway they sucks, I think we should ask other developers around world for contribution to build Urho3d (or any name) a unite game engine (more like Merging all engine to one, of course not code but merging and grouping people together), however if you probably ask them, most of them will reject.

So people please, do not make another engine, just focus on one, Urho3d has this potential to become one unite game engine.

-------------------------

hdunderscore | 2017-01-02 01:11:12 UTC | #77

There are other factors to consider. For one they probably initially thought to not release the engine open source, so making their own fork made sense. Then they open sourced it, but still they get to decide the quality standards that are acceptable for their engine-- by adhering to their own standards they could develop new features faster rather than waiting for their work to receive approval via pull request. Also, by making their own engine they didn't need to worry about doing things that might not fit the goals of Urho3D.

I agree, I've seen many similar featured open-source engines with huge amounts of work put into them that might have been better if they focused effort into one engine (eg, urho3d, atomic, maratis, polycode, minko.io, gameplay3d), but in the game engine world sometimes it's better to start new every few years to keep up with new technology, than to beat a dead horse (eg, blender game engine, irrlicht, source, quake, etc ).

-------------------------

gawag | 2017-01-02 01:11:12 UTC | #78

[quote="Shylon"]If The Atomic Game Engine team was focusing only on Urho3d then we had more complete Game Engine, if Panda3d, Ogre3d, Irrlich and .... (a very long list of free engines) team and contributes was focusing on one unit engine, then we had a very good community driven game engine, LIKE BLENDER (a good free 3d software), the main problem is everyone wants to build an engine, and halfway they sucks, I think we should ask other developers around world for contribution to build Urho3d (or any name) a unite game engine (more like Merging all engine to one, of course not code but merging and grouping people together), however if you probably ask them, most of them will reject.
So people please, do not make another engine, just focus on one, Urho3d has this potential to become one unite game engine.[/quote]
Yeah getting hobbyists together is really hard.

It's quite a while since I last checked Irrlicht, Crystalspace and Ogre. Ogre seems to be active under the hood but Crystalspace looked pretty dead the last time I checked. As I was searching for a new engine I also found one called Delta3D but I never really looked into it because I randomly looked at Urho3D first. It seems kinda active but not that much: [delta3d.org/](http://delta3d.org/)
Urho has a great potential, especially compared to Ogre, as it is a complete Game Engine and not just a 3D Engine. And it usually just works on any system and is relatively polished. Crystalspace is/was also a complete Game Engine but as I used it, it was really buggy, super slow and most stuff wasn't working properly.

As I already mentioned several times: It would be a giant promotion to have various very simple games that proof and show what Urho can do, as in "Yeah that's also possible with Urho". Can be inspired by successful games in various genres. Some of those may yield new features for Urho, or find bugs, or improve stuff or introduce new systems as libraries.

Would be also great to have a professional team working on a game with Urho that contributes stuff back.
We really need [b]organized manpower[/b]. Seems like we have a relative big community but everyone is kinda working on his own. Who would work with others?

-------------------------

cadaver | 2017-01-02 01:11:12 UTC | #79

Very nice move on Atomic's part!

Yeah the core idea of hobbyism & hobby open source participation (as opposed to corporate open source) is to work on things you're interested on. Unfortunately it's unlikely for anyone's hobby passion to be fulfilling someone else's dreams, so I agree it's hard to get together a "critical mass" group of talented developers who have the same aim.

If we speak realistically, Urho / Atomic is a good implementation of game engine state of the art from a few years back. It's certainly usable for getting games done, and the architecture is solid. However it's not necessarily suitable for the more modern and high-performance methods (Data-oriented design, more utilization of CPU cores, getting good utilization of new to-the-metal graphics APIs). Though I can't think of any other permissive open source game engines that are ready for that either (*), and most proprietary engines, at least those with a long legacy probably aren't any better. What I'm saying is that if your goals are high, Urho may not be the "final" open source base to build on so to speak, but you'd be better off starting a new "god" engine project :slight_smile:

(*) Ogre2+ is heading in a future-prepared direction, but it's just a rendering engine. It makes choices that are oriented around the "AZDO" approach (such as creating large vertex buffers and managing them manually) that may not be universally good choices, for example on mobiles. From what I read the focus on optimizations makes the API hard to use.

-------------------------

Enhex | 2017-01-02 01:11:13 UTC | #80

Note that using the latest technologies isn't desirable, since some people won't have computers that support them.
Even OpenGL 3.2 isn't supported by the low end Intel HD Graphics GPUs.

Unless you're going to have AAA multi-million $$$ game production it's unlikely that you'll really need to squeeze every last drop of performance to get your "cinematic" 24 FPS using the newest technologies.
If you don't have that kind of requirement it's better to use older tech and support more potential users.

For my project I'm using full detail models(didn't try to optimize them), and with GTX670 it runs at 200(max) FPS.

-------------------------

codingmonkey | 2017-01-02 01:11:13 UTC | #81

>Intel HD Graphics GPUs.
My laptop igf - Intel4000HD supports OpenGL 4.0 (Intel(R) HD Graphics 4000 with 188 ext.)  
So I thinks 3.2 is very very old gapi, from previous century :slight_smile:

-------------------------

cadaver | 2017-01-02 01:11:13 UTC | #82

But factor in Linux drivers and I don't know when you can start using recent-ish OpenGL if you don't want to lock out random parts of your audience :slight_smile:

-------------------------

jenge | 2017-01-02 01:11:13 UTC | #83

@everyone THANKS!

@cadaver So far so good on the MIT, happy to share the same license along with the code!  Major bump in traffic, being picked up places like Phoronix, with a Urho3D shoutout (though he lost the link, boo!) [phoronix.com/scan.php?page=n ... ine-Opened](http://www.phoronix.com/scan.php?page=news_item&px=Atomic-Game-Engine-Opened)

@hd_ Those are some good insights and definitely factors, I would say that Urho3D has a higher code standard.  We've been in more of a "production" mode on Atomic, though it does have a higher standard than much stuff I have seen :wink:

@weitjong I wrote Atomic's CEF3 integration, been doing browser integrations a long time.  Here's one I did when I worked at GarageGames on Torque3D in 2009: [youtube.com/watch?v=ymI80FKBXfE](https://www.youtube.com/watch?v=ymI80FKBXfE)

@gawag We have nothing to do with that Thunderbeast Entertainment site, and "they" is I, and I am on the forums, so if you have a question might just be easier to ask than make so many assumptions  :smiley: 

@Shylon Indeed, however I have very precise ideas on the tech and how we're going to build games with it.  Lots of stuff in Atomic wouldn't make sense to PR against Urho3D (and vice versa).  There isn't any way we would have gotten to this point in around 16 months if we had taken any other approach.  THUNDERBEAST GAMES LLC has 1 coder, that's me, and some awesome contributors

I'd like to make it easier to move code between the projects for sure, one snag is that at one point Urho's "Engine" namespace was renamed to "Urho3D", which had a cascade effect on Atomic as all our stuff and script bindings were in the Engine namespace, so the Urho3D namespace became the Atomic namespace.  

- Josh

-------------------------

weitjong | 2017-01-02 01:11:13 UTC | #84

[quote="jenge"]@weitjong I wrote Atomic's CEF3 integration, been doing browser integrations a long time.  Here's one I did when I worked at GarageGames on Torque3D in 2009: [youtube.com/watch?v=ymI80FKBXfE](https://www.youtube.com/watch?v=ymI80FKBXfE)[/quote]
Don't get me wrong. I wasn't implying anything with my earlier comment. I just want to say that I have seen the CEF3 integration (using Urho3D as the game engine, of course) the first time there.

-------------------------

gawag | 2017-01-02 01:11:14 UTC | #85

[quote="cadaver"]
If we speak realistically, Urho / Atomic is a good implementation of game engine state of the art from a few years back. It's certainly usable for getting games done, and the architecture is solid. However it's not necessarily suitable for the more modern and high-performance methods (Data-oriented design, more utilization of CPU cores, getting good utilization of new to-the-metal graphics APIs). Though I can't think of any other permissive open source game engines that are ready for that either (*), and most proprietary engines, at least those with a long legacy probably aren't any better. What I'm saying is that if your goals are high, Urho may not be the "final" open source base to build on so to speak, but you'd be better off starting a new "god" engine project :slight_smile:

(*) Ogre2+ is heading in a future-prepared direction, but it's just a rendering engine. It makes choices that are oriented around the "AZDO" approach (such as creating large vertex buffers and managing them manually) that may not be universally good choices, for example on mobiles. From what I read the focus on optimizations makes the API hard to use.[/quote]
So "modern engines" use a faster but harder to use approach? Sounds bad for beginners / non-expert game programmers. Generally and optimally one wants a good mix between usability and performance.
Could the approaches be mixed? Like in doing for example a high performance part like vegetation with a more Data-oriented design and normal stuff where one doesn't need every bit of performance where usability is more important? Like in putting the hard to use but faster stuff in libraries.

How high is the cost for being more "traditional" and "user oriented"? Like 10% slower? 20%? 30%?

-------------------------

Shylon | 2017-01-02 01:11:14 UTC | #86

Personally I think it is easier compare to 10 years ago, see C++ now with c++11 or 14 it is like python, see GDC and CPP conference engineers all shares their tech and let people know for new techniques, hard part is inventing a new ways, see for example Unreal implemented PBR/PBS and now engine without PBS is not acceptable for most people.  :slight_smile:

-------------------------

dragonCASTjosh | 2017-01-02 01:11:14 UTC | #87

With the community we have i believe its possible to keep up with allot of they key engine tech such as PBR, the bigger question is where it fits into Atomic and Urho as they each have there minimal target platforms and some of the techniques wont work on these platforms for example getting Screen Space Reflections on mobile and web platforms is extreamly slow. To keep up with everything we will need developers to devote most of there time to areas of the engines for example im happy to dedicate myself to rendering.

-------------------------

cadaver | 2017-01-02 01:11:14 UTC | #88

[quote="gawag"]
So "modern engines" use a faster but harder to use approach? Sounds bad for beginners / non-expert game programmers. Generally and optimally one wants a good mix between usability and performance.
Could the approaches be mixed? Like in doing for example a high performance part like vegetation with a more Data-oriented design and normal stuff where one doesn't need every bit of performance where usability is more important? Like in putting the hard to use but faster stuff in libraries.

How high is the cost for being more "traditional" and "user oriented"? Like 10% slower? 20%? 30%?[/quote]
Any percentage figures are extremely hard or impossible to give. Note that from what I understand I'd put both Unity and Unreal4 in the same category as Urho, which rather value usability over super performance, and also have "fat" entities/components with logic inside them (Of course UE4 does some advanced stuff rendering-wise, and has more features all around.) 

Some examples of a data-oriented & threading friendly, but harder for user operations, would be raycasts and navigation. Traditionally these execute synchronously in the main thread, causing immediate framerate drop or stall if they are too slow, but the API use is very simple: you get the result immediately. In an "advanced" engine you would submit a task to do a raycast or navigation query, these get taken for execution by the job scheduler, and you get the result sometime later, without stalling the main thread.

If you're interested, read up on console developers' engines, for example Naughty Dog's. They typically had to take up multicore, memory and SSE related optimizations in their proprietary engines into much greater use earlier, due to for example the PS3's architecture.

-------------------------

gawag | 2017-01-02 01:11:15 UTC | #89

[quote="cadaver"]
Some examples of a data-oriented & threading friendly, but harder for user operations, would be raycasts and navigation. Traditionally these execute synchronously in the main thread, causing immediate framerate drop or stall if they are too slow, but the API use is very simple: you get the result immediately. In an "advanced" engine you would submit a task to do a raycast or navigation query, these get taken for execution by the job scheduler, and you get the result sometime later, without stalling the main thread.

If you're interested, read up on console developers' engines, for example Naughty Dog's. They typically had to take up multicore, memory and SSE related optimizations in their proprietary engines into much greater use earlier, due to for example the PS3's architecture.[/quote]

So a big point is getting stuff out of the rendering thread?
Can Urho be "easily" used to calculate render independent stuff like AI and physics in different threads? Could that be made possible/easier?

When programming an AI I think one doesn't really care about the rendering loop and more about checking positions of enemies, players and other things and about the navigation mesh. Can separate threads change the scene like move nodes or apply forces to physical objects? Could be tricky to schedule every small operation in an efficient way, but could be possible. What can Urho do currently in that direction?

-------------------------

cadaver | 2017-01-02 01:11:15 UTC | #90

Urho does the same as Unity which allows to put script / logic hooks to physics update substeps (FixedUpdate), which makes it rather hard to implement physics in a separate thread. If we disallowed that, then it could be threaded, provided there's added synchronization, but again it's a performance <-> usability tradeoff.

When you program in C++ you can go crazy with your own background-threaded algorithms, especially if they don't need to modify the scene, or can for example post their updates to some queue handled by the main thread.

As a generic mechanism for threaded AI or logic execution inside the engine, especially when accounting for scripting, I don't have an idea how it should or could be done.

EDIT: for those interested, I looked a bit more in detail how UE4 does things:
- There is a game logic thread and a render thread. Both can submit jobs for additional worker threads,
- Only render thread actually handles GPU objects. Game logic thread must pass "commands" to modify them.
- For rendering, "proxy" objects exist of renderable game objects on the render thread side. This and the point above is a significant complication compared to e.g. Urho
- Physics runs concurrently with logic on another thread. By default physics is variable framerate and thus FPS affects results. You don't get "fixedupdate" callbacks for logic, but optionally fixed time substepping can be enabled. I didn't check in detail how the logic and physics results are merged (e.g. at what point in time a command like "add force to game object" is applied to the physics engine.)

-------------------------

gawag | 2017-01-02 01:11:20 UTC | #91

[quote="cadaver"]Urho does the same as Unity which allows to put script / logic hooks to physics update substeps (FixedUpdate), which makes it rather hard to implement physics in a separate thread. If we disallowed that, then it could be threaded, provided there's added synchronization, but again it's a performance <-> usability tradeoff.[/quote]
That hooking vs. threaded physics and AI option could be switched with a CMake option and defines for 0 runtime cost and proper compiler errors (non existing functions). Or those functions are actually called in separate threads... I still would suggest an optional option as one has to pay more attention when working asynchronously.

[quote="cadaver"]When you program in C++ you can go crazy with your own background-threaded algorithms
...[/quote]

I've also been thinking about what options there are.
Someone on the IRC posted this technique: [panda3d.org/blog/triple-your-frame-rate/](http://www.panda3d.org/blog/triple-your-frame-rate/)
I've seen that technique before somewhere else, it splits the independent rendering steps into different threads to have three "slices".
Could that be done with Urho as well?

About other ways to multi thread stuff: I came up with two possible ways.
One solution is the job scheduling that you mentioned the Unreal engine uses. Such a job queue sounds rather complicated and like having a real overhead.
The other possible solution I came up with is to partly synchronize threads with mutexes and/or conditional variables. All the stuff that can only be done at a specific moment (when no one else is modifying the scene for example) is done in serial and not parallel. I would have to look into mutexes and conditional variables again but it's kinda like this:
[code]
void NonMainThread()   // multiple threads do this, like for AI, physics or whatever
{
    // plan all operations like pathfinding and the actions to do
    ...
    MutexGuard mg=MutextMainThread.GetMutexGuard();    // wait until the MainThread is ready and lock a mutex via a RAII mutex guard
    // execute all planned actions in this serial part (AKA "synchronized part")
    ...
}   // the mutex guard is destroyed and automatically unlocks the mutex to get back into parallel mode
...
void Update()   // main thread
{
    ...
    MutexMainThread.unlock();  // let every waiting "worker thread" do his planned actions in serial. Every worker thread should
                               // do only one "set" of actions (not unlock, replan and lock again -> possible deadlock).
    MutexMainThread.lock();    // go back into parallel mode
}
[/code]
I assume the non-main threads can do stuff like scene manipulations if it is synchronized like that with the main thread? Or is there some weird thread ownership like Qt has?

The second method is pretty manual and avoids a possible giant and slow job queue. Also it is more flexible as it can do everything and doesn't have to rely on special actions queued (depending on the implementation).

All variants I can think of are not that easy/"idiot safe" as a scene change (or another non-thread-safe action) may still be tried in the parallelized part and not the serial part where it is actually safe.

[quote]EDIT: for those interested, I looked a bit more in detail how UE4 does things:[/quote]
Hehe :stuck_out_tongue:
This interesting "problem" occupied me as well since the multi threading idea came up. Had a partly written reply lying here since then and kept thinking about it.

Is it safe to read from the scene (like node positions or doing raytraces) when the main thread is rendering? The parallel mode has to be entered for every non-tread-safe operation of course. Usually most machines do also have atomic operations where expensive mutexes can be avoided but I doubt we can really use that as most stuff requires multiple operation without someone getting inbetween. BTW: on x86 every read is atomic even without using the special atomic instructions (manually or via C++11 std::atomic).

Edit: I think the synchronizing has to be done with a mutex for every thread that is unlocked by the main thread when it can do one "set". Has been quite a while since writing my last thread pool or something similar. But unconditional variables had been also required for something in that direction...
Edit2: Oh! I thing the conditional variables are required when one doesn't want to lock the main thread and just lock or unlock worker threads. Which is not the case here so it should work with simple mutexes. If I'm not mistaken.

-------------------------

cadaver | 2017-01-02 01:11:20 UTC | #92

We already have a simple job system in Urho which is used by the rendering and animation, and you can also use it for your own tasks. There is no dependency tracking for them though.

In general it should be safe to read the scene, at least if you're sure that the main thread logic isn't simultaneously destroying the scene nodes or components you're accessing. Just be aware the reading a node's world position can actually trigger modifications when it has to refresh the position from the node hierarchy, but that should converge to the same result even if being called from multiple threads.

-------------------------

boberfly | 2017-01-02 01:11:27 UTC | #93

Hey cadaver,

You might know of this one already, but I always found this engine's concept of making everything a task (and the YaTS taskpool) to be really interesting:
[url]http://bouliiii.blogspot.ca/2011/11/point-frag-distributed-game-engine.html[/url]
[url]https://github.com/bsegovia/point-frag/blob/master/src/sys/tasking.hpp[/url]

Stealing the thread here, but I thought I'd mention it as we're comparing other engines and their approaches...

-------------------------

cadaver | 2017-01-02 01:11:28 UTC | #94

Thanks for posting! I've been searching for "next-gen" open source engines having e.g. an advanced threading setup, this may well be worth a look.

-------------------------

boberfly | 2017-01-02 01:11:29 UTC | #95

Raytracing occlusion culling is also interesting, it might be faster in a small buffer with a fast BVH structure than software raster occlusion culling, like his blog suggests and more threadable and more tolerant to higher poly-count occluders. Maybe throwing something like Embree at it might do the trick... :slight_smile:

-------------------------

jenge | 2017-01-02 01:12:46 UTC | #96

[url=http://docs.atomicgameengine.com/forum_images/LinuxUpdates.png][img]http://docs.atomicgameengine.com/forum_images/LinuxUpdates_Thumb.png[/img][/url]

Hey all, lots of good stuff going on with Atomic.  There have been significant updates to the Atomic Editor under Linux over the last couple months.  It is still a work in progress, though is getting closer to having a binary distribution :slight_smile:

We have improved TypeScript project support, including compilation of TS in the Atomic Editor!

[img]http://docs.atomicgameengine.com/forum_images/TSCompilation.png[/img]

There has also been work on better API docs, [url]http://docs.atomicgameengine.com/api/modules/atomic.html[/url] as well as a bunch of other updates and bug fixes.  

There is now a "Master Builds" section on the download page for recent editor builds with Windows, OSX, Android, iOS, and WebGL deployment, with Linux being in progress.  This will be automated, however for now it is still best to strategically select a commit :slight_smile: [atomicgameengine.com/download/](http://atomicgameengine.com/download/)

I really want to apply some focused work on getting the Atomic and Urho source trees closer together, as to facilitate easier code migration between them.  This is a pretty big task at this point and probably needs to be broken up into stages.  

- Josh

-------------------------

jenge | 2017-01-02 01:13:16 UTC | #97

Hey all,

I've been putting a lot of work into C# scripting, here's a look at realtime C# inspector fields with the Monaco code editor from VSCode, which is integrated via the Chromium WebView :slight_smile:

[img]http://docs.atomicgameengine.com/forum_images/CSharpInspector.gif[/img]

The editor also integrates with Visual Studio and VSCode and the tooling is capable of generating solutions, here's the same project in VS:

[img]http://docs.atomicgameengine.com/forum_images/VSIntegration.PNG[/img]

Atomic supports JavaScript, TypeScript, C#, and languages that ride on JavaScript and C#, like Haxe/CoffeeScript/Etc.  This is a look at the TypeScript project support with full intellisense provided by Monaco:  

[img]http://docs.atomicgameengine.com/forum_images/MonacoTS.gif[/img]

There has also been work on better Android deployment from the editor with support for release apk's:

[img]http://docs.atomicgameengine.com/forum_images/AndroidReleaseAPK.jpg[/img]

Whew!  I am looking forward to merging Urho master soon here, it has been some months and a goal is to get the codebases closer together.  The graphics agnostic headers will be a huge win as well :slight_smile: :slight_smile: :slight_smile:

- Josh

-------------------------

rku | 2017-01-02 01:13:16 UTC | #98

I usually say that integrating with existing IDEs instead of reinventing the wheel is better but wow.. this does blow away your mind.. Not many engines can boast script editor with full autocompletion, syntax highlighting etc.. Even if it is made in javascript :wink: Truly amazing work.

[quote]I really want to apply some focused work on getting the Atomic and Urho source trees closer together, as to facilitate easier code migration between them. This is a pretty big task at this point and probably needs to be broken up into stages. [/quote]

As reiterated multiple times in [url=http://discourse.urho3d.io/t/overhaul-proposal/2087/1]this[/url] thread - urho3d could benefit from c++ editor immensely. Since you atomic engine has such thing and engines are basically brothers maybe it would be in the realm of possibility for engines to share at least that part? I bet cadaver would be very happy if that happened especially since atomic editor has way more features and is written in c++.

-------------------------

cadaver | 2017-01-02 01:13:17 UTC | #99

If the editor code comes from Atomic it still doesn't change the fact that it would need a (mostly) steadily contributing developer to handle updates, required Atomic -> Urho changes and editor issues. I assume it will be less work than writing an editor from scratch, though.

However what makes greatly sense to me is to think of Atomic as the IDE and project management built on top of Urho, instead of reimplementing those in Urho. It isn't exactly a reality right now since Atomic has grown so different and has a different featureset in some respects, but it could be that way if the codebases are brought closer.

-------------------------

jenge | 2017-01-02 01:13:17 UTC | #100

The first version of the editor was solely in C++, though as soon as we had mature UI script bindings and especially TypeScript support, the UI was rewritten in TS.  Atomic has a "ToolCore" library which is shared by command line tooling and the Atomic Editor.  So, asset handling, etc are in C++ and steered by script.

Atomic is geared to be a production tool for shipping apps and games.  This means we have deadlines that Urho does not and I don't foresee Atomic and Urho merging.  Though, it should definitely be easier to move code between the two, or other forks of them.   

Urho has proven a great base to build on and even after all this crunch, I still love working with the code.  I am so going to make a game with all this stuff! :smiley:

-------------------------

