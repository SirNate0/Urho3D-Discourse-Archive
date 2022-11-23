rasteron | 2017-01-02 01:07:15 UTC | #1

I was hoping there could be some behavior or steering component for AI, aside from Detour/Crowd navigation generating navmeshes..

[b]
seek, flee, pursue, evade, arrive, wander, follow, obstacle and collision avoidance.
[/b]

[b]Behavior Tree Starter Kit (ZLIB)[/b]
[github.com/aigamedev/btsk](https://github.com/aigamedev/btsk)

[b]OpenSteer (MIT)[/b] 2D/3D

[img]https://raw.githubusercontent.com/meshula/OpenSteer/master/doc/images/typical_SteerTest.png[/img]

[sourceforge.net/projects/opensteer/](http://sourceforge.net/projects/opensteer/)
[github.com/meshula/OpenSteer](https://github.com/meshula/OpenSteer)


[b]MicroPather (ZLIB)[/b] 2D/3D

[img]http://www.grinninglizard.com/MicroPather/screen0.jpg[/img]
[img]http://www.grinninglizard.com/MicroPather/screen1.jpg[/img]

[grinninglizard.com/MicroPather/index.htm](http://www.grinninglizard.com/MicroPather/index.htm)
[sourceforge.net/projects/micropather/](http://sourceforge.net/projects/micropather/)

-------------------------

Lumak | 2017-01-02 01:07:15 UTC | #2

Steering behavior has always been an interesting topic. I remember seeing OpenSteer containing similar behavior implementation for racing, opposed to pedestrians, a number of years ago (could be a different library all together, can't remember). I might look into that feature later on if I decide to make a racing game.

-------------------------

rasteron | 2017-01-02 01:07:17 UTC | #3

[b]@Lumak[/b]

Me too, got interested when I saw other demos and frameworks. Here's one from Panda3D built-in AI (Panda AI)

[video]https://www.youtube.com/watch?v=bYcbQogUx5o[/video]

OpenSteer would be a great choice..

[b]@Sinoid[/b]
Thanks for sharing, that is a good start.

-------------------------

gabdab | 2017-01-02 01:07:18 UTC | #4

It is quite easy to use opensteer .
You just overcome the 2D limitation by using rays .
It is based on a sort of behaviour tree ..
Even though I have problems with rectangle obstacles , my animated model disappears
 ssometimes .

-------------------------

