TheComet | 2017-01-02 01:14:43 UTC | #1

After quite a long and heated discussion with an artist on our team about workflow, I got to thinking about a feature I'd really like to see (if it's not already possible).

In the editor, when adding a prefab, it gets [i]copied[/i] into the scene. This is undesirable if later on you decide to change something in the prefab: Those changes won't update the existing instantiations that are already in the scene.

What would really be cool is for a prefab to be referenced by XML file name when you add it to he scene and reloaded every time said XML is modified. Saving the scene would only serialize those references but not the actual contents of the prefab.

I realise implementing this would require some deep changes. How possible is it to see this in a future version?

-------------------------

cadaver | 2017-01-02 01:14:43 UTC | #2

There is an issue for this. [github.com/urho3d/Urho3D/issues/1636](https://github.com/urho3d/Urho3D/issues/1636)

It's indeed a quite deep feature, when you consider also possible nesting, or having non-prefab objects as children of prefabs etc.

A "cheap" implementation with no core engine changes would just work inside the editor, store a prefab reference to a node as a var and watch its reloads, or refresh prefabs at scene load time if necessary.

-------------------------

magic.lixin | 2017-01-02 01:14:45 UTC | #3

my solution was very simply and ugly, add a prefab tag for the node which was load from a prefab xml file, everytime when loading scene in the editor, recreate the node by the prefab defination.

-------------------------

TheComet | 2017-01-02 01:14:47 UTC | #4

Thanks for the suggestions, will try it out

-------------------------

