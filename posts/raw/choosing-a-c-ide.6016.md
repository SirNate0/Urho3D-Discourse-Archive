Penny | 2020-03-26 09:20:36 UTC | #1

Looks very interesting. Do you have an idiots guide?

I am not a great fan of Visual Studio. It feels like it has too much of an overhead. I'm used to command line linkers etc, and writing code in say notepad. Is there an option for that with C++?

-------------------------

Dave82 | 2020-03-26 09:20:36 UTC | #2

[quote="Penny, post:1, topic:6016"]
and writing code in say notepad
[/quote]

Don't even try that... without tracking , debugging , compile , set , highlight , code management , IDE without intellisense support is impossible to write games in c++. You will need an editor to write your code except if you're a real masochist who enjoys remembering which file does what , and remember all your functions for all possible classes in the whole engine. Not to mention the possibilities of typos which are the absolutely impossible to track without an advanced IDE  Don't do that.

If you're on WIndows download a c++ IDE (Visual Studio , Code Blocks or whatever you like) .

For Visual studio i use these steps to create a new Urho3d project.
1. Create empty win32 project.
2. Include Urho3d.h and other files you want to use in you project. (Sound , DebugRenderer ,AnimatedModel etc)
3. Write code

-------------------------

SirNate0 | 2020-03-26 09:20:37 UTC | #3

Writing code in notepad is possible. I also would not recommend it, but if you wanted to go that route I would suggest mingw as your compiler and using the Makefile Target for CMake, then you just use make (mingw32-make or something like that possibly) to build it. Again, I don't recommend that, but using VSCode or Notepad++ as an editor together with that would be a more tolerable experience than just notepad. Auto complete (intellisense is Microsoft's branding for their auto complete features in VS) is very nice, but even simplistic implementations like in Notepad++ can be tolerable. Debugging without an IDE, however, is a much more painful experience, so I highly recommend you stick with a proper IDE for that purpose. 

If you think VS is too large, try CodeBlocks, it feels more minimal to me. Personally, I still recommend QT Creator over anything else, though I don't know if you can get it on Windows.

-------------------------

Modanung | 2020-03-26 09:21:20 UTC | #4

A post was merged into an existing topic: [Idiots guide to Hello World](/t/idiots-guide-to-hello-world/6000/53)

-------------------------

bvanevery | 2020-03-26 09:20:37 UTC | #5

I don't get the fascination with, or adulation of, Visual Studio.  My C++ skills may be rusty, but I used EMACS and Makefiles just fine 25 years ago.  Yes EMACS is a fair amount more than just a text editor, but 25 year old EMACS obviously doesn't have as many bells and whistles as VS today.

I don't think people should be "squirrelly and subjective" about their choice of editor or IDE either.  Use whatever works, until you have experience and have *well founded* reasons for why you say something *doesn't* work.  "Discomfort" isn't a valid excuse for avoiding something.  Everything in computer programming is discomfort at first.

-------------------------

Modanung | 2020-03-26 09:20:37 UTC | #6

I'm not a big fan of [Stasi](https://en.wikipedia.org/wiki/Stasi)ware<sup>[\[1\]](http://luckeyproductions.nl/images/PRISMslide.jpg)[\[2\]](https://web.archive.org/web/20180624044030/https://news.softpedia.com/news/visual-studio-2015-secretly-inserts-telemetry-code-into-c-plus-plus-binaries-505113.shtml)[\[3\]](https://web.archive.org/web/20180705230135/https://www.reddit.com/r/Windows10/comments/3f69pi/does_windows_10_really_allow_microsoft_to_access/)[\[4\]](https://web.archive.org/web/20200322185915/https://www.heise.de/tp/features/How-NSA-access-was-built-into-Windows-3444341.html)[\[5\]](https://en.wikipedia.org/wiki/EternalBlue)[\[6\]](https://en.wikipedia.org/wiki/SKYNET_(surveillance_program))etc</sup>, to put it lightly. Anyone promoting its use facilitates eroding the cornerstone of democracy and human rights in general (both his/her own and those of others), willingly or not. No amount of bells and whistles can compensate for this. Just because you're conforming to the herd does not make you any less complicit.

-------------------------

bvanevery | 2020-03-26 09:20:37 UTC | #7

