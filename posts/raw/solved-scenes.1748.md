sovereign313 | 2017-01-02 01:09:51 UTC | #1

Hi,

So, i've created essentially a cutscene via animated sprites.  It all works wonderfully.  Now, what I'm trying to figure out how to do, is to remove the scene and it's elements, and then create a new scene (ie: start of the actually level/game).  I've read this topic: [topic50.html](http://discourse.urho3d.io/t/solved-changing-level-scene/72/1)

But I'm not sure this is working as I'd expect (I get segfaults).  I basically try to recreate everything using the same pointers (scene_, cameraNode_, Octree, etc) but it segfaults.  Do I need to somehow disable the viewport before doing all this?  I'd like to remove the scene and it's pointers completely, as after the 'cutscene' there is no need of the resources being used any more.

any help would be greatly appreciated.

-------------------------

mightymarcus | 2017-01-02 01:09:51 UTC | #2

I'm very new to Urho3D and don't know if it helps, but I read something about it's weak and shared pointers.

Have you tried weak pointers? (i guess with weak pointers the pointers will be deleted if nothing references them anymore)

[urho3d.github.io/documentation/1 ... k_ptr.html](http://urho3d.github.io/documentation/1.4/class_urho3_d_1_1_weak_ptr.html)

-------------------------

sovereign313 | 2017-01-02 01:09:51 UTC | #3

Sweet, thanks for the heads up.

I did get it working just now by using a new scene_ pointer.  The key though (what was crashing) was that I needed to UnsubscribeFromAllEvents() before creating the new scene.  Which makes a lot of sense.  You don't want event notifications for stuff you've deleted :-/

So:

[code]
UnsubscribeFromAllEvents();
scene_->RemoveAllChildren();
CreateScene();
[/code]

-------------------------

