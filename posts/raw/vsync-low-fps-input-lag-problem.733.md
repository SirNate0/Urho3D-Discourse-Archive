Enhex | 2017-01-02 01:02:32 UTC | #1

Hi,

I'm experiencing severe input lag with vsync on.
Few things I noticed about it:
- Holding down more button causes the lag to increase.
- There's more lag in full screen than in window mode.
- In windowed mode it can cause the mouse to travel far enough to leave the window. (suggesting something prevents it from re-centering)

You can experience it in the ninja snow war game or character demo. try looking around fast with your mouse, then try to hold down WASD (all of them) and look around fast again. You'll notice it's slightly more laggy.
In my game I experience extreme case of this lag which makes the game unplayable since it requires very responsive controls.

I noticed that when I enabled vsync and use SetMaxFps(60); the lag is greatly reduced and capped at a lower point (i.e. I don't get extremely long freezes). It may suggest that there's some sort of desync between input polling and updates.
Another thing that may cause it is lost mouse messages. I barely know anything about it but if the vsync busy polling doesn't check for mouse messages, that could mean mouse messages are missed?

Another thing I noticed is that when I reduce the frame rate to something low such as 20-30, hold down any button and move the mouse, the mouse speed slows down and resets in intervals of few seconds.
I tested it and the values I get from input->GetMouseMoveX() and input->GetMouseMoveY() are the ones that scale down.
In windowed mode the mouse can leave the window when the mouse speed is slow enough.

Note that I don't experience anything similar with other games, only when I use Urho3D.

What can cause this problem and how can it be fixed?


[b][u]EDIT[/u][/b]
Right now SDL2's event queue is the main suspect.

-------------------------

Enhex | 2017-01-02 01:02:34 UTC | #2

I found the sources of the lag.

The first one is SDL_PeepEvents. Switching to SDL_PollEvent greatly reduced the lag.
The only main difference is that SDL_PeepEvents is thread safe, but that shouldn't be a problem since the input Update() isn't threaded.

The second cause is the following line in D3D9Graphics.cpp:
[code]impl_->presentParams_.PresentationInterval = D3DPRESENT_INTERVAL_ONE;[/code]

For some reason when using vsync option via Urho3D that lag occurs, but when I set it through my graphics card settings (Nvidia GTX670) I get vsync without the input lag.

Using max FPS 60(my monitor refresh rate) or 59(slightly less lag) with vsync does reduce the lag to almost unnoticeable level, but vsync still introduces some lag that doesn't happen with the hardware configured vsync.


I tried forcing OpenGL and I it doesn't have the lag problem.
I noticed that OpenGL uses SDL_GL_SetSwapInterval() to enable/disable vsync, that may suggest that it changes something with SDL that prevents the lag.
OpenGL build still lags if SDL_PeepEvents is used, so SDL_PollEvent is a must.

-------------------------

cadaver | 2017-01-02 01:02:34 UTC | #3

We already pump events once to fill SDL's internal event queue from OS, then process all of them. PollEvents() would call PumpEvents() on its own, and could theoretically loop forever if new OS-level events are being added all the time, so I'm reluctant to change this.

On D3D9 you should try calling Graphics::SetFlushGPU(true). This will force the CPU to not get ahead of GPU and therefore reduce the apparent input lag, but will cost some performance due to the syncing/stalling that will be happening each frame.

-------------------------

Enhex | 2017-01-02 01:02:34 UTC | #4

The lag happens in both OpenGL and DirectX when using SDL_PeepEvents.
I did profiling with the Urho profiler when using vsync and with SDL_PollEvent I get between 0.3-1.5 ms max when moving the mouse and/or pressing buttons, while with SDL_PeepEvents I get 16-18 ms max. In my experience the lag was much worse and could cause halt which were as long as several 100's of miliseconds and inconsistent mouse speed.
I also tested it with an empty project using the external lib guide and I got the same result.

Maybe there's a way to configure SDL so the lag won't happen with SDL_PeepEvents (maybe using threading), but until it's found SDL_PollEvent will work better.

-------------------------

cadaver | 2017-01-02 01:02:34 UTC | #5

The internal SDL code is almost the same, maybe the difference is that SDL_PollEvent() will call SDL_PumpEvents() again for each received event.

However, I observed subjectively smoother mouse input under Windows with vsync on when using SDL_PollEvent(), so I'll commit the change you suggested. It can always be reverted if it leads into trouble. Can't comment on the subject of lag difference though.

-------------------------

