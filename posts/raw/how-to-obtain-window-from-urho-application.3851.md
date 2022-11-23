Elendil | 2017-12-15 15:15:33 UTC | #1

How to obtain window from Urho Application? I need pointer of main window from Urho, I check documentation but I didn't find info about window in Application class. I need it for this kind of function
> bool attach(GLFWwindow *window) {
>      HWINDOW hw = hwnd(window);
>      // ...
>      return true;
>      }

Instead GLFWindow I need Urho3DWindow.

-------------------------

SirNate0 | 2017-12-15 18:17:18 UTC | #2

You can get the window from the [Graphics](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_graphics.html) subsystem, so hopefully one of these will work for you:
```
void* Graphics::GetExternalWindow () const
 	Return OS-specific external window handle. Null if not in use. 
 
SDL_Window* Graphics::GetWindow () const
 	Return SDL window. 
```

-------------------------

Elendil | 2017-12-15 18:50:37 UTC | #3

Thanks, but what window use Urho Application class? I use firstProject tutorial as reference and there is no window creation. I asume this is done automatically by Urho application.

-------------------------

SirNate0 | 2017-12-16 00:43:58 UTC | #4

I'm not certain what you're trying to do, but yes, as long as you don't start the engine in headless mode it will create the window for you behind the scenes (when the Graphics class is created, I'm pretty sure). If you're trying to get it to use a window that already exists you can pass the external window handle as an engine parameter --
 see the documentation [here](https://urho3d.github.io/documentation/HEAD/_main_loop.html) for a list (you want  ExternalWindow, I think).

-------------------------

Elendil | 2017-12-16 10:38:24 UTC | #5

[quote="SirNate0, post:4, topic:3851"]
I’m not certain what you’re trying to do,
[/quote]

I want obtain pointer of main application window from Urho, where is rendering done. I need it for attach to this window Sciter window. I am following GLFW example from Sciter where in example is used this technique with window.
Btw I did something, but I am not sure if it is right:
>     HWINDOW hwnd(SDL_Window *window)
>     {
>     	SDL_SysWMinfo sysInfo;
>     	SDL_VERSION(&sysInfo.version);
>     	SDL_GetWindowWMInfo(window, &sysInfo);
>     	return sysInfo.info.win.window;
>     }
		gr = new Graphics(context_);
		sdlW_ = gr->GetWindow();
		
		if (sciter::attach(sdlW_)) // gr->GetWindow()
		{
			SciterLoadFile(hwnd(sdlW_), L"Data/sciter-glfw-basic-facade.htm");

			// ...
		}

if // if GetSubsystem<Graphics>()->GetWindow();  instead gr->GetWindow(); is used, then mouse is allways visible, even if mouse is hidden with code. And I am not sure if I get really main window wtih GetSubsystem.

-------------------------

SirNate0 | 2017-12-16 17:42:45 UTC | #6

I'm pretty sure you should *not* be doing that (creating a `new Graphics`) - I think doing so requests the GPU twice, and probably tries to create two windows (though I've not looked at the code to see). Whether or not that is okay, the `GetSubsystem<Graphics>->GetWindow()` approach should be correct. I'm not certain what you mean by "main window" - isn't there only one? My guess about your mouse visibility issue is that, assuming you've set it up correctly in Urho, Sciter probably makes the mouse visible on its end, though I can't say for sure...

-------------------------

Elendil | 2017-12-16 21:26:05 UTC | #7

Thanks, I tried lot of things, but without succes. It is too much for me, I never do this kind of things. I'll use internal Urho GUI or try TurboBadger UI.

-------------------------

