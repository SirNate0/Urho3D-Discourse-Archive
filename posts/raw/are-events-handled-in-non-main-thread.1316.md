TikariSakari | 2017-01-02 01:06:46 UTC | #1

Are events handled in non main thread, because I am initializing a scene in one and if I reinit the same scene by loading from xml-file, there is a high chance that it will crash somehow. It might actually lose textures etc.

Basicly I am doing something like this:
[code]

	// clear old map, remove children
	Urho3D::Node* sceneNode = scene_->GetChild("scene", true);
	if (sceneNode)
		sceneNode->GetParent()->RemoveAllChildren();


	ResourceCache* cache = GetSubsystem<ResourceCache>();

	// Technically add same nodes from xml-file.
	XMLFile* file = cache->GetResource<XMLFile>("newmap.xml");
	scene_->InstantiateXML(file->GetRoot("scene"), Urho3D::Vector3::ZERO, Quaternion());

	map_->GenerateMapFromScene(scene_->GetChild("Map", true));
[/code]

Also inside generatemap, I am going through the vertexbuffer-data. The resourcecache might somehow cause some weirdness when I am deleting stuff from scene, and basically instantly adding same stuff few lines later, which is not that good idea. Anyways I will try to isolate the crash a bit better tomorrow and hopefully manage to reproduce it with smaller amount of code. It could just be my horrible spaghetti code somewhere leaking memory/pointers pointing to unreached memory and causing tons of problems. 

I am not even sure which systems are using extra threads, but it seems the crashes are mostly happening from worker threads, . Also the problem is, that this doesn't happen on every execution, it just sometimes happens or crashes in various ways.

-------------------------

cadaver | 2017-01-02 01:06:47 UTC | #2

If you don't especially request it by using the async scene load functionality, the resources aren't loaded threaded.

Crashes in the worker threads could however easily appear during scene rendering, if the scene has become corrupt, e.g. dangling pointers to deleted objects, and the rendering preparations executed on the WorkQueue, like culling, tries to access these objects. Another reason would be the scene being modified (objects being deleted) after rendering preparation (E_RENDERUPDATE event) but before rendering, in which case the scene isn't actually corrupt, but the rendering preparation data structures contain stale pointers.

You can try the -nothreads command line option to disable workers, however then I suspect you'll get the same crash(es) in the main thread.

-------------------------

TikariSakari | 2017-01-02 01:06:48 UTC | #3

I think I found the issue, and indeed it is me completely derping with the instancing of xml. I exported blender scene by assetimporter and this one creates node that has an attribute name called "Scene" and I was loading <scene> -objects from xml. Basically I only wanted to instantiate the node that had attribute name "Scene" and sub nodes of it. Since it always instanced whole xml-file into already existing scene, I had multiple debugrenderer and octree components in the scene. So it is no wonder something odd might happen.

Interestingly enough retrospective, I think ive had this for very long time (probably since the beginning of my project), but it only started crashing when I tried to change levels, aka delete old stuff and load new.

-------------------------

