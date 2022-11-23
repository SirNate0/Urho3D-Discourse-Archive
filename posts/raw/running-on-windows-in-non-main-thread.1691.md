Bart | 2017-01-02 01:09:30 UTC | #1

Hello all,
I would like to ask a quick question (searched for it here but could not find definite answer):
Is it possible to create and run Urho instance inside a C++ application in a non-main thread on Windows? Or is this by definition not possible because graphics interface etc..?

Thanks!

-------------------------

cadaver | 2017-01-02 01:09:33 UTC | #2

The window event pulling (main loop) and rendering has to happen in the same thread. Trying to do otherwise you'll be on your own. 

Some mechanisms in Urho check whether they're being executed from the main thread for safety (events etc.) What you might be able to do is to "reassign" the main thread with Thread::SetMainThread() to some other thread, before doing any major Urho operations like creating/initializing the Engine class. Then continue to run the main loop from that thread.

-------------------------

