TheComet | 2017-01-25 02:22:36 UTC | #1

I noticed that SDL_Init() is called only in the constructor of Graphics, however, in headless mode, Grahpics is never created. The Input, UI, FileSystem, and Audio subsystems and a few other objects will still call SDL functions, though.

Why does headless mode work?

-------------------------

cadaver | 2017-01-26 13:17:23 UTC | #2

SDL_Init() is basically used here to tell "we are going to be a windowful application" and it inits the major SDL subsystems like video & audio. You can still use minor SDL "helper" functionality without. 

Audio is actually a bit of luck because the Engine init doesn't call Audio::SetMode() in headless mode. However you could call it yourself, which could result in something nasty happening. 

The point you raise is good, all the code related to this is worth reviewing. Though right now I can't think of a better place to call SDL init, because ideally the individual subsystems should be usable e.g. without Engine class at all, and window opening / graphics rendering is tied strongest to SDL being fully initialized.

-------------------------

TheComet | 2017-01-26 14:41:12 UTC | #3

I didn't realise you could use Graphics without Engine. Now it makes sense to me why SDL was initialised like that.

Might I suggest moving `SDL_Init()` into the `Context` class? Depending on whether SDL should be initialised in headless mode or not, `SDL_Init()` could be called in the constructor or explicitly. For instance, here's what the explicit method might look like:

    Graphics::Graphics(Context* context) : 
        Object(context),
        // more stuff
    {
        context_->RequireSDL(SDL_INIT_VIDEO); 
    }

    Graphics::~Graphics()
    {
        context_->ReleaseSDL();
    }

`Context` would take care of initialising the various SDL systems by using `SDL_WasInit()` and additionally keep a global "reference count" of how many times SDL was initialised, so it knows when to call SDL_Quit().

The audio subsystem would similarly call `context_->RequireSDL()` but pass in SDL_INIT_AUDIO.

Of course, the lazy solution could be to call `SDL_Init(SDL_INIT_EVERYTHING)` in the constructor of `Context` and be done with it.

-------------------------

cadaver | 2017-01-26 15:34:57 UTC | #4

Yes, that's a good idea.

-------------------------

TheComet | 2017-01-26 17:54:08 UTC | #5

I'll submit a PR in that case, since I'm already poking around in these areas.

-------------------------

