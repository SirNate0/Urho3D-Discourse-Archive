buhb11 | 2017-01-02 01:04:13 UTC | #1

Hello!

I'm very new to Urho3D and I'd like to start using it as my main game engine/framework for now on.But first I need to know if I can only use Lua whitout c++.Or only use C++ if I need something to be implemented.Can I do that and still make games/apps for android with only lua?Where can I download some Lua examples?  :slight_smile:

-------------------------

hdunderscore | 2017-01-02 01:04:13 UTC | #2

Yes, you could use Urho with Lua only (eg, look at Bin/Data/LuaScripts, you will see all the samples are available in Lua), you could also use AngelScript and C++ as almost all samples are available in each for demonstration.

-------------------------

GoogleBot42 | 2017-01-02 01:04:13 UTC | #3

Make sure you enable lua when compiling Urho3D because is isn't enabled by default.  See here: [url]http://urho3d.github.io/documentation/1.32/_building.html[/url] This might be useful too if you are less clear on how to compile:  [url]http://urho3d.wikia.com/wiki/Build_Urho3D_on_Windows_%28MinGW%29[/url]

Here is the lua documentation: [url]http://urho3d.github.io/documentation/1.32/_lua_scripting.html[/url]   :wink:

EDIT: You will probably want this too: [url]http://urho3d.github.io/documentation/1.32/_running.html[/url]

-------------------------

konradbeck | 2019-11-03 16:18:39 UTC | #4

 @hdunderscore,

You mention that 'Yes, you **could**' but **should** you?

When does using a scripting language become advantageous?

If I wanted to design a game with many levels is this where a scripting language would shine?

Or when multiple versions were released, would a script be more beneficial if no new features were introduced?

-------------------------

JTippetts | 2019-11-03 21:49:31 UTC | #5

Lua is just another language. The main benefit it offers is essentially in allowing you to skip the compilation step, which can mean faster iteration time during design/prototyping. There is nothing keeping you from mixing C++ and Lua as needed. I've found it beneficial to use Lua for things such as AI script components, while implementing performance-critical stuff in C++.

Note that there are still [issues](https://github.com/urho3d/Urho3D/issues/649) regarding garbage collection if you generate lots of garbage at one time, without interleaved GC sweeps in Lua. It can be mitigated by explicitly calling the GC when you are doing garbage-heavy things like iterating all the pixels of an Image or things of that nature, but it's something to be aware of. Anything that returns an Urho3D object by value is a potential pain point here, so things like procedural generation of various things might better be implemented in C++.

-------------------------