Well, Surveillance Capitalism licensing is a somewhat orthogonal set of concerns, to the efficacy of a programming IDE.  I don't know how much hiding is worthwhile, because if you hide *too* hard, you actually stick out compared to your peers.  Sometimes it's better to hide in plain sight, rather than making yourself more noticeable about what you resist.  If I really really cared about this stuff, I'd ditch my GMail account.  Instead, I just don't basically trust it and don't send any emails that would really require security.  If I end up feeling a need for more security in my life at some point, like game development stuff I wanted to keep secret, then maybe I'd reconsider.  But as a lone wolf indie developer, I don't have to communicate about my game stuff to anyone through email anyways, so there's not much of a problem for me in the real world right now.

Anyways, yes, there can be other reasons to object to VS.  I don't know what kind of surveillance they're doing lately, but I've consistently found myself setting various things in various softwares to "opt out, no, no thanks, I don't want to participate" etc.

-------------------------

Modanung | 2020-03-26 09:57:46 UTC | #8

Surveillance capitalism is the lucrative slope that *ends* in irreversible Orwellian totalitarianism. Just as goosestepping is not the *problem* of fascism, but rather a part of the normalization process that leads to disaster. IDEs - and game engines like [Unity](https://spyware.neocities.org/articles/unity.html) - that output spyware by default belong in the trash bin, period. **Outputting spyware should be considered as *nullifying* an IDEs efficacy**. If dystopian actualities prevent you from making the right choice, you are giving in. It would be foolish to think our choice of software is irrelevant because it is "only virtual". Devices are in your house and on your body, screens are modernized paper. Boycott remains to be one of the more powerful forms of protest. It's easy until it's too late, a small effort before it becomes impossible.

And no I do not have a Google/Facebook account, there are [alternatives to](https://alternativeto.net) everything. Like Urho3D.

-------------------------

bvanevery | 2020-03-26 09:20:37 UTC | #9

I refuse Facebook, having recognized the way it undermines civil institutions, long before people were talking about surveillance capitalism.  But I have a GMail account.  I'm still broke, so paying for things like that still matters to me.  My compromise is to take precautions.  If they're data mining me to try to show me ads, I've gotta be like the *worst* target ever!  I'm pretty anti-consumerism, and I use ad blockers.

I do notice that YouTube has managed to successfully identify some genres of videos that I'm more likely to watch though.  I won't compulsively sit around watching videos though, and I'm hard to distract from the research tasks I've set for myself.

I think my use of GMail is far more problematic than my use of VS.  My GMail has much more to say about me as a person, than VS ever will.  I haven't even studied what VS might be collecting.  Ok, I'll crack a webpage on that, long as I'm typing this.  "Telemetry".  That's about as specific as I've been able to get.

-------------------------

weitjong | 2020-03-26 09:20:37 UTC | #10

Please keep on topic.

-------------------------

Modanung | 2020-03-26 11:56:18 UTC | #11

Good to see you @weitjong. Topic split.

@bvanevery It is _egocentric_ not to consider the effects your choices have on other people. It is *shortsighted* to think data collected by companies is not passed on. Part of the problem with IDEs that spit out spyware is that these programs are not marked as such, nor do developers carry badges that warn others about the fact they are distributing listening devices. Using VS is - at the very least - morally reprehensible and should be considered irresponsible behaviour by any informed software developer.

-------------------------

Eugene | 2020-03-26 13:14:17 UTC | #12

For serious/huge things, I prefer Visual Studio due to great toolbox of code refactoring and debugging tools. I really don't know any free IDE than have intellisense comparable to VS.
It's also nice to have DX11 Graphics Debugger and profiler integrated in IDE.
When I need these tools, I don't really have any option except VS.

When I don't need all these complicated things, I prefer VS Code.
It's open-source, fast (faster and more stable than VS) and I really like the interface.

-------------------------

Modanung | 2020-03-26 15:39:00 UTC | #13

@Eugene Could you describe the exact features QtCreator lacks in comparison to VS (Code)?
...apart from producing spyware.

-------------------------

Eugene | 2020-03-26 15:48:56 UTC | #14

I didn't use QtCreator for about 8 years, cannot exactly tell what's the difference.
It was lackluster back then. I can try it some day tho... I suppose it may have changed after these years.

> …apart from producing spyware.

Elaborate how text editor can produce spyware.

-------------------------

Modanung | 2020-03-26 15:53:08 UTC | #15

[quote="Eugene, post:14, topic:6016"]
Elaborate how text editor can produce spyware.
[/quote]
By being software and not pen and paper.

-------------------------

Eugene | 2020-03-26 15:56:05 UTC | #16

[quote="Modanung, post:15, topic:6016"]
By being software and not pen and paper.
[/quote]
So? The product of IDE is plain text (code).
Please point out spyware in the code that I write using VS.

-------------------------

Modanung | 2020-03-26 16:02:26 UTC | #17

It's called _code injection_ and does not modify source files. Do you not hit that convenient compile button?

-------------------------

Eugene | 2020-03-26 16:04:49 UTC | #18

I do. As long as compiled program stays on my machine (that already have shitload of unavoidable proprietary software), why should I care?

I don’t use IDE to release applications, I use it to develop.

I don’t even mention that it is compiler toolchain that injects code, not IDE. You don’t like one toolchain, you pick another.

-------------------------

Modanung | 2020-03-26 16:50:58 UTC | #19

[quote="Eugene, post:18, topic:6016"]
[...] why should I care?
[/quote]
Think about that. My earlier posts in this topic also contain multiple answers to this question.

Unavoidable proprietary software is an unknown concept to me. Instead I consider proprietary software to be *unacceptable*... like unlabeled foodstuffs.

-------------------------

bvanevery | 2020-03-26 18:25:18 UTC | #20

TL;DR: DirectX is critical and unavoidable to me.  This affects IDE choice.  **DirectX dominates the 3D gaming desktop.**

I want to make money selling 3D games in either the RPG or 4X TBS genres, possibly combining aspects of both.

Consoles are not a good fit to 4X, as the genre has tended to need a lot of keyboard shortcuts.  I suspect it is probably also much easier to play with a mouse or touchpad.  TBH I preferred using a full sized keyboard with a numeric keypad to move units around, but I've gotten used to doing without that.  Although modern consoles do actually support keyboards and mice, it's not culturally what most people do, and probably not most people's living room setup either.

Consoles are also not indie friendly.  There have been some attempts at indie consoles, say the Ouya or Steam Machines, but they have failed.

Although some people on mobile phones want 4X games, I find the idea of giving that to them, kind of a joke.  I only believe in gaming on reasonably sized screens.  A touch tablet, maybe, but definitely not a phone.

Mobile gamers also have limited attention spans.  4X games are long, and not suited to being broken up into the short attention span / multitasking / grab a few minutes here and there play attitudes of the mobile gaming demographic.  These don't look like desirable customers, at all.  There's a reason these platforms don't see much in the way of "deeply involved" games.  They don't have the UI to support it, nor the customer attitudes to desire it, in enough volume to matter to a developer.  If someone wants to prove me wrong on these pronouncements, they're welcome to try their hand in the free market, but I'm not going to.  Doesn't smell like any kind of money pot to me, it smells like fool's errand.

Linux isn't a viable consumer gaming platform.  I did Linux recently for 3 years, waiting for Steam Machines to come save us all.  They didn't, they failed.  I gave up.  Linux just has too many distro and graphics stack politics to deal with, and no companies actually trying to make money in the consumer software space.  From a consumer usability standpoint it's a joke.  People do buy some games on Linux, but from a make money numbers standpoint, the math simply isn't there.  From an engineering and cultural reality standpoint, it never will be.  You spend enough time in the trenches with enough open source projects, and you'll realize why.  These people simply can't ship consumer software, they're clueless.  There's all kinds of dull boring things that need to happen for feeble ordinary people to be able to use software, and most of the FLOSS crowd is hardcore expert tweak this tweak that write programs for other programmers.  Only money changes most people's discipline in that regard, and like I said, no big corp is pushing to make money with Linux in consumer software.

In the real world, 4X TBS is a desktop phenomenon.  That leaves Windows or MacOS as the candidates.  Windows is clearly the superior gaming platform to MacOS, in terms of customers.  I can't even remember if Apple has gotten in any way serious about game development.  For so many years, they didn't care about game developers at all.  Didn't fit with their "cool upscale lifestyle" music marketing or whatever.  Both platforms have proprietary 3D graphics APIs.

OpenGL is toast.  The device driver deployment on Windows has historically been bad.  When you're selling products for money, this matters.  You can't just tell customers to tweak and fiddle and hope for their best.  Their 3D drivers have to work, and in the real world on Windows, those have been DirectX drivers.  Apple used to do OpenGL, but in recent years they've been actively killing it in favor of Metal.

OpenGL is also technically inferior to DirectX.  It's a crappy API with all the "get a pointer" dancing around.  It didn't do multitasking, although I haven't kept up on whether that's changed in more recent releases.  DX11 had multitasking.  Nobody would care if OpenGL has finally caught up *now*, as OpenGL has no future in gaming.  That's the whole story of OpenGL, too many years of not improving in industry fast enough.

Vulkan isn't viable yet.  My recent research suggests that Microsoft has been more open source cooperative about Vulkan than I would have expected.  At least to the extent that their cooperation allows HLSL to become The One True Shading Language To Rule Them All.    Since my Commodity Graphics Group back at DEC was burned by Microsoft back in the day, my trust in them as a corporate entity is low.  The playbook of getting involved in some area, so that they can yank the rug out from under it later, is an old one.  I'll believe Vulkan is a viable commercial platform on Windows, when a lot of AAA game studios are shipping on Windows and it's clearly not a problem.

I haven't studied Apple's politics about Vulkan, but I expect them to do everything possible to thwart it, in favor of Metal.

In the real world, DirectX falls out of the bottom of my commercial gaming equation, as a necessary and unavoidable piece of the toolchain.  People have all kinds of options for writing *a* game.  But for what *I* want to do, it ends up being Windows and DirectX.

**Visual Studio has some bells and whistles for DirectX debugging**, that I'm not fully up on yet.  It remains to be seen what I'll need in this regard.  What the production realities are.

Me making money as an indie game developer, when I am currently *broke*, is far more crucial than any spyware code injection issues.  I don't have the luxury of avoiding the exit door to poverty, if I want to do it on my own terms as a game designer.  And no, I'm not going to go write some other kind of game, just because someone is worried about an IDE injecting spyware.

The issue of stopping code injections in a release build, is a problem I can take up, *when* I have a game that's near to shipping.  A lot could change before then.  [Jai](https://en.wikipedia.org/wiki/Jonathan_Blow#JAI_language) could finally come out.  I could invent my own language.  That's a more serious possibility now, as I find it very difficult to sign off on Lua 5.4 as a 3D graphics programming model.  And in any event I'm not afraid of builds and build systems, as that's the last thing I made money on.  I'm an old school ASM coder, I think I can handle some linkage issues if I *want* to handle them. I just know that "spyware issues" are *not* mission critical to me and will *not* help me with getting out of poverty.  I live out of a car.  I don't have time for such concerns.

I check my "opt out, no, no, no thank you, oh hell no" buttons early and often, when I install stuff.  That's what I'm willing to do for now, and it's something other people can do.  The biggest impact from me choosing this way, is tech companies aren't going to get telemetry about genuine bugs in their products.  I find that regrettable, but since public trust about this sort of thing is pretty much broken, I'm calling that collateral damage.  

I've never gone up a full security learning curve about Windows, ever.  I don't even install any kind of anti-virus software.  I let Windows Defender do stuff, and I've been doing that since Windows Vista.  No harm has come of it.  My level of sophistication, has been running Malwarebytes manually every once in awhile, when I get suspicious.

My philosophical attitude is that your security and privacy is to some extent an illusion.  Things are gonna snoop you, because even most techies don't have the time to whack all the security moles that are coming up all the time.  A person who wants to ruin computers, or infiltrate computers, can do so.  Nevermind a corporation or a government.  If you want to fight those battles against "big entities", you can try.  But you should consider whether this is *the battle of your life*, that really must be won.  I know that *my* battle is to produce Art, in the medium of computer games.  That battle is plenty hard enough, without adding extra ideological burdens on top of it.

There's also a question of, when you get to the point of being willing to take on *additional concerns* to make a better world, *which* concerns of the many possible Social Justice concerns, are you going to take on?  'Cuz a solo developer certainly doesn't have time for all of them.  How about minority and gender representation in games?  How about accessibility?  There's a blind guy who posts in r/4Xgaming lately.  I *could try* to solve his problems, at some considerable technical cost to me as a developer.  Maybe I think that's more important than jousting at spyware?  Might depend on which problem turns out to be technically easier or harder.  There's also the question of which one is more *interesting* to work on.  I have ideas about the blind stuff.

-------------------------

SirNate0 | 2020-03-26 20:41:33 UTC | #21

[quote="bvanevery, post:20, topic:6016"]
My philosophical attitude is that your security and privacy is to some extent an illusion. Things are gonna snoop you, because even most techies don’t have the time to whack all the security moles that are coming up all the time. A person who wants to ruin computers, or infiltrate computers, can do so. Nevermind a corporation or a government. If you want to fight those battles against “big entities”, you can try. But you should consider whether this is *the battle of your life* , that really must be won. I know that *my* battle is to produce Art, in the medium of computer games. That battle is plenty hard enough, without adding extra ideological burdens on top of it.
[/quote]

Well said! This pretty much describes my philosophy as well. That said, I'm still sticking with Linux, but that's because it's useful for other reasons. And with SPIRV-Cross and Angle, etc., hopefully the future is near when glsl and hlsl as a choice don't really matter, which is basically the only important distinction between using Urho's OpenGL and DirectX backends. (And yes, that's probably overly optimistic, but whatever).

-------------------------

bvanevery | 2020-03-26 22:27:17 UTC | #22

This may not be a concern for most people, but from an archival standpoint, of what APIs and languages will be preserved by future generations, I think Windows, DirectX, and HLSL are more likely to have emulators for them.  I don't particularly want to make ephemeral games that are gone in 2 decades.  Films have a many decades lifespan now, and I want games to have similar longevity.  That's not an easy proposition in the present.

I think OpenGL lost the commercial gaming wars, big time.  That's going to affect archiving in the future, I think.

There is unfortunately a lot of other stuff about games that is going to bitrot out.

-------------------------

SirNate0 | 2020-03-27 01:13:29 UTC | #23

In terms of emulating desktop games in the future you may be right, but given the prevalence of mobile games (as well as some consoles like the Nintendo Switch) that used OpenGL, I really don't expect OpenGL to have much of a lifespan issue (well, at least OpenGL ES. It's a bit less certain about desktop OpenGL).

