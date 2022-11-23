alexrass | 2017-01-02 01:07:43 UTC | #1

Found an interesting page on github:
[url]https://github.com/r-lyeh/scriptorium[/url]

lua is faster than angelscript in this tests... (Fibonacci tests for now)
It will be interesting to see the results of more tests. Although I still like Angelscript.

[u]Please no holywars))[/u]

UPD:
Forgot to say that it is in the repository a bunch of useful code.

-------------------------

Hevedy | 2017-01-02 01:07:43 UTC | #2

Thanks for that good to see things like this.

-------------------------

cadaver | 2017-01-02 01:07:44 UTC | #3

Something involving also calls to C / C++ side bound objects would be more realistic for a game scripting scenario.

-------------------------

Pyromancer | 2017-01-02 01:07:44 UTC | #4

I've always seen it this way. Lua is the champion of being easier to use by scripters (tables for days) and just really damn fast in execution and small in size, while Angelscript has always been the champion of being easy to bind to C++ code and in being more familiar to C++/C#/Java users at the cost of size. It's what made it my scripting language of choice in college since I was that crazy bitch who implemented a damn game engine as her senior project (admittedly it was pretty garbage, but it worked... sorta...  :unamused:) and trust me, I looked into pretty much every scripting language there is... even scheme... don't judge me. Each has their own merits and it's always going to be slower to execute than C++ (unless the code is JIT compiled, in which case Lua has them beat... unless Andreas merged an x32/x86_64 JIT compiler implementation into the mainline. Not sure. Haven't checked in on them in a while. I know there's an ARM JIT implementation floating around somewhere for Angelscript.)

-------------------------

Hevedy | 2017-01-02 01:07:45 UTC | #5

In the modern engines now they are using the script to C++ and compiled C++ for the packaged games, for example Unity is doing that and Unreal Engine 4 will be the next with that ready the Blueprints code convert to C++ and then is compiled and included in the game.

-------------------------

Enhex | 2017-01-02 01:07:45 UTC | #6

While Lua is faster and easier to learn, AngleScript offers safety and structure.
Considering that the purpose of scripting languages in games is rapid development and not performance, AS is the winner for me since it will be easier to avoid and deal with bugs.

-------------------------

boberfly | 2017-01-02 01:07:45 UTC | #7

My thoughts on scripting these days:

I might have mentioned this before, but something akin to the blueprints system in UE4 and runtime-compiled C++ sounds interesting. Especially if you make some kind of node network-to-C++ conversion tool, with the ability to just drop-in hand-crafted C++ where needed and just make some reflection info to integrate in said node network tool. Events can be registered and tapped into for node networks and such. Have a build button which just does RC++ hot-reload management of game components, stuff like that. The end result can all be just static linked so it just works in emscripten/IOS where shared libs or jits are prohibitive, or bytecode would be too slow.

I didn't know of micropython being used for an embeddable scripting engine but it makes sense. For me the python bind wouldn't be for the run-time but for pipeliney stuff to integrate into a DCC package or talk to PyQt/PySide, asset management packs, etc. So there would just be an import Urho3D module to an existing python runtime. I'm such a fanboy of python, coming from a vfx background... :stuck_out_tongue:

-------------------------

1vanK | 2017-07-29 05:50:37 UTC | #8

I compared lua and angelscript samples with "-nolimit" option. On average, the angelscript has x1.5 - x2 FPS than LUA (without LuaJIT and with LuaJIT, no big differrence because no heavy mathematics in script I think).

-------------------------

weitjong | 2017-07-29 07:25:44 UTC | #9

Our current implementation of LuaScript subsystem is not as optimal as AngelScript subsystem due to tolua++ binding. The binding produces tons of warnings/errors from the static analyzer, does not do reference counting, and has a few pitfalls when converting values between Lua/C++ languages, just to name a few. I also observe that in some cases, although renders just fine, produces different overall outcome than its Angelscript counterpart. Take the PhysicsStressTest, for example, near the end of the program run you can clearly see something is wrong with LuaScript subsystem when under stress. The LuaScript subystem is a contributed code. Aster has contributed the code and left us to maintain it :slight_smile:. There is a stale branch to change the Lua binding from tolua++ but it has not seen the light of day. If you are using Lua or plan to use Lua in your game, probably you want to evaluate that stale branch. A new maintainer for the LuaScript subystem is needed.

