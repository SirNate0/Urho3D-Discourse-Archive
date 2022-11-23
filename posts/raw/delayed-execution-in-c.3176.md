smellymumbler | 2017-05-29 21:11:28 UTC | #1

Unity allows your to delay the execution of a function by using something like this: Invoke("DoSomething", 2);

DoSomething will be called after 2 seconds. I can call Invoke inside Update(), Awake() or any other callback.

-------------------------

ppsychrite | 2017-05-29 21:19:14 UTC | #2

You could launch another thread that waits two seconds, executes the function and stops. There's many ways to do that.

-------------------------

smellymumbler | 2017-05-29 21:32:32 UTC | #3

What's the "Urho" way?

-------------------------

ppsychrite | 2017-05-29 21:36:48 UTC | #4

I haven't looked into it that much but it looks like Urho3D has it's own way of doing it instead of using c++11 threads.
https://urho3d.github.io/documentation/1.5/_multithreading.html

-------------------------

smellymumbler | 2017-05-29 21:53:14 UTC | #5

Yeah, but it seems to be just a task queue. WorkItem does not contain any delay info, or the WorkQueue. You can just add new WorkItem's to the WorkQueue, no scheduling.

-------------------------

ppsychrite | 2017-05-29 21:57:12 UTC | #6

There appears to also be a Sleep function in the Timer class that you could call. https://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_time.html

If all else fails you could just use c++11's chrono and thread headers for multithreading and do this_thread sleep_for :wink:

-------------------------

Pencheff | 2017-05-29 22:02:54 UTC | #7

How about creating a scheduler that you add tasks to. A task holds the invoke time and a delegate to a method or a function. Subscribe to E_UPDATE for example and on every tick check if a task is to be executed.

-------------------------

