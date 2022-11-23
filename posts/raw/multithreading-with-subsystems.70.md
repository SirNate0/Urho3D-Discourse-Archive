NemesisFS | 2017-01-02 00:57:45 UTC | #1

Hi,

I just read some of the documentation about Multithreading and now I`m wondering why the Subsystems dont utilize those more often. Wouldnt it be nice if i.e. the renderer, physics and i/o subsystems would each have an own thread?
Also I havent found info about allocation. How does it work inside a thread? Does the whole Engine use the default allocater at the moment?

-------------------------

Azalrion | 2017-01-02 00:57:45 UTC | #2

Had a bit of a discussion about this before when looking at multi-threaded resource loading. Currently there are limitations due on:

[ul]Logging
Profiling
Sending events
Doing anything with the GPU[/ul]

We're pretty busy on doing video, text formatting and a few other things so we dropped multi-threaded loading for now but some of the conclusions we made were that urho could be made thread safe for certain areas in a number of ways.

Logging - Logging can be made thread safe because the current std lib function is already thread safe the only aspect of it that is not thread safe is the event system for capturing log messages, so its dependent on that being made safe.

Event System - Event system could be made thread safe but weren't happy with our solution as it involves the event handling functions locking each object as it handles the events and anything that touches on the gpu would need to be queued to handle at the start of the next rendering phase.

-------------------------

cadaver | 2017-01-02 00:57:45 UTC | #3

Tying eg. the application update logic, scripts and physics into threading would be quite hard. Currently there's a strictly sequential update, which I'll illustrate with script functions but it would be the same with C++:

- Scene update (with deltatime dt)
- - For each script object which uses it: Update(dt) 
- - Physics update, which is split into multiple fixed timestep updates if necessary
- - - For each script object which uses it: FixedUpdate(fixedDt)
- - - Update Bullet world with fixedDt
- - - For each script object which uses it: FixedPostUpdate(fixedDt)
- - For each script object which uses it: PostUpdate(dt)

In this scenario, if the physics was on another thread, the fixed updates still couldn't proceed before the physics step is ready. We could make varying timestep script update and physics update happen simultaneously, but that would lose the control to apply logic per physics step, which is often essential for things like character control.

I'm hesitant to do any multithreading which either introduces more latency into the frame overall, or makes programming the logic harder. The renderer could however be made to utilize threads better, for example preparation of multiple views could happen simultaneously on threads. I now have a development machine with a very beefy GPU but somewhat poor CPU and I see the framerate doubling when I *disable* occlusion in the water example (2 views), which certainly is not optimal.

Memory allocation happens with default new and delete, which are threadsafe. However note that the SharedPtr's have no thread safety, so their reference counts aren't safe to increase/decrease from multiple threads. It's best to use raw pointers in all threaded work (this also assumes the objects being worked on won't be born or killed during threaded updates)

-------------------------

NemesisFS | 2017-01-02 00:57:45 UTC | #4

Okay, I think I`ve underestimated the difficulties implied my making greater use of multithreading.

Nevertheless I fancy the architecture of having Subsystems which are thread-safe and have an own memory-pool and use a event/message-system for communication...
I think it would be pretty robust (once its implemented) and with the increasing number of processor-cores even in low end devices it makes sense.

-------------------------

cadaver | 2017-01-02 00:57:46 UTC | #5

It depends on the programming model you're willing to take into use, and the latency you're willing to accept. For example raycasts, are you OK with not receiving the result instantly, but instead you get a pointer to a pending raycast task which will signal itself when it has been completed. Also, you could be calculating logic ahead of time in a separate thread, but you cannot receive user input from the future, so it would actually be using old inputs and thus introducing latency.

In my opinion Urho3D may already be a bit inflexible (due to the large amount of functionality it already implements) for threading model experiments, of course if you don't mind tearing down a large part of it and rebuilding the functionality, then it's OK :wink:

As realistic steps for better thread usage, without destroying anything from the API, I would see:
- Background loading of resources up to the point when they have to be uploaded to the GPU by the main thread
- Tasks/threads utilized more for render view preparation. This could include the UI, provided it happens at a point in the frame where UI modification is guaranteed to not happen

-------------------------

