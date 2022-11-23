redmouth | 2017-06-05 19:53:22 UTC | #1

    SharedPtr<Sprite> gameLogo; //defined in class MainScreen

The button becomes vague after adding unused function CreateLogo, without method CreateLogo() the button shows clearly.  Really weird.

 
    void MainMenuScreen::CreateLogo()
    {
        // Get logo texture
        ResourceCache* cache = GetSubsystem<ResourceCache>();
        Texture2D* logoTexture = cache->GetResource<Texture2D>("Textures/FishBoneLogo.png");
        if (!logoTexture)
            return;
    
        // Create logo sprite and add to the UI layout
        gameLogo = parent->CreateChild<Sprite>();
    
        // Set logo sprite texture
        gameLogo->SetTexture(logoTexture);
    
        int textureWidth = logoTexture->GetWidth();
        int textureHeight = logoTexture->GetHeight();
    
        // Set logo sprite scale
        gameLogo->SetScale(256.0f / textureWidth);
    
        // Set logo sprite size
        gameLogo->SetSize(textureWidth, textureHeight);
    
        // Set logo sprite hot spot
        //gameLogo->SetHotSpot(textureWidth, textureHeight);
    
        Graphics* graphics = GetSubsystem<Graphics>();
        int x = graphics->GetWidth()/2 - 256/2;
        int y = int(textureHeight * gameLogo->GetScale().y_);
        gameLogo->SetPosition(x, y);
        // Set logo sprite alignment
        //gameLogo->SetAlignment(HA_CENTER, VA_TOP);
    
        //gameLogo->SetPosition(128, 256);
    
        // Make logo not fully opaque to show the scene underneath
        gameLogo->SetOpacity(0.9f);
    
        // Set a low priority for the logo so that other UI elements can be drawn on top
        gameLogo->SetPriority(-100);
    }

screen showing well-rendered button:
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/a205231f916a8d87867338d9346736dcd0aeb813.png" width="690" height="431">

vague buttons:
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/4c4d5cced34e256a862f4522e9874fd95d6f0775.png" width="690" height="431">

-------------------------

Lumak | 2017-06-05 17:00:39 UTC | #2

It happens when you have no default UI style, add:

[code]
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    UI* ui = GetSubsystem<UI>();

    UIElement* root = ui->GetRoot();
        // Load the style sheet from xml
        root->SetDefaultStyle(cache->GetResource<XMLFile>("UI/DefaultStyle.xml"));

[/code]

-------------------------

redmouth | 2017-06-06 00:48:54 UTC | #3

I have already set DefaultStyle for UI ROOT.   The pasted code is not referenced anywhere in the project.  Removing the unused code the button rendered clearly.

-------------------------

Lumak | 2017-06-06 01:35:16 UTC | #4

Have you ran 02_HelloGUI to see if that fails? Essentially, what you got is a simpler version of that.

-------------------------

redmouth | 2017-06-06 05:22:46 UTC | #5

02 does not fail. It works very well.

-------------------------

Lumak | 2017-06-06 18:09:57 UTC | #6

Right. So the data required for default UI style is there. The typical reason where UI buttons show different textures is because the default UI style is yet set. Be sure that the default UI style is set before creating any UI elements - follow the 02_HelloGUI example.  Better yet, modify and work with the sample code.

-------------------------

redmouth | 2017-06-08 15:42:51 UTC | #7

Updated:

The following code will show the logo and other UIs as expected

        Graphics* graphics = GetSubsystem<Graphics>();
        ResourceCache *cache = GetSubsystem<ResourceCache>();
        UI *ui = GetSubsystem<UI>();
        Sprite *sprite = ui->GetRoot()->CreateChild<Sprite>("sprite");
        Texture2D *texture2D = cache->GetResource<Texture2D>("Textures/FishBoneLogo.png");
        sprite->SetTexture(texture2D);
        int width = 256;
        int height = 128;
        /*int textureWidth = texture2D->GetWidth();
        int textureHeight = texture2D->GetHeight();*/
        sprite->SetSize(width, height);
        sprite->SetPosition(graphics->GetWidth()/2 - width/2, 0);


but with the following uncommented

        /*int textureWidth = texture2D->GetWidth();
        int textureHeight = texture2D->GetHeight();*/

all the UIs become vague as shown above.  Note here the call to texture2D->GetWidth() and texture2D->GetHeight() must be retained.

        Graphics* graphics = GetSubsystem<Graphics>();
        ResourceCache *cache = GetSubsystem<ResourceCache>();
        UI *ui = GetSubsystem<UI>();
        Sprite *sprite = ui->GetRoot()->CreateChild<Sprite>("sprite");
        Texture2D *texture2D = cache->GetResource<Texture2D>("Textures/FishBoneLogo.png");
        sprite->SetTexture(texture2D);
        int width = 256;
        int height = 128;
        int textureWidth = texture2D->GetWidth();
        int textureHeight = texture2D->GetHeight();
        sprite->SetSize(width, height);
        sprite->SetPosition(graphics->GetWidth()/2 - width/2, 0);

-------------------------

Lumak | 2017-06-08 19:13:16 UTC | #8

Yeah, that's weird. I see nothing wrong with what you wrote that'll cause your UI elements to lose texture.
It's as if there's function/data misalignment in linking caused by partial rebuild of the Urho3Dlib due to some change in its components or library. I'd suggest doing a [b]clean rebuild of the build tree[/b] and your project, but you mentioned 02 sample works properly, so I don't know if it'll help.

-------------------------

