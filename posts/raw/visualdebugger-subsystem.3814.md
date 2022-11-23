TrevorCash | 2018-02-15 17:32:26 UTC | #1

I found myself wanting a basic tool for quickly adding debug geometry to my scene at any time using a single call and then having it disappear automatically later after a delay.  So I made a subsystem called VisualDebugger that wraps calls to DebugRenderer like DebugRenderer->AddLine(..) etc.


https://github.com/TrevorCash/Urho3D/blob/master/Source/Urho3D/Graphics/VisualDebugger.h


Initialization/setup:

> RegisterSubsystem(new VisualDebugger(context_));

Specify camera for displaying labels in the world:

> GetSubsystem\<VisualDebugger>()->SetPrimaryCamera(camera);


In HandlePostRenderUpdate() Issue the draw call to draw all geometry:

> GetSubsystem\<VisualDebugger>()->DrawDebugGeometry(scene_->GetComponent\<DebugRenderer>());


Example Usage anywhere:

> VisualDebuggerUILabel* label = GetSubsystem\<VisualDebugger>()->AddLabel(Vector3(0,0,0), "my debug label in the world");


By default geometry will last 2 seconds until it is deleted.  

This can be changed with a call to SetObjectLifeTimeMs() Or by calling label->SetLifeTimeMs() for individual control.

You can also restrict the max number of draw-able objects and/or the maximum time spent in the DrawDebugGeometry() call.

-------------------------

TrevorCash | 2017-12-31 22:55:54 UTC | #2

This video shows how I use the visual debugger to debug the world generation sampling in GreatGame:
https://youtu.be/440CXsz1glA

-------------------------

