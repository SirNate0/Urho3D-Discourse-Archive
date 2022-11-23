jjy | 2017-01-14 06:28:02 UTC | #1

I just want to find a way for script components communication. I looked through the code of ScriptInstance but I don't find any api for this except event. 

It will be nice if something like the following is supported.

[lua]
local cmpt = self.node:GetComponent("OtherScript")
cmpt:callSomeMethod()

If it is not supported, how much work is needed to add this feature?

-------------------------

Eugene | 2017-01-14 08:06:49 UTC | #2

+1, I wanted such feature.
However, I don't know good design for such functionality because GetComponent now searches C++ components.

-------------------------

jjy | 2017-01-14 13:41:57 UTC | #3

After some research, it seems that Urho3d uses a shared lua state across the app. And the LuaScriptInstance creates an instance of the LuaScriptObject when the script is loaded. If we can created a global variable holding the LuaScriptObject instance, then we can access it from other script components.  Variable name collision may be a problem. Some naming convention is needed. Finally, add some GetComponent methods to the LuaScriptObject class to find the right object quickly.

I'm new to Lua and Urho3d. Any suggestions?

-------------------------

JTippetts1 | 2017-01-16 13:46:56 UTC | #4

local thingamajig=node:GetScriptObject("WhichScriptObject")
thingamajig:doohickey()

-------------------------

jjy | 2017-01-16 10:04:36 UTC | #5

It works. Thank you.

How to reload the whole lua state in editor? I have to restart the editor every time I changed the script.

-------------------------

Eugene | 2017-01-16 15:43:06 UTC | #6

Great! This is already implemented!
I use to miss some nice Urho features...

-------------------------

JTippetts1 | 2017-01-16 20:04:09 UTC | #7

I think that re-loading a script in Lua is still problematic. The AngelScript module has no issues with destroying/rebuilding a component on script reload, but I'm not sure they ever did really concoct a way to do the same elegantly in Lua. You can re-load the file, but I don't believe that will affect any script objects already in existence.

-------------------------

