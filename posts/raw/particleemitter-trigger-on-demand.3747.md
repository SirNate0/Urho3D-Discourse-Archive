stark7 | 2017-11-16 16:36:08 UTC | #1

Hello,

My use case is that when a rigidbody detects a collision, I want a ParticleEmitter to trigger only once (like an explosion effect) and then stop by itself instead of triggering continuously until the node is removed. Is there a trigger on demand for particle emitters?

Also setting AutoRemoveMode doesn't seem to do anything for me for some reason, in either the editor or my project.

-------------------------

orefkov | 2017-11-17 15:11:30 UTC | #2

Do you set "Active Time" attribute for PartitionEffect other than 0?
Usually I just clone "prefab" with needed partitions and set AutoRemoveMode.

-------------------------

stark7 | 2017-11-17 15:11:27 UTC | #3

Thanks! I never set an Active time before, that seems to work now as intended.

-------------------------

