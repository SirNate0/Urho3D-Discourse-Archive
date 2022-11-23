codder88 | 2017-01-02 01:07:42 UTC | #1

Hello,

I'm new to Urho3D.

I'm trying to create a copy-paste functionality for scene nodes.

Actually when copying nodes I put them in a Urho3D::Vector

Urho3D::Vector<Urho3D::Node*> stack_;
stack_.Push(selectedNodes[i]);

Where selectedNodes is a vector which holds references to selected nodes. // Urho3D::Vector</Urho3D::Node*> selectedNodes;

The problem is when pasting because I'm trying to add a referenced node to the scene.

scene_->AddChild(stack_[i]); // Doesn't add nodes that already exists (this because scene_ already holds a reference to the stack_ node)

My question is: How to duplicate nodes if already exists in the scene?

-------------------------

