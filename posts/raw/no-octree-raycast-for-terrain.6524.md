grokko | 2020-11-14 09:03:14 UTC | #1

Could you show me a quick positive Raycast to an Octree Component Terrain Node *?
My raycasts work for other creatures('n' of them') but never for the Terrain...
MS

    indent preformatted text by 4 spaces
    if(diffTime>dalekI->firingTime) {					
					Vector3 myPos = -dalekI->getNode()->GetPosition();
					Vector3 dir = cameraNode_->GetPosition() + myPos;
					dir.Normalize();
					dalekI->ray1 = Ray(myPos, dir);
					PODVector<RayQueryResult> results;
					RayOctreeQuery query(results, dalekI->ray1, RAY_TRIANGLE, 2000, DRAWABLE_GEOMETRY);
					scene_->GetComponent<Octree>()->RaycastSingle(query);
					if (results.Size()) {
						RayQueryResult& result = results[0];			
						Node * hit = result.node_;
						if((Node *)terrainNode == hit) {
							dalekI->boolShot = false;
							logMe2("DALEK FIRED at terrainB!!!!", i, i);
						} else {
							dalekI->boolShot = true;
							logMe2("DALEK didn't FIRED at terrainB!!!!", i, i);
						}
					} else {
						dalekI->boolShot = true;
					}
					if(dalekI->boolShot) makeMeAnotherMissile(dalekI, scene_, i);
					lastTime = nowTime;
					dalekI->firingTime = (rand() % 4000) + 2000;		 						
					((CDalek *)dalekI)->myTimer->Reset();

> Blockquote

-------------------------

Eugene | 2020-11-14 07:53:37 UTC | #2

Please format code properly.
Also, what do you mean by “doesn’t work”?

-------------------------

grokko | 2020-11-14 18:45:57 UTC | #3

Hi Everyone!
  I was able to get around the situation by 1) ray testing for CameraNode, and, 2) only firing the shot if the query detects the camera. This way, I don't get bullets flying through the Terrain...! Neat!

Lord Fiction

-------------------------

Eugene | 2020-11-14 19:05:11 UTC | #4

[quote="grokko, post:1, topic:6524"]
`if((Node *)terrainNode == hit)`
[/quote]
I think the issue is here. Terrain is not a geometry, therefore it cannot be returned from octree query.
You may get one of terrain patches tho.

-------------------------

