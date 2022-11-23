cirosantilli | 2017-12-22 23:01:02 UTC | #1

I want the world to evolve deterministically, independent of how long it takes to render the frame.

Or in other words, in 2D, I want the step that is passed to `b2World::Step` to be always the same.

It is fine if that leads to a non responsive UI, and it is also fine if I have more than one step per frame.

I've put a cout next to  `b2World::Step` of a simple program, and the step value is not always the same.

-------------------------

1vanK | 2017-12-22 20:16:06 UTC | #2

urho2D does not support fixed yet, but you can setMaxFps(60)

-------------------------

cirosantilli | 2017-12-22 23:01:36 UTC | #3

Thanks. Why `setMaxFps(60)` could help?

-------------------------

Eugene | 2017-12-22 23:24:44 UTC | #4

[quote="cirosantilli, post:1, topic:3872"]
I want the world to evolve deterministically, independent of how long it takes to render the frame.
[/quote]

Neither Bullet nor Box2D are deterministic. Do you use physics?

-------------------------

1vanK | 2017-12-23 03:06:29 UTC | #5

> Thanks. Why setMaxFps(60) could help?

timeStep wiil be stable (of course, not on a weak computer)

> Neither Bullet nor Box2D are deterministic. Do you use physics?

bullet use fixedStep

-------------------------

Eugene | 2017-12-23 11:11:57 UTC | #6

[quote="1vanK, post:5, topic:3872"]
bullet use fixedStep
[/quote]

It doesn't make Bullet determenistic, unfortunatelly.

-------------------------

cirosantilli | 2017-12-23 12:10:59 UTC | #7

Hmmm, Box2D is deterministic given a single binary, which is at least enough for debugging properly: https://github.com/erincatto/Box2D/wiki/FAQ which is already good enough for me.

-------------------------

