sabotage3d | 2017-01-02 01:01:24 UTC | #1

Hi ,

Is it currently possible to raycast while a rigid body is moving. I am trying to predict impact point . And that's the only method I can think of. 


Thanks in advance,

Alex

-------------------------

codingmonkey | 2017-01-02 01:01:25 UTC | #2

Do you mean this Raycasting ? You will need two things to do this: 1 - vector - start world position point and 2. - direction, for build ray. Then you should perform raycast query and call octree->RaycastSingle(query); it write hits if its has been to PODVector<RayQueryResult> results;
 
[code]	float maxDistance = 100.0f;
	Ray Ray = Ray(position, direction)

	// Pick only geometry objects, not eg. zones or lights, only get the first (closest) hit
	PODVector<RayQueryResult> results;
	RayOctreeQuery query(results, Ray, RAY_TRIANGLE, maxDistance, DRAWABLE_GEOMETRY, -1);
	Octree* octree = scene_->GetComponent<Octree>();
	octree->RaycastSingle(query);
	
	if (results.Size())
	{
		RayQueryResult& result = results[0];
		hitPos = result.position_;
		hitDrawable = result.drawable_;
		return true;
	}

	return false;[/code]

-------------------------

sabotage3d | 2017-01-02 01:01:25 UTC | #3

Thanks, but I am trying to query a moving rigid body. Send a ray from the rigid body's centroid use the velocity  as direction of the toward a passive body so that I can predict the impact.
The question is can I can query velocity and centroid of moving rigid body ?

-------------------------

Azalrion | 2017-01-02 01:01:26 UTC | #4

Centroid per say is not calculated, closest available is RigidBody::GetCenterOfMass. Direction wise RigidBody also provides GetLinearVelocity and GetAngularVelocity and Node provides GetWorldDirection providing the forward direction updated by the RigidBody movement.

-------------------------

sabotage3d | 2017-01-02 01:01:26 UTC | #5

Thanks these will be useful.

-------------------------

