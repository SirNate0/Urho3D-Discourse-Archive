codder | 2017-01-02 01:12:27 UTC | #1

Hello,

I'm a bit confusing about how to load and draw a Texture from memory.

I have a memory buffer containing raw compressed pixels.

But how do I do the transition from it to Image->Texture->Sprite?

Sorry for my newbie question

-------------------------

Victor | 2017-01-02 01:12:27 UTC | #2

If you have your material/shader setup already you can use the material and do the following

[code]
// Get your material
Cache* cache = GetSubsystem<ResourceCache>();
Material* mat = cache->GetResource<Material>("../yourmat.xml");

// Get the image and create the texture.
Image* srcImg = SetupImage(pixels);
Texture2D* tex = new Texture2D(GetContext());

// Set the texture data.
tex->SetName("SomeTextureName");
tex->SetSize(srcImage->GetWidth(), srcImage->GetHeight(), Graphics::GetRGBAFormat()); // Or whatever format you are using
tex->SetData(srcImg, useAlpha); // Set the image here
tex->SetFilterMode(TextureFilterMode::FILTER_BILINEAR);

// Update the material.
mat->SetTexture(TerrainUnit::TU_DIFFUSE, tex); // On desktop you can have up to 8... sure wish it was 10-12 heh
[/code]

I hope that helps! Some settings you may not need but I though I'd show you what's available. 

As for sprites, once you've put the image data into your texture you'd of course call sprite->SetTexture(). Although if you were using a shader you would set the material as above for your sprites (best to use an image atlas if you were doing this in the shader).

-------------------------

