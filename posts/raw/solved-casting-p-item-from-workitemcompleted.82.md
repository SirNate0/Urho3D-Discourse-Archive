friesencr | 2017-01-02 00:57:51 UTC | #1

pardon my c++ newbish.

i am trying to cast the workitem pointer from the completed event.

my code isn't working so well:
[code]const WorkItem* item = (const WorkItem*)eventData[P_ITEM].GetPtr();[/code]

here is the source code for the work queue
[code]
if (i->sendEvent_)
{
    eventData[P_ITEM] = (void*)(&(*i));
    SendEvent(E_WORKITEMCOMPLETED, eventData);
}
[/code]
 
Thanks

-------------------------

NemesisFS | 2017-01-02 00:57:51 UTC | #2

It should work if you dont call GetPtr(). eventData[P_ITEM] is a void pointer, you just need to cast it to a WorkItem Pointer (if im not mistaken).

Also I guess you should use "static_cast<WorkItem*>".

-------------------------

cadaver | 2017-01-02 00:57:51 UTC | #3

Actually your line should work. Here's a complete somewhat stupid example, inserted into the StaticScene example.

[code]
float resultVariable = 0.0f;

void MyWork(const WorkItem* item, unsigned threadIndex)
{
    float* result = static_cast<float*>(item->start_);
    for (unsigned i = 0; i < 1024 * 1024 * 1024; ++i)
        *result += sqrtf((float)i);
}

void StaticScene::Start()
{
    WorkItem item;
    item.priority_ = 0;
    item.start_ = &resultVariable;
    item.workFunction_ = MyWork;
    item.sendEvent_ = true;
    
    GetSubsystem<WorkQueue>()->AddWorkItem(item);
    SubscribeToEvent(E_WORKITEMCOMPLETED, HANDLER(StaticScene, HandleWorkItemCompleted));

    ...
}

void StaticScene::HandleWorkItemCompleted(StringHash eventType, VariantMap& eventData)
{
    using namespace WorkItemCompleted;
    WorkItem* item = static_cast<WorkItem*>(eventData[P_ITEM].GetPtr());
    // This should also work just as well
    // const WorkItem* item = (const WorkItem*)eventData[P_ITEM].GetPtr(); 
    
    float* result = static_cast<float*>(item->start_);
    LOGINFO("Calculation result was " + String(*result));
}
[/code]

-------------------------

friesencr | 2017-01-02 00:57:52 UTC | #4

i think i understand what is going on...  this is a very different way of thinking for me.  I think my head exploded.  I was able to cast the WorkItem from the beginning but the pointers didn't match up.

I could be way off base.

I allocated my worker on 'the stack'
[code]
	void CreateDungeon()
	{
		WorkItem item;
		item.sendEvent_ = true;
		item.workFunction_ = GenerateDungeonStart;
		dungeonWorker = &item;
		workQueue->AddWorkItem(item);
	}
[/code]

AddWorkItem doesn't take a pointer to a work item so it 'copies' the variable.  After the scope of the function the dungeonWorker actually gets 'nullified'.  I have no idea what it is pointing to after the item gets destroyed.  It amuses me that I will utilize allocating variables on stack to make it so i don't cleanup but now I didn't think of this inverted scenario.  My main motivation for using the pointer was to make it so i could track a work item and when the work item was completed to use the completed handler to and do some work based on the task that was completed.

The api seems to be suited for splitting up work to utiltize multiple cores more effectively.  I think everytime i saw threads being used they ended up all blocking using the queue#complete function within the same frame.  I can see that there is some code to try to prevent too many tasks from running long:

This is in the WorkerThread
[code]while (!queue_.Empty() && timer.GetUSec(false) < MAX_NONTHREADED_WORK_USEC)[/code]

It looks like GetSubsystem<WorkQueue> is a singleton?  Since complete gets called every frame tasks would never be able to run more then a frame?  If I wanted to have a task run longer would I want to make a new WorkQueue for my game specific code?

In the dreadful posibility of a single threaded system we might be able to add a WorkItem.current pointer to hold the current position of an iterator and suspend a task to pickup where it left off next frame for a longer running task as though as a sort of hackish coroutine.   maybe we can make the work function return a bool for whether it has been completed or not?

also a posible improvement to the api would be for the ability to specifify a workitem in the subscribe method:

[code]SubscribeToEvent(myWorkItem, E_WORKITEMCOMPLETED, HANDLER(MyApp, HandleDungeonGenerationComplete));[/code]

-------------------------

cadaver | 2017-01-02 00:57:52 UTC | #5

A couple of things..

