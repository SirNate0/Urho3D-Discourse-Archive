thebluefish | 2017-01-02 01:04:36 UTC | #1

I'm attempting to finish up the C++ editor that scorvi put out. I added the ability to delete nodes, but it crashes when one node is a child of another and both are being deleted.

The angelscript version works as follows:
[code]
// Remove nodes
    for (uint i = 0; i < selectedNodes.length; ++i)
    {
        Node@ node = selectedNodes[i];
        if (node.parent is null || node.scene is null)
            continue; // Root or already deleted

        uint nodeIndex = GetListIndex(node);

        // Create undo action
        DeleteNodeAction action;
        action.Define(node);
        group.actions.Push(action);

        node.Remove();
        SetSceneModified();

        // If deleting only one node, select the next item in the same index
        if (selectedNodes.length == 1 && selectedComponents.empty)
            hierarchyList.selection = nodeIndex;
    }
[/code]

And my code in C++:
[code]
Urho3D::Vector<Urho3D::Node*> nodes = _editorSelection->GetSelectedNodes();
for (unsigned int i = 0; i < nodes.Size(); i++)
{
	Urho3D::Node* node = nodes[i];

	if (!node->GetParent() || !node->GetScene())
		continue;

	node->Remove();
}
[/code]

The crash appears to be caused by a bad pointer held by the child node. The parent node is already removed, and the child node's parent_ pointer points to 0xfeeefeee instead of being null (This is a Visual Studio value). AFAIK the angelscript bindings uses the Node's GetParent/SetParent methods. Does anyone see a problem with my approach?

-------------------------

cadaver | 2017-01-02 01:04:36 UTC | #2

AngelScript handles are equal to SharedPtr's, so they force keeping the selectedNodes alive until they're both removed from the scene, and selectedNodes has been cleared.

But in this kind of operation it would be more correct to hold a vector of WeakPtr's to all the nodes you want to delete. No need to sort by depth, and you don't cause nodes to be left alive any longer than they should, you just check if each WeakPtr has expired (due to hierarchy already deleting the node) and if so skip to the next.

-------------------------

thebluefish | 2017-01-02 01:04:37 UTC | #3

Ahhh ok, that makes sense. That's good to know for future cases where I'm converting angelscript to C++. I now do it the following way:

[code]
Urho3D::Vector<Urho3D::WeakPtr<Urho3D::Node>> nodePtrs;
auto nodes = _editorSelection->GetSelectedNodes();
for (auto itr = nodes.Begin(); itr != nodes.End(); itr++)
{
	Urho3D::WeakPtr<Urho3D::Node> node(*itr);
	nodePtrs.Push(node);
}
for (auto itr = nodePtrs.Begin(); itr != nodePtrs.End(); itr++)
{
	Urho3D::WeakPtr<Urho3D::Node> node = *itr;

	if (!node || !node->GetParent() || !node->GetScene())
		continue;

	node->Remove();
}
nodes.Clear();
[/code]

This works great. Thanks again!

-------------------------

