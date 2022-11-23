Simeon | 2022-11-04 11:34:00 UTC | #1

I would like to use Texture3D for rendering of random cuts of a 3D texture volume but the texture is always black when displayed on triangles. Even with a 3D texture I set to white, the texture on triangles is always black. If I use a standard Texture2D then it works.
Here is the test I do to see the issue (def or undef ```__3DTEXTURE__``` to switch between Texture2D and Texture3D test)
```
    auto w = 256, h = 256, d = 256;

    auto format = Graphics::GetRGBAFormat();
    constexpr std::size_t nbChannels = 4;

#ifdef __3DTEXTURE__
    auto texture = SharedPtr<Texture3D>(new Texture3D(context_));
    texture->SetNumLevels(1);
    if (!texture->SetSize(w, h, d, format)){
        spdlog::error("Failed to create texture ....");
    }
    std::vector<std::uint8_t> dataBuff(w*h*d*nbChannels, 255); // fill texture with white
    if (!texture->SetData(0, 0,0,0, w, h, d, dataBuff.data())) {
        spdlog::error("Failed to create texture ....");
    }
#else
    auto texture = SharedPtr<Texture2D>(new Texture2D(context_));
    texture->SetNumLevels(1);
    if (!texture->SetSize(w, h, format)){
        spdlog::error("Failed to create texture ....");
    }
    std::vector<std::uint8_t> dataBuff(w*h*nbChannels, 255); // fill texture with white
    if (!texture->SetData(0, 0,0, w, h, dataBuff.data())) {
        spdlog::error("Failed to create texture ....");
    }
#endif

    auto mat = SharedPtr<Material>(new Material(context_));
    mat->SetCullMode(Urho3D::CULL_NONE);
    mat->SetNumTechniques(1);
    mat->SetTechnique(0, cache_->GetResource<Technique>("Techniques/DiffUnlitAlpha.xml"));
    mat->SetTexture(TextureUnit::TU_DIFFUSE, texture);

    std::vector<float> vertexData;

    // 2 triangles for a quad ...
    std::vector<std::array<Vector3,3>> trianglesTextureCoords = {
        {Vector3{0,0,0.5},
         Vector3{1,0,0.5},
         Vector3{0,1,0.5}},
        {Vector3{0,1,0.5},
         Vector3{1,0,0.5},
         Vector3{1,1,0.5}}
    };

    for (auto const& t : trianglesTextureCoords) {
        for (auto const& v: t) {
            // vertex
            vertexData.emplace_back(0.5*(v.x_-0.5));
            vertexData.emplace_back(0.5*(v.y_-0.5));
            vertexData.emplace_back(v.z_);
            // normal
            vertexData.emplace_back(0);
            vertexData.emplace_back(0);
            vertexData.emplace_back(1);
            // texture coordindates
            vertexData.emplace_back(v.x_);
            vertexData.emplace_back(v.y_);
#ifdef __3DTEXTURE__
            vertexData.emplace_back(v.z_);
#endif
        }
    }

    std::vector<unsigned> indexData = {0,1,2,3,4,5};

    Urho3D::SharedPtr<Urho3D::Model> model(new Urho3D::Model(context_));
    Urho3D::SharedPtr<Urho3D::VertexBuffer> vb(new Urho3D::VertexBuffer(context_));
    Urho3D::SharedPtr<Urho3D::IndexBuffer> ib(new Urho3D::IndexBuffer(context_));
    Urho3D::SharedPtr<Urho3D::Geometry> geom(new Urho3D::Geometry(context_));

    vb->SetShadowed(true);
    Urho3D::PODVector<Urho3D::VertexElement> elements;

    elements.Push(Urho3D::VertexElement(Urho3D::TYPE_VECTOR3, Urho3D::SEM_POSITION));
    elements.Push(Urho3D::VertexElement(Urho3D::TYPE_VECTOR3, Urho3D::SEM_NORMAL));
#ifdef __3DTEXTURE__
    elements.Push(Urho3D::VertexElement(Urho3D::TYPE_VECTOR3, Urho3D::SEM_TEXCOORD));
#else
    elements.Push(Urho3D::VertexElement(Urho3D::TYPE_VECTOR2, Urho3D::SEM_TEXCOORD));
#endif
    vb->SetSize(trianglesTextureCoords.size()*3, elements);
    vb->SetData(&vertexData[0]);

    ib->SetShadowed(true);
    ib->SetSize(indexData.size(), true);
    ib->SetData(&indexData[0]);

    geom->SetVertexBuffer(0, vb);
    geom->SetIndexBuffer(ib);
    geom->SetDrawRange(Urho3D::TRIANGLE_LIST, 0, indexData.size());

    model->SetNumGeometries(1);
    model->SetGeometry(0, 0, geom);

    Urho3D::Vector<Urho3D::SharedPtr<Urho3D::VertexBuffer> > vertexBuffers;
    Urho3D::Vector<Urho3D::SharedPtr<Urho3D::IndexBuffer> > indexBuffers;
    vertexBuffers.Push(vb);
    indexBuffers.Push(ib);

    Urho3D::PODVector<unsigned> morphRangeStarts;
    Urho3D::PODVector<unsigned> morphRangeCounts;
    morphRangeStarts.Push(0);
    morphRangeCounts.Push(0);
    model->SetVertexBuffers(vertexBuffers, morphRangeStarts, morphRangeCounts);
    model->SetIndexBuffers(indexBuffers);

    auto planeNode = node->CreateChild();
    planeNode->SetPosition(Vector3(0,0,0.1));
    auto* planeObject = planeNode->CreateComponent<StaticModel>();
    planeObject->SetModel(model);
    planeObject->SetMaterial(mat);

    // add big background to see the texture if black ...
    {
        auto background = node->CreateChild();
        background->SetPosition(Vector3(0,0,10));
        background->Rotate(Quaternion(90.,{1,0,0}));
        background->SetScale(10000);
        auto* planeObject = background->CreateComponent<StaticModel>();
        planeObject->SetModel(cache_->GetResource<Model>("Models/Plane.mdl"));
        auto m = SharedPtr<Material>(new Material(context_));
        m->SetShaderParameter("MatDiffColor", Color(0.3,0.3,1.));
        m->SetFillMode(Urho3D::FillMode::FILL_SOLID);
        m->SetCullMode(CULL_NONE);
        planeObject->SetMaterial(m);
    }

```
Is there something wrong in my use of Texture3D?

