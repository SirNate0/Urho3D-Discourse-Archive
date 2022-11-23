slapin | 2017-01-02 01:14:14 UTC | #1

Regarding my city generation topic I have a set of small-scale questions regarding Urho3D
and best practices to do things.

The first question is - how can I create Model so I can use several materials with it,
but it should be single model still. I know it is related to Geometry, so Model should contain Geometry for each material.
But I have problems setting-up proper model, as I don't really understand how to set up VertexBuffer and IndexBuffer for
this configuration, what is actual sequence? I could not find any code sample about this :frowning:
I'd be very happy to see AngelScript code sample for this.

What I do to dissect such model:

[code]
class DissectModel {
    String name;
    Model@ model;
    Geometry@ geometry;
    VertexBuffer@[] buffers;
    float[] vertex_data;
    uint16[] index_data;
    VectorBuffer[] vertexdata;
    Array<Vector3> verts;
    IndexBuffer@ ib;
    uint16[] index;
    DissectModel(String fn, int geonum)
    {
        model = cache.GetResource("Model", fn);
        geometry = model.GetGeometry(geonum, 0);
        ib = geometry.indexBuffer;
        VectorBuffer indexdata = ib.GetData();
        for(int i = 0; i < geometry.numVertexBuffers; i++) {
            buffers.Push(geometry.vertexBuffers[i]);
            vertexdata.Push(geometry.vertexBuffers[i].GetData());
            uint num_verts = geometry.vertexBuffers[i].vertexCount;
            uint vertex_size = geometry.vertexBuffers[i].vertexSize;
            Print("num_verts: " + String(num_verts));
            Print("vertexSize: " + String(vertex_size));
            if (buffers[i].HasElement(TYPE_VECTOR3, SEM_POSITION))
                Print("Has position at " +
                    String(buffers[i].GetElementOffset(TYPE_VECTOR3, SEM_POSITION)));
            else
                continue;
            if (buffers[i].HasElement(TYPE_VECTOR3, SEM_NORMAL))
                Print("Has normal at " +
                    String(buffers[i].GetElementOffset(TYPE_VECTOR3, SEM_NORMAL)));
            else
                continue;
            if (buffers[i].HasElement(TYPE_VECTOR2, SEM_TEXCOORD))
                Print("Has texture coordinate  at " +
                    String(buffers[i].GetElementOffset(TYPE_VECTOR2, SEM_TEXCOORD)));
            for (int j = 0; j < num_verts; j++) {
                vertexdata[i].Seek(j * vertex_size + buffers[i].GetElementOffset(TYPE_VECTOR3, SEM_POSITION));
                verts.Push(vertexdata[i].ReadVector3());
                vertexdata[i].Seek(j * vertex_size + buffers[i].GetElementOffset(TYPE_VECTOR3, SEM_NORMAL));
                verts.Push(vertexdata[i].ReadVector3());
            }
            indexdata.Seek(geometry.indexStart * ib.indexSize);
            for (int j = 0; j < geometry.indexCount; j++) {
                uint16 idx = indexdata.ReadUShort();
                Print("Index: " + String(j) + " idx: " + String(idx));
                index.Push(idx);
            }
        }
    }
    Array<Vector3> get_vertices(Vector3 offt = Vector3())
    {
        Array<Vector3> ret;
        for(int i = 0; i < index.length; i++) {
            ret.Push(verts[index[i] * 2] + offt);
        }
        return ret;
    }
}
[/code]

