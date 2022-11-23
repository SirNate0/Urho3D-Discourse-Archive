GodMan | 2020-03-24 02:32:35 UTC | #1

So I'm having trouble deciding the best way for my npc's to check if the player is within a bounding radius for deciding to melee the player.

    void AIMelee::boundingSphere(StringHash eventType, VariantMap& eventData)
    {
    	Sphere boundingRadius(node_->GetWorldPosition() + Vector3(0, 1.0f, 0), 1.5f);
    	debug = scene_->GetComponent<DebugRenderer>();

    	i = boundingRadius.IsInside(scene_->GetChild("AdjNode", true)->GetWorldPosition());

    	if (i == INSIDE)
    	{
    		oktoMelee_ = true;
    	}
    }

I'm looking for something with the best performance. No need to constantly check. My ideas turned into crap.

-------------------------

WangKai | 2020-03-24 03:52:13 UTC | #2

```
boundingRadius.IsInside()
```
is very cheap. If you don't have thousands of NPCs, I don't see there is need to optimize.

You can cache the values you use in `boundingSphere`, update them and reuse, so it would be a little faster.

-------------------------

Modanung | 2020-03-24 10:28:50 UTC | #3

What event are you subscribing to?
Using `FixedUpdate` instead of `Update` for artificial thoughts should be more performant.

Also note there's an `IsInsideFast` function which skips the _intersects_ check.

-------------------------

GodMan | 2020-03-24 20:33:38 UTC | #4

So this is what I am doing. What can I improve?

    //AIMelee.cpp
    void AIMelee::FixedUpdate(float timeStep)
    {
    	CrowdAgent* agent = node_->GetComponent<CrowdAgent>();

    	if (health <= 0 && dead_ == false)
    	{
    		PlaySound("Sounds/death_mjr.ogg",1.5f,50.0f,70.0f);
    		idle->PlayExclusive("Models/hunter_combat_landing_dead.ani", 0, false, 0.3f); .

    		if (node_->HasComponent<CrowdAgent>())
    		{
    			agent->Remove();
    		}
    		shape->SetCapsule(10.0f, 5.0f, Vector3(0.0f, 5.0f, 0.0f));
    		body->SetMass(0);
    		dead_ = true;
    	}
        // This is our check to see if player is within radius to attack
    	boundingSphere();
    }



        // AIMelee.h
    	/// Handle scene update. Called by LogicComponent base class.
    	void Update(float timeStep)
    	{

    		elapsedTime_ += timeStep;



    		// Disappear when duration expired
    		if (duration_ >= 0 && dead_ == true)
    		{
    			duration_ -= timeStep;
    			if (duration_ <= 0)
    			{
    				node_->Remove();
    			}
    		}

    		if (oktoMelee_ == true)
    		{
                     // If melee is true from boundingSphere(); 
    			melee();
    		}
    	}




    //AIMelee.cpp
    void AIMelee::melee()
    {

    	debug = scene_->GetComponent<DebugRenderer>();

    	CollisionShape* shape_ = handboneNode->CreateComponent<CollisionShape>();
    	shape_->SetCapsule(2.0f, 2.0f, Vector3::ZERO, Quaternion::IDENTITY);

    	PhysicsRaycastResult raycResult;
    	auto* physicsWorld = scene_->GetComponent<PhysicsWorld>();

    	const Vector3 start = handboneNode->GetWorldPosition();
    	const Vector3 end = start + (Vector3::FORWARD * 100.0f);

    	idle->Play("Models/hunter_combat_melee%1.ani", 0, false, 0.2f);

    	physicsWorld->ConvexCast(raycResult, shape_, start, Quaternion::IDENTITY, end, Quaternion::IDENTITY);

    	RigidBody* resultBody{ raycResult.body_ };
    	Character* _Node;
    	int damage = 15;

    	if (resultBody)
    	{

    		Node* resultNode{ resultBody->GetNode() };

    		if (_Node = resultNode->GetDerivedComponent<Character>())
    		{
    			_Node->setHealth(_Node->getHealth() - damage);
    			resultBody->ApplyImpulse(Vector3(1.0f, 1.0f, 1.0f)* 1.0f);
    		}

    	}
    }

-------------------------

QBkGames | 2020-03-27 09:27:56 UTC | #5

If you have one player and lots of enemies, there may be one optimization you can do (a technique I use in my game "Planetoid Escape"). Instead of having each enemy query the world state to see if the player is in range, have the player query the world, (i.e. do the bounding sphere check) and broadcast its location to all enemies within range. This way you reduce the possible 10s or 100s of bounding sphere checks per frame to just one.

If different enemies have different ranges, just do the bounds with the largest radius and then each enemy still has to check if the the player is in range when getting the position message from the player, but avoids doing the bounds check (which should be more expensive).

I haven't done thorough performance gain investigation of this technique, but in theory it should be an improvement.

-------------------------

George1 | 2020-03-26 01:19:05 UTC | #6

If you have two player or 10 players then it will be different.

The implementation then be different.   Each Mob need to keep a list of sorted distance so that he can chase the closest player.   The mob can be more intelligent.

-------------------------

