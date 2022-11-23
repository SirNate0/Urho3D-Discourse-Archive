Mike | 2017-01-02 00:58:20 UTC | #1

After using UnsubscribeFromAllEvents() I can't issue commands in the console.
Is it the intended behavior and if so how to reactivate commands?

For example, in Sample.lua, if I do something like:

[code]
        engine:CreateConsole()
        UnsubscribeFromAllEvents()
        engine:CreateConsole()
[/code]
Then I can't issue commands anymore.

-------------------------

cadaver | 2017-01-02 00:58:20 UTC | #2

In the current LuaScript implementation, this means literally unsubscribe from all, even those the LuaScript system is internally listening to. This should be quite easy to fix.

EDIT: this should be fixed now in latest master.

-------------------------

Mike | 2017-01-02 00:58:20 UTC | #3

Great, everything is OK  :stuck_out_tongue:

-------------------------

