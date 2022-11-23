rogerdv | 2017-01-02 01:08:44 UTC | #1

Is this going to make it into Urho3d, in the future? It seems awesome, the are offering TressFX, GeometryFX, and many interesting things, under MIT license.

-------------------------

bvanevery | 2017-01-02 01:08:52 UTC | #2

Well you could try to code it up.   :smiley: 

Since AMD just announced this, its future and relevance to industry is uncertain.  So, absent personal enthusiasm, it would probably be a lot of work and risk for Urho's 2 core developers to take on, I reckon.

Generally what worries me in the health and success of any open source 3d engine, is the development of an [i]ecology[/i], not more technology.  By that I mean, demos, samples, and even complete games that actually work.  Developers who stay in the orbit of the engine and continue to keep things working, rather than moving on to something else.  Several years ago I did a serious evaluation of Ogre3D.  I went through their entire website building every single project that was listed as an "Ogre based project".  Lots of them didn't work anymore and I moved them all to an "inactive projects" page.  By the time I finished that the body count was high.  The actual ecology of Ogre was a lot smaller than it had looked.  It demonstrated some kind of heydey where people were doing a lot of stuff, but then somehow drifted away and left things to bitrot.  Maybe the Ogre APIs changed enough that people didn't want to do the work.  Maybe Ogre was too slow to adopt newer 3D APIs, particularly DX11.  Heck they only claimed to have done that [i]this year[/i] which I think is pretty sad really.  I think I did that website cleanup 3 years ago, and I remember someone was just sorta getting started with DX11 back then.  Reading their forums, I remember a lot of anti forward movement energy, that they weren't going to take on newer APIs "just because".  I'm guessing their heyday probably followed a fairly predictable curve of when DX9 was strongest.  2015 is pretty late to be getting on with DX11 frankly.  We've got DX12 now to say "won't take on a newer API 'just because'...."

Anyways back then I ditched Ogre.  I'd done my due diligence, and I left a clean kitchen for the next guy trying to figure out the same thing.  That was disheartening because at the time, Ogre seemed to be the best that pure open source had to offer.  Their major strategic mistake IMO was insisting on being a 3d rendering engine, not a 3d game engine.  So they wouldn't bless any particular scripting language for instance.  You can't maintain a developer ecology without one, people just don't want to do heavy duty game development only in C++.  Things like Lua bindings would be maintained 3rd party.  As they'd amount to 1 guy working on it, that 1 guy would eventually get bored, and the binding would bitrot.

It seems Ogre will stay that way, because the monetization model has become incorporating it into commercial game engines.  Like that guy who ran off and did NeoAxis.  Well at least he had all that motivation to do the integration work, the potential of money at the end of the rainbow, but it doesn't help pure open source any.  Pure open source is capable of accomplishing quite a lot, but it does require people to evaluate and work towards [i]sustainable [/i]project directions.

I'm guessing that GPUOpen is not a sustainable ambition for Urho3D.  A highly motivated individual could always prove me wrong.  Just remember that boredom is always the enemy.  You think you have all this time to do things in open source... well you don't.  You will eventually get bored.  You have to accomplish exciting, sustainable things [i]before [/i]you get bored.  Otherwise you'll turn around and realize you're bored, you're not getting paid for it, it's not doing you any good, and you're Done [TM].

-------------------------

rogerdv | 2017-01-02 01:08:52 UTC | #3

Precisely because of my bad experience with Ogre3d is why I think that engines need to develop technology, besides ecology. The whole point of a game engine, IMHO, is having tools that prevent you  (the developer) from having to work integrating stuff like physics, or creating tools like scene editors. I see GPUOpen as an opportunity to have state of the art features in open source engines, and the cost of integrating it will be lesser than implementing it from scratch. Why not to take it? Of course, it is wise to wait and see what really happens with this initiative.

-------------------------

bvanevery | 2017-01-02 01:08:52 UTC | #4

[quote="rogerdv"]Precisely because of my bad experience with Ogre3d is why I think that engines need to develop technology, besides ecology.[/quote]

Ogre was [i]too [/i]slack in that regard.  I mean come on, can't stay married to your codebase and do DX9 forever.  I also recall their lead dev being really negative about DX11 for awhile.  That's not a good tone to set in a project, the sort of "ah no way in hell, this isn't even really important" energy.  People tend to follow along the lead in that, and just shut up, not even dare to contribute for fear of being shot down.  It's better to say, you can have it if you'll do it.

