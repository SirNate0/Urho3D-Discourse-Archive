Enhex | 2017-01-02 01:07:16 UTC | #1

I'm trying to create a compound shape with SetCustomConvexHull().
What happens is as if all the vertices are combined into a single mesh, and I get a single convex hull.

[code]
// Create a collision shape for each shape, resulting compound collision
for (const auto& shape : shapes)
{
	// Get the shape's geometry
	auto collisionGeometry = node->CreateComponent<CustomGeometry>(LOCAL);
	for (const auto& vertex : shape.vertices)
	{
		Vector3 position(vertex.x, vertex.y, vertex.z);
		collisionGeometry->DefineVertex(position / scale);
	}

	// Create a collision shape
	auto collisionShape = node->CreateComponent<CollisionShape>(LOCAL);
	collisionShape->SetCustomConvexHull(collisionGeometry);
}
[/code]


If I use Set[Primitive]() or SetConvexHull, it does work as expected, creating seperate shapes.
Is it a bug with SetCustomConvexHull()?
Does a node can have only a single CustomGeometry component?

-------------------------

cadaver | 2017-01-02 01:07:16 UTC | #2

This is related to looking up the CustomGeometry in serialization. To have an unified mechanism for both immediate use and serialization, node ID's are used. It ends up looking up the same (first) customgeometry for each shape, regardless of the pointer you give.

This should be changeble to use component ID's instead.

-------------------------

Enhex | 2017-01-02 01:07:16 UTC | #3

Ok, I looked up what you said and saw it in the source code.

I want to use manually defined Urho3D::Model instead.
I haven't tried it yet, but when I looked in ConvexData::ConvexData I saw:
[code]
        geom->GetRawData(vertexData, vertexSize, indexData, indexSize, elementMask);
        if (!vertexData || !indexData)
        {
            LOGWARNING("Skipping geometry with no CPU-side geometry data for convex hull collision");
            continue;
        }
[/code]

If only vertexData is used, why would it skip if there's no indexData?
I want to get away with only defining a vertex buffer for a Model which is used exclusively for physics.

-------------------------

cadaver | 2017-01-02 01:07:16 UTC | #4

Good find, that's just the result of copypaste and can be fixed.

Preferably we should be able to create VertexBuffers with no GPU side representation for these kinds of uses.

-------------------------

cadaver | 2017-01-02 01:07:16 UTC | #5

All discussed changes are in the master branch. VertexBuffer & IndexBuffer constructors take a new optional forceHeadless parameter.

-------------------------

Enhex | 2017-01-02 01:07:16 UTC | #6

Just tested it, and compound collision shapes with CustomGeometry works.  :smiley: 

Now I wonder if there's even a reason to use Model instead of CustomGeometry?

-------------------------

cadaver | 2017-01-02 01:07:16 UTC | #7

CustomGeometry is considered an easy and slower shortcut to defining geometry. If the performance when initializing your objects is acceptable, and you're not going to use indexed geometry, and you're not going to share the same shape between multiple objects (you can however reference the same CustomGeometry from multiple collision shapes), then I see nothing wrong in using it.

-------------------------

