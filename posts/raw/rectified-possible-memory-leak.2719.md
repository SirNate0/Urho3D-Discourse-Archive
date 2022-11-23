George1 | 2017-01-21 03:05:11 UTC | #1

Hi,
I'm testing large object creation and removing with the following test code. This is needed for my usage purpose. I have found memory grow rapidly after some times.

Here is the test code. I added inside the HandleUpdate of the example 4.


    int counter = 0;
    Node* mushroomNodeTest [1000];
    double obj = 0;
    void StaticScene::HandleUpdate(StringHash eventType, VariantMap& eventData)
    {
    	counter++;
    	if (counter == 1)
    	{
    		obj+=1000;
    		//instructionText->SetText(String(obj));
    		
    		for (int i = 0; i < 1000; ++i)
    		{
    			mushroomNodeTest[i] = scene_->CreateChild("Mushroom");
    			mushroomNodeTest[i]->SetPosition(Vector3(Random(90.0f) - 45.0f, 0.0f, Random(90.0f) - 45.0f));
    			mushroomNodeTest[i]->SetRotation(Quaternion(0.0f, Random(360.0f), 0.0f));
    			mushroomNodeTest[i]->SetScale(0.5f + Random(2.0f));
    			StaticModel* mushroomObject = mushroomNodeTest[i]->CreateComponent<StaticModel>();
    		}
    	}

    	if (counter == 2)
    	{
    		if (mushroomNodeTest)
    		{
    			for (int i = 0; i < 1000; ++i)
    			{
    				mushroomNodeTest[i]->Remove();
    				
    			}
    		}
    		counter = 0;
    	}

        using namespace Update;

        // Take the frame time step, which is stored as a float
        float timeStep = eventData[P_TIMESTEP].GetFloat();

        // Move the camera, scale movement with time step
        MoveCamera(timeStep);
    }

-------------------------

artgolf1000 | 2017-01-19 02:22:42 UTC | #2

Try this after remove all nodes:
[code]// Release all unused resources
GetSubsystem<ResourceCache>()->ReleaseAllResources(false);
[/code]

-------------------------

George1 | 2017-01-19 03:19:23 UTC | #3

Hi, I tried both debug and release mode, with both true/false setting.

That doesn't seems to be working.

Best Regards

-------------------------

Eugene | 2017-01-19 06:03:45 UTC | #5

It doesn't seem that this is some memory leak in code. MSVC reports nothing and Urho itself is unlikely to have a leak in such generic mechanism.

I suppose that you are just doing wrong things in general that lead to memory fragmentation and growing of used memory amount. Probably Urho need more pools, but it won't be made in near future.

-------------------------

George1 | 2017-01-19 08:58:38 UTC | #6

[quote="Eugene, post:5, topic:2719"]
at you are just doing wrong things in general
[/quote]

What do you mean? Have you test the function I posted? 

This is the function inside the default example 4. I just added in 2 for loops and three globals to demonstrate the problem. 

After creating and removing 8 million nodes with static model components your ram usage will be at 1GB.

Do you think that bit of the code I posted is wrongly written?

Thanks

-------------------------

Eugene | 2017-01-19 09:12:06 UTC | #7

[quote="George1, post:6, topic:2719"]
What do you mean? Have you test the function I posted?
[/quote]

Yes, I reproduced memory growing. But I _think_ that it is not a memory leak, but memory fragmentation caused by allocating tons of small objects: every node and every StaticModel internally cause many allocations. I think so because this problem is invisible for leak analyzers and there is no evidence except task manager that is not very reliable.

Redundant allocating is a problem of Urho, is some sense. I'd like to look at it at some point.
However, your problem is caused by your code. Nodes and components are not designed to be constantly created and destroyed, so the best solution is to avoid it.

BTW, are you able to _crash_ app with out-of-memory?

-------------------------

George1 | 2017-01-21 08:09:50 UTC | #8

I haven't able to crash the app yet ^^.

I'm creating a discrete event sim. The method I'm using required to create and destroy lots of objects. That's why I'm stress test this. I want to run at least 50 years at the rate of 1 node created and destroy per simulation second.

I have created 8.65 milliions objects in my code and the memory turns out mostly due do create and destroy node with static model on Urho3D engine. That was running over 100 days simulation in less than 3 minutes. My target was 1 billion object. But I think I will run out of ram at that rate.

Let me see if I can crash my app :).

-------------------
Updated:
Tested 100 million create and delete on my application code. The memory usage seems to be stable at 1.40 Gb.

Cheers

-------------------------

Eugene | 2017-01-19 12:53:08 UTC | #10

[quote="George1, post:8, topic:2719"]
Tested 100 million create and delete on my application code. The memory usage seems to be stable at 1.40 Gb.
[/quote]

Thank you! It confirms my guess. Stabling means that it is an issue about probably memory fragmentation or memory management in Windows, not leak in Urho.

However, Urho needs some pools, IMO.

-------------------------

codingmonkey | 2017-01-19 13:22:38 UTC | #11

[quote="Eugene, post:10, topic:2719"]
However, Urho needs some pools, IMO.
[/quote]

Indeed! Also more orientation on Data Driven

-------------------------

Lumak | 2017-01-20 19:16:18 UTC | #12

I tested George's code and verified that the memory usage increases due to fragmentation but no memory leak.  On Win10, VS2013 debug - took 25 mins. to settle and fragmented 1/2 GB just on a simple scene with his code.

I am curious as to how @Dave82 's Infested game is holding up when transitioning from indoor to outdoor and vice versa frequently.

-------------------------

Dave82 | 2017-01-20 20:47:29 UTC | #13

It works without any problem so far.I didn't encountered any memory growth in frequent removing/loading resources.I tested it a lot and after a certain time the memory usage stops growing.Sometimes even goes down drastically even if i load a new resource (possibly a bigger chunk of memory is released by the OS than the new resource).

-------------------------

George1 | 2017-01-21 03:04:36 UTC | #14

Thanks for the message.
As per my last message, this question should be marked as solved for now.

I have further test my simulation framework with 500 millions create and delete components and nodes (Running for quite a while). The memory became stable at 1.4GB on my system.

Regards

-------------------------

Lumak | 2017-01-21 16:34:58 UTC | #15

I know that 1k creation and removal per frame test is a bit extreme but good to know that a real game doesn't see this problem.

-------------------------

