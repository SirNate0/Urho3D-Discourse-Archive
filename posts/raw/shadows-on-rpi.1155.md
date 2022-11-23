esak | 2017-01-02 01:05:45 UTC | #1

I have made a little test-pgm where shadows for objects are displayed.
This works fine on Windows, but not on RPI 2. Is this a limitation, maybe in OpenGL ES?
(I have used the same Urho3D version on both platforms: snapshot from master taken 2015-06-25.)

-------------------------

weitjong | 2017-01-02 01:05:46 UTC | #2

There is effectively only one shadow cascade map split for non-desktop graphics, so most probably you have to adjust the parameters for the Light::SetShadowCascade() call.

-------------------------

esak | 2017-01-02 01:05:48 UTC | #3

I have tried changing the parameters to Light::SetShadowCascade(), without any success.
(I have tried leaving out this call also to get the default values which I thought should work, but it doesn't.)
My code is basically copied from the sample 11_Physics. The same problem occurs with this sample on the RPI.
Is there something more you have to do to get this working on the RPI?

-------------------------