[quote]
The whole point of a game engine, IMHO, is having tools that prevent you  (the developer) from having to work integrating stuff like physics, or creating tools like scene editors. I see GPUOpen as an opportunity to have state of the art features in open source engines, and the cost of integrating it will be lesser than implementing it from scratch. [/quote]

Ok but your feature list for any given game you actually want to make, and mine, and someone else's, are not the same.  I doubt I care about physics at all.  I definitely don't care on these cheesy business class laptops I'm currently kicking around, trying to see what I can get out of them.  No CPU or GPU budget for that sort of thing.  I think a little bit about what I might do with some kind of physics somewhere, but it's not core to my thought processes as a game designer.  I think about things like AI, units killing each other, and procedurally generated content.  So programming languages are really important to me.  Importers from modeling / animation packages are not.  I haven't weighed in on the "language binding" discussion because I haven't seen how far I can get with Lua or AngelScript yet.  I have an ambition to write my own language, something more like a high level assembler or forth, but I'm not going to talk about my own needs or desires there until I've actually done something.  Maybe I won't even need it.  But part of why I sought out a MIT licensed 3d game engine codebase like Urho3D, is to provide the scaffolding for proving what I need in this ultimate game development language.

My experience is that volunteers can't be "rationed out" as arbitrary labor for arbitrary projects.  They work on their own priorities.  They can do a *lot* of work on something if they're really into it.  Good volunteer leaders get out of the way of people like that, to see what they can gain from their enthusiasm.  Bad leaders say "no."  So the point is, if it's your enthusiasm, run with it!  But don't expect others to just run with it, whatever "it" is, just because you're enthused.  They probably have other things they're enthused about, that are commanding and sucking away their energies.  I'm saying in OSS, we primarily have the power of leading by example.

[quote]Why not to take it?[/quote]

'Cuz it's a lot of work that someone has to do.  Do you want to do it?  The 2 core devs seem pretty open to people taking on "great things" if they're going to make them work + maintain them.  The latter isn't a trivial commitment either.  Maintenance is ongoing work.

[quote]Of course, it is wise to wait and see what really happens with this initiative.[/quote]

Yeah even in your shoes, assuming you're highly motivated to take this on, I'd caution you.  It's best to wait and see if anyone else cares.  What if you poured blood on the table for Mantle, for instance?  Totally irrelevant now.

What about blood, sweat, and tears for Oculus Rift, or any of the other recent VR wunderkinds?  Where the heck are any of those things??  Steam Machines, are they going anywhere?  Ouya?

-------------------------

rogerdv | 2017-01-02 01:08:53 UTC | #5

[quote="bvanevery"][quote="rogerdv"]Precisely because of my bad experience with Ogre3d is why I think that engines need to develop technology, besides ecology.[/quote]

Ok but your feature list for any given game you actually want to make, and mine, and someone else's, are not the same.  I doubt I care about physics at all.  I definitely don't care on these cheesy business class laptops I'm currently kicking around, trying to see what I can get out of them.  No CPU or GPU budget for that sort of thing.  I think a little bit about what I might do with some kind of physics somewhere, but it's not core to my thought processes as a game designer.  I think about things like AI, units killing each other, and procedurally generated content.  So programming languages are really important to me.  Importers from modeling / animation packages are not.  I haven't weighed in on the "language binding" discussion because I haven't seen how far I can get with Lua or AngelScript yet.  I have an ambition to write my own language, something more like a high level assembler or forth, but I'm not going to talk about my own needs or desires there until I've actually done something.  Maybe I won't even need it.  But part of why I sought out a MIT licensed 3d game engine codebase like Urho3D, is to provide the scaffolding for proving what I need in this ultimate game development language.[/quote]

Nobody said that making games or game engines were easy. The problem with a game engine is that you have to consider the needs of a hughe amount on developers. I want to make a 3D RPG that looks good (but first Im forced to make a simple 2D game to solve a lot of problems I have), you want AI and procedural content, somebody else will have totally different needs.  The core team has to please all of us, as long as it suit their idea and the needs are not plainly impossible.

[quote]
'Cuz it's a lot of work that someone has to do.  Do you want to do it?  The 2 core devs seem pretty open to people taking on "great things" if they're going to make them work + maintain them.  The latter isn't a trivial commitment either.  Maintenance is ongoing work.
[/quote]

Im not good enough for that. If I were, I would be contributing to the engine right now.

