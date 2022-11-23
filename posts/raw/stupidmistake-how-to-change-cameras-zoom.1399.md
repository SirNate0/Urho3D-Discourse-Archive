Vagabond | 2017-01-02 01:07:30 UTC | #1

In the staticScene sample I tried this (Changed line 120 and inserted a new one below it):
[code]
119 | cameraNode_ = scene_->CreateChild("Camera");
120 | Camera* camera = cameraNode_->CreateComponent<Camera>();
121 | camera->SetZoom(1.0f);
[/code]
But as no matter what value I placed in there the view was the same every time I compiled and ran that sample, here I am.  
Edit: Remembered I had changed the target name in my CMakeLists.txt file... Sorry for wasting your time.  :blush:

-------------------------

rasteron | 2017-01-02 01:07:30 UTC | #2

Hey Vagabond,

First of, Welcome to the forums! :slight_smile: I have not tested this in C++, but in Angelscript it is done by:

[code]
cameraNode = scene_.CreateChild("Camera");
Camera@ camera = cameraNode.CreateComponent("Camera");    
camera.zoom = 0.1f;
[/code]

[img]http://i.imgur.com/A3tYAbS.png[/img]

You should probably check if you just need to do a clean and rebuild of your executable.

-------------------------

Pyromancer | 2017-01-02 01:07:30 UTC | #3

In the vein of rifle scopes and the like, you could also potentially move the camera on the look vector a certain distance and rotate it around the current "real" position of the player.

So your scene hierarchy would be a root node that moves and rotates he camera, then the camera itself as a separate node parented to that root node.

-------------------------

