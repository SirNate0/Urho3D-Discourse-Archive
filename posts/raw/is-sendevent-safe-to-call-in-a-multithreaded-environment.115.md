GIMB4L | 2017-01-02 00:58:07 UTC | #1

I was trying out some multithreading, and when I called SendEvent from my thread I found I had a nasty race condition. Can SendEvent be called from a separate thread, and is there a recommended way to queue up events for Urho to fire?

-------------------------

cadaver | 2017-01-02 00:58:07 UTC | #2

SendEvent() is an (almost) immediate function call, which also modifies some state in the Context object, so it's certainly not safe from threads other than the main thread.

Because SharedPtr & WeakPtr reference counting are both thread-unsafe, developing a robust event queuing mechanism that can take eg. pointer parameters too in the event data VariantMap is right now hard to do. I'd rather model the system so that you submit work to the WorkQueue subsystem, and watch for the task completions in the main thread (you optionally get an event when a task is done.)

-------------------------

GIMB4L | 2017-01-02 00:58:08 UTC | #3

Alright, makes sense. Thanks again!

-------------------------

