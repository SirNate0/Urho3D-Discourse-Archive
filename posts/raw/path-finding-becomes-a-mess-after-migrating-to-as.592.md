rogerdv | 2017-01-02 01:01:34 UTC | #1

I succesfully implemented character movement in my proyect a few days ago, yesterday, I was trying to migrate the code to AngeScript, but it doesnt works. The character moves just in a slightly approximate direction to the click point and goes beyond it. 
Here is my code:

[code]
navMesh = gameScene.GetComponent("NavigationMesh");
if (input.mouseButtonPress[MOUSEB_LEFT]){
			IntVector2 pos = input.mousePosition;
			Ray cameraRay = cam.gameCamera.GetScreenRay(pos.x / graphics.width, pos.y / graphics.height);
			RayQueryResult result = gameScene.octree.RaycastSingle(cameraRay, RAY_TRIANGLE, 300, DRAWABLE_GEOMETRY);
			if (result.drawable !is null)	{
        Vector3 hitPos = result.position;
				Vector3 pathPos = navMesh.FindNearestPoint(hitPos, Vector3(1.0f, 1.0f, 1.0f));
				player.MoveTo(navMesh, pathPos);
			}
		}
[/code]

Character update function:

[code]	void Update(float timeStep)
	{
		if (currentPath.length > 0) {
			animCtrl.PlayExclusive("Models/Jack_Walk.ani",0,true);
			Vector3 nextWaypoint = currentPath[0]; // NB: currentPath[0] is the next waypoint in order

      // Rotate Jack toward next waypoint to reach and move. Check for not overshooting the target
      float move = 4.0f * timeStep;
			float distance = (node.position - nextWaypoint).length;
        if (move > distance)
            move = distance;

        node.LookAt(nextWaypoint, Vector3(0.0f, 1.0f, 0.0f));
        node.Translate(Vector3(0.0f, 0.0f, 1.0f) * move);

        // Remove waypoint if reached it
        if ((node.position - nextWaypoint).length < 0.1)
            currentPath.Erase(0);
    }

	}[/code]

The navigation mesh is generated in the editor. I ported to AS from my C++ code using AS skeletal sample as guide, but seems I missed something here.

-------------------------

Mike | 2017-01-02 01:01:34 UTC | #2

Your player.MoveTo() function may conflict with node.Translate in Update().

-------------------------

rogerdv | 2017-01-02 01:01:34 UTC | #3

Hmm, Update is supposed to be called every frame and displace character if there is a path. MoveTo is called when player clicks and takes care of generating the path, should not be called more unless player clicks again.

-------------------------

Mike | 2017-01-02 01:01:34 UTC | #4

Did you check with debug geometry (navMesh.DrawDebugGeometry(true);) if your destination and path are OK?

-------------------------

rogerdv | 2017-01-02 01:01:34 UTC | #5

I did now, and seems to be ok, sane as displayed in editor. I also noticed something, while the character is moving, clicks are ignored. It seems like the navmesh is fine, but the click coordinates are the ones causing the problem.

-------------------------

rogerdv | 2017-01-02 01:01:35 UTC | #6

You are a genius. Indeed, in the C++ code there is a (float) cast, but I removed it because I didnt knew the syntax in AS. And seems that it was in fron of my eyes, there in the sample. Now it works perfectly. Thanks a lot.

-------------------------

