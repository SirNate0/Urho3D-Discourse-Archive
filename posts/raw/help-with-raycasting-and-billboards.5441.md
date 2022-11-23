codexhound | 2019-08-09 23:24:05 UTC | #1

So I have a billboard that overlaps some of my models and I want to be able to handle clicks on only the models. The ray-cast query I have right now only gets results of the top level, meaning if the model is overlapping with the billboard space, it isn't in the ray-cast results. I have set the billboards occluder and occludee properties to false but still I can't see the clicks for the model. When a billboard does not overlap the model is in the results. Is there something I'm missing?

 
     RayOctreeQuery query(results, cameraRay, RAY_TRIANGLE, maxDistance, DRAWABLE_GEOMETRY);
                scene_->GetComponent<Octree>()->RaycastSingle(query);
	        std::cout << "Query Size: " << results.Size() << std::endl;
	if (results.Size())
	{
		for (int i = 0; i < results.Size(); i++) {
			//find models in the ray results, don't want anything else for now
			RayQueryResult& result = results[i];
			auto * currentDrawable = result.drawable_;
			StaticModel* model = dynamic_cast<StaticModel*>(currentDrawable);
			if (model != nullptr) {
				hitPos = result.position_;
				hitDrawable = result.drawable_;
				return true;
			}
		}
	}

The code above always returns 1 result, and it's either the model (if it wasn't being overlapped) or the billboard.

-------------------------

lezak | 2019-08-09 23:24:13 UTC | #2

1. Change viewlayer (make shure that camera has proper mask set, so it still be visible) for billboard or model (in this case make sure that You're using proper view mask for raycast).
2. Use Octree:Raycast instead of RaycastSingle

-------------------------

codexhound | 2019-08-09 22:52:09 UTC | #3

Ahh, the RaycastSingle function call was the problem. Thanks

-------------------------

