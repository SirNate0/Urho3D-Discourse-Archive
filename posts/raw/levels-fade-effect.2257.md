artgolf1000 | 2018-02-02 09:48:28 UTC | #1

Hi,

I am testing levels fade effect from each other, and I'm satisfied with the result.

Levels are independent scenes and UI elements, you can use 'BaseLevel' class to derive actual levels, either 2D or 3D scenes.

If you want to switch levels from anywhere, just need to send an event, only level name needed.

Cheers!

MyEvens.h
[code]
#pragma once

#include <Urho3D/Urho3DAll.h>

/// User defined event
namespace MyEvents
{
    static const StringHash E_SET_LEVEL = StringHash("Set levels");
}
[/code]

LevelManager.h
[code]
#pragma once

#include <Urho3D/Urho3DAll.h>
#include "UILevel.h"

class LevelManager : public Object
{
    URHO3D_OBJECT(LevelManager, Object);
public:
    LevelManager(Context* context):
    Object(context)
    {
        // Register all classes
        RegisterAllFactories();

        // Listen to set level event
        SubscribeToEvent(MyEvents::E_SET_LEVEL, URHO3D_HANDLER(LevelManager, HandleSetLevelQueue));
    }

private:
    void RegisterAllFactories()
    {
        // Register classes
        context_->RegisterFactory<UILevel>();
        context_->RegisterFactory<Level1>();
        context_->RegisterFactory<Level2>();
    }
    
    void HandleSetLevelQueue(StringHash eventType, VariantMap& eventData)
    {
        // Busy now
        if (level_queue_.Size()) {
            return;
        }
        // Push to queue
        level_queue_.Push(eventData[MyEvents::E_SET_LEVEL].GetString());
        
        // Subscribe HandleUpdate() function for processing update events
        SubscribeToEvent(E_UPDATE, URHO3D_HANDLER(LevelManager, HandleUpdate));

        // Init fade status
        fade_status_ = 0;
    }
    
    void HandleUpdate(StringHash eventType, VariantMap& eventData)
    {
        using namespace Update;
        
        // Take the frame time step, which is stored as a float
        float timeStep = eventData[P_TIMESTEP].GetFloat();
        
        // Move sprites, scale movement with time step
        fade_time_ -= timeStep;
        
        // Prepare to fade out
        if (fade_status_ == 0) {
            // No old level
            if (!level_) {
                fade_status_++;
                return;
            }
            // Add a new fade layer
            AddFadeLayer();
            fade_window_->SetOpacity(0.0f);
            fade_time_ = MAX_FADE_TIME;
            fade_status_++;
            return;
        }
        
        // Fade out
        if (fade_status_ == 1) {
            // No old level
            if (!level_) {
                fade_status_++;
                return;
            }
            fade_window_->SetOpacity(1.0f-fade_time_/MAX_FADE_TIME);
            
            // Increase fade status
            if (fade_time_ <= 0.0f) {
                fade_status_++;
            }
            return;
        }

        // Release old level
        if (fade_status_ == 2) {
            // No old level
            if (!level_) {
                fade_status_++;
                return;
            }
            // We can not create new level here, or it may cause errors, we have to create it at the next update point.
            level_ = SharedPtr<Object>();
            fade_status_++;
            return;
        }
        
        // Create new level
        if (fade_status_ == 3) {
            // Create new level
            level_ = context_->CreateObject(StringHash(level_queue_.Front()));
            // Remove the old fade layer
            if (fade_window_) {
                fade_window_->Remove();
            }
            // Add a new fade layer
            AddFadeLayer();
            fade_window_->SetOpacity(1.0f);
            fade_time_ = MAX_FADE_TIME;
            fade_status_++;
            return;
        }
        
        // Fade in
        if (fade_status_ == 4) {
            fade_window_->SetOpacity(fade_time_/MAX_FADE_TIME);
            
            // Increase fade status
            if (fade_time_ <= 0.0f) {
                fade_status_++;
            }
            return;
        }
        
        // Finished
        if (fade_status_ == 5) {
            // Remove fade layer
            fade_window_->Remove();
            fade_window_ = SharedPtr<Window>();
            // Unsubscribe update event
            UnsubscribeFromEvent(E_UPDATE);
            // Remove the task
            level_queue_.PopFront();
            // Release all unused resources
            GetSubsystem<ResourceCache>()->ReleaseAllResources(false);
            return;
        }
    }
    
