Bluemoon | 2017-01-02 01:00:33 UTC | #1

The little secret I have about My Urho3D encounter is that I actually found out about Urho3D through AngelScript  :wink:. And to be honest I'm really impressed by the beautiful integration of AngelScript into Urho3D. But the problem is that its really easy to get carried away by this beauty and go on scripting almost every part of your application (I'm "almost" guilty here  :smiley: ). In order to save myself from this easily neglected mistake I'll really like to know the performance hits and penalties that can be incurred while using AngelScript and the areas where they present themselves. And perhaps if there is an advice for a soon-to-become-script-addict I'll really need it  :unamused:

-------------------------

thebluefish | 2017-01-02 01:00:33 UTC | #2

I don't have any numbers, but I did do benchmarking with Angelscript ~2 years ago when I was working with Ogre3D. TBH the performance was pretty bad, it was something like 25-30 times slower than native C++ when it came to some complex calculations. LUA was something like 10-15 times slower than native C++ in comparison. Of course, I only did a few limited tests that may scale better in C++ than any scripting languages.

In Urho3D however, most of the performance-critical parts are ran in native code. If you're writing a game, then most of what you're doing is simply calling native functions to do the actual work, instead of doing the slow calculations directly within your script.

Personally I find it easiest to write most of my objects and game logic in C++ and extend various functionality to scripting. This allows me to maintain tight control of the actual logic, while still allowing easy expandability via scripts. For example, in my multiplayer card game, the base Card class is in C++, while the cards are actually defined via Script. That way the performance critical parts such as shuffling cards, drawing cards, and managing them is handled native while things such as card effects are handled by the script.

-------------------------

Bluemoon | 2017-01-02 01:00:33 UTC | #3

[quote="thebluefish"]
In Urho3D however, most of the performance-critical parts are ran in native code. If you're writing a game, then most of what you're doing is simply calling native functions to do the actual work, instead of doing the slow calculations directly within your script.
[/quote]

 :slight_smile: That's exactly the point I put in mind while scripting being rest assured that the calculation intensive routines are handled in native functions.

-------------------------

izackp | 2017-01-02 01:00:33 UTC | #4

[quote="thebluefish"]it was something like 25-30 times slower than native C++[/quote]

Was this before the JIT version of Angel Script? JIT should be a bit better than that I think...


Nonetheless, Angel Script is really close to c++ so it wouldn't be too hard to port code over ^.^

-------------------------

friesencr | 2017-01-02 01:00:33 UTC | #5

[quote="izackp"][quote="thebluefish"]it was something like 25-30 times slower than native C++[/quote]

Was this before the JIT version of Angel Script? JIT should be a bit better than that I think...


Nonetheless, Angel Script is really close to c++ so it wouldn't be too hard to port code over ^.^[/quote]

