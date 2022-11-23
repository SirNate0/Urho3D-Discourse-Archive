George | 2017-01-02 01:07:11 UTC | #1

Dear all,
When using calling  scene_->Update(my own UpdateTimeStep)  inside the E_UPDATE event I found that my components (Node translation) rendering are a few frame behind. This occur after the [b] first three passes[/b] in the E_UPDATE event.


According to the doc, I can use E_SCENEUPDATE event.  But E_SCENEUPDATE doesn't seem to be existed in the current revision. 

Is there anyway to force render update after  scene_->Update(my own UpdateTimeStep) ? Or where is the best place to do  scene_->Update() to make sure that it occurs just before render update.

Thanks
George

-------------------------

cadaver | 2017-01-02 01:07:12 UTC | #2

Are you talking about skeletal animations? These will be lazy-updated during the render update.

If you want to sample the node positions after animation, you have a couple of options. The octree sends E_SCENEDRAWABLEUPDATEFINISHED after the animation updates are done. You could also use E_POSTRENDERUPDATE. You cannot reasonably force this update. Note that E_POSTRENDERUPDATE is a delicate place in the frame; deleting visible nodes at this point will likely crash the engine.

-------------------------

George | 2017-01-02 01:07:12 UTC | #3

Thanks  cadaver.
I disabled the skeletal animation, but also found that the first 3 passes over the E_UPDATE event, but doesn't do render update.

The code does goes through my components 3 times where node::Translate() have been called. But I don't see the render update. 

After that first three passes, it works normally.

Regards

-------------------------

