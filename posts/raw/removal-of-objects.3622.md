nergal | 2017-09-30 16:44:22 UTC | #1

I'm a bit confused in what order I should remove an object where I have the following parts:
     SharedPtr<Node> node;
    SharedPtr<Model> model;
    SharedPtr<VertexBuffer> vb;
    SharedPtr<IndexBuffer> ib;
    SharedPtr<Geometry> geom;
    PODVector<VertexElement> elements;
    SharedPtr<StaticModel> object;
    SharedPtr<CollisionShape> shape;
    SharedPtr<RigidBody> body;

So I've created a model with vertexbuffers and rigidbody. At a certain point I want to remove the object. What order should I use?

I thought I could use the node->Remove(), but that crashes the program since it causes null pointers.

Any advice?

-------------------------

Eugene | 2017-09-30 21:17:59 UTC | #2

You should design your classes being able to destroy automatically. So, `node->Remove()` should work fine.
Ensure that you don't keep _any_ SharedPtr onto Nodes/Components at the moment of removal.
Usually it means that you shouldn't keep _any_ SharedPtr onto such objects longer than for a moment.

-------------------------

