nergal | 2017-10-14 15:56:31 UTC | #1

I want to load an png image but not sure how. I've found the Image class but I can't find an usage example for how to load an png and then use that class to read pixels from the loaded png.

Could I please get a hint? :slight_smile: 

(I'm using C++ not Lua)

-------------------------

ext1 | 2017-10-15 01:52:07 UTC | #2

To load a PNG image as an UI element, you could use something like this:

    BorderImage* yourImage_ = new BorderImage(context_);
    yourImage_->SetTexture(cache->GetResource<Texture2D>("yourImage.png"));
    yourImage_->SetSize(100,100);
    yourImage_->SetAlignment(HA_LEFT,VA_TOP);
    yourImage_->SetPosition(0,0);
    uiRoot_->AddChild(yourImage_);

To load a PNG image as a sprite, check the samples [24_Urho2DSprite](https://github.com/urho3d/Urho3D/tree/master/Source/Samples/24_Urho2DSprite) and [36_Urho2DTileMap](https://github.com/urho3d/Urho3D/tree/master/Source/Samples/36_Urho2DTileMap).

And to load a PNG image as an "object" on the 3D space, I guess you could load it on a plane object (similar to how it was done on sample [38_SceneAndUILoad](https://github.com/urho3d/Urho3D/tree/master/Source/Samples/38_SceneAndUILoad)), maybe like this:

    Node* planeNode_ = scene_->CreateChild("Plane");
    planeNode_->SetScale(Vector3(2.0f, 2.0f, 2.0f));
    planeNode_->SetRotation(Quaternion(-90.0f, 0.0f, 0.0f));
    StaticModel* planeObject = planeNode_->CreateComponent<StaticModel>();
    planeObject->SetModel(cache->GetResource<Model>("Models/Plane.mdl"));
    planeObject->SetMaterial(cache->GetResource<Material>("Materials/yourMaterial.xml"));

And yourMaterial.xml:

    <material>
    <technique name="Techniques/DiffUnlit.xml"/>
    <texture name="yourImage.png" unit="diffuse"/>
    <parameter name="MatDiffColor" value="1 1 1 1"/>
    <parameter name="MatSpecColor" value="1 1 1 1"/>
    </material>

I don't have much experience with the engine yet, so I don't know how you could read the pixels of the PNG image. But I guess you could use the [File API](https://urho3d.github.io/documentation/1.4/class_urho3_d_1_1_file.html) and the [Deserializer](https://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_deserializer.html) for that. Maybe something like this:

    Something imagePixels = (cache->GetFile("yourImage.png"))->Read();

Or:

    File imageFile(context_, GetSubsystem<FileSystem>()->GetProgramDir() + "yourImage.png", FILE_READ);
    Something imagePixels = imageFile.Read();

-------------------------

JTippetts | 2017-10-15 09:19:27 UTC | #3

You can use [Image](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Resource/Image.h) to load a PNG and read pixels. Pass a Deserializer (such as a [File](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/IO/File.h) ) to the Load method. You can then call GetPixel() on the image.

-------------------------

nergal | 2017-10-15 09:38:49 UTC | #4

So I've loaded an File, but how do I use that in the Deserializer class? I don't understand how to make the Deserializer class use the File object, in order to pass it to Image->BeginLoad().

-------------------------

JTippetts | 2017-10-15 10:44:15 UTC | #5

File inherits from Deserializer. Just pass the file to Image->Load(). (Image inherits Load() from Resource, which will call both BeginLoad() and EndLoad()).

    File file(context,fname);
    Image i;
    i.Load(file);

-------------------------

