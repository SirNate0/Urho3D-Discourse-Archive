JTippetts1 | 2021-10-13 23:16:01 UTC | #1

Is there a way to fast-forward a particle system? I have a project with a number of particle systems emulating material flow through various pipes and ducts, and I'd like those systems to be well in-progress when the app starts, rather than seeing them start and flow. It seems like you could use ParticleEmitter::Update(FrameInfo), but that method seems to be internal and is not exposed to script. What is the best way to do this that is accessible via Lua?

-------------------------

JSandusky | 2021-10-16 04:11:45 UTC | #2

Add a warm-starting bool to either the effect or the emitter? During update check the ```viewFrameNumber_``` to see if the gap is too large for a warm-start system and if so loop the update details until a particle is removed (that should be good enough, once a particle is removed the system should be *mature*).

Edit: the tricky part is going to be the stuff with the period timers. If it becomes a problem you don't want the fake time per loop to be too small (many loops) or too large (clumping), so that may be yet another tuning or added parameter point.

-------------------------

Modanung | 2021-10-17 16:02:35 UTC | #3

What about a time ma`Scene`?

-------------------------

JSandusky | 2021-10-17 23:37:56 UTC | #4

If you mean the multiplier/scale of time that will lead to clumping and mess with other stuff. Unless restoring particle system state from some saved data you have to loop through artificial timesteps to reach a hot state or it'll just emit all particles but never advance them. (I just settled on `1.0 / GetSubsystem<Engine>()->GetMinFPS(); // 1/10 if minfps unchanged` for the step)

The hassle is just that you basically have to plug the required functionality into the particle-emitter, otherwise you end up having to add a bunch of extra cruft such as events for when something comes into view for drawing so you can hack in loading some saved particle-state from somewhere. Warm-starting is just much easier to do then adding another set of serialized particle data for first-time-seen and then having to plug in the commensurate GUI/functions to grab the data for it, etc and also less consequential than plugging in more events (particularly for such a common thing as ... "*hey dude! I just came into view!*).

-------------------------

JSandusky | 2021-10-18 00:14:18 UTC | #5

I dealt with it by adding a `lastViewFrameNumber_` (the comment on viewFrameNumber_ is wrong, it's not the last one, it's always the current one by the time you get to update).
```
    bool doWarmStart = false;
    if (warmStart_ && lastViewFrameNumber_ < frame.frameNumber_ - 1 && !CheckActiveParticles())
    {
        doWarmStart = true;
        const float maxStep = GetSubsystem<Engine>()->GetMinFps(); //default is 10, so 1/10 below in most cases.
        lastTimeStep_ = Max(lastTimeStep_, 1.0f / maxStep);
    }
```

Then wrapping the update into a `do { ... } while(emitting_ && doWarmStart);`, whenever a billboard is set to disabled doWarmStart is then set to false (terminating the loop).

Works dandy on the stock effects I've tried (fire, smoke, etc).

Downside over update invisible is that it pops in due to absence of an appropriate bounding box.

-------------------------

SirNate0 | 2021-12-08 14:22:24 UTC | #6

I recently came across the same problem and found a way to do it without changing the engine particle code, though with the caveat that I know exactly when and which particle systems I'm trying to fast-forward (as I create them in the code right before this). Though this code just runs it for a second in 0.1 second intervals, not checking for a particle disappearing or anything.
```
bool updInv = effect_->GetUpdateInvisible();
effect_->SetUpdateInvisible(true);
for (unsigned i = 0; i < 10; ++i)
{
	constexpr float TS = 0.1f;
	auto& map = target->GetContext()->GetEventDataMap();
	using namespace ScenePostUpdate;
	map[P_SCENE] = target->GetScene();
	map[P_TIMESTEP] = TS;
	// Need this to get it to "needUpdate_" together with the UpdateInvisible.
	emitter->OnEvent(target->GetScene(),E_SCENEPOSTUPDATE,map);
	FrameInfo frame{
		i, TS, {640,480},nullptr
	};
	// And this to get it to actually animate the particles.
	emitter->Update(frame);
}
effect_->SetUpdateInvisible(updInv);
```

-------------------------

Modanung | 2021-12-08 19:14:14 UTC | #7

How about something like this?
```
void ParticleAccelator(ParticleEmitter* emitter, float time)
{
    Node* node{ emitter->GetNode() };
    Scene* oven{ new Scene(emitter->GetContext()) };
    emitter->SetNode(oven);

    while (time > .0f)
    {
        const float dt{ Min(time, .05f) };
        oven->Update(dt);
        time -= dt;
    }

    emitter->SetNode(node);
    oven->Remove();
}
```

(unrun)

-------------------------

