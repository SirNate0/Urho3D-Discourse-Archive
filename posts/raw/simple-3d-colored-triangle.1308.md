skaiware | 2017-01-02 01:06:43 UTC | #1

Dear guys
I m trying to display a simple 3d triangle using simple vertex color using:

[code]
        Node* node = m_scene->CreateChild("SimpleTriangle");
        Model* model = new Model(context_);
        StaticModel* staticModel = node->CreateComponent<StaticModel>();
        model->SetNumGeometries( 1 );
        //Urho3D::BoundingBox bb;
        Urho3D::SharedPtr<Urho3D::Geometry> newGeometry(new Urho3D::Geometry(context_));
        Urho3D::Vector<float> vertexData;
        Urho3D::Vector<unsigned short> indexData;
        vertexData.Push(0); vertexData.Push(0); vertexData.Push(0);  vertexData.Push(Color::RED.ToUInt());
        vertexData.Push(0); vertexData.Push(100); vertexData.Push(0); vertexData.Push(Color::RED.ToUInt());
        vertexData.Push(100); vertexData.Push(0); vertexData.Push(0); vertexData.Push(Color::RED.ToUInt());
        indexData.Push(0); indexData.Push(1); indexData.Push(2);
        Urho3D::SharedPtr<Urho3D::VertexBuffer> vertexBuffer(new Urho3D::VertexBuffer(context_));
        vertexBuffer->SetShadowed(true);
        vertexBuffer->SetSize( 3, Urho3D::MASK_POSITION|Urho3D::MASK_COLOR);
        vertexBuffer->SetData(&vertexData[0]);
        // create index buffer
        Urho3D::SharedPtr<Urho3D::IndexBuffer> indexBuffer(new Urho3D::IndexBuffer(context_));
        indexBuffer->SetShadowed(true);
        indexBuffer->SetSize(indexData.Size(), false );
        indexBuffer->SetData(&indexData[0]);
        // add buffers to geometry
        newGeometry->SetVertexBuffer(0, vertexBuffer); // , vertexDecl
        newGeometry->SetIndexBuffer(indexBuffer);
        newGeometry->SetDrawRange(Urho3D::TRIANGLE_LIST, 0, indexData.Size());

        model->SetGeometry(0, 0, newGeometry);
        model->SetNumGeometryLodLevels(0,1);

        staticModel->SetModel(model);
[/code]
but the triangle is all dark/black/brown.

I have tried:
- to add vertex normals
- to manually create a material and to set it : material->SetTechnique(0, cache->GetResource<Technique>("Techniques/NoTextureNormal.xml") );
- to add a global scene light

Would anyone know how to simply display a colorful triangle using vertex colors in the vertex buffer ?
Cheers
Thanks
S.

-------------------------

thebluefish | 2017-01-02 01:06:43 UTC | #2

Do you have a light? I know you have a "global scene light", but is it actually illuminating your tri?

-------------------------

skaiware | 2017-01-02 01:06:43 UTC | #3

[quote="thebluefish"]Do you have a light? I know you have a "global scene light", but is it actually illuminating your tri?[/quote]

Thanks. 
Yes there are even 2 lights:
[code]
        // Create a directional light without shadows
        Node* lightNode = m_scene->CreateChild("DirectionalLight");
        lightNode->SetDirection(Vector3(0.5f, -1.0f, 0.5f));
        lightNode->SetPosition(Vector3(0,100,0));
        Light* light = lightNode->CreateComponent<Light>();
        light->SetLightType(LIGHT_DIRECTIONAL);
        light->SetColor(Color(1.f, 1.f, 1.f));
        light->SetSpecularIntensity(100.0f);

        // add a light to the camera node as well
        {
            Light* light = m_camera_node->CreateComponent<Light>();
            light->SetLightType(LIGHT_POINT);
            light->SetRange(200);
            light->SetBrightness(200.0);
            light->SetColor(Color(1,1,1,1.0));
        }
[/code]
but no impact, triangle still black/dark.
S.

-------------------------

skaiware | 2017-01-02 01:06:43 UTC | #4

[quote="Sinoid"]You need to use a technique that includes "VERTEXCOLOR" as a preprocessor definition.

Thanks.
Here it is I have tried different techniques such way:
[code]
        Urho3D::SharedPtr<Urho3D::Material> material(new Urho3D::Material(context_));
        material->SetTechnique(0, cache->GetResource<Technique>("Techniques/DiffVCol.xml") ); // tried most DiffVCol .......
        staticModel->SetMaterial(material);
[/code]
but no way, triangle still black.
WTH....

-------------------------

thebluefish | 2017-01-02 01:06:43 UTC | #5

Try NoTextureUnlitVCol.xml

-------------------------

skaiware | 2017-01-02 01:06:43 UTC | #6

[quote="thebluefish"]Try NoTextureUnlitVCol.xml[/quote]

[img]http://s23.postimg.org/igksg780r/triangle.png[/img]

Tried but no way... 
Thanks anyway.
S.

-------------------------

thebluefish | 2017-01-02 01:06:43 UTC | #7

So wait, are you defining your own material or using an existing material? What happens if you turn off shadows? What happens if you reverse the winding order?

[code]
indexData.Push(0); indexData.Push(2); indexData.Push(1);
[/code]

-------------------------

JTippetts | 2017-01-02 01:06:44 UTC | #8

I think part of the problem is that you are pushing the color (Color::RED.ToUInt()) into a float Vector. This involves an implicit cast from unsigned int to float, which changes the bit representation of the value. Later, when this float value is re-interpreted as 4 separate unsigned char, the values are not the same.

