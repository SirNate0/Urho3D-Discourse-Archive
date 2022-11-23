Leith | 2019-05-27 06:44:26 UTC | #1


I have created a ParticleEmitter in the Editor, and exported it "by node" to xml.

When I call Scene::InstantiateXML (which takes position and orientation arguments), handing in a random world position, I notice that, for one frame, the new emitter is created at (0,0,0), and emits some particles there - apparently, the position and orientation we provide are not immediately applied, and so later in the same frame, we get particles emitted at the wrong world location.
Every time I create a new randomly positioned particle emitter instance, I get a "puff" of particles near (0,0,0)

-------------------------

Leith | 2019-05-28 02:00:11 UTC | #2

When I examine the content of the xml representing my particle emitter prefab, I realize that I have exported data for a bunch of particles - I had "serialize particles" enabled when I exported the emitter, so this partly explains why I am seeing such an obvious puff of particles being created at (0,0,0).

-------------------------

