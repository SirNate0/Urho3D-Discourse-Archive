codingmonkey | 2017-01-02 01:08:04 UTC | #1

if you want to debug your raycast, it's probably will be helpful

[code]
class MyApp : public Application
{
public:
    // accumulated red lines for debug renderer 
	PODVector<Pair< Vector3, Vector3>> lines;

    virtual void Start()
    {
		// Called after engine initialization. Setup application & subscribe to events here
		SubscribeToEvent(E_MOUSEBUTTONDOWN, URHO3D_HANDLER(MyApp, HandleMouseButtonDown));
		SubscribeToEvent(E_POSTRENDERUPDATE, URHO3D_HANDLER(MyApp, HandlePostRenderUpdate));
    }

	void HandleMouseButtonDown(StringHash eventType, VariantMap& eventData)
	{
		using namespace MouseButtonDown;
		int button = eventData[P_BUTTON].GetInt();

		Input* input = GetSubsystem<Input>();

		if (button == MOUSEB_LEFT) 
		{
			//do reacast
			ResourceCache* cache = GetSubsystem<ResourceCache>();

			Renderer* r = GetSubsystem<Renderer>();
			Viewport* vp = r->GetViewport(0);
			Camera* camera = vp->GetCamera();

			Ray ray = camera->GetScreenRay(0.5f, 0.5f);

			PODVector<RayQueryResult> results;
			RayOctreeQuery query(results, ray, RAY_TRIANGLE, 1000.0f, DRAWABLE_GEOMETRY, 1);			

			Octree* octree = gameScene->scene->GetComponent<Octree>();
			octree->RaycastSingle(query);
			//octree->Raycast(query);

			if (results.Size())
			{
				for (unsigned int i = 0; i < results.Size(); i++)
				{
					RayQueryResult& result = results[i];

					if (1)
					{
						Vector3 hitNormal = result.normal_;
						Vector3 hitPoint = result.position_;
						Node* hitNode = result.node_;
						
						// the "hitPrefab.xml" just node with StaticModel sphere
						Node* node = gameScene->scene->InstantiateXML(cache->GetResource<XMLFile>("Objects/hitPrefab.xml")->GetRoot(), hitPoint, Quaternion::IDENTITY, LOCAL);
						// donwscale little
						node->SetScale(Vector3::ONE * 0.2f);
                        
                        // buid new line from hit position oriented into worldspace by hitNormal
						Pair<Vector3, Vector3> line;
						line.first_ = hitPoint;
						line.second_ = hitPoint + hitNormal * 2.0f; // 2.0 is len of line
						lines.Push(line);
						break;
					}
				}
			}			
		}
	}
	
	void HandlePostRenderUpdate(StringHash eventType, VariantMap& eventData)
	{
		DebugRenderer* debug = gameScene->scene->GetOrCreateComponent<DebugRenderer>();
		
		for (int i = 0; i < lines.Size(); i++)
		{
			debug->AddLine(lines[i].first_, lines[i].second_, Color(1, 0, 0), false);
		}
		
	}

}	
[/code]

[spoiler][pastebin]uDmbEets[/pastebin][/spoiler]

-------------------------

sabotage3d | 2017-01-02 01:08:04 UTC | #2

thanks a lot :slight_smile:

-------------------------

