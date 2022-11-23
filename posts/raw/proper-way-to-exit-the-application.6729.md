shifttab | 2021-02-25 12:12:29 UTC | #1

I have a subsystem that listens to E_EXITREQUESTED which is called when quitting the application by clicking on the x close button of the window but it is not called when quitting with `GetSubsystem<Engine>()->Exit();`

How can I gurantee that E_EXITREQUESTED is triggered?

-------------------------

throwawayerino | 2021-02-26 02:36:56 UTC | #2

The event is intended as a way to call `Engine::Exit()`, not the other way around.
Have you considered sending the `E_EXITREQUESTED` event yourself? [Engine subsystem listens to it](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Engine/Engine.cpp#L978).

-------------------------

