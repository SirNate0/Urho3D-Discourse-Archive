nergal | 2017-09-22 12:53:41 UTC | #1

Is there any multithreading example using Urho3d's internal work queues and workers?

I want to test it out to perform some computational heavy functions in.

-------------------------

Eugene | 2017-09-22 13:25:16 UTC | #2

Well, Urho renderer itself _is_ multithreading example.

-------------------------

nergal | 2017-09-22 14:06:42 UTC | #3

Are the worker-model thought of being used internally in urho only?
Should some internal work queue be used for new workloads?

Could you please point me to an example in the code where it is used? (I've tried to find some code in the source)

-------------------------

Eugene | 2017-09-22 14:35:22 UTC | #4

Since WorkQueue is public system, you could use it for your own tasks. Search for `AddWorkItem` for examples.

However, WorkQueue is not the best task processor and has some design flaws.
It is intended to be short-term task runner, a kind of local parallelism. You put your items, wait for competeness and use results.
If you want your items be running in background among multiple frames, I don't recommend to use WorkQueue. Be careful with priorities, at least.

-------------------------

Victor | 2017-09-22 14:43:05 UTC | #5

Personally, what has worked for me has been using Urho's Thread model and rolling your own ThreadManager class. I also use my own EventManager that can call events from threads since Urho's event system prevents you from calling outside of the main thread. You will have to be careful with this approach however...

Also, Urho provides the Mutex/MutexLock classes to help thread safe your shared resources.

-------------------------

