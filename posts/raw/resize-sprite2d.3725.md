antonio-cg | 2017-11-09 20:54:20 UTC | #1

Hello, i have some trouble with sprite2D, i have 3 diferents images with diferents sizes, i need to make the 3 images to the same size, im using 	

Sprite2D* test = cache->GetResource<Sprite2D>("Urho2D/album.jpg");

to load the image but i can access to the image to resize, any ideas how i can do it?

-------------------------

kostik1337 | 2017-11-10 09:34:28 UTC | #2

I think, you need to load your image as Image first, resize it ([Resize()](https://urho3d.github.io/documentation/1.7/class_urho3_d_1_1_image.html#a5be924efa3bb0f85f2d812d0149aedda)), then load it into Texture2D, and set that texture into Sprite2D

-------------------------

antonio-cg | 2017-11-10 16:23:08 UTC | #3

i try loading into texture but dosent works i try this code,

        Image* img = cache->GetResource<Image>("Urho2D/album.jpg");
    	img->Resize(300, 300);
    	Texture2D* tex = new Texture2D(context_);
    	tex->SetData(img);
    	Sprite2D* temSprite = new Sprite2D(context_);
    	temSprite->SetTexture(tex);
    	SharedPtr<Node> nodoAlbum(scene_->CreateChild("StaticSprite2D"));
    	nodoAlbum->SetPosition(Vector3(0.0f, 0.0f, 1.0f));
    	StaticSprite2D* staticSpriteAlbum = nodoAlbum->CreateComponent<StaticSprite2D>();
    	staticSpriteAlbum->SetSprite(temSprite);

-------------------------

kostik1337 | 2017-11-13 09:08:46 UTC | #4

Try adding
staticSpriteAlbum->SetDrawRect(Rect(-1, -1, 1, 1));
staticSpriteAlbum->SetTextureRect(Rect(-1, -1, 1, 1));
staticSpriteAlbum->SetUseTextureRect(true);
Also, it seems you don't really need to resize image pixels, you can adjust sprite size with SetDrawRect method

-------------------------

