miz | 2017-01-02 01:10:24 UTC | #1

Hi, I've got a problem when running the game I'm making on the Rpi2. For some reason when I'm clicking on things in game the OS cursor is not disabled so upon closing the game I find I've opened all sorts of windows and written long strings of w, a, s and d in all of them. Is there a way to disable OS input while the game is running? I couldn't find a way.
Thanks :slight_smile:

-------------------------

weitjong | 2017-01-02 01:10:24 UTC | #2

There is a bug in our current RPI port in regards to input (keyboard and mouse) event handling. We have erroneously still relied on X11 stack for the input event handling. We thought we do not use any of X11 subystem already. We only find out about this bug in our recent work to migrate to SDL 2.0.4. In the new SDL-2.0.4-upgrade branch we have tried to rectify this. In the new branch you will need to have additional libevdev2 development library (if you are using Raspbian) installed before building the Urho3D. Unfortunately though the new branch is not yet ready. So, YMMV if you attempt to check it out now.

Alternatively, if you cannot wait then you can try to manually edit the Source/ThirdParty/SDL/include/SDL_config_linux.h to disable all of these below. In our current implementation in the master branch, this file is being shared by Linux and RPI, so we could not safely do that, but instead we could probably disable them conditionally when targeting RPI. But since the merging of SDL-2.0.4-upgrade branch is imminent, we will probably not do this fix now in the master branch. However, that should not stop you from doing so if you cannot wait.
[code]#define SDL_VIDEO_DRIVER_X11_DYNAMIC "libX11.so.6"
#define SDL_VIDEO_DRIVER_X11_DYNAMIC_XEXT "libXext.so.6"
/* #undef SDL_VIDEO_DRIVER_X11_DYNAMIC_XCURSOR */
/* #undef SDL_VIDEO_DRIVER_X11_DYNAMIC_XINERAMA */
/* #undef SDL_VIDEO_DRIVER_X11_DYNAMIC_XINPUT2 */
#define SDL_VIDEO_DRIVER_X11_DYNAMIC_XRANDR "libXrandr.so.2"
/* #undef SDL_VIDEO_DRIVER_X11_DYNAMIC_XSS */
/* #undef SDL_VIDEO_DRIVER_X11_DYNAMIC_XVIDMODE */
/* #undef SDL_VIDEO_DRIVER_X11_XCURSOR */
/* #undef SDL_VIDEO_DRIVER_X11_XINERAMA */
/* #undef SDL_VIDEO_DRIVER_X11_XINPUT2 */
/* #undef SDL_VIDEO_DRIVER_X11_XINPUT2_SUPPORTS_MULTITOUCH */
#define SDL_VIDEO_DRIVER_X11_XRANDR 1
/* #undef SDL_VIDEO_DRIVER_X11_XSCRNSAVER */
#define SDL_VIDEO_DRIVER_X11_XSHAPE 1
/* #undef SDL_VIDEO_DRIVER_X11_XVIDMODE */
#define SDL_VIDEO_DRIVER_X11_SUPPORTS_GENERIC_EVENTS 1
#define SDL_VIDEO_DRIVER_X11_HAS_XKBKEYCODETOKEYSYM 1[/code]

-------------------------

weitjong | 2017-01-02 01:10:24 UTC | #3

BTW, your game will run much faster when you don't run any DE in the background. Configure your RPI to boot into text mode and start the game directly there from the console.

-------------------------

miz | 2017-01-02 01:10:31 UTC | #4

Thanks for the help!

-------------------------

UrOhNo3D | 2017-01-02 01:10:36 UTC | #5

[quote="weitjong"]Alternatively, if you cannot wait then you can try to manually edit the Source/ThirdParty/SDL/include/SDL_config_linux.h to disable all of these below.
[code]#define SDL_VIDEO_DRIVER_X11_DYNAMIC "libX11.so.6"
#define SDL_VIDEO_DRIVER_X11_DYNAMIC_XEXT "libXext.so.6"
/* #undef SDL_VIDEO_DRIVER_X11_DYNAMIC_XCURSOR */
/* #undef SDL_VIDEO_DRIVER_X11_DYNAMIC_XINERAMA */
/* #undef SDL_VIDEO_DRIVER_X11_DYNAMIC_XINPUT2 */
#define SDL_VIDEO_DRIVER_X11_DYNAMIC_XRANDR "libXrandr.so.2"
/* #undef SDL_VIDEO_DRIVER_X11_DYNAMIC_XSS */
/* #undef SDL_VIDEO_DRIVER_X11_DYNAMIC_XVIDMODE */
/* #undef SDL_VIDEO_DRIVER_X11_XCURSOR */
/* #undef SDL_VIDEO_DRIVER_X11_XINERAMA */
/* #undef SDL_VIDEO_DRIVER_X11_XINPUT2 */
/* #undef SDL_VIDEO_DRIVER_X11_XINPUT2_SUPPORTS_MULTITOUCH */
#define SDL_VIDEO_DRIVER_X11_XRANDR 1
/* #undef SDL_VIDEO_DRIVER_X11_XSCRNSAVER */
#define SDL_VIDEO_DRIVER_X11_XSHAPE 1
/* #undef SDL_VIDEO_DRIVER_X11_XVIDMODE */
#define SDL_VIDEO_DRIVER_X11_SUPPORTS_GENERIC_EVENTS 1
#define SDL_VIDEO_DRIVER_X11_HAS_XKBKEYCODETOKEYSYM 1[/code][/quote]

Hi,
Can you please clarify what you mean here? When you say 'to disable all of these below', do you mean comment out the lines which are not currently commented out or does this also mean that the 'undef's should be uncommented?

Thanks!

-------------------------

weitjong | 2017-01-02 01:10:36 UTC | #6

I meant to say, comment out those that are still being defined. Our RPI port should not depend on X11 display server or other X11 stack. In the SDL-2.0.4-upgrade branch, even the Linux desktop platform is not solely dependent on X11 as the only display server now.

-------------------------

UrOhNo3D | 2017-01-02 01:10:42 UTC | #7

[quote="weitjong"]In the SDL-2.0.4-upgrade branch, even the Linux desktop platform is not solely dependent on X11 as the only display server now.[/quote]

Thank you for your quick and useful response.
Is the SDL-2.0.4-upgrade branch suitable for building at this point? If not, how long do you anticipate it will be before it can be used or merged into master?

I will attempt to use your suggested method today in the meantime.

-------------------------

weitjong | 2017-01-02 01:10:42 UTC | #8

The new branch is ready when it is ready :wink:  No promise, but it should happen rather sooner. If you don't care about other recent bug fixes and improvement in the master branch then you can check the SDL-2.0.4-upgrade branch today. At the moment that branch only has remaining build issues with web and iOS platforms. You should not have problem when targeting Windows, Linux, Android, and RPI platforms. In fact it is good if you can do so, so that you can help us to test it and to report back any new issues we don't know yet.

-------------------------

