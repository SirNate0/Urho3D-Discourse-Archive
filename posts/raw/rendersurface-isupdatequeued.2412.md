Andre_B | 2017-01-02 01:15:15 UTC | #1

When i queue an update to a RenderSurface i know that it gets executed at the end of the current frame. With the result obtained on the next frame.

However render surface has these two functions:

    /// Return whether manual update queued. Called internally.
    bool IsUpdateQueued() const { return updateQueued_; }
    
    /// Reset update queued flag. Called internally.
    void ResetUpdateQueued();

My question is:
Does the IsUpdateQueued function reset to false, after a queue update, when the rendering of this render surface is finished?

Since these two functions are called internally i would like to know when are they being called.

-------------------------

