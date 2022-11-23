Hevedy | 2017-01-02 01:01:55 UTC | #1

GameMonkey Script looks like good mix and simple between the Angel and Lua scripts and more simple than Angel is possible add this to Urho ?
[gmscript.com/](http://www.gmscript.com/)

-------------------------

OvermindDL1 | 2017-01-02 01:01:56 UTC | #2

[quote="Sinoid"]Pretty much everything here: [post3098.html#p3098](http://discourse.urho3d.io/t/python-scripting-addition/485/5) applies to any scripting language you'd want to add.[/quote]
It would be very nice to create external library mappings for all of Urho3D Scriptable functions, then dynamically load (or statically build in) different scripting engines that use those.  That would allow every type of language from informed mappings like AngelScript, GameMonkey, Lua, and Python, to allowing languages like luajit to use their full FFI mappings at full speed.  That would be the best thing to do overall.  I would start with just a Urho3D CMake module like the current AS or LUA modules that handles dynamic and static scripting binding loading as well as an exposed C interface for them to use.

-------------------------

silverkorn | 2017-01-02 01:02:01 UTC | #3

I guess you guys should follow this Github issue then: [github.com/urho3d/Urho3D/issues/490](https://github.com/urho3d/Urho3D/issues/490)

-------------------------

