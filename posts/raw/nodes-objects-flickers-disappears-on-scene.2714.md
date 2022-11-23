Jimmy781 | 2017-01-17 03:26:41 UTC | #1

Hey guys , i created several nodes and static models on a scene which i'm viewing from above . 

However when i zoom in/out , the items flickers and disappears (reappears when i zoom in) . Sometimes it works fine , other times not .

I'm not really sure whats causing it

-------------------------

hdunderscore | 2017-01-17 04:06:18 UTC | #2

Camera view/draw distance maybe?

-------------------------

Jimmy781 | 2017-01-17 23:44:55 UTC | #3

Is there any function to set that ?

    CamNode = scene.CreateChild(name: "camera");
                camera = CamNode.CreateComponent<Camera>();
               

                camera.FarClip = 300000;

                CamNode.Position = new Vector3(0.0f, 200.0f, 0.0f);

-------------------------

GoogleBot42 | 2017-01-18 00:47:00 UTC | #4

Did you set the bounding box of the model correctly?  (If you loaded the model from from one of the included Urho3D models this won't be a problem.  This is probably only a problem if you generated your own model/meshes on the fly at runtime.)

Do you think you could post a screenshot or animated gif?

-------------------------

