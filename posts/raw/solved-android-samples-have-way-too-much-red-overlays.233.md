Faizol | 2017-01-02 00:59:03 UTC | #1

Hi all,

  Firstly I'm sorry if these two questions are redundant as I've tried unsuccessfully to search it in the forum.

  I successfully followed the instruction on how to compile and install Urho3D on Android devices. However whenever I tried to run the samples, the colors are way too much red that it's hard to see the objects. As for the second problem, whenever a sample is run, the running sample seems to can't go back to the main menu. The only way for me to run another example is by forcefully stop the running example and to start the samples all over again.

  I compiled Urho3D and the samples against Android API 14 (Android 4.0, target ID 7). The testing hardware is Galaxy Note 10.1 (Android 4.1.2). Is there a pointer on how to solve this?

  Thank you in advanced.

-------------------------

Faizol | 2017-01-02 00:59:03 UTC | #2

Update:
Turns out the solution is very simple. Just turn on "Disable hardware overlays" in the Developer Options setting.

Thanks.

-------------------------

cadaver | 2017-01-02 00:59:03 UTC | #3

There is also a pending pull request which apparently will fix this. It's somewhat odd (request 0 bits depth buffer, related to choosing the OpenGL ES pixel format) but just needs to be tested.

-------------------------

Faizol | 2017-01-02 00:59:04 UTC | #4

[quote="cadaver"]There is also a pending pull request which apparently will fix this. It's somewhat odd (request 0 bits depth buffer, related to choosing the OpenGL ES pixel format) but just needs to be tested.[/quote]

Hi cadaver,

  Thanks for the heads up. Is it possible to know a rough estimate when the fix gonna be merged?

  On a side note, what's the features roadmap and perhaps schedules planned for the future releases, if any?

  Thank you.

-------------------------

cadaver | 2017-01-02 00:59:04 UTC | #5

I tested the pull request and unfortunately it can't be merged, as the proposed fix would disable depth buffering altogether.

My guess is that a proper fix would involve hacking the SDL function which determines the EGL pixel format to use, but I personally have no hardware for testing this. The function in question is SDL_EGL_ChooseConfig() in Source/ThirdParty/SDL/src/video/SDL_egl.c

We don't have an actual organized roadmap, the best approximation to one is to follow the issues, development discussion here, and the branches in addition to master branch at github.

-------------------------

Faizol | 2017-01-02 00:59:05 UTC | #6

Hi cadaver,

  I've tried to reproduce the issue but failed everytime. And I tried this (for both checked the "Disable hardware overlay" option and off). I have since the last post uninstalled a few video player programs from the device as I have a vague memory that one of the programs did have an option to set hardware overlay. Is it possible to know exactly where should I change the SDL_EGL_ChooseConfig() in SDL_egl.c just to be sure of this?

 Thanks.

-------------------------

cadaver | 2017-01-02 00:59:05 UTC | #7

You can try commenting out the lines

[code]
    attribs[i++] = EGL_DEPTH_SIZE;
    attribs[i++] = _this->gl_config.depth_size;
[/code]
Other than that, I don't have ideas.

-------------------------

