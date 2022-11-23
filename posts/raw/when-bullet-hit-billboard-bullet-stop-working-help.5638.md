Elendil | 2019-10-01 20:46:11 UTC | #1

My bullet (not bullet physics) working ok when bullet hit box. But I have above box billboard to show HP and if bullet hit billboard and then my box, it stop working and bullet is going away and don't care about my box.

It even doesnt work when bullet fly throught billboard on scene which have not any connections with my object.

I have no clue where can be problem.

This is code how I create object inside GameApp

    			Node* boxNode_ = scene_->CreateChild("Box");
    			boxNode_->SetPosition(Vector3(x, -3, z));
    			boxNode_->SetScale(Vector3(2, 2, 2));
    			MyCube * mc = boxNode_->CreateComponent<MyCube>();
    			mc->CreateObject(boxNode_, cache);

---
My custom object

    void Urho3D::MyCube::CreateObject(Node * node, ResourceCache * cache)
    {
    	m_node = node;
    	Node * node_model = m_node->CreateChild("MyCube");
    	m_model = node_model->CreateComponent<StaticModel>();
    	// ...

    	// billboard
    	// ...
    	m_node_billboard = m_node->CreateChild("HealthBar");
    	m_node_billboard->SetPosition(Vector3(0, 0.8, 0));
    	m_bs = m_node_billboard->CreateComponent<BillboardSet>();
    	m_bs->SetNumBillboards(1);
    	// ...
    	m_bs->Commit();

    	// ...
    }
---
And here is my bullet code

    void Urho3D::MyBullet::mf_Update(StringHash eventType, VariantMap & eventData)
    {
    	if (myBulletNode != nullptr && myBulletScene != nullptr && m_STOP == false)
    	{
    		Vector3 hitPos;
    		Drawable* hitDrawable;
    		float timeStep = eventData[Update::P_TIMESTEP].GetFloat();

    		if (Raycast((float)(m_Speed*timeStep), hitPos, hitDrawable))
    		{
    			Node* hitNode = hitDrawable->GetNode();
    			if (hitNode->GetName() == "MyCube")
    			{
    				MyCube * myCube = hitNode->GetParentComponent<MyCube>();
    				if (myCube != nullptr)
    				{
    					myCube->mf_ISetDamage(m_damage);
    					m_STOP = true;
    				}
    			}
    		}
    		myBulletNode->Translate(Vector3(0, 0, 1) * m_Speed * timeStep);
    	}
    	if (m_STOP == true)
    	{
    		myBulletNode->Remove();
    	}
    }

    bool Urho3D::MyBullet::Raycast(float maxDistance, Vector3 & hitPos, Drawable *& object)
    {
    	object = 0;
    	if (myBulletNode == nullptr || myBulletScene == nullptr)
    		return false;

    	Graphics * graphics = GetSubsystem<Graphics>();

    	Ray ray(myBulletNode->GetPosition(), myBulletNode->GetDirection());

    	PODVector<RayQueryResult> results;
    	RayOctreeQuery query(results, ray, RAY_TRIANGLE, maxDistance, DRAWABLE_GEOMETRY);

    	myBulletScene->GetComponent<Octree>()->RaycastSingle(query);

    	if (results.Size())
    	{
    		RayQueryResult& result = results[0];
    		hitPos = result.position_;
    		object = result.drawable_;
    		return true;
    	}
    	return false;
    }

-------------------------

Modanung | 2019-10-01 22:10:04 UTC | #2

Have you tried inserting some `assert`s and `Log::Write` to diagnose your problem?

-------------------------

SirNate0 | 2019-10-02 05:35:35 UTC | #3

You seem to be selecting the first result from the raycast, which will hit the billboard if you leave the default view masks for the raycast and the billboard. If you still looking want to not hit the billboard, consider removing a bit from the view mask and checking that bit with the raycast.

If that isn't the problem your facing could you clarify what the issue is? How does it not work? How is the bullet going away?

-------------------------

Elendil | 2019-10-02 17:48:00 UTC | #4

[quote="SirNate0, post:3, topic:5638"]
You seem to be selecting the first result from the raycast, which will hit the billboard if you leave the default view masks for the raycast and the billboard.
[/quote]
This is my problem. Billboard have some "sphere" area and if bullet is in this sphere area it detect allways billboard instead box.

I forgot about this: `myBulletScene->GetComponent<Octree>()->RaycastSingle(query);`
and changing it to `this myBulletScene->GetComponent<Octree>()->Raycast(query);`
after that I can collect hits and ignore billboards.


[quote="SirNate0, post:3, topic:5638"]
If you still looking want to not hit the billboard, consider removing a bit from the view mask and checking that bit with the raycast.
[/quote]
I quite not understand this, can you please explain it more?

-------------------------

SirNate0 | 2019-10-02 17:48:00 UTC | #5

All drawables have a [viewmask](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_drawable.html#ab0a0cb81cefb83249a578069c4adc4d8) that is &'ed with the [RayOctreeQuery::viewMask_](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_ray_octree_query.html#a960e05dc69a509ef726fffe9137ccd5d) to check if the drawable should be allowed to be hit. If you set the viewmask of your hp bar to be, for example `~1` and then raycast against `1` and then the hp bars will be excluded from the raycast. I believe the default viewmask is `0xffffffff` (maybe twice the width for 64 bit), so that should leave the remaining drawables unaffected (i.e. you will still hit the box).

-------------------------

Elendil | 2019-10-02 17:47:46 UTC | #6

Thanks, I tried change ViewMask for my billboard. It works.

But I still don't understand how it works. Because my box still get hits from raycast (this is ok, just want understand it now). That means, all created drawable objects have some default viewmask value which are allways query in raycast, even if I raycast with specific value? `RayOctreeQuery query(results, ray, RAY_TRIANGLE, maxDistance, DRAWABLE_GEOMETRY, 1);` 
1 = specific raycast value for viewmask. Billboard have value 2 for viewmask. I can swap the values (1 for billboards and 2 for raycast) and billboard will be excluded.

-------------------------

SirNate0 | 2019-10-02 19:00:09 UTC | #7

If I'm not mistaken, how it works is that every drawable has an integer's worth of bits (say 32 for our purposes) that act sort of like a set of different groups the drawable can belong to. By default, every drawable belongs to every available group. By setting the view mask in the drawable, you can change the groups it is a member of (so setting the view mask to 1 would give it membership only in group 0 (1<<0), setting it to 2 would make it only a member of group 1, setting it to 3=1|2 would give it membership in groups 0 and 1, etc.). The view mask in the raycast query works the same way, but it selects which groups are checked. If an object is in any single group that is being queried (i.e. object.viewmask_ & query.viewmask_ != 0), the raycast can hit that object.

-------------------------

