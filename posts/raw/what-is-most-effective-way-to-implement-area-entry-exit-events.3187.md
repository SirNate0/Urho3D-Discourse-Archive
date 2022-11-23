slapin | 2017-06-01 22:13:39 UTC | #1

Hi, all!

I need to implement areas where players/npcs can enter and some event happens/variable set.
on area exit some other event happens.

For example, when player character stays in area near door,  the message is displayed "Press E to open"
and when he presses E that door opens. If he is not in this area, there's no message and reaction to E is
different.
Also can be used as quest spots, better car enter/exit sequences, almost everything.

How would you implement this knowing there will be thousands in the area?
I know it should be possible to do this using "trigger" RigidBodies, but something tells me it will kill
frame rate to unmanageable levels.
Also as compromize these spots can be spawned around player, but how to trigger spawn?
I can record each spot coordinates in K-D tree and spawn ones within 10 unit radius and remove distant ones,
but how to implement the situation when distant NPC should trigger such spot? Looks like entire map of these should
be provided somehow...

-------------------------

ricab | 2017-06-01 23:00:35 UTC | #2

Most of the rigid bodies will be filtered in the broad phase, so the impact on performance might not be all that big. But if you are concerned you could mock up a scene and measure time consumption. If you find there is a very large impact, I suppose you could subdivide your world and load different scenes as needed.

-------------------------

slapin | 2017-06-01 23:49:15 UTC | #3

well, my world is going to be procedurally generated, so I will need to build influence maps and partitioning,
so I will auto-spawn spots as needed, thanks.

-------------------------

