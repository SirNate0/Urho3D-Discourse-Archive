mostafa901 | 2019-11-07 08:49:03 UTC | #1

Hi,
I am newbie to Urho. so impressed. is there a possibility to zoom extent the camera?
to be more clear, when importing an architecture scene, sometimes the camera is located inside the building, that take the user a while to zoom out. if there is a way to instantly after loading to zoom extent (move the camera out), or even a way to get the bounding box of the model so i can add some distance to the camera position.

 I would be grateful. Thanks a lot.

-------------------------

guk_alex | 2019-11-06 16:41:12 UTC | #2

Yes, you can get BoundingBox of your model, get its center - and then set camera position relative to that center and size; then use LookAt on the camera node to rotate it relative to the object.

-------------------------

mostafa901 | 2019-11-06 17:12:39 UTC | #3

Perfect... looks like, I should play with the node than the camera it self. Thanks... 
regarding boundingbox.
I realized I can get bounding box from Model but not from node. I am currently importing xml file to the scene.. so, when i tried to look after the node, there is no Getboundingbox which makes sense. so how can i treat the node as a model?

-------------------------

mostafa901 | 2019-11-07 08:47:42 UTC | #4

gottcha Thanks

```
var modelnode = new Node();
modelnode.LoadXml(path);

modelnode.Rotate(new Quaternion(90, 0, 0), TransformSpace.Parent);
modelnode.Name = Path.GetFileNameWithoutExtension(path);

scene.AddChild(modelnode);
var bbx = scene.Children.Last().Children.SelectMany(o => o.Components).Where(x => x is StaticModel).Cast<StaticModel>().Select(o => o.BoundingBox);
var max = new Vector3(bbx.Max(o => o.Max.X), bbx.Max(o => o.Max.Y), bbx.Max(o => o.Max.Z));

await CameraNode.RunActionsAsync(new EaseInOut(new MoveBy(3, Vector3.Add(max, new Vector3(10f, 10f, 10f))), 10f));
CameraNode.LookAt(scene.Children.Last().Position);
```

-------------------------

Modanung | 2019-11-07 08:53:55 UTC | #5

Could `Octree::GetWorldBoundingBox()` be of any use in your case?

Also, welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

mostafa901 | 2019-11-07 09:36:58 UTC | #6

Thanks for the welcoming :slight_smile: 
I couldn't find such method (GetWorldBoundingBox) under Octree, but i did find it under drawables but as private method. [see this](https://github.com/xamarin/urho/blob/cfeff3d45eaaee536e978f857c453dde3ec1c7ed/Bindings/Portable/Generated/Drawable.cs#L322)

not sure if there is something i miss, or there are different versions of Urho??!!

-------------------------

Modanung | 2019-11-07 18:54:42 UTC | #7

Yes, you seem to be using a discontinued fork.

The *true* Urho can be found here:
https://github.com/urho3d/urho3d

-------------------------

