ab4daa | 2019-07-10 13:48:01 UTC | #1

I tested E_CLICK and E_CLICKEND events with the dragg-able fish in HelloGUI sample.

	SubscribeToEvent(draggableFish, E_CLICK, URHO3D_HANDLER(HelloGUI, HandleclickEnd));
Works fine.

But once I change the dragg-able fish from Button to BorderImage.
The events will no longer fire. 

Is this an intentional behavior?
Thanks

-------------------------

Leith | 2019-07-10 14:27:04 UTC | #2

I am no master of Urho 2D UI stuff - but I don't think BorderImage was intended to be interactive - most of the other UI classes derive from it, just because it can "draw something". This does not imply that it's an interactive base class.

-------------------------

ab4daa | 2019-07-10 14:39:11 UTC | #3

Probably.
I just don't know what makes Button sends the events but BorderImage.
The events are sent in a generic UI function and looks like apply to all UIelements.

For now I think a Button without hover and press offset may be OK.

-------------------------

Virgo | 2019-07-10 16:44:32 UTC | #4

Button inherits BorderImage which inherits UIElement.
But latter one doesn't implement UIElement::OnKey() , so yes, it's intentional.



[Button::OnKey();](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/UI/Button.cpp#L149)

    void Button::OnKey(Key key, MouseButtonFlags buttons, QualifierFlags qualifiers)
    {
        if (HasFocus() && (key == KEY_RETURN || key == KEY_RETURN2 || key == KEY_KP_ENTER || key == KEY_SPACE))
        {
            // Simulate LMB click
            OnClickBegin(IntVector2(), IntVector2(), MOUSEB_LEFT, 0, 0, nullptr);
            OnClickEnd(IntVector2(), IntVector2(), MOUSEB_LEFT, 0, 0, nullptr, nullptr);
        }
    }

-------------------------

Virgo | 2019-07-11 08:02:19 UTC | #5

:smiley:PS: OnClickBegin() and OnClickEnd() are Button members, they send the click events.

EDIT: **they actually fire press events**, not click ones.
sry for the misleading answer

-------------------------

ab4daa | 2019-07-11 00:33:39 UTC | #6

The events in Button::OnClickBegin() and Button::OnClickEnd() are E_PRESSED and E_RELEASED.
They can be used as clicked events, but my initial purpose is to handle click on a BorderImage.

When clicking on a BorderImage, in UI::ProcessClickBegin() the 

	WeakPtr<UIElement> element(GetElementAt(windowCursorPos, true, &cursorPos));

is NULL, but it is not NULL if click on a Button.(Don't know why)

The element variable is then passed to UI::SendClickEvent(), cause E_CLICK event fire or not.

-------------------------

Virgo | 2019-07-11 07:40:22 UTC | #7

haha i didnt check the events names, sry for the wrong answer.
checking urho3d ui sources, there are comments on GetElementAt() functions saying
`By default returns only input-enabled elements.`
im still trying to find out where they wrote those codes checking if the element is input-enabled or not
:hugs:

-------------------------

Virgo | 2019-07-11 11:12:44 UTC | #8

I think i found it, UI::GetElementAt() checks result elements' enable state, but by default BorderImage's `Is Enabled` attribute is `fales`
i suggest you try to set it true for your BorderImage and see if it fires the click events

-------------------------

Leith | 2019-07-11 09:17:46 UTC | #9

I don't think BorderImage subscribes to receive click events, and correspondingly, I believe has no methods to sink them... this component simply does not care to receive input events, so it can't respond to them.

-------------------------

Virgo | 2019-07-11 10:15:09 UTC | #10

hey Leith!
i just checked source, click events are sent in `UI::SendClickEvent()`


    void UI::SendClickEvent(StringHash eventType, UIElement* beginElement, UIElement* endElement, const IntVector2& pos, MouseButton button,
        MouseButtonFlags buttons, QualifierFlags qualifiers)
    {
        VariantMap& eventData = GetEventDataMap();
        eventData[UIMouseClick::P_ELEMENT] = endElement;
        eventData[UIMouseClick::P_X] = pos.x_;
        eventData[UIMouseClick::P_Y] = pos.y_;
        eventData[UIMouseClick::P_BUTTON] = button;
        eventData[UIMouseClick::P_BUTTONS] = (unsigned)buttons;
        eventData[UIMouseClick::P_QUALIFIERS] = (unsigned)qualifiers;

        // For click end events, send also the element the click began on
        if (eventType == E_UIMOUSECLICKEND)
            eventData[UIMouseClickEnd::P_BEGINELEMENT] = beginElement;

        if (endElement)
        {
            // Send also element version of the event
            if (eventType == E_UIMOUSECLICK)
                endElement->SendEvent(E_CLICK, eventData);
            else if (eventType == E_UIMOUSECLICKEND)
                endElement->SendEvent(E_CLICKEND, eventData);
        }

        // Send the global event from the UI subsystem last
        SendEvent(eventType, eventData);
    }

in the caller functions the `endElement` argument is obtained through `UI::GetElementAt()`
so if we want click event from BorderImage, we just need to make them to be considered "input-enabled", which i suppose its determined the "Is Enabled" attribute.
:smiley: i finally gotcha?

-------------------------

Leith | 2019-07-11 10:55:16 UTC | #11

The receiver, BorderImage, wont receive it, because it never subscribed to the event
Urho uses a listener pattern - listeners can subscribe to receive events, either from a specific sender, or from anywhere - if we dont subscribe, we are not notified

-------------------------

ab4daa | 2019-07-11 11:14:03 UTC | #12

You are right.
Thanks for nice explanation :+1:

Never noticed that it is default disabled.

-------------------------

Virgo | 2019-07-11 11:17:07 UTC | #13

:innocent: bro i think you got something wrong, there is no receiver here, `endElement->SendEvent()` called here is actually [`Urho3D::Object::SendEvent()`](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Core/Object.cpp#L297) that sends the event (just a guess, there is way too much source code to read, i gave up).

-------------------------

Modanung | 2019-07-11 11:27:14 UTC | #14

At the risk of being only slightly off-topic...
Doesn't this ask for a seperate `OnKeyDown()` and `OnKeyUp()`?
[quote="Virgo, post:4, topic:5292"]
```
void Button::OnKey(Key key, MouseButtonFlags buttons, QualifierFlags qualifiers)
{
    if (HasFocus() && (key == KEY_RETURN || key == KEY_RETURN2 || key == KEY_KP_ENTER || key == KEY_SPACE))
    {
        // Simulate LMB click
        OnClickBegin(IntVector2(), IntVector2(), MOUSEB_LEFT, 0, 0, nullptr);
        OnClickEnd(IntVector2(), IntVector2(), MOUSEB_LEFT, 0, 0, nullptr, nullptr);
    }
}
```
[/quote]

-------------------------

Leith | 2019-07-11 11:32:42 UTC | #15

Urho eventing is very flexible. I did not say anything was not possible, but I did give hints about how eventing works.

-------------------------

Virgo | 2019-07-11 11:35:17 UTC | #16

:rofl: checked source code, i dont understand it either

-------------------------

Modanung | 2019-07-11 11:51:27 UTC | #17

I suspect the current implementation to be somewhat of a shortcut. Introducing separate down and up functions would introduce more complexity then one might initially think.

-------------------------

