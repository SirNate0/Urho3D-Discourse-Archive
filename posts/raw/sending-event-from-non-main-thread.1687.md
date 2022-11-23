atai | 2017-01-02 01:09:29 UTC | #1

Hi, I run into this Urho3D (1.5)  error on GNU/Linux:

#0  Urho3D::Object::SendEvent (this=0x7fffe0039ab0, eventType=..., eventData=...)
    at /store/software/urho3d/Urho3D.git/Source/Urho3D/Core/Object.cpp:290
290	        URHO3D_LOGERROR("Sending events is only supported from the main thread");


Is there any particular reason I cannot send event from a non-main thread?  Is it possible to support non-main thread sending events on certain platforms which may not have main thread only restrictions?

-------------------------

cadaver | 2017-01-02 01:09:29 UTC | #2

A Urho event is basically an immediate function call to the handler, and because events are frequently used to communicate scene or UI changes, it would be generally unsafe to respond from anywhere else than the main thread, and this is not supported on any platform. It also simplifies the internals a lot.

You will need to implement a queue (naturally protected by a threadsafety primitive, such as mutex), to which messages are submitted by the other thread(s) and received by the main thread in a well-determined part of the frame update, then forwarded as events. This is e.g. how the FileWatcher class operates.

-------------------------

atai | 2017-01-02 01:09:30 UTC | #3

Hi, thanks for the reply.  I would expect that the certain tasks can be restricted to the main thread due to OS restrictions, but sendEvent() would be usable in other threads  so for example we can invoke services from other thread.  For people familiar with Android, which has the restriction that the UI calls can be only made in the main thread, sendEvent() or similar calls can be used from other threads to update the UI.

Also now I get around this restiction by setting the thread that is doing the work to be the main thread.  So it is kind of arbitrary in Urho3d what thread can be the main thread?

-------------------------

thebluefish | 2017-01-02 01:09:30 UTC | #4

Main thread *shouldn't* matter in terms of technical capability. Urho3D will check whether it is the main thread to enforce the notion that sending an event from one thread to another is not thread-safe. Sure, you could get around this by denoting another thread as the main thread; however you're just getting around a safety feature. It does not change whether or not you're going to get undefined behavior by firing events from anything but the original main thread.

-------------------------

cadaver | 2017-01-02 01:09:31 UTC | #5

Note that we could implement (in the engine) a generic queue for non-mainthread events, and for example say they will always be taken from the queue in the beginning of next frame. However I'm against it for two reasons:

- It confuses the nature of events, as it would make them behave differently depending on whether sent from the main thread or not. Because now events are always immediate, the event data map can be used by the callee to communicate return values. For queued events this would not be possible.
- What if you wanted to handle the event in a different phase of the frame, for example during scene update?

-------------------------

