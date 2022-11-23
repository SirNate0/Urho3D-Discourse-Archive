GoogleBot42 | 2017-01-18 01:48:35 UTC | #1

I used the pretty much used the theoretically working code from here exactly: http://discourse.urho3d.io/t/solved-how-to-create-mesh/35  This post is a bit old so maybe things have changed a bit?

It simply doesn't render correctly depending on the direction and position of the camera.  It seems to fail whenever the camera is close or when the object almost falls off of the camera.

Here is it messing up

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/d3000653d838b1799ab08d5105cc1490f3e5f120.png" width="642" height="500">

But when I back up a bit it works

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/94f6e90c9177bf40dc7f4ce9d366463259301ad2.png" width="642" height="500">

[code]
    float dirLightVertexData[] =
    {
        -1, 1, 0,
        1, 1, 0,
        1, -1, 0,
        -1, -1, 0,
    };

    unsigned short dirLightIndexData[] =
    {
        0, 1, 2,
        2, 3, 0,
    };

    SharedPtr<VertexBuffer> dlvb(new VertexBuffer(context_));
    dlvb->SetShadowed(true);
    dlvb->SetSize(4, MASK_POSITION);
    dlvb->SetData(dirLightVertexData);

    SharedPtr<IndexBuffer> dlib(new IndexBuffer(context_));
    dlib->SetShadowed(true);
    dlib->SetSize(6, false);
    dlib->SetData(dirLightIndexData);

    Geometry *dirLightGeometry_ = new Geometry(context_);
    dirLightGeometry_->SetVertexBuffer(0, dlvb);
    dirLightGeometry_->SetIndexBuffer(dlib);
    dirLightGeometry_->SetDrawRange(TRIANGLE_LIST, 0, dlib->GetIndexCount());

    SharedPtr<Model> testModel(new Model(context_));
    Vector<SharedPtr<VertexBuffer> > dlvbVector;
    Vector<SharedPtr<IndexBuffer> > dlibVector;
    dlvbVector.Push(dlvb);
    dlibVector.Push(dlib);
    testModel->SetNumGeometries(1);
    testModel->SetNumGeometryLodLevels(0, 1);
    testModel->SetGeometry(0, 0, dirLightGeometry_);

    // Define the model buffers and bounding box
    PODVector<unsigned> emptyMorphRange;
    testModel->SetVertexBuffers(dlvbVector, emptyMorphRange, emptyMorphRange);
    testModel->SetIndexBuffers(dlibVector);
    testModel->SetBoundingBox(BoundingBox(Vector3(-1.0f, -1.0f, 0.0f), Vector3(1.0f, 1.0f, 0.0f)));

    Node* testnodea = scene_->CreateChild("testasdasd");
    testnodea->SetScale(Vector3(1.0f, 1.0f, 1.0f));
    StaticModel* testObjecta = testnodea->CreateComponent<StaticModel>();
    testObjecta->SetModel(testModel);
    testObjecta->SetMaterial(cache->GetResource<Material>("Materials/BlueUnlit.xml"));
    testnodea->SetPosition(Vector3(-1.0f, 5.0f, 2.0f));
[/code]

Any help is nice!  Thanks!

-------------------------

1vanK | 2017-01-10 01:27:38 UTC | #2

"Materials/BlueUnlit.xml" uses VColor?

-------------------------

GoogleBot42 | 2017-01-10 02:12:31 UTC | #3

Turns out that material doesn't exist.  Whoops.  I should have checked before I copied the code.  But it is not the problem.  :unamused:

You can see this bellow.  Now both of the quads you can see are both the same material.  The other quad is using "Models/Plane.mdl" included in the standard urho3d assets.  The two should be identical just scaled differently.

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/a5c25964bfa4596715b4621ed5ce437d6473109f.png" width="642" height="500">

-------------------------

cadaver | 2017-01-10 08:45:40 UTC | #4

If you want the model to be lit and texture mapped, it needs normals and UVs.

-------------------------

GoogleBot42 | 2017-01-11 01:28:15 UTC | #5

Thanks!  I was just being dumb. That should have been obvious to me. :joy:  So that problem I was having has been solved.

[b]EDIT: Never mind I figured it out.  See here: [url]https://urho3d.github.io/documentation/1.6/class_urho3_d_1_1_index_buffer.html#acad3ececff56c39f52703e514b730364[/url][/b]

Alright, now I am running into an issue in that I need more greater than a unsigned short for my indices.  Granted I am not being entirely efficient but I want to do some testing to see how much I can render in one draw call.

[b]Is there a way I can set 32bit indices?[/b]

Here I am trying to make a 14x14x14 big cube of cubes.  As you can see, it falls a bit short because I go over the index of 65,535.

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/1ea82bf2bebb26fd52b437b1bc98fe7d3977b141.png" width="642" height="500">

-------------------------

1vanK | 2017-01-11 08:26:04 UTC | #6

[quote="GoogleBot42, post:5, topic:2688"]
Is there a way I can set 32bit indices?
[/quote]

SetSize (unsigned indexCount, **bool largeIndices**, bool dynamic=false)

-------------------------

GoogleBot42 | 2017-01-12 06:09:12 UTC | #7

Yeah I figured it out.  Thanks though :)

-------------------------

GoogleBot42 | 2017-01-12 06:13:29 UTC | #8

Here is a working screenshot if anyone is a bit curious.  Much bigger.

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/5a81660635e88893563c6df90d0785438c8c4bd0.png" width="642" height="500">

Also I got the basics of polyvox running (soon to be textured too :wink:).  

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/7541684600f4d59386b5338222ba6ba6e024e276.png" width="642" height="500">

-------------------------

bloop | 2018-11-30 10:42:07 UTC | #9

That is looking great! I am starting to look at PolyVox and Urho as well. Did you implement a bespoke shaders?

-------------------------

