Ray_Koopa | 2017-01-02 01:13:53 UTC | #1

I'm still trying to make an optimal hierarchy for my scene, but can't fully solve one issue.
I want to create content via code and do not want to use the XML editor for this yet, as 90% of my game objects are dynamically generated walls and floors.

Let's say I have a node which [b]requires[/b] two child models:
- a grid which can be moved up and down (e.g. a static model)
- Another pointer model placed on that grid (with a Raytrace).
Thus the node is basically the cursor in 3D space for an in-game editor.

Without those models, the whole node doesn't make any sense. It must have those child models and nodes hosting them. Those models also don't make sense anywhere else.

So I thought of a script component on the cursor node to just create the children:
[ul][li]CursorNode
> CursorComponent (Component)
[list][*]GridNode (created by CursorComponent)
> GridModel (StaticModel, created by CursorComponent) [/li]
[li]PointerNode (created by CursorComponent)
> PointerModel (StaticModel, created by CursorComponent)[/li][/ul][/*:m][/list:u]

Is that good code design? Or are there better design choices I should take here?

-------------------------

jmiller | 2017-01-02 01:13:53 UTC | #2

I often have components add child nodes and other components, and find OnNodeSet() convenient for initializing (for deserializing however, see how VehicleDemo does that):

[code]void Cursor3D::OnNodeSet(Node* node) {
  if (!node) { // removed from node
    return; }
  SubscribeToEvent(E_UPDATE, URHO3D_HANDLER(Cursor3D, HandleUpdate));
  // e.g.  node_->CreateComponent ...
}[/code]

Currently, I create a "CursorBase" node with the Cursor3D component. It can be attached to the camera node, it has a Plane for raycasts, and a WeakPtr to a completely independent node with the actual visual cursor it positions. But you can make the hierarchy whatever seems most convenient for you, e.g. if you find the inherited transforms useful.

-------------------------

