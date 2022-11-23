Kest | 2022-05-14 20:09:04 UTC | #1

Hello, I'm trying to get this custom mesh importer to work. It sorta' works but does not display things right, an example being: 

![example.PNG|690x350](upload://cEAmbB0dsktmSNzLAciw038gbVl.jpeg)

Code is here, if anyone can point out my errors I'd greatly appreciate it! I'm still trying to learn the good the engine can provide!

```c++
void RMesh::LoadRMesh(const String& filepath)
{
    FileSystem* fsys = new FileSystem(context_);
    File source(context_, fsys->GetProgramDir() + filepath, FILE_READ);
    const String file = source.GetName();

    String header = ReadBlitzString(source);
    URHO3D_LOGINFO(header);

    if (header != "RoomMesh") //Check if the file is a valid RMesh file.
    {
        URHO3D_LOGERROR(file + " is not a valid RMesh!");
        return;
    }

    SharedPtr<Model> model(new Model(context_));
    unsigned int vertexDecl = MASK_POSITION;

    int meshcount = source.ReadInt();
    model->SetNumGeometries(meshcount);

    for (int i = 0; i < meshcount; i++)
    {
        SharedPtr<Geometry> geom(new Geometry(context_));

        //List the datatypes in the vertex vector.
        //unsigned int vertexDecl = MASK_POSITION;

        URHO3D_LOGINFO("RMESH LOOP: " + (String)(i + 1));

        for (int j = 0; j < 2; j++)
        {
            byte texflag = source.ReadUByte();
            if (texflag != 0)
            {
                String texString = ReadBlitzString(source);
                if (!texString.Empty())
                {
                    URHO3D_LOGINFO("Texture found: " + texString);
                }
            }
        }

        Vector<float> vertData_;

        int vertcount = source.ReadInt();
        for (int j = 0; j < vertcount; j++)
        {
            //URHO3D_LOGINFO("Reading vertex loop: " + (String)(j + 1));
            float x = source.ReadFloat();
            float y = source.ReadFloat();
            float z = source.ReadFloat();

            Vector3 pos = Vector3(x, y, z);
            vertData_.Push(pos.x_);
            vertData_.Push(pos.y_);
            vertData_.Push(pos.z_);

            for (int k = 0; k < 2; k++)
            {
                float u = source.ReadFloat();
                float v = source.ReadFloat();
                Vector2 uv = Vector2(u, v);

                //vertData_.Push(uv.x_);
                //vertData_.Push(uv.y_);
            }

            byte r = source.ReadUByte();
            byte g = source.ReadUByte();
            byte b = source.ReadUByte();
            Vector3 color = Vector3(r, g, b);

            //vertData_.Push(color.x_);
            //vertData_.Push(color.y_);
            //vertData_.Push(color.z_);
        }

        Vector<uint> indData_;

        int tricount = source.ReadInt();
        for (int j = 0; j < tricount; j++)
        {
            //URHO3D_LOGINFO("Reading index loop: " + (String)(j + 1));
            int tri1 = source.ReadInt();
            int tri2 = source.ReadInt();
            int tri3 = source.ReadInt();

            Vector3 poly = Vector3(tri1, tri2, tri3);

            indData_.Push(tri1);
            indData_.Push(tri2);
            indData_.Push(tri3);
        }

        SharedPtr<VertexBuffer> vertexBuf(new VertexBuffer(context_));
        vertexBuf->SetShadowed(true);
        vertexBuf->SetSize(vertcount, vertexDecl);
        vertexBuf->SetData(&vertData_[0]);

        URHO3D_LOGINFOF("Vertex buffer done in loop %d.", i);

        SharedPtr<IndexBuffer> indexBuf(new IndexBuffer(context_));
        indexBuf->SetShadowed(true);
        indexBuf->SetSize(tricount, false);
        indexBuf->SetData(&indData_[0]);

        URHO3D_LOGINFOF("Index buffer done in loop %d.", i);

        geom->SetVertexBuffer(0, vertexBuf);
        geom->SetIndexBuffer(indexBuf);
        geom->SetDrawRange(TRIANGLE_LIST, 0, tricount);


        URHO3D_LOGINFOF("Geometry done in loop %d, setting model geometry.", i);

        model->SetGeometry(i, 0, geom);
        model->SetNumGeometryLodLevels(i, 1);
    }

    URHO3D_LOGINFO("Seems successful, committing...");

    StaticModel* mesh = node_->CreateComponent<StaticModel>();

    mesh->SetModel(model);

    URHO3D_LOGINFO("Done with " + file);
}
```

-------------------------

SirNate0 | 2022-05-13 02:31:43 UTC | #2

To me it looks like it's probably a problem with the index buffer. Are you sure the indices can be read directly (e.g. Object files indices start at 1 instead of 0)? And does the size of your uint match the large (32 bit) vs not large (16 bit) setting of your index buffer?

Additionally, I'm pretty sure `indexBuf->SetSize(tricount, false);` should use the number of indices so 3x the number of triangles.

-------------------------

JSandusky | 2022-05-13 03:34:22 UTC | #3

If it's legacy data it could be triangle-stripified from back when that was a win. That tower bit unless the vertex data is completely wrong stinks of triangle strips (you see weird patterns like that come out).

-------------------------

Kest | 2022-05-13 20:26:12 UTC | #4

Thanks to all who replied!

The problem was that it read data as an Int instead of what it's actually referred to as an ushort.

-------------------------

