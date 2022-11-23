nergal | 2017-11-25 18:46:30 UTC | #1

I have a lot of custom geoemtries that are rebuild quite-often (voxel chunks). When I've recreated the geometry I do the following to re-create the model. Is this the correct way of doing this in Urho3d or am I doing something that gives me overhead performance wise? (Note the "isBuilt" check first where I for the first time create the object otherwise just updates the index/vertex buffers)

        if(!iisBuilt) {
            vb->SetShadowed(true);
            ib->SetShadowed(true);
            int bb = 0;
            if(size_x > size_y && size_x > size_z) {
                bb = size_x;
            } else if(size_y > size_x && size_y > size_z) {
                bb = size_y;
            } else {
                bb = size_z;
            }
            model->SetBoundingBox(BoundingBox(0, (float)bb));
            model->SetNumGeometries(1);

            elements.Push(VertexElement(TYPE_VECTOR3, SEM_POSITION));
            elements.Push(VertexElement(TYPE_VECTOR3, SEM_NORMAL));
            elements.Push(VertexElement(TYPE_VECTOR3, SEM_COLOR));

            geom->SetVertexBuffer(0, vb);
            geom->SetIndexBuffer(ib);

            model->SetGeometry(0, 0, geom);
            node->SetPosition(Vector3(from_x, from_y, from_z));
            object = node->CreateComponent<StaticModel>();
            object->SetOccluder(true);
        } else {
            vb->Release();
            ib->Release();
        }
        
        vb->SetSize(vertices.Size(), elements);
        vb->SetData(&vertexData[0]);

        ib->SetSize(vertices.Size(), false);
        ib->SetData(&indexData[0]);

        geom->SetDrawRange(TRIANGLE_LIST, 0, vertices.Size());

        Vector<SharedPtr<VertexBuffer> > vertexBuffers;
        Vector<SharedPtr<IndexBuffer> > indexBuffers;
        vertexBuffers.Push(vb);
        indexBuffers.Push(ib);

        PODVector<unsigned> morphRangeStarts;
        PODVector<unsigned> morphRangeCounts;
        morphRangeStarts.Push(0);
        morphRangeCounts.Push(0);
        model->SetVertexBuffers(vertexBuffers, morphRangeStarts, morphRangeCounts);
        model->SetIndexBuffers(indexBuffers);

        object->SetModel(model);
        ResourceCache* cache=GetSubsystem<ResourceCache>();
        object->SetMaterial(cache->GetResource<Material>("Materials/vcolors.xml"));
        object->SetCastShadows(true);

Any input would be helpful! Thanks

-------------------------

Victor | 2017-11-27 00:33:24 UTC | #2

Here's what I do for updating geometry (thread safe)
https://gist.github.com/victorholt/40a22fa3936eb66b0ba5831198aee1d1#file-custommesh-cpp-L398-L423

Tested it on voxel rendering and runs pretty fast when updating
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/8/8276543d1902dc40c6f8c15d23de4c4cb0ba9ed5.jpg'>

-------------------------

Victor | 2017-11-27 00:29:49 UTC | #3

Actually... I might need to change where I do the MutexLock in that code since you want your critical blocks to be small... Still, currently it works well.

-------------------------

nergal | 2017-11-27 20:33:38 UTC | #4

Thanks for sharing, I will compare your code with mine later and try it out :)

-------------------------

NicolasRicard | 2018-12-13 15:37:54 UTC | #5

I tried to make new custom geometry inside a thread, but after I added it to the scene, it crashes, any idea ?
@Victor: I think your project is similar to mine :slight_smile:

-------------------------

Victor | 2018-12-13 15:57:19 UTC | #6

Hey there! As long as you're not attempting any rendering, generating the vertex buffers, or setting of textures inside of another thread you should be fine. All graphical aspects of the code should be done in the main thread, however, calculations (for normals, tangents, voxels chunks, etc), can be put onto another thread.

I hope that helps! :)

-------------------------

NicolasRicard | 2018-12-13 16:26:27 UTC | #7

I create node, create Custom Geometry and create the vertices, apply materials... inside an other thread

I load textures and techniques in the main thread.

I do all the rest of the loading an other thread and I add it to the scene in the main thread.

How is it not possible to create the vertex buffers in an other thread ?

-------------------------

Sinoid | 2018-12-13 17:24:28 UTC | #8

> How is it not possible to create the vertex buffers in an other thread ?

You can't set buffer data from a thread that isn't the main thread.

-------------------------

NicolasRicard | 2018-12-13 18:51:08 UTC | #9

Actually, I can ! I just succeded.
Below is the solution for the main thread side. For the other thread, you just have not to commit CustomGeometry...
```cpp
    Urho3D::Node* tmpNode;
    if (pipeline->try_pop(tmpNode)) {
      Urho3D::PODVector<Urho3D::CustomGeometry*> components;
      tmpNode->GetComponents<Urho3D::CustomGeometry>(components, true);
      for (auto compo : components) {
        compo->Commit();
      }
      m_scene->AddChild(tmpNode);
    }
```

-------------------------

Sinoid | 2018-12-13 20:37:47 UTC | #10

~~Interesting, what renderer are you using?~~~ nvm, I overlooked the commit.

-------------------------

