najak3d | 2021-07-19 05:12:05 UTC | #1

Urho docs say this about it Material.SetGlobalVar:
Set global variable with the respective key and value.


What does this mean?  It sounds potentially appealing.   I often have many copies of the same material, and I have need for updating the same parameter on all of them to the SAME VALUE.   Currently, I'm doing a foreach() through all material instances and called "SetShaderParameter(...)" for each.  It would be nice to have a global variable that they all look to for their uniform value.

-------------------------

Eugene | 2021-07-19 19:16:04 UTC | #2

[quote="najak3d, post:1, topic:6929"]
What does this mean?
[/quote]
It's the same thing as
`static Variant x = <something>`
somewhere in your code, except you can access it by name anywhere.

Global vars are (almost) ignored by the engine.

-------------------------

najak3d | 2021-07-19 19:15:59 UTC | #3

What are some typical usages for the "static Variant" construct?  Where is it useful, and why?

-------------------------

Eugene | 2021-07-19 19:19:40 UTC | #4

[quote="najak3d, post:3, topic:6929"]
Where is it useful, and why?
[/quote]
If you want to have some global state which you want to access in different places, and you don't have good native way to do it. E.g. if you have AS scripts in components. Each script is isolated, so you cannot just have "global variable" used in multiple scripts. So, you use global context to store such variables.

-------------------------

najak3d | 2021-07-19 19:47:34 UTC | #5

Thank you!   That makes sense.

-------------------------

