napard | 2017-01-02 01:14:29 UTC | #1

Hi, I'm quite newbie with the engine, while porting an old code base to Urho3D I often get stuck despite using the examples as a guide, so...

I'd like to know how to specify a custom color per vertex, the DynamicGeometry example has not enough information as there is no color nor texture coordinates specification in vertex data for that example. Until now, I've managed to set only vertex and normal data, but adding color information does not work and the model only gets shaded/colored by the ambient light, this is what I have (not the full code):

[code]struct VertexData
{
    VertexData(float* pData, size_t pN, Urho3D::Vector3 pPosition) :
        data(pData), n(pN), position(pPosition) {}
    
    float* data;
    size_t n;
}

struct IndexData
{
    IndexData(uint16_t* pData, size_t pN) :
        data(pData), n(pN) {}

    uint16_t* data;
    size_t n;
};

std::vector<VertexData> v;
std::vector<IndexData> i;

// Vertex semantics specification.
Urho3D::PODVector<Urho3D::VertexElement> elements;
elements.Push(Urho3D::VertexElement(Urho3D::TYPE_VECTOR3, Urho3D::SEM_POSITION));
elements.Push(Urho3D::VertexElement(Urho3D::TYPE_VECTOR3, Urho3D::SEM_NORMAL));
elements.Push(Urho3D::VertexElement(Urho3D::TYPE_VECTOR4, Urho3D::SEM_COLOR));

// Vertex buffer.
Urho3D::SharedPtr<Urho3D::VertexBuffer> vb(new Urho3D::VertexBuffer(mContext));

vb->SetShadowed(true);
vb->SetSize(static_cast<unsigned int>(v.n / 10), elements); // 10 is floats per vertex
vb->SetData(v.data);
delete[] v.data;
v.data = nullptr;

// Index buffer.
Urho3D::SharedPtr<Urho3D::IndexBuffer> ib(new Urho3D::IndexBuffer(mContext));

ib->SetShadowed(true);
ib->SetSize(static_cast<unsigned int>((*i).n), false);
ib->SetData((*i).data);
delete[] (*i).data;
(*i).data = nullptr;[/code]

And a vertex entry would by:

[code]std::vector<float> vertices;

vertices.push_back(x);
vertices.push_back(y);
vertices.push_back(z);

vertices.push_back(0);
vertices.push_back(0);
vertices.push_back(1);

vertices.push_back(1.0f); // I'd like red on this vertex...
vertices.push_back(0.0f);
vertices.push_back(0.0f);
vertices.push_back(1.0f);[/code]

Thanks in advance!

-------------------------

Eugene | 2017-01-02 01:14:30 UTC | #2

Make sure that you use material with enabled vertex colors.
See DiffVCol* techniques.

-------------------------

1vanK | 2017-01-02 01:14:30 UTC | #3

[urho3d.github.io/documentation/ ... ffers.html](https://urho3d.github.io/documentation/1.6/_vertex_buffers.html)

-------------------------