That said, if I get back into writing shaders (or at least trying to; I mostly avoid it, as almost everything I want has already been written by others) I may give visual studio and Direct X a try. I seem to recall porting HLSL to GLSL was pretty straightforward for the most part (as I want to support more than just Windows). It would be nice to have a tool tell me where my sharer is broken rather than just having it render black :slight_smile:

-------------------------

bvanevery | 2020-03-27 02:28:12 UTC | #24

You may be right that OpenGL ES has the possibility of longevity.  Might be the only OpenGL that survives.  So the other issue, is whether any mobile games end up being important enough for people to archive / restore / emulate.  I think the "short attention span" nature of the platforms, doesn't bode well for that, but who knows.

It's too early to say how WebGL is going to do, or whether anything will be made with it, that is archivally important.

-------------------------

johnnycable | 2020-03-27 15:45:43 UTC | #25

[quote="bvanevery, post:20, topic:6016"]
Linux isn’t a viable consumer gaming platform. I did Linux recently for 3 years, waiting for Steam Machines to come save us all. They didn’t, they failed. I gave up. Linux just has too many distro and graphics stack politics to deal with, and no companies actually trying to make money in the consumer software space. From a consumer usability standpoint it’s a joke. People do buy some games on Linux, but from a make money numbers standpoint, the math simply isn’t there. From an engineering and cultural reality standpoint, it never will be. You spend enough time in the trenches with enough open source projects, and you’ll realize why. These people simply can’t ship consumer software, they’re clueless. There’s all kinds of dull boring things that need to happen for feeble ordinary people to be able to use software, and most of the FLOSS crowd is hardcore expert tweak this tweak that write programs for other programmers. Only money changes most people’s discipline in that regard, and like I said, no big corp is pushing to make money with Linux in consumer software.
[/quote]

