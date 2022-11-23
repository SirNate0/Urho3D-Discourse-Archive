andrekoehler | 2017-05-09 12:30:16 UTC | #1

I'm using UrhoSharp to port a golf simulation that was using the (M)OGRE engine.

The following test animation has no effect:
ValueAnimation rot = new ValueAnimation(context_);
rot.SetKeyFrame(impact.Time, Quaternion.Identity);
rot.SetKeyFrame(stroke.AnimationLength, Quaternion.FromAxisAngle(Vector3.UnitZ, 360));

It seems like the angles 0, 360, n*360 are all treated equal, but I want the object to be rotated multiple times between two keyframes.

In (M)OGRE, there was an option NodeAnimationTrack.UseShortestRotationPath for that purpose that could be disabled.
Is there a similar option in Urho3D?
Is specifying in-between keyframes the only possible workaround?

-------------------------