- When you submit a task to the WorkQueue, it will get copied like you noticed, so the pointer in the completion event will be different. The WorkQueue has initially been used only for the Renderer's internal tasks and the completion event facility has been an afterthought, so using them is not as convenient as it should be. If each WorkItem would be an Object it could send its own completion event, however there's some overhead to that.

- Tasks will not be suspended, they always run to completion, and I don't intend to change that. The 1000ms timer is only for the case when there are no worker threads. You should test if whether it makes more sense to you to actually allocate at least 1 worker thread even on a single-core system. You should not make another WorkQueue on your own, as that creates another batch of (number of CPUs) worker threads which may be too much. Instead the existing one can be used to run tasks that are as long as you want, just put a priority that is less than M_MAX_UNSIGNED on them, so that the time-critical renderer tasks (which have priority M_MAX_UNSIGNED) can also run on other free worker threads (or on the main thread) in the meanwhile.

-------------------------

Azalrion | 2017-01-02 00:57:53 UTC | #6

How about passing in a WorkItem pointer instead and having the 'keep alive' list being a list of SharedPtr<WorkItem>'s instead.

That way the complete volatile boolean is usable outside of the WorkQueue and comparisons can be made as long as where the WorkItem was added keeps its own SharedPtr copy so that the memory isn't freed when the WorkQueue cleanses complete items.

-------------------------

cadaver | 2017-01-02 00:57:53 UTC | #7

We can support both forms, submitting SharedPtr's to work items, and submitting a const reference (where WorkQueue will make a copy, just like before). The Renderer / View do not care of individual tasks after submitting, they only need them all to complete, so they'll continue to use the latter. When submitting pointers it's important to check that the item isn't already in the queue.

-------------------------

Azalrion | 2017-01-02 00:57:53 UTC | #8

Is there a need to support both apart from backward compatibility? Its easy enough to modify the render functions to use the shared pointer method, it reduces the complexity of the WorkQueue only supporting a single method, shouldn't be much difference in performance either as you've got two use cases copying the WorkItem or creating a new SharedPtr<WorkItem>.

Anyway, added a pull request with the single version and Render functions refactored to see whether the single method is suitable.

-------------------------

cadaver | 2017-01-02 00:57:53 UTC | #9

Yes, it's true that the performance of the methods doesn't matter once we start using sharedptr's to track the items, then it's anyway a new dynamic allocation for each. Previously, as it was a list of items and not pointers, the allocations would be pooled internally like in a Vector.

-------------------------

cadaver | 2017-01-02 00:57:54 UTC | #10

Took the pull request as-is. It's better to see outright in the client code that a new work item is being dynamically allocated. And of course it's possible to reuse the same work item if it's performed only once per frame :wink:

-------------------------

Azalrion | 2017-01-02 00:57:54 UTC | #11

That's my next plan, refactor out all the cases in Octree and View where its based on the number of threads to re-use the pointers to save having them allocated every frame. Might be possible to do the same for render paths but thats slightly more risky as that can change during runtime, but a guard could be put in place to re-allocate if the number of render path commands changes.

-------------------------

cadaver | 2017-01-02 00:57:54 UTC | #12

A thought came to my mind that WorkQueue itself could allocate items into a "free" pool, to reuse them automatically.

-------------------------

Azalrion | 2017-01-02 00:57:54 UTC | #13

Oh now that's an interesting idea, just off the top of my head two ways to work it.

First you could do something like:
[code]
SharedPtr<WorkItem> item = WorkQueue::GetWorkItem();
// Do stuff.
WorkQueue::AddItem(item); //We wouldn't want to add it to the active queue from the available pool till we know its ready.
[/code]
Which would be a bit more explicit but also would allow circumvention of the pool. The other method and one which I'm leaning towards could be something like:
[code]
WorkItem item;
// Do stuff.
SharedPtr<WorkItem> reference = WorkQueue::AddItem(item);
[/code]
You'd have to do some conversions from the reference to copy the details from the passed reference to a free SharedPtr but it would mean that we could ensure all allocations were part of the pool.

Of course both would share behind the scenes stuff such as a separate queue for currently queued items and assigned items which wouldn't change much between the current format. I'll have a play see what comes out of it, the big question would be on when would it be safe to shrink the queue down, perhaps maintain a delta between frames of the number of used / requested items and if it lasts then shrink down to remove one time or infrequent usage of the WorkQueue.

Edit:

So had a play and decided that I prefer the flexibility of the first method where you can use the pool if you want or you can use your own SharedPtr allocation or even your own pool if you need to.

-------------------------

cadaver | 2017-01-02 00:57:54 UTC | #14

I prefer the first method too for the freedom it gives you.

-------------------------