And I use the following code to generate single-geometry model"
[code]
mixin class ScratchModel {
    float[] vertex_data;
    uint16[] index_data;
    BoundingBox bbox = BoundingBox(Vector3(0.0, 0.0, 0.0), Vector3(1.0, 1.0, 1.0));
    int num_vertices()
    {
        return vertex_data.length / 6;
    }
    Model@ model = Model();
    void create()
    {
        for (uint i = 0; i < num_vertices(); i += 3) {
            Vector3 v1(vertex_data[6 * i], vertex_data[6 * i + 1], vertex_data[6 * i + 2]);
            Vector3 v2(vertex_data[6 * i + 6], vertex_data[6 * i + 7], vertex_data[6 * i + 8]);
            Vector3 v3(vertex_data[6 * i + 12], vertex_data[6 * i + 13], vertex_data[6 * i + 14]);

            Vector3 edge1 = v1 - v2;
            Vector3 edge2 = v1 - v3;
            Vector3 normal = edge1.CrossProduct(edge2).Normalized();
            vertex_data[6 * i + 3] = vertex_data[6 * i + 9] = vertex_data[6 * i + 15] = normal.x;
            vertex_data[6 * i + 4] = vertex_data[6 * i + 10] = vertex_data[6 * i + 16] = normal.y;
            vertex_data[6 * i + 5] = vertex_data[6 * i + 11] = vertex_data[6 * i + 17] = normal.z;
        }
        VertexBuffer@ vb = VertexBuffer();
        IndexBuffer@ ib = IndexBuffer();
        Geometry@ geom = Geometry();

        vb.shadowed = true;
        Array<VertexElement> elements;
        elements.Push(VertexElement(TYPE_VECTOR3, SEM_POSITION));
        elements.Push(VertexElement(TYPE_VECTOR3, SEM_NORMAL));
        vb.SetSize(num_vertices(), elements);
        VectorBuffer temp;
        for (uint i = 0; i < vertex_data.length; ++i)
            temp.WriteFloat(vertex_data[i]);
        vb.SetData(temp);

        ib.shadowed = true;
        ib.SetSize(num_vertices(), false);
        temp.Clear();
        for (uint i = 0; i < num_vertices(); ++i)
            temp.WriteUShort(index_data[i]);
        ib.SetData(temp);

        geom.SetVertexBuffer(0, vb);
        geom.SetIndexBuffer(ib);
        geom.SetDrawRange(TRIANGLE_LIST, 0, num_vertices());
        model.numGeometries = 1;
        model.SetGeometry(0, 0, geom);
        model.boundingBox = bbox;
    }
    void add_vertex(Vector3 v)
    {
        vertex_data.Push(v.x);
        vertex_data.Push(v.y);
        vertex_data.Push(v.z);
        for (int i = 0; i < 3; i++)
            vertex_data.Push(0);
        uint16 idx = index_data.length;
        index_data.Push(idx);
    }
}
class Triangle : ScratchModel {
    Node@ node = Node();
    StaticModel@ object;
    float[] vertex_data = {
        0, 0, 0,   0, 0, 0,
        0, 1, 0,   0, 0, 0,
        1, 0, 0,   0, 0, 0,
    };
    uint16[] index_data = {
        0, 1, 2
    };
    BoundingBox bbox = BoundingBox(Vector3(0.0, 0.0, 0.0), Vector3(1.0, 1.0, 0.0));
    Triangle()
    {
        create();
        object = node.CreateComponent("StaticModel");
        object.model = model;
    }
}
[/code]

So I need to extend it to have multiple Geometry to use multiple materials. I know VertexBuffer and IndexBuffer can be shared with all
geometries (but I don't understand if it is mandatory, I'm very new to the subject). Any ideas?
Any help will be appreciated.

-------------------------

horvatha4 | 2017-01-02 01:14:14 UTC | #2

Hi!
If I should something recommend to you, make a friendship with the C++.

Now I working around this thema too, so what I use to start is this:
[code]
// first create a Node
		Node* no = scene_->CreateChild("path");
		Vector3 pos(0, 0, 0);
		pos.y_ = set_any_height_you_want;
		no->SetPosition(pos);
		no->SetRotation(Quaternion(0, 10, 0));// rotate Node 10 grad clockwise around the Y/Up

