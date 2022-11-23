gawag | 2017-01-02 01:10:54 UTC | #1

The mouse cursor behavior gets kinda ridiculous when having set a shape (not using the OS default). Basically I just want to be able to toggle between "mouse cursor mode" and "camera/movement mode" like many games do.

[code]
SharedPtr<Cursor> cursor;
...
// starting phase
XMLFile* style = cache->GetResource<XMLFile>("UI/DefaultStyle.xml");
UI* ui=GetSubsystem<UI>();
ui->GetRoot()->SetDefaultStyle(style);
cursor=new Cursor(context_);
cursor->SetStyleAuto(style);
ui->SetCursor(cursor);
GetSubsystem<Input>()->SetMouseVisible(true);
...
// in my toggle function
GetSubsystem<Input>()->SetMouseGrabbed(!GetSubsystem<Input>()->IsMouseGrabbed());  // toggle grabbing of mouse
GetSubsystem<Input>()->SetMouseVisible(!GetSubsystem<Input>()->IsMouseVisible());       // ignore mouse cursor (the cursor is still visible but weird when having set a cursor)
if(GetSubsystem<UI>()->GetCursor())                                                                               // toggle the set cursor to 0 to have the default OS cursor again, which is hidden via SetMouseVisible
    GetSubsystem<UI>()->SetCursor(0);
else
    GetSubsystem<UI>()->SetCursor(cursor);
[/code]
Maybe I'm missing something but such a mode switch shouldn't be that complicated and hard to do as it currently is.
What about a ui->SetCursorActive(bool) that does basically ui->SetCursor(0) and Input->SetMouseVisible(false) in the false case or SetCursor(last_cursor) and Input->SetMouseVisible(true) in the true case?
There could be also ui->EnableCursor() and ui->DisableCursor().
Am I doing it right and is this intended to be like this?

Urho version is the newest from GitHub and 1.5 behaves the same.

-------------------------

hdunderscore | 2017-01-02 01:10:54 UTC | #2

The easy way is to use Input->SetMouseMode(MM_ABSOLUTE) for your UI mode, and Input->SetMouseMode(MM_RELATIVE) for your FPS mode, or sim ply toggling UI cursor visiblity.

-------------------------

gawag | 2017-01-02 01:10:54 UTC | #3

[quote="hd_"]The easy way is to use Input->SetMouseMode(MM_ABSOLUTE) for your UI mode, and Input->SetMouseMode(MM_RELATIVE) for your FPS mode, or sim ply toggling UI cursor visiblity.[/quote]
Just toggling visibility doesn't help because when the cursor is set, it is still drawn even when the OS cursor is invisible.

With SetMouseMode I could change my toggle function to:
[code]
if(GetSubsystem<Input>()->GetMouseMode()==MM_RELATIVE)
{
    GetSubsystem<Input>()->SetMouseMode(MM_ABSOLUTE);
    GetSubsystem<UI>()->SetCursor(cursor);
}
else
{
    GetSubsystem<Input>()->SetMouseMode(MM_RELATIVE);
    GetSubsystem<UI>()->SetCursor(0);
}
[/code]
The SetCursor is still weird but it is required. This is a bit better though, but the Cursor being always visible when set to non-OS, via SetCursor, is still odd.

-------------------------

weitjong | 2017-01-02 01:10:55 UTC | #4

I think hd_ is correct. The cursor is just like any UI-element, so setting the cursor visibility to false should hide the cursor without calling SetCursor(0). Also take note that like OS cursor, the software-rendered cursor will also attempt to return back to its so-called normal shape.

-------------------------

gawag | 2017-01-02 01:10:55 UTC | #5

[quote="weitjong"]I think hd_ is correct. The cursor is just like any UI-element, so setting the cursor visibility to false should hide the cursor without calling SetCursor(0). Also take note that like OS cursor, the software-rendered cursor will also attempt to return back to its so-called normal shape.[/quote]

Oh! I didn't see that it's a UIElement and has a SetVisible(bool). I thought the only "sane looking option" was input->SetMouseVisible(bool).
No Idea how I missed that.  :blush: 
Now a switch function could look like:
[code]
if(GetSubsystem<Input>()->GetMouseMode()==MM_RELATIVE)
{
    GetSubsystem<Input>()->SetMouseMode(MM_ABSOLUTE);
    cursor->SetVisible(true);
}
else
{
    GetSubsystem<Input>()->SetMouseMode(MM_RELATIVE);
    cursor->SetVisible(false);
}
[/code]
That looks decent.

-------------------------

