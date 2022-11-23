Jimmy781 | 2017-01-02 21:41:16 UTC | #1

Hey guys ,

I created a plane :

_scene = new Scene();
_scene.CreateComponent<Octree>();

var planeNode = _scene.CreateChild("Plane");
planeNode.Scale = new Vector3(500.0f, 1.0f, 500.0f);


I have an image 500px*500px which i set on the plane :

planeObject.SetMaterial(Material.FromImage("staticmap.png"));


However , it seems the 1.0f is not equal to 1px of the image . (I wanted the plane and the image to have the same size or ratio - e.g : 1px of the image = 1.0f of the plane)

Is there any way to do that ?

and how much is 1.0f of Vector compared to 1px ?

-------------------------

hdunderscore | 2017-01-03 00:18:39 UTC | #2

Seems like this is an UrhoSharp question.

Screenshot of issue?

1.0f in Vector space has different values in pixel depending on camera/viewport set up. There are handy functions to handle conversion from world to screenspace and back (WorldToScreenPoint and ScreenToWorldPoint):
UrhoSharp: https://developer.xamarin.com/api/type/Urho.Camera/ 
Urho C++: https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_camera.html

-------------------------

jmiller | 2017-01-03 01:19:33 UTC | #3

Based on the name of your image, I thought it possible you might be interested in this.
http://discourse.urho3d.io/t/constant-billboard-size/2041

-------------------------

