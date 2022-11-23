napard | 2017-01-02 01:15:20 UTC | #1

I have a model with a custom generated geometry, it is created and attached as a child of the main scene object like this (You have seen this code before in my previous posts):

[code]                Urho3D::PODVector<Urho3D::VertexElement> elements;
                elements.Push(Urho3D::VertexElement(Urho3D::TYPE_VECTOR3, Urho3D::SEM_POSITION));
                elements.Push(Urho3D::VertexElement(Urho3D::TYPE_VECTOR3, Urho3D::SEM_NORMAL));
                elements.Push(Urho3D::VertexElement(Urho3D::TYPE_VECTOR4, Urho3D::SEM_COLOR));
                elements.Push(Urho3D::VertexElement(Urho3D::TYPE_VECTOR2, Urho3D::SEM_TEXCOORD));

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

                Urho3D::Node* _node;
                mNodes.push_back(_node = mScene->CreateChild());

                _node->SetPosition(Urho3D::Vector3((*v).first.x, (*v).first.y, (*v).first.z));

                Urho3D::StaticModel* object = _node->CreateComponent<Urho3D::StaticModel>();
                object->SetModel(model);

                Urho3D::ResourceCache* res_cache = _node->GetSubsystem<Urho3D::ResourceCache>();

                Urho3D::Material* material = res_cache->GetResource<Urho3D::Material>(
                    "Materials/mat1.xml");
                
                object->SetMaterial(material);
[/code]

Now, I'd like to know how to free the attached node and all of its resources correctly, I mean, I'm afraid it could be a leak somewhere if it isn't done in the correct order or I miss something. This is the freeing part:

[code]        
        // 'n' is the node being freed...

        // Get static model.
        auto static_model = n->GetComponent<Urho3D::StaticModel>();
        // Get model.
        auto model = static_model->GetModel();
        // Get geometry.
        auto geometry = model->GetGeometry(0, 0);
    
        // Clear geometry.
        geometry->SetIndexBuffer(nullptr);
        geometry->SetVertexBuffer(0, nullptr);

        // Set null geom to model.
        model->SetGeometry(0, 0, nullptr);
        model->SetNumGeometries(0);

        // Set null material to static model.
        static_model->SetMaterial(nullptr);
        // Set null model to static model.
        static_model->SetModel(nullptr);

        // Remove static model from node.
        n->RemoveComponent(static_model);
    
        // Are these already freed here???
        //delete geometry;
        //delete model;
        //delete static_model;

        // Remove node from main scene.
        mScene->RemoveChild(n);
[/code]

Could anyone please tell me if this deallocation scheme is correct?

Thanks

-------------------------

