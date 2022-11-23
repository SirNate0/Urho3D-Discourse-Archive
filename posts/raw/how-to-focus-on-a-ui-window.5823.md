evolgames | 2020-01-19 15:29:59 UTC | #1

HI, I have several UI windows that I'm using for settings adjustments.
Everything is working well and the documentation is easy to apply.

However, I'm not able to figure out how to focus on and bring a window to the front via code. I'm using Lua. When I click on the window, it focuses automatically. But I can't figure out how to push this with a line of code. The way I set up the windows, they are all created and visibility is being toggled. So, the user clicks "Settings" and the settings window toggles visibility. I want to put a line in there that focuses the window to the front (so it isn't behind the others) when it is made visible.

I have tried these:
```
ui.focusElement=nil
ui:SetFocusElement(masswindow, true)
masswindow:SetFocus(true)
masswindow:SetBringToFront(true)
```
to no avail. I must be missing something. I suppose I could destroy and recreate windows each time they were made visible, but that sounds really unnecessary.

What can I do for this? I even thought about faking the mouse click on the window...

-------------------------

Modanung | 2020-01-18 23:32:28 UTC | #2

Have you tried `ui.SetFocusElement(masswindow, false)`?

-------------------------

evolgames | 2020-01-18 23:37:31 UTC | #3

Yeah that doesn't work either unfortunately.

-------------------------

1vanK | 2020-01-19 15:29:52 UTC | #4

Samples\37_UIDrag\UIDrag.cpp

```
void UIDrag::CreateGUI()
{
    ...
        // Enable the bring-to-front flag and set the initial priority
        b->SetBringToFront(true);
        b->SetPriority(i);
```

-------------------------

evolgames | 2020-01-19 14:27:05 UTC | #5

That worked, thanks! Didn't need the bring to front part.
I'm doing mine in Lua. Strangely the lua example doesn't have those lines of code about priority.

For anyone wondering, nothing I've listed worked except changing the priority.

```
masswindow:SetVisible(not masswindow:IsVisible())
masswindow:SetPriority(1)
```

This works just fine. I'm assuming from here that I just cycle the priority placing. I could make a simple loop that pushes every other window (about 6) back by one for their priority. I wonder why this isn't in the lua 37_UIDrag...

Anyways, this is what I looking for, thanks again.

-------------------------

