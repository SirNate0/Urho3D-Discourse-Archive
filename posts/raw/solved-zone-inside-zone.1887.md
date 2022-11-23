Shylon | 2017-01-02 01:11:07 UTC | #1

It seems Zone inside Zone not get along with each-other well, for example one zone has a blue ambient and another small red zone inside blue zone. in editor when moving inside those zones only you see 1 of them.

-------------------------

cadaver | 2017-01-02 01:11:07 UTC | #2

The important thing to notice is that when rendered, each drawable will pick one zone, so if you have e.g. a large plane mesh you won't see multiple zones' effect on it. Use the zones' priority value to control which overlapping zone has higher priority.

-------------------------

1vanK | 2017-01-02 01:11:07 UTC | #3

You can create an intermediate zone and use "Use gradient" option

-------------------------

Shylon | 2017-01-02 01:11:08 UTC | #4

Thanks for all answers, Priority did work, using gradient is good options too beside priority.
:slight_smile:

-------------------------

