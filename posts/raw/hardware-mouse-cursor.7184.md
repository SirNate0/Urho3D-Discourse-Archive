JTippetts1 | 2022-02-04 15:42:52 UTC | #1

Something that has been bothering me for awhile is obtaining smooth, responsive mouse motion with custom UI::Cursors. Whenever I use the UI cursor (Input::SetMouseVisible(false)) the cursor moves with a great deal of lag due to being locked to the game render cycle, and while it gets worse at lower framerates, even at high framerates it is still noticeable. However, SetMouseVisible(true) just shows the standard system cursor, and not the Cool(TM) game-specific colored cursor I want to show.

Now, I understand that SDL does allow specifying an image for the system cursor via SDL_CreateColorCursor, and looking at the code for UI::Cursor it appears that it is doing so, but it still seems to be rendering the cursor on the render cycle and not at the system level. Is there something else or something different that I need to be doing in order to get a fast, responsive, system-level custom cursor? Do I need to do an end run around UI and go to SDL directly, or am I just missing something?

-------------------------

Lys0gen | 2022-02-04 19:09:08 UTC | #2

What system are you on and how are you setting it?

I just tried it with the code below on Win7 and made my update loop very laggy but the cursor is just as smooth as the default HW cursor. Will try it on Debian later.


    Urho3D::UI* appUI = GetSubsystem<Urho3D::UI>();
    SharedPtr<Urho3D::Cursor> cursor(new Urho3D::Cursor(context_));
    cursor->SetStyleAuto();
    appUI->SetCursor(cursor);

-------------------------

JTippetts1 | 2022-02-04 22:37:12 UTC | #3

Yeah, that's exactly what I do. On Win10, MinGW build, OpenGL renderer. If I push my draw distance out far enough, then when the framerate drops the cursor becomes extremely laggy. Switching mouse visible to true, the system cursor operates smoothly as normal even at single-digit FPS, but the UI cursor just lags and lags and it feels bad.

-------------------------

Lys0gen | 2022-02-05 04:26:17 UTC | #4

Just in case: When did you last update Urho? Until I patched mine a few months ago I had a bunch of issues with SDL related stuff as well (windowed fullscreen didn't work & the app force disabled the windows aero UI for some reason, didn't check the cursor back then though...).

-------------------------

