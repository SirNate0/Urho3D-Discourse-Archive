jzpekarek | 2020-06-06 22:54:33 UTC | #1

Hi, I recently upgraded from Urho3D 1.5 to Urho3D 1.7.1, and ran into a bug that I can't seem to resolve that wasn't a problem in 1.5. I found that when I have multiple instances of a model that use the same material, the objects all disappear. This is building on Windows, Direct3d9 (I got linker errors I couldn't resolve when I tried Direct3D11).

I modified the StaticScene example to just create two boxes as shown below, and assign the same material to both. When I run the example, the boxes are not visible. If I change the second box to use material2, then I see the two boxes. I also found that you can use the same material on different models, and it seems to work as expected, so it appears there is an issue when using the same Material and same Model together on multiple objects. Any ideas? 

Node* boxNode1 = scene_->CreateChild("Box");
boxNode1->SetPosition(Vector3(-4.0f, 0.0f, 15.0f));
boxNode1->SetScale(5.0f);
Model* box = cache->GetResource<Model>("Models/Box.mdl");
Material* material1 = cache->GetResource<Material>("Materials/Mushroom.xml");
Material* material2 = cache->GetResource<Material>("Materials/Terrain.xml");

StaticModel* boxObject1 = boxNode1->CreateComponent<StaticModel>();
boxObject1->SetModel(box);
boxObject1->SetMaterial(material1);

//Create a second node, using the same model and material
Node* boxNode2 = scene_->CreateChild("Box");
boxNode2->SetPosition(Vector3(4.0f, 0.0f, 15.0f));
boxNode2->SetScale(5.0f);
StaticModel* boxObject2 = boxNode2->CreateComponent<StaticModel>();
boxObject2->SetModel(box);
boxObject2->SetMaterial(material1);

-------------------------

jzpekarek | 2020-06-06 23:41:22 UTC | #2

One other thing I just realized is that the StaticScene example isn't working for me either. If I comment out the line below, then I see all the mushrooms (all white), but with the line below enabled, they all disappear (but with some strange drawing artifacts on the right side of the screen).

//mushroomObject->SetMaterial(cache->GetResource<Material>("Materials/Mushroom.xml"));

-------------------------

jzpekarek | 2020-06-07 00:22:31 UTC | #3

Sorry for continuing to reply to my own post, but I figured out that the problem is related to the dynamic instancing (which happens with multiple identical models with the same material). If I turn that off, then the example works as expected, so it appears there is a problem with the dynamic instancing.

Renderer* renderer = GetSubsystem<Renderer>();
renderer->SetDynamicInstancing(false);

-------------------------

JTippetts | 2020-06-07 02:55:17 UTC | #4

Make sure you update your CoreData folders to ensure you are using the shaders for the newer Urho3D version. Having a stale CoreData folder can result in issues like that.

Additionally, 1.7 is confirmed to be buggy. Although there hasn't been a stable release since then, the current master is pretty stable and has fixed a lot of the issues that plague 1.7, so my recommendation is that you update to master.

-------------------------

jzpekarek | 2020-06-07 20:36:33 UTC | #5

Thanks for the suggestion, updating the CoreData didn't work, so I'll try updating to the latest source. I downloaded the 1.8 Alpha source (not sure if that is the same as the master), but I'm still working on getting it to build (my Visual Studio was too old, so I tried upgrading to VS 2019, and somehow the installation got corrupted, so fighting with that now)

-------------------------

jzpekarek | 2020-06-09 02:25:16 UTC | #6

FYI, upgrading to 1.8 alpha fixed the dynamic instancing issue!

-------------------------

