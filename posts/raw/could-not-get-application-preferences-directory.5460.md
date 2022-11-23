capelenglish | 2019-08-13 13:11:00 UTC | #1

I have written a bunch of games in C++ and use a python script (subprocess.Popen) to launch them. This has been working just fine for over a year. Just recently, I've begun to get the following error when launching a game:

    [Tue Aug 13 08:49:52 2019] INFO: Initialized input
    [Tue Aug 13 08:49:52 2019] INFO: Initialized user interface
    [Tue Aug 13 08:49:52 2019] INFO: Initialized renderer
    [Tue Aug 13 08:49:52 2019] WARNING: Could not get application preferences directory
    [Tue Aug 13 08:49:52 2019] INFO: Set audio mode 44100 Hz stereo interpolated
    [Tue Aug 13 08:49:52 2019] INFO: Initialized engine
    [Tue Aug 13 08:49:52 2019] WARNING: Could not get application preferences directory

It doesn't always happen, but when it does, my display just shows a grey screen and the game doesn't come up. The directory

    ~/.local/share/urho3d

exits and if I run the game from the command line it works just fine. I have tried setting the userid and groupid using the Popen preexec_fn argument, but that has made no difference. The only thing I can think of is some sort of corrupt file system. 

Does anyone have an idea as to what is going on?

-------------------------

Modanung | 2019-08-13 15:01:19 UTC | #2

I have no idea, but did you look into the definition of `GetAppPreferencesDir()`?
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/IO/FileSystem.cpp#L742-L757

-------------------------

capelenglish | 2019-08-13 18:03:02 UTC | #3

I did. I also looked at SDL_GetPrefPath.

    const char *envr = SDL_getenv("XDG_DATA_HOME");

so I ran

    env | grep XDG

and got

    XDG_SESSION_ID=2
    XDG_DATA_DIRS=/usr/local/share:/usr/share:/var/lib/snapd/desktop
    XDG_RUNTIME_DIR=/run/user/1000

obviously, I don't have XDG_DATA_HOME defined. I'm not sure where this env should point since it has never been defined in the past...

-------------------------

Modanung | 2019-08-13 18:05:05 UTC | #4

Maybe this is useful then?
https://askubuntu.com/questions/157722/setting-xdg-data-dirs-and-xdg-data-home#157733

-------------------------

