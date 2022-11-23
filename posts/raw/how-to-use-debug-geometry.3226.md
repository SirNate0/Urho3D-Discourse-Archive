slapin | 2017-06-08 16:27:30 UTC | #1

I probably miss something obvious, but anyway...

I want to display axes position at runtime for a set of bone nodes. How could I do this?
Also, I want to display quaternion rotation axes, any ideas?

I try to AddNode to DebugRendered but I don't see anything displayed on screen.
Also how to display quaternion/rotation si there some widget? I want to display local coordinate system
represented by quaternion (no node in this case).

It looks I miss something findamental about DebugRenderer...

-------------------------

Eugene | 2017-06-08 18:06:54 UTC | #2

[quote="slapin, post:1, topic:3226"]
It looks I miss something findamental about DebugRenderer.
[/quote]

Probably you miss that Debug Renderer is 'stateless', so your AddNode is not kept among frames

-------------------------

slapin | 2017-06-08 18:13:31 UTC | #3

is there some sequence required for proper display of debug geometry?

-------------------------

Eugene | 2017-06-08 18:33:12 UTC | #4

You shall add all primitives you want to draw not later that E_BEGINVIEWRENDER event come.

-------------------------

slapin | 2017-06-08 18:35:01 UTC | #5

Should I add them in special event handler or I can do that anywhere on the path?

-------------------------

