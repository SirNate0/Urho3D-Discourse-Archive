scorvi | 2017-01-02 00:57:32 UTC | #1

hi all,

i am new to urho3d and have some problems generating a simple cube mesh in c++ code.

how do i create a simple cube mesh without loading a model from file ?  and how do i create a simple material for this mesh?

i have also a problem debuging the samples in visual studio. it can not find the debuging information dont know why ? 

thx,
greetings from germany :slight_smile:

-------------------------

cadaver | 2017-01-02 00:57:32 UTC | #2

If you don't require it to be a proper Model resource that you assign to eg. StaticModel component, the easiest way is to use the CustomGeometry component, which allows you to specify vertices, normals, UVs etc. one by one. It's very much inspired by Ogre's ManualObject. The downsides are that it's an unique instance, so you can't render many of them without defining the vertices for each, and the geometry is always unindexed.

To create a proper Model programmatically, create the vertex & index buffers with data, create a Geometry object which references the buffers and sets a draw range, then create a Model object and assign the geometry to it. Studying the AssetImporter tool's code may be of use, as it does exactly that to save a model. For inspiration in how to define the vertex & index data & geometries you can also look at Renderer::CreateGeometries() function which creates the deferred rendering lighting volumes purely in code.

To create a Material, just create one and assign a suitable Technique resource (for example CoreData/Techniques/Diff.xml) to it by calling Material::SetTechnique(). The material should have quite sane defaults (white diffuse color, clockwise vertices are rendered, no textures initially.)

If on the other hand you also want to create the Technique from scratch, that's more complicated, as you need to create the shader passes (base, lighting etc.) and assign shaders to each. In that case I recommend taking a look at how Technique loads itself.

-------------------------

scorvi | 2017-01-02 00:57:32 UTC | #3

thx

so i am using this code to create a test model, but can not see anything .... dont know why....

[gist]https://gist.github.com/VladimirPobedinskiy/8557669[/gist]

-------------------------

cadaver | 2017-01-02 00:57:32 UTC | #4

There was not much missing. The number of geometries needs to be set, the LOD geometry indices start from 0 for SetGeometry(), and a bounding box that matches the vertex data.

[quote]
    SharedPtr<Model> testModel(new Model(context_));
    Vector<SharedPtr<VertexBuffer> > dlvbVector;
    Vector<SharedPtr<IndexBuffer> > dlibVector;
    dlvbVector.Push(dlvb);
    dlibVector.Push(dlib);
    testModel->SetNumGeometries(1); // Added 
    testModel->SetNumGeometryLodLevels(0, 1);
    testModel->SetGeometry(0, 0, dirLightGeometry_); // Fixed

    // Define the model buffers and bounding box
    PODVector<unsigned> emptyMorphRange;
    testModel->SetVertexBuffers(dlvbVector, emptyMorphRange, emptyMorphRange);
    testModel->SetIndexBuffers(dlibVector);
    testModel->SetBoundingBox(BoundingBox(Vector3(-1.0f, -1.0f, 0.0f), Vector3(1.0f, 1.0f, 0.0f))); // Added
[/quote]

-------------------------

