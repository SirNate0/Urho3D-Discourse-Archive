George | 2017-01-02 01:07:14 UTC | #1

Hi everyone,
My progress so far has been great, although I have just touch the surface of the engine. I can animate 10k boxes moving on 10k conveyors. However, the animation is being slow since I call scene_->update() too many times in discrete event code. I wanted to limited the number of render updates in the code.

I need help with this one:
--------------------------------
Is it possible to activate all node components Update() functions without rendering update?

For example: I want to invoke the node components Update() function 2 or more times before calling a single render update using scene_->update().

Thanks
George

-------------------------

cadaver | 2017-01-02 01:07:14 UTC | #2

How a LogicComponent's Update ends up being called is due to the following:

Scene sends E_SCENEUPDATE event as part of Scene::Update().
Each LogicComponent or its subclass in the scene responds to it individually, and the event handler function calls the component's own Update().

If you want to eliminate the overhead of this individual event handling, call SetUpdateEventMask(0) on your components to disable the event handling completely, then call the Update function manually on them from some centralized frame event handler.

Note that Scene::Update() has nothing to do with render updates (your post is somewhat confusing), instead it's invoked by a separate event each frame.

-------------------------

George | 2017-01-02 01:07:14 UTC | #3

Thanks mate.
I disable automate update so I'm calling Scene::Update() manually.

If Scene::Update() has nothing to do with render updates, can I call Scene::Update() multiple times inside the  E_RENDERUPDATE event? 
By doing it this way I trigger LogicComponent's Update multiple times before I get one render frame?

-------------------------

cadaver | 2017-01-02 01:07:14 UTC | #4

E_RENDERUPDATE is used internally, and it's at the part of frame where scene should no longer be modified, as like the event name tells, the engine is already preparing for rendering.

Use the application-wide update events E_UPDATE or E_POSTUPDATE instead to hook up your own per-frame logic. You can call Scene::Update() multiple times during these events if you want, and this would also trigger the logic component updates.

-------------------------

George | 2017-01-02 01:07:14 UTC | #5

Thank mate,
That clarify my understanding of scene_->update();

Best Regards

-------------------------

