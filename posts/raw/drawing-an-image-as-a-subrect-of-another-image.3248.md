johnnycable | 2017-06-14 13:39:00 UTC | #1

Hello, I'm trying to draw some 2d stuff but I'm missing something. In the code I create a node with sprite2d comp by using a section of another image, but it doesn't show on the screen. As a base I'm using example 24. In create scene I add:

    auto createNode = [&](String spriteName) ->Node* {
        Node* node = scene_->CreateChild();
        StaticSprite2D* spriteComp {node->CreateComponent<StaticSprite2D>()};
        Sprite2D* sprite = cache->GetResource<Sprite2D>(spriteName);
        spriteComp->SetSprite(sprite);
        return node;
    };

    auto subSpriteShow = [&](){
    
        int subImageRow = 0;
        int subImageCol = 0;
        
        //load the whole image
        Image* wholeImage = cache->GetResource<Image>("GameData/2D/mona lisa.png");
        int wholeImageSize = wholeImage->GetWidth();
        //images are squared by design
        int subImageSize = wholeImageSize / 4;
        
        //left-top-right-bottom
        IntRect subImageRect = IntRect(
                                 subImageCol * subImageSize, subImageRow * subImageSize,
                                 subImageCol * subImageSize + subImageSize, subImageRow * subImageSize + subImageSize);
        
        Image* subImage = wholeImage->GetSubimage(subImageRect);
        
        if (!subImage) {
            URHO3D_LOGERROR("Not able to slice image. Aborting.");
            return;
        }
        
        //testing output. it outputs a correct image
        subImage->SavePNG("GameData/2D/mona slice.png");
        
        //create Texture2D
        Texture2D* subTex2D = new Texture2D(context_);
        subTex2D->SetData(subImage);
        subTex2D->SetSize(subImageSize, subImageSize, Graphics::GetRGBAFormat(), TextureUsage::TEXTURE_STATIC);
        
        //create Sprite2D
        Sprite2D* subSprite = new Sprite2D(context_);
        subSprite->SetTexture(subTex2D);
        subSprite->SetRectangle(subImageRect);

        //this works ok, using the created image, and shows it on screen
        //lisaNode = createNode("GameData/2D/mona slice.png");
        
        //this doesn't show anything
        //create node
        lisaNode = scene_->CreateChild("lisaNode");
        lisaNode->SetPosition(Vector3::ZERO);
        
        //create component
        spriteText2d = lisaNode->CreateComponent<StaticSprite2D>(LOCAL);
        spriteText2d->SetSprite(subSprite);
        spriteText2d->SetLayer(100);
        

        
    };
    
    subSpriteShow();

If I use the saved image, everything shows ok. There must be st I'm missing in the construction of sub sprite... thanks in advance.

-------------------------

Lumak | 2017-06-16 03:15:57 UTC | #2

In your subTex2D creation process:
[quote="johnnycable, post:1, topic:3248"]
//create Texture2D
    Texture2D* subTex2D = new Texture2D(context_);
    subTex2D-&gt;SetData(subImage);
    subTex2D-&gt;SetSize(subImageSize, subImageSize, Graphics::GetRGBAFormat(), TextureUsage::TEXTURE_STATIC);
[/quote]

call SetSize() before SetData()

-------------------------

johnnycable | 2017-06-15 11:14:42 UTC | #3

That did the trick. Now something is shown, but feels like kind of overstreched...
Original Image:
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/88a101501608457450c92710855100b1be250b2a.png" width="500" height="500">

Cut Image, saved by subImage->SavePNG:

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/2e8e4cb93e02ca66590563ff0dcbe92a14032b42.png" width="128" height="128">

Image displayed by Sprite2D:

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/9c87fb07e24cd69c9577ea17cdfbb2f3b38494c1.png" width="328" height="314">

(Size is the same as previous on screen)

Just one more test revealed that:

subSprite->SetRectangle(IntRect(0,0,128,128)) show the image correctly. I was setting the size of the whole image, not the subdivided one.

Thanks again for the help.

-------------------------

