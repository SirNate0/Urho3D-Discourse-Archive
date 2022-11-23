Eugene | 2017-01-02 01:13:41 UTC | #1

I need to update (i.e. change model and material of) some StaticModel component every X (m)sec in paused Editor.
I tried to use LogicComponent::Update but it does not work in pause, of course.
I tried to use StaticModel::UpdateGeometry but even if called from main thread, destruction of old model in the middle of rendering cause crash inside Urho renderer.
Now I just stored old StaticModel::GetModel to prevent destruction. Is there more clean way to do what I want?
This hack just move my problem aside. It is not solution.

-------------------------

cadaver | 2017-01-02 01:13:41 UTC | #2

"Update" event (the application-wide one, not scene update) should be safe, and run irrespective of whether scene(s) are paused or not.

-------------------------

Eugene | 2017-01-02 01:13:41 UTC | #3

Damn, I have completely forgotten about events.. Thank you, it works.

-------------------------

