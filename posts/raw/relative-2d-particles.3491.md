qwertysam | 2017-08-25 15:55:42 UTC | #1

Hello,

I'd like to have a 2D particle emitter that is relative to a node of my choosing and not proprietarily the scene node. (For example, a fire particle emitter that is attatched to the player node at the engine of a space ship).

Going through the 3D documentation, I have found that both [ParticleEffect](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_particle_effect.html) and [ParticleEmitter](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_particle_emitter.html) appear to support this through the function **SetRelative(true|false)**. 

When looking through the documentation for their 2D counterparts, neither [ParticleEffect2D](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_particle_effect2_d.html) nor [ParticleEmitter2D](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_particle_emitter2_d.html) seem to have implementations of this. 

ParticleEmitter2D seems to be my best bet on achieving this, as the ParticleEffect2D yields no relation to anything node or scene related (unlike ParticleEffect).

Thank you for reading, any guidance is appreciated!

-------------------------

ricab | 2017-08-27 13:48:10 UTC | #2

Have a look at the Urho2DParticle sample. You just need to create the particle emitter through `Node::CreateComponent` on the node of your choosing. Here is an extract from the sample:

```
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    ParticleEffect2D* particleEffect = cache->GetResource<ParticleEffect2D>("Urho2D/sun.pex");
    if (!particleEffect)
        return;

    particleNode_ = scene_->CreateChild("ParticleEmitter2D");
    ParticleEmitter2D* particleEmitter = particleNode_->CreateComponent<ParticleEmitter2D>();
    particleEmitter->SetEffect(particleEffect);
```

-------------------------

qwertysam | 2017-08-27 19:36:57 UTC | #3

I apologize, I realize now that my question might not be as clear as I thought.

As an example, here is a fire effect that I made
![image|384x471](upload://tQBbxLh3pxWxCZQDRS6rw7y9z6g.png)

It looks great, except for when my player is travelling at higher velocities

![image|348x454](upload://iO4yt6HjdIXkwgi2qqkcJ8hl8rd.png)

The ParticleEmitter2D itself follows the player node accurately, and the reason for the particles appearing like this is due to them being created at regular intervals, allowing the ParticleEmitter2D to travel away from the previously emitted particle, therefore creating a broken stream of particles.

A simple suggestion would be to increase the emission frequency of the particles. I have tried that, and the results do not differ because the particle system updates at regular intervals, only creating new particles ones it "trips" past the desired interval. **The underlying issue here** is that when a particle is created, it does not properly maintain the current velocity of the ParticleEmitter2D's node.

My ship has a velocity of (0, 50000), and the particles being emitted have a velocity of (0, -70), when really they should have a velocity of (0, 50000 - 70).

*As another example,* if I were to create a ParticleEmitter2D for the smoke that emits from the end of a gun node, and were to create a playable area inside of a moving spaceship node where the player could shoot bullets inside the spaceship, the smoke particles would have the same broken stream effect. The velocity of the particles should be relative to the ship, but are relative to the world by default.

And **that** is what I am tried to overcome. I would like velocities of the fire particles to be relative to the spaceship.

Thank you for your suggestion!

-------------------------

kostik1337 | 2017-08-28 09:08:44 UTC | #4

Unfortunately, this has not been implemented yet for ParticleEmitter2D. I have plans to implement it someday, but it's not high priority for me now.
As a workaround, I can suggest you to set ParticleEffect2D's angle and speed accordingly to the speed of the spaceship, e.g. if you are moving at the speed (0, 50000), then set emitter's speed at a little less than 50000 and angle _upwards_ your ship, so particles positions would be not that divergent.

-------------------------

