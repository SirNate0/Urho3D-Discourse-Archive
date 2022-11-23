vivienneanthony | 2017-01-02 01:00:47 UTC | #1

Hi,

I'm trying to add little icons for a player status on a UI. This is the code. It keeps tellling me in the debug. Anyone knows whats wrong?

Vivienne


[code]
[Tue Oct 14 09:10:14 2014] DEBUG: Loading resource UI/Buttons/healthbarindicate.png
[Tue Oct 14 09:10:14 2014] ERROR: Could not load unknown resource type 882E
[Tue Oct 14 09:10:14 2014] DEBUG: Set occlusion buffer size 256x160 with 5 mip levels
[/code]

[code]/// Update player info
void ExistenceClient::UpdatePlayerInfoBar(void)
{

    /// Get resources
    ResourceCache * cache = GetSubsystem<ResourceCache>();
    UI* ui_ = GetSubsystem<UI>();

    /// Get  UIElement
    UIElement * PlayerInfoUIElement = (UIElement*)ui_->GetRoot()->GetChild("PlayerInfoUIElement", true);

    /// Create a sprite
    Sprite * spriteSlot = new Sprite(context_);

    /// Load sprite
    spriteSlot->SetTexture(cache->GetResource<Texture>("Resources/Textures/blankindicatorlarge.png"));
    spriteSlot->SetPosition(4,4);

    PlayerInfoUIElement -> AddChild(spriteSlot);
[/code]
}

-------------------------

thebluefish | 2017-01-02 01:00:47 UTC | #2

Hi,

882E is the StringHash for Texture. Texture is a base class used for Texture2D and Texture3D, and cannot be used directly.

To fix, change
[code]
spriteSlot->SetTexture(cache->GetResource<Texture>("Resources/Textures/blankindicatorlarge.png"));
[/code]

to
[code]
spriteSlot->SetTexture(cache->GetResource<Texture2D>("Resources/Textures/blankindicatorlarge.png"));
[/code]

You may need to update your headers.

-------------------------

