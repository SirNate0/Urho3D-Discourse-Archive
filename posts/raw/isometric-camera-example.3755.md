smellymumbler | 2017-11-19 00:37:54 UTC | #1

Is there any example of a good isometric camera, like Fallout or Diablo?

-------------------------

JTippetts | 2017-11-19 01:45:43 UTC | #2

I did a little demo of an isometric camera, with some click-to-move pathfinding some time back. https://github.com/JTippetts/U3DIsometricTest

-------------------------

smellymumbler | 2017-11-21 01:50:41 UTC | #3

I tried to run it, but it didn't work. :frowning:

    ERROR: Could not find resource Scripts/levelgenerator.lua
    [Mon Nov 20 19:42:58 2017] ERROR: Lua Execute failed for Data/Scripts/main.lua: [string "Data/Scripts/main"]:5: module 'Scripts/levelgenerator' not found

-------------------------

JTippetts | 2017-11-21 06:29:32 UTC | #4

That's pretty weird. I just did a clean clone and it works okay for me. Are you using the Urho3DPlayer.exe that comes with it, or are you using a newer one? Because that project is months old, so I don't know  how well it would work with a newer player.

-------------------------

