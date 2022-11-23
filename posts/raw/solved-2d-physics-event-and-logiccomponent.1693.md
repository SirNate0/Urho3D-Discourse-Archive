Botanick | 2017-01-02 01:09:31 UTC | #1

Hello \0

I am trying to sort out the 2d Physics implementation stuff for myself. Right now [i]LogicComponent[/i] do not have any subscription for 2d physics update events, so we can't use [i]LogicComponent#FixedUpdate[/i] and other fixed update related methods in this case because no one will call them :frowning: . How we are supposed to fixed steps for 2d graphics in this case? subscribe manually? or may be extending [i]LogicComponent[/i] class?

-------------------------

Botanick | 2017-01-02 01:09:33 UTC | #2

Another question is: do we think that [i]PhysicsWorld2D[/i] and 3D version of it [i]PhysicsWorld[/i] can exists simultaneously? if no - then I can just subscribe LogicComponent for the 2D events, if 2D physics world component created

-------------------------

cadaver | 2017-01-02 01:09:33 UTC | #3

In this case the correct way is to add this functionality to LogicComponent, instead of using workarounds. It seems to simply be an overlooked case.

-------------------------

cadaver | 2017-01-02 01:09:33 UTC | #4

Should now be fixed in master branch for all of LogicComponent, ScriptInstance and LuaScriptInstance.

-------------------------

