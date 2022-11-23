fcroce | 2017-01-02 01:12:24 UTC | #1

Hello everyone,

I'm trying to create a simple cube with a texture2D from HTML5:

The idea is to bind a texture from JS (a video texture in particular) and read it from unit 0 in my technique ( uniform sampler2D sVideo0; )

URHO3D code:
[code]
        boxNode_=scene_->CreateChild("Box");
        boxNode_->SetPosition(Vector3(0,2,15));
        boxNode_->SetScale(Vector3(3,3,3));
        StaticModel* boxObject=boxNode_->CreateComponent<StaticModel>();
        boxObject->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
        
        Urho3D::SharedPtr<Urho3D::Material> material(new Urho3D::Material(context_));
        cubetexture_ = SharedPtr<Texture2D>( new Texture2D(context_));
        cubetexture_->SetSize(128, 128, Graphics::GetRGBAFormat(), TEXTURE_DYNAMIC);
        material->SetTexture(TextureUnit(), cubetexture_);

        material->SetTechnique(0, cache->GetResource<Technique>("Techniques/VideoWebGL.xml"));
        boxObject->SetMaterial(material);
[/code]

How can I pass "cubetexture_" to javascript, or viceversa create it with gl.createTexture(); and use that one on URHO3D instead?

I'm quite lost on how can the 2 system communicate through emscripten except EM_ASM() to call JS from C++

-------------------------

fcroce | 2017-01-02 01:12:27 UTC | #2

After a few tests I found out that if I create the texture in javascript and store it with a bindTexture, I can force it as active and use on rendering.

Problem is that I'd need a "pre render update" event for the cube, so I can activate the texture until it finishes the rendering procedure and follow up with the rest of the code (other objects will activate and render their own textures via the usual material and technique).

"HandleRenderUpdate" is too generic for that or eventually I should filter the cube only... no idea.

Any suggestion is appreciated, thanks.

-------------------------

