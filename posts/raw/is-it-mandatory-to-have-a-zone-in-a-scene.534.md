rogerdv | 2017-01-02 01:01:11 UTC | #1

I see that the samples create a zone, even for that basic scenes, are they essential?

-------------------------

cadaver | 2017-01-02 01:01:11 UTC | #2

If you don't mind the Renderer using the default zone, which has a dark grey ambient color and black fog (I don't remember the fade distance), you don't have to create a zone.

You could also adjust the values from the default zone. See Renderer::GetDefaultZone().

-------------------------

rogerdv | 2017-01-02 01:01:11 UTC | #3

Is it possible to have several zones in a single scene  (if it is very large, like a Skyrim world)? And totally unrelated, is it possible to have a very large world? the terrain has multipage capabilities?

-------------------------

cadaver | 2017-01-02 01:01:11 UTC | #4

Yes, you can have several zones. Each object uses the values from the zone that it's in. You can also create "gradient" zones for ambient level changes, see [urho3d.github.io/documentation/HEAD/_zones.html](http://urho3d.github.io/documentation/HEAD/_zones.html)

The Terrain component itself manages a single heightmap without paging. In a large world I imagine you would instantiate/delete chunks of scenery as you move around, each of which could contain their own terrain. The engine itself does not have automatic functionality for this so it's something you would manage manually. This would likely also include "normalizing" the coordinates to avoid float inaccuracies. Basically, always have the chunk that the player currently resides in, at world origin, and move the chunks around when you transition between them.

-------------------------