Color::RED as an unsigned int (4 bytes combined from r,g,b,a) has the value of 4278190335 which, if re-interpreted as byte-sized color components, gives you r=255, g=0, b=0, a=255. However, casting to a float then interpreting that float as unsigned int gives you an unsigned value of 1333723137 which unpacks to r=79 g=127 b=0 a=1.

The usual method for building a vertex stream like this is to pack it into an unsigned char buffer rather than a float buffer. See the dynamic geometry sample ( [github.com/urho3d/Urho3D/blob/m ... y.cpp#L111](https://github.com/urho3d/Urho3D/blob/master/Source/Samples/34_DynamicGeometry/DynamicGeometry.cpp#L111) ) for what this can look like. (In the sample, you are locking an existing vertex stream as an unsigned buffer, but the process of creating a stream is similar.)

I haven't tried your code to see if this is the actual issue or not, but perhaps it will help.

-------------------------

skaiware | 2017-01-02 01:06:44 UTC | #9

[quote="thebluefish"]So wait, are you defining your own material or using an existing material? What happens if you turn off shadows? What happens if you reverse the winding order?
[/quote]

Hi 
- I m creating a new Material on purpose:         
  Urho3D::SharedPtr<Urho3D::Material> material(new Urho3D::Material(context_));
  and then setting the technique material->SetTechnique(0, cache->GetResource<Technique>("Techniques/XXXXXXXXX.xml") ); 
- I have tried staticModel->SetCastShadows(false);  but no effect
- I have tried reverse winding : the triangle is ofcourse now visible from the back but still all black
Let me try JTippetts advice.
Thanks.
S.

-------------------------

skaiware | 2017-01-02 01:06:44 UTC | #10

Here it is I have tried to play with a unsigned int vertex buffer but nothing does appear at all probably because the model expects 4bytes per vertex position and 1 byte for the color. I could not load box.mdl because the mesh I am generating does contain variable number fo vertexes.
Now JTippet is probably right, the direct cast from uint to float is dirty, modifying the value of the color. 
Here is  what I have tried to avoid any corruption to the UINT color:

[code]
        Node* node = m_scene->CreateChild("SimpleTriangle");
        Model* model = new Model(context_);
        StaticModel* staticModel = node->CreateComponent<StaticModel>();
        model->SetNumGeometries( 1 );
        Urho3D::BoundingBox bb;
        Urho3D::SharedPtr<Urho3D::Geometry> newGeometry(new Urho3D::Geometry(context_));
        Urho3D::Vector<float> vertexData;
        std::cout << "sizeof(unsigned char)" << sizeof(unsigned char) <<  std::endl; // usually 1 byte
        std::cout << "sizeof(float)" << sizeof(float) <<  std::endl; // usually 4 bytes
        Urho3D::Vector<unsigned short> indexData;
        unsigned int r = Color::RED.ToUInt();
        float colorFloat = 0;
        memcpy(&colorFloat, &r, sizeof(float));

        #define ADD_VERTEX(V, C) bb.Merge(V); vertexData.Push(V.x_); vertexData.Push(V.y_); vertexData.Push(V.z_); vertexData.Push(0); vertexData.Push(100); vertexData.Push(0); vertexData.Push(C);

        Urho3D::Vector3 v1(0,0,0); ADD_VERTEX(v1, colorFloat);
        Urho3D::Vector3 v2(100,0,0); ADD_VERTEX(v2, colorFloat);
        Urho3D::Vector3 v3(0,0,100); ADD_VERTEX(v3, colorFloat);
        indexData.Push(0); indexData.Push(2); indexData.Push(1);

        Urho3D::SharedPtr<Urho3D::VertexBuffer> vertexBuffer(new Urho3D::VertexBuffer(context_));
        vertexBuffer->SetShadowed(true);
        vertexBuffer->SetSize( 3, Urho3D::MASK_POSITION|Urho3D::MASK_NORMAL|Urho3D::MASK_COLOR);
        vertexBuffer->SetData(&vertexData[0]);
        // create index buffer
        Urho3D::SharedPtr<Urho3D::IndexBuffer> indexBuffer(new Urho3D::IndexBuffer(context_));
        indexBuffer->SetShadowed(true);
        indexBuffer->SetSize(indexData.Size(), false);
        indexBuffer->SetData(&indexData[0]);
        // add buffers to geometry
        newGeometry->SetVertexBuffer(0, vertexBuffer); // chek me: add vertexDecl ?
        newGeometry->SetIndexBuffer(indexBuffer);
        // TRIANGLE_LIST = 0, LINE_LIST, POINT_LIST, TRIANGLE_STRIP, LINE_STRIP, TRIANGLE_FAN
        newGeometry->SetDrawRange(Urho3D::TRIANGLE_LIST, 0, indexData.Size());

        model->SetGeometry(0, 0, newGeometry);
        model->SetNumGeometryLodLevels(0,1);
        model->SetBoundingBox(bb);

        ResourceCache* cache = GetSubsystem<ResourceCache>();

        Urho3D::SharedPtr<Urho3D::Material> material(new Urho3D::Material(context_));
        material->SetTechnique(0, cache->GetResource<Technique>("Techniques/NoTextureVCol.xml") );
        staticModel->SetMaterial(material);
        staticModel->SetCastShadows(false);

        staticModel->SetModel(model);
[/code]  
but the triangle is still not red: playing with the normal, it is either black when null normal or grey with upward normal.
Damned...
Thanks
S.

-------------------------

