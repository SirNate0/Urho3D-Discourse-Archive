esak | 2017-01-02 01:06:03 UTC | #1

If I create several collisionshapes to a node (Node::CreateComponent), and then call Node::RemoveComponent on the node.
Are all the collisionshapes removed then, or do I need to do some more to clean up all the shapes nicely?
(I didn't manage to figure out this from the source code.)

-------------------------

jmiller | 2017-01-02 01:06:03 UTC | #2

Hi esak,

Correct;
/// Remove the first component of specific type from this node.
void RemoveComponent(StringHash type);

One way to remove all components of a type is to create a PODVector<type> and pass it to this method:
void Node::GetComponents(PODVector<Component*>& dest, StringHash type, bool recursive) const
then iterate over dest and (*it)->Remove() each.

implementation details
[github.com/urho3d/Urho3D/blob/m ... e/Node.cpp](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Scene/Node.cpp)

-------------------------

cadaver | 2017-01-02 01:06:03 UTC | #3

A Node member function to remove all components of certain type won't be hard to add, thanks for the idea!

-------------------------

esak | 2017-01-02 01:06:03 UTC | #4

Thanks for the answer! It works.  :slight_smile:

-------------------------

