Pihozamo | 2017-08-21 02:46:41 UTC | #1

The class SplinePath uses Nodes for waypoints, and looking at it, seems like it could just use Vector3 for waypoints, is there any reason as to why it uses Nodes instead of Vector3s? I ask because I was thinking about committing an update to it.

-------------------------

slapin | 2017-08-21 02:57:25 UTC | #2

I think the reason is you can set this up graphically in the Editor.

-------------------------

Eugene | 2017-08-21 04:09:43 UTC | #3

[quote="Pihozamo, post:1, topic:3470"]
I ask because I was thinking about committing an update to it.
[/quote]

So, you will have to implement generic gizmo for Editor too.

-------------------------

slapin | 2017-08-21 04:28:59 UTC | #4

If you don't need graphical setting-up you can just use generic Spline object.

-------------------------

1vanK | 2017-08-21 06:05:32 UTC | #5

you can attach objects to nodes

-------------------------

