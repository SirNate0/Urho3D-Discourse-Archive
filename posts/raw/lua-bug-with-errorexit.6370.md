SuperVehicle-001 | 2020-09-06 02:16:08 UTC | #1

Not 100% sure if this is the place for it, so I apologize beforehand if it isn't.

ErrorExit() closes the application and creates an error window when called, however it doesn't do that in Lua. When calling ErrorExit() from Lua, the application will be closed but there won't be an error message.

It's not a big deal, since one can use ErrorDialog() for the error message then call ErrorExit() immediately after that, but still worth mentioning. I'm on version 1.7.1 of the engine, by the way.

-------------------------

Modanung | 2020-09-06 07:45:19 UTC | #2

[quote="SuperVehicle-001, post:1, topic:6370"]
I’m on version 1.7.1
[/quote]

Did you try with the lasted master from GitHub?
When you have - and the problem persists - it might be worth opening an issue.

-------------------------

SuperVehicle-001 | 2020-09-06 21:14:43 UTC | #3

I've tried it and it still happens, yes.

Call ErrorExit() anywhere in ```Rotator.lua```, then boot 22_LuaIntegration. It will close with no message window regardless of what arguments are or are not given.

-------------------------

Modanung | 2020-09-06 22:49:08 UTC | #4

Then you may want to open an issue.

-------------------------

