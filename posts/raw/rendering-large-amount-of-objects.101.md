bobsod | 2017-01-02 00:58:00 UTC | #1

I've run into a problem that I just can't seem to figure out.

I make the ground out of hexagons that are based off a .mdl file that I just change the material of.

I started off with with a base plane that is not meant to be removable based off the HugeObjectCount tutorial(which was a great help!)

[code]	StaticModelGroup* hexagonsLastGrp = 0;

	if (!hexagonsLastGrp || hexagonsLastGrp->GetNumInstanceNodes() >= 50 * 50)
	{
		Node* hexPlane = scene_->CreateChild("hexPlane");
		hexagonsLastGrp = hexPlane->CreateComponent<StaticModelGroup>();
		hexagonsLastGrp->SetModel(cache_->GetResource<Model>("Models/SmallHex.mdl"));
		hexagonsLastGrp->SetMaterial(cache_->GetResource<Material>("Materials/Grass/Grass3.xml"));
	}
	const float testOff = sin(ang) * radius;

	for (int x = 0; x != 50; ++x)
	{

		for (int z = 0; z != 50; ++z)
		{

			float zPos = z * radius;

			if (x % 2 != 0)
			{
				zPos += testOff;
			}

			Node* hexFloorNode = scene_->CreateChild("hexPlaneNode");
			hexFloorNode->SetPosition(Vector3(x * height, 2.0f, zPos));
			hexNodes_.Push(SharedPtr<Node>(hexFloorNode));
			hexagonsLastGrp->AddInstanceNode(hexFloorNode);
		}
	}[/code]

I then added a plane of water above this.
At this point my fps sits around 200.

My next goal was to start adding the editable tiles above this, so I created another plane of hexs above the water using the same method as above, everything rendered fine and my fps was still 200.
But at this point, I realized that if I went to remove 1 individual hex, it would remove the entire plane.

[code]void GiveUp::RemoveHexagon()
{
	Vector3 hitPos;
	Drawable* hitDrawable;

	if (Raycast(250.0f, hitPos, hitDrawable))
	{
		Node* hitNode = hitDrawable->GetNode();
		if (hitNode->GetName() == "hexPlane")
		{
			hitNode->Remove();
		}
//

	}
}[/code]

I tried different methods of attempting to get the child of that plane at the mouse location, but couldn't seem to come up with anything that worked.

I then tried to build the plane without adding the hex's into a StaticModelGroup, this worked, and I could then remove a hexagon one at a time, but my fps at this point stood around 1-20, I assume because the amount of batches.

Does anyone know of a way to keep the calls low, while still being able to remove an individual model?

-------------------------

friesencr | 2017-01-02 00:58:00 UTC | #2

does this method help?  try that instead of the Remove.

StaticModelGroup#RemoveInstanceNode 

