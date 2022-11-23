practicing01 | 2017-01-02 01:08:11 UTC | #1

Edit: What I ended up doing was setting markers, deleting the key frames outside of those markers and translating the needed frames to the beginning of the timeline.

Hello, I've bought a model that came with all of its animations together.  In blender they're all in the same timeline.  I set the timeline start/end frame values to match the animation that needs exporting.  I set the urho3d exporter to export the timeline.  In the editor, the beginning of the animation is not the first frame but some odd interpolation from something else.  After that it blends into the proper animations.  Any help with different export methods would be appreciated, thanks.

Beginning of animation (error):
[spoiler][img]http://img.ctrlv.in/img/15/11/19/564d18da50db0.png[/img][/spoiler]

Arrival into correct animation:
[spoiler][img]http://img.ctrlv.in/img/15/11/19/564d18f847c3e.png[/img][/spoiler]

-------------------------

codingmonkey | 2017-01-02 01:08:11 UTC | #2

I guessing that this is Unity's style animation track to keep all animation in one common timeline. Actually this is awful (IMO) method to keeping animation.
I do not know that methods using by Blender-Exporter to determine selected start/end, I guessing it only save whole track. 
In this case you may try to find keys in this common animation track and try to copy only need animation keys to new actions. 
After this just save this action as separated animations as usual.

-------------------------

