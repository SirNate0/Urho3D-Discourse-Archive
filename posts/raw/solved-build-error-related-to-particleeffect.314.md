AGreatFish | 2017-01-02 00:59:34 UTC | #1

Since I pulled the latest changes from git I get the following errors when trying to compile Urho3DPlayer:

[code]/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::GetRandomTimeToLive() const'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetDampingForce(float)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetEmitterSize(Urho3D::Vector3 const&)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::ParticleEffect(Urho3D::Context*)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetNumParticles(unsigned int)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetRelative(bool)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetMinDirection(Urho3D::Vector3 const&)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetMaxRotation(float)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetMinVelocity(float)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetMinEmissionRate(float)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::GetRandomDirection() const'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetMinRotationSpeed(float)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `typeinfo for Urho3D::ParticleEffect'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetMaxRotationSpeed(float)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetTextureFrame(unsigned int, Urho3D::TextureFrame const&)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetUpdateInvisible(bool)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetSorted(bool)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetMaxDirection(Urho3D::Vector3 const&)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetColorFrame(unsigned int, Urho3D::ColorFrame const&)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetScaled(bool)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::GetRandomSize() const'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetInactiveTime(float)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::GetRandomVelocity() const'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetActiveTime(float)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetSizeAdd(float)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetMaterial(Urho3D::Material*)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::GetColorFrame(unsigned int) const'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetMinRotation(float)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetAnimationLodBias(float)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetMinParticleSize(Urho3D::Vector2 const&)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetEmitterType(Urho3D::EmitterType)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::RegisterObject(Urho3D::Context*)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetMinTimeToLive(float)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetMaxVelocity(float)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetMaxEmissionRate(float)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetMaxParticleSize(Urho3D::Vector2 const&)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetConstantForce(Urho3D::Vector3 const&)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::GetTextureFrame(unsigned int) const'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetSizeMul(float)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::SetMaxTimeToLive(float)'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::GetRandomRotation() const'
/Urho3D_Git/Lib/libUrho3D.so: undefined reference to `Urho3D::ParticleEffect::GetRandomRotationSpeed() const'[/code]

I recently upgraded some of my dev environment, so that might be the cause.

Or is it a bug that was introduced by the recent changes to the particle systems ?

I'm on Linux 64 bit.

-------------------------

friesencr | 2017-01-02 00:59:34 UTC | #2

It works on my x64 linux box.  That is a new class that was added.  I havn't figured out when make thinks it should recompile or when cmake's update macros trigger.  Try rerunning ./cmake_gcc and then rerun make.  If that doesn't work i delete my build folder.

-------------------------

AGreatFish | 2017-01-02 00:59:34 UTC | #3

Ok, now it works for me, as well   :blush: 

I rebuilt my .cbp file after after changing my build environment but apparently I forgot rebuilding it after pulling the latest changes.

-------------------------

