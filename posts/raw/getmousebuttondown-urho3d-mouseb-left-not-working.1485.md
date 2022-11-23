simple | 2017-01-02 01:08:06 UTC | #1

Somebody have same problem like me with newest version of urho3d?

If i bind engine's externalWindow with QWidget->winId() (which is parented with QMainWindow) or wxControl->GetHandle() then GetMouseButtonDown(Urho3D::MOUSEB_LEFT) doesnt work.
If I bind engine's externalWindow wirh QMainWindow->winId() then GetMouseButtonDown(Urho3D::MOUSEB_LEFT) works.
Not sure with earlier version of urho3d, but I earlier also use wxWidgets and use wxControl (as child window) then GetMouseButtonDown(Urho3D::MOUSEB_LEFT) works, now not working.
(probably externalWindow with wxFrame->GetHandle() will also work (anyway this not tested))

maybe GetMouseButtonDown(Urho3D::MOUSEB_LEFT) not working with all window childrens, only works with main windows???

-------------------------

cadaver | 2017-01-02 01:08:06 UTC | #2

I recommend to debug inside Urho's Input class: are you getting the SDL mouse event? If yes, is it being discarded because the inputFocus_ flag is false (or some other reason)?

-------------------------

simple | 2017-01-02 01:08:06 UTC | #3

I was debugged app, and i found problem with [b]SDL_WINDOW_INPUT_FOCUS[/b]. 
This flag is always zero.
So urho3d GainFocus and just after LoseFocus because of this line:

[b]        if (inputFocus_ && (flags & SDL_WINDOW_INPUT_FOCUS) == 0)
            LoseFocus();[/b]

So problem was widget was not focused, but [b]QWidget::setFocus(), QWidget::activateWindow(),SetActiveWindow(this->GetHandle()) and wxControl::SetFocus()[/b]
doesnt send window-message [b]WM_ACTIVATE [/b]where [b]SDL_WINDOW_INPUT_FOCUS [/b]is set by [b]SDL_SetKeyboardFocus(data->window);[/b]
I decided send this message maually by this code (is little dirty but work):
[b]SendMessageA((HWND)this->winId(),WM_ACTIVATE,WA_ACTIVE,0);[/b]

-------------------------

cadaver | 2017-01-02 01:08:07 UTC | #4

Thanks for the debugging. It looks like we should perhaps always assume SDL_WINDOW_INPUT_FOCUS for external windows.

-------------------------

