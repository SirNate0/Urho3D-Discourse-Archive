1vanK | 2017-12-12 17:39:20 UTC | #1

I have 3D-scene and UI-buttons over it. When user toch button,any other actions should not be doing

I try
```
void BoardLogic::HandleTouchBegin(StringHash eventType, VariantMap& eventData)
{
    using namespace TouchBegin;
    IntVector2 screenPos = IntVector2(eventData[P_X].GetInt(), eventData[P_Y].GetInt());
    int touchID = eventData[P_TOUCHID].GetInt();

    // UI-element touched
    if (INPUT->GetTouch(touchID)->touchedElement_)
        return;

    // Interaction with scene objects
}
```
but it does not work. Any tips?

-------------------------

Modanung | 2017-12-12 18:56:06 UTC | #2

`GetSubsystem<UI>()->GetElementAt(screenPos, true)`?

-------------------------

1vanK | 2017-12-12 18:54:45 UTC | #3

[quote="Modanung, post:2, topic:3838, full:true"]
GetSubsystem&lt;UI&gt;()-&gt;GetElementAt(screenPos, true)
[/quote]

Ah thanks, I absolutely forgot this method, although I used it before

-------------------------

