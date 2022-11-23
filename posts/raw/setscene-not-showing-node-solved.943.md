practicing01 | 2017-01-02 01:04:17 UTC | #1

Hello, I'm trying to transfer a node and its components from one scene to another.  I know the node exists in the destination scene because I can get its components and child nodes.  However, the model itself is not visible.  Any help would be appreciated, thanks.

[code]
...
	player_->RemoveAllChildren();
	player_->RemoveAllComponents();
	File loadFile(context_,main_->filesystem_->GetProgramDir()
			+ "Data/Models/" + modelFilename + ".xml", FILE_READ);
	Scene* scene = new Scene(context_);
	scene->LoadXML(loadFile);
	player_ = scene->GetChild("player");
	player_->SetScene(scene_);
	player_->GetComponent<AnimationController>()->PlayExclusive("Models/idle.ani", 0, true, 0.0f);
	scene->Remove();
...
[/code]

-------------------------

cadaver | 2017-01-02 01:04:17 UTC | #2

Moving nodes from scene to another is not supported. The reason is that they would need to let go and re-acquire of global components like Octree & PhysicsWorld.

If you want to load prefabs, use Scene::InstantiateXML() function to load a node hierarchy you want directly into the correct scene.

-------------------------

practicing01 | 2017-01-02 01:04:17 UTC | #3

Thx for the quick reply.  I'm getting the console error: "Could not load Node, null source element"  when using the following code:
[code]
...
XMLFile* xmlFile = main_->cache_->GetResource<XMLFile>("Models/" + modelFilename + ".xml");
scene_->InstantiateXML(xmlFile->GetRoot(modelFilename), Vector3::ZERO, Quaternion(), LOCAL);
...
[/code]

-------------------------

cadaver | 2017-01-02 01:04:17 UTC | #4

Prefabs files should contain a root element of type "node", so a scene file is not directly usable. Easy way to convert is to load the scene in editor, select the node you want, and File -> Save Node as.

-------------------------

practicing01 | 2017-01-02 01:04:17 UTC | #5

Success! Thanks.

-------------------------

