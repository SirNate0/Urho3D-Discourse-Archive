christianclavet | 2017-01-02 01:10:57 UTC | #1

Hi, I've read somewhere in the posts that the window creation mechanism was handled by SDL. But that it was not possible to create multiple windows. Done a search to see if SDL could support that and found that it would be possible to open multiple windows with a GL render context in each using the command [b][i]SDL_GL_MakeCurrent [/i][/b]().

[url]http://wiki.libsdl.org/SDL_GL_MakeCurrent[/url]

Is the version that URHO3D use support this? For creating applications with URHO, this ability would be really nice to have. But I know this is only for GL, so perhaps not supported by any other renderer... Perhaps there is something else that make that not possible... I'm just starting with URHO.

I also have another question about the mouse pointer, I see there are the OS mouse pointer and the UI mouse pointer. Does URHO have any commands to manipulate/check the OS mouse pointer? I just remarked that the mouse pointer position is reset to the center of the window when the URHO application is launched when I checked the demos. For a game it's ok, but kinda strange for an application.

Thanks.

-------------------------

George | 2017-01-02 01:10:58 UTC | #2

Hi Christian
I want to know the first question too.


For mouse
	Input* input = GetSubsystem<Input>();
	input->SetMouseMode(MouseMode::MM_ABSOLUTE);
	input->SetMouseVisible(true);

Regards

-------------------------

cadaver | 2017-01-02 01:10:58 UTC | #3

Multiple windows in the same application aren't supported.

-------------------------

christianclavet | 2017-01-02 01:11:00 UTC | #4

Thanks. Understood, URHO can only be used for a single window and a single opengl context. I should have put this question on another thread (general) and not in support. Sorry.

Wow! I've tried to see if I could use SDL directly (saw that the includes of multiples THIRD PARTY stuff was accessible) When the demo opened, it opened a separate windows that seem to support a openGL context! So I have a URHO application that have a main windows and a external SDL window!!!  :smiley: 

Added only this part of code from the SDL wiki:
[code]SDL_Window *window;                    // Declare a pointer

    SDL_Init(SDL_INIT_VIDEO);              // Initialize SDL2

    // Create an application window with the following settings:
    window = SDL_CreateWindow(
        "An SDL2 window",                  // window title
        SDL_WINDOWPOS_UNDEFINED,           // initial x position
        SDL_WINDOWPOS_UNDEFINED,           // initial y position
        640,                               // width, in pixels
        480,                               // height, in pixels
        SDL_WINDOW_OPENGL                  // flags - see below
    );
[/code]
This opened a separate windows (empty), and had the main windows containing the URHO element.

What I would like mostly to do with URHO is applications. And this seem to open the door to multiple windows with URHO (As long as I keep URHO in the main windows and use and manage the others with SDL), I will have to see how to get the events for the other windows using SDL perhaps.
 
The other windows would mostly have GUI, so I will need to use a external GUI like imgui. Could perhaps even find a way to later take RTT rendering from URHO and sent it to the other SDL windows.
So a big thanks to have created a way to access the other libs that URHO uses with the includes! This really make it a lot easier! Can we do stuff like this with all the libs that URHO3D uses and not only SDL?

EDIT: Opps. Just found out that there must be one a single OPENGL context per application. (At least that's what happening now. The windows open, but URHO see the second context and cause a problem.) I'll have to find another way to have that.

-------------------------

weitjong | 2017-01-02 01:11:00 UTC | #5

We in general do not expose the 3rd-party headers to Urho3D lib users unless it is absolutely necessary, i.e. the build system only installs those headers that our Urho3D headers depend on, with a few exceptions such as Lua. However, nothing prevent you from installing the others for your own app.

-------------------------

cadaver | 2017-01-02 01:11:03 UTC | #6

Was there the problem with static linking that if user wants to use e.g. SDL or Bullet functions that were not used by Urho itself, they wouldn't be included in the Urho library?

-------------------------

weitjong | 2017-01-02 01:11:03 UTC | #7

On the contrary I think that kind of problem would only happen with shared lib. With static lib it basically just an archive of all object files, whether Urho uses them or not.

-------------------------

