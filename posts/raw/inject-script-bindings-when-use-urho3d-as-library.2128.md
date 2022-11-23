Eugene | 2017-01-02 01:13:18 UTC | #1

I want to export some new components/functions/etc to Lua and AS.
Do you have some best practice for such task?
I don't want to change source of Urho3D master repo until it is the last chance.

-------------------------

cadaver | 2017-01-02 01:13:19 UTC | #2

For AngelScript, you can get the AngelScript engine from the Script subsystem, then proceed to register your interface similarly to how Urho does it for the inbuilt classes.

For Lua maybe someone else can fill in details, but the basic principle is that you need to have your generated bindings functions, and register them to the Lua state you can get from the LuaScript subsystem. Inbuilt bindings have the functions tolua_XXXLuaAPI_open(lua_State*) per subdirectory or subsystem.

-------------------------

