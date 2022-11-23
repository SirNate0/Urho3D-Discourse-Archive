TheSHEEEP | 2017-01-02 01:13:21 UTC | #1

Hey there,

I've been looking into various engines for an idea of mine and do find Urho (I guess "hero" sounded too generic ? :wink: ) very interesting.
The feature set seems really impressive and it seems the engine has almost everything I would need.

However, one thing I find very troubling and that is that according to documentation and this thread ( urho3d.prophpbb.com/topic47.html ) it is not possible to make scripts run in sub-threads.

That one is a serious drawback, as threaded scripting (or at least separating gameplay logic from rendering/physics/etc.) is a necessity for any game that has larger demands on CPU than an average shooter.
Take any strategy game with thousands (okay, maybe hundreds) of units planning their moves, many AI players, large amounts of pathfinding, etc. (take maybe Europa Universalis as an example) - if all of that had to be done in order within one thread, it simply wouldn't be possible to have a proper AI going.

Is there any way around this restriction? 
I do not think much CPU demanding logic can be done if the gameplay has to run on the same thread as everything else.

-------------------------

Enhex | 2017-01-02 01:13:21 UTC | #2

1. You can do threaded game logic without scripts. You can read about threading restrictions here: [urho3d.github.io/documentation/H ... ading.html](http://urho3d.github.io/documentation/HEAD/_multithreading.html)
2. Premature optimization. You didn't make anything yet and you already decided it isn't performing well.
There are strategy games from 15-20 years ago running many units on a single weak CPU. I think you won't even need multithreading for optimization at all.

-------------------------

TheSHEEEP | 2017-01-02 01:13:21 UTC | #3

[quote="Enhex"]1. You can do threaded game logic without scripts. You can read about threading restrictions here: [urho3d.github.io/documentation/H ... ading.html](http://urho3d.github.io/documentation/HEAD/_multithreading.html)[/quote]
Yes, and according to the doc, this is unsafe in a non-main thread:
Executing script functions

However, I thought it might be possible to just run the scripting system isolated from everything else in another thread somehow. Or maybe a second instance of the scripting system (while restricting access to some functions that touch graphics, for example). I don't know what possibilities there are - my Urho3D experience so far is build it & create & run own project with it -, hence this thread.

Of course, being in C++, I could do threaded game logic myself. However, that would mean not using all the nice Lua intergration that is already there, with all the features attached. And doing my own Lua integration, which might end up worse than the one that is there already, does not sound like a great idea to me.

[quote="Enhex"]2. Premature optimization. You didn't make anything yet and you already decided it isn't performing well.
There are strategy games from 15-20 years ago running many units on a single weak CPU. I think you won't even need multithreading for optimization at all.[/quote]
You do not know anything about what I am planning, nor what I did already, nor what research I did on the subject, nor what experience I have.
Yet here you go, assuming I have no clue what I am talking about and lecturing me.
Don't do that. Besides, do you seriously think a game like Supreme Commander or Europa Universalis is running single-threaded? :smiley:

From experience, I know that this is a detail that is almost impossible to change later on in a timely manner, once all systems are in place. Just like adding multiplayer later on would be (well, usually). So I'd rather solve a problem that is extremely likely to appear before it does. Because I know that it is problematic, I'm not guessing here.

All of that said, I'll do another project first anyway to test engine capabilities. That will already have quite an amount of logic attached (though more at a level that should be doable single-threaded).
I'm just researching possible engines to do that with first.

-------------------------

godan | 2017-01-02 01:13:21 UTC | #4

What about something like this:

- Implement a C++ subsystem that is responsible for calculating the paths of 10000 agents (or something...)
- Implement a nice, quarantined, function that calculates the path for one agent.
- Use the WorkQueue and WorkItem classes to submit all 10000 agents.
- Listen for the E_WORKCOMPLETE event.

Now, this is all C++ stuff. Based on the link you posted, and a quick look at the source, it does indeed look like you can't access the threading system via script. However, could you not expose a couple high level functions of the above C++ subsystem to script? Something like "PushAgent", "GetAgentPaths", "IsCalculationDone", etc?

Note that adding things to the Scene is certainly not thread safe, but raycasting is fine, as are most read operations (I think). 

Basically, I'm suggest the old proverb: "Anything can be fixed by adding a level of abstraction"   :slight_smile:

-------------------------

cadaver | 2017-01-02 01:13:21 UTC | #5

I would second godan's suggestion. Note that depending on the kind of modifications being done to the scene, even reading may not be safe. If objects just move, it's generally safe to raycast into the scene in other threads. However if you're creating and deleting objects, this involves reallocation (iterator invalidation) in various structures such as scene's child node vector, or the octree, in which case you could have an occasional unpredictable crash. One way to mitigate this is to have phases within the frame that are guaranteed to finish first before moving to another, for example 1) object creation/destruction phase 2) threaded work phase. IMO the best solution is to have the threaded worker things operate on their own data outside the scene.

