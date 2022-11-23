bvanevery | 2020-02-17 04:18:06 UTC | #1

Lua 5.4 is ["almost ready"](https://www.lua.org/).  Does anyone desire this?

Urho3D's Lua is 5.1 and it has LuaJIT available.

I'm actually a Lua noob, and have been learning about the Lua world's *fragmentation*.  This guy Mike Pall made this amazing LuaJIT which greatly increased Lua 5.1's performance.  Then Lua 5.2 came out, and he refused to go forwards with it.  Minor version numbers in Lua are released many years apart, do make some substantial changes, and they can break stuff.  That's their numbering culture.  So he probably had his reasons.  Then [in mid-2015 he stepped down](https://www.freelists.org/post/luajit/Looking-for-new-LuaJIT-maintainers) from running his LuaJIT project anymore.  He does contribute maintenance and bugfixes, and so do various other people, but nobody with his level of design talent stepped up to take his place.  LuaJIT is stagnant somewhere between 5.1 and 5.2 and will never go to 5.3.  Let alone 5.4.

Lots of people value the performance of LuaJIT so it has caused a significant fracturing of the Lua community.  For all intents and purposes, the language got forked, and the name of that fork is LuaJIT.  The consequences "as years go by" are problematic.  Lua library authors have 5.1/LuaJIT, 5.2, and 5.3 targets to consider, and now soon 5.4.  A lot of authors don't do the work of keeping up with this.  Things just rot and die.

This is considered somewhat ok in Lua culture, as the language was designed to be embedded in apps, not to be some big developer ecology like Python has turned into.  An app living by a specific version of Lua, and never "upgrading" it, is considered ok.

The problem I see is, *Urho3D* needs a stable and growable ecology, something that users can build on.  If Lua is to be a strategy for such an ecology, well fragmentation and ongoing loss of support, is *problematic*.  Even if you don't care about Lua libraries in general, you have to care about Lua stuff written for Urho3D, or there simply isn't an ecology to speak of.

The problem isn't unique to Lua.  Python is in a 2.x vs. 3.x schism.

-------------------------

rku | 2020-02-17 13:16:22 UTC | #2

What does new Lua bring to the table? Do new features offset loss of JIT capability?

P.S. it is "ecosystem".

-------------------------

S.L.C | 2020-02-17 16:31:32 UTC | #3

JIT shines when used in conjunction with FFI. When you use it on native registered vm closures, their benefit stop looking so promising.

And considering all of urho API is registered that way, and that the purpose of a script is to invoke that API for the majority of time. You'll see that the JIT stops being helpful.

You don't and shouldn't do heavy processing on the scripting side of the engine. The whole purpose of a scripting language is to improve fast prototyping. Anything beyond that is a step backwards.

I've said this and I'll keep saying it. You should keep heavy computational code away from a scripting language. That isn't it's purpose.

If Lua 5.4 makes programming easier, then you should take that instead. If it reduces boilerplate, then you should take it.

-------------------------

bvanevery | 2020-02-17 18:23:02 UTC | #4

This is long but I will get to your question, in a "let's start from the very beginning" kind of way.

I am still learning about various pros and cons of the different Lua versions.  As I said before, a big problem is library support.  5.1 might have the best supported libraries for all I know, in the sense that code still basically works.  But I'm doubting that stuff back on that version, is getting "fresh ongoing effort".  Might all just be in maintenance mode with no major improvements to anything.

LuaJIT is reputed to be difficult to debug.  Seems to be a combo of the "tracing compiler" not being easy to walk through, and the codebase not being all that straightforward.  People argue about whether LuaJIT internals are easy or difficult to fathom, but it doesn't sound like a job for amateurs.  LuaJIT has a rather different design center from Lua, as the developers of the latter are determined to have it be straightforward C code that will run on everything.  LuaJIT in contrast, is willing to add complication for the sake of performance, and will only run on platforms where the native assembly code work has been done for them.

LuaJIT's FFI is reputed to be better than what Lua offers, and is a feature that will drag developers into LuaJIT specific code, not just stuff that works for Lua 5.1.  It really is a language fork in that way.  There are also forks of the fork, such as LuaVela (Unix only) and moonjit (multi platform).

Now finally I get to what you asked.  :-)  Summaries from [Lua.org](https://www.lua.org/versions.html):

> Lua 5.2 was released on 16 Dec 2011. Its [main new features](https://www.lua.org/manual/5.2/readme.html#changes) are yieldable pcall and metamethods, new lexical scheme for globals, ephemeron tables, new library for bitwise operations, light C functions, emergency garbage collector, goto statement, and finalizers for tables.

LuaJIT may have also provided a number of those features, but I'm not sure which.  LuaJIT did not go completely forwards to 5.2 compliance, because of changes in how ["environments"](https://www.lua.org/manual/5.2/manual.html#8) worked.

> Lua 5.3 was released on 12 Jan 2015. Its [main new features](https://www.lua.org/manual/5.3/readme.html#changes) are integers, bitwise operators, a basic utf-8 library, and support for both 64-bit and 32-bit platforms.

64-bit platform support is what got my attention.  LuaJIT had a 2 GB memory limit for awhile, although someone claimed they overcame that.  That said, there's the official LuaJIT 2.0.5 release, and the 2.1.0-beta3 release, both from 2017.  2.1 seems to be in permanent beta and it wouldn't surprise me if that's what gives you higher than 2 GB.

Library authors who are working on 5.3 stuff now, are "current".  One might hope that would give their work more shelf life for the future.  I haven't gauged their opinion of [upcoming changes for 5.4](https://www.lua.org/work/doc/):
*     new generational mode for garbage collection
*     to-be-closed variables
*     const variables
*     userdata can have multiple user values
*     new implementation for math.random
*     warning system
*     debug information about function arguments and returns
*     new semantics for the integer 'for' loop
*     optional 'init' argument to 'string.gmatch'
*     new functions 'lua_resetthread' and 'coroutine.close'
*     string-to-number coercions moved to the string library
*     allocation function allowed to fail when shrinking a memory block
*     new format '%p' in 'string.format'
*     utf8 library accepts codepoints up to 2^31 

5.4 offers various [incompatibilities](https://www.lua.org/work/doc/manual.html#8), as minor numbers in Lua releases are allowed to break stuff.  One that strikes me as offering a lot of debugging to authors of previous code bases:

* The coercion of strings to numbers in arithmetic and bitwise operations has been removed from the core language. The string library does a similar job for arithmetic (but not for bitwise) operations using the string metamethods. However, unlike in previous versions, the new implementation preserves the implicit type of the numeral in the string. For instance, the result of `"1" + "2"` now is an integer, not a float.

The Incompatibilities section also talks about *binary* incompatibility between different versions of Lua.  Supporting multiple versions of Lua in Urho3D, would add implementation burdens.  I can't tell how much at this point.

-------------------------

bvanevery | 2020-02-17 17:56:12 UTC | #5

[quote="S.L.C, post:3, topic:5931"]
If Lua 5.4 makes programming easier, then you should take that instead. If it reduces boilerplate, then you should take it.
[/quote]

Binding to C++, does not appear to be a "which version of Lua?" problem.  Rather, it's a "which binding project has the most active development and is doing the best job?" problem.  A notable candidate is [Sol2 3.0](https://github.com/ThePhD/sol2).  The dev is active on the Lua mailing list, has strong performance claims for his call overhead, and he supports all the various Luas and LuaJITs.  Not quite sure about 5.4, but he seems like the kind of guy who's probably already on it.

I have not determined whether Sol2 3.0 produces its bindings automatically.  That's important to Urho3D, because the manual labor requirements of Lua and AngelScript bindings are blocking pull requests from being accepted.  There's really no reason a C++ contributor should have to worry about that sort of thing.  I get the distinct impression, that Urho3D is hemorrhaging contributors in a completely unsustainable way, and that this problem *must* be solved.

I also suspect that every C++ Lua binding regime, does their thing a little differently, so won't be pin-for-pin compatible one for the other.  One will have to make a choice about which horse to run the race with.

The tolua++ that Urho3D currently uses, is ancient and not under any kind of development.  Looking into that, is actually what got me started on this whole Lua ecosystem evaluation.  It's all a lot hairier than I expected.

-------------------------

Eugene | 2020-02-17 18:53:57 UTC | #6

[quote="bvanevery, post:5, topic:5931"]
I have not determined whether Sol2 3.0 produces its bindings automatically. That’s important to Urho3D, because the manual labor requirements of Lua and AngelScript bindings are blocking pull requests from being accepted
[/quote]
I had an impression that only SWIG has truly automatic bindings with C++ header scan.
Or are you talking about semi-automatic bindings where you have to manually list functions without signatures?

-------------------------

bvanevery | 2020-02-17 19:37:58 UTC | #7

Lua has *many* extant C++ binding projects and at this time, I can't tell what their various capabilities are.  Lots more "weeds" to figure out.  What each project can do, is not the only dimension.  Which projects are getting "the love" ?  Who's gonna get hit by a bus?  LuaJIT got hit by a bus, Urho3D got hit by a bus, it's a real problem when the 1 core developer moves on.

In this basic reality, I figured out pretty quickly, that there's no point worrying about Lua 5.3 at all.  Either find out if Urho3D users are deeply vested in LuaJIT, or they are interested in "modernization" ala 5.4.

Lua-centric approaches to the C++ binding problem, have the unusual possibility of using Parsing Expression Grammar (PEG) to do the job.  One of the main authors of Lua, is noted for popularizing the use of PEG, via his [LPeg](http://www.inf.puc-rio.br/~roberto/lpeg/) library.  It is reasonable to expect some expertise in the use of PEG among hardcore Lua developers.  Relying on this aspect of the Lua ecosystem to tackle Urho3D's binding problems, is not unreasonable.

I'm insufficiently familiar with Urho3D's APIs to know how regular they are, but it wouldn't be a rocket science wild assed guess, to imagine writing up some PEG to handle various corner cases, and call it a day.  This would require people capable of understanding PEG to participate in Urho3D's ongoing maintenance, as occasionally something would come up that wasn't automatically handled.  But such a PEG person could then put the problem to bed, and everyone would get on with Life.  I expect the level of difficulty would be something like, people who understand CMake build systems, vs. those that don't.  CMake is *not* inherently hard to understand, it's just a lot of grunge.  Similarly a PEG pattern matching regime.

When I did that failed Mozilla Autoconf --> CMake conversion project in 2007, I did it with piles of Regular Expressions.  Super hairy!  It was working though.  I could have used some PEG.  I didn't know about it at the time, and didn't have time to learn it, in order to make money.  CMake had regexes in it already, so I abused the *hell* out of that, pushing their implementation in ways that were surely never intended for production use.

PEG is also worth considering for AngelScript binding problems.  I haven't looked into AS binding issues yet.

I'm thinking a corollary of attracting and retaining Lua developers who know a smattering of PEG, is that one must offer *the best* Lua (probably 5.4) and not simply *the fastest* Lua (LuaJIT).  Especially, the kinds of people who hang out on the Lua development mailing list.  Apparently game developers do *not* hang out on that list for the most part.  They got stuck back in LuaJIT land, the thinking goes.

-------------------------

rku | 2020-02-18 07:58:53 UTC | #8

Word of advice: do not write bindings generator unless such thing does not exist. Use existing software. Bindings are not trivial even if it may seem so. You will eventually start reimplementing something like SWIG. World would appreciate a better-written SWIG alternative, but we want results now instead of in 5 years.

Check this out https://github.com/SteveKChiu/lua-intf

-------------------------

bvanevery | 2020-02-20 19:40:11 UTC | #9

Thanks for what I assume is an endorsement.  http://lua-users.org/wiki/BindingCodeToLua lists *numerous* C++ binders.  The problem is not whether such a thing exists.  The problem is which one is actually good, gets current development love, would be ready for Lua 5.4, and solves problems that have been noted in the Urho3D archives.  [Sol3 has a feature matrix](https://sol2.readthedocs.io/en/latest/features.html#the-feature-matrix) comparing the options available.  Whatever the author's bias, to even bother to do a big comparison like that, is a pretty strong endorsement for the seriousness of Sol3.  And you're right, there's definitely more to this binding problem than the "call it a day" off-the-shelf stuff I was hoping for.

My thought as of this morning, is that Urho3D *must have* an ecosystem of stuff written on top of a stable scripting language with a future.  An example of the kind of ecosystem feature I need, is an in-game UI that actually works and is production quality in aesthetic possibility.  i.e. that absorbs art assets or otherwise can yield game specific pleasing results.

It could be an AngelScript ecosystem *if* I had confidence that the AS community was capable of recruiting enough people and building such things.  But I don't have confidence that AS has the critical mass needed to sustain such efforts.  It doesn't even have a Reddit sub.  It has [its official forum on Gamedev.net](https://www.gamedev.net/forums/forum/34-angelcode/), that's it.  I even find that 1 forum hard to read and search through.  AS has made its mark *in a number of games*, but as far as building an ecosystem around it, I don't see *any* evidence of success.  The number of AS projects on GitHub are trivial to count up.  Checked SourceForge too.  Looks like sustaining an ecosystem hasn't even been basically a goal or on the radar of the AS community.  AS may have accomplished a great purpose once upon a time, "make it easier to talk to C++", but it's not the only scripting language out there with that claim to fame.

Lua, despite being fractured and having serious ecosystem problems, *dwarfs* AS.  A reasonable number of game developers know what it is, and that it's gotten used successfully in the game industry by some big AAA players.  The people who hang out on [Lua-l](https://www.lua.org/lua-l.html) know that ecosystem is a concern, and that luarocks *kinda sucks* as a package repository.  People wring hands, remains to be seen what anyone does about its future, but at least a critical mass of people know that *it needs to have* a future.

Python dwarfs Lua.  *Lots* of people know it exists as a language, something that Lua can't really say.  Nobody's giving Python the time of day for game engines, due to it being slow and the serious structural limitation of the [Global Interpreter Lock](https://realpython.com/python-gil/).  But it absolutely dominates the Visual Effects industry.  Blender and Autodesk both do it, and Python 3.7 is going to be the [VFX Reference Platform](https://vfxplatform.com/#footnote-python3) this year.  Python 2.7 was end-of-lifed at the beginning of this year.  The 12 year battle is all but over: Python will go kicking and screaming into a unified 3.x era now.

Here's a Reddit sampling of what it means for one community to *dwarf* another.  Number of Members in subs:
* r/programming - 2.5m
* r/Python - 504k
* r/gamedev - 403k
* r/learnpython - 305k
* r/blender - 196k
* r/Unity3D - 169k
* r/csharp - 133k
* r/cpp - 121k
* r/3Dmodeling - 53.3k
* r/vfx - 39.8k
* r/godot - 33.6k
* r/Maya - 26.1k
* r/3dsmax - 16.2k
* r/lua - 8.9k
* an AngelScript sub does not exist

I will never work on a C# ecology.  Unity owns that space.  Competing against them in open source is *insane*.  For those that actually are insane, there are a number of C# based engines already, such as [NeoAxis](https://www.neoaxis.com/) from the Ogre3D pedigree.  Whereas, Python 3.x is a legit basis for competition against Unity, because *nobody* is doing it successfully (Panda3D is the only one trying and their rendering technology still sucks), and Python in game *production* does matter.

If you *wanted new blood* in Urho3D, you'd build stuff in Python and make it work.

If for some reason you were tepid and unwilling to do that, you'd have to tackle the ecosystem problem in Lua.  And the only way that could possibly go into the future with a real ecosystem, is with the backing of the core Lua developers and Lua 5.4.  LuaJIT can't handle this problem.  Performance is great but it's a development dead end.

It's perfectly reasonable to ask if Lua is a good horse to bet on.  If not Lua, AngelScript, Python, or C#, then it would have to be some language not previously discussed.

Today I learned that someone is working on [Lua 5.4 support for Godot](https://github.com/perbone/luascript).  Also claims LuaJIT support, which baffles me.  Maybe it's all just WIP.  "Currently I'm experimenting with ways to generate the Lua bindings for the Godot API."  They are using something called [Parsing Expression Grammar Template Library](https://github.com/taocpp/PEGTL) (PEGTL).  No mention of this in the Sol3 feature matrix or the list of various known C++ binding tools.  Looks like the work of a "Lua jock" just rolling their own and NIH.

-------------------------

rku | 2020-02-19 07:26:51 UTC | #10

[quote="bvanevery, post:9, topic:5931"]
Unity owns that space. Competing against them in open source is *insane* .
[/quote]

They do not own shit. It is like saying unreal owns C++... And there is an unique spot where people want unity, but opensource. And with developer being in control. And with easy mixing of C++/C# code. So that effort is not futile at least. Not trying to downtalk python idea though, i am a huge python fan. If Urho3D had python instead of lua/AS then there would be no rbfx and no C#, that is for sure. I hope someone eventually makes automatic python bindings happen.

-------------------------

Eugene | 2020-02-19 08:03:52 UTC | #11

I don't believe python can really be "instead" of core scripting like Lua/AS.
Python is more like C# in this sense.
You don't embed Python/C# scripts into C++ engine (Python is really not embedding-friendly).
You embed C++ into Python/C# project.
That's different use case for me.

-------------------------

rku | 2020-02-19 08:51:35 UTC | #12

[quote="Eugene, post:11, topic:5931"]
Python is really not embedding-friendly
[/quote]

I would say that is not true. All you need is python3.x.dll + zip with stdlib in order to embed it. Python is easier to embed than C# in a sense that we can make bindings using pybind11, without having extra step of .py glue code generation.

-------------------------

1vanK | 2020-02-19 09:45:01 UTC | #13

[quote="Eugene, post:11, topic:5931, full:true"]
I don’t believe python can really be “instead” of core scripting like Lua/AS.
Python is more like C# in this sense.
You don’t embed Python/C# scripts into C++ engine (Python is really not embedding-friendly).
You embed C++ into Python/C# project.
That’s different use case for me.
[/quote]

Blender - example of embedding Python

-------------------------

Eugene | 2020-02-19 10:37:10 UTC | #14

[quote="1vanK, post:13, topic:5931"]
Blender - example of embedding Python
[/quote]
Well, I never said it's impossible... The effort and complexity is huge, especially if we want to maintain "all from source" Urho paradigm.
It would be overkill to pay such price just for scriptable console

-------------------------

rku | 2020-02-19 13:07:34 UTC | #15

When it comes to python common practice is to treat runtime as an external dependency. In case of games it gets more complicated because game should ship everything needed. Engine should use system python installation during development and bundle it with final product. So yeah, it stops being everything-in-tree.

-------------------------

bvanevery | 2020-02-19 16:29:47 UTC | #16

I just don't see any reasonable reality, where Unity and Unreal aren't acknowledged as the 900 lb. gorillas of the game industry.  There's been an almost shocking amount of consolidation and standardization on these platforms.  Most game devs *really aren't* into open source, they want to get on with making games and making money.  The business propositions are pretty simple for them.  They *don't want* to be the under-the-hood expert, it's not profitable for them.

[quote="rku, post:10, topic:5931"]
And there is an unique spot where people want unity, but opensource. And with developer being in control. And with easy mixing of C++/C# code.
[/quote]

And there are projects a lot farther down that road, much more mature, than Urho3D is.  I actually have no idea what your rbfx work is like by comparison.  I saw what happened in the Ogre3D ecosystem with NeoAxis splitting off.  The latter is clearly the one that exhibited long term project professionalism, that had a core developer behind it, who wanted to make sure his effort was sustainable and could make him some money.  When I came to Ogre3D maybe 4 or 5 years ago, it had become the amateur hour.  BTW their dev lead, "Sinbad", had stepped down.  It's a pattern.

I *do not* think there is room in the marketplace, for a large number of open source C# 3D engines.  Unreal is sucking all the air out of the room, and there are only so many volunteers to go around.  What happens when some "young buck" starts seriously worrying about paying their own bills, keeping a roof over their head, advancing a demanding career, getting married, and starting a family?  All their time as a single person starts to disappear.  They realize their C# 3D skill is valuable to the Unity ecosystem and *zip*, gone.  Another one bites the dust.

Why am *I* still at this?  Because I'm *old*, and *single*.  I come from an era when people rolled their own 3d engines and thought assembly code was a good idea.  I've acquired so much knowledge about stuff, that I just can't stand the idea of using Unity.

[quote="rku, post:10, topic:5931"]
If Urho3D had python instead of lua/AS then there would be no rbfx and no C#, that is for sure. I hope someone eventually makes automatic python bindings happen.
[/quote]

I'm surprised to hear you're that positive about it.  The GIL is a serious risk.  It will impose all kinds of application structural burdens on an Urho3D game.  If you want to think hard about what can be done to get around that, I'll listen.  The preponderance of the evidence is, the "performance" areas of the Python ecosystem haven't been dealing with real time user interaction.  Something like NumPy is *not* relevant to the concerns of a game developer.  They're doing batch processing.  Ditto the VFX rendering farms.

Python could certainly work for *non-performant* games, like for instance a modern adventure game, but I wouldn't want that to be the advertizing campaign for Urho3D.  I'd want to solve the performance problem somehow.  "You'd have to have part of your game off in a separate Python process" seems to be the textbook answer.  That kind of boundary, does sound like it would carry significant burdens for the application model.

[quote="Eugene, post:11, topic:5931"]
I don’t believe python can really be “instead” of core scripting like Lua/AS.
[/quote]

I agree.  A 3d engine needs at least the *perception* of scripting performance, for marketing purposes.  I don't believe you can really win an ease-of-use argument if you don't also have something that's "fast".  Doesn't have to be LuaJIT fast, but it does have to be faster than CPython.  And you're probably going to have to prove it, not just claim it.  Like have samples that have benchmarks and show how Python, Lua 5.1, LuaJIT, and Lua 5.4 are doing on them.

Also, Lua has no GIL issue.  That's structurally significant.

[quote="1vanK, post:13, topic:5931"]
Blender - example of embedding Python
[/quote]

Blender probably doesn't have performance characteristics appropriate for a real time 3d game.  The GIL, and the "embed Python" or "embed Urho3D" issue, is highly relevant here.  Remember that historically, Python came to be important in the VFX industry because of *running rendering farms*.  Not applications development.

[quote="rku, post:15, topic:5931"]
Engine should use system python installation during development
[/quote]

No, as that puts the burden on Urho3D to support *all* Pythons 3.x, in *all* hairy system configurations.  It's not how I've seen any application do their Python support.  They pick the Python they're using, and they stick with it.  Maya, 3DSMAX, Blender, Panda3D, this is the drill.  At some point they may bump their Python to something higher, but they control the configuration, not you the user.

Ok technically I have not drilled down to the installation procedures for all of these packages, on say Linux, to know what they do for sure.  I *suspect* this.  On Windows, most certainly they control the full installation and version of Python.  Linux has the [VFX Reference Platform](https://vfxplatform.com/), which matters to the VFX industry.  Note that is *not* consumer software, you can't presume any equivalent "regime of sanity".  If Autodesk gets customer support call, and customer doesn't have VFX Reference, Autodesk says !#$! you.  If game consumer whines and complains that something doesn't work, game developer *looks bad*.

-------------------------

SirNate0 | 2020-02-19 16:20:57 UTC | #17

I don't really see why the GIL is much of a concern in comparing to Lua/AngelScript - to the best of my knowledge ([https://urho3d.github.io/documentation/HEAD/_multithreading.html](https://urho3d.github.io/documentation/HEAD/_multithreading.html)) Urho does not currently support multithreaded scripts, which I understand to be the main (only?) issue caused by the GIL.

-------------------------

rku | 2020-02-19 16:32:58 UTC | #18

[quote="bvanevery, post:16, topic:5931"]
I’m surprised to hear you’re that positive about it. The GIL is a serious risk. It will impose all kinds of application structural burdens on an Urho3D game.
[/quote]

Not really. GIL is only a problem in multithreaded code. It is irrelevant in case of scripting game logic in Urho3D because scene updates must always be done on the main thread.

[quote="bvanevery, post:16, topic:5931"]
No, as that puts the burden on Urho3D to support *all* Pythons 3.x, in *all* hairy system configurations.
[/quote]
Python has a stable ABI so in case of bindings you can even build a binary that will be compatible with multiple versions. And you as a developer pick one version and stick to it, sure, but it would still be a system installation. I said that runtime has to be shipped with game as opposed to using system installation on user's machine (that would be crazeeee)

-------------------------

bvanevery | 2020-02-19 16:51:53 UTC | #19

[quote="SirNate0, post:17, topic:5931"]
Urho does not currently support multithreaded scripts, which I understand to be the main (only?) issue caused by the GIL.
[/quote]

Painting oneself into a corner with Pythonisms, however, is not a good idea.  What if at some point, someone figures out that multithreading a Lua script yields a measurable performance gain for something?  Like when the Lua ecosystem gets bigger and is put under more CPU pressure.  I certainly would keep trying to throw more and more things into Lua, that's pretty much the point of having a game scripting capability.  At some point it's going to teeter and totter over somehow.

[quote="rku, post:18, topic:5931"]
It is irrelevant in case of scripting game logic in Urho3D because scene updates must always be done on the main thread.
[/quote]

Who says that will be true forever?  Open source engines have to seek demonstrable bases of competition.

Especially, how do you finally put LuaJIT to bed, once and for all?  By *optimizing* how Lua 5.4 is used.  Gotta optimize something somewhere sometime, in a real application.  Any opportunity is needed.  Whether someone will finally do the work someday or not.

-------------------------

SirNate0 | 2020-02-19 23:25:08 UTC | #20

[quote="bvanevery, post:19, topic:5931"]
Painting oneself into a corner with Pythonisms, however, is not a good idea. What if at some point, someone figures out that multithreading a Lua script yields a measurable performance gain for something?
[/quote]
What about it? Then Lua will be the better choice over Python, in this hypothetical scenario. Python will still be easier/more enjoyable to write code in (which is subjective, of course). But to even get there, someone will have to enable multithreading support for Lua (and probably add much better threading support to Urho). If you want to do this work, by all means proceed, I'm certain it would greatly benefit Urho.

-------------------------

bvanevery | 2020-02-20 00:03:20 UTC | #21

I have to decide to ride either the Lua horse or the Python horse.  Even if I wanted both, it is only sane to implement one before the other.  I don't start things unless I can finish them.  Finishing one, the question is, what's the payoff?  If that starts yielding dividends, what is the need and impact upon the other?  They're not orthogonal.  Do I try to infect Urho3D with Lua 5.4 culture, or with Python 3.x culture?  Leading with one, affects the level of effort that will be put towards the other.

What I *wanted*, was to do [Jai](https://en.wikipedia.org/wiki/Jonathan_Blow#JAI_language) culture, or my own language culture.  But neither are shipped, and I must get on with real work now.

I do not currently understand all the implications of the GIL.  I do know that there's a serious issue to overcome, that the entire game industry has spoken about this.  I think I will look at some 2D Python 3.x stuff, and see if I can figure out where it "falls over".  See if Blender has benchmarks and profiling too.

-------------------------

rku | 2020-02-20 05:47:58 UTC | #22

Implications of GIL: only one thread can execute *python bytecode* at one time. This means that calls to a long-running native function can release GIL enabling other python code on another thread to run. I still do not see how we could do multithreaded scene updates from scripts.

-------------------------

bvanevery | 2020-02-20 05:55:23 UTC | #23

I was thinking more like 20 complex bots entirely scripted, in either Python or Lua.  Or user written AI analysis of a Civ-style map, entirely in Python or Lua.  Might be piggish, but easy for someone to write up, especially modders.  If you had the cores, why not do it?  "Interesting" if one language allows this and the other doesn't.

-------------------------

bvanevery | 2020-02-20 19:56:12 UTC | #24

There is something important in the VFX industry, called Katana, that is used for production pipelines somehow.  It does Python *and* Lua.  A user comments on [what he ends up doing](http://stefanmuller.com/my-katana-opscript-and-lua-journey/):
>After 3 years of Python scripting, I finally reached that point where I can confidently say that I roughly know, what I am doing. Then I fall in love with Katana and while interface and node graph stuff can be accessed/modified via Python, OpScripts are – for performance reasons – Lua based.
>
>Well, off to something new then. :p

Someone wrote a tech piece on why you choose Python, Lua, or C++ when working with Katana.  [Her findings](https://support.foundry.com/hc/en-us/articles/360001288699-Q100443-Scripting-and-Programming-in-Katana):
> **PYTHON - PERFORMANCE CONSIDERATIONS**
>
>Where faster performance is required, Python isn’t always an ideal choice (partly due to the dreaded [GIL](https://wiki.python.org/moin/GlobalInterpreterLock)).
>
>In the context of parameter expressions, a faster alternative to Python expressions is available for simple expressions that reference nodes or parameters. This is called [Reference Expressions](https://learn.foundry.com/katana/dev-guide/ParameterExpressions/ReferenceExpressions.html), please follow the link to the Katana Developer Guide for further information.
>
>Previous releases of Katana have suffered from stability issues when running Python-based AttributeScripts and asset plug-ins out-of-process through the so-called Katana ProcessManager.
>
>While the stability of ProcessManager was improved in the Katana 2.5 release (see TP 128448 in the [Katana 2.5v1 Release Notes](https://thefoundry.s3.amazonaws.com/products/katana/releases/2.5v1/Katana_2.5v1_ReleaseNotes/index.html)), the performance of Python especially in the context of scene evaluation is problematic.
>
>Lua offers better performance, making it a preferred scripting language for scene graph processing operations using [OpScript](https://learn.foundry.com/katana/Default.html#ug/working_with_attributes/opscript_nodes.html) nodes.
>
> **LUA**
>
>Lua is used within the OpScript node in Katana. Using OpScript/Lua it’s possible to access the Op API, which is both faster and more powerful than Python. In particular, the OpScript node allows you to modify the structure of the scene graph hierarchy, such as deleting locations, creating new child locations as well as setting and editing attributes.

Katana is [Lua 5.1 or LuaJIT 2.1](https://learn.foundry.com/katana/dev-guide/EnvironmentVariables.html#debugging) (presumed beta3).  LuaJIT is default:
>KATANA_OPSCRIPT_INTERPRETER
    Switches the Lua interpreter used by the OpScript node to either Lua 5.1 (if set to ‘Lua_5_1’) or LuaJIT 2.1 (if unset, or set to ‘LuaJIT_2_1’). LuaJIT provides better performance.

My takeaway from all of this, is you can do scene graph level magic with LuaJIT that you simply can't do with Python.  But whether you can pull it off in Lua 5.4, is unknown.  Lua is a simpler programming model than Python.  You don't worry about the GIL, you don't have to do any elaborate dance to structure your game around it.  You can make a highly threaded scripted game if you want to.  Katana would seem to be proof of concept of this, their sales literature is all about performance stuff.  But in choosing Lua, you *do* have to deal with Lua, which is "weird".  Not *bad*, but different.

Blender devs believe that "Python Modifiers / Compositing / Sequence Effects" are [AntiFeatures](https://wiki.blender.org/wiki/Reference/AntiFeatures) that should never be included in Blender:
>Python is not well suited for fast interactive operations on large data sets such as pixels or vertices.
>
>Even in cases where computation can be optimized, Python has a global interpreter lock (GIL), making any operations which use it single threaded.
>
>Using LLVM may be an option (as we already have for OSL), this would be long term project which needs to be carefully integrated into Blender's architecture.

So again, this is something that Lua can do, that Python cannot.

-------------------------

