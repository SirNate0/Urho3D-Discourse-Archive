GIMB4L | 2017-01-02 00:58:42 UTC | #1

I have my own state system, but I'm not entirely sure how to fully stop a scene from updating or being rendered, and deleting it in general. I've tried scene.Remove() but that doesn't do much. How do I completely stop and delete a scene?

-------------------------

cadaver | 2017-01-02 00:58:43 UTC | #2

Generally the application always owns the scenes in Urho3D, the engine doesn't. Node::Remove() removes from parent, but since scene has no parent that has no effect.

In Angelscript, to destroy a scene, you must null all "strong" handles ( @ symbol ) pointing to it. In Lua you would call the destructor ( scene:delete() )

You can also call Clear() on the scene to delete all components and child nodes, then you could re-use and refill it with new content.

-------------------------

GIMB4L | 2017-01-02 00:58:43 UTC | #3

I'll give that a shot, thanks!

-------------------------

GIMB4L | 2017-01-02 00:58:43 UTC | #4

I can't get it to work, the scene still isn't being deleted. Strong handles are no fun.

-------------------------

