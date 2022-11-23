Devy | 2018-05-01 07:26:03 UTC | #1

I'm hoping the other code will be unnecessary, but I'm trying to convert a std::vector full of Urho3D Vector3's to an array that will be used in a dynamic mesh then a model.

Here's my relevant code:

            const unsigned numVertices = vertices.size();

            std::vector<float> vertexData;
            
            for (int i=0; i < numVertices; i++){
                vertexData.push_back(vertices[i].xyz.x_);
                vertexData.push_back(vertices[i].xyz.y_);
                vertexData.push_back(vertices[i].xyz.z_);

                vertexData.push_back(vertices[i].normal.x_);
                vertexData.push_back(vertices[i].normal.y_);
                vertexData.push_back(vertices[i].normal.z_);
            }

            SharedPtr<Model> fromScratchModel(new Model(context_));
            SharedPtr<VertexBuffer> vb(new VertexBuffer(context_));
            SharedPtr<IndexBuffer> ib(new IndexBuffer(context_));
            SharedPtr<Geometry> geom(new Geometry(context_));

            // Shadowed buffer needed for raycasts to work, and so that data can be automatically restored on device loss
            vb->SetShadowed(true);
            // We could use the "legacy" element bitmask to define elements for more compact code, but let's demonstrate
            // defining the vertex elements explicitly to allow any element types and order
            PODVector<VertexElement> elements;
            elements.Push(VertexElement(TYPE_VECTOR3, SEM_POSITION));
            elements.Push(VertexElement(TYPE_VECTOR3, SEM_NORMAL));
            vb->SetSize(numVertices, elements);
            vb->SetData(vertexData.data());

            ib->SetShadowed(true);
            ib->SetSize(numVertices, false);
            ib->SetData(indices.data());

            geom->SetVertexBuffer(0, vb);
            geom->SetIndexBuffer(ib);
            geom->SetDrawRange(TRIANGLE_LIST, 0, numVertices);

            fromScratchModel->SetNumGeometries(1);
            fromScratchModel->SetGeometry(0, 0, geom);
            fromScratchModel->SetBoundingBox(BoundingBox(Vector3(-0.5f, -0.5f, -0.5f), Vector3(0.5f, 0.5f, 0.5f)));

            Node* node = scene_->CreateChild("FromScratchObject");
            node->SetPosition(Vector3(0.0f, 3.0f, 0.0f));
            auto* object = node->CreateComponent<StaticModel>();
            object->SetModel(fromScratchModel);

Here's where I got my idea for putting the vertices in a float std::vector: [https://github.com/urho3d/Urho3D/blob/218e4d7592cf8681001e795cac6672fb29fb156a/Source/Samples/34_DynamicGeometry/DynamicGeometry.cpp#L168](https://github.com/urho3d/Urho3D/blob/218e4d7592cf8681001e795cac6672fb29fb156a/Source/Samples/34_DynamicGeometry/DynamicGeometry.cpp#L168)

To explain my above code: A have a std::vector full of Urho3D Vector3's and I want to convert them to something that a dynamic mesh can use, and to do this I put each vector's components into a std::vector of floats that will later be used as an array. From the link, it looks like you are supposed to put the vertex data into an array like so: Vector3.x, Vector3.y, Vector3.z, normal.x, normal.y, normal.z then you do the same for the next 6 indexes.

My problem is that I am not getting a mesh that is correct (I can upload a picture). I'm wondering if the way I'm doing all of this is correct, or maybe I should go review my code that generates the original Vector3 std::vector. The part I'm most concerned with is the for-loop at the very top of the code.

Thanks for any help, please ask for clarification on anything!

TAGS: procedural, dynamic, mesh, vertices, vertex, list, vector, array, bounding, box, bounding-box, convert, conversion.

-------------------------

Devy | 2018-05-01 07:24:38 UTC | #2

Turns out I was not using the right number for the number of indices my mesh needed. After using the correct number my code looks like so (also added an array used for the bounding box):
                
            unsigned numVertices = vertices.size();
            unsigned numIndices = indices.size();

            std::vector<float> vertexData;
            Vector3 vert_array[numVertices];
            
            for (int i=0; i < numVertices; i++){
                vertexData.push_back(vertices[i].xyz.x_);
                vertexData.push_back(vertices[i].xyz.y_);
                vertexData.push_back(vertices[i].xyz.z_);
                vert_array[i] = vertices[i].xyz;

                vertexData.push_back(vertices[i].normal.x_);
                vertexData.push_back(vertices[i].normal.y_);
                vertexData.push_back(vertices[i].normal.z_);
            }

            SharedPtr<Model> fromScratchModel(new Model(context_));
            SharedPtr<VertexBuffer> vb(new VertexBuffer(context_));
            SharedPtr<IndexBuffer> ib(new IndexBuffer(context_));
            SharedPtr<Geometry> geom(new Geometry(context_));

            // Shadowed buffer needed for raycasts to work, and so that data can be automatically restored on device loss
            vb->SetShadowed(true);
            // We could use the "legacy" element bitmask to define elements for more compact code, but let's demonstrate
            // defining the vertex elements explicitly to allow any element types and order
            PODVector<VertexElement> elements;
            elements.Push(VertexElement(TYPE_VECTOR3, SEM_POSITION));
            elements.Push(VertexElement(TYPE_VECTOR3, SEM_NORMAL));
            vb->SetSize(numVertices, elements);
            vb->SetData(&vertexData[0]);
            

            ib->SetShadowed(true);
            ib->SetSize(numIndices, false);
            ib->SetData(&indices[0]);

            geom->SetVertexBuffer(0, vb);
            geom->SetIndexBuffer(ib);
            geom->SetDrawRange(TRIANGLE_LIST, 0, numIndices);

            fromScratchModel->SetNumGeometries(1);
            fromScratchModel->SetGeometry(0, 0, geom);

            fromScratchModel->SetBoundingBox(BoundingBox(vert_array, numVertices));

            
            Node* node = scene_->CreateChild("FromScratchObject");
            node->SetPosition(Vector3(0.0f, 3.0f, 0.0f));
            auto* object = node->CreateComponent<StaticModel>();
            object->SetModel(fromScratchModel);

Hopefully this can help someone in the future who needs to figure out how to set a bounding box and convert vertices to the correct format for a dynamic mesh.

-------------------------

