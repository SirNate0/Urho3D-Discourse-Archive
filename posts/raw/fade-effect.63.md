globus | 2017-01-02 00:57:42 UTC | #1

My adaptation of Ogre3D [b]FadeEffectOverlay[/b] sample code for Urho3D.
([url]http://www.ogre3d.org/tikiwiki/tiki-index.php?page=FadeEffectOverlay[/url])

It easy for add this object in any place of code.
And, easy for modify it for add support "change sprite texture" or "Pulse fade effect"

It can be used for example:
    change level or sinematic effects
     blood effects when hero damage

This realized in C++.
For use:

[code]#include "Fader.h"
.......
Fader* fdr = new Fader(context_);// give context from you Object to Fader.
.......
fdr->FadeOut(1.0f); // 1.0f - fade time in seconds[/code]

[b]Fader.h[/b]

[spoiler][code]#pragma once

#include "Object.h"

namespace Urho3D
{
class Sprite;
}

using namespace Urho3D;

class Fader : public Object
{
    OBJECT(Fader);

protected:
    enum fadeState_{
		FADE_NONE,
		FADE_IN,
		FADE_OUT,
		}fadeState_;

    // Fader sprite.
	SharedPtr<Sprite> faderSprite_;

    float currentAlpha_;
    float currentDuration_;
    float totalDuration_;
    bool faderDone_;
    bool faderNowCalled_;

public:

    Fader(Context* context);
    ~Fader(void);

    void BlackScreen();
    void FadeIn(float duration = 1.0f);
    void FadeOut(float duration = 1.0f);
    void fadeNowIn(float duration = 1.0f);	// Can only be called once
    void fadeNowOut(float duration = 1.0f);	// Can only be called once
    void fade(float timeSinceLastFrame);
    bool isFaderCalled(void){return faderNowCalled_;};	
    bool isFaderDone(void){ return faderDone_; };

private:
    // Subscribe to necessary events.
    void SubscribeToEvents();
    // Handle application update. Fader need for Time step.
    void HandleUpdate(StringHash eventType, VariantMap& eventData);
};[/code][/spoiler]

[b]Fader.cpp[/b]

[spoiler][code]#include "CoreEvents.h"
#include "ResourceCache.h"
#include "Sprite.h"
#include "Texture2D.h"
#include "UI.h"
#include "Graphics.h"

#include "Fader.h"

// All Urho3D classes reside in namespace Urho3D
using namespace Urho3D;

Fader::Fader(Context* context) :
    Object(context)
{
    // ======== Create default Sprite ===============
	Graphics* gfx = GetSubsystem<Graphics>();
	
    // Get Fader texture
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    Texture2D* faderTexture = cache->GetResource<Texture2D>("Textures/2x2_black.png");
    if (!faderTexture)
        return;

    // Create fader sprite and add to the UI layout
    UI* ui = GetSubsystem<UI>();
    faderSprite_ = ui->GetRoot()->CreateChild<Sprite>();

    // Set fader sprite texture
    faderSprite_->SetTexture(faderTexture);

    // Set fader sprite size
    faderSprite_->SetSize(gfx->GetWidth(), gfx->GetHeight());

    // Set fader sprite alignment
    faderSprite_->SetAlignment(HA_LEFT, VA_TOP);
    
    // Hide by default
    faderSprite_->SetVisible(false);
    
    // Z order for fader so that other UI elements can be drawn on bottom
    faderSprite_->SetPriority(400);
    // ======== End Create default Sprite ===========

	// Reset all to default state.
    fadeState_ = FADE_NONE;
    currentAlpha_ = 0.0f;
    faderDone_ = true;
    faderNowCalled_ = false;

	SubscribeToEvents();
}

Fader::~Fader(void)
{
}

    /// Subscribe to necessary events.
void Fader::SubscribeToEvents()
{
    // get Time step for Fader in E_RENDERUPDATE Core step
    SubscribeToEvent(E_RENDERUPDATE, HANDLER(Fader, HandleUpdate));
}

void Fader::HandleUpdate(StringHash eventType, VariantMap& eventData)
{
    if (faderNowCalled_)
	{
	    using namespace Update;
	    
		float timeStep = eventData[P_TIMESTEP].GetFloat();

        if(!faderDone_)
			fade(timeStep);
	}
}

void Fader::BlackScreen()
{
    if(faderDone_)
    {
        faderSprite_->SetOpacity(1.0f);
        faderSprite_->SetVisible(true);
    }
}

void Fader::FadeIn(float duration)
{
    if( duration < 0 )
        duration = 1.0f;//-duration;
//    if( duration < 0.000001 )
//        duration = 1.0;
    currentAlpha_ = 1.0f;
    totalDuration_ = duration;
    currentDuration_ = duration;
    fadeState_ = FADE_IN;
	faderSprite_->SetVisible(true);

    faderDone_ = false;
	faderNowCalled_ = true;
}

void Fader::FadeOut(float duration)
{
	if( duration < 0 )
		duration = 1.0f;//-duration;
//	if( duration < 0.000001 )
//		duration = 1.0;

	currentAlpha_ = 0.0f;
	totalDuration_ = duration;
	currentDuration_ = 0.0f;
	fadeState_ = FADE_OUT;
	faderSprite_->SetVisible(true);

	faderDone_ = false;
	faderNowCalled_ = true;
}

void Fader::fadeNowIn(float duration)
{
	if( faderNowCalled_ == false )
	{
		FadeIn(duration);
		faderNowCalled_ = true;
	}
}

void Fader::fadeNowOut(float duration)
{
	if( faderNowCalled_ == false )
	{
		FadeOut(duration);
		faderNowCalled_ = true;
	}
}

void Fader::fade(float timeStep)
{
	if( fadeState_ != FADE_NONE && faderSprite_)
	{
		// Set the currentAlpha_ value of the _overlay
		    faderSprite_->SetOpacity(currentAlpha_);

		// If fading in, decrease the currentAlpha_ until it reaches 0.0
		if( fadeState_ == FADE_IN )
		{
			currentDuration_ -= timeStep;
			currentAlpha_ = currentDuration_ / totalDuration_;
			if( currentAlpha_ < 0.0f )
			{
	            faderSprite_->SetVisible(false);
				fadeState_ = FADE_NONE;
				faderDone_ = true;
				faderNowCalled_ = false;
			}
		}

		// If fading out, increase the currentAlpha_ until it reaches 1.0
		else if( fadeState_ == FADE_OUT )
		{
			currentDuration_ += timeStep;
			currentAlpha_ = currentDuration_ / totalDuration_;
			if( currentAlpha_ > 1.0 )
			{
	            faderSprite_->SetVisible(false);
				fadeState_ = FADE_NONE;
				faderDone_ = true;
				faderNowCalled_ = false;
			}
		}
	}
}[/code][/spoiler]

-------------------------

