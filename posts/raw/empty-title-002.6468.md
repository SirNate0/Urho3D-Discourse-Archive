vram32 | 2020-12-11 13:10:44 UTC | #1

Empty content.......

-------------------------

vmost | 2020-12-11 13:10:50 UTC | #3

Check out `SetCursor()` code, it removes old cursor when setting to null.

```
void UI::SetCursor(Cursor* cursor)
{
    if (cursor_ == cursor)
        return;

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

-------------------------

Modanung | 2020-10-29 17:22:17 UTC | #5

Better use `nullptr`.
https://stackoverflow.com/a/20509811/3618748

> _"If you have to name the null pointer, call it nullptr; that's what it's called in C++11. Then, "nullptr" will be a keyword."_ -- [**Bjarne Stroustrup**](https://en.wikipedia.org/wiki/Bjarne_Stroustrup)

-------------------------

Modanung | 2020-10-29 17:41:37 UTC | #7

It's my favourite return value. :slightly_smiling_face:

-------------------------

