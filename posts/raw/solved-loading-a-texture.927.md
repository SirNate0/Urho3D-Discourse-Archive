GoogleBot42 | 2017-01-02 01:04:08 UTC | #1

Hello yet another silly question.  I can load a image in Urho3D but how do I load a texture?

Here is an image.

[code]Image* img = cache->GetResource<Image>("Textures/UrhoIcon.png");[/code]

But a texture doesn't work and there doesn't seem to be any way to conver an image to a texture.

[code]Texture* tex = cache->GetResource<Texture>("Textures/UrhoIcon.png");[/code]

This results in no texture returned and the error:

[code]ERROR: Could not load unknown resource type 0261882E[/code]

-------------------------

thebluefish | 2017-01-02 01:04:08 UTC | #2

You will need to use Texture2D instead of Texture. See [url=http://discourse.urho3d.io/t/sprite-will-not-load-on-ui/484/1]this post[/url] for the details.

-------------------------

TikariSakari | 2017-01-02 01:04:08 UTC | #3

If you are using materials, you can just put the name of texture into the materials xml, such as the material/stone.xml:

[code]
<material>
    <technique name="Techniques/DiffNormalPacked.xml" quality="1" />
    <technique name="Techniques/Diff.xml" quality="0" />
    <texture unit="diffuse" name="Textures/StoneDiffuse.dds" />
    <texture unit="normal" name="Textures/StoneNormal.dds" />
    <parameter name="MatSpecColor" value="0.3 0.3 0.3 16" />
</material>
[/code]

Just change the textures file to yours.

Then I used something like this to create custom texture on the fly. Although I do still need to use material file of a model.

[code]
	// Using some random material to create image that we can use for our painted texture
	auto mat = cache->GetResource<Material>( "Materials/UrhoDecal.xml");

	auto tex = SharedPtr<Texture2D>( new Texture2D(context_));
	tex->SetSize(0, 0, 0, TEXTURE_DYNAMIC);

	mat->SetTexture(TextureUnit(), tex);


	auto img = SharedPtr<Image>(new Image(context_));

	img->SetSize(512, 512, 4);
	img->Clear(Color(1, 1, 1, 1));
	for (int y = 0; y < 128; ++y)
	{
		int x = 0;
		for (; x < 128; ++x)
			img->SetPixel(x, y, Color((float)rand() / RAND_MAX, (float)rand() / RAND_MAX,
				(float)rand() / RAND_MAX, (float)rand() / RAND_MAX));


		for (; x < 256; ++x)
			img->SetPixel(x, y, Color(0.5f, 0.f, 0.f, 1.f ));

		for (; x < 384; ++x)
			img->SetPixel(x, y, Color(0.0f, 0.5f, 0.f, 1.f));

		for (; x < 512; ++x)
			img->SetPixel(x, y, Color(0.3f, 0.3f, 0.8f, 1.f));
	}
	tex->SetData(img, false);


[/code]
I am not going to lie, I did find the code from internet and modified it, so honestly I have no idea what the TextureUnit is, but it seems to work, which is good enough for me.

-------------------------

GoogleBot42 | 2017-01-02 01:04:09 UTC | #4

Thanks for your help guys!  I simply needed to use "Texture2D" instead of "Texture".  It works great.  TikariSakari that is useful information about creating textures. (which I probably will need to do later).  Thanks!

-------------------------

GoogleBot42 | 2017-01-02 01:04:09 UTC | #5

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

GoogleBot42 | 2017-01-02 01:04:11 UTC | #6

Asked and answered here: [url]http://discourse.urho3d.io/t/am-i-leaking-memory-here/931/1[/url]

-------------------------

