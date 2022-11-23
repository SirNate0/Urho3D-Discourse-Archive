practicing01 | 2017-01-02 01:04:02 UTC | #1

Edit: Solved since merging latest master.

Hello, I'm calling Raycast() twice, the first time is fine, the second it crashes.  The first time is with one scene, the second with a different scene.  I don't think the second scene has problems because if I cast the first time with the second scene it doesn't crash.  Relavent snippets:

Variable init stuff:

[code]
...

	//Load scene.

	main_->cameraNode_->RemoveAllChildren();
	main_->cameraNode_->RemoveAllComponents();
	main_->cameraNode_->Remove();

	File loadFile(context_,main->filesystem_->GetProgramDir()
			+ "Data/Scenes/solcommCity.xml", FILE_READ);
	main_->scene_->LoadXML(loadFile);

	main_->cameraNode_ = main_->scene_->GetChild("RavenMech")->GetChild("camera");
	main_->viewport_->SetCamera(main_->cameraNode_->GetComponent<Camera>());

	//Load moveButt scene.

	scene_ = new Scene(main_->GetContext());
	cameraNode_ = new Node(main_->GetContext());

	File loadFile2(context_,main->filesystem_->GetProgramDir()
			+ "Data/Scenes/moveButts.xml", FILE_READ);
	scene_->LoadXML(loadFile2);

	cameraNode_ = scene_->GetChild("camera");
...
[/code]

crash happens below:

[code]
...
	Ray cameraRay = cameraNode_->GetComponent<Camera>()->GetScreenRay(
			(float) eventData[P_X].GetInt() / main_->graphics_->GetWidth(),
			(float) eventData[P_Y].GetInt() / main_->graphics_->GetHeight());

	PODVector<RayQueryResult> results;

	RayOctreeQuery query(results, cameraRay, RAY_TRIANGLE, 1000.0f,
			DRAWABLE_GEOMETRY);

	scene_->GetComponent<Octree>()->Raycast(query);
...
results.Clear();
	cameraRay = main_->cameraNode_->GetComponent<Camera>()->GetScreenRay(
				(float) eventData[P_X].GetInt() / main_->graphics_->GetWidth(),
				(float) eventData[P_Y].GetInt() / main_->graphics_->GetHeight());
	query.ray_ = cameraRay;
	main_->scene_->GetComponent<Octree>()->Raycast(query); //CRASH
...
[/code]

-------------------------

cadaver | 2017-01-02 01:04:02 UTC | #2

Where exactly does it crash? (you may need to run in debug mode)

Does it still crash if you disable worker threads? (-nothreads command line option, or engine startup parameter WorkerThreads = false)

-------------------------

practicing01 | 2017-01-02 01:04:02 UTC | #3

engineParameters_["WorkerThreads"] = false; didn't work.  It crashes at main_->scene_->GetComponent<Octree>()->Raycast(query); //CRASH

-------------------------

franck22000 | 2017-01-02 01:04:02 UTC | #4

Have you created an octree component in the scene root ?

Like so for example:

[code]Octree* _SceneOctree = _SceneNode->CreateComponent<Octree>();[/code]

-------------------------

practicing01 | 2017-01-02 01:04:03 UTC | #5

Yep.

-------------------------

cadaver | 2017-01-02 01:04:03 UTC | #6

If that's the exact point of crash, and not some function inside the Octree class, then I recommend nullchecking the whole chain of objects you're accessing. Has something caused the Octree to be destroyed at the point when you call Raycast?

-------------------------

practicing01 | 2017-01-02 01:04:03 UTC | #7

I'm not touching the octree, the only things I'm modifying are on the lines "results.Clear();" , "cameraRay = ..." and "query.ray_ = cameraRay;" . gdb backtrace: [pastebin.com/NZ7jtp0H](http://pastebin.com/NZ7jtp0H)

[code]
Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0xb795db40 (LWP 2397)]
0x08521ffc in Urho3D::Renderer2D::ProcessRayQuery(Urho3D::RayOctreeQuery const&, Urho3D::PODVector<Urho3D::RayQueryResult>&) ()
(gdb) backtrace
#0  0x08521ffc in Urho3D::Renderer2D::ProcessRayQuery(Urho3D::RayOctreeQuery const&, Urho3D::PODVector<Urho3D::RayQueryResult>&) ()
#1  0x08215085 in Urho3D::RaycastDrawablesWork(Urho3D::WorkItem const*, unsigned int) ()
#2  0x08401350 in Urho3D::WorkQueue::ProcessItems(unsigned int) ()
#3  0x08402b6f in Urho3D::WorkerThread::ThreadFunction() ()
#4  0x081f9ecf in Urho3D::ThreadFunctionStatic(void*) ()
#5  0xb7fa4f70 in start_thread () from /lib/i386-linux-gnu/libpthread.so.0
#6  0xb7ce8bee in clone () from /lib/i386-linux-gnu/libc.so.6
[/code]

-------------------------

cadaver | 2017-01-02 01:04:03 UTC | #8

Renderer2D is the component that handles the collective rendering and raycasting for Urho2D drawables. Do you have 2D sprites in your scene, and do you manipulate them (disable/enable them, or remove from the scene) before the raycast? There can be issues with managing the drawable list in the Renderer2D code: possible double-addition etc.

The ideal would be if you can make a reproduction case that uses nothing but Urho built-in assets and submit as a github issue.

-------------------------

practicing01 | 2017-01-02 01:04:04 UTC | #9

Yes I have a 2d sprite in the middle of the screen (the player).  Disabling before the raycast and re-enabling after the raycast stopped the crash.  This is a problem because I plan on having hundreds of sprites onscreen and can't be doing that then.

-------------------------

cadaver | 2017-01-02 01:04:04 UTC | #10

I committed a possible null exception fix in the master branch (Drawable2D material may be null and used in sorting before it's assigned by frame update.) Check if that fixes the issue.

-------------------------

practicing01 | 2017-01-02 01:04:04 UTC | #11

Thanks, I don't know what magical spell you cast but after merging with the latest master, no more crash.  If this issue pops up again, I'll update the thread.

-------------------------

