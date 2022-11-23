Sasha7b9o | 2017-01-02 01:07:29 UTC | #1

Hi. Need for capture a mouse and own cursor.
I do so:
[code]    gInput->SetMouseMode(MM_RELATIVE);
    style = gCache->GetResource<XMLFile>("UI/DefaultStyle.xml");
    SharedPtr<Cursor> cursor(new Cursor(gContext));
    cursor->SetStyleAuto(style);
    gUI->SetCursor(cursor);[/code]
However thus the interface Urho doesn't react to the cursor.
Please help. Thanks.

-------------------------

jmiller | 2017-01-02 01:07:30 UTC | #2

Hi, and welcome to the forum. :slight_smile:

The mouse cursor and UI can be a little confusing at first.
In case you have not seen this documentation section, it should help:
[urho3d.github.io/documentation/HEAD/_input.html](http://urho3d.github.io/documentation/HEAD/_input.html)

I use MM_RELATIVE when I do not want to interact with the UI.
When I want to handle UI:
GetSubsystem<Input>()->SetMouseMode(MM_ABSOLUTE);
MM_ABSOLUTE also makes the UI cursor visible, as if you did this:
GetSubsystem<UI>()->GetCursor()->SetVisible(true);

There is also UI::GetCursorPosition() as well as Input::GetMousePosition().

HTH?

-------------------------

Sasha7b9o | 2017-01-02 01:07:30 UTC | #3

Thanks for the help, but, unfortunately, it a little than will help me.
It is necessary for me that the cursor didn't go beyond a window and I interacted with the interface.
To documentation it is written about MM_RELATIVE: 
> When the virtual cursor is also invisible, UI interaction will still function as normal.

however any interaction it isn't observed even at the visible cursor.

-------------------------

Sasha7b9o | 2017-01-02 01:07:30 UTC | #4

??, the problem is solved.
By some improbable tragic accident in a code the line gInput->SetMouseVisible (true) crept in.
The example "SceneReplication" helped to understand. Everything is very simple:
[code]XMLFile *styleCursor = gCache->GetResource<XMLFile>("UI/DefaultStyle.xml");
    SharedPtr<Cursor> cursor(new Cursor(gContext));
    cursor->SetStyleAuto(styleCursor);
    gUI->SetCursor(cursor);[/code]
All thanks

-------------------------

