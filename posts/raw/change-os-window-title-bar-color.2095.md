godan | 2017-01-02 01:13:02 UTC | #1

I've done a bit of searching on this topic and couldn't get a clear answer:

Is it possible to set the color of the window title bar color of the OS window? I know we can set the icon and title, and I'm pretty sure that there is no current code to set the color, but is it possible? It is definitely doable with OS specific code, but does SDL expose anything? If it is possible, this would be a great feature to have.

-------------------------

godan | 2017-01-02 01:13:02 UTC | #2

I think it would also be fine to get the HWND and whatever the OSX equivalent is and modify the title bar directly....can you just cast from the SDL_Window? I've not spent much time with SDL (clearly...:slight_smile:).

-------------------------

rasteron | 2017-01-02 01:13:03 UTC | #3

Of course it is possible with SDL, if supported. I got a related issue where I needed to display a notification window on Android and I tested it on my custom engine which also uses SDL.

So in summary if this is not officially included you do have to expose it on your own. :wink:

-------------------------

godan | 2017-01-02 01:13:03 UTC | #4

Hrm, not sure I understand. I'm fine with writing my own "SetTitleBarColor" function or something, however I can't figure out where the relevant data is. For instance, this seems to be the SDL_Window struct (SDL_sysvideo.h line 70):

[code]/* Define the SDL window structure, corresponding to toplevel windows */
struct SDL_Window
{
    const void *magic;
    Uint32 id;
    char *title;
    SDL_Surface *icon;
    int x, y;
    int w, h;
    int min_w, min_h;
    int max_w, max_h;
    Uint32 flags;
    Uint32 last_fullscreen_flags;

    /* Stored position and size for windowed mode */
    SDL_Rect windowed;

    SDL_DisplayMode fullscreen_mode;

    float brightness;
    Uint16 *gamma;
    Uint16 *saved_gamma;        /* (just offset into gamma) */

    SDL_Surface *surface;
    SDL_bool surface_valid;

    SDL_bool is_hiding;
    SDL_bool is_destroying;

    SDL_WindowShaper *shaper;

    SDL_HitTest hit_test;
    void *hit_test_data;

    SDL_WindowUserData *data;

    void *driverdata;

    SDL_Window *prev;
    SDL_Window *next;
};[/code]

Obviously, the SetWindowTitle and SetWindowIcon modify the "title" and icon fields. But it doesn't look like there is anything title bar related in here. Are you suggesting modifying the SDL code base to get at that info? I think that might be a bit out of my league.

As a shot in the dark, is the title bar color related to the window background color? I found a couple references to that, but it seems unlikely.

-------------------------

cadaver | 2017-01-02 01:13:03 UTC | #5

Urho itself uses the following code to get HWND from SDL window, after which you could use Win32 API operations on it. 

[code]
static HWND GetWindowHandle(SDL_Window* window)
{
    SDL_SysWMinfo sysInfo;

    SDL_VERSION(&sysInfo.version);
    SDL_GetWindowWMInfo(window, &sysInfo);
    return sysInfo.info.win.window;
}
[/code]
Though title bar color sounds like it would be dictated by the Windows display style. Here's something maybe relevant: [stackoverflow.com/questions/2056 ... ollbar-etc](http://stackoverflow.com/questions/2056774/win32-how-can-i-set-the-color-of-windows-title-scrollbar-etc)

-------------------------

weitjong | 2017-01-02 01:13:04 UTC | #6

Are you planning to change the window title color for your individual application? If yes, then I think it is an uphill task. I do not think SDL has the feature you are looking for. In my opinion, it is not because they cannot, but because there is no such API at the OS level. Now I am not saying OS could not change its windows title color as such. We can customize the color and more with "window decorator" applications, however, they usually apply the changes as a theme to all the windows and not individual window.

-------------------------

Sir_Nate | 2017-01-02 01:13:04 UTC | #7

At least on Ubuntu it should be possible (probably very difficult, but possible) -- Chrome manages to do it (I have no idea how, though). I think Microsoft office does something similar on Windows. I can't say for other platforms however.

Another option is to draw the window without a frame/titlebar, and then draw your own titlebar (and borders) on that, though I'm not sure if this has support on all platforms.

-------------------------

godan | 2017-01-02 01:13:04 UTC | #8

Hey thanks for the tips. Yes, in my reading there seem to be strong opinions on individual apps changing supposedly system wide settings (i.e. desktop themes). I guess what I'm after is something that looks like Spotify: 

[img]https://dl.dropboxusercontent.com/u/69779082/Spotify_title_bar.PNG[/img]

Here, the OS has it's standard title bar that handles window positioning and sizing, but is seamless with the app ui. 

That said, I have done some experiments with a borderless window, where I implement a title bard that is responsible for moving the window. I've been getting very strange behaviour. I'm using the E_DRAGMOVE event of a UI button to add a delta to the window position:

[code]
	using namespace DragMove;

	int X = eventData[P_DX].GetInt();
	int Y = eventData[P_DY].GetInt();
        moveDelta = IntVector2(X, Y);
	Graphics* g = GetSubsystem<Graphics>();

	IntVector2 pos = g->GetWindowPosition();
	pos += moveDelta;
	g->SetWindowPosition(pos);
[/code]

This gives very strange results, where the window moves by quite a bit (i.e 400-500 pixels) in the direction of the drag vector. I think if I could get this code to work, I might opt for a purely "Urho" handling of the window position.

-------------------------

rasteron | 2017-01-02 01:13:04 UTC | #9

[quote]Hrm, not sure I understand. I'm fine with writing my own "SetTitleBarColor" function or something, however I can't figure out where the relevant data is. For instance, this seems to be the SDL_Window struct (SDL_sysvideo.h line 70):[/quote]

I did mention [b]IF[/b] SDL supports it which apparently does not, but based on that reference, I think what you are looking for is more like using a full ui toolkit like QT which can handle skinning and is cross-platform.

I would not be surprised if that spotify client is made with Qt.

[community.spotify.com/t5/Help-D ... d-p/157256](https://community.spotify.com/t5/Help-Desktop-Linux-Windows-Web/Why-go-with-QT/td-p/157256)
[github.com/Elleo/cutespotify](https://github.com/Elleo/cutespotify)
[github.com/Elleo/libQtSpotify](https://github.com/Elleo/libQtSpotify)

There's already a Urho/Qt widget integration example here made by Aster for starters:

[topic318.html](http://discourse.urho3d.io/t/qt-based-2d-particle-editor-for-urho3d/327/1)
[github.com/aster2013/ParticleEditor2D.git](https://github.com/aster2013/ParticleEditor2D.git)

Good luck!

-------------------------

godan | 2017-01-02 01:13:09 UTC | #10

Thanks for all the help! For now, I've decided that having the OS title bar match the UI color scheme is not so important  :wink:  I think it looks pretty good as is (pure Urho UI):

[img]https://dl.dropboxusercontent.com/u/69779082/Iogram_titleBar.PNG[/img]

-------------------------

