Enhex | 2017-01-02 01:08:11 UTC | #1

Is it possible to manually add time to a scene in relatively big deltas? (f.e. several seconds)
If so would it cause precision problems?
Or will have non-deterministic outcome compared to stepping the same amount over several frames (significant enough)?

Maybe by setting the engine's min FPS to 0, and max FPS in such a way that it will step all the time in a single frame?
Maybe Engine::SetNextTimeStep() ?
Maybe step several normal frames until enough time has passed?

It also needs to affect only a single scene.

I'm mainly concerned about how it would affect model animation, particle effects and physics simulation.

-------------------------

thebluefish | 2017-01-02 01:08:11 UTC | #2

[code]
float newDeltaTime = 5.f;
myScene->Update(newDeltaTime);
[/code]

Physics simulation is done on a fixed update, so this has no effect. Anything else done on a fixed update would not see an effect.

Consequently anything done on a standard Update would not be updated, as E_UPDATE would not be called (E_UPDATE actually triggers Scene::Update). So anything you want to be updated should either be done during a "fixed" update (E_PHYSICSPRESTEP) or a scene update (E_SCENEUPDATE).

Particle Emitter works off a Scene-based event so it should work fine.

Animated Model doesn't use any Update events, it's instead queried by the Octree (as a Drawable).

-------------------------

