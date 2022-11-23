Jimmy78 | 2017-01-02 01:15:40 UTC | #1

I'm using accelerometer to rotate my scene on android and it works well the first time . 
Then when i push the app to the background and re-enter - it crashes . Same thing when i close the app and open again.

I think it has something to do with the way the urho app is being created/destroyed .

[ERROR] FATAL UNHANDLED EXCEPTION: System.InvalidOperationException: Underlying native object was deleted for Handle=-1750703552. Node.SetRotation

12-19 21:20:19.344 I/MonoDroid(22006): UNHANDLED EXCEPTION:
12-19 21:20:19.354 I/MonoDroid(22006): System.InvalidOperationException: Underlying native object was deleted for Handle=-1750703552. Node.SetRotation
12-19 21:20:19.354 I/MonoDroid(22006):   at Urho.Runtime.ValidateRefCounted[T] (T obj, System.String name) [0x0008b] in <7887716be55746c783630ffe8634d8f1>:0 
12-19 21:20:19.354 I/MonoDroid(22006):   at Urho.Node.SetRotation (Urho.Quaternion rotation) [0x00000] in <7887716be55746c783630ffe8634d8f1>:0 
12-19 21:20:19.364 I/MonoDroid(22006):   at Urho.Node.set_Rotation (Urho.Quaternion value) [0x00000] in <7887716be55746c783630ffe8634d8f1>:0 

class UrhoMapApp : Urho.Application {


        Node CameraNode;
        private Scene scene;

       async void CreateScene()
        {


            //Scene Creation 
            scene = new Scene();
            scene.CreateComponent<Octree>();

            CameraNode = scene.CreateChild(name: "camera");
            camera = CameraNode.CreateComponent<Camera>();

            CameraNode.Position = new Vector3(0.0f, 0.1f, 0.0f);

                 AccelX.Changed += (s, e) =>
                 {
                       CameraNode.Rotation = new Quaternion(0, AccelX.value, 0);
                 };

        }

}

-------------------------