[urho3d.github.io/documentation/a ... 1981a50b35](http://urho3d.github.io/documentation/a00288.html#aa4a8b13095413c4e31dce41981a50b35)

-------------------------

bobsod | 2017-01-02 00:58:00 UTC | #3

That does seem like it would work, thank you.

The problem I'm running into trying to implement it, is the fact that "hexPlaneNode" never seems to get hit by the ray, all it ever returns is "hexPlane".  I'm not sure if I'm fully understanding how it all works, or maybe just overthinking it. 

[code]	Vector3 hitPos;
	Drawable* hitDrawable;
	Vector<SharedPtr<Node>> children_;
	StaticModelGroup* selTest;

	if (Raycast(250.0f, hitPos, hitDrawable))
	{
		Node* hitNode = hitDrawable->GetNode();
		if (hitNode->GetName() == "hexPlane")
		{
			selTest = hitNode->GetComponent<StaticModelGroup>();
			selTest->RemoveAllInstanceNodes();
		}


	}[/code]
Just to test, that correctly removes the entire plane.  If I try RemoveInstanceNode(hitNode) , it's a no go.  Since I couldn't call RemoveInstanceNode directly from hitNode, this was my method to extract the model group from it(bad?)

-------------------------

cadaver | 2017-01-02 00:58:00 UTC | #4

When your raycast hits a StaticModelGroup object, it will return its own scene node. The subObject_ variable of the result should tell the index of the instance node that was hit, you can then use StaticModelGroup::GetInstanceNode(index).

I hope you understand the implications to culling and lighting when using a StaticModelGroup (it basically acts like one huge object and the instances are not culled individually). You do not need to use StaticModelGroup to get the benefit of instancing, when you use opaque materials. What hardware are you running on, do you run in release mode? On a typical modern PC 50 x 50 objects should not yet necessitate using of StaticModelGroup.

However, if your objects have alpha materials and need to be sorted, your performance will suffer a lot sooner, and alpha-sorted objects also won't be instanced. In fact using StaticModelGroup with an alpha blend material will possibly produce incorrect results if the sorting is simply skipped (not sure about this, need to verify.)

-------------------------

bobsod | 2017-01-02 00:58:00 UTC | #5

Hardware:
AMD FX 8320
8G ddr3
radeon 7870
1x 128gb ssd, 3x 1tb HDD

I didn't have any fps issues creating the first 2 planes (50x50 hex and water) it was the 2nd hex plane ontop of those that would cause me to drop to well below 10 fps.

Image of both:
[img]https://imagizer.imageshack.us/v2/1024x768q90/560/wmwk.png[/img]

Only Base + water:
[img]https://imagizer.imageshack.us/v2/1024x768q90/849/sqkp.png[/img]

-------------------------

cadaver | 2017-01-02 00:58:00 UTC | #6

Do you have alpha blending in your materials? If you use the profiler, where does it show the most time being taken?

-------------------------

bobsod | 2017-01-02 00:58:00 UTC | #7

No, there is not any alpha blending in my materials, I'll have to wait until I get home to run the profiler

-------------------------

bobsod | 2017-01-02 00:58:00 UTC | #8

Hmm. ok I redid the plane this time without grouping....and everything works.

[code]	const float testOff = sin(ang) * radius;
	for (int x = 0; x != 50; ++x)
	{
		for (int z = 0; z != 50; z++)
		{
			float zPos = z * radius;

			if (x % 2 != 0)
			{
				zPos += testOff;
			}

			Node* hexPlaneNode = scene_->CreateChild("hexPlaneNode");
			hexPlaneNode->SetPosition(Vector3(x * height, 0.5, zPos));
			StaticModel* planeNode = hexPlaneNode->CreateComponent<StaticModel>();
			planeNode->SetModel(cache_->GetResource<Model>("Models/SmallHex.mdl"));
			planeNode->SetMaterial(cache_->GetResource<Material>("Materials/Grass/Grass3.xml"));
			
		}
	}[/code]


I guess I should of saved the old method to see what I was doing, but I know my batch count was in the 400k+'s, and now it stays under 10.

Everything working: 
[img]https://imagizer.imageshack.us/v2/1024x768q50/802/95i8.png[/img]
My fps now sits in the 100-150 range, I'm assuming thats ok for this amount?

I apologize, guess I should of messed around with things a bit before asking :slight_smile:

Thanks everyone!

-------------------------

cadaver | 2017-01-02 00:58:01 UTC | #9

You're OK at least for the moment, the time spent in UpdateViews is starting to creep up but it's not serious yet. You have reflective water, right? That essentially doubles the amount of objects and CPU processing required (once for the actual viewport, then for the reflection). You could play around with viewmasks to skip objects which don't actually contribute visibly to the reflection (the second hex layer?)

For example: let viewmask stay default (0xffffffff) on things that need to render both in the viewport and in the reflection.
Set viewmask to 0x80000000 for things that should *not* be rendered in the reflection.
Then set the reflection camera's viewmask to 0x7fffffff.

Also, if "Main_d" means running in Debug mode, by all means run in Release and outside the VS debugger for actual performance profiling. Even running Release inside the debugger will cause some CPU operations to be slower.

-------------------------

bobsod | 2017-01-02 00:58:01 UTC | #10

I didn't even think of the viewmask, thank you.  That dropped the update views down into the 6's

-------------------------

