Taqer | 2019-06-16 19:30:09 UTC | #1

Hi, 
I have a problem, in my situation, I have many images, some are identical, and others different.
Say I want to flip just a part of identical images, I observed that if I will load one image and then try to load the same image second time, it will not really load it, but just assign already loaded image right?
So if I want to flip only few of identical images, it will flip all of them, how to avoid that?

-------------------------

Leith | 2019-06-17 09:33:52 UTC | #2

Typically, we use UV coordinates to determine how an image (texture) is mapped to a 2d quad or 3d triangle. Which Urho class are you using to display your images?

Think of your image as having X and Y "pixel values" between 0 and 1 - we can define four (cyclic) corners : <0,0>, <0,1>, <1,1>, <1,0> - these are the corners of your image, no matter what its actual pixel dimensions are - these are the "NDC" coordinates of a rectangle in 2D. (Homework: look up NDC)
Things like "sprites" typically just have upper and lower corner "min/max corner" coordinates, often described in terms of NDC texture coordinates (aka UV's) but if we can imagine that our original image has four corner coordinates, we can "rotate" (and/or flip) our image by setting the corner coordinates appropriately. 
We can even use UV's to describe which element of an "atlas texture" or "sprite sheet" we would like to refer to. We don't need to just use 0 and 1. We can use values inbetween. This means more than one sprite can exist on the same input texture/image.

In OpenGL, the 0,0 corner tends to be in the lower left, while 1,1 is in the top right.
Conversely, in DirectX, 0,0 is (more sanely in my opinion) in the top left, while 1,1 is the bottom right.

I am not sure which specification Urho decides to use, but so far it has not presented as a problem.

-------------------------

Taqer | 2019-06-17 14:50:49 UTC | #3

Im using Image class and Flip() function. I know how UV work, just wanted to know how to "instantiate" those images so I can affect only those I want and not all.

-------------------------

guk_alex | 2019-06-17 14:51:39 UTC | #4

Basically, if you assign the images onto some objects, you can rotate the object itself. What is you usecase for that Images?

-------------------------

Taqer | 2019-06-17 14:55:32 UTC | #5

But they are UI elements not nodes, I dont see rotation functions.

-------------------------

guk_alex | 2019-06-17 16:16:02 UTC | #6

UI elements are not nodes, you're right. You might need other workflow for it depending what do you want from ui.
What about Sprite class from UI? It have rotation control functions, but you need to work with Textures in that case, not Images.

-------------------------

ab4daa | 2019-06-17 17:08:04 UTC | #8

Did a quick test to clone Image.
Hope I do not misunderstand your problem.

	Image*  img = cache->GetResource<Image>("Textures/Logo.png");
	SharedPtr<Image> img2 = MakeShared<Image>(context_);
	img2->SetSize(img->GetWidth(), img->GetHeight(), img->GetComponents());
	img2->SetData(img->GetData());
	img2->FlipHorizontal();

	SharedPtr<Texture2D>  tex = MakeShared<Texture2D>(context_);
	tex->SetSize(img->GetWidth(), img->GetHeight(), Graphics::GetRGBAFormat());
	tex->SetData(img, true);
	BorderImage  * bi = uiRoot_->CreateChild<BorderImage>();
	bi->SetBlendMode(BLEND_ADD);
	bi->SetSize(128, 128);
	bi->SetTexture(tex);
	bi->SetPosition(0, 0);

	SharedPtr<Texture2D>  tex2 = MakeShared<Texture2D>(context_);
	tex2->SetData(img2, true);
	BorderImage  * bi2 = uiRoot_->CreateChild<BorderImage>();
	bi2->SetBlendMode(BLEND_ADD);
	bi2->SetSize(128, 128);
	bi2->SetTexture(tex2);
	bi2->SetPosition(128, 0);

![%E5%9C%96%E7%89%87|646x500](upload://nIvhpf1g3tT37A0Sx3Nma7BnI0g.png)

-------------------------

