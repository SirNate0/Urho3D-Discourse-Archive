johnnycable | 2017-06-02 17:21:17 UTC | #1

Hello there, I need some help. I'm trying to draw a simple line with CustomGeometry class using 24_Urho2DSprite example, but I'm failing at it. I removed all other drawing code (that about sprites) and left a black screen. Then I'm adding the following code:

    // custom geometry
    
    auto scp = camera->ScreenToWorldPoint(Vector3(0.5f,0.5f,-1));
    
    Node* lineNode = scene_->CreateChild("lineNode");
    CustomGeometry* cg = lineNode->CreateComponent<CustomGeometry>();
    cg->Clear();
    cg->SetNumGeometries(1);
    cg->BeginGeometry(0, PrimitiveType::LINE_LIST);
    //    cg->DefineGeometry(0, PrimitiveType::POINT_LIST, 3, false,false, false, false);
    cg->DefineVertex(Vector3(0,0,0));
    cg->DefineVertex(Vector3(10,10,0));
    cg->DefineColor(Color::WHITE);
    //cg->SetMaterial(<#Urho3D::Material *material#>); ??? is there a default material?
    cg->Commit();
    
    lineNode->SetPosition(scp);

What am I missing?

-------------------------

Modanung | 2017-06-03 14:21:06 UTC | #2

Maybe try a material with `fill` set to `wireframe`?

-------------------------

johnnycable | 2017-06-03 14:21:07 UTC | #3

Added

    Material* mat = new Material(context_);
    cg->SetMaterial(mat);

and this gave out:

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/2b1f5d5cd6a108eb9e93d18ecc8aa8f4d72c5a17.png" width="690" height="487">

the subtle white thin line. Every material fill gave the same.
Thank you. Looks like custom geometry is an easy input for this kind of things.
Now I have to find a suitable tessellator, and some geometry generator.

-------------------------

