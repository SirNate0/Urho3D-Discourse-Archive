SteveU3D | 2019-05-23 13:20:02 UTC | #1

Hi,
I wrote a function to create a 3D arrow made of one cylinder an two cones : 

    void create3DArrow(Node** inArrowNode, float inSize)
    {
      ResourceCache* cache = GetSubsystem<ResourceCache>();

      //create a 3D arrow with one cylinder and two cones
      SharedPtr<Node> mArrowCylinderNode;
      SharedPtr<StaticModel> mArrowCylinderObject;
      SharedPtr<Node> mArrowCone1Node;
      SharedPtr<StaticModel> mArrowCone1Object;
      SharedPtr<Node> mArrowCone2Node;
      SharedPtr<StaticModel> mArrowCone2Object;

      float coneSize = 1.5;
      float coneThickness = 1.0;
      float coneZ = inSize/2.0 - coneSize/2.0;
      float cylinderSize = inSize - 2*coneSize;
      float cylinderThickness = 0.5;

      mArrowCylinderNode = scene_->CreateChild("ArrowCylinder");
      mArrowCylinderObject = mArrowCylinderNode->CreateComponent<StaticModel>();
      mArrowCylinderObject->SetModel(cache->GetResource<Model>("Models/Cylinder.mdl"));
      mArrowCylinderNode->SetScale(Vector3(cylinderThickness, cylinderSize, cylinderThickness));
      mArrowCylinderNode->SetPosition(Vector3(0, 0, 0));

      mArrowCone1Node = scene_->CreateChild("ArrowCone1");
      mArrowCone1Object = mArrowCone1Node->CreateComponent<StaticModel>();
      mArrowCone1Object->SetModel(cache->GetResource<Model>("Models/Cone.mdl"));
      mArrowCone1Node->SetScale(Vector3(coneThickness, coneSize, coneThickness));
      mArrowCone1Node->SetPosition(Vector3(0, coneZ, 0));

      mArrowCone2Node = scene_->CreateChild("ArrowCone2");
      mArrowCone2Object = mArrowCone2Node->CreateComponent<StaticModel>();
      mArrowCone2Object->SetModel(cache->GetResource<Model>("Models/Cone.mdl"));
      mArrowCone2Node->SetScale(Vector3(coneThickness, coneSize, coneThickness));
      mArrowCone2Node->SetRotation(Quaternion(180, 0, 0));
      mArrowCone2Node->SetPosition(Vector3(0, -coneZ, 0));

      *inArrowNode = scene_->CreateChild("Arrow");
      (*inArrowNode)->AddChild(mArrowCylinderNode, 0);
      (*inArrowNode)->AddChild(mArrowCone1Node, 1);
      (*inArrowNode)->AddChild(mArrowCone2Node, 2);

    }

So I do : 
    
    Node* myArrow;
    float arrowSize = 10;
    create3DArrow(&myArrow, arrowSize );

And then I can do : 

    myArrow->SetPosition(...); //the center is the center of the cylinder
    myArrow->SetRotation(...);

which gives me for example : 

