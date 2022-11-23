GoogleBot42 | 2017-01-02 01:04:10 UTC | #1

I have a quick question.  I have the following code:

[code]    Node* cubeNode = scene_->CreateChild("Cube");
    cubeNode->SetPosition(Vector3(0,0,0));
    StaticModel* boxModelComp = cubeNode->CreateComponent<StaticModel>();
    boxModelComp->SetModel( cache->GetResource<Model>("Models/Box.mdl") );

    Material* mat = new Material(context_);
    mat->SetNumTechniques(1);
    mat->SetTechnique(0, cache->GetResource<Technique>("Techniques/Diff.xml") );
    mat->SetTexture(TU_DIFFUSE, cache->GetResource<Texture2D>("Textures/UrhoIcon.png"));
    boxModelComp->SetMaterial(0, mat);[/code]

Do I need to delete the old default material of the staticmodel component?  Am I leaking memory?

-------------------------

cadaver | 2017-01-02 01:04:10 UTC | #2

No, you're not leaking memory.

All components that are using some resource (model, material..) hold it inside a shared pointer to guarantee it stays alive. So in this case, when you construct a new material and don't add it to the resource cache but only assign it to the StaticModel component, the only shared pointer reference is within the that component, and the material will be destroyed the same time that component is destroyed. And btw. by default all drawables start with a null material (which means the View will fetch a default material when rendering.)

You *would* leak memory if the StaticModel would for some reason fail to assign the material, for example if you specified an out-of-range material index. For that kind of situations you could create the material inside a SharedPtr to begin with:

[code]
SharedPtr<Material> mat(new Material(context_));
[/code]

-------------------------

GoogleBot42 | 2017-01-02 01:04:11 UTC | #3

That makes sense!  Very good design!

[quote="cadaver"]You *would* leak memory if the StaticModel would for some reason fail to assign the material[/quote]

 :slight_smile:   Thanks for that!  I would have missed that!

-------------------------

