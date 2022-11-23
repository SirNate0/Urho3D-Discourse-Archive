ab4daa | 2018-12-15 11:04:28 UTC | #1

Hi,

Today I figured out that when running application like sample 20_HugeObjectCount(toggle object moving and object group),
  the bottleneck of URHO3D_PROFILE(ReinsertToOctree) comes from StaticModelGroup::OnWorldBoundingBoxUpdate() in Drawable::GetWorldBoundingBox().

Maybe it could be updated multi-threaded?
I added the following in Octree.cpp
<pre><code>
void UpdateDrawablesBBWork(const WorkItem* item, unsigned threadIndex)
{
	Drawable** start = reinterpret_cast<Drawable**>(item->start_);
	Drawable** end = reinterpret_cast<Drawable**>(item->end_);

	while (start != end)
	{
		Drawable* drawable = *start;
		if (drawable)
			const BoundingBox& box = drawable->GetWorldBoundingBox();
		++start;
	}
}
...
void Octree::Update(const FrameInfo& frame)
{
...
// Reinsert drawables that have been moved or resized, or that have been newly added to the octree and do not sit inside
    // the proper octant yet
    if (!drawableUpdates_.Empty())
    {
        URHO3D_PROFILE(ReinsertToOctree);
    /*****parallel update world bounding box*****/
		WorkQueue* queue = GetSubsystem<WorkQueue>();
		int numWorkItems = queue->GetNumThreads() + 1; // Worker threads + main thread
		int drawablesPerItem = Max((int)(drawableUpdates_.Size() / numWorkItems), 1);
		PODVector<Drawable*>::Iterator start = drawableUpdates_.Begin();
		// Create a work item for each thread
		for (int i = 0; i < numWorkItems; ++i)
		{
			SharedPtr<WorkItem> item = queue->GetFreeItem();
			item->priority_ = M_MAX_UNSIGNED;
			item->workFunction_ = UpdateDrawablesBBWork;
			item->aux_ = NULL;

			PODVector<Drawable*>::Iterator end = drawableUpdates_.End();
			if (i < numWorkItems - 1 && end - start > drawablesPerItem)
				end = start + drawablesPerItem;

			item->start_ = &(*start);
			item->end_ = &(*end);
			queue->AddWorkItem(item);

			start = end;
		}

		queue->Complete(M_MAX_UNSIGNED);
 /*****end parallel update world bounding box*****/
        for (PODVector<Drawable*>::Iterator i = drawableUpdates_.Begin(); i != drawableUpdates_.End(); ++i)
        {
            Drawable* drawable = *i;
            drawable->updateQueued_ = false;
            Octant* octant = drawable->GetOctant();
            const BoundingBox& box = drawable->GetWorldBoundingBox();
...
}
</code></pre>

The result is satisfying, I got 113FPS => 133 FPS for sample 20_HugeObjectCount(toggle object moving and object group).
I ran some other samples, looks normal.
But I am unfamilier with engine code, I guess I should ask here whether this modification is valid.
Thanks!

-------------------------

Sinoid | 2018-12-12 19:19:12 UTC | #2

Looks valid to me. 

The threaded-updates already go before what you're doing so as far as I'm aware it's okay to be priming the bounds in the WorkQueue.

-------------------------

weitjong | 2018-12-14 14:39:01 UTC | #3

Would you mind to submit that as a PR, if you are OK to contribute that code.

-------------------------

ab4daa | 2018-12-14 17:00:39 UTC | #4

If the code helps, of course.
But I never make a pull request. haha

Would you mind to elaborate a bit about which branch to pull request, coding style..etc?
Thanks!

-------------------------

Modanung | 2018-12-14 19:33:31 UTC | #5

You can find the documentation on Urho's coding conventions [here](https://urho3d.github.io/documentation/HEAD/_coding_conventions.html). For pull requests it is common to create a new branch containing all the modifications.

-------------------------

ab4daa | 2018-12-15 03:03:00 UTC | #6

Thanks, I created my first pull request XD.

-------------------------

Sinoid | 2018-12-15 04:37:13 UTC | #7

Two comments:

#1)

            PODVector<Drawable*>::Iterator end = drawableUpdates_.End();
            if (i < numWorkItems - 1 && end - start > drawablesPerItem)
                end = start + drawablesPerItem;

Was there a reference you got that from, it's not the clearest thing. I get the intent but it took a bit of looking at it to see it.

#2)

For testing purposes (on your end, not in the actual final code) I'd add an assert on the WorkQueue's incomplete tasks right before you start filling it with your new code, just to be sure that the engine doesn't have anything going that could be in contention, ie. `assert(workQueue->IsComplete(0));` If that doesn't trigger on any of the samples than I think you're solid, user WorkQueue tasks are not Urho3D's responsibility - thus check samples only.

I did do this locally (but I'm very very out of date with master) and had nothing trip it.

---

This is a noticeable boost though on the garbage Intel HD4000 I tried your changes out. 17% is nothing to scoff at.

**Edit:** please examine more, a lot of us have worked with this code so long we're blind, fresh eyes catch so much, I wouldn't be surprised if you can find another boost the work-queue can bring that we'd miss. (do note though that threaded update already covers particles/animation/etc)

-------------------------

ab4daa | 2018-12-15 06:39:10 UTC | #8

Hi Sinoid,
#1)
You mean it is not so readable?

#2)
Thanks for the test method.
I added the assertion( assert(queue->IsCompleted(0)); ) 
and ran through samples (except some network related) in debug build of both github version and 1.7.

It is not triggered.

-------------------------

Sinoid | 2018-12-15 06:43:14 UTC | #9

Correct on #1, just would like some corroboration on that style as it's not very readable. I understood what you were doing, but I don't expect everyone to understand it. A comment could be enough.

#2: then I think you're genuinely good.

Nice work!

-------------------------

