thebluefish | 2017-01-02 01:06:29 UTC | #1

I'm having an odd issue with ExternalWindow. I'm working with wxWidgets + Urho3D using a custom wxPanel to provide a HWND that I sent to Urho3D. It renders perfectly, but I seem to get no input. In fact, only SDL_WINDOWEVENT gets fired.

Thinking that this was some input handling issue, I attempted to manually process events as so:
[code]
void wxUrho3D::OnKeyUp(wxKeyEvent& event)
	{
		SDL_Event sdlEvent;
		sdlEvent.type = SDL_KEYUP;
		sdlEvent.key.keysym.sym = event.GetKeyCode();
		sdlEvent.key.keysym.mod = event.GetModifiers();
		SDL_PushEvent(&sdlEvent);
	}

	void wxUrho3D::OnKeyDown(wxKeyEvent& event)
	{
		SDL_Event sdlEvent;
		sdlEvent.type = SDL_KEYDOWN;
		sdlEvent.key.keysym.sym = event.GetKeyCode();
		sdlEvent.key.keysym.mod = event.GetModifiers();
		SDL_PushEvent(&sdlEvent);
	}

	void wxUrho3D::OnMouseUp(wxMouseEvent& event)
	{
		SDL_Event sdlEvent;
		sdlEvent.type = SDL_MOUSEBUTTONUP;
		sdlEvent.button.state = SDL_RELEASED;
		sdlEvent.button.button = SDL_BUTTON_LEFT;

		auto position = event.GetPosition();
		sdlEvent.button.x = position.x;
		sdlEvent.button.y = position.y;

		SDL_PushEvent(&sdlEvent);
	}

	void wxUrho3D::OnMouseDown(wxMouseEvent& event)
	{
		SDL_Event sdlEvent;
		sdlEvent.type = SDL_MOUSEBUTTONDOWN;
		sdlEvent.button.state = SDL_PRESSED;
		sdlEvent.button.button = SDL_BUTTON_LEFT;

		auto position = event.GetPosition();
		sdlEvent.button.x = position.x;
		sdlEvent.button.y = position.y;

		SDL_PushEvent(&sdlEvent);
	}
[/code]

These functions *are* firing correctly, however Urho3D doesn't seem to be processing the SDL events. Any ideas on what's going on?

-------------------------

thebluefish | 2017-01-02 01:06:29 UTC | #2

Thanks for the bit on 'inputFocus_', that led me to what I was looking for!

So I changed the following in Input.cpp:
[code]
if (inputFocus_ && (flags & SDL_WINDOW_INPUT_FOCUS) == 0 && inputFocus_ && (flags & SDL_WINDOW_MOUSE_FOCUS) == 0)
            LoseFocus();
[/code]

However I don't know if there's any downside to this approach. It seems that using a wxWidgets panel as an external window, the window doesn't have SDL_WINDOW_INPUT_FOCUS but *does* have SDL_WINDOW_MOUSE_FOCUS.

-------------------------

thebluefish | 2017-01-02 01:06:30 UTC | #3

There was still the issue of "gaining" focus. That is, the first event causing focus (tab, mouse click) will give the window focus but not register as input. I'm playing around with a forceFocus_ flag, which Input automatically sets when there's an external handle. So far, it seems to work find for all cases I've tested. However right now my Linux install is jacked and I don't have a Mac, so who knows if it will work properly across all platforms.

-------------------------