If you want a large amount of units, I'd really recommend doing everything performance-critical in C++, since you have that option. Actual script language could take care of user-facing elements like UI, or some infrequent event triggers.

However it's also true that Urho is heavily based on a single main thread paradigm, in the interest of retaining the engine simple and easy to use (multithreaded gameplay scripting is loaded with pitfalls, if you think about it). The reality is that for some projects this will be inadequate. It's also unlikely to change without a major rework. In that case it's no shame to choose another engine instead of Urho, if you find one that's more fitting.

-------------------------

TheSHEEEP | 2017-01-02 01:13:21 UTC | #6

Thanks for the input, there are some good suggestions.

Pathfinding is certainly something I'd like to do on another thread anyway - however, I don't know if that lends itself well with Detour/Recast.
The only thing I did with it once was basically calling a function that would give a possible way from point A to B within the navigation mesh.
Now that, I think, would be safe to do on a WorkItem.
However, in a real game, these pathing calculations would have to be updated taking into account the positions of other agents. I'm not quite sure how that works in Detour or Urho, but I'll look at the pathfinding example to see how it is done in the engine.
But pathfinding is something I'd mostly do in C++ anyway, I wouldn't want that in gameplay scripts (not more than "actor:moveTowards(targetCoordinates, whenReachedCallback, whenBlockedCallback)" at least). Ideally, scripters shouldn't worry about pathfinding at all.

[quote]IMO the best solution is to have the threaded worker things operate on their own data outside the scene.[/quote]
I fully agree. However, how would that even be possible with gameplay data? You can't have each WorkItem have its own copy of the game world :wink:
That's the problem with worker queues. They are just not applicable in many situations. Not for gameplay logic, at least.
Imagine a forest where thousands of beings are just doing their business, the AI for each one calculating next steps based on information about the world, its surroundings, etc. You cannot have thousands of copies of relevant game data. Imagine the synching afterwards :smiley:

But I think your suggestion to split everything into phases would solve the problem acceptably. It is really not important for gameplay calculations if they are based on 1 frame old logic. So the bird following its prey in the forest would be advancing by some space, even though the prey just got eaten by the wolf, which the bird would be noticed of only next frame. Perfectly acceptable.
So, a very simplified game frame could look like this (assuming that there is separate set for gameplay and Urho data, which is a good idea anyway):

1. Object creation/deletion (including callbacks to Lua scripts to notify about object deletion so that Lua scripts can remove references, like the bird losing the prey reference)
2. Game logic (threaded, step 3 happens before step 2 finishes), which changes gameplay data ONLY
3. Urho engine loop, which changes Urho data ONLY
4. Wait for step 2 to finish
5. Apply gameplay data to Urho data*

