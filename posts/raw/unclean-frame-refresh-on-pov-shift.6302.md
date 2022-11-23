vmost | 2020-08-07 20:41:38 UTC | #1

Hi, recently started getting Urho3D set up, and noticed a concerning behavior in one of the samples. It can be demonstrated with '20_HugeObjectCount'. Basically, if you zoom out and then wiggle the camera around some frames only partially refresh. I mean, I move the camera around and only some of the cubes' positions are updated. The effect appears as a 'jaggedness' around the edges of the set of cubes, and 'banding' within the set. When the camera moves faster, the jaggedness is more pronounced.

Is that intended behavior? Inevitable behavior? Fixable behavior? Unimportant behavior in a more realistic use of the engine? Why does this happen?

-------------------------

SirNate0 | 2020-08-07 20:04:32 UTC | #2

Do you have vsync enabled? It sounds a lot like what you might get with vsync disabled.

-------------------------

Modanung | 2020-08-07 20:48:40 UTC | #3

You can enable v-sync for the Urho3DPlayer by starting it with the **`-v`** flag (also try **`-h`**), and in your projects either with `engineParameters_[EP_VSYNC] = true;` in `YourApplication::Setup()` *or* with `GetSubsystem<Graphics>()->SetMode(...)` after that.

@vmost ...and welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

vmost | 2020-08-07 20:56:09 UTC | #4

Worked like a charm, thanks! It seems enabling vsync reduces the frame rate, which makes sense cause now every frame has to fully refresh.

-------------------------

Modanung | 2020-08-07 21:05:00 UTC | #5

V-sync is when a program waits for entire frames to render before they are submitted to the render buffer. *Without* v-sync, this submission interval is equal to that of the refresh rate.... something like that. :slightly_smiling_face:

So when you're frame rate is lower than your refresh rate it's a choice  between *double* or *bisected* frames.

-------------------------

vmost | 2020-08-08 15:37:12 UTC | #6

Is manually adjusting vsync at run-time very inefficient? I am reading up on it and apparently [enhanced sync](https://www.digitaltrends.com/computing/what-is-vsync/) performs better by switching vsync on and off depending if the frame rate is higher or lower than monitor refresh rate.

EDIT: I just want to say, examining how the engine works, it's really incredible. Everything is an object... you could have frames within frames or engines within engines. Crazy

-------------------------

vmost | 2020-08-11 14:46:54 UTC | #7

Vsync is an interesting concept. Would it be worthwhile to implement a lightweight version of enhaned vsync? Like this
```
//concept: turn vsync on/off manually based on frame rate
	//if nominal frame rate > monitor refresh rate + safety factor then
		//vsync = on
		//max frame rate = user-defined (or default) max frame rate
	//else
		//vsync = off
		//max frame rate = monitor refresh rate

	//nominal frame rate: the frame rate if no limit was in place
	//safety factor: 95% or 99% confidence interval around nominal frame rate of last N frames
	//note: store a simple bool that indicates the last vsync controller update's outcome, so we can skip the vsync on/off logic
    //note2: have to add a FpsTracker derived class of Timer for keeping track of the nominal frame rate, since that info is lost by the system timer

	//disable vsync controller if advanced vsync techniques are available (i.e. automatic switching vsync on/off)

	//subscribe vsync controller update to Graphics::EndFrame() event (E_ENDRENDERING) so the frame rate limiter can be removed as soon as possible, and Timer::EndFrame() (E_ENDFRAME) so we know how much time was spent on the frame rate limiter
```
Of course, it would be even more efficient if integrated directly into the engine.

-------------------------

Modanung | 2020-08-11 16:24:30 UTC | #8

I'm not a vsyncologist. Maybe someone else could provide useful feedback.

-------------------------

vmost | 2020-08-16 20:16:08 UTC | #9

If there are any vsyncologists out there.. I am struggling to understand some very odd behavior. I made a simple class to insert a delay into each frame, in order to toggle the FPS up and down, have a switch for vsync on/off, and display the FPS and 'nominal FPS' on-screen. Nominal FPS is the FPS if 'switch window buffer' and 'frame rate limiter' are ignored. This way if vsync is on it's easy to see what the FPS would be if vsync were off.

When a basic program starts up I get some really nice FPS, on the order of 1k FPS for optimized release builds, or around 330 FPS for debug builds. As expected, when vsync turns on the real FPS drops to 60 Hz. Adding some delay reduces the nominal FPS without affecting real FPS.
[Vsync off, no added delay]
![Screen Shot 2020-08-16 at 2.45.58 PM|690x392](upload://kwO5A6G0xKbxmTJZtoFYIH8BndF.png)
[Vsync on, no added delay]
![Screen Shot 2020-08-16 at 2.46.20 PM|690x395](upload://wBUSyKJEaWjah5rY7iWLxCUgJFS.png) 
[Vsync on, 7ms added delay]
![Screen Shot 2020-08-16 at 2.46.52 PM|690x396](upload://8AV8F0px7CDg9lMdNILxXC9S7rg.png)

Now, the strange behavior appears when I drive the nominal FPS below 60Hz while vsync is on... The real FPS doesn't drop to 30Hz, it stays the same! As far as I can tell, vsync is working normally at 50Hz, since with vsync off the FPS stays at 50Hz and screen tearing is evident. What is going on here? My graphics card is an old Intel HD Graphics 4000, and as far as I can tell triple buffering is off. I can't believe my monitor refresh rate is changing... and `GetSubsystem<Graphics>()->GetRefreshRate()` is returning 60Hz constantly (I checked).
[Vsync on, added delay pushes nominal FPS to 50Hz]
![Screen Shot 2020-08-16 at 2.47.47 PM|690x394](upload://iNScoUitC0A7GamLlUVwLqlfAS.jpeg) 

Possible hint... I went to windowed mode and wiggled the window around, which caused 'Present' to spike dramatically and FPS to drop a bunch.

Note: I inserted the delay into 'RenderViews' as part of a failed experiment, its placement has no impact.

P.S. The [Urho3D profiler](https://github.com/urho3d/Urho3D/wiki/DebugHud-and-Profiling) is incredibly easy to use.

-------------------------

