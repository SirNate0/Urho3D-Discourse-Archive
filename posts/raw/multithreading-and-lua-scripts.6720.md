Lys0gen | 2021-02-18 19:24:23 UTC | #1

Hello,

to my disappointment I realized that [Urho does not support running scripts outside of the main thread](https://urho3d.github.io/documentation/HEAD/_multithreading.html). I only found [this thread](https://discourse.urho3d.io/t/scripts-in-other-threads/2132) that expresses similar concerns but no ideal solution. That was quite some time ago, perhaps by now someone knows of a better way to handle this.


Assuming that using AngelScript instead of LUA would have the same issue, I only see two options:

a) Modify Urhos LUA subsystem so that there can be multiple LuaScript instances (one for each thread) which don't interfere with each other. No idea how feasible/how much work this would be
b) Ditch Urhos LUA altogether and use a different, perhaps more up to date, implementation that can do this. What would be best here?
c) ...other ideas?


If you wonder **why** I want this it is simple: In my game I have multiple AI actors and I want their behaviour completely scriptable but also run in threads as these scripts could get expensive or there could be a lot of actors at the same time.

Trying it out I had to find out the hard way that running the script in a thread (not even parallelizing the scripts themselves, just having a single worker thread in the background) definitely crashes the application after some ticks.

Thanks for any input.

-------------------------

S.L.C | 2021-02-18 19:56:37 UTC | #2

The engine itself cannot be used most of the time from other threads even from C++. This is not a scripting only problem. Actually, it's not even a problem. That's just how things work in a game engine. Imagine every function and method having to acquire locks in order to be thread safe. Your performance would be out the window instantly.

At most you can do is create a worker that can process data separately. Assuming whatever it processes doesn't touch the rest of the non-thread-safe code. Which is pretty much everything. This works well for loading resources and doing computationally intensive tasks like dealing with occlusion and stuff like that.

So with that in mind, the same concept could probably be applied to scripts as well. You basically create a separate script state that poses as a worker and all it does is process stuff. But not touch anything from the engine. Basically it'll be mostly empty isolated state for processing and logic only.

And then you'd have to find ways to communicate between those script threads. That's just how scripting engines have been and will continue to be. I'm not really sure how you expect it to be. There is no alternative if you're looking for one tbh.

Either way, you'll have to get your hands dirty and do some c++ :smiley:

-------------------------

Lys0gen | 2021-02-18 20:38:01 UTC | #3

[quote="S.L.C, post:2, topic:6720"]
You basically create a separate script state that poses as a worker and all it does is process stuff. But not touch anything from the engine. Basically it’ll be mostly empty isolated state for processing and logic only.
[/quote]

Yes that is how pretty much everything is already.
All the game logic is independent of Urho, pretty much the only contact points are when I handle UI events or in reverse update the UI/rendered objects with game data. Well now of course with the exception of where I call the LUA scripts.

[quote="S.L.C, post:2, topic:6720"]
So with that in mind, the same concept could probably be applied to scripts as well. You basically create a separate script state that poses as a worker and all it does is process stuff.
[/quote]
And that is pretty much also what I do. I basically have a LUA function, lets call it "processAI" which gets passed an user object. The script then evaluates the object (no connection to anything of Urho) and may or may not queue a few "todos" by calling a (threadsafe) C++ function that I created bindings for with tolua++.


Now the crashes are pretty random, sometimes after 5 seconds, sometimes it runs fine for a couple of minutes. But they are definitely caused by the LUA subsystem and there must be a way around that, I'm just not sure which path would be the best to achieve that.

-------------------------

S.L.C | 2021-02-18 22:48:08 UTC | #4

[quote="Lys0gen, post:3, topic:6720"]
Now the crashes are pretty random, sometimes after 5 seconds, sometimes it runs fine for a couple of minutes. But they are definitely caused by the LUA subsystem and there must be a way around that, I’m just not sure which path would be the best to achieve that.
[/quote]

I'm guessing that you're using the same Lua state in more than one thread? Since you're saying Lua is the only thing you're doing work with.

Isn't there some native multi-threading available directly for Lua? I don't really touch Lua in general but being popular there's bound to be an external library or something like that which enables multi-threading  without explicit help from Urho engine. Like [this](https://github.com/effil/effil) for example.

Basically, enough to give you a parallel sub-routine or something like that where you can do your AI stuff.

-------------------------

JSandusky | 2021-02-20 21:05:46 UTC | #5

From the outside Lua is thread-safe only if you access the `lua_state` from only 1 thread at a time, so you can have multiple lua_states in threads but not one master. That creates some headaches as both bindings and table instances are centered around the state objects.

So you have to use some flavor of inside-lua-specifically library like @S.L.C points or work around it with C++ side objects that are storing the data that needs to be shared. So you could cludge in some threading where you only access some specific Urho3D native objects and that'd work where you spin up a number of lua_state's for each thread by refactoring the `LuaScript` class.

You could plausibly concoct some table registration scheme to register them for synchronization but that'll be a can of worms and you'll have both choke-points where you have to trigger the sync and have an additional "dirty" marking layer (most likely in your metatables, thus interfering with any Lua class library you're using). Won't be pleasant.

Angelscript has similar problems too, so changing language won't help.

-------------------------

Lys0gen | 2021-02-20 21:05:35 UTC | #6

Thanks for the input! I think I still haven't made my setup 100% clear, all I needed was a way to call a "processing function" on multiple threads. No resource sharing between those threads. Anyway


[quote="JSandusky, post:5, topic:6720"]
so you can have multiple lua_states in threads but not one master.
[/quote]

this is what I'm doing now. I now ditched Urho's Lua subsystem as it seems to be designed to only ever have one global state (although I did lift a lot of functionality from the relevant code parts).

What I'm doing now is:
1. Create X new threads, each of them initializes their own lua_State with tolua bindings and so forth, then loads the required script files
2. Every thread has a work queue which gets filled with LUA function calls, by default it is set to wait with a std::condition_variable
3. When I want the functions to be processed I poll the condition_variable

Seems to work great so far, at least I haven't experienced any crashes yet.

Thanks again!

-------------------------

George1 | 2021-02-21 23:21:29 UTC | #7

You can do most things on different threads...   Compute path, change positions etc..   But don't add and remove node or component on your thread.  When adding boolean condition to delete component or node, you have to monitor and manage this in both the main and your threads.

-------------------------

