restless | 2020-04-08 12:29:24 UTC | #1

In my project I generate geometry programmatically, and I simply fill the VertexBuffer and IndexBuffer, then supply them to the Model and it works.

I read this https://urho3d.github.io/documentation/1.7.1/_vertex_buffers.html and sometime ago I seen code from somewhere on how to create Model manually... It ended up something like this in my code (unnecessary details are omitted):

    SharedPtr<Model> model (new Model(pContext));

    model->SetNumGeometries(2);
    Vector<SharedPtr<IndexBuffer>> model_index_buffers;
    Vector<SharedPtr<VertexBuffer>> model_vertex_buffers;

    //// first pair of buffers goes to geom1

    SharedPtr<Geometry> geom1(new Geometry(pContext));
    SharedPtr<VertexBuffer> vb1(new VertexBuffer(pContext, false));
    SharedPtr<IndexBuffer> ib1(new IndexBuffer(pContext, false));

    // pass your generated data
    vb1->SetShadowed(true);
    vb1->SetSize(...); 
    vb1->SetData(...);

    ib1->SetShadowed(true);
    ib1->SetSize(...);
    ib1->SetData(...);

    geom1->SetVertexBuffer(0, vb1);
    geom1->SetIndexBuffer(ib1);
    geom1->SetDrawRange(Urho3D::TRIANGLE_LIST, 0, ...);

    model->SetGeometry(/*0th Geometry*/0, /*0th LOD*/0, geom1);
    model_vertex_buffers.Push(vb1);
    model_index_buffers.Push(ib1);

    //  I don't know why, but afaik this part is required?
    Vector<unsigned> morphRangeStarts;
    Vector<unsigned> morphRangeCounts;
    morphRangeStarts.push_back(0);
    morphRangeCounts.push_back(0);

    //// repeat everything with second geometry ...

    // Questionable part: this two calls are not necessery to render the model,
    // but are required for Model::SaveFile to work
    model->SetIndexBuffers(model_index_buffers);
    model->SetVertexBuffers(model_vertexRangeStarts, morphRangeCounts);

It's pretty dense and elaborate, but the essense is that we set up multiple Geometry classes each containing vertex/index buffers pair, and then pass them into Model **then again** we pass all of the vertex/index buffers to the Model.

Structure roughly looks like this:

    Model {
        Vector<IndexBuffer>;
        Vector<VertexBuffer>;

        Geometry1 {
            IndexBuffer;
            VertexBuffer;
        }

        Geometry2 {
            IndexBuffer;
            VertexBuffer;
        }
    }

So, is it only me not totally understanding the logic here, or do we have an inconsistency in the engine? What I see as illogical is having 2 ways to contain the Vertex/Index buffers (through Model and through containing Geometries).

The thing is, I can get away with passing vertex/index buffers through Geometries only, but then Model::SaveFile saves  nothing.

Thanks for reading it to the end :) Will be thankful for any leads on this.

-------------------------

SirNate0 | 2020-04-08 15:03:49 UTC | #2

Tentatively I think the vertexBuffers_ and indexBuffers_ are never actually used - based off a quick search none of the code actually calls `Model::GetIndexBuffers`, for example.

Others more familiar with engine may be able to answer better, though.

-------------------------

1vanK | 2020-04-08 16:55:12 UTC | #3

```
Model { Vector<IndexBuffer>; Vector<VertexBuffer>;
```

If I remember it right, logically this is storage for all buffers because different geometries can use same buffers, so we avoid duplication when saving to file

-------------------------

weitjong | 2020-04-08 17:07:36 UTC | #4

See https://urho3d.github.io/documentation/HEAD/_file_formats.html. Is this what you are looking for?

-------------------------

restless | 2020-04-08 17:29:42 UTC | #5

The file format description and the Model::SaveFile kinda confirms that the primary place to store buffers is Model. So then, when we refer to them in Geometry, we could use indexes, just as we do in .mdl file format.

So I take it as if Geometry::Set*Buffer() taking pointer to buffer is a convenience/shortcut? I think it would help a lot if we put some note into Geometry API that each supplied Buffer pointer should also be stored in Model directly... I donno, I am still confused a bit :D

-------------------------

SirNate0 | 2020-04-08 20:06:43 UTC | #6

Okay, so it seems to me that Model stores the "complete" list of Vertex/Index Buffers, at least in terms of saving and loading. Each Geometry also stores a list of Vertex/Index buffers, to be used at a given LOD and with a given material (I believe the different Geometries within a given Model each get their own material in StaticModel). When saving, rather than having duplicate buffers, the index in the "complete" list is used, but in general within the engine only the specific entries for a given Geometry are used at one time, and by having multiple pointers to it rather than an index into the global list performance is likely increased a bit.

It seems to me that we should either do as you suggest, add some comments in the Geomtry API that each buffer should also be added to the Model, or add an additional parameter to `bool SetGeometry(unsigned index, unsigned lodLevel, Geometry* geometry);` along the lines of `bool addNewBuffers = false` that will add the Vertex/Index Buffers to the Model from their pointers in the Geometry if they are not already present in the Model's vector's. Personally, I would prefer the default to be true for this, but false would preserve the existing behavior.

Personally, I'm not certain why it's not possible to just add a VertexBuffer to the model without setting a new vector for all of them. Perhaps more importantly, I think a warning message should be added to `LookupVertexBuffer` and `LookupIndexBuffer` to warn that the appropriate buffer was not found when saving, otherwise it appears that all should be well. (I suspect that some code I have from earlier actually behaves improperly in this regard, though I only now have any idea why)

-------------------------

