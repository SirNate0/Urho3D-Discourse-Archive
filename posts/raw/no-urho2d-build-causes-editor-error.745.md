Bluemoon | 2017-01-02 01:02:37 UTC | #1

Urho3D Editor throws error when Urho3D is build without the 2D components... This error comes from the  EditorHierachyWindow.as at line 879 and 883 where ParticleEffect2D is referenced, it throws the error because ParticleEffect2D (and other 2D component) does not exist in the build.

If it's worth it, I believe it will be awesome to implement a work-around for this issue so that those using the Urho3D library without 2D components can still use the Editor without problem

-------------------------

cadaver | 2017-01-02 01:02:37 UTC | #2

It would have to be worked around by completely generic component access, ie. attributes. Will make the code ugly, but is potentially possible.

Note that similarly, building without physics will cause several errors in the editor. That I don't think is worth working around.

-------------------------

Bluemoon | 2017-01-02 01:02:37 UTC | #3

[quote="cadaver"]It would have to be worked around by completely generic component access, ie. attributes. Will make the code ugly, but is potentially possible.

Note that similarly, building without physics will cause several errors in the editor. That I don't think is worth working around.[/quote]

Okay... I'll dabble around in the code and see what I can tweak  :slight_smile:

-------------------------

JTippetts | 2017-01-02 01:02:37 UTC | #4

Personally, I just keep a build with everything enabled (Lua, Urho2D, AngelScript, everything) for when I need to do work with the editor or for when I want to experiment with something. Seems much easier to do that than to try to munge the code to get it to work without one of the systems.

-------------------------

cadaver | 2017-01-02 01:02:46 UTC | #5

This should now be fixed in the master branch, by using bare Resource & Component classes, and SetAttribute().

-------------------------