    void AddFadeLayer()
    {
        fade_window_ = new Window(context_);
        // Make the window a child of the root element, which fills the whole screen.
        GetSubsystem<UI>()->GetRoot()->AddChild(fade_window_);
        fade_window_->SetSize(GetSubsystem<Graphics>()->GetWidth(), GetSubsystem<Graphics>()->GetHeight());
        fade_window_->SetLayout(LM_FREE);
        // Urho has three layouts: LM_FREE, LM_HORIZONTAL and LM_VERTICAL.
        // In LM_FREE the child elements of this window can be arranged freely.
        // In the other two they are arranged as a horizontal or vertical list.
        
        // Center this window in it's parent element.
        fade_window_->SetAlignment(HA_CENTER,VA_CENTER);
        // Black color
        fade_window_->SetColor(Color(0.0f, 0.0f, 0.0f, 1.0f));
        // Make it topmost
        fade_window_->BringToFront();
    }
    
    List<String> level_queue_;
    SharedPtr<Object> level_;
    SharedPtr<Window> fade_window_;
    float fade_time_;
    int fade_status_;
    const float MAX_FADE_TIME = 1.0f;
};
[/code]

BaseLevel.h
[code]
#pragma once

#include <Urho3D/Urho3DAll.h>

class BaseLevel : public Object
{
    URHO3D_OBJECT(BaseLevel, Object);
public:
    BaseLevel(Context* context):
    Object(context) {}

    virtual ~BaseLevel()
    {
        Dispose();
    }
protected:
    virtual void Init() {}
    
    virtual void Run()
    {
        if (scene_) {
            scene_->SetUpdateEnabled(true);
        }
    }
    
    virtual void Pause()
    {
        if (scene_) {
            scene_->SetUpdateEnabled(false);
        }
    }
    
    virtual void Dispose()
    {
        // Pause the scene, remove all contents from the scene, then remove the scene itself.
        if (scene_) {
            scene_->SetUpdateEnabled(false);
            scene_->Clear();
            scene_->Remove();
        }
        
        // Remove all UI elements from UI sub-system
        GetSubsystem<UI>()->GetRoot()->RemoveAllChildren();
    }
    SharedPtr<Scene> scene_;
};
[/code]

Level1.h
[code]
#pragma once

#include <Urho3D/Urho3DAll.h>
#include "BaseLevel.h"

class Level1 : public BaseLevel
{
    URHO3D_OBJECT(Level1, BaseLevel);
    
public:
    /// Construct.
    Level1(Context* context) :
    BaseLevel(context)
    {
        Init();
    }

    virtual ~Level1()
    {
    }

protected:
    virtual void Init()
    {
        BaseLevel::Init();

        // Create the scene content
        CreateScene();
        
        // Create the UI content
        CreateUI();
        
        // Subscribe to global events for camera movement
        SubscribeToEvents();
    }
    
private:
    void CreateScene()
    {
        scene_ = new Scene(context_);
    }
    
    void CreateUI()
    {
    }
    
    void SubscribeToEvents()
    {
    }
};
[/code]

C++
[code]
// Switch level
VariantMap& eventData = GetEventDataMap();
eventData[MyEvents::E_SET_LEVEL] = "Level2";
SendEvent(MyEvents::E_SET_LEVEL, eventData);
[/code]

-------------------------

Lumak | 2017-01-02 01:14:19 UTC | #2

Can't see how cool it is w/o a video. Can you provide one?

-------------------------

artgolf1000 | 2017-01-02 01:14:20 UTC | #3

Yes, here is the video: [url]https://youtu.be/7dM-z8o5Mic[/url]

-------------------------

Lumak | 2017-01-02 01:14:20 UTC | #4

Nice.  Thank you for sharing this.  This will come in handy.

-------------------------

1vanK | 2017-01-02 01:14:20 UTC | #5

Nice!

-------------------------

artgolf1000 | 2018-02-02 03:48:09 UTC | #6

virtual ~BaseLevel()
{
    Dispose();
}

Fixed memory leak.

-------------------------