// then a CustomGeometry Component
		CustomGeometry *cg = no->CreateComponent<CustomGeometry>();
		cg->SetNumGeometries(1);
		cg->SetMaterial(rCache_->GetResource<Material>("Materials/NoTexUnlitVCol.xml"));
		cg->BeginGeometry(0, TRIANGLE_STRIP);// <- from this line I declare the 1. geometry, I give its type too. Look in: Urho3D\Source\Urho3D\Graphics\GraphicsDefs.h

		cg->DefineVertex(Vector3( 1.0f, 2.0f, 0.0f));// first vector pos
		 cg->DefineColor(Color  ( 1.0f, 0.0f, 0.0f));// first vector color
		cg->DefineVertex(Vector3(-1.0f, 2.0f, 0.0f));// second vector pos
		 cg->DefineColor(Color  ( 0.0f, 1.0f, 0.0f));// second vector color ... and so on
		cg->DefineVertex(Vector3( 1.0f, 2.0f, 1.0f));
		 cg->DefineColor(Color  ( 1.0f, 1.0f, 0.0f));
		cg->DefineVertex(Vector3(-1.0f, 2.0f, 1.0f));
		 cg->DefineColor(Color  ( 0.0f, 0.0f, 1.0f));
		cg->Commit();// end the geometry. I think it close all opened Geometries too.
		cg->SetCastShadows(false); // don't need shadows
[/code]

What is important is set the Material. I made a new one. Its called "NoTexUnlitVCol.xml". Stored in "......\bin\Data\Materials".
Its just 3 lines:
[code]
<material>
    <technique name="Techniques/NoTextureUnlitVCol.xml" />
</material>
[/code]

And the result:
[img]http://www.pts-club.com/static/HORVATHA4/pics/vl2016091801.png[/img]

I don't need lights, normals, textures and tangents, but you can set all them, vector to vector, one by one. As you wish. Just don't forget to set the Material too.

As I see in the videos, you don't need so detailed windows. There is a techic, "normal bumpmap". Maybe you need just make cubes and play with its textures.

Arpi

-------------------------

cadaver | 2017-01-02 01:14:14 UTC | #3

You can use different Geometry objects to define different draw ranges into the same vertex & index buffers.

CustomGeometry component is sort of the "learning wheels" version of defining geometry and not recommended for large data amounts. If for example your city repeats the same building multiple times, by defining it as an actual programmatically created Model resource you will get the benefit of instancing.

-------------------------

slapin | 2017-01-02 01:14:15 UTC | #4

Thanks a lot for explanation. I already use Model resource.
What should I modify in my code to add another Geometry there?
I see the situation like this:

1. I create VertexBuffer and IndexBuffer, fill them with data of first Geometry
2. Create Geometry
3. Set IndexBuffer and VertexBuffer to Geometry.
4. SetRange
5. Create Model and set Geometry there.

So to change to 2 geometries I need to do:
1. I create VertexBuffer and IndexBuffer, fill them with data of first Geometry
2. Append data of second Geometry to both IndexBuffer and VertexBuffer as if it was new (indexes start counting from 0)
2. Create Geometry1 and Geometry2.
3. Set IndexBuffer and VertexBuffer to Geometry1 and Geometry2.
4. SetRange for both Geometry1 and Geometry2 indicating starting vertex, number of vertices, starting index and number of indexes.
5. Create Model, SetGeometry for both (setting numGeometries to 2 beforehand).

Is it correct? Anything requiring special attention?

Thanks a lot!

-------------------------

cadaver | 2017-01-02 01:14:15 UTC | #5

Looks correct otherwise, but make sure the index data references the second geometry correctly. E.g. if the first geometry used vertices 0-99, and second geometry uses vertices from 100 onward, make sure that is reflected in your second geometry's index data.

-------------------------

slapin | 2017-01-02 01:14:15 UTC | #6

Thanks a lot.
Is there any code examples on how to set up proper index values for 2 geometries?

Thanks for your help.

-------------------------

cadaver | 2017-01-02 01:14:15 UTC | #7

OgreImporter & AssetImporter (in Source/Tools) both contain looping through the source data's geometries / submeshes, and copying the index data over while minding the base vertex index of the geometry.

-------------------------

