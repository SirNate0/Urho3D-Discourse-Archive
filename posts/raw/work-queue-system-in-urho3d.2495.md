codder | 2017-01-02 01:15:49 UTC | #1

Hello,

Can somebody explain me how work queue is working in Urho3D and where is used internally?
How it differs from other multi-threaded task scheduler systems?

Thanks

-------------------------

Eugene | 2017-01-02 01:15:49 UTC | #2

[quote="codder"]Hello,

Can somebody explain me how work queue is working in Urho3D and where is used internally?
How it differs from other multi-threaded task scheduler systems?

Thanks[/quote]
Task that is consumed by Work Queue goes into threads and get completed at some point (or wait for completing in main thread, if no working threads)
I don't know how other task scheduler systems works so I can't explain the difference.
Work Queue is internally used (only?) within rendering systems.

-------------------------

codder | 2017-01-02 01:15:49 UTC | #3

Why is not used by the physics subsystem? Background resource loading is using a dedicated thread or is consumed by the work queue?
I'm trying to understand better how the multi-threading system is working in Urho3D.

-------------------------

cadaver | 2017-01-02 01:15:49 UTC | #4

Physics ties into fixed step scene updates and scripts, so it cannot be easily put into a thread without incurring concurrency or locking problems. Basically, while physics calculates, you don't have sensible other things to do, if you also want to run scene logic in lockstep with physics updates.

Resource background loading uses its own thread. It *could* use the work queue, but it was potentially simpler to do as a own thread, it sleeps most of the time anyway. So far Urho itself only uses the work queue for short-lived tasks on the same frame, like spreading culling or light processing to many cores when preparing the rendering view.

-------------------------

