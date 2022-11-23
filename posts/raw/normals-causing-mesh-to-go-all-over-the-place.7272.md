Kest | 2022-05-30 22:50:15 UTC | #1

Hello again, I bring an issue that's recently come up. So I've been working on my mesh importer and everything is working properly, except for defining normals. I've calculated the normals automatically and they seem to be right, but one issue is that when I apply them to the Vertex Data, it spawns this.

![fdgfsd|593x500](upload://1qPuplVG1BYmueVmwLuOM3T6SoK.png)

I have this defining the features of the model.
```
unsigned elements = MASK_POSITION | MASK_TEXCOORD1 | MASK_TEXCOORD2 | MASK_NORMAL;
```

I've been looking for answers about this, I'm thinking that it's not in the proper order or something, but if someone is able to suggest something I'd greatly appreciate it. Thanks!

-------------------------

extobias | 2022-05-31 01:16:26 UTC | #2

Hi,
Maybe trying with renderdoc could give a hint about whats going on.

-------------------------

Kest | 2022-05-31 03:32:43 UTC | #3

I'm unfamiliar with RenderDoc, should I show the code to make it easier or would you rather RenderDoc?

-------------------------

Eugene | 2022-05-31 06:00:40 UTC | #4

Yeah, but how to you fill the data itself? Note that order of vertex elements in mask is irrelevant, you should fill stuff in predefined order. See VertexBuffer.cpp code.

-------------------------

Kest | 2022-06-02 17:00:27 UTC | #5

Hello, I'm currently setting this to the side, though I will come back to this later. Though if you want to take a look I'll leave this here.

```
for (int i = 0; i < meshcount; i++)
    {
        SharedPtr<Geometry> geom(new Geometry(context_));

        URHO3D_LOGINFO("RMESH LOOP: " + (String)(i + 1));

        for (int j = 0; j < 2; j++)
        {
            byte texflag = source.ReadUByte();
            if (texflag != 0)
            {
                String texString = ReadBlitzString(source);
                if (!texString.Empty())
                {
                    texString.Replace(".jpg", "");
                    texString.Replace(".png", "");
                    URHO3D_LOGINFO("Texture found: " + texString);

                    if (texString.Contains("_lm"))
                    {
                        mat = readMaterial(texString);
                        if (!lmMats.Contains(mat))
                        {
                            URHO3D_LOGDEBUG("Getting Lightmap!");
                            lmMats.Push(mat);
                        }
                    }
                    else
                    {
                        mat = readMaterial(texString);
                        brushMats.Push(mat);
                    }
                }
            }
        }

        //Visible
        Vector<float> vertData_;
        //Vector3 normal = Vector3(0, 1, 0);
        int vertcount = source.ReadInt();
        for (int j = 0; j < vertcount; j++)
        {
            //URHO3D_LOGINFO("Reading vertex loop: " + (String)(j + 1));
            float x = source.ReadFloat();
            float y = source.ReadFloat();
            float z = source.ReadFloat();

            vertices.Push(Vector3(x, y, z));

            float Diffu = source.ReadFloat();
            float Diffv = source.ReadFloat();

            float LMu = source.ReadFloat();
            float LMv = source.ReadFloat();

            //URHO3D_LOGDEBUGF("UV: %s", uv.ToString());

            //Gonna' see on how to make this work. -Kest
            byte r = source.ReadUByte();
            byte g = source.ReadUByte();
            byte b = source.ReadUByte();
            Color color = Color(r, g, b);

            //Push into vertData_
            vertData_.Push(x);
            vertData_.Push(y);
            vertData_.Push(z);

            //vertData_.Push(normal.x_);
            //vertData_.Push(normal.y_);
            //vertData_.Push(normal.z_);

            vertData_.Push(Diffu);
            vertData_.Push(Diffv);

            vertData_.Push(LMu);
            vertData_.Push(LMv);

            bb.Merge(Vector3(x, y, z));
        }

        Vector<ushort> indData_;

        int tricount = source.ReadInt();
        for (int j = 0; j < tricount; j++)
        {
            ushort tri1 = (ushort)source.ReadInt();
            ushort tri2 = (ushort)source.ReadInt();
            ushort tri3 = (ushort)source.ReadInt();

            indData_.Push(tri1);
            indData_.Push(tri2);
            indData_.Push(tri3);

            Vector3 v0 = vertices[tri1];
            Vector3 v1 = vertices[tri2];
            Vector3 v2 = vertices[tri3];

            Vector3 d1 = v0 - v1;
            Vector3 d2 = v2 - v1;

            Vector3 normal = d1.CrossProduct(d2).Normalized();

            vertData_.Push(normal.x_);
            vertData_.Push(normal.y_);
            vertData_.Push(normal.z_);
        }

        unsigned elements = MASK_POSITION | MASK_NORMAL | MASK_TEXCOORD1 | MASK_TEXCOORD2;

        SharedPtr<VertexBuffer> vertexBuf(new VertexBuffer(context_));
        vertexBuf->SetShadowed(true);
        vertexBuf->SetSize(vertcount, elements);
        vertexBuf->SetData(&vertData_[0]);

        URHO3D_LOGINFOF("Vertex buffer done in loop %d.", i + 1);

        SharedPtr<IndexBuffer> indexBuf(new IndexBuffer(context_));
        indexBuf->SetShadowed(true);
        indexBuf->SetSize(tricount * 3, false);
        indexBuf->SetData(&indData_[0]);

        URHO3D_LOGINFOF("Index buffer done in loop %d.", i + 1);

        geom->SetVertexBuffer(0, vertexBuf);
        geom->SetIndexBuffer(indexBuf);
        geom->SetDrawRange(TRIANGLE_LIST, 0, tricount * 3);

        URHO3D_LOGINFOF("Geometry done in loop %d, setting model geometry.", i + 1);

        model->SetGeometry(i, 0, geom);
        model->SetNumGeometryLodLevels(i, 1);
    }
```

-------------------------

Eugene | 2022-06-03 06:57:26 UTC | #6

This is default order of elements:
![image|690x262](upload://sZRf5wVohcFRX2vIs2lykpX2jfl.png)
So you need to shuffle your write code according to it.

The possible caveat is reading code. If you are reading arbitrary mesh, elements theoretically may be stored in arbitrary order, and you have to check exact elements, offsets and types to get exact bytes.

If your original buffer consists only of legacy elements in specific order (like on picture), it's okay to read it as you do it.

-------------------------

elix22 | 2022-06-03 09:42:18 UTC | #7

unsigned elements = MASK_POSITION | MASK_NORMAL |  MASK_TEXCOORD1 | MASK_TEXCOORD2 | ;

You are defining the above elements   , **Position , Normal , 2 UV channels** 
But your code doesn't reflect that , where is this Color coming from ?
You are writing your generated normal at the end (in the vertData) , but it must be written immediately after the Position. 
 
@Eugene  is right , the order and byte size and Element mask must reflect your model .

You can look at these links for reference.
https://github.com/urho3d/Urho3D/blob/master/Source/Tools/AssetImporter/AssetImporter.cpp#L2476
https://github.com/urho3d/Urho3D/blob/master/Source/Tools/AssetImporter/AssetImporter.cpp#L2406

In addition for each VertexBuffer  you create/write , you must set both the vertices count and element mask

See
https://github.com/urho3d/Urho3D/blob/master/Source/Tools/AssetImporter/AssetImporter.cpp#L1032
https://github.com/urho3d/Urho3D/blob/master/Source/Tools/AssetImporter/AssetImporter.cpp#L1046
https://github.com/urho3d/Urho3D/blob/master/Source/Tools/AssetImporter/AssetImporter.cpp#L1057

-------------------------

