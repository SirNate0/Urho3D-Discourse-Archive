setzer22 | 2017-01-02 01:05:47 UTC | #1

When is exactly the Start function for Lua ScriptObjects called? 

I've tried checking LuaScriptInstance.cpp/.h and I find it strange because LSOM_START is only declared and never used, unlike the others. So I can't really find where and when is the Start method called.

Thanks!

-------------------------

cadaver | 2017-01-02 01:05:47 UTC | #2

There's Lua code in LuaScriptInstance.pkg which handles the object creation and also calls Start().

-------------------------

setzer22 | 2017-01-02 01:05:47 UTC | #3

Oh, so it's done when the lua binding functions are called, that makes sense.

Thank you! :smiley:

-------------------------