*And vice versa! If physics says the bird is at X, but gameplay says the bird is at Y, that must be resolved somehow. Not an easy topic, I know.
Actually, I will look at the physics sample, maybe it is possible to do the physics calculations extra between step 1 and 2. Would be worth it just to avoid that synchronization nightmare - at least if not much is going on physics wise (and it isn't in my ideas).

Bonus question: If I activated LuaJIT when building Urho3D, do I have to take any additional steps to make sure LuaJIT is used instead of the slower "normal" Lua?

-------------------------

TheSHEEEP | 2017-01-02 01:13:21 UTC | #7

Considering doing the physics calculation earlier than the rendering:
There is the Engine::runFrame method, which I suppose is responsible for ... well, doing one entire frame.
However, looking at that function, I cannot figure out how I could split up that process to decide when to do the single steps myself.

What I'm looking for is basically something like:
doPhysicsFrame()
doPathfindingFrame()
doAudioFrame()
doRenderFrame()
etc.

To decide myself when to do which part.

I know I could get the PhysicsWorld from the scene and simply call Update(time) on that myself. And probably do exactly the same thing with the other components like CrowdManager.
But if I did that, I could not make use of the runFrame method any more, correct?

-------------------------

cadaver | 2017-01-02 01:13:22 UTC | #8

You can take a look at [urho3d.github.io/documentation/H ... _loop.html](http://urho3d.github.io/documentation/HEAD/_main_loop.html) which explains the events sent as a result of RunFrame(). Customizing the execution order is likely to require engine changes. The hardest part to untangle is the scene update, where both physics & crowd manager hook into the scene subsystem update. Maybe you could get away with not calling Scene::Update() at all, but I don't explicitly recommend it, since you would cripple related functionality (scene async loading, attribute animations)

-------------------------

TheSHEEEP | 2017-01-02 01:13:22 UTC | #9

I see. In that case, I think could listen to E_SCENEPOSTUPDATE (or another one that happens after physics, but before most other things) and start the gameplay logic there.
Well, that's one problem solved (in theory, at least :wink: ).

Pathfinding would be great to do threaded as well, but that one really would count as premature optimization.

-------------------------

TheSHEEEP | 2017-01-02 01:13:23 UTC | #10

Hmmm, after having a more in-depth look at the documentation and the Lua scripting, I noticed that tolua++ was used.
That shocked me quite a bit, to be honest, as tolua++ hasn't been maintained for years and supposedly suffers from quite a lot shortcomings (naturally, dead code usually has that habit :slight_smile: ).
Did you make changes to the library?

In the end, it might be wisest for me to just roll my own LuaJIT binding, also considering that I won't be able to use too much of the already existing one due to the threading.
It might also make it easier to apply my game logic states to Urho's internal components. I could do a clear separation that way.
Besides, I already used OOLUA and it worked fine for me (though I will look at other bindings, too, [url=http://sol2.readthedocs.io/en/latest/]Sol2[/url] seems highly promising).

Now, if I did not use any of Urho's own scripting, do you think I could still use the LuaJIT that is compiled into the Urho library, or is there anything that would prevent that (custom source modifications or something like that, maybe)?

Also, this was probably missed last time due to my wall of text (sorry):
[quote]Bonus question: If I activated LuaJIT when building Urho3D, do I have to take any additional steps to make sure LuaJIT is used instead of the slower "normal" Lua?[/quote]

Sorry for derailing my own thread, you can split this topic if you want, of course :slight_smile:
And finally, don't get me wrong, I'm complaining a lot here, but I really like what I see so far (except tolua++, tz!). 
You are right that no engine should try to perfectly fit all purposes and I get the decision to stay single-threaded (it is fine for most cases, I'm sure).
And from the looks of it, I can easily change what I have to change in order to make Urho fit my needs better.

-------------------------

cadaver | 2017-01-02 01:13:23 UTC | #11

Aster is working on updated Lua bindings using a different library (Kaguya), however they will take some time still. We are well aware of tolua++'s shortcomings.

Be aware that when speaking of Urho scripting languages, AngelScript was integrated first and actually informed some of the design decisions in the engine itself, like reference counting. It also comes with its inbuilt bindings system. Lua was integrated later, and practically requires a separate binding library (which may not match with the engine 100%), so it will practically always remain a second-class citizen in comparison, no matter how well done the Lua bindings are.

-------------------------

weitjong | 2017-01-02 01:13:23 UTC | #12

I just want to add that although it is considered as second-class citizen, the "LuaScript" subsystem is deemed stable enough for some that we have decided to enable it by default (via URHO3D_LUA build option). This option will pull normal "Lua" 3rd-party library into the build, unless you explicitly enabled the URHO3D_LUAJIT build option which will instead pull in "LuaJIT" 3rd-party library. Currently, JIT or no-JIT, tolua++ will be used as the tool to auto-generate the Lua API binding source code on the fly. So, if you want to roll your own Lua API binding then you have to modify the build system yourself to replace this portion of the logic. Otherwise, no, there is no extra steps to ensure you will be using LuaJIT once the relevant build option is enabled.

-------------------------

TheSHEEEP | 2017-01-02 01:13:23 UTC | #13

[quote="weitjong"]So, if you want to roll your own Lua API binding then you have to modify the build system yourself to replace this portion of the logic.[/quote]
If I roll my own binding, wouldn't that mean that I can just ignore Urho's one?
Like, simply never create a LuaScriptInstance component.

Though I think the more clean solution would probably be to build Urho completely without scripting support and then link against LuaJIT mysef.

-------------------------

weitjong | 2017-01-02 01:13:23 UTC | #14

It really depends on how deep you want to go. You will have to modify the LuaScript subsystem anyway even when you decide to reuse it.

-------------------------

Enhex | 2017-01-02 01:13:24 UTC | #15

If you're so performance critical that you must use threading, why do you want to use scripting?
Scripting will slow you down much more than threading will speed you up.
You're contradicting yourself.

-------------------------

TheSHEEEP | 2017-01-02 01:13:24 UTC | #16

[quote="Enhex"]If you're so performance critical that you must use threading, why do you want to use scripting?
Scripting will slow you down much more than threading will speed you up.
You're contradicting yourself.[/quote]
1. Slow down? Not much, not if scripting with LuaJIT, it almost reaches C++ performance in many cases, especially if you know how to optimize Lua code. And here, it runs threaded while Urho is busy rendering. Of course, pure C++ running threaded would be even faster, no doubt.

2. The reason is twofold:
- Speed of development. Developing in C++ is slooooooooow. The need to recompile, the need to take good caution in order not to screw things up, etc. 
- Modding capability. This is a must-have for me as I find it vital for the community buildup and longevity of any game. And modding capability without proper scripting? Eh... I'd rather not.

So, yes, it seems contradicting, but having both is a requirement to me. And I'm accepting that it will mean less performance than I'd reach with pure C++.

-------------------------

