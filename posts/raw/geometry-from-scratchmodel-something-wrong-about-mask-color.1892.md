elemusic | 2017-01-02 01:11:11 UTC | #1

i have read 34_DynamicGeometry example,trying to learn how to write a custom LineRender with only position and vertex color.
somehow it didn't work as expected.
i want to draw a triangle with alpha color(1,0,0,0.5f)
the result is some triangle with wrong direction,front to back,guess there maybe some vertex format mistake,i can't figure out
[code]
float vertexData[] = {
		// Position     Color
		-5, 5, 0,		1,0,0,0.5f,
		5, 5, 0,		1,0,0,0.5f,
		-5, -5, 0,		1,0,0,0.5f
	};//clock wise

	const unsigned short indexData[] = {
		0, 1, 2
	};

	const unsigned numVertices = 3;

	SharedPtr<Model> fromScratchModel(new Model(context_));
	SharedPtr<VertexBuffer> vb(new VertexBuffer(context_));
	SharedPtr<IndexBuffer> ib(new IndexBuffer(context_));
	SharedPtr<Geometry> geom(new Geometry(context_));

	vb->SetShadowed(true);
	vb->SetSize(numVertices, MASK_POSITION | MASK_COLOR);
	vb->SetData(vertexData);

	ib->SetSize(numVertices, false);
	ib->SetData(indexData);

	geom->SetVertexBuffer(0, vb, MASK_POSITION | MASK_COLOR);
	geom->SetIndexBuffer(ib);
	geom->SetDrawRange(TRIANGLE_LIST, 0, numVertices);

	fromScratchModel->SetNumGeometries(1);
	fromScratchModel->SetGeometry(0, 0, geom);

	Node* node = scene_->CreateChild("FromScratchObject");
	node->SetPosition(Vector3(3.0f, 0.0f, 0.0f));

	StaticModel* sModel = node->CreateComponent<StaticModel>();
	sModel->SetModel(fromScratchModel);
	sModel->SetMaterial(cache->GetResource<Material>("Materials/MyConstColor.xml"));
[/code]

and here is the MyConstColor.xml,just call BasicVColUnlitAlpha
[code]
<material>
    <technique name="Techniques/BasicVColUnlitAlpha.xml" />
</material>
[/code]

the problem is the color vertex format does not work as expected.

if i change for just position,it's ok.
[code]
float vertexData[] = {
		// Position
		-5, 5, 5,
		5, 5, 5,
		-5, -5, 5
	};
...
vb->SetSize(numVertices, MASK_POSITION);
geom->SetVertexBuffer(0, vb, MASK_POSITION);
...
[/code]

if i use the 34_DynamicGeometry example with position and nomal,it works as well.
[code]
float vertexData[] = {
            // Position             Normal
            0.0f, 0.5f, 0.0f,       0.0f, 0.0f, 0.0f,
            0.5f, -0.5f, 0.5f,      0.0f, 0.0f, 0.0f,
            0.5f, -0.5f, -0.5f,     0.0f, 0.0f, 0.0f
}
vb->SetSize(numVertices, MASK_POSITION|MASK_NORMAL);
geom->SetVertexBuffer(0, vb, MASK_POSITION | MASK_NORMAL);
[/code]

If add color,then everything goes wrong... :confused: 
what the problem with color?
how can i make it right?

-------------------------

codingmonkey | 2017-01-02 01:11:12 UTC | #2

Hi, you better looking into code to clarify what is color format in vertex
So open VS studio and Urho3d project, press Ctrl+F - type "CustomGeometry" and you got this:
[code]
/// Custom geometry vertex.
struct CustomGeometryVertex
{
    /// Position.
    Vector3 position_;
    /// Normal.
    Vector3 normal_;
    /// Color.
    unsigned color_;
    /// Texture coordinates.
    Vector2 texCoord_;
    /// Tangent.
    Vector4 tangent_;
};
[/code]

and then you probably may see this also:
[code]
void CustomGeometry::DefineColor(const Color& color)
{
    if (vertices_.Size() < geometryIndex_ || vertices_[geometryIndex_].Empty())
        return;

    vertices_[geometryIndex_].Back().color_ = color.ToUInt();
    elementMask_ |= MASK_COLOR;
}
[/code]

So use or keep code near with you for seeing struct format and how methods are working.

-------------------------

elemusic | 2017-01-02 01:11:18 UTC | #3

thanks codingmonkey,never thought color use unsigned int,now everything go well.

-------------------------