A bit brunt but to the point, lol. Linux is not for gaming.

[quote="bvanevery, post:20, topic:6016"]
I haven’t studied Apple’s politics about Vulkan, but I expect them to do everything possible to thwart it, in favor of Metal.
[/quote]

Simply there's none. Apple is not interested. Only option is thru https://discourse.urho3d.io/t/metal-moltenvk-support-for-ios-an-mac-devices/4845. You're limited to opengl es something, but for TBS should do fine.


[quote="bvanevery, post:20, topic:6016"]
The issue of stopping code injections in a release build
[/quote]

The only successful code injection I know of is that of XCode couple years ago. Those chinese guys kept XCode on a server of their own, so they didn't had to wait hours for downloading. Someone discovered it and injected a malware into it. Lots of apps shipped with the trick and made a mess. Then Apple blocked everything and started the Holy Security Crusade against the Evils Hackers. Bow to my tie, everyone.

One last thing about TBS. Playing TBS is like playing chess, but on much longer time span possibly. Clearly unsuited for something fast like mobile, but possibly good for anything else. It's a genre that heavily relies on fan, so, in my head, I would concentrate on finding the community before the platform...

-------------------------

SirNate0 | 2020-03-27 16:20:37 UTC | #26

[quote="johnnycable, post:25, topic:6016"]
One last thing about TBS. Playing TBS is like playing chess, but on much longer time span possibly. Clearly unsuited for something fast like mobile, but possibly good for anything else.
[/quote]

