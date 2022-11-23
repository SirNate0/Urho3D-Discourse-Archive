thebluefish | 2017-01-02 00:59:00 UTC | #1

A little thing I want to do at the beginning of a level is to advanced the physics simulation by 5-10 seconds to allow any objects to "settle". I have tried the following methods to do so:

[code]_scene->Update(10.f);[/code]
[code]physics->Update(10.f);[/code]
[code]physics->GetWorld()->stepSimulation(10.f, 1024);[/code]
[code]_scene->SetTimeScale(2.5f);
_scene->Update(10.f);
_scene->SetTimeScale(1.f);[/code]

However no matter how I update it, it always locks up the simulation for the full duration. So doing [code]physics->GetWorld()->stepSimulation(10.f, 1024);[/code] will still cause a 10-second delay to the user.

Update: I've gotten it to work with the following snippet:

[code]physics->GetWorld()->setInternalTickCallback(0, 0, true);
    physics->GetWorld()->setInternalTickCallback(0, 0, false);

	physics->GetWorld()->stepSimulation(10.f, 1024);

	physics->GetWorld()->setInternalTickCallback(Urho3D::InternalPreTickCallback, static_cast<void*>(physics), true);
    physics->GetWorld()->setInternalTickCallback(Urho3D::InternalTickCallback, static_cast<void*>(physics), false);[/code]

However this seems like a really dirty way to advanced the time.

-------------------------

cadaver | 2017-01-02 00:59:01 UTC | #2

To fast-forward the physics simulation without actually taking a large amount of real time or CPU power necessarily means doing the calculations at lower accuracy, which may lead to unwanted results like objects tunneling through other objects. You could try decreasing the physics world FPS, or the amount of simulation steps taken, to a low value for the "fast-forward" step (try something like 10 fps, or even lower if necessary), then restoring the original value when normal simulation should continue.

-------------------------

