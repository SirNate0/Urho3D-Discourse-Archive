shahram.shobeiri | 2019-05-20 18:52:04 UTC | #1

What I'm trying to do is implementing a 360 degree image viewer in Xamarin.Forms. 
I'm using UrhoSharp and here are the steps of what I've done to view a 360 degree image:

* Creating a 3d sphere model
* Loading a 360 degree (Panorama) image
* Set image as the Material of the Sphere

All the above steps are OK and I can see the flatten image from different view points but the problem is some kind of waves or distortions are in the image and the line which supposed to be straight are wavy. I don't know what setting could solve the problem, please help.

Here is the wavy outcome:
![930a2tzfg5jg|281x500](upload://z9LhU00QUGuLbWb5hEXi0MSVqRa.jpeg) 
And here is my code:

```
private void CreateScene()
{
        // Scene
        var scene = new Scene();
        scene.CreateComponent<Octree>();


        // Node (Rotation and Position)
        var node = scene.CreateChild("room");
        node.Position = new Vector3(0, 0, 0);
        //node.Rotation = new Quaternion(10, 60, 10);
        node.SetScale(1f);

        // Model
        var modelObject = node.CreateComponent<StaticModel>();
        modelObject.Model = ResourceCache.GetModel("Models/Sphere.mdl");

        var zoneNode = scene.CreateChild("Zone");
        var zone = zoneNode.CreateComponent<Zone>();
        zone.SetBoundingBox(new BoundingBox(-300.0f, 300.0f));
        zone.AmbientColor = new Color(1f, 1f, 1f);

        //get image from byte[]

        //var url = "http://www.wsj.com/public/resources/media/0524yosemite_1300R.jpg";
        //var wc = new WebClient() { Encoding = Encoding.UTF8 };

        //var mb = new MemoryBuffer(wc.DownloadData(new Uri(url)));
        var mb = new MemoryBuffer(PanoramaBuffer.PanoramaByteArray);
        var image = new Image(Context) { Name = "MyImage" };
        image.Load(mb);

        //or from resource

        //var image = ResourceCache.GetImage("Textures/grave.jpg");
        var isFliped = image.FlipHorizontal();
        if (!isFliped)
        {
            throw new Exception("Unsuccessful flip");
        }
        var m = Material.FromImage(image);
        m.SetTechnique(0, CoreAssets.Techniques.DiffNormal, 0, 0);
        m.CullMode = CullMode.Cw;
        //m.SetUVTransform(Vector2.Zero, 0, 0);
        modelObject.SetMaterial(m);

        // Camera
        var cameraNode = scene.CreateChild("camera");
        var camera = cameraNode.CreateComponent<Camera>();
        camera.Fov = 75.8f;

        // Viewport
        Renderer.SetViewport(0, new Viewport(scene, camera, null));
    }
```

-------------------------

Modanung | 2019-05-20 18:55:20 UTC | #2

Hello @shahram.shobeiri and welcome. Sorry for being blunt (or rather anti-sharp), but I'm afraid these are not the UrhoSharp/Xamarin forums, this question is off-topic here.
You're welcome, or even encouraged, to rewrite your project using Urho3D - as opposed to UrhoSharp - and ask this community for any support along the way.

-------------------------

Bananaft | 2019-05-23 17:44:35 UTC | #3

Those are triangles linearly interpolating their UVs. You can either increase number of polygons in your sphere or generate accurate UVs in pixel shader.

-------------------------

shahram.shobeiri | 2019-05-22 12:13:22 UTC | #4

Thanks @Bananaft, I'm completely new in Urho3D and 3D concepts, How can I increase number of polygons in my sphere?

-------------------------

Modanung | 2019-05-23 17:44:34 UTC | #5

[quote="shahram.shobeiri, post:4, topic:5166"]
How can I increase number of polygons in my sphere?
[/quote]


https://www.blender.org/download/

-----
https://github.com/reattiva/Urho3D-Blender

[quote="shahram.shobeiri, post:4, topic:5166"]
I’m completely new in Urho3D
[/quote]

You're using UrhoSharp, it is not the same as Urho3D.

-------------------------

Bananaft | 2019-05-23 17:44:30 UTC | #6

Yeah, sphere is just a model in models folder. You have to model and export a new one. B.t.w. you can observe the same UV artifact in blender.

-------------------------

shahram.shobeiri | 2019-05-23 17:58:49 UTC | #7

Finally my problem solved. Even though @Modanung said the topic is irrelevant to Urho3D but your response was really helpful for me.
I understood that I should increase the polygons of my sphere by creating a new model in a tool like Blender and export it to MDL format by a add-in and use the new model in my code.
Thank you very much @Bananaft and @Modanung.
Here is the outcome:
![Screenshot_1558631341|281x500](upload://j24tMTqPzaRkXjV76cJc1vZ9ncc.jpeg)

-------------------------

Modanung | 2019-05-23 18:06:04 UTC | #8

[quote="shahram.shobeiri, post:7, topic:5166"]
...but your response was really helpful for me.
[/quote]
I can't help it. :slight_smile:

I'm glad you solved your problem and I hope the times ahead will be bearable, looking at your location.

-------------------------

