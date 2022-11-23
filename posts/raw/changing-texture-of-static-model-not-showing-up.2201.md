bbm | 2017-01-02 01:13:53 UTC | #1

I have a opencv mat and a StaticModel loaded from a file which I converted a collada to mdl. StaticModel loads good with it's original texture. but I want to change it dynamically.

[code]
        assert(!cvWraper.mat.empty());
        // I get the model
        StaticModel *staticModel = mNode->GetComponent<StaticModel>();
        assert(staticModel != nullptr);
        // then I get the texture from it's material
        Texture *textureBase = staticModel->GetMaterial(0)->GetTexture(TU_DIFFUSE);
        assert(textureBase != nullptr);
        Texture2D *texture = dynamic_cast<Texture2D*>(textureBase);
        assert(texture != nullptr);
        bool success = true;
        // And I update the texture
        if(texture->GetWidth() != cvWraper.mat.cols ||
            texture->GetHeight() != cvWraper.mat.rows ||
            texture->GetFormat() != GL_RGBA) {
            texture->SetNumLevels(0);
            success = texture->SetSize(cvWraper.mat.cols, cvWraper.mat.rows, GL_RGBA, TEXTURE_DYNAMIC);
            assert(success);
        }
        success = texture->SetData(0, 0, 0, cvWraper.mat.cols, cvWraper.mat.rows, cvWraper.mat.data);
[/code]

After the update I see no changes.  Am I missing something? Is there a "Texture did update" function? I'm using OpenGL. If I force calling SetSize function above then I see black where the texture is supposed to be. Texture contains alpha components.

Thank you.

-------------------------

cadaver | 2017-01-02 01:13:53 UTC | #2

At least for testing, I suggest creating a new texture from scratch and setting its format/size explicitly, instead of modifying the one loaded by the material. That way you can be sure any settings in the original texture aren't interfering.

If texture->SetData() returns success true, the data has already been pushed to OpenGL.

-------------------------

bbm | 2017-01-02 01:13:53 UTC | #3

I've been playing around and keep getting black. I tried creating a new texture and I'm still getting black.

[code]
        //Texture2D *texture = dynamic_cast<Texture2D*>(textureBase);
        Texture2D *texture = new Texture2D(mNode->GetContext());
        texture->SetNumLevels(0);

       // ....
        Material *material = staticModel->GetMaterial(0);
        material->SetTexture(TU_DIFFUSE, texture);
[/code]

I don't know, what the issue can be.

-------------------------

bbm | 2017-01-02 01:13:53 UTC | #4

omg I see the issue

[code]
// this 
texture->SetNumLevels(0);
// should be
texture->SetNumLevels(1);
[/code]

Setting numlevels to 1 makes sense too. Thank you it's working now :smiley:, love your game engine great work.

-------------------------

cadaver | 2017-01-02 01:13:53 UTC | #5

Number of levels 0 means "use as many as necessary to reach 1x1 mip level" in which case you indeed have to fill them all to not get black, depending on the sampling distance. Good that you figured it out!

-------------------------

simonsch | 2018-03-14 08:33:05 UTC | #6

Sry to wake up this old thread but i can't get it working at all.

I wanted to display a simple cube with the Jack_face.jpg and tried creating a new material and a new corresponding texture but the cube remains simply white. Here my code from scene creation:

>  texture = new Texture2D(context_);
    texture->SetNumLevels(1);
    texture->SetSize(1024, 1024, GL_RGB);
    texture->SetData(0, 0, 0,1024, 1024, cache->GetResource<Image>("Textures/Jack_face.jpg"));
    
    material = new Material(context_);
    material->SetTexture(TU_DIFFUSE,texture);

    cubeNode = scene_->CreateChild("cube");
    cubeNode->SetPosition(Vector3(0, 0, 7));
    cubeNode->SetScale(Vector3(5.0f, 5.0f, 5.0f));

    cubeObject = cubeNode->CreateComponent<StaticModel>();
    cubeObject->SetModel(cache->GetResource<Model>("Models/Box.mdl"));

    cubeObject->SetMaterial(material);

When i use one of the provided materials like the skybox, the cube is textured with it.

> cubeObject->SetMaterial(cache->GetResource<Material>("Materials/Skybox.xml"));

I really don't understand how to create a Texture from image and create a correspoding material as well applying it onto a 3D Model via c++, i wish there was a tutorial for this kind of stuff.

-------------------------

