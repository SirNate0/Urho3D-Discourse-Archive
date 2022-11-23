socrobot | 2019-02-13 05:32:03 UTC | #1

 I wonder whether the camera has only one scene binding?

The camera Created through scene as follow:
cameraNode = scene_.CreateChild(“Camera”);
cameraNode.CreateComponent(“Camera”);

But the when create viewport,It need pass scene &amp; camera as follow:
Viewport@ viewport = Viewport(scene_, cameraNode.GetComponent(“Camera”));

if I use another scene with the same camera : Viewport@ viewport = Viewport(sceneTest, cameraNode.GetComponent(“Camera”))
it still work!

-------------------------

