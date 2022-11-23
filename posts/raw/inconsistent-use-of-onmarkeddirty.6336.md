vmost | 2020-08-20 03:34:15 UTC | #1

Learning about components, and I encountered this concept of a 'dirty node'. Basically, a scene node stores its position relative to the root scene node (aka the 'world transform' of the scene node), and when its local position (relative to its parent scene node) changes, the world transform is no longer accurate. That inaccuracy means the scene node is 'dirty', and it gets 'cleaned' by updating the stored world transform with `Node::UpdateWorldTransform()`.

Components, which are attached to nodes, have the option (i.e. the implementer of a Component has the option) to respond to a node being made dirty, with the virtual function `Component::OnMarkedDirty()`. However, the calls to `OnMarkedDirty()` in Node.cpp seem inconsistent. There are only three calls:
- in `Node::AddListener()`, when a component is added as a listener to a node then if the node is dirty `OnMarkedDirty()` will be called right away; supposedly the whole point of components 'listening' to arbitrary nodes is for being able to respond when those nodes become dirty (or enabled/disabled)
- that idea is backed up by the second call, in `Node::MarkDirty()` (name is self-explanatory), where all of the node's listener components call `OnMarkedDirty()`
- the third call, however... is in `Node::AddComponent(...)`; but nowhere do I see a component being added as a listener to the node that owns it

Note: yes, nodes both own components, and have a list of other (owned and unowned) components called 'listeners'. Separate lists

So, why is `OnMarkedDirty()` called in `AddComponent()`, if a component doesn't listen to its own node unless explicitly told to?

-------------------------

George1 | 2020-08-20 05:35:58 UTC | #2

This is a component based lib. Visual and  behavior are driven at component level.

Please correct me if I'm wrong, I think the node is listening to the component rather than component listening to a node.

-------------------------

Eugene | 2020-08-20 07:10:12 UTC | #3

I have spent 5 mins looking at the code and I failed to find plausible answer.
Could be historical artifact. Could be some non-trivial scenario.

-------------------------

vmost | 2020-08-20 17:10:28 UTC | #4

The node maintains a list of 'listeners', which are components that listen to the node. The purpose is knowing when the node is dirty.

-------------------------

vmost | 2020-08-20 17:18:06 UTC | #5

Checked the git blame, it looks like an 8yr old mistake. I guess OnMarkedDirty() doesn't get used very much.

-------------------------

George1 | 2020-08-21 00:59:52 UTC | #6

Maybe the big fish, Lasse, can answer this.  
OnMarkDirty can be a performance issue in some components e.g. splinepath.  You don't want to call it in every update.  In some situations (e.g. splinepath component), manually update is needed.

-------------------------

vmost | 2020-08-21 01:19:45 UTC | #7

Well the question here is why it gets called when a component is added to a node, even if that component isn't listening to the node.

-------------------------

George1 | 2020-08-21 01:43:41 UTC | #8

I think components hold reference to the node.  So any change to the component surely updates the node.  Again let Lasse answer this.

-------------------------

Modanung | 2020-08-24 14:50:35 UTC | #9

`markedDirty_` plays an important role in network replication as well:

https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Scene/Component.cpp#L200

-------------------------

