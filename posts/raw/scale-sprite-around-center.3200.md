redmouth | 2017-06-03 16:25:38 UTC | #1

    ResourceCache* cache = GetSubsystem<ResourceCache>();
    Graphics* graphics = GetSubsystem<Graphics>();
    Sprite* sprite = ui->GetRoot()->CreateChild<Sprite>("Spite");
    int size = 128;
    sprite->SetSize(size, size);
    sprite->SetPosition(graphics->GetWidth()/2 - size/2, graphics->GetHeight()/2 - size/2);
    sprite->SetTexture(cache->GetResource<Texture2D>("Textures/1.png"));
    //SharedPtr<ValueAnimation> scaleAnimation(new ValueAnimation(context_));
    ValueAnimation* scaleAnim = new ValueAnimation(context_);
    scaleAnim->SetKeyFrame(0.0f, Vector2(1.0f, 1.0f));
    scaleAnim->SetKeyFrame(10.0f, Vector2(0.5f, 0.5f));

    sprite->SetAttributeAnimation("Scale", scaleAnim, WM_ONCE);



The above code scale the sprite with it's left-top corner position fixed, how to make it scale around the center?

-------------------------

slapin | 2017-06-03 22:00:22 UTC | #3

I think scale then move approach should fix your problem.

-------------------------

redmouth | 2017-06-04 10:11:31 UTC | #4

Adding a Position attribute animation works.

I'm confused , for Sprite, the "Position" attribute animation does not accept IntVector2, but only Vector2.

-------------------------

