Jimmy78 | 2017-01-02 01:15:39 UTC | #1

Hey guys , 

I just started working with 3D and using urho but the lack of documentation is really bad . 

I'm following the samples but even then , without some basic background into the functionalities - its really hard . 

1 . How to place objects on a plane ?

I created a scene , a plane and put a camera at point 0,0,0

scene = new Scene();
scene.CreateComponent<Octree>();

PlaneN = scene.CreateChild("Plane");
PlaneN.Scale = new Vector3(100, 1, 100);

plane = PlaneN.CreateComponent<StaticModel>();
plane.Model = ResourceCache.GetModel("Models/Plane.mdl");
plane.SetMaterial(ResourceCache.GetMaterial("Materials/StoneTiled.xml"));

Node lightNode = scene.CreateChild("DirectionalLight");
lightNode.SetDirection(new Vector3(0.6f, -1.0f, 0.8f));
Light light = lightNode.CreateComponent<Light>();
light.LightType = LightType.Directional;

CameraNode = scene.CreateChild(name: "camera");
 camera = CameraNode.CreateComponent<Camera>();
 camera.FarClip = 300;
CameraNode.Position = new Vector3(0.0f, 0.0f, 0.0f);

----------------- I tried to put some objects on the plane but they appear halfway through and some does not even show up.

Node modelNode;

            modelNode = scene.CreateChild("Box");
            modelNode.Position = new Vector3(5.0f, 0.0f, 0.0f);

            modelNode.SetScale(1.0f);

            var obj = modelNode.CreateComponent<StaticModel>();
            obj.Model = ResouceCache.GetModel("Models/Box.mdl");
            obj.SetMaterial(ResouceCache.GetMaterial("Materials/Stone.xml"));
            obj.CastShadows = true;

Node modelNode2;

            modelNode2 = scene.CreateChild("Box2");
            modelNode2.Position = new Vector3(5.0f, 10.0f, 5.0f);

            modelNode2.SetScale(1.0f);

            var obj2 = modelNode2.CreateComponent<StaticModel>();
            obj2.Model = ResouceCache.GetModel("Models/Box.mdl");
            obj2,SetMaterial(ResouceCache.GetMaterial("Materials/Stone.xml"));
            obj2.CastShadows = true;


2. How does the vector 3 position work ?

Lets say i want to put some items around my camera in a 360 degree way , they will be at the same level but different distances from the midpoint of the scene

modelNode.Position = new Vector3(5.0f, 0.0f, 0.0f);   // creates a box 5f away from the camera

modelNode2.Position = new Vector3(5.0f, 10.0f, 5.0f);  // does not show up at all

3 . What are Materials and Textures ?

Lets say i want to apply an image to a sphere/box - how do i do it ?

-------------------------

Modanung | 2017-01-02 01:15:39 UTC | #2

The y-axis (second argument for a Vector3) points up. The invisible boxes that are created at y = 10.0f are probably above view.

The box that does appear - albeit halfway the plane - is halfway the plane because you put it at the same height as the plane and it's pivot is at the center of the box.

To put things in a circle you're best off using a for loop and Quaternion. Which in C++ could look something like this:
[code]
int numObjects{ 5 };
for (int i{0}; i < numObjects; ++i) {

    Node* objectNode{ scene->CreateChild() };
    objectNode->SetPostion(Quaternion(i * (360.0f / numObjects), Vector3::UP) * Vector3(5.0f, 0.5f, 0.0f));
    objectNode->CreateComponent<StaticModel>()->SetModel("Models/Box.mdl");
}
[/code]

-------------------------

