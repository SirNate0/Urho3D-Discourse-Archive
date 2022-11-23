artgolf1000 | 2017-01-02 01:15:49 UTC | #1

Hi,

I wrote this when I started to learn Urho3D, you may like it:)

If you have a UI control, such as a button or something else, you can add behaviors to it by UI toys, like click, drag, zoom, and whatever behaviors you can imagine.

In this way, you can create your own common behavior library to reuse later.

C++
[code]BaseUIToy* toy;
Button* button = GetSubsystem<UI>()->GetRoot()->GetChildStaticCast<Button>(String("Button"), true);
toy = new MyClickBegin(context_);
button->AddChild(toy);
toy->Start();
toy = new MyDrag(context_);
button->AddChild(toy);
toy->Start();
toy = new MyZoom(context_);
button->AddChild(toy);
toy->Start();
[/code]

BaseUIToy.h
[code]#pragma once

#include <Urho3D/Urho3DAll.h>

/// Custom logic component for UI element.
class BaseUIToy : public UIElement
{
    URHO3D_OBJECT(BaseUIToy, UIElement);
    
public:
    /// Construct.
    BaseUIToy(Context* context) :
    UIElement(context)
    {
        SetFixedSize(0, 0);
    }
    ~BaseUIToy()
    {
        Stop();
    }
    virtual void Start() = 0;
    virtual void Stop() {}
};
[/code]

MyClick.h
[code]#pragma once

#include <Urho3D/Urho3DAll.h>
#include "BaseUIToy.h"

/// Custom logic component for rotating a scene node.
class MyClick : public BaseUIToy
{
    URHO3D_OBJECT(MyClick, BaseUIToy);
    
public:
    /// Construct.
    MyClick(Context* context) :
    BaseUIToy(context)
    {
    }
    
    /// Called when the component is added to a scene node. Other components may not yet exist.
    virtual void Start()
    {
        if (parent_) {
            Button* button = static_cast<Button*>(parent_);
            // Subscribe to button release (following a 'press') events
            SubscribeToEvent(button, E_RELEASED, URHO3D_HANDLER(MyClick, HandleButtonPressed));
        }
    }
    
    /// Called when the component is detached from a scene node, usually on destruction. Note that you will no longer have access to the node and scene at that point.
    virtual void Stop()
    {
        // Remove all events
        UnsubscribeFromAllEvents();
    }
    
    virtual void HandleButtonPressed(StringHash eventType, VariantMap& eventData) = 0;

private:
};
[/code]

MyClickBegin.h
[code]#pragma once

#include <Urho3D/Urho3DAll.h>
#include "MyClick.h"

/// Custom logic component for rotating a scene node.
class MyClickBegin : public MyClick
{
    URHO3D_OBJECT(MyClickBegin, MyClick);
    
public:
    /// Construct.
    MyClickBegin(Context* context) :
    MyClick(context)
    {
    }
    
    void HandleButtonPressed(StringHash eventType, VariantMap& eventData)
    {
        // Do something here
    }

private:
};
[/code]

MyDrag.h
[code]#pragma once

#include <Urho3D/Urho3DAll.h>
#include "BaseUIToy.h"

/// Custom logic component for rotating a scene node.
class MyDrag : public BaseUIToy
{
    URHO3D_OBJECT(MyDrag, BaseUIToy);
    
public:
    /// Construct.
    MyDrag(Context* context) :
    BaseUIToy(context)
    {
    }
    
    /// Called when the component is added to a scene node. Other components may not yet exist.
    virtual void Start()
    {
        if (parent_) {
            UIElement* element = static_cast<UIElement*>(parent_);
            SubscribeToEvent(element, E_DRAGBEGIN, URHO3D_HANDLER(MyDrag, HandleDragBegin));
            SubscribeToEvent(element, E_DRAGMOVE, URHO3D_HANDLER(MyDrag, HandleDragMove));
            SubscribeToEvent(element, E_DRAGEND, URHO3D_HANDLER(MyDrag, HandleDragEnd));
        }
    }
    
    /// Called when the component is detached from a scene node, usually on destruction. Note that you will no longer have access to the node and scene at that point.
    virtual void Stop()
    {
        // Remove all events
        UnsubscribeFromAllEvents();
    }
    
    void HandleDragBegin(StringHash eventType, VariantMap& eventData)
    {
        // Get UIElement relative position where input (touch or click) occurred (top-left = IntVector2(0,0))
        UIElement* draggedElement = static_cast<UIElement*>(eventData["Element"].GetPtr());
        dragBeginElementPosition_ = draggedElement->GetPosition();
        dragBeginPosition_ = IntVector2(eventData["X"].GetInt(), eventData["Y"].GetInt());
    }
    
    void HandleDragMove(StringHash eventType, VariantMap& eventData)
    {
        IntVector2 dragCurrentPosition = IntVector2(eventData["X"].GetInt(), eventData["Y"].GetInt());
        UIElement* draggedElement = static_cast<UIElement*>(eventData["Element"].GetPtr());
        draggedElement->SetPosition(dragBeginElementPosition_ + (dragCurrentPosition - dragBeginPosition_));
    }
    
    void HandleDragEnd(StringHash eventType, VariantMap& eventData)
    {
    }

private:
    /// Remembered drag begin position.
    IntVector2 dragBeginElementPosition_;
    IntVector2 dragBeginPosition_;
};
[/code]

MyZoom.h
[code]#pragma once

#include <Urho3D/Urho3DAll.h>
#include "BaseUIToy.h"

/// Custom logic component for rotating a scene node.
class MyZoom : public BaseUIToy
{
    URHO3D_OBJECT(MyZoom, BaseUIToy);
    
public:
    /// Construct.
    MyZoom(Context* context) :
    BaseUIToy(context)
    {
    }
    
    /// Called when the component is added to a scene node. Other components may not yet exist.
    virtual void Start()
    {
        counter = 0;
        increasing = true;

        // Subscribe HandleUpdate() function for processing update events
        SubscribeToEvent(E_UPDATE, URHO3D_HANDLER(MyZoom, HandleUpdate));
    }
    
    /// Called when the component is detached from a scene node, usually on destruction. Note that you will no longer have access to the node and scene at that point.
    virtual void Stop()
    {
        // Remove all events
        UnsubscribeFromAllEvents();
    }
    
    /// Handle the logic update event.
    void HandleUpdate(StringHash eventType, VariantMap& eventData)
    {
        if (parent_) {
            UIElement* element = parent_;
            element->SetSize(48 + counter, 48 + counter);
            
            if (increasing) {
                counter++;
            } else {
                counter--;
            }
            if (counter % 16 == 0) {
                increasing = !increasing;
            }
        }
    }
    
private:
    int counter;
    bool increasing;
};
[/code]

-------------------------

sabotage3d | 2017-01-02 01:15:50 UTC | #2

Thanks. That would be really useful for mobile.

-------------------------

