v0van1981 | 2017-01-02 01:02:46 UTC | #1

like

[img]https://seagullcity.files.wordpress.com/2013/10/20131013213349.png[/img]

any ideas?

-------------------------

codingmonkey | 2017-01-02 01:02:48 UTC | #2

It seems that your particles use physics collisions, and as far as I know the Urho's particles not can this yet.
But you can always write your own particle system based on physics )

And if do this fx without physics, that the psystem on image seems to me there are have two emitter with textured of the thin spark. 
1. psys has sphere direction for patricles
2. psys has left or right orient for particles
3  you may add third psys with less count of particles for lower part and set for this psys little angle around 15-30 degrees.

-------------------------

OvermindDL1 | 2017-01-02 01:02:51 UTC | #3

You would not necessarily need a physics engine to do that reflection, an affector on the particles could do that reflection at a plane for example to fake it quickly.

-------------------------

v0van1981 | 2017-01-02 01:02:51 UTC | #4

The problem lies elsewhere. How to rotate sprites particles to movement direction? I do not find this parameter.

-------------------------

cadaver | 2017-01-02 01:02:52 UTC | #5

I'm sure there are a lot of missing particle system features, simply because we haven't been able to think about all possible requirements or parameters. Most preferred course of action is to just add the required features to ParticleEmitter / ParticleEffect classes and submit a pull request.

-------------------------

