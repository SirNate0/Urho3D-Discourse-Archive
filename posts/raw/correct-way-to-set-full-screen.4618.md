mrchrissross | 2018-10-25 10:34:56 UTC | #1

Hi everyone,

I'd just like to know the correct way to set full screen. Currently I'm using:

    GetSubsystem<Graphics>()->ToggleFullscreen();

This does make the game fullscreen however the problem I'm having is the resolution is low, everything is quite pixelated. I've tried this on two monitors, the first does a fullscreen however the game picture remains the same size with black all around it. The second just comes out pixelated.

Am I supposed to set a resolution?

Thanks in advance,

-------------------------

Modanung | 2018-10-25 10:44:17 UTC | #2

`Graphics::ToggleFullscreen()` _only_ toggles fullscreen. To set a resolution as well you can combine it with `Graphics::SetMode(int width, int height)` or use `Graphics::SetMode(int width, int height, bool fullscreen, bool borderless, bool resizable, bool highDPI, bool vsync, bool tripleBuffer, int multiSample, int monitor, int refreshRate)` instead.

-------------------------

mrchrissross | 2018-10-25 10:44:58 UTC | #3

Is there a quick way to get the current monitor resolution through urho?

-------------------------

Modanung | 2018-10-25 10:51:31 UTC | #4

I think `Graphics::GetDesktopResolution(int monitor)` should get you that.
`Graphics::GetResolutions(int monitor)` will get you a `PODVector<IntVector3>` of available resolution/refresh-rate pairs.

-------------------------

mrchrissross | 2018-10-25 10:52:23 UTC | #5

What is the default resolution set to, when the game is started? (the default resolution that urho sets?) Also what is "highDPI"? sorry for all the questions

-------------------------

Modanung | 2018-10-25 10:53:28 UTC | #6

By default the engine starts in full screen at the current desktop resolution.
[quote="mrchrissross, post:5, topic:4618"]
Also what is “highDPI”?
[/quote]
I'm not sure, might be for Apple retina screens.

-------------------------

mrchrissross | 2018-10-25 10:59:45 UTC | #7

so far this is what I have:
```
if (input->GetKeyDown(KEY_P)) 
{ 
    IntVector2 screenRes = GetSubsystem<Graphics>()->GetSize();
    GetSubsystem<Graphics>()->ToggleFullscreen(); GetSubsystem<Graphics>()->SetMode(screenRes.x_, screenRes.y_);
}
```
However this still comes out quite pixelated :confused:

-------------------------

Modanung | 2018-10-25 10:58:56 UTC | #8

Ah, yes. So setting the resolution to the current size will not change anything. :slight_smile:

-------------------------

mrchrissross | 2018-10-25 11:04:15 UTC | #9

Took a screen cap, http://imgur.com/a/6PLQls1
It doesnt look the best. The space ship is quite pixelated. Do you know how I could solve this?

-------------------------

Modanung | 2018-10-25 11:09:26 UTC | #10

Try replacing `Graphics::GetSize()` with `Graphics::GetDesktopResolution(0)`. To set the _initial_ resolution you can set `engineParamaters_` of your `Application` during `Setup()`.
Also you'll want to use `GetKeyPress` instead of `GetKeyDown` for things that toggle.

-------------------------

mrchrissross | 2018-10-25 11:14:02 UTC | #11

That seems to have worked, how can I set engineParamaters_ in the Setup()? I've only got a Start()

(So that this automatically happens from start)

Also when i press the P key it minimizes the application first and I press clicked it in the taskbar to op in again

-------------------------

Modanung | 2018-10-25 11:28:49 UTC | #12

Here's an example of how to use engine parameters:
https://gitlab.com/luckeyproductions/Octalloc/blob/master/mastercontrol.cpp#L44-L56

I've gotten used to reactivating games after entering full screen. I'm not sure what causes it but I don't think this problem is limited to or caused by Urho3D.

-------------------------

mrchrissross | 2018-10-25 11:51:36 UTC | #13

Alight thanks a lot of this, really appreciate it. Everything seems to be working here :slight_smile:

-------------------------

Modanung | 2018-10-25 11:53:04 UTC | #14

Glad I could help. :)

-------------------------

