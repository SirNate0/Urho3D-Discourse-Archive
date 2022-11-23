setzer22 | 2017-01-02 01:02:43 UTC | #1

Hello everyone!

I've had an issue with my code, and even though I've fixed it I don't get why it failed before and why it works now. I'll try to explain a basic scenario where this happens. 

There's a C++ component CComponent that stores a matrix (Vector<Vector<StructType>>) as a member field (not a pointer but the actual matrix). There's a CComponent instance in the current scene and neither the component nor its node get deleted.

StructType holds a couple of integers and bools and a SharedPtr<Urho3D::Node>. Also, CComponent has two functions: retrieveNode(i,j) and storeNode(i,j,Node* node) that do exactly what their names say, get and set a node reference from a position in the matrix for a CComponent instance.

Now, retrieveNode and storeNode are registered as: Node@ retrieveNode(int i, int j) and void storeNode(int i, int j, Node@ node), to the script API, and here comes the problem.

From a script (ScriptA) I get a node from the scene subsystem and do this:
[code]
Node@ node = scene.getNode(id)
ccomponent_instance.storeNode(i,j,node);
[/code]

And from a script B, I do:
[code]
void Update(float timeStep) {
    ...
    Node@ node = ccomponent_instance.retrieveNode(i,j);
    //do things to that node, like getting a component and asking for values, nothing unusual
}
[/code]

The thing is that each time I retrieve a node pointer from CComponent its refcount decreases by one, until it gets to 0 and then the pointer gets auto-deleted, I checked that by printing the Refs() value for the node before returning it in CComponent.

I checked the source where the ScriptAPI is being registered to see if I was missing something and I saw that all references to class pointers like Node* were declared like Node@+, changing that fixed the issue and now the RefCount remains the same after calling the function from a Script several times.

I think the @+ is the right way to do it, and I've been able to read from the AngelScript documentation that it's an "Auto handle", but I don't quite get what that means and how AddRef and ReleaseRef are actually implemented in Urho.

Could anyone please clarify this to me a bit more? I'm kind of lost...

Thanks!

-------------------------

