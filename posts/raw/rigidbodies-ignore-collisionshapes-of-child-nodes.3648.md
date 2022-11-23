SeanV | 2017-10-11 05:38:12 UTC | #1

I've noticed that in Urho3D, rigidbodies do not account for colliders in child nodes.

A rigidbody component will notice multiple collisionshapes on the same node, and create a btCompoundShape including each. However, if I have an object with a matching collisionshape and parent it to a node containing a rigidbody, the child's collisionShape is completely ignored.

This might be intended behavior, but I feel like it is unintuitive at least for me, coming from Unity where a rigidbody will make use of every collider in the hierarchy. I've tried to change the code for this, but I've had no luck.

In Rigidbody.cpp:

    PODVector<CollisionShape*> shapes;
    //CHANGED CODE: recursive search for every CollisionShape in children nodes
    node_->GetComponents<CollisionShape>(shapes, true);
    for (PODVector<CollisionShape*>::Iterator i = shapes.Begin(); i != shapes.End(); ++i)
        (*i)->NotifyRigidBody(false);

In CollisionShape.cpp:

    btCompoundShape* CollisionShape::GetParentCompoundShape()
    {
        if (!rigidBody_)
        rigidBody_ = GetComponent<RigidBody>();
        //CHANGED CODE: if there is not a rigidbody in the same node, look for a rigidbody at the top of the hierarchy
        if (!rigidBody_)
        {
            rigidBody_ = GetNode()->GetSuperParent()->GetComponent<RigidBody>();
            //GetSuperParent() returns the highest node in the hierarchy that is not the scene itself
	    }
        return rigidBody_ ? rigidBody_->GetCompoundShape() : 0;
    }

What I've been doing as a workaround is that when I parent a node at runtime, I create a copy of the CollisionShape component and attach it to the parent node with the rigidbody. However, I need to keep track of which CollisionShape copies correspond to which children, for example so that I can remove CollisionShapes when removing the child node. Would love for some guidance on this. Thanks!

-------------------------

Alex-Doc | 2017-10-11 06:11:48 UTC | #2

I've been investigating a similar issue a couple days ago, my approach was different though:
I'm using PhysicsWorld with a custom Broadphase Filter Callback which checks if the colliders are in the same hierarchy. The performance was quite bad so I dropped off the idea.

Adding a vector to PhysicsWorld containing "ignore pairs" which are the shape IDs, could be faster but I still have to try it.

-------------------------

Lumak | 2017-10-11 13:50:17 UTC | #3

Make use of Node's user var functionality:
[code]
    /// Set a user variable.
    void SetVar(StringHash key, const Variant& value);
    /// Return a user variable.
    const Variant& GetVar(StringHash key) const;
[/code]

Additionally, you might consider using:
[code]
    /// Add a pre-created component. Using this function from application code is discouraged, as component operation without an owner node may not be well-defined in all cases. Prefer CreateComponent() instead.
    void AddComponent(Component* component, unsigned id, CreateMode mode);

    /// Remove a component from this node.
    void RemoveComponent(Component* component);

[/code]

-------------------------

