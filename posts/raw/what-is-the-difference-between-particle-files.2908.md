Commandor | 2017-03-16 19:47:26 UTC | #1

What is the difference between in particle files with tags:
`<particleeffect> and <particleemitter>` ???

-------------------------

1vanK | 2017-03-16 20:45:53 UTC | #2

particleeffect is part of particleemitter component (settings)

-------------------------

Commandor | 2017-03-16 20:51:28 UTC | #3

I know about it. But what is the difference between these tags `<particleeffect> and <particleemitter>` in the files xml?

For example:

`<?xml version="1.0"?>
**<particleeffect>**
    <material name="Materials/Particle.xml" />
    <numparticles value="1000" />
    <updateinvisible enable="true" />
    <relative enable="false" />
    <scaled enable="true" />
    <sorted enable="false" />
    <animlodbias value="0" />
    <emittertype value="box" />
    <emittersize value="0.05 0.05 0.05" />
    <direction min="-0.1 0.02 -0.1" max="0.1 0.02 0.1" />
    <constantforce value="0 2 0" />
    <dampingforce value="1" />
    <activetime value="0" />
    <inactivetime value="0" />
    <emissionrate min="40" max="45" />
    <particlesize min="0.1 0.1" max="0.3 0.3" />
    <timetolive min="2" max="2" />
    <velocity min="0" max="0.5" />
    <rotation min="0" max="0" />
    <rotationspeed min="0" max="0" />
    <sizedelta add="0" mul="0.8" />
    <colorfade color="1 1 0.45 0" time="0" />
    <colorfade color="1 0.63 0.45 1" time="0.5" />
    <colorfade color="0.5 0.32 0.22 0.5" time="1.5" />
    <colorfade color="0 0 0 0" time="2" />
</particleeffect>`

and

`<?xml version="1.0"?>
**<particleemitter>**
    <material name="Materials/Smoke.xml" />
    <numparticles value="1000" />
    <updateinvisible enable="true" />
    <relative enable="false" />
    <activetime value="0" />
    <animlodbias value="0" />
    <inactivetime value="0" />
    <emissionrate min="20" max="25" />
    <sorted enable="false" />
    <rotationspeed min="-30" max="30" />
    <emittertype value="box" />
    <emittersize value="0.05 0.05 0.05" />
    <direction min="-0.1 0.02 -0.1" max="0.1 0.02 0.1" />
    <dampingforce value="1" />
    <velocity min="0" max="0.5" />
    <particlesize min="0.1 0.1" max="0.2 0.2" />
    <sizedelta add="0" mul="1.5" />
    <timetolive value="4" />
    <constantforce value="0 2 0" />
    <colorfade color="0.2 0.2 0.2 0" time="0.0" />
    <colorfade color="0.2 0.2 0.2 0" time="1.5" />
    <colorfade color="0.2 0.2 0.2 0.1" time="2.0" />
    <colorfade color="0.6 0.6 0.6 0" time="4.0" />
</particleemitter>`

-------------------------

1vanK | 2017-03-16 20:59:32 UTC | #4

different way for loading, also particleemitter can contain info about all particles in some time (state of emitter)

-------------------------

1vanK | 2017-03-16 21:06:45 UTC | #5

Ah, I see, in Ninja example "particleemitter" loaded by SetEffect(). I think it is just mistake

-------------------------

Commandor | 2017-03-16 21:11:25 UTC | #6

But both options work without SetEffect().
It would be more correct for a ParticleEmitter to contain only parameters relating only to it.

-------------------------

