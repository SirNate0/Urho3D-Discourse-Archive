sabotage3d | 2017-01-02 01:06:34 UTC | #1

Is it currently possible to cache particles and reuse them later or record them from a third party software ?

-------------------------

sabotage3d | 2017-01-02 01:06:35 UTC | #2

I am working with this library at the moment: [github.com/wdas/partio/](https://github.com/wdas/partio/) 
I am trying to set positions, color, age and other custom attributes inside Urho3d from a binary particle file. Is there currently any API that would allow me to set these particle arrays ?

-------------------------

cadaver | 2017-01-02 01:06:35 UTC | #3

The ParticleEmitter class is tied to the ParticleEffect resource, so if ParticleEffect's features are enough you could create a ParticleEffect at runtime from your third-party data.

If this is not flexible enough, your next options are making tweaks to ParticleEmitter so that it allows better public access and/or tweaks to the particles (please submit a pull request in this case if you believe it would benefit others), and finally creating your own particle emitter drawable using BillboardSet as a base class.

-------------------------

sabotage3d | 2017-01-02 01:06:35 UTC | #4

Thanks cadaver. Is it a bad idea if I make a new node type called ParticleCache or I have to modify the existing ParticleEmitter classes ?

-------------------------

cadaver | 2017-01-02 01:06:35 UTC | #5

ParticleCache sounds more like a subsystem instead of a component (Node itself shouldn't ever be subclassed, as that won't serialize properly.) If it's a central location which many emitters access, then it sounds like a subsystem. If it's something that you'll add to every node that emits particles, then it's just a plain component.

There are actually two kinds of subsystems in Urho: sceneless (like Graphics, ResourceCache) and "subsystem components" (like Octree, PhysicsWorld) that are added to the root of the scene.

About whether you need to modify ParticleEmitter, I have no idea. If it can't do what you need it to do (for example public access to the actual live particles), then yes.

-------------------------

sabotage3d | 2017-01-02 01:06:35 UTC | #6

I am thinking ParticleCache should be seperate from ParticleEmitter. And it should act like container similar to the AnimatedModel is would jut accept particle file. Would it create problems ?
Also I am thinking of creating methods like setPosition, setColor, setRotation and so on, where these are per particle arrays.

-------------------------

