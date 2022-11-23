ucupumar | 2017-01-02 01:00:12 UTC | #1

I can't set mouse position because SetMousePosition() is private function. 
How to get around this?

-------------------------

cadaver | 2017-01-02 01:00:12 UTC | #2

When the OS mouse cursor is hidden, it's being constantly centered to the window to allow unlimited move. This is an internal mechanism in which Input's SetMousePosition() is used.
When the OS mouse cursor is visible, there is indeed no public function to move it. Generally it would be obnoxious to the user if the OS cursor moved against the user's control.
However, this is different from the UI mouse cursor element, which you are allowed to move as you wish.

What is your use case? Do you have the OS cursor hidden or visible? In case you really need to move the actual OS cursor, you can use SDL functions. Input::SetMousePosition does

[code]
    SDL_WarpMouseInWindow(graphics_->GetImpl()->GetWindow(), position.x_, position.y_);
[/code]

-------------------------

ucupumar | 2017-01-02 01:00:18 UTC | #3

Sorry for late response.
I want to move cursor on my main menu because it always started on center of the screen. I want to move it to side of the screen.

I tried SDL_WarpMouseInWindow() but it gives me error:
[code]C:\Program Files (x86)\Urho3D\include\OpenGL\OGLGraphicsImpl.h:36: error: glew.h: No such file or directory
 #include <glew.h>
                  ^[/code]
And I tried another way by move UI cursor using this code:
[code]UI_ = context_->GetSubsystem<UI>();
Cursor* mouseCursor = UI_->GetCursor();
mouseCursor->SetPosition(1,1);[/code]But function GetCursor() always returns null pointer. It seems cursor object on UI is never created in the first place.

Do you know something about this?

-------------------------

scorvi | 2017-01-02 01:00:18 UTC | #4

[quote="ucupumar"]Sorry for late response.
I want to move cursor on my main menu because it always started on center of the screen. I want to move it to side of the screen.

I tried SDL_WarpMouseInWindow() but it gives me error:
[code]C:\Program Files (x86)\Urho3D\include\OpenGL\OGLGraphicsImpl.h:36: error: glew.h: No such file or directory
 #include <glew.h>
                  ^[/code]
And I tried another way by move UI cursor using this code:
[code]UI_ = context_->GetSubsystem<UI>();
Cursor* mouseCursor = UI_->GetCursor();
mouseCursor->SetPosition(1,1);[/code]But function GetCursor() always returns null pointer. It seems cursor object on UI is never created in the first place.

Do you know something about this?[/quote]

hey 

you have to create the cursor first. 
[code] // Create a Cursor UI element because we want to be able to hide and show it at will. When hidden, the mouse cursor will
// control the camera, and when visible, it will point the raycast target
XMLFile* style = cache->GetResource<XMLFile>("UI/DefaultStyle.xml");
SharedPtr<Cursor> cursor(new Cursor(context_));
cursor->SetStyleAuto(style);
ui->SetCursor(cursor);[/code]

and then can you set the position.

-------------------------

ucupumar | 2017-01-02 01:00:18 UTC | #5

Sorry, my bad. But I still can't move mouse position. What's really happen?
Is UI cursor should be activated first or something?

-------------------------

ucupumar | 2017-01-02 01:00:20 UTC | #6

Oh, I knew the problem. UI cursor can't be moved if I set input_->SetMouseVisible(true).
If I only use UI cursor, cursor_->SetPosition(x, y) will works!  :astonished:

-------------------------

weitjong | 2017-01-02 01:00:20 UTC | #7

These are two separate entities while they may look the same. One is the OS provided system cursor,  while the other is Urho UI rendered software cursor image. They are mutually exclusive. Showing OS system cursor will suppress the rendering of soft-cursor,  so setting its position appears to be not working.

-------------------------