I actually disagree with this, for single player games at least. Because of the turned-based nature, a turn-based strategy game should be fine on mobile, as long as the state can be saved every turn and a turn can generally be completed in around a minute. Then the player is free to stop and come back later every turn, which is very similar to a lot of the mobile games out there where a level takes a minute or two to finish. In terms of the audience, who knows, it may be a lucky success and become fairly popular, it may not. That said, desktop is probably a better TBS target, especially given the touch interface and small screens of most mobile devices. I just think it is unreasonable to call it unsuitable for mobile or to assume mobile games are fast paced - many are, but there are also plenty of turn based mobile games and untimed puzzle games.

-------------------------

bvanevery | 2020-03-27 16:32:13 UTC | #27

Getting off-topic, but briefly, r/4Xgaming is the identifiable audience.  I've already staked out a presence there the past 2 years with my modding work.  Meaningful turn advancement in 1 minute is wishful thinking in the genre.  It also typically takes multiple turns for anything of interest to happen in this genre.  It's a *lot* of unit pushing.  I wrack my brains about how to speed that up, as a matter of game design, but they are not easy theoretical problems.  If they were, I would have made my game and my money 20 years ago.  I'm brave to keep trying, as opposed to giving up on this niche genre entirely as a lost cause.

I doubt OpenGL ES is going to have a good driver deployment story on Windows.

