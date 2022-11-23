Sinoid | 2018-02-02 05:22:41 UTC | #1

I'm probably not the only one that can't stand the way things resize in windowed mode (on Windows at least).

This snippet attaches an SDL callback for window-resizing so the window will continue to paint while being resized, it's usually behind a by a short bit but it's much better than watching a giant black square expand.

Specific snippet for D3D11Graphics.cpp (applies to wherever each target starts the window):

    static int ResizingEventWatcher(void* data, SDL_Event* event)
    {
        if (event->type == SDL_WINDOWEVENT &&
            event->window.event == SDL_WINDOWEVENT_RESIZED) {
            SDL_Window* win = SDL_GetWindowFromID(event->window.windowID);
            if (win == (SDL_Window*)data) 
            {
                Context* ctx = (Context*)SDL_GetWindowData(win, "CONTEXT");
                auto graphics = ctx->GetSubsystem<Graphics>();
                auto renderer = ctx->GetSubsystem<Renderer>();
                if (renderer && graphics->IsInitialized())
                {
                    graphics->OnWindowResized();
                    ctx->GetSubsystem<Engine>()->RunFrame(); 
                    // or break the frame down as desired if running won't cut it
                    // beware of glorious rawPtr crashes from unexpected state, ie. Time system not running, etc
                    // resized event still happens, just after this happens a whole bunch
                }
            }
        }
        return 0;
    }

    bool Graphics::OpenWindow(int width, int height, bool resizable, bool borderless)
    {
        if (!externalWindow_)
        {
            unsigned flags = 0;
            if (resizable)
                flags |= SDL_WINDOW_RESIZABLE;
            if (borderless)
                flags |= SDL_WINDOW_BORDERLESS;

            window_ = SDL_CreateWindow(windowTitle_.CString(), position_.x_, position_.y_, width, height, flags);
        }
        else
            window_ = SDL_CreateWindowFrom(externalWindow_, 0);

        if (!window_)
        {
            URHO3D_LOGERRORF("Could not create window, root cause: '%s'", SDL_GetError());
            return false;
        }

    // < NEW CODE > ============================================

        SDL_SetWindowData(window_, "CONTEXT", GetContext());
        SDL_AddEventWatch(ResizingEventWatcher, window_);

    // < END NEW CODE > ========================================

        SDL_GetWindowPosition(window_, &position_.x_, &position_.y_);

        CreateWindowIcon();

        return true;
    }

Likely Windows specific unless other OS' have similar issues with sizing seizing.

-------------------------

weitjong | 2018-02-02 10:29:49 UTC | #2

Could be related to this issue.

https://github.com/urho3d/Urho3D/issues/2150

The OP of the issue didn’t respond to the last comment and so the issue was closed. I think your solution might help in his case as well. 

If it is generic enough then we welcome you submit it as PR.

-------------------------

