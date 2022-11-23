v534 | 2017-01-02 01:12:05 UTC | #1

How would you flip a 3D animation horizontally? I would like to have an animation for the right side, and then mirror it for a second animation for the left side.

-------------------------

Modanung | 2017-01-02 01:12:06 UTC | #2

The best I can come up with is the [i]Paste Pose[/i] function in Blender. By first selecting all bones in post mode, hitting Ctrl+C, then Space -> "Paste Pose" and check Flipped on X-axis. That will do the trick in Blender for a single frame. :unamused:

-------------------------

Mike | 2017-01-02 01:12:08 UTC | #3

I've done a quick test by cloning the animation as mirrored and it works fine. Next step is to also allow to play the animation in reverse for completeness.
Performancewise, I'm wondering what could be the optimal approach to get the job done (I've assumed that modifying the keyframes on the fly would be worst than using a manual Animation ressource, but there may be better options).

-------------------------

