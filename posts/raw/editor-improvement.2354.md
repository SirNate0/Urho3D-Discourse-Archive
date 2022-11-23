artgolf1000 | 2017-01-02 01:14:55 UTC | #1

Hi,

If using free UI layout in a certain window, I want to drag UI elements to proper places, so I added the function when GUI interface hides to speed up UI layout design.

Note that you need to check the property of 'Is Enabled' of a UI element before you can drag it.

Here is the modified part of Urho3D/bin/Data/Scripts/Editor/EditorUI.as

[code]
...
IntVector2 dragBeginElementPosition;
IntVector2 dragBeginPosition;
...
void HandleDragBegin(StringHash eventType, VariantMap& eventData)
{
    UIElement@ uiElement = eventData["Element"].GetPtr();
    if (uiElement is null)
        return;

    dragBeginElementPosition = uiElement.position;
    dragBeginPosition = IntVector2(eventData["X"].GetInt(), eventData["Y"].GetInt());
}

void HandleDragMove(StringHash eventType, VariantMap& eventData)
{
    UIElement@ uiElement = eventData["Element"].GetPtr();
    if (uiElement is null)
        return;

    IntVector2 dragCurrentPosition = IntVector2(eventData["X"].GetInt(), eventData["Y"].GetInt());
    uiElement.position = dragBeginElementPosition + (dragCurrentPosition - dragBeginPosition);
}

void HandleDragEnd(StringHash eventType, VariantMap& eventData)
{
    UIElement@ uiElement = eventData["Element"].GetPtr();
    if (uiElement is null)
        return;

    // Do nothing
}

void HideUI(bool hide = true)
{
    if (uiHidden == hide) {
        return;
    }

    if (hide) {
    	SubscribeToEvent("DragBegin", "HandleDragBegin");
    	SubscribeToEvent("DragMove", "HandleDragMove");
    	SubscribeToEvent("DragEnd", "HandleDragEnd");
    } else {
    	UnsubscribeFromEvent("DragBegin");
    	UnsubscribeFromEvent("DragMove");
    	UnsubscribeFromEvent("DragEnd");
    }
    ...
}
[/code]

-------------------------