![3DArrow|182x500](upload://c20EIVhsu6KJFCoMmU4Wgw4XgmR.jpg)

My question is how to modify the size of the cylinder in the arrow to make it longer or smaller once it is created. I don't want to have class members for the cylinder and the cones as I create several arrows. So how to access the cylinder and the cones in the parent node myArrow to change their scale and position / rotation?
Thanks.

-------------------------

TheComet | 2017-08-08 07:35:48 UTC | #2

What you could do is create a new component. Something like this? (untested)

    class Arrow3D : public Urho3D::Component
    {
        URHO3D_OBJECT(Arrow3D, Urho3D::Component);
    public:
        Arrow3D(Urho3D::Context* context);
        static void RegisterObject(Urho3D::Context* context);

        void SetSize(float size);

    protected:
        virtual void OnNodeSet(Urho3D::Node* node) override;
        
    private:
        void CreateObjects();
        void DestroyObjects();
        
    private:
        float size_;
        Urho3D::SharedPtr<Urho3D::Node> mArrowCylinderNode;
        Urho3D::SharedPtr<Urho3D::Node> mArrowCone1Node;
        Urho3D::SharedPtr<Urho3D::Node> mArrowCone2Node;
    };

    Arrow3D::Arrow3D(Urho3D::Context* context) :
        Component(context),
        size_ = (1.0f) // Default size of arrow
    {
    }

    void Arrow3D::RegisterObject(Urho3D::Context* context)
    {
        context->RegisterFactory<Arrow3D>("Custom Objects");
    }

    void Arrow3D::SetSize(float size)
    {
        size_ = size;
        if (node_ == NULL)
            return;
        
        float coneSize = 1.5;
        float coneThickness = 1.0;
        float coneZ = size_/2.0 - coneSize/2.0;
        float cylinderSize = size_ - 2*coneSize;
        float cylinderThickness = 0.5;
        
        mArrowCylinderNode->SetScale(Vector3(cylinderThickness, cylinderSize, cylinderThickness));
        
        mArrowCone1Node->SetScale(Vector3(coneThickness, coneSize, coneThickness));
        mArrowCone1Node->SetPosition(Vector3(0, coneZ, 0));
        
        mArrowCone2Node->SetScale(Vector3(coneThickness, coneSize, coneThickness));
        mArrowCone2Node->SetRotation(Quaternion(180, 0, 0));
        mArrowCone2Node->SetPosition(Vector3(0, -coneZ, 0));
    }

    void Arrow3D::OnNodeSet(Urho3D::Node* node)
    {
        if (node == NULL)
            DestroyObjects();
        else
            CreateObjects();
    }

    void Arrow3D::CreateObjects()
    {
        Urho3D::ResourceCache* cache = GetSubsystem<ResourceCache>();
        Urho3D::Model* model;

        mArrowCylinderNode = node_->CreateChild("ArrowCylinder");
        model = mArrowCylinderNode->CreateComponent<StaticModel>();
        model->SetModel(cache->GetResource<Model>("Models/Cylinder.mdl"));
        
        mArrowCone1Node = scene_->CreateChild("ArrowCone1");
        model = mArrowCone1Node->CreateComponent<StaticModel>();
        model->SetModel(cache->GetResource<Model>("Models/Cone.mdl"));
      
        mArrowCone2Node = scene_->CreateChild("ArrowCone2");
        model = mArrowCone2Node->CreateComponent<StaticModel>();
        model->SetModel(cache->GetResource<Model>("Models/Cone.mdl"));
        
        SetSize(size_);
    }

    void Arrow3D::DestroyObjects()
    {
        if (mArrowCylinderNode == NULL)
            return;
            
        mArrowCylinderNode->Remove();
        mArrowCone1Node->Remove();
        mArrowCone2Node->Remove();
        
        mArrowCylinderNode = NULL;
        mArrowCone1Node = NULL;
        mArrowCone2Node = NULL;
    }

Then, during engine Start(), you register it:

    void Application::Start()
    {
        Arrow3D::RegisterObject(context_);
    }

And finally, you can just create the arrow like so:

    Node* arrowNode = scene_->CreateChild("Arrow");
    Arrow3D* arrow = arrowNode->CreateComponent<Arrow3D>();
    arrow->SetSize(5);

-------------------------

1vanK | 2017-08-07 15:02:34 UTC | #3

I'm not sure I fully understood the question. May be `arrow->GetChild() ` will help you

-------------------------

slapin | 2017-08-07 15:40:13 UTC | #4

You can always GetChild("name") and then SetScale() the child.

-------------------------

SteveU3D | 2017-08-08 07:35:42 UTC | #5

Thanks! I do C++ and I didn't think of OOP and creating a special object for my arrow, shame on me :expressionless:
The GetChild("name") is good too but I think that the Arrow class will be better for what I need to do.

-------------------------

