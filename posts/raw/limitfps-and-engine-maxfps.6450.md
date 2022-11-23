btschumy | 2020-10-21 13:35:40 UTC | #1

I have been trying to get my app to run at a higher FPS than 60.  This is on a iPad Pro that can display 120 FPS (and is achieved in my SceneKit version of the app).

I have set the LimitFPS in the ApplicationOptions to "false" and set the Engine.MaxFps to "120".  Despite that the app runs at 60 FPS.

It is possible that this limit is somehow being imposed by Xamarin or UrhoSharp, but I don't think so.

The comment for LimitFPS is: 
"Determines whether we should limit the frames (defaults to true), the default is limit is 200 FPS for desktop, and 60 fps, despite of the flag settings."

What does the comment "despite the flag settings" mean?

Anyone have any thought on how to get greater than 60 FPS?  I'm sure it is not due to the scene complexity and that is the best it can do.

-------------------------

btschumy | 2020-10-21 14:32:31 UTC | #3

Thanks for the suggestion.  The only place  I can see that Urhosharp exposes VSync is in the Graphics.SetMode() call.  I have tries calling it like this at the end of my setup.

Graphics.SetMode(Graphics.Width, Graphics.Height, Graphics.Fullscreen, Graphics.Borderless, 
			                 Graphics.Resizable, Graphics.HighDPI, false, Graphics.TripleBuffer, 
			                 Graphics.MultiSample, Graphics.Monitor, Graphics.RefreshRate);

The "false" argument is for VSync.

This made no difference.

I doubt the Adaptive Refresh Rate is involved.  That is just how the ProMotion graphics in the iPad works.  I don't think there is a way to toggle it.

-------------------------

vmost | 2020-10-21 14:42:41 UTC | #4

Have you checked if your app can actually reach 120 FPS on that device? One way to test this is to grab the nominal frame rate based on the delta between events `E_ENDFRAME` and `E_ENDRENDERING`. Note that IOS devices always use VSync, so you will only ever get FPS equal to divisors of the monitor refresh rate.

In the past all IOS devices had 60 Hz monitors, so it's possible the Graphics implementation is artificially limiting your FPS to 60. Probably something wrapped in a `#ifdef IOS`.

-------------------------

btschumy | 2020-10-21 15:03:07 UTC | #5

I'm sure it can do better than 60 FPS.  I cap at 60 FPS whether I have 1000's of nodes or 0.  

I searched the code for "IOS" and didn't see anything that would limit the FPS, but I certainly could have missed something.

-------------------------

vmost | 2020-10-21 15:47:35 UTC | #7

However, check line 739 `// If on iOS/tvOS and target framerate is 60 or above, just let the animation callback handle frame timing instead of waiting ourselves`

If the problem is Urho3D I don't think it's in `Engine`

-------------------------

btschumy | 2020-10-21 15:52:07 UTC | #8

That is setting the default value for maxFPS.  As explained in my first posting,  I set it to 120 when configuring things.  I have verified setting this does something.   If I set it to 30 FPS, that is indeed the limit.

-------------------------

btschumy | 2020-10-21 15:53:30 UTC | #9

I'm not sure what that means: "just let the animation callback handle frame timing instead of waiting ourselves".

Is there something I can change to make this work?

-------------------------

vmost | 2020-10-21 15:56:23 UTC | #10

It means ignore the frame rate limiter and just let the graphics system update the frame when it wants to. If vsync is enabled then it will wait until a monitor refresh cycle is complete before flipping the buffers to display a new frame. If vsync is disabled then it will flip the buffers as soon as the execution flow hits that part of the code.

-------------------------

vmost | 2020-10-21 16:00:42 UTC | #11

[This page](https://answers.unity.com/questions/32841/is-it-possible-to-get-above-30-fps-on-an-ios-devic.html) suggests looking in the AppController.mm file generated by xcode. Maybe that has some evidence about what's going on.

-------------------------

vmost | 2020-10-21 16:31:34 UTC | #12

Actually I might be wrong about the animation callback... Apparently the animation callback is an internal loop within the device. Basically on IOS instead of a simple loop for iterating frames, the 'animation callback' is called by the device for each frame. This implies the device could insert a delay before each call to run a frame.

To see how the animation callback is handled you need to dive into the voodoo known as `Urho3D/Source/ThirdParty/SDL/src/video` I'm totally lost in there...

-------------------------
