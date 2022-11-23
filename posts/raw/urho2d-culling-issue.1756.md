OvermindDL1 | 2017-01-02 01:09:54 UTC | #1

I am attempting to use Urho2D, however anytime the camera node is rotated (say, with rotate2d), the clipping bounds of the Urho2D nodes appear to be getting constrained on the left/right axis.  Easiest way to reproduce it, just open the sample of 24_Urho2DSprite, at the end of the HandleUpdate method just add:
[code]cameraNode_->Rotate2D(timeStep*10.0f);[/code]
Then run it and watch what happens.  I am trying to have a follow camera above the 2D player that rotates as the player rotates, however that appears difficult to do when everything becomes invisible at about 45 degrees...

It also happens on the 36_Urho2DTileMap sample by adding the same code at the same place, you can watch the tiles vanish at the edges on in.

-------------------------

