Pihozamo | 2017-05-14 15:41:19 UTC | #1

Hello, I'm trying to create a sort of grid navmesh using raycasts, however, for some reason the raycast return false when it shouldn't. Here is the code:

    void Game::CreateNavigationGraph(const IntVector3& startPos)
    {
    	const Vector3 downVec(0, -1, 0);
    	const IntVector3 dirVecs[] = { IntVector3(1, 0, 0), IntVector3(-1, 0, 0), IntVector3(0, 0, 1), IntVector3(0, 0, -1) };
    	Drawable* hitDrawable;

    	HashSet<IntVector3> visited;
    	HashSet<IntVector3> onStack;
    	Vector<IntVector3> ar;
    	Vector<Vector3> hitPoints;
    	ar.Push(startPos);

    	while (!ar.Empty()) {
    		Vector3 hitPos;
    		const IntVector3 v = ar.Back();
    		ar.Pop();
    		onStack.Erase(v);

    		if (Raycast(100.0f, hitPos, hitDrawable, Ray(Vector3(v), downVec))) {
    			for (int i = 0; i < 4; i++) {
    				const IntVector3 v2 = v + dirVecs[i];

    				if (!visited.Contains(v2) && !onStack.Contains(v2)) {
    					ar.Push(v2);
    					onStack.Insert(v2);
    					//Log::Write(LOG_INFO, String(v2));
    				}
    			}
    			hitPoints.Push(hitPos);
    		}
    		visited.Insert(v);
    	}

    	//Log::Write(LOG_INFO, String(hitPoints.Size()));
    	for (int i = 0; i < hitPoints.Size(); i++) {
    		ResourceCache* cache = GetSubsystem<ResourceCache>();
    		Node* n = scene_->CreateChild("Cube");
    		n->SetPosition(hitPoints[i]);
    		n->SetScale(Vector3(0.2f, 0.2f, 0.2f));
    		StaticModel* model = n->CreateComponent<StaticModel>();
    		model->SetModel(cache->GetResource<Model>("Models/Cube.mdl"));
    		model->SetCastShadows(true);
    		//Log::Write(LOG_INFO, String(hitPoints[i]));
    	}
    }

For the Raycast function:

    bool Gourmet::Raycast(const float& maxDistance, Vector3& hitPos, Drawable*& hitDrawable, const Ray& ray)
    {
    	hitDrawable = 0;

    	// Pick only geometry objects, not eg. zones or lights, only get the first (closest) hit
    	PODVector<RayQueryResult> results;
    	RayOctreeQuery query(results, ray, RAY_TRIANGLE, maxDistance, DRAWABLE_GEOMETRY);
    	scene_->GetComponent<Octree>()->RaycastSingle(query);
    	if (results.Size())
    	{
    		RayQueryResult& result = results[0];
    		hitPos = result.position_;
    		hitDrawable = result.drawable_;
    		return true;
    	}

    	return false;
    }

I've made sure I applied the scale, position and location of my plane model on Blender, and I'm not sure why it doesn't work. It seems to me that it maybe some type of optimization made by the Octree, because it seems that it stops working after a certain distance.

-------------------------

slapin | 2017-05-14 01:26:41 UTC | #2

When I had problems like this, moving such code into FixedUpdate and waiting a few seconds before starting of raycast did the trick.

-------------------------

lezak | 2017-05-14 15:40:43 UTC | #3

[quote="Pihozamo, post:1, topic:3125"]
It seems to me that it maybe some type of optimization made by the Octree, because it seems that it stops working after a certain distance.
[/quote]

Instead of using octree raycast try to use Drawable::ProcessRayQuery on your model

-------------------------

Pihozamo | 2017-05-14 12:35:24 UTC | #4

@lezak That solved the problem! But do you know why the Octree doesn't apply raycasts after a certain block distance?

-------------------------

lezak | 2017-05-14 22:35:02 UTC | #5

I came across same issue just few days ago and since then I havn't had time to look into it closers. I think that it is caused, at least in my case, by model being bigger then octant in which it is placed and octree raycast takes into account only geometries that fit this octant. For example after decreasing number of subdivisions in octree raycast will also give expected results.

-------------------------

