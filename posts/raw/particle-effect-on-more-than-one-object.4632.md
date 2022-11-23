mrchrissross | 2018-11-01 10:32:03 UTC | #1

Hi,

I've tried to add a particle effect to another object other than my spaceship however they seem to share a connection of some sort as when the particle effect for the other object starts, both with start. 

Spaceship Particle:

    fireEmitter = mSpaceship.engineNode->CreateComponent<ParticleEmitter>();
	fireEmitter->SetEffect(cache->GetResource<ParticleEffect>("Particle/torch_fire.xml"));
	fireEffect = fireEmitter->GetEffect();
	fireEffect->SetMinTimeToLive(0.2);
	fireEffect->SetMaxTimeToLive(0.4);
	fireEffect->SetEmitterSize(Vector3(0.0f, 0.0f, mSpaceship.engineNode->WorldToLocal(mSpaceship.rb->GetLinearVelocity()).z_));

	smokeEmitter = mSpaceship.engineNode->CreateComponent<ParticleEmitter>();
	smokeEmitter->SetEffect(cache->GetResource<ParticleEffect>("Particle/torch_smoke.xml"));
	smokeEffect = smokeEmitter->GetEffect();
	smokeEffect->SetMinEmissionRate(50);
	smokeEffect->SetMaxEmissionRate(100);

Missile Particle:

    missileFireEmitter = node->CreateComponent<ParticleEmitter>();
	missileFireEmitter->SetEffect(cache->GetResource<ParticleEffect>("Particle/torch_fire.xml"));
	missileFireEffect = missileFireEmitter->GetEffect();
	missileFireEffect->SetMinTimeToLive(0.2);
	missileFireEffect->SetMaxTimeToLive(0.4);
	missileFireEffect->SetEmitterSize(Vector3(0.0f, 0.0f, node->WorldToLocal(rb->GetLinearVelocity()).z_));

	missileSmokeEmitter = node->CreateComponent<ParticleEmitter>();
	missileSmokeEmitter->SetEffect(cache->GetResource<ParticleEffect>("Particle/torch_smoke.xml"));
	missileSmokeEffect = missileSmokeEmitter->GetEffect();
	missileSmokeEffect->SetMinEmissionRate(50);
	missileSmokeEffect->SetMaxEmissionRate(100);

Thanks,

-------------------------

mrchrissross | 2018-11-01 10:45:51 UTC | #2

It seems that by changing the

    missileFireEmitter->SetEffect(cache->GetResource<ParticleEffect>("Particle/torch_fire.xml"));
    missileSmokeEmitter->SetEffect(cache->GetResource<ParticleEffect>("Particle/torch_smoke.xml"));

to
  
    missileFireEmitter->SetEffect(cache->GetResource<ParticleEffect>("Particle/Fire.xml"));
    missileSmokeEmitter->SetEffect(cache->GetResource<ParticleEffect>("Particle/Smoke.xml"));

Has separated them, but why? and does this mean I can no longer use torch_fire.xml on any other particle effects?

-------------------------

Modanung | 2018-11-01 11:18:06 UTC | #3

`Resource`s should be cloned if you want to create variations, otherwise they will be reused since your are moving pointers around. Simply add `->Clone()` before the last closing bracket to separate the effect from its original.

-------------------------

mrchrissross | 2018-11-01 11:17:43 UTC | #5

Thank you mate, this solved the problem :slight_smile:

-------------------------

