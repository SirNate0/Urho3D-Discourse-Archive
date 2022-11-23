Cpl.Bator | 2017-01-02 01:12:20 UTC | #1

Hello everybody, in first, thank you for this amazing engine ! 

i've got a some question , i want to continue my old-game with your engine ( [youtube.com/watch?v=zbCcQOPXzmI](https://www.youtube.com/watch?v=zbCcQOPXzmI) )
but , i'm from SFML , and i use spritesheet animation without third party tool.
   - What is the way for use spritesheet animation without any external tool ?

I use a "custom" ressource manager ( with sfml ) for load / get resource , with my resource manager i can load them in separate thread and i can display a beautiful load screeen.
  - what is the good way for doing the same result with urho3D ?

In advance , thanks.

-------------------------

1vanK | 2017-01-02 01:12:20 UTC | #2

I use this code for animating UI Sprite (not Sprite2D):

[code]void UIManager::StopAnimation(Sprite* element)
{
    element->SetAttributeAnimationTime("Image Rect", 0.0f);
    element->SetAttributeAnimationSpeed("Image Rect", 0.0f);
}

void UIManager::StartAnimation(Sprite* element)
{
    element->SetAttributeAnimationSpeed("Image Rect", 1.0f);
}

void UIManager::AddAnimation(Sprite* element, const char* textureName, int frameWidth, int frameHeight,
                             int totalNumFrames, int maxColumns, float delay)
{
    element->SetTexture(CACHE->GetResource<Texture2D>(textureName));
    element->SetBlendMode(BLEND_ALPHA);
    element->SetSize(frameWidth, frameHeight); // Sprite size on screen.

    SharedPtr<ValueAnimation> animation(new ValueAnimation(context_));
    float time = 0.0f;

    for (int i = 0; i < totalNumFrames; i++)
    {
        int row = i / maxColumns;
        int col = i % maxColumns;
        IntRect rect(col * frameWidth, row * frameHeight, (col + 1) * frameWidth, (row + 1) * frameHeight);
        animation->SetKeyFrame(time, rect);
        time += delay;
    }

    // At the end again show firs frame
    animation->SetKeyFrame(time, IntRect(0, 0, frameWidth, frameHeight));

    animation->SetInterpolationMethod(IM_NONE);
    element->SetAttributeAnimation("Image Rect", animation);
}
[/code]

Using:
[code]
    auto animatedSprite = UI_ROOT->CreateChild<Sprite>();
    AddAnimation(animatedSprite, "Textures/AnimExclam.png", 20, 64, 20, 10, 1.0f / 24);
[/code]

[img]http://savepic.ru/9708239.png[/img]

I have not tried, but most likely this approach will work for Sprite2D.

-------------------------

Cpl.Bator | 2017-01-02 01:12:20 UTC | #3

thank you, i will try this method soon.

-------------------------

