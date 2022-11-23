Enhex | 2017-05-03 18:23:19 UTC | #1

It seems the WorkQueue implementation suffers from lock contention problem.

I've ran concurrency profiling in VS2017 on sample 18_CharacterDemo, and I'm getting ~400 lock contentions at any given moment (per frame?):
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/c4305312a434f59f521d8deee3fe8682e0c6041a.png'>

Which mostly come from WorkQueue::ProcessItems():
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/bb9d196731a5149b0510de7ddbec92ef1e4894a0.png'>

Probably depends on the CPU, for some users this doesn't have any noticeable effect, for others it causes small stuttering, and if they use -nothreads it significantly reduces the stuttering.

I'm not proficient with multithreaded programming, but maybe lock-free queue can be used here to solve this problem?
There're libraries such as [Boost.Lockfree](http://www.boost.org/doc/libs/1_64_0/doc/html/lockfree.html) and [libcds](https://github.com/khizmax/libcds) that provide implementations.

-------------------------

cadaver | 2017-05-03 18:21:04 UTC | #2

It could be looked into; from what I investigated the worst part is the possible latency when spinning up a worker thread, not necessarily lock contention itself. On the other hand, workers shouldn't spin 100% of the CPU when they don't have work to do.

-------------------------

sabotage3d | 2017-05-04 14:27:20 UTC | #3

When C++11 is enabled maybe we can have something like this: https://github.com/cameron314/concurrentqueue.

-------------------------

cadaver | 2017-05-04 16:39:49 UTC | #4

Forgot to say that some of the lock contention is intentional, because blocking the worker threads and preventing them spinning the CPU when they don't have work is done with the same lock. Tried a signal back then (for waking them up) and it resulted in worse latency.

This is an unorthodox design, so better solutions are gladly received. Possibly something like that once a worker thread wakes up for one frame, it doesn't go to sleep, but spins for more tasks.

The problem is that we're not a 100% task-driven engine, but the main thread still orchestrates things heavily, and worker threads do only occasional work.

-------------------------

Victor | 2017-05-04 17:18:32 UTC | #5

I think I ran into an issue where my WorkerThreads were running on the main thread, and for some reason I couldn't push them off into their own thread. My guess is that my implementation was just incorrect, so I ended up making my own thread class that extended Urho3D::Thread, and I created a ThreadManager class. 

Perhaps there could be an example at some point with the proper use of using the worker thread system. While the documentation seems pretty straight forward, I feel like I was still not grasping some of the concepts, and therefore my implementation was just wrong. Perhaps an example of creating a loading screen would be ideal (if any has some time). :)

-------------------------

Pencheff | 2017-05-11 07:37:06 UTC | #6

How about [condition variables](http://en.cppreference.com/w/cpp/thread/condition_variable). Implementing a worker thread is straightforward, push some work into a queue and signal through a condition variable that one/many workers are waiting.

-------------------------

Pencheff | 2017-05-13 10:49:22 UTC | #7

Indeed, I just did profiling in my project - the worker threads are spending more time in mutex locking than 3 of my worker threads for decoding/rendering full HD mpeg4 video. I'd be glad to PR once I get some spare time.

-------------------------

