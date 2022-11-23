setzer22 | 2017-01-02 01:06:01 UTC | #1

For this thread I'll talk about the Lua implementation but I think everything applies to AngelScript as well. 

My idea is making multiple LuaScript subsystems at the same time possible. A very useful use case for this is allowing the programmer to create two separate script APIs, one for the Lua parts of the game code (This one would have all the Urho3D API available) and another one targeted to mod scripts, with a custom-defined API and no access to Urho3D whatsoever.

It's not an option to use the current LuaScript subsystem to create a mod API for a game because having access to the context and the scene makes cheating incredibly easy, and unless that's the intended behaviour, the mod API should be clearly a sandboxed environment.

My idea in order to implement this into Urho is to create a base class LuaScriptAbstract from which LuaScript would inherit its functionality, moving all the generic stuff in the base class, and leaving just the Urho API registration in LuaScript. After that, anyone can subclass LuaScriptAbstract and inherit functionality such as ExecuteFile or FindFunction, without having to worry about the lua_State having all the Urho3D types and classes already bound.

With this, the programmer can easily register LuaScript and ModLuaScript as two sepparate subsystems and use both as needed, so programming the game in Lua remains an option while being able to create a Lua mod API.

I'm going to implement this and submit a pull request if I manage to do it alright. Comments are welcome!

-------------------------

setzer22 | 2017-01-02 01:06:01 UTC | #2

As a quick fix, a simpler way to do it is just to add an optional boolean (defaulting to true) telling LuaScript's constructor whether to register Urho3D's functions. Then, one could simply subclass LuaScript and call the parent's constructor with false as a parameter, something like this:

[code]
class ModLuaScript : public LuaScript {
    OBJECT(ModLuaScript);
public:
    ModLuaScript(Context* context) : LuaScript(context, false) { }
    virtual ~ModLuaScript() { };
};
[/code]
With this, all the code already using LuaScript remains untoched. But I'm not actually sure if LuaScript would fit the requirements for being a subsystem with this (i.e. Having a constructor that only takes one parameter, the context). I'm assuming optional parameters don't count in this case. Anyway I've done it and it certainly works for me. 

What are your thoughts on this guys? It would be good to hear from someone who knows the Lua subsystem better than myself in order to make a proper fix, this feels hack-ish.

-------------------------

