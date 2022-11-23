rogerdv | 2017-01-02 01:01:07 UTC | #1

Im trying to make the mouse cursor visible, studied the demos, but seems that I missed something. 
I tried this:

[code]Cursor* cursor = GetSubsystem<UI>()->GetCursor();
		 cursor->SetVisible(true);
[/code]

but seems that second line is not conrrect, because it causes a segfault. Whats the correct way to make cursor visible?

-------------------------

cadaver | 2017-01-02 01:01:07 UTC | #2

That is valid only if a cursor UI element (which is separate from the OS cursor) has actually been set by the application. You should be able to avoid the crash by nullchecking. 

Controlling the OS mouse cursor visibility happens through the Input subsystem -> Input::SetMouseVisible().

-------------------------

