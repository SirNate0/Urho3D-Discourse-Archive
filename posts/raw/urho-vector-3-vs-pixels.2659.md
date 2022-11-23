Jimmy781 | 2017-01-03 04:43:52 UTC | #1

I'm new to 3D engines and i have a question .

I created a plane.

    _scene = new Scene();
    _scene.CreateComponent();

    var planeNode = _scene.CreateChild("Plane");
    planeNode.Scale = new Vector3(500.0f, 1.0f, 500.0f);

I have an image 500px*500px which i set on the plane :

`planeObject.SetMaterial(Material.FromImage("image.png"));`


Since both are square , does that mean that the image will take the full size of the plane and that 1px will be equal to 1f  (on the plane) regardless of its actual size ?

-------------------------

urho3d | 2017-01-03 05:57:00 UTC | #2

Duplicate Topic: http://discourse.urho3d.io/t/urho-plane-vector3-size-to-px/2658

-------------------------

urho3d | 2017-01-03 05:57:06 UTC | #3



-------------------------

