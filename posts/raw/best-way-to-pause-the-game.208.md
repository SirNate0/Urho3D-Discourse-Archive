thebluefish | 2017-01-02 00:58:53 UTC | #1

I want to pause the game when the player goes into the pause menu. The UI should still be working, but physics and other updates should not.

I've played around with changing:
[code]if (pauseMinimized_ && input->IsMinimized())[/code]
to:
[code]if (pauseMinimized_ /*&& input->IsMinimized()*/)[/code]

and using SetPausedMinimized to toggle this. It works great in actually pausing the game without causing further issues, but the UI doesn't update as a result. So before I go hack up the engine again, I want to make sure I'm not missing something huge.

-------------------------

friesencr | 2017-01-02 00:58:53 UTC | #2

The scene object is by default automatically updated every frame.

[urho3d.github.io/documentation/a ... cfd95db635](http://urho3d.github.io/documentation/a00302.html#a44c46009d055c833246a44cfd95db635)

This may be what you want.

-------------------------

thebluefish | 2017-01-02 00:58:53 UTC | #3

That works perfectly, thank you.

-------------------------

gawag | 2017-01-02 01:04:58 UTC | #4

The links is dead now and I think it lead to [urho3d.github.io/documentation/1 ... cfd95db635](http://urho3d.github.io/documentation/1.32/class_urho3_d_1_1_scene.html#a44c46009d055c833246a44cfd95db635)
[quote]void Urho::Scene::SetUpdateEnabled (bool enable)     Enable or disable scene update. [/quote]

Works as I hoped.

-------------------------