-------------------------

johnnycable | 2020-03-28 16:23:39 UTC | #28

[quote="bvanevery, post:27, topic:6016"]
I wrack my brains about how to speed that up
[/quote]

why not RTS then? [20 character filler]

-------------------------

bvanevery | 2020-03-28 17:33:30 UTC | #29

*Too* fast and stressful.  No depth.

Similar problem with "why not simplify a game of Sid Meier's Alpha Centauri down to the level of a European style board game?"  Because such games don't have any complexity challenge to them.  I did a board game group for a year or two, got to try a lot of different modern ones that people kept on bringing to the group.  Figuring out their optimal production strategies was *very* easy and I would often beat people in that group, even never having played the game in question before.

-------------------------

johnnycable | 2020-03-29 16:02:28 UTC | #30

[quote="bvanevery, post:29, topic:6016"]
Sid Meier’s Alpha Centaur
[/quote]

Only played civilization by this guy. That is quite a good game. Didn't know about this expansion. Looks good. :laughing:

-------------------------

bvanevery | 2020-03-29 16:47:07 UTC | #31

Best bang for the buck in 4X TBS currently.  It's cheap on GOG and some people still develop major new capabilities for it.  Like me!  Here's my [mod](http://alphacentauri2.info/index.php?topic=20959.0).

-------------------------

johnnycable | 2020-03-30 14:56:36 UTC | #32

Ah, got you dirty little modder!
Alas, at a 9 m/p you could have really done a game of your own. A simple one, at least...
Anyway this SMAC thing looks really big. Could give it a try, but I'm a little afraid about times... until I'm quarantined, anyway, I need to spare some extra time... so...

-------------------------

bvanevery | 2020-03-30 15:09:30 UTC | #33

I don't believe in simple though.  Also, I believe in quality.  That was the cost of the quality.

-------------------------