Even better than a jit it has an aot. [github.com/quarnster/asaot](https://github.com/quarnster/asaot)  It will convert angelscript to c++.  I havn't tested it though.

-------------------------

thebluefish | 2017-01-02 01:00:34 UTC | #6

[quote="izackp"][quote="thebluefish"]it was something like 25-30 times slower than native C++[/quote]

Was this before the JIT version of Angel Script? JIT should be a bit better than that I think...[/quote]

I believe so, but I can't be 100% certain. Any decent JIT should be close to C++ performance-wise methinks. 2-3x slower would be perfectly acceptable in that case.

I wonder if we can get some performance tests utilizing Urho3D, comparing native, Angelscript, and LUA.

AOT compilation would be nice, but I'm concerned if it would affect device compatibility given the various different architectures we can port to. Maybe include the scripts, and have the engine automatically save the bytecode on first execution?

-------------------------

boberfly | 2017-01-02 01:00:34 UTC | #7

Oh yeah I almost forgot about this AOT compiler for Angelscript, very cool. There's no docs on how to use it but I guess it could make sense from reading the samples for awhile.

This makes me think about working on my failed attempt again at porting Urho3D to Emscripten/HTML5, and I see SDL2 is now ported over. Having angelscript go into AOT form would let it turn into LLVM bytecode and then eventually javascript. Originally having angelscript being interpreted in javascript would've been painful for performance I'd imagine.

Now, hurry up WebGL I want GL 4.5 features in there already... :slight_smile:

-------------------------

marynate | 2017-01-02 01:00:34 UTC | #8

[quote="thebluefish"]
...
I wonder if we can get some performance tests utilizing Urho3D, comparing native, Angelscript, and LUA.
...
[/quote]

I did a comparison using sample 24 Urho2DSprite with 2000 sprites, here's the result:

[ul]
[li]c++ [b]970[/b][/li]
[li]Angelscript [b]280[/b][/li]
[li]LuaJIT [b]112[/b][/li]
[li]Lua [b]85[/b][/li][/ul]

and if anyone curious, same test with unity and godot (2000 random moving 2d sprites):

[ul]
[li]Unity [b]340[/b][/li]
[li]Godot [b]170[/b][/li][/ul]

-------------------------

thebluefish | 2017-01-02 01:00:34 UTC | #9

I'm guessing that's FPS?

That kind of slow-down is fairly acceptable for scripting, certainly much better than it used to be.

As long as the performance-critical parts are left to native, it should be easy to get top-notch performance while still being able to extend plenty of functionality to scripting.

-------------------------

izackp | 2017-01-02 01:00:35 UTC | #10

[quote="thebluefish"]AOT compilation would be nice, but I'm concerned if it would affect device compatibility given the various different architectures we can port to.[/quote]

Another thing to consider is that it is against Apple's policy to dynamically load native code on iPhones. So, JIT compilation is out of the question for iOS devices. 

From what I've seen the code gets compiled to c++ which means you should be able to compile the script for any device that c++ supports.

-------------------------

thebluefish | 2017-01-02 01:00:35 UTC | #11

Ah ok, I didn't read too much on AOT compilation, so I thought it still dynamically loaded it much like JIT.

-------------------------

gokr | 2017-01-02 01:00:36 UTC | #12

[quote="marynate"][quote="thebluefish"]
...
I wonder if we can get some performance tests utilizing Urho3D, comparing native, Angelscript, and LUA.
...
[/quote]

I did a comparison using sample 24 Urho2DSprite with 2000 sprites, here's the result:

[ul]
[li]c++ [b]970[/b][/li]
[li]Angelscript [b]280[/b][/li]
[li]LuaJIT [b]112[/b][/li]
[li]Lua [b]85[/b][/li][/ul]

and if anyone curious, same test with unity and godot (2000 random moving 2d sprites):

[ul]
[li]Unity [b]340[/b][/li]
[li]Godot [b]170[/b][/li][/ul][/quote]

Soo... Angelscript is faster than LuaJIT? And only a tad faster than regular Lua? That sounds.... odd. Can you share how you compared?

regards, G?ran

-------------------------

cadaver | 2017-01-02 01:00:36 UTC | #13

I understood that in things like array/table access Lua will have an advantage, as Lua arrays are native to the language, while in AngelScript they are bound like any external class and induce calls through the binding system.

Moving a large amount of sprites will stress mainly the bindings (GetPosition(), SetPosition() etc.)

I know Lua will suffer a large overhead if the bindings safety checks are enabled (-DURHO3D_SAFE_LUA=1) but they should be off by default.

-------------------------

marynate | 2017-01-02 01:00:36 UTC | #14

[quote="gokr"]
Soo... Angelscript is faster than LuaJIT? And only a tad faster than regular Lua? That sounds.... odd. Can you share how you compared?

regards, G?ran[/quote]

For testing scene, I use  24_Urho2DSprite (bumping the sprite count up to 2000)

For building Urho3DPlayer, I used following defines:

c++ / angelscript / luajit
[code]-DURHO3D_OPENGL=1 -DURHO3D_LUA=1 -DURHO3D_LUAJIT=1 -DURHO3D_SAMPLES=1 -DURHO3D_TOOLS=1 -DURHO3D_EXTRAS=1 -DURHO3D_MINIDUMPS=0[/code]

lua
[code]-DURHO3D_OPENGL=1 -DURHO3D_LUA=1 -DURHO3D_LUAJIT=0 -DURHO3D_SAMPLES=1 -DURHO3D_TOOLS=1 -DURHO3D_EXTRAS=1 -DURHO3D_MINIDUMPS=0[/code]

-------------------------

gokr | 2017-01-02 01:00:38 UTC | #15

[quote="cadaver"]I understood that in things like array/table access Lua will have an advantage, as Lua arrays are native to the language, while in AngelScript they are bound like any external class and induce calls through the binding system.

Moving a large amount of sprites will stress mainly the bindings (GetPosition(), SetPosition() etc.)

I know Lua will suffer a large overhead if the bindings safety checks are enabled (-DURHO3D_SAFE_LUA=1) but they should be off by default.[/quote]

I played around a bit myself and also read up on the net. Feel free to correct me but I think that tolua++ uses the regular Lua C API for integration. Its quite slow, and tolua++ is also considered to be quite slow compared to many of the other C++ binding generators like Dub or OOLua. Now... if one wants to get the full insane speed of LuaJIT one should [b]ideally[/b]:

[ul]
* Use LuaJIT FFI for calling into C
* As much as possible avoid callbacks from C into Lua
[/ul]

LuaJIT FFI is crazy good and makes C calls as cheap as they are in C itself. Yeah, really. And LuaJIT seems to be able to inline them while JITting too. Unfortunately there aren't that many C++ binding generators that use LuaJIT FFI (I found a few experiments). But calling back into LuaJIT is costly even using LuaJIT FFI - I think like... 30x slower, so the advice from Mike Pall (LuaJIT genius author) here is "don't do it". At least not many, many times :

 So... if we have TONS of objects and these are iterated over in C (say on every frame) and we do callbacks into LuaJIT for updating them - [b]we get hosed by the overhead[/b]. The fact that Lua is almost the same speed as LuaJIT is very telling here. LuaJIT should SMOKE it.

So what to do about callbacks? One way is to move the loop to Lua and "pull" the objects via an API over some iterator in C. This would turn it to "calls from Lua to C" and thus remove the overhead completely. Mike calls this a "pull" API instead of a "push" API design.

Since we want to basically build everything in Lua this may become important to us. And just so everyone knows - LuaJIT is very, very, very fast. It "should" generally beat the pants of regular Lua and Angelscript and come close to C++ speed. The numbers imply that all of that speed is lost here.

-------------------------

