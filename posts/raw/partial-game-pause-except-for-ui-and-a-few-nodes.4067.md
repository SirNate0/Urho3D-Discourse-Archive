slapin | 2018-03-02 22:15:48 UTC | #1

Hi, all!

How can I do complete pause for everything in game (including physics, components, etc.) but still have UI
and some selected things running (i.e. camera)?

I need this for game pause during menus, for "photo" mode and for some silly effects.
I know about https://discourse.urho3d.io/t/best-way-to-pause-the-game/208 and I will use it if there is no other
way, but is there some way to pause subtree of nodes, but leave a few unpaused?

Thanks!

-------------------------

jmiller | 2018-03-03 03:19:18 UTC | #2

Selective subscriptions to E_UPDATE and E_SCENEUPDATE (Scene::SetUpdateEnabled (bool enable) as mentioned in your link)

Node/UIElement/Component ::SetEnabled(bool)

Node::GetChildren(PODVector<Node*>& dest, bool recursive) const // for working with subtrees (and there's similar for UIElement)

HTH

-------------------------

