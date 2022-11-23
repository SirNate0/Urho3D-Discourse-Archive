Elendil | 2019-09-11 13:47:28 UTC | #1

It is possible create window and add it as child in main urho3d window?

From documentation Urho have SDL as windowing system if I am right, therefore I need use SDL directly or it is possible do it with Urho?

-------------------------

Elendil | 2019-09-11 16:56:20 UTC | #2

I did something but it is not working (windows is not visible or shown)

    // inside virtual void Start()
    		SDL_Window * sdlw = context_->GetSubsystem<Graphics>()->GetWindow();
    		wpfC = WPFI::CreateWPFControl(0, 0, 600, 300);
    		SDLWindows::CreateSecondWindow(wpfC, sdlw);
    // -----------------------------------------------------------------------

    
    void SDLWindows::CreateSecondWindow(HWND hwnd, SDL_Window * sw)
    {
    	Uint32 flags = SDL_WINDOW_SHOWN
    		| SDL_WINDOW_FOREIGN
    		| SDL_WINDOW_MOUSE_CAPTURE
    		| SDL_WINDOW_ALWAYS_ON_TOP
    		| SDL_WINDOW_BORDERLESS
    		;

    	SDL_InitSubSystem(SDL_INIT_VIDEO);
    	sw = SDL_CreateWindowFrom(hwnd, flags); // with flags or without, not difference
    	if (sw == nullptr)
    	{
    		std::cout << "-------------------\n" << "sdlWnd = NULL\n" << "-------------------\n";
    	}
    	else
    	{
    		std::cout << "-------------------\n" << "sdlWnd = ok\n" << "-------------------\n";
    	}

    	SDL_SetWindowTitle(sw, "SDL Window - Set by SDL"); 
    	SDL_Surface* s = SDL_GetWindowSurface(sw);
    	SDL_FillRect(s, &s->clip_rect, 0xffff00ff);
    	SDL_UpdateWindowSurface(sw);
    	//SDL_RaiseWindow(sw);
    }

-------------------------

Dave82 | 2019-09-11 18:27:23 UTC | #3

Since you use HWND your app won't  be cross platform. If you don't want cross platform support then you could use winapi directly and GetExternalWindow to obtain the main window's hwnd and use it as a parent. Theoretically...

-------------------------

Elendil | 2019-09-11 18:47:43 UTC | #4

Thanks for reply.
But ExternalWindow is NULL by default (from documentation). You mean obtain main window from Urho3D ?
If possible I want use Urho3D window as main window.
Btw. I am not looking for crossplatform solution.

-------------------------

Elendil | 2019-09-11 20:40:35 UTC | #5

I have trouble get right HWND from window

    SDL_Window * sdlw = context->GetSubsystem<Graphics>()->GetWindow();
    HWND mw = SDLWindows::GetWindowHWND(sdlw);

    // ...

    HWND SDLWindows::GetWindowHWND(SDL_Window * wnd)
    {
    	SDL_SysWMinfo sysInfo;

    	SDL_VERSION(&sysInfo.version);
    	SDL_GetWindowWMInfo(wnd, &sysInfo);
    	return sysInfo.info.win.window;
    }

    // ...

    HWND www = SetParent(wpfC, mw);
    if (www == NULL)
    	{
    		std::cout << "------------------------------\n"
    			<< "www = NULL\n"
    			<< GetLastError() << "\n"
    			<< "------------------------------\n";
    	}

I got **Invalid window handle** (1400). Error
I am sure that SDL window is problematic because my wpfC HWND is working on my previous test project, but instead SDL window I use win32 window.

-------------------------

Elendil | 2019-09-12 00:03:33 UTC | #6

I found solution for Invalid window handle.

I edit source code of Urho3D engine and create function 
   
    void *GetSDLWindowHWND()
    HWND hWnd = static_cast<HWND>(context->GetSubsystem<Graphics>()->GetSDLWindowHWND());

after that, SetParent() function working and my window child is displayed in Urho3D main window.

But one problem with that, when I set parent for my window, background is not transparent. It make "hole" in to Urho renderer. On my test project without Urho, it is working as expected.

-------------------------

Modanung | 2019-09-12 08:41:59 UTC | #7

Could you share a screenshot displaying this issue? I'm not sure what you mean by it "making a hole".

-------------------------

Elendil | 2019-09-12 09:23:37 UTC | #8

making hole means, window is transparent, but what is displayed behind transparent is not Urho3D but some default win32 background color.

1. First image is how it should look like. (window is displayed as not child)

2. Second image is how it is like if window is child with SetParent and use ElementHost for make background transparent. (if is not transparent, background is black)

![urhoNG1|690x397](upload://pdAq0ujG6ezeB7XEghATij9XBHs.jpeg) ![urhoNG2|690x457](upload://wAmhCPUDmPmRrNP8p61UKqEWM3p.jpeg)

-------------------------

Leith | 2019-09-13 00:43:40 UTC | #9

Hey Elendil!
See <https://wiki.libsdl.org/SDL_SetWindowOpacity>
Note it only works for certain platforms, such as Windows and OSX.

-------------------------

Modanung | 2019-09-13 09:24:01 UTC | #10

On Linux is does work using Qt:
https://discourse.urho3d.io/t/the-legendary-fish-on-your-desktop/5455

@Elendil Are you sure you need a second SDL window, btw?
In the screenshots the second window does not leave the main window.

-------------------------

Elendil | 2019-09-13 12:00:35 UTC | #11

[quote="Leith, post:9, topic:5565"]
See https://wiki.libsdl.org/SDL_SetWindowOpacity
Note it only works for certain platforms, such as Windows and OSX.
[/quote]
I need only Windows. Does the SetWindowOpacity make whole windows transparent or only certain area (which have transparent background)? Because this is big difference and I need window with background transparent (as you see on images I post above) where objects (text and button) are not transparent.

---

[quote="Modanung, post:10, topic:5565"]
Are you sure you need a second SDL window, btw?
In the screenshots the second window does not leave the main window.
[/quote]
This is the right question, if you know how to embed WPF renderer in to Urho renderer, I don't need second window. (I know that WPF can do D3DImage but I am not sure if it is right way to go with performance).
And yes, I need the second window not leave main window and resize as main window resize.

I need use WPF as GUI. Therefore I need second window which will be front of Urho3D renderer and tied to the main window as described. If it will be SDL_Window or WPF or Win32, I don't care. I tried use WPF as ExternalWindow for Urho, problem with that is Renderer is front of WPF content. I am going to try another few ideas.

-------------------------

Modanung | 2019-09-13 14:50:14 UTC | #12

[quote="Elendil, post:11, topic:5565"]
And yes, I need the second window not leave main window and resize as main window resize.

I need use WPF as GUI.
[/quote]

What reasons do you have to not use Urho's UI subsystem in this case?

-------------------------

Elendil | 2019-09-13 14:59:53 UTC | #13

I am much confortable with WPF. Another + is once it will be working, I can easyly use it in another game engine.

-------------------------

