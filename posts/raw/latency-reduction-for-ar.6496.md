Simeon | 2020-11-02 10:14:24 UTC | #1

I'am doing tests using AR devices with Urho3d on linux environements. It's working well: building stereo view and using the 6dof tracker to update view of the scene. But the latency is too high. I have done multiple tests:

* using opengl vsync: it increases the latency of around the refresh rate period of the display, but tearing was already removed without vsync activated. It don't seems to be the solution.
* increasing the engine FPS: the latency is lower but I see that the engine is waiting if rendering is fast but after the rendering. At the end  it will increase resources consumption and add judder when rendering FPS is lower than display refresh rate.

Maybe asynchronous time warping strategy could be a good idea deal with latency issue? Did someone already have done kind of ATW with urho3d ?

-------------------------

vmost | 2020-11-02 13:35:19 UTC | #2

If there is no tearing you must have some kind of vsync solution on by default. IIRC the only levers available to Urho3D are: vsync on/off, triple buffering on/off, and max/min FPS. Try disabling both triple buffering and vsync explicitly.
```
bool UpdateScreenModes(const ScreenModeParams &screen_params) const
{
	IntVector2 screen_size = GetSubsystem<Graphics>()->GetSize();

	return GetSubsystem<Graphics>()->SetDefaultWindowModes(screen_size.x_, screen_size.y_, screen_params);
}

void UnsetRefreshModes() const
{
    ScreenModeParams screen_params = GetSubsystem<Graphics>()->GetScreenModeParams();
    screen_params.vsync_ = false;
    screen_params.tripleBuffer_ = false;
    UpdateScreenModes(screen_params);
}
```

Note: it seems triple buffering is only available to D3D9.

-------------------------

Simeon | 2020-11-02 15:16:44 UTC | #3

Thank you, I try it don't see the difference (except more latency with vsync). I guess I have some system wide or gpu wide synchro activated, but I then don't find an access to a kind of swap buffer to catch the display refresh time. If I can catch the "swap buffer" time I think it is possible to implements kind of ATW, but I don't know if it accessible by urho3d. Any idea about that?

Thanks a lot !

-------------------------

vmost | 2020-11-02 15:54:59 UTC | #4

What do you mean by latency exactly? Lower FPS than expected?

-------------------------

Simeon | 2020-11-02 16:42:41 UTC | #5

I don't mean low FPS, I mean latency from the end of the rendering to the actual display on the monitor. For example the latency from head motion to camera 6dof pose update is very low (<3ms) and with a small scene the rendering time is also low (<2ms) but the latency at the end on the display is >20 ms. So there is a lost of time between the end of rendering (at E_ENDRENDERING event) and the actual display on monitor. I wonder if urho3d or OpenGL gives a way to access the actual "displayed" time to implements kind of ATW.

-------------------------

vmost | 2020-11-02 18:56:42 UTC | #6

One thing you could test is adding an artificial delay at the `E_ENDRENDERING` event, and see if it impacts the frame rate. If it doesn't, then all that time is being spent waiting for a buffer swap of some kind. If it does, then there is some blockage in the display pipe. I wouldn't be surprised if your AR devices force vsync. IOS devices do this as well, no way around it.

Not too sure what ATW is, but you can always use `Urho3D::Timer` class to get timings between different events, and insert delay with
```
    m_timer.Reset();
	while (true)
	{
	    elapsed = m_timer.GetUSec(false);
	    if (elapsed >= delay)
	        break;

	    // Sleep if 1 ms or more off the frame limiting goal
	    if (delay - elapsed >= 1000LL)
	    {
	        auto sleepTime = (unsigned)((delay - elapsed) / 1000LL);
	        Time::Sleep(sleepTime);
	    }
	}
```

This actually gives me an interesting idea for improving vsync (I have a silly experimental vsync controller project). To reduce input lag, you want the delta between 'input consumption' and 'display new frame' to be very low. This way input collected in frame A affects frame B. Vsync adds a big delay between input consumption and frame display, so input on frame A may be collected while frame B is waiting to be displayed. So instead, move the vsync delay to E_ENDFRAME, which is the only event between `SDL_GL_SwapWindow()` and `E_BEGINFRAME` where inputs are consumed. Perhaps this is ATW? The main cost is more frequent frame losses, which may be avoidable to some extent.

-------------------------

Eugene | 2020-11-02 19:06:06 UTC | #7

[quote="Simeon, post:5, topic:6496"]
So there is a lost of time between the end of rendering (at E_ENDRENDERING event) and the actual display on monitor.
[/quote]
`E_ENDRENDERING` is the end of engine submitting draw commands to GPU. Whatever latency GPU adds is the question of said GPU drivers.

The latency you are talking about is outside of engine control.
Try tinkering with internal presentation settings and things like these:
 https://docs.microsoft.com/en-us/windows/win32/api/dxgi/ne-dxgi-dxgi_swap_effect

-------------------------

Simeon | 2020-11-03 07:54:50 UTC | #8

Ok, thank you, yes it should help to reduce resources. But it isn't exactly ATW, see here for a explanation of ATW: https://uploadvr.com/reprojection-explained/.

-------------------------

Simeon | 2020-11-03 08:05:06 UTC | #9

Ok, understand that it is outside engine control. After some readings, I think GPU manufacturers introduced new features to make it possible (for example https://developer.nvidia.com/vrworks/headset/contextpriority), I'am not aware about all those technics. Thanks for the link, more focused now on linux/android use cases, I will see if I found something in OpenGL extensions. If you have some ideas about that I'm interesting, thanks !

-------------------------

