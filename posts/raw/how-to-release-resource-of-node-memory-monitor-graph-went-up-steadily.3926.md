ab4daa | 2018-01-09 15:03:44 UTC | #1

Sorry for the basic question... but I cannot figure out.

In 1.7 release source code sample 20_HugeObjectCount, I add following code in HugeObjectCount::HandleUpdate() to remove and add nodes every 3 seconds at runtime.
My environment is win7+vs 2017 community +x64
<pre><code>{//test
	static float accTime = 0.0f;
	accTime += timeStep;
	if (accTime >= 3.0f)
	{
		accTime = 0.0f;
		ResourceCache* cache = GetSubsystem&lt;ResourceCache>();
		if (!useGroups_)
		{
			/*remove boxes*/
			while( boxNodes_.Size())
			{
				SharedPtr&lt;Node> n = boxNodes_.Back();
				boxNodes_.Pop();
				n->Remove();
			}

			/*add back boxes*/
			// Create individual box StaticModels in the scene
			for (int y = -125; y < 125; ++y)
			{
				for (int x = -125; x < 125; ++x)
				{
					Node* boxNode = scene_->CreateChild("Box");
					boxNode->SetPosition(Vector3(x * 0.3f, 0.0f, y * 0.3f));
					boxNode->SetScale(0.25f);
					StaticModel* boxObject = boxNode->CreateComponent&lt;StaticModel>();
					boxObject->SetModel(cache->GetResource&lt;Model>("Models/Box.mdl"));
					boxNodes_.Push(SharedPtr&lt;Node>(boxNode));
				}
			}
		}
		else
		{
			/*remove boxes*/
			const Vector&lt;SharedPtr&lt;Node> >& boxgrp = scene_->GetChildren();
			for (unsigned ii = 0; ii < boxgrp.Size(); ii++)
			{
				StaticModelGroup * lastGroup = boxgrp[ii]->GetComponent&lt;StaticModelGroup>();
				if (lastGroup != NULL)
					lastGroup->RemoveAllInstanceNodes();
			}
			while( boxNodes_.Size())
			{
				SharedPtr&lt;Node> n = boxNodes_.Back();
				n->Remove();
				boxNodes_.Pop();
			}

			/*add back boxes*/
			unsigned ii = 0;
			StaticModelGroup * lastGroup = boxgrp[ii]->GetComponent&lt;StaticModelGroup>();
			for (int y = -125; y < 125; ++y)
			{
				for (int x = -125; x < 125; ++x)
				{
					if (lastGroup == 0 || lastGroup->GetNumInstanceNodes() >= 25 * 25)
					{
						for (ii = ii + 1;; ii++)
						{
							StaticModelGroup * next = boxgrp[ii]->GetComponent&lt;StaticModelGroup>();
							if (next != NULL)
							{
								lastGroup = next;
								break;
							}
						}
					}
					Node* boxNode = scene_->CreateChild("Box");
					boxNode->SetPosition(Vector3(x * 0.3f, 0.0f, y * 0.3f));
					boxNode->SetScale(0.25f);
					boxNodes_.Push(SharedPtr&lt;Node>(boxNode));
					lastGroup->AddInstanceNode(boxNode);
				}
			}
		}
	}
}</code></pre>

Basically it uses node->remove() to remove node.
But I saw memory usage monitor in visual studio 2017 just went larger and larger no matter use of staticModelGroup or not.
![mem_usage|288x82](upload://vo2rxgvUW0VR807a6za3zMZKnYI.png)
Do I write something wrong? 
Thanks!

-------------------------

Eugene | 2018-01-09 15:25:59 UTC | #2

[quote="ab4daa, post:1, topic:3926"]
But I saw memory usage monitor in visual studio 2017 just went larger and larger
[/quote]
Memory monitor doesn't show how much memory your application _use_. It only shows how much memory the OS _allocates_ for your application. It may allocate whole RAM, actually, I never care.

If you want to confirm memory leak, crash your app or use leak detection tools.

-------------------------

ab4daa | 2018-01-09 15:25:53 UTC | #3

Thanks, I feel a burden released.:grinning:

-------------------------

