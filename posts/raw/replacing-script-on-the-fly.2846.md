slapin | 2017-03-03 18:12:43 UTC | #1

Hi, all!

How can I replace script on the fly from the same script?

I try to do this:

                   node.RemoveComponent("ScriptInstance");
                   node.CreateScriptObject(scriptFile, "Dummy");
 
but I get null pointer with 2nd line. Any ideas?

-------------------------

1vanK | 2017-03-03 18:45:26 UTC | #2

You remove a script from himself and wonder why it does not works?

-------------------------

slapin | 2017-03-04 16:17:58 UTC | #3

Well, I don't see anywhere that I can't do this. Can I?
The logic that script have to be changed is inside script. Any tricks?

-------------------------

1vanK | 2017-03-04 16:25:37 UTC | #4

> The logic that script have to be changed is inside script. Any tricks?

```
if (state == 1)
  do1();
else if (state == 2)
  do2();
```

-------------------------

slapin | 2017-03-04 16:30:29 UTC | #5

Well, my script is about 2MB and I want to refactor it so that it uses separate classes, otherwise it is out of control. I currently have this approach but my behavior trees got too big to implement this as simple sequence of ifs. Asso state machinery became so complex it is hard to add additional states or make changes without breaking things :(

-------------------------

Eugene | 2017-03-04 18:13:07 UTC | #6

I somewhy think that ScriptComponent doesn't have to be implemented in single *.as file. Why not to use `#include`s and refactor your script code without dynamic change of script class?

You may also try to add script component first and then remove old component.

-------------------------

slapin | 2017-03-04 19:05:09 UTC | #7

Well, the problem is more complex than that.

Imagine I have 3 NPC types
Station - stays in place, doesn't walk anywhere, doesn't interact with environment
Wanderer - selects goals according to its internal state and walks everywhere needed
Chaser - follows player or other NPC.

All NPCs can be friend/neutral and enemy to player and any other NPC/faction.
Also NPCs are visually different, some are unique.
Also there is dependency on distance - 3 versions of NPCs are for far away, away and close.
They differ in behavior and many other aspects (like path-based motion vs physics-based motion)
Also any NPC can become any different type because of player actions dynamically as many times as needed as quickly as needed.

So there are many complicated things associated with each NPC.
At first I implemented a script (with many #includes) which I used for NPC for all things,
but everything depended on everything and intermixed. I implemented more or less
proper class system to isolate some things, but quickly found that many things in
each NPC system supersede each other. And now I think that instead of writing single complex class (of ScriptObject) which would handle everything I might write several completely independent classes,
which would handle different aspects of NPC and replace them on the run.
Is it right idea or should I do something else to reduce complexity and finally start to understand what is going on? As I want to add IK to characters and clothes system, which will farther complicate
NPC script and with current state I will have big trouble adding there anything at all :(

-------------------------

slapin | 2017-03-05 13:12:01 UTC | #8

Well, I found solution - I just need ti implement Behavior trees and load them as needed.
The concept seems to work very well and makes code very simple.

-------------------------

