cap | 2017-01-02 01:06:03 UTC | #1

I'm trying to use Raycast on a Scene's Octree, and it's not behaving as I expected so I think I am confused about how to set things up properly.

I have triangle meshes to fill the scene and to do this I basically follow sample 34_DynamicGeometry to fill the vertex buffers, calculate normals, etc., of a Model from scratch and then add it as a StaticModel -- basically following 34_DynamicGeometry to the letter.

After the scene objects are loaded, here's an example of how we try a raycast:

Ray myRay = Ray(Vector3(0,0,-20), Vector3(0,1,0));
PODVector<RayQueryResult> results;
RayOctreeQuery query(results, myRay, RAY_TRIANGLE, 1000.0f, DRAWABLE_GEOMETRY);
scene_->GetComponent<Octree>()->Raycast(query);
std::cout << "manual ray cast number of results= " << results.Size() << std::endl;

When there is a triangle mesh surface directly above (in the y-direction and well within 1000.0f) this point, we're not finding any hits from the raycast. (And I'm pretty sure we're casting from the correct points and that things are where we think they are.) Occasionally we do find hits, for some reason more frequently from queries originating near the origin.

We've experimented with putting just one triangle directly above a query point. We've tried flipping the orientation of the face(s). There's something about the behaviour or the set up we are just not understanding.

Any tips? Rookie mistakes we should know about? Thanks,

cap.

-------------------------

cadaver | 2017-01-02 01:06:04 UTC | #2

Are you sure your model(s)' bounding boxes are set correctly? Does it work if you use Urho built-in models like Box.mdl? 

Also try checking out the Decals example, it uses octree raycasts to determine where to paint decals.

-------------------------

godan | 2017-01-02 01:06:04 UTC | #3

It turns out that you can't do a raycast query from the Start function of a class inheriting from Application.h. I'm not sure exactly why this is, but if you postpone the raycast until the app does a couple frames, the raycast works. I guess the octree is still initializing during the Application Start function.

-------------------------

cadaver | 2017-01-02 01:06:04 UTC | #4

Yes, that is absolutely true, the octree will update itself prior to rendering and will not reflect the object positions correctly for raycasts before. If necessary, you can call Octree::Update() manually. That function needs a frameinfo structure which is normally filled by Renderer but you should be able to just feed it dummy data.

-------------------------

godan | 2017-01-02 01:06:04 UTC | #5

Also, I've just noticed that you can't raycast against on Octree from a worker thread. Is there any possibility to work around this?

It seems that the error is thrown during Drawable::ProcessRayQuery and in particular the Drawable::GetWorldBoundingBox() function.

I know that add things to the Scene is not thread safe, but I had assumed reading properties of the scene would be ok.

-------------------------

cap | 2017-01-02 01:06:04 UTC | #6

Thanks, yes that was the problem, calling the raycasts in Start().

(Incidentally the Box.mdl models did show up with raycasts called from inside Start().)

-------------------------

cadaver | 2017-01-02 01:06:05 UTC | #7

Need to test the raycast from worker thread. I believe the problem is that it will create work tasks for speeding up the raycast, and doing that from a worker thread -> boom. A check for main thread can be added. But like you said you'll be responsible for your own synchronization.

-------------------------

cadaver | 2017-01-02 01:06:05 UTC | #8

Octree::Raycast() should now be possible to call from any thread; it only uses the WorkQueue itself when called from the main thread, outside of WorkQueue::Complete().

-------------------------

