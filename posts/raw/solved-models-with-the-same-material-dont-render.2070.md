Sir_Nate | 2017-01-02 01:12:48 UTC | #1

If I create 2 nodes with 2 Static/Animated Model components and assign them the same model and the same material (or don't assign both of them a material), when they both appear in the camera's field of view they disappear (but I can see them if only one is in the field of view).
If I, for example, Clone() the material, it works, or if I assign one model a different material, or if I use a different model with the same material. 
If I save the scene and open it in the Editor, though, it displays fine (but on the other hand, if I open it in the Editor which I open through my application, the same disappearance occurs).

Any suggestions?

-------------------------

cadaver | 2017-01-02 01:12:48 UTC | #2

This sounds like instancing going wrong. OS? Graphics API being used? Do the samples exhibit the same behavior? Does it help if you switch instancing off in e.g. editor settings?

-------------------------

Sir_Nate | 2017-01-02 01:12:48 UTC | #3

I figured it out -- it had something to do with a file in CoreData -- I just copied the folder from the newer copy of the Urho repository and it works now.

-------------------------

cadaver | 2017-01-02 01:12:48 UTC | #4

Yes, transmitting instance coordinates in shaders changed when the arbitrary vertex declaration refactoring was done.

-------------------------

