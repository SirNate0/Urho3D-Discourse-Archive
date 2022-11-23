xpol | 2017-01-02 01:02:39 UTC | #1

Currently the lua script for a script object is like this:

[code]
-- Rotator.lua
Rotator = ScriptObject()
-- ...
[/code]

This is fine, but it uses global to communicate.
It could be better if we do:

[code]
-- Rotator.lua
local Rotator = ScriptObject()
-- ...

return Rotator
[/code]

and use require system or at least the script return value for getting the Rotator object instead of globals.

-------------------------

