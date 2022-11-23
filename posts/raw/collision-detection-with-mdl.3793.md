thib2017 | 2017-11-26 21:25:51 UTC | #1

Hi, I'm new on urho3D, I created a simple plane jointed with 4 cylinder on blender and I imported it on an urho3D project but I don't understand how to correctly use the collision detection with a .mdl who is not a simple cube, a cylinder etc ...

I thanks per advance if somebody can help me or give me the right example or documentation.

-------------------------

Modanung | 2017-11-26 21:43:47 UTC | #2

For dynamic objects you can use the `CollisionShape::SetConvexHull` method. Static objects can also use triangle meshes as shape through `CollisionShape::SetTriangleMesh`.
Both functions ask for a `Model*` which you can acquire by invoking:
`GetSubsystem<ResourceCache>()->GetResource<Model>("...")`

And welcome to the forums! :confetti_ball:

-------------------------

thib2017 | 2017-11-26 21:24:05 UTC | #3

Thank you for the fast response ! Now It works better but it's not totally right.

Here is my code :

> Node* TempleNode = scene_->CreateChild("Temple");
> TempleNode->SetPosition(Vector3(0.0f, 6.0f, 3.0f));
> TempleNode->SetScale(Vector3(1.0f, 1.0f, 1.0f));
>  StaticModel* TempleObject = TempleNode->CreateComponent<StaticModel>();
>  TempleObject->SetModel(cache->GetResource<Model>("temple/temple.mdl"));
> 
> body = TempleNode->CreateComponent<RigidBody>();
> body->SetMass(10.0f);
> 
> Model* TempleModel = GetSubsystem<ResourceCache>()->GetResource<Model>("temple/temple.mdl");
> 
> CollisionShape* Templeshape = TempleNode->CreateComponent<CollisionShape>();
> 
> Templeshape->SetConvexHull(TempleModel);

and here is a screenshot of the result : [https://imgur.com/dedDUMu](https://imgur.com/dedDUMu)

-------------------------

Modanung | 2017-11-26 21:43:47 UTC | #4

Static objects in Bullet have a mass of 0. Also you used the convex hull instead of the triangle mesh.

A definition of convex: "Curved or rounded outward like the exterior of a sphere or circle."
Your temple model is not fully convex. :slight_smile:

-------------------------

thib2017 | 2017-11-26 21:46:20 UTC | #5

Thank you very much! It works well with theTriangle Mesh instead of the Convex Hull and without body->SetMass(10.0f).

PS : I'm not just new with urho3D I'm also new with 3D programming.

-------------------------

