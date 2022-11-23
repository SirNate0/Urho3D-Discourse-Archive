OvermindDL1 | 2017-01-02 01:01:21 UTC | #1

I was walking through the callstacks and found that there is a *LOT* of checks in View::UpdateGeometries that do little.  It is a fairly cheap function overall compared to the overall callstack, but adding a few more cache's (or maybe an Event or two depending on how fast that call process is) could cut out a *lot* of the tests.  Specially in my scene I am noticing on line 1179 the loop of `for (unsigned i = 0; i < renderPath_->commands_.Size(); ++i)` are testing all of the renderPaths for if `(!IsNecessary(command))` and `if (command.type_ == CMD_SCENEPASS)`, wouldn't it be better to have a dedicated cache/vector for the ones that fullfill these that are updated as necessary instead of looping?  This one overall is trivial though, the big one that had a lot of hits on my scene was on line 1219 the loop of `for (PODVector<Drawable*>::Iterator i = geometries_.Begin(); i != geometries_.End(); ++i)` loops over all geometries, of which there are quite a *lot*, but it just tests for either `if (type == UPDATE_MAIN_THREAD)` or `else if (type == UPDATE_WORKER_THREAD)`, yet all of them in my scene are UPDATE_NONE, so it is looping needlessly.

Just a notice I had, it is still very little time compared to, say, just clearing the screen, but it looks like a simple optimization that could potentially give a noticeable boost, though tests would say for sure instead of just guessing.  :slight_smile:

-------------------------

cadaver | 2017-01-02 01:01:22 UTC | #2

Looping the renderpath commands even several times should basically be negligible, and it doesn't grow with the number of scene objects.

The question of looping through the geometries to find out how they're updated is a good one, that can possibly be moved as part of the base pass gathering.

Generally, a profiler like CodeAnalyst will know best the code hotspots.

EDIT: after going through the code, I cannot in good conscience move the geometry's update type check earlier. It's probably something that would never effect 99.9% of cases, but there's the odd possibility that due to some interaction, eg. when an object is viewed from multiple views, it would first return being OK with a threaded update, but later (close to rendering) it would actually decide it needs a main thread update, for example updating its vertex buffer. In that case, if we had already determined it to want a threaded update and went with that, we'd crash. It has to be noted that it would be a nice optimization, because in the HugeObjectCount sample I see the SortAndUpdateGeometry block to take 0.5 ms, which cannot be called negligible anymore. That scene has 62500 objects though, so it's an extreme case.

EDIT 2: by re-checking threaded updated drawables (there should be very few of them) just before they're put to the threaded queue, the optimization should be safe.

-------------------------

