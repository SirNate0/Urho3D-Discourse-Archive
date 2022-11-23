v0van1981 | 2017-01-02 01:05:41 UTC | #1

How to create node three and then add it to the scene?

[code]  Node* result = new Node(context_);
  Model* model = cache->GetResource<Model>("Models/Mushroom.mdl");
  Material* material = cache->GetResource<Material>("Materials/Mushroom.xml");
  Node* node = result->CreateChild();
  StaticModel* staticModel = node->CreateComponent<StaticModel>();
  staticModel->SetModel(model);
  staticModel->SetMaterial(material);
  staticModel->SetCastShadows(true);
  node->SetPosition(Vector3(0, 0, 0));
  scene_->AddChild(result); // do not works, model is not added to scene [/code]

[code]  Node* result = new Node(context_);
  scene_->AddChild(result); // ------------------------  it's work
  Model* model = cache->GetResource<Model>("Models/Mushroom.mdl");
  Material* material = cache->GetResource<Material>("Materials/Mushroom.xml");
  Node* node = result->CreateChild();
  StaticModel* staticModel = node->CreateComponent<StaticModel>();
  staticModel->SetModel(model);
  staticModel->SetMaterial(material);
  staticModel->SetCastShadows(true);
  node->SetPosition(Vector3(0, 0, 0));
[/code]

-------------------------

cadaver | 2017-01-02 01:05:41 UTC | #2

Drawable components need to find the octree at their creation time, so the scenario isn't supported. Make sure the node is in the scene before creating components. Easiest is to always use scene->CreateChild() instead of new'ing a node, and reparent later if necessary.

There is a related "reverse" issue in github tracker (drawable continues to render if its node has refcount even when removed from scene), so this might be revisited later. But for now you need to follow that rule.

-------------------------

v0van1981 | 2017-01-02 01:05:41 UTC | #3

I try to realise background loading parts of big world and connect it to scene? Any way for it?

-------------------------

cadaver | 2017-01-02 01:05:41 UTC | #4

If you're doing this in a background thread, don't - operations like setting a model for a StaticModel are only safe to do in the main thread.

Use Instantiate() or InstantiateXML() to load pieces of scene (prefabs) into the scene. Beforehand, you can background load resources used by them, which is supported by ResourceCache in a background thread. For this, you can "misuse" Scene's LoadAsync() or LoadAsyncXML() functions in the LOAD_RESOURCES_ONLY mode. This should mostly but not completely mitigate framerate hitches caused by loading the new node(s).

Urho3D doesn't however promise fitness for large world scenarios such as this so be prepared to modify the engine heavily if you want true background loading of scenenode hierarchies.

-------------------------

friesencr | 2017-01-02 01:05:41 UTC | #5

[quote="cadaver"]If you're doing this in a background thread, don't - operations like setting a model for a StaticModel are only safe to do in the main thread.

Use Instantiate() or InstantiateXML() to load pieces of scene (prefabs) into the scene. Beforehand, you can background load resources used by them, which is supported by ResourceCache in a background thread. For this, you can "misuse" Scene's LoadAsync() or LoadAsyncXML() functions in the LOAD_RESOURCES_ONLY mode. This should mostly but not completely mitigate framerate hitches caused by loading the new node(s).

Urho3D doesn't however promise fitness for large world scenarios such as this so be prepared to modify the engine heavily if you want true background loading of scenenode hierarchies.[/quote]

Lasse what would you do to overcome the floating point precision in Urho for very large scenes?

-------------------------

cadaver | 2017-01-02 01:05:41 UTC | #6

Without actually moving to doubles, which may be a problem on the GPU side, move the world regions (pieces) around so that 0,0,0 is always the center of the region the player is in. This may not be trouble-free or cheap performance-wise, though (think physics for example)

-------------------------

cadaver | 2017-01-02 01:05:47 UTC | #7

The support for correctly working Drawables etc. after constructing outside the scene and then moving in later should now exist in the master branch.

There are some pitfalls, which can be devious, for example a RigidBody does not store its velocities until the Bullet rigidbody exists, and it can't create that before belonging to a scene. Also, joining rigidbodies with constraints depends on node ID's, which are not assigned before the nodes/components are in the scene.

-------------------------

friesencr | 2017-01-02 01:05:47 UTC | #8

There is a spline path that uses NodeID if I recall too.  

Does the system create all the nodes and then all the components?

-------------------------

cadaver | 2017-01-02 01:05:47 UTC | #9

Roughly yes, in normal deserialization, a node gets loaded first (and is created directly into the scene, so there isn't this "disconnected mode" happening), then its components, then its child nodes.

Furthermore, because the runtime ID's may be different than ones in the scene file or prefab, all created objects are stored into the SceneResolver which will go through all ID attributes and remap the old IDs to new IDs after loading the scene or the prefab is complete.

-------------------------

