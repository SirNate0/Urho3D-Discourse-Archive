mrchrissross | 2018-10-27 13:36:51 UTC | #1

Hi, 

I'm trying to get my particles look as if a flame is coming out of the exhaust of my spaceship. It looks fine when viewed directly behind it: https://imgur.com/WAyz3qR

However from the side it looks like this: https://imgur.com/LiCgHS7

Any help would be much appreciated :slight_smile:

-------------------------

jmiller | 2018-10-27 15:29:01 UTC | #2

Hi!

There are a few ways to better fill the volume:

Add more particles (I have used a lot; they are efficient); tune. Perhaps the emit number could be tweaked for velocity.
Particles can also have long + narrow texture, can be oriented, can be very short lifespan..

For examples, you may have seen 'fire' etc.
  https://github.com/urho3d/Urho3D/tree/master/bin/Data/Particle


RibbonTrail: not particles, but great for making a smooth efficient trail. We have used these together with particles before.
(Samples/44_RibbonTrailDemo)

-------------------------

mrchrissross | 2018-10-27 15:53:54 UTC | #3

    fireEmitter = mSpaceship.engineNode->CreateComponent<ParticleEmitter>();
	fireEmitter->SetEffect(cache->GetResource<ParticleEffect>("Particle/torch_fire.xml"));
	fireEffect = fireEmitter->GetEffect();
	fireEffect->SetMinEmissionRate(200);
	fireEffect->SetMaxEmissionRate(800);
	fireEffect->SetMinTimeToLive(0.2);
	fireEffect->SetMaxTimeToLive(0.4);

	smokeEmitter = mSpaceship.engineNode->CreateComponent<ParticleEmitter>();
	smokeEmitter->SetEffect(cache->GetResource<ParticleEffect>("Particle/torch_smoke.xml"));
	smokeEffect = smokeEmitter->GetEffect();
	smokeEffect->SetMinEmissionRate(50);
	smokeEffect->SetMaxEmissionRate(100);

This is what I have currently ^^

I got it from this link: [http://urho3d.wikia.com/wiki/Particle_Effects](http://) 

I tried the ribbon trail and as the craft is close to the screen it looks very 2D.

Thanks,

-------------------------

Modanung | 2018-10-27 17:26:45 UTC | #4

I believe part of the problem may be that the positions where the particles are spawned is not interpolated. Maybe scaling the emitter size with the object's velocity would fill the gap nicely?

-------------------------

mrchrissross | 2018-10-27 17:37:59 UTC | #5

Sorry for being a newb but how do I do that?

-------------------------

Modanung | 2018-10-27 18:00:21 UTC | #6

`fireEffect->SetEmitterSize(Vector3(0.0f, 0.0f, node_->WorldToLocal(rigidBody_->GetLinearVelocity()).z_`
...if I'm not mistaken.

-------------------------

mrchrissross | 2018-10-27 20:13:47 UTC | #7

Thats absolutely perfect, thank you so much, looks amazing :slight_smile: is it alright to ask another quick question while on here or should I open a new topic, It's just to do with collision in zero gravity. When my spacecraft collides with a box it sets the node or rigidbody funny, to get around this i have to quickly set mass to zero then back to one.

-------------------------

Modanung | 2018-10-27 21:19:38 UTC | #8

I'm not sure what could be causing that.

-------------------------

Sinoid | 2018-10-28 01:05:26 UTC | #9

It should really be the responsibility of the `ParticleEmitter` to interpolate new particle starting positions. I'll give it a whirl, should only be a handful of changes.

**Edit:** [this gist should do it](https://gist.github.com/JSandusky/73b4db349983d184b90e4dd96b74d30f), changes are in `ParticleEmitter::Update` `ParticleEmitter::EmitNewParticle` and the ctor/header (for the cached positions, and sig change to EmitNewParticle). Couldn't test, temporarily one-handed and can't work a mouse worth a damn with my left - but it doesn't break anything in NinjaSnowWar.

-------------------------

jmiller | 2018-10-29 17:47:58 UTC | #10

Thanks for asking; with more detail can venture a better guess; I am assuming you mean the spacecraft node/rb are set funny.

Is it using TriangleMesh CollisionShape?
Per https://urho3d.github.io/documentation/HEAD/_physics.html
> Note that the triangle mesh collision shape is not supported for moving objects; it will not collide properly due to limitations in the Bullet library. In this case the convex hull or GImpact triangle mesh shape can be used instead.

-------------------------

mrchrissross | 2018-10-30 21:44:02 UTC | #11

Gravity is set to zero and when I hit an object with my spacecraft. The craft will spin. I can still move but the spacecraft will spin whilst moving in the direction i wish to go to. 

Currently, I'm using a box collider: 

    collider->SetBox(Vector3::ONE);

And thank you Sinoid, your help is much appreciated and works like a charm :slight_smile:

-------------------------

jmiller | 2018-11-03 13:55:55 UTC | #12

Ah - good info. Apart from mass, you could tune RigidBody physics attributes -- I think **Angular Damping** in particular?

Can find these in physics docs linked, [class reference](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_rigid_body.html), [ScriptAPI.dox](https://github.com/urho3d/Urho3D/blob/master/Docs/ScriptAPI.dox) ..

-------------------------

mrchrissross | 2018-10-30 21:55:24 UTC | #13

Alright thank you very much for this, I'll be sure to check it :slight_smile:  if you have the time would you be able to check out my other question available at https://discourse.urho3d.io/t/quaternion-rotation/4628.

I'm absolutely baffled by it :frowning:

-------------------------

