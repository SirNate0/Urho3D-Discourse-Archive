SirNate0 | 2017-03-08 04:24:02 UTC | #1

When using static SharedPtr<class derived from Object> classmembers, my game crashes upon exiting when the destroyed object tries to remove itself from the list of event senders in the (already destroyed) context. What is a good way to avoid this? Just don't use static objects (it is probably relatively easy now that the context has the global variables)?

Thanks!

-------------------------

1vanK | 2017-03-08 07:52:15 UTC | #2

You can not use sharedptr in global space or as static https://github.com/urho3d/Urho3D/issues/802

For global objects you can create own sybsystem and store objects in it

-------------------------

Eugene | 2017-03-08 08:12:11 UTC | #3

Actually, you can. But it's pretty dirty and you have to release this pointer maunally before context destruction.

-------------------------

