urnenfeld | 2020-12-25 12:03:26 UTC | #1


While some Effect paramenters look to feed the emiter by the [pointer kept](https://github.com/urho3d/Urho3D/blob/4048798fc53929d5d8e59bfe9917092e401b049e/Source/Urho3D/Graphics/ParticleEmitter.cpp#L460) to the [effect](https://github.com/urho3d/Urho3D/blob/4048798fc53929d5d8e59bfe9917092e401b049e/Source/Urho3D/Graphics/ParticleEffect.cpp#L790) and would apply instantly... 

This is not taking effect for me:

    particleFlareEffect_->SetMinDirection (Vector3::DOWN);
    particleFlareEffect_->SetMaxDirection (Vector3::DOWN * 20);
    particleFlareEmitter_->ApplyEffect();

But some other parameters are (*Numparticles*) [ApplyEffect](https://github.com/urho3d/Urho3D/blob/4048798fc53929d5d8e59bfe9917092e401b049e/Source/Urho3D/Graphics/ParticleEmitter.cpp#L344)...

        particleFlareEffect_->SetNumParticles(100);
        particleFlareEmitter_->ApplyEffect();

Additionally if you change some effect parameters programatically, and you [set it again](https://github.com/urho3d/Urho3D/blob/4048798fc53929d5d8e59bfe9917092e401b049e/Source/Urho3D/Graphics/ParticleEmitter.cpp#L263)(SetEffect), The function silently [would return](https://github.com/urho3d/Urho3D/blob/4048798fc53929d5d8e59bfe9917092e401b049e/Source/Urho3D/Graphics/ParticleEmitter.cpp#L265) without affecting the particle (as the pointer of the object would be the same).

I have been struggling changing the direction of an emission. At the end just changing the numparticles (from the **Emiter**) worked for me, but tried many other changes from the **Effect** unsuccessfully. 

Also I see parameters under a xml `<particleemitter>` tag and others in a `<particleeffect>`

What is the procedure of changing an ongoing ParticleEmmiter Effect?

-------------------------

