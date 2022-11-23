att | 2017-01-02 00:59:27 UTC | #1

Hi,
I want to let sprite to respond to touch events, so I subclassed the sprite class, here is my implementation,
[code]#ifndef __Urho3D__SpriteButton__
#define __Urho3D__SpriteButton__

#include "Sprite.h"

using namespace Urho3D;

class SpriteButton : public Sprite
{
    OBJECT(SpriteButton);
//    BASEOBJECT(SpriteButton);
    
public:
    SpriteButton(Context *context);
    virtual ~SpriteButton();
    
    static void RegisterObject(Context* context);
    
    /// React to mouse click begin.
    virtual void OnClickBegin(const IntVector2& position, const IntVector2& screenPosition, int button, int buttons, int qualifiers, Cursor* cursor);
    /// React to mouse click end.
    virtual void OnClickEnd(const IntVector2& position, const IntVector2& screenPosition, int button, int buttons, int qualifiers, Cursor* cursor, UIElement* beginElement);
    /// React to mouse drag motion.
    virtual void OnDragMove(const IntVector2& position, const IntVector2& screenPosition, int buttons, int qualifiers, Cursor* cursor);
};

#endif /* defined(__Urho3D__SpriteButton__) */[/code]

[code]#include "Precompiled.h"
#include "Context.h"
#include "ResourceCache.h"
#include "Texture2D.h"
#include "SpriteButton.h"

namespace Urho3D
{
    extern const char* UI_CATEGORY;
}

SpriteButton::SpriteButton(Context *context)
: Sprite(context)
{
    
}

SpriteButton::~SpriteButton()
{
    
}

void SpriteButton::RegisterObject(Context* context)
{
    context->RegisterFactory<SpriteButton>(UI_CATEGORY);
    COPY_BASE_ATTRIBUTES(SpriteButton, Sprite);
    
    UPDATE_ATTRIBUTE_DEFAULT_VALUE(SpriteButton, "Is Enabled", true);
//    UPDATE_ATTRIBUTE_DEFAULT_VALUE(Button, "Focus Mode", FM_FOCUSABLE);
}

void SpriteButton::OnClickBegin(const IntVector2& position, const IntVector2& screenPosition, int button, int buttons, int qualifiers, Cursor* cursor)
{
    
}

void SpriteButton::OnClickEnd(const IntVector2& position, const IntVector2& screenPosition, int button, int buttons, int qualifiers, Cursor* cursor, UIElement* beginElement)
{
    
}

void SpriteButton::OnDragMove(const IntVector2& position, const IntVector2& screenPosition, int buttons, int qualifiers, Cursor* cursor)
{
    
}[/code]

But, it not work. Did the sprite can respond to touch events? and how can I do it?
Thank you very much!

-------------------------

friesencr | 2017-01-02 00:59:27 UTC | #2

Every ui element will respond to click/touch events.  They will not necessarily work like a button where it has a press/release.   Touch/Click start will fire though.  Did you add your ui element to the ui->root?

-------------------------

friesencr | 2017-01-02 00:59:27 UTC | #3

I would also check to see if the sprite has a size.  Some of the other ui elements are set to not clip their contents.  So the contents are completely visible but the holder has no size.

-------------------------

att | 2017-01-02 00:59:27 UTC | #4

[quote="friesencr"]Every ui element will respond to click/touch events.  They will not necessarily work like a button where it has a press/release.   Touch/Click start will fire though.  Did you add your ui element to the ui->root?[/quote]

I created the sprite like this,
[code]    SpriteButton *sprite = GetSubsystem<UI>()->GetRoot()->CreateChild<SpriteButton>();
    Texture2D *tex = cache_->GetResource<Texture2D>("Textures/colour.png");
    sprite->SetTexture(tex);
    sprite->SetImageRect(IntRect(132, 0, 64+132, 64));
    sprite->SetSize(200, 200);
    sprite->SetHotSpot(IntVector2(sprite->GetWidth()/2, sprite->GetHeight()/2));
    sprite->SetBlendMode(BLEND_ADD);
    sprite->SetColor(Color::WHITE);
    sprite->SetPosition(width * 0.5f, height * 0.5f);[/code]

-------------------------

att | 2017-01-02 00:59:27 UTC | #5

[quote="friesencr"]I would also check to see if the sprite has a size.  Some of the other ui elements are set to not clip their contents.  So the contents are completely visible but the holder has no size.[/quote]

I found the problem, the sprite must set enable manually like sprite->SetEnable(true), and then it can accept click events.
But I had updated the enable value like this, 
[code]void SpriteButton::RegisterObject(Context* context)
{
    context->RegisterFactory<SpriteButton>(UI_CATEGORY);
    COPY_BASE_ATTRIBUTES(SpriteButton, Sprite);
    
    UPDATE_ATTRIBUTE_DEFAULT_VALUE(SpriteButton, "Is Enabled", true);
//    UPDATE_ATTRIBUTE_DEFAULT_VALUE(Button, "Focus Mode", FM_FOCUSABLE);
}[/code]
It seems not updated the enable attribute value.

-------------------------

weitjong | 2017-01-02 00:59:27 UTC | #6

I believe you need to set the property in the constructor as well, as how it is done in the Button class implementation.

-------------------------

