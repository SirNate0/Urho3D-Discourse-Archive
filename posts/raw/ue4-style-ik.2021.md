namic | 2017-01-02 01:12:20 UTC | #1

UE4 has the ability to create blueprints to define character animation. For example, i had something similar to this: [forums.unrealengine.com/showthr ... Style%2923](https://forums.unrealengine.com/showthread.php?67186-WIP-Pose-Based-Animation-Blending-%28Overgrowth-Style%2923)

Trying to reimplement that in Urho, but i wasn't able to find any API to describe the manipulation of bones. Is this possible? Could anyone point me to the right place or present a few examples? The technique above is heavily inspired by these:

[aigamedev.com/open/editorial/ani ... evolution/](http://aigamedev.com/open/editorial/animation-revolution/)
[gdcvault.com/play/1020583/An ... e-Approach](http://www.gdcvault.com/play/1020583/Animation-Bootcamp-An-Indie-Approach)

Urho having such features would be extremely valuable for indies, specially because we don't have enough money to spend on expensive animation.  :smiley:

-------------------------

1vanK | 2017-01-02 01:12:21 UTC | #2

[topic1040.html](http://discourse.urho3d.io/t/solved-ik-foot-placement/1010/1)
[topic1273.html](http://discourse.urho3d.io/t/unity-ikcontrol-script/1229/1)

EDIT: [github.com/urho3d/Urho3D/wiki/H ... trol-bones](https://github.com/urho3d/Urho3D/wiki/How-to-manually-control-bones)

-------------------------

hunkalloc | 2022-11-16 05:01:05 UTC | #3

not sure if this answers the question. the video specifically mentions creating keyframes and being able to set blend modes between those keyframes.

is it possible to configure what blend mode is going to be used between animation frames in Urho?

-------------------------

