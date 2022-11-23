Taqer | 2019-09-15 11:14:17 UTC | #1

Hi, I have a problems with switching multiple cursors in game.

When I change cursor, it flickers for a moment with default OS cursor, it's a small thing but I want to remove it.

I have 6 cursors graphics, defined in style .xml file, and a method to change cursors:

    void GameMode::ChangeCursor(GameCursorType type)
    {
    	if (currentCursorType == type) return;
    	currentCursorType = type;

    	//this will crash \/ \/ \/
    	//UI* ui = GetSubsystem<UI>();
    	//Cursor * cursor = ui->GetCursor();
    	//cursor->SetShape(cursorNames[type]);
    	//ui->SetCursor(cursor);

    	//this will flicker cursor \/ \/ \/
    	UI* ui = GetSubsystem<UI>();
    	SharedPtr<Cursor> cursor = SharedPtr<Cursor>(new Cursor(context_));
    	cursor->SetStyleAuto(ui->GetRoot()->GetDefaultStyle());
    	cursor->SetShape(cursorNames[type]);
    	ui->SetCursor(cursor);
    }

I tried to change cursor at the end of the frame but that didn't help.

-------------------------

Modanung | 2019-09-15 16:34:27 UTC | #2

Have you tried the first method without the last call to `SetCursor`?

It might be an unexpected/unhandled situation and should be unnecessary in this case. I believe `SetCursor` may remove the only counted reference of the cursor you're holding a pointer to. If so, the function could use an `if (cursor == cursor_) return;` at the beginning.

[details=UI::SetCursor]
```
void UI::SetCursor(Cursor* cursor)
{
    // Remove old cursor (if any) and set new
    if (cursor_)
    {
        rootElement_->RemoveChild(cursor_);
        cursor_.Reset();
    }
    if (cursor)
    {
        rootElement_->AddChild(cursor);
        cursor_ = cursor;

        IntVector2 pos = cursor_->GetPosition();
        const IntVector2& rootSize = rootElement_->GetSize();
        const IntVector2& rootPos = rootElement_->GetPosition();
        pos.x_ = Clamp(pos.x_, rootPos.x_, rootPos.x_ + rootSize.x_ - 1);
        pos.y_ = Clamp(pos.y_, rootPos.y_, rootPos.y_ + rootSize.y_ - 1);
        cursor_->SetPosition(pos);
    }
}
```
[/details]

-------------------------

Modanung | 2019-09-15 16:09:54 UTC | #3

Indeed this causes a segmentation fault:
[spoiler]
```
UI* ui{ GetSubsystem<UI>() };
ui->SetCursor(new Cursor(context_));
```
[/spoiler]
**`ui->SetCursor(ui->GetCursor());`**

-------------------------

Taqer | 2019-09-15 16:37:01 UTC | #4

Works, thanks :slightly_smiling_face:
Also its important to first set cursor in UI.

-------------------------

Modanung | 2019-09-15 17:55:24 UTC | #5

Nice!

PR made:
https://github.com/urho3d/Urho3D/pull/2505

-------------------------

