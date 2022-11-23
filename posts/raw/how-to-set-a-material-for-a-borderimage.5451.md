majhong | 2019-08-12 07:21:50 UTC | #1

I found that BorderImage has a member function SetMaterial
	void SetMaterial (Material *material)  
	//Set material for custom rendering.

I got an incorrect display (probably a small part of the texture)  when i had set a  material for it.

the material is a video frame (yuv420p piexl format)   refferd to  Theora video playback (https://discourse.urho3d.io/t/theora-video-playback/2144/8)

the follow is my code:
1 create a  BorderImage

            UIElement* root = GetSubsystem<UI>()->GetRoot();
            BorderImage* pImgFrame=root->CreateChild<BorderImage>();
            pImgFrame->SetPosition(0,0);
            pImgFrame->SetSize(640,360);

2 set a material
            pImgFrame->SetMaterial(outputMaterial);

It is ok to assign the outputMaterial to a cube or a plane.![help|651x500](upload://cALgH1GVbwImyrFHJMTVSFltPeX.jpeg)

-------------------------

Leith | 2019-08-12 07:09:03 UTC | #2

What is your use case for changing the material?
If you're just trying to display an image, this may help:

[code]
            // Set up a UI Element to display the SplashScreen Image
            ResourceCache* cache = GetSubsystem<ResourceCache>();
            UI* ui = GetSubsystem<UI>();
            splashUI = new BorderImage(context_);
            splashUI->SetName("Splash");
            Texture2D* texture = cache->GetResource<Texture2D>("Textures/LogoLarge.png");
            splashUI->SetTexture(texture); // Set texture
            splashUI->SetSize(texture->GetWidth(), texture->GetHeight());
            splashUI->SetAlignment(HA_CENTER, VA_CENTER);
            ui->GetRoot()->AddChild(splashUI);
[/code]

Not the best example in the world, granted..

-------------------------

majhong | 2019-08-12 07:37:42 UTC | #3

i want to display a web camera in a borderimage!

the outputMaterial have convert a yuv420p to rgb32  format!

-------------------------

Dave82 | 2019-08-12 08:30:43 UTC | #4

Call SetFullImageRect() on your borderimage. But if you need a 2d render surface just use a sprite2d.

-------------------------

Pencheff | 2019-08-12 09:17:19 UTC | #5

Or BorderImage::SetImageRect() with the width and height of the video texture:
[code]
video_view_->SetImageRect(IntRect(0, 0, video_width, video_height));
[/code]

-------------------------

majhong | 2019-08-12 10:10:37 UTC | #6




video_box_->SetMaterial(outputMaterial);        
Texture*  pTexture= video_box_->GetTexture();

i got a nullprt for  GetTexture when i set the outputMaterial.

so the SetFullImageRect or SetImageRect do not work!

-------------------------

majhong | 2019-08-12 10:13:35 UTC | #7

thanks !
it is ok


        video_box_->SetMaterial(outputMaterial);
        Texture*  pTexture=outputMaterial->GetTexture(TU_DIFFUSE);
        video_box_->SetTexture(pTexture);
        video_box_->SetFullImageRect();

-------------------------

Pencheff | 2019-08-12 10:15:32 UTC | #8

I was just about to mention that you explicitly need to set the BorderImage texture even if the material already has one, since BorderImage needs a valid texture to calculate UV when you use Set****Rect() methods.

-------------------------