-------------------------

1vanK | 2017-07-29 06:23:35 UTC | #10

PhysicsStressTest just use differrent methods for drop objects (AS use offsets for pos, LUA - time delay)

-------------------------

JTippetts | 2017-07-29 06:57:54 UTC | #11

I've thought about taking up the job of redoing the Lua bindings. I've been evaluating some of the newer/more actively developed bindings libraries towards that end. The tolua++ based stuff has _problems_. Bad problems. Problems that have been around for years, and are only likely to get worse as the tolua++ code rots. I love Lua, and just can't seem to make myself like AngelScript at all, so maybe I'll try to make some time for this.

Many of the libraries I have been evaluating are C++11, or rely on boost for pre-C++11, which is part of what has held me back.

-------------------------

Eugene | 2017-07-29 08:13:10 UTC | #12

When we migrate to C++11, it will be possible to use nice Lua binding libraries..

-------------------------

slapin | 2017-07-29 09:27:55 UTC | #13

> C++11 Lua

*facepalm*

-------------------------

Eugene | 2017-07-29 10:24:47 UTC | #14

Huh? Most of nice Lua bindings use variadics and so on to do anything, am I wrong?

-------------------------

JTippetts | 2017-07-29 11:12:09 UTC | #15

Well, I mean... C++11 hasn't even been the most up to date standard for _years_. It's pretty irrational to expect other third-party developers of libraries we want to use to stick to older standards, when the new goodies make some things so much easier. Unless we want to re-write every third party library custom, eventually most of them are going to outpace Urho3D. I'd say going to C++11 is a _bare minimum_. If I were to rewrite the Lua bindings now, I'd just have the config option force the C++11 flag, rather than include boost or some other heavyweight monstrosity simply to keep from requiring C++11. I'm aware that boost is already a dependency, I just wouldn't like it to be because of _me_.

Edit: My personal choice, that I use for non-Urho projects, is sol2. But seeing as that's at the least C++14, and people already have their knickers in a bind over C++11, I'd have to pick something else.

-------------------------

slapin | 2017-07-29 11:12:22 UTC | #16

Well, there is no any C++ code needed to do good bindings for Lua.
If you do a lot of auto-bindings for classes you will end-up with ineffective code.
If you need effectiveness, you need to do some hard work. And C++11 things will not help you with that.

I do lua bindings for about 5 years now, can help if wished. But without manual labor there is no
much sense to do any changes.

-------------------------

JTippetts | 2017-07-29 11:18:11 UTC | #17

It's true. You don't need any C++ code to bind to Lua. You could just stick to C. Maybe even go with assembly. No need for that silly C++ at all. I think that if the requirement for the Lua binding were to be to use no C++ binding generators, and just write everything from scratch in the Lua API, I'd have to reevaluate my willingness to redo the Lua bindings. Even with a generator, finding the time to do it will be tough. If you wanted to take on such a beast, though, rather than just obstruct, I'd be inclined to cheer you on.

-------------------------

Eugene | 2017-07-29 11:55:24 UTC | #18

Do you suggest to either use C++ generators like tolua++ or write those insane stack ops manually?
I think that "one line - one entity" bindings like AS is much better than these two.

-------------------------

slapin | 2017-07-29 13:19:36 UTC | #19

AS bindings are really insane in size of code path/ I think you would not want to do that. Lua is fit for manual binding,
it works best. Generated bindings are often too verbose and ineffective. So if you don't want to go manual path,
you better leave things as is.

-------------------------

slapin | 2017-07-29 13:21:14 UTC | #20

Anyawy, I don't want toscare you - if you carefully prepare a set of macros and templates, this still be better than generated binding.

-------------------------

JTippetts | 2017-07-29 13:47:18 UTC | #21

