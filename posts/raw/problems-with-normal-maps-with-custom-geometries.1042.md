Tinimini | 2017-01-02 01:05:01 UTC | #1

I seem to be unable to get materials with normal maps defined to show up when I have a custom geometry created from scratch. Works just fine with a material with only a diffuse map, but when you add the normal map, all you get is a black model. Attached is a quick test I made. It has one box model (created from Box.mdl) and one quad that is created from scratch. The box shows the material just fine, but the quad end up black. Any idea what's going on?

[code]
Node* boxNode = scene_->CreateChild("Box");
boxNode->SetPosition(Vector3(0, 0, 0));
Model* boxModel = cache->GetResource<Model>("Models/Box.mdl");
StaticModel* boxObject = boxNode->CreateComponent<StaticModel>();
boxObject->SetModel(boxModel);
Material *material = cache->GetResource<Material>("Materials/Stone.xml");
boxObject->SetMaterial(material);

const unsigned numVertices = 6;

float vertexData[] = {
    0.0f, 0.0f, 0.0f,    0.0f, 0.0f, -1.0f,    0.0f, 0.0f,
    0.0f, 1.0f, 0.0f,    0.0f, 0.0f, -1.0f,    0.0f, 1.0f,
    1.0f, 0.0f, 0.0f,    0.0f, 0.0f, -1.0f,    1.0f, 0.0f,
    1.0f, 1.0f, 0.0f,    0.0f, 0.0f, -1.0f,    1.0f, 1.0f,
    1.0f, 0.0f, 0.0f,    0.0f, 0.0f, -1.0f,    1.0f, 0.0f,
    0.0f, 1.0f, 0.0f,    0.0f, 0.0f, -1.0f,    0.0f, 1.0f
};

const unsigned short indexData[] = {
    0,  1,  2,
    3,  4,  5
};

SharedPtr<Model> fromScratchModel(new Model(context_));
SharedPtr<VertexBuffer> vb(new VertexBuffer(context_));
SharedPtr<IndexBuffer> ib(new IndexBuffer(context_));
SharedPtr<Geometry> geom(new Geometry(context_));
vb->SetShadowed(true);
vb->SetSize(numVertices, MASK_POSITION|MASK_NORMAL|MASK_TEXCOORD1);
vb->SetData(vertexData);

ib->SetShadowed(true);
ib->SetSize(numVertices, false);
ib->SetData(indexData);

geom->SetVertexBuffer(0, vb);
geom->SetIndexBuffer(ib);
geom->SetDrawRange(TRIANGLE_LIST, 0, numVertices);

fromScratchModel->SetNumGeometries(1);
fromScratchModel->SetGeometry(0, 0, geom);
fromScratchModel->SetBoundingBox(BoundingBox(Vector3(0.0f, 0.0f, 0.0f), Vector3(1.0f, 1.0f, 1.0f)));

Node* node = scene_->CreateChild("FromScratchObject");
node->SetPosition(Vector3(0.0f, 2.0f, 0.0f));
StaticModel* object = node->CreateComponent<StaticModel>();
object->SetModel(fromScratchModel);
Material *mat = cache->GetResource<Material>("Materials/Stone.xml");
object->SetMaterial(mat);
[/code]

-------------------------

Tinimini | 2017-01-02 01:05:01 UTC | #2

Looks like my UV coordinates where a bit messed up in my example. But that doesn't really change anything. The correct vertexData is:
[code]
float vertexData[] = {
    0.0f, 0.0f, 0.0f,    0.0f, 0.0f, -1.0f,    0.0f, 1.0f,
    0.0f, 1.0f, 0.0f,    0.0f, 0.0f, -1.0f,    0.0f, 0.0f,
    1.0f, 0.0f, 0.0f,    0.0f, 0.0f, -1.0f,    1.0f, 1.0f,
    1.0f, 1.0f, 0.0f,    0.0f, 0.0f, -1.0f,    1.0f, 0.0f,
    1.0f, 0.0f, 0.0f,    0.0f, 0.0f, -1.0f,    1.0f, 1.0f,
    0.0f, 1.0f, 0.0f,    0.0f, 0.0f, -1.0f,    0.0f, 0.0f
};
[/code]

-------------------------

cadaver | 2017-01-02 01:05:01 UTC | #3

You need valid tangents for normal mapping.

See the Tangent.cpp / Tangent.h files in Graphics subdirectory for an utility function that can calculate them. That is incompatible with a CustomGeometry though, as it wants to work directly with indexed raw vertex data. But you should be able to adapt the code for your case.

-------------------------

Tinimini | 2017-01-02 01:05:01 UTC | #4

Aah! Cool, thanks. I will take a look.

-------------------------

Tinimini | 2017-01-02 01:05:01 UTC | #5

Oh, and I'm not using CustomGeometry. I'm building the vertex & index buffers by hand and using them. Would those be eligible to be fed into the Tangent generation?

-------------------------

cadaver | 2017-01-02 01:05:01 UTC | #6

Yes. Just reserve space for tangents (4 floats for each vertex) in the vertex data, they come after the texcoords.

-------------------------

Tinimini | 2017-01-02 01:05:01 UTC | #7

Yay! It works! Thank you so much for your help.
I just added this to the test I posted:
[code]
GenerateTangents(vertexData, 12 * sizeof(float), indexData, sizeof(unsigned short), 0, numVertices, 3 * sizeof(float), 6 * sizeof(float), 8 * sizeof(float));
[/code]

A quick and dirty test with nasty hard coding, but looks like the normal maps work properly now.

-------------------------

Tinimini | 2017-01-02 01:05:01 UTC | #8

Oh, and of course in addition to that, I added the 4 floats to my vertexData

-------------------------

