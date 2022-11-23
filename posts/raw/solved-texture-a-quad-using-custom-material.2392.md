napard | 2017-01-02 01:15:09 UTC | #1

How can I texture a quad using custom material and specified texture?
Which image formats are supported?
Is there an example for this somewhere? ...

-------------------------

Sir_Nate | 2017-01-02 01:15:09 UTC | #2

Do you mean a quad like the screen, or an arbitrary quadrilateral within the world?

-------------------------

napard | 2017-01-02 01:15:09 UTC | #3

I mean as per vertex texture coordinates on a quad mesh model, as simple as that. I have some custom geometry model and I'd like to apply a texture on it, dunno where to start...

In detail, this is what I'm trying to achieve:

[code]    
    // How do I create or reuse a material which accepts vertex color AND texture coordinates?
    // Are those inputs compatible together? Are they mutually exclusive?

    Urho3D::PODVector<Urho3D::VertexElement> elements;
    elements.Push(Urho3D::VertexElement(Urho3D::TYPE_VECTOR3, Urho3D::SEM_POSITION));
    elements.Push(Urho3D::VertexElement(Urho3D::TYPE_VECTOR3, Urho3D::SEM_NORMAL));
    elements.Push(Urho3D::VertexElement(Urho3D::TYPE_VECTOR4, Urho3D::SEM_COLOR));    // Vertex color.
    elements.Push(Urho3D::VertexElement(Urho3D::TYPE_VECTOR2, Urho3D::SEM_TEXCOORD)); // Tex coords.

    Urho3D::SharedPtr<Urho3D::VertexBuffer> vb(new Urho3D::VertexBuffer(mContext));

    vb->SetShadowed(true);
    vb->SetSize(static_cast<unsigned int>((*v).second.n / 12), elements);
    vb->SetData((*v).second.data);
    delete[] (*v).second.data;
    (*v).second.data = nullptr;

    Urho3D::SharedPtr<Urho3D::IndexBuffer> ib(new Urho3D::IndexBuffer(mContext));

    ib->SetShadowed(true);
    ib->SetSize(static_cast<unsigned int>((*i).second.n), false);
    ib->SetData((*i).second.data);
    delete[] (*i).second.data;
    (*i).second.data = nullptr;

    mGeometry = Urho3D::SharedPtr<Urho3D::Geometry>(new Urho3D::Geometry(mContext));

    mGeometry->SetVertexBuffer(0, vb);
    mGeometry->SetIndexBuffer(ib);
    mGeometry->SetDrawRange(Urho3D::TRIANGLE_LIST, 0, static_cast<unsigned int>((*i).second.n));
    i++;

    Urho3D::SharedPtr<Urho3D::Model> model(new Urho3D::Model(mContext));

    model->SetNumGeometries(1);
    model->SetGeometry(0, 0, mGeometry);

    Urho3D::Node* node = mScene->CreateChild();

    node->SetPosition(Urho3D::Vector3((*v).first.x, (*v).first.y, (*v).first.z));

    Urho3D::StaticModel* object = node->CreateComponent<Urho3D::StaticModel>();
    object->SetModel(model);

    Urho3D::ResourceCache* res_cache = node->GetSubsystem<Urho3D::ResourceCache>();


    // How do I create or reuse a material which accepts vertex color AND texture coordinates?
    // Which technique is valid for that?
    Urho3D::SharedPtr<Urho3D::Material> material(new Urho3D::Material(mContext));
    material->SetTechnique(0, res_cache->GetResource<Urho3D::Technique>(
        //"Techniques/NoTextureVCol.xml"
        //"Techniques/DiffVCol.xml"
	// ...
        ));


        object->SetMaterial(material);
[/code]

-------------------------

napard | 2017-01-02 01:15:11 UTC | #4

Nevermind, I figured it out at last...

-------------------------