Leave things as is? I ask you, have you attempted a large-scale project using the Lua bindings? A full game, start to finish, written in Lua? My game, Goblinson Crusoe, is just such a beast, though I am slowly but steadily reimplementing every script object as a C++ component due to the issues with the tolua++ bindings. These problems have been intermittently documented through issues raised by myself over the years, and outside of the ugly generated code (ironic that you argue for things to stay "as is" the later argue that generated bindings are verbose and ineffective; I wonder if you've even looked at the generated bindings now) there are issues with garbage collection that rear their ugly heads if you do things in certain ways. One such degenerate case crops up for me _all the time_ when doing procedural generation of a map.

When generating a map, it is common to iterate in X and Y across some range, say 0 to 128 in each dimension for a moderately sized map. In the current system, if you generate any kind of garbage bound through tolua (ie, any Urho3D object, even ones returned by value) inside the inner loop, then God help you. I believe it was established that tolua internally creates tables to hold these tolua-managed objects, and these tables can grow to unwieldy sizes when objects are generated in this inner loop. Even after the garbage is collected, these tables are never resized, causing huge performance issues during later garbage collection duties as these large tables are iterated.

 I may be misremembering  the exact nature of the issue, since it's been a long time since I tried to fight with it, but the effects are noticeable and unpleasant. In my game, they manifest as periodic intervals of extreme stuttering as LuaGarbageCollection spends an increasing amount of time churning its wheels for awhile. I can see frame drops from an average of 43 fps to an average of 8 fps while the profiler shows skyrocketing LuaGarbageCollection time for a period of five or six seconds, before returning to normal. While these massive allocations of garbage can be mitigated by moving any nested-loop generation structures into a C++ module of some sort, that's not really a fix for the problem.

The Lua bindings need to be redone. That's been known for quite awhile. There was some hope when aster started his branch, but that is long dead. I'd venture to say that as they stand, the Lua bindings are actually _detrimental_ to the health of Urho3D, possibly conveying an impression of poor performance on the engine as a whole.

"Anyawy, I don’t want toscare you - if you carefully prepare a set of macros and templates, this still be better than generated binding."

What do you think a third party binding generator is? It's usually a set of macros or templates. I've written bindings using the raw Lua API, I've written them using various third party generators, and I can say that you'd have to be insane to forgo the convenience of a binding library in favor of raw Lua API, especially in an engine as large and complex as this is becoming. And I'd rather leave the maintenance of that "set of macros and templates" in the hands of a third-party developer devoted to their project, than put maintenance of those onto the Urho3D team. Ideally, the binding generator should be stable, relatively bug-free right from the start, and usable in a manner similar to the AngelScript bindings.

There are a small handful of different libraries that fit this mold: sol2, Kaguya, lua-intf, etc... These are among the more elegant and easy to use; there are other, frequently uglier, usages. The thing that sets most of the more elegant solutions apart is a reliance upon features provided either by boost or by language features introduced by later C++ standards, C++11 and beyond. sol2 wants C++14 or better, so that's probably out. But trying to write our own set of templates and macros to match functionality with one of these libraries seems like a waste of effort to me.

-------------------------

weitjong | 2017-07-29 14:26:47 UTC | #22

I don't think sol2 requirement is that high according to this [section](https://github.com/ThePhD/sol2#supported-compilers) from their README. Even if it requires C++14, I also do not see it as a problem. Our CI server should be able to handle it. 

p.s. don't feed the troll.

-------------------------

slapin | 2017-07-29 20:13:38 UTC | #23

Well, this looks like misunderstamding. I'm also a victim of Urho scriptimg (uing AS) and I had to move everything to C++
because of incredible performance issues.
When using Lua in general it is much easier to use own bindings than auto-generated ones for classes. This is my opinion
established through the years. I used various binding generators for bindings too, but they provide lots of overhead. Some 
of them allow to write portions of specially-handled code manually, I'd look for that opportunity.
Myself I prefer manually writing whole binding, that gives best results with binding parameters and speed. But I agree
that for project like Urho this might take ages to implement, so I'd identify most problematic parts and reimplement these as manual bindding.

-------------------------

