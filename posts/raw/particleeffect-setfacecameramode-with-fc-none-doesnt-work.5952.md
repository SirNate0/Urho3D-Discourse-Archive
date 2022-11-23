Dave82 | 2020-02-29 11:56:54 UTC | #1

It doesn't matter if i enable this , the particles still keep facing the camera. I'm using 1.7 and this worked in 1.5

As i see FC_DIRECTION doesn't work either. Both behave just like face XYZ...

This is FC_DIRECTION. The white squared particles should rotate towards their direction which is clearly not happening... 

https://www.youtube.com/watch?v=cJ87wQpz-t4

-------------------------

Dave82 | 2020-02-29 08:59:36 UTC | #2

The problem is solved. The 1.7 ParticleEffect now stores FaceCameraMode in the particle xml file so if you load and your effect after you set emitter->SetFaceCameraMode() it will be overridden at loading time.
It's interesting that somehow the faceCamera mode is overridden even if the faceCameraMode attribute is not present in the xml file 
(clearly the if (source.HasChild("faceCameraMode")) should fail and not change faceCameraMode)

-------------------------

