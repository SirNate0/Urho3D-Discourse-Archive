sabotage3d | 2017-01-02 01:15:42 UTC | #1

Hi,
I am getting some weird behaviour with range-based for loop in C++11 with Urho3D containers. It looks like undefined behaviour as sometimes I am getting a crash and sometimes I am not. I hope I am not doing it completely wrong. As far as I remember this should work with STL containers and smart pointers. 
This is a simple example:

[code]SharedPtr<ParticleEmitter> particleEmitter1_;
SharedPtr<ParticleEmitter> particleEmitter2_;

particleEmitter1_ = particleNode_->CreateComponent<ParticleEmitter>();
particleEmitter1_->SetEffect(particleEffect1_);

particleEmitter2_ = particleNode_->CreateComponent<ParticleEmitter>();
particleEmitter2_->SetEffect(particleEffect2_);

Vector<SharedPtr<ParticleEmitter>> particleEmitters_;
particleEmitters_.Push(particleEmitter1_);
particleEmitters_.Push(particleEmitter2_);

for (auto particleEmitter : particleEmitters_)
{
	particleEmitter->SetEmit(false);
}
[/code]

-------------------------

cadaver | 2017-01-02 01:15:42 UTC | #2

Need to investigate. I can't think of any existing/known reason why this should produce crashes.

-------------------------

cadaver | 2017-01-02 01:15:42 UTC | #3

In a quick test on VS2015, I didn't see anything bad happening. What compiler are you on?

-------------------------

S.L.C | 2017-01-02 01:15:42 UTC | #4

Have you tried different variants like reference, const reference, maybe even dropping the auto:
[code]for (auto & particleEmitter : particleEmitters_)[/code]
[code]for (const auto & particleEmitter : particleEmitters_)[/code]
[code]for (SharedPtr<ParticleEmitter> & particleEmitter : particleEmitters_)[/code]
[code]for (const SharedPtr<ParticleEmitter> & particleEmitter : particleEmitters_)[/code]

Maybe the compiler sees you're fetching a copy with each iteration and tries to optimize some things.

In the auto version, try a "typeid(particleEmitter).name()" to see if some implicit conversion doesn't happen there. Can't be paranoid enough :smiley:

-------------------------

sabotage3d | 2017-01-02 01:15:42 UTC | #5

Sorry for the delay I am on OSX 10.10.5 with Clang version 4.0.0. I couldn't get it to crash from yesterday after I updated Qt Creator. If it happens again I will try to narrow the possibilities. I am on Urho3D 1.6 on a merge from these commits 1017e82 e3b9e87.

-------------------------