-------------------------

Simeon | 2022-11-04 12:22:05 UTC | #2

The issue may come from the shaders that do not support 3D texture coordinates. Any idea how to do it ?

-------------------------

SirNate0 | 2022-11-04 14:30:42 UTC | #3

I think you are not using a Technique for the Material that will use the sampler3D for your texture. There's a VolumeMap sampler that you can map your texture to fit the material if you don't want to have to make extra changes. I don't know if any of the Techniques/Shaders that come with the engine use it however, so you may have to write your own shader to use it. A very brief search makes it look like only the ColorCorrection shader makes use of it.

Alternatively, change your shader to use the 3d sampler for the diffuse unit (Samplers.glsl - copy to another file and include that instead).

-------------------------

Simeon | 2022-11-04 15:44:32 UTC | #4

Ok. Tank you for the answer.
The main issue I have when doing a new shader is how to use 3D texture coordinates  because ```iTextCoord``` in glsl is 2D and not 3D and  :
```
elements.Push(Urho3D::VertexElement(Urho3D::TYPE_VECTOR3, Urho3D::SEM_TEXCOORD));
```
do not feed a shader variable. Using an other existing variable (ex: `Urho3D::SEM_NORMAL`) the 3D texture works if I use the `iNormal` for texture coordinates. I do not found where  the mapping between shaders variables and `Urho3D::VertexElement` is done. Do you know where is it done ?

-------------------------

SirNate0 | 2022-11-04 16:12:59 UTC | #5

**Answering where what you need to edit is**
Generally in Transforms.glsl. Your specific shader may vary, but Basic.glsl, LitSolid.glsl, etc. use that. You could maybe use the CubeTexCoord, but I'm not sure what else uses it.

https://github.com/urho3d/Urho3D/blob/master/bin/CoreData/Shaders/GLSL/Transform.glsl#L16

---
**Answering where the mapping is done**
I believe the actual mapping is handled by this code, but you probably shouldn't change it.
https://github.com/urho3d/Urho3D/blob/544ce6a558a034decf92e2684168e3d1c848666e/Source/Urho3D/GraphicsAPI/OpenGL/OGLShaderProgram.cpp#L139-L172

-------------------------

