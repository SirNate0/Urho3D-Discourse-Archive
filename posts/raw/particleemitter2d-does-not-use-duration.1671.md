JimMarlowe | 2017-01-02 01:09:24 UTC | #1

ParticleEmitter2D does not respond correctly to a duration parameter from pex file, I found this by attempting to play an explosion pex file that became a [b]fireball from heck[/b].

The problem is in Source/Urho3D/Urho2D/ParticleEmitter2D.cpp
in the function "void ParticleEmitter2D::Update(float timeStep)"
in the line "if (emissionTime_ >= 0.0f)",  the comparison should be ">" instead of ">=".

To test this, use the 25_Urho2DParticle.as sample program, it does not need to be modified itself.
In the Data/Urho2D/greenspiral.pex asset file, add the line  "<duration value="3.00"/>" somewhere after the <particleEmitterConfig> tag.

What you currently see when running 25_Urho2DParticle, is a green constantly moving spiral.
What you should see with a duration set, is a green spiral that creates a segment for 3 seconds then stops, while the existing segment draws into the center of the screen and finally disappears (moving the cursor out of the way makes it easier to see).
if you have a shorter duration particle, the flaw is much more visible.

-------------------------