[quote]
[Yeah even in your shoes, assuming you're highly motivated to take this on, I'd caution you.  It's best to wait and see if anyone else cares.  What if you poured blood on the table for Mantle, for instance?  Totally irrelevant now.

What about blood, sweat, and tears for Oculus Rift, or any of the other recent VR wunderkinds?  Where the heck are any of those things??  Steam Machines, are they going anywhere?  Ouya?[/quote]

Technologies are created, and some of them die. Well, I would say that all of them die, eventually (OpenGL is dying, to be replaced with Vulkan). But some of them last enough to be worth the effort of working on them.
I just think that GPUOpen is offering too much to just discard it.

-------------------------

bvanevery | 2017-01-02 01:08:53 UTC | #6

[quote="rogerdv"]
Nobody said that making games or game engines were easy.[/quote]

It isn't, but our job as end users is to make [i]games[/i].  Engines and technology are a means to an end.  We don't need infinite amounts of technology to make a good game.  I've spent 4 full time months just polishing up someone else's [url=http://wesnoth.org/]Battle for Wesnoth[/url] campaign.  4 man months!  Not working on any engine.  Not producing any art assets.  Just tweaking dialogue and tons of game balancing.  "To Lands Unknown" had a lot of really inspiring things going for it back in the day, but it sure didn't play well.  The lead dev simply didn't have much experience writing Wesnoth campaigns.

The point is if you say "I must have amazing new technology X" to write a game, you're not going to get a game done!  Content development itself requires loads of work, loads of refining.  In fairness I could have shaved a lot of time off if I hadn't been working with Wesnoth's WML and had a save game system that could let me restart at arbitrary points in a war after editing something.  Instead I just had to start the scenario from Turn 1 again.  Lessons for the future to reduce iteration time.  Best case it would have still taken me 2 full time months to do the work I did.

[quote]
The problem with a game engine is that you have to consider the needs of a hughe amount on developers.
[/quote]

No, the 2 lead devs for an OSS project do not.  What they can do, is offer a tent where you can make yourself the 3rd lead dev, or someone else can become the 4th lead dev, etc.  I haven't asked about Uhro3D's financials, how anything is sustained.  But I seriously doubt there's any equation that says, "worrying about lots of people's problems, makes us money, and sustains our efforts."  It's open source.  People who want big things done, usually have to contribute them.  I've restricted all the issues I've filed to very, very small things.  Things I could have eventually done myself if Weitjong weren't so fast with CMake.

[quote]
 I want to make a 3D RPG that looks good (but first Im forced to make a simple 2D game to solve a lot of problems I have), you want AI and procedural content, somebody else will have totally different needs.  The core team has to please all of us, as long as it suit their idea and the needs are not plainly impossible.
[/quote]

I hope I'm not just picking on your choice of words when I say no, they don't.  I don't expect anyone to write AIs for me, or integrate languages for me.  I'll get these things done if it helps my own game development.  I'll contribute them if they work out and there's actually some reason someone else would benefit from them.

[quote]
Im not good enough for that. If I were, I would be contributing to the engine right now.
[/quote]

Ah, ok.  Hopefully I've provided some perspective on scale of development.  If one can't do things oneself, I think it best to ask for [i]small [/i]things.   :smiley:  Even small things may take a lot more work than you realize.  I've got a few things I've put in the issue tracker, I know they're very boring to work on.  I filed them so they are not forgotten.  Some day my own development will march on and I'll probably get to them.  Or maybe I get hit by a truck, who knows.

[quote]
Technologies are created, and some of them die. Well, I would say that all of them die, eventually (OpenGL is dying, to be replaced with Vulkan). But some of them last enough to be worth the effort of working on them.
I just think that GPUOpen is offering too much to just discard it.[/quote]

The problem is people in the 3d industry are getting paid to work on all these things, many of which die.  Basically, they're spamming the tech space with whatever wunderkind they think will get their company some attention.  The individual programmer at one of these outfits does not necessarily have to care about their success or failure in the marketplace.  If you're an employee and you don't have any serious stock options, your job is basically a stepping stone for whatever [i]you [/i]personally want to do.  Not what's best for the company, best for the world, or best for indie game developers working on open source stuff.  You can barf a ream of code and be gone next year.  I've seen it happen enough times before.

Meanwhile the indie gamer small fry (I live on food stamps) doesn't have the luxury of working on lots of arbitrary stuff.  The important thing is to get a game done, that the indie wants done, and then try to sell it.  I try to "see the game possible with what I've got."  If I don't have something, and I think I want it, I try to estimate how much work it's going to take to get it.  Integrating GPUOpen?  No way man!  And if I wouldn't do it, I sure as heck wouldn't ask anyone else to.

-------------------------

rogerdv | 2017-01-02 01:08:53 UTC | #7

No, not asking for somebody to develop AI for you, simply providing some easy way to do it (one of my problems with Urho was that, didnt knew how to attach an script to an entity to execute AI). My opinion is: you (engine developer) build a hammer. I just ask, can you build a better hammer by adding X feature? And, if it is feasible, possible and fits into the master plan, you add X feature. 
About graphics, I always say that good gameplay and plot are better than graphics (thats my writer side talking). But if I can choose to have all of them, why not?

-------------------------

bvanevery | 2017-01-02 01:08:53 UTC | #8

Well, we haven't actually talked about the practicalities about integrating GPUOpen, so probably why I'm not having an easy time communicating why it's a "large" request.  Maybe you could look into it, even if you don't intend to do it, so you can get an idea.  At any rate I suppose this thread stands as a marker for anyone else coming along interested in GPUOpen.  If someone offers the practical idea of how to do it, then there it will be.

I don't have anything to say about AI hooks because I'm still back on making shaders work on bad HW.  Yes I could replace my bad HW, but with my limited means, I don't intend to do that until April.  Plan to get as much as I can out of my crap laptops before then.  Parts of language wouldn't depend on bad 3d HW anyways.  The irony is once I have the good HW I'll probably start caring about DX12.   :smiley:

-------------------------

rogerdv | 2017-01-02 01:08:53 UTC | #9

[quote="bvanevery"]
I don't have anything to say about AI hooks because I'm still back on making shaders work on bad HW.  Yes I could replace my bad HW, but with my limited means, I don't intend to do that until April. [/quote]
Yep, i know that feeling. MyPC is built with a case recovered from trash.

[quote]
 Plan to get as much as I can out of my crap laptops before then.  Parts of language wouldn't depend on bad 3d HW anyways.  The irony is once I have the good HW I'll probably start caring about DX12.   :smiley:[/quote]

One of the statements of marxist philosophy says: the man thinks according to his life (not lives according to his thoughts). Which means that if you have good HW, you stop worrying about bad HW.

-------------------------

bvanevery | 2017-01-02 01:08:53 UTC | #10

[quote="rogerdv"] Which means that if you have good HW, you stop worrying about bad HW.[/quote]

Unless you have a serious intent to ship to customers on low end machines.  I don't know that I do.  It depends on what is possible on such machines, as well as what is scaleable.  I have a large erstwhile 3d optimization jock side to me.  Once upon a time I wrote OpenGL driver code for money.  Beating other vendors on Viewperf and GLPerf and all that.  A slower machine, is a good indicator for whether you're making progress with optimization.  With anything meaningful, you should see results.  And if not then of course you're wasting your time.  Anything less than 20% benchmarked improvement is a waste of time in my experience, just noise.  You can run all sorts of tests for a few days, it can take a lot of time.  Got nice spreadsheet, better see some results for all that testing.  It's generally faster to understand how your HW works and just wing it with your best guess how to improve things.  Unfortunately in the shader compilation era I don't know how the HW works anymore under the hood, and I'm not even sure I can know.

When I get the new HW I'll still have to decide what the "minimum HW spec" is for an expected customer.  It is definitely way too early to expect DX12 to have any deployment.

-------------------------

cadaver | 2017-01-02 01:08:55 UTC | #11

[quote="bvanevery"]I haven't asked about Uhro3D's financials, how anything is sustained.  But I seriously doubt there's any equation that says, "worrying about lots of people's problems, makes us money, and sustains our efforts." [/quote]
Urho3D uses free services for hosting and is developed on free time, so there are no finances involved in the project itself.

Last year, and now again I'm working on an open source project at work that uses Urho3D, which means that engine issues specifically linked to development of that particular project can be worked on "company time" but that shouldn't be taken to mean that the engine itself is backed by my employer, or by any of the other corporate entities involved.

-------------------------

bvanevery | 2017-01-02 01:08:55 UTC | #12

Ok thanks for clarifying.  I was afraid to ask.  Kudos to you guys for accomplishing what you have.

-------------------------

