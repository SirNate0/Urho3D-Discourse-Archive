Mike | 2017-01-02 00:58:02 UTC | #1

When parenting a SoundSource3D to a movable node, it doesn't follow it. Is this the intended behavior?

-------------------------

cadaver | 2017-01-02 00:58:02 UTC | #2

SoundSource3D should update itself every frame using its world position relative to the sound listener's world position, so theoretically it should work properly when parented.

-------------------------

Mike | 2017-01-02 00:58:02 UTC | #3

Sorry, my mistake, my SoundListener was not at the right place.

-------------------------

