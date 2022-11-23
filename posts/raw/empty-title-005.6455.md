vram32 | 2020-12-11 13:13:33 UTC | #1

Empty content.......

-------------------------

vmost | 2020-10-23 14:19:47 UTC | #2

I did a test with a simple app and managed a couple million separate events per second. There shouldn't be a noticeable impact from multiple subscriptions vs a handler hub.

-------------------------

Eugene | 2020-10-23 14:21:47 UTC | #3

Event handlers are relatively cheap, so it won't be a problem unless you have _a lot_ of event handlers.

As a side note, I don't recommend to rely on the order of event evaluation.
So you may want to use single event handler if you want to explicitly order execution.

-------------------------

vmost | 2020-10-23 14:29:10 UTC | #4

In my tests the bulk of CPU time for sending an event is in allocating members for the variable `processed` in `SendEvent()`. However, only one member is allocated for each separate object (event receiver), even if that object has multiple handlers, so my educated guess is calling multiple handlers for a single receiver is relatively cheap compared to the base cost of handling the event.

-------------------------

weitjong | 2020-12-12 05:49:24 UTC | #6



-------------------------

