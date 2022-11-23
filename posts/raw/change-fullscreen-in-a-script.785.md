JulyForToday | 2017-01-02 01:02:53 UTC | #1

Hi. I'm completely new to using Urho, and definitely like what I see. But ran into a snag (as tends to inevitable happen)

I want to be able to set up a script so that way the user has some way to toggle fullscreen mode, change resolution, etc.

Tried poking around the editor's scripts a bit to see if it had that kind of functionality, but could not find anything. In the documentation for the engine class there doesn't seem to be a way to directly specify these sorts of values. The documentation on engine initialization indicates using the engine's ParseParameter() method. I'm new to AngleScript, and C++ was never my strong point, so I'm not sure how to correctly set up a VariantMap to feed it. Also, the documentation seems to imply these parameters get used when the engine starts, but can they be used to also work after that, while the engine is running?

Using the commandline options mentioned on the UhroPlayer's documentation page works fine for starting the editor (and samples) in windowed mode and resizable. But obviously it's desirable in an actual game to change these settings while it's running. Wouldn't mind the editor being able to do that as well.

-------------------------

weitjong | 2017-01-02 01:02:53 UTC | #2

Welcome to our forum. I believe the "fullscreen toggle" is a built-in feature of the engine already. In fact, it needs to be disabled explicitly if you don't want it. Try pressing Alt+Enter.

-------------------------

friesencr | 2017-01-02 01:02:53 UTC | #3

You get get the graphics subsystem and set fullscreen there.  there are lots of settings on the graphcis subystem.  going off the top of my head.

AS
graphics.fullscreen = true

c++
context->GetSubsystem<Graphics>->SetFullscreen(bool);

-------------------------

JulyForToday | 2017-01-02 01:02:53 UTC | #4

Wow, I feel silly. The [url=http://urho3d.github.io/documentation/1.32/_rendering.html]Rendering Section[/url] has the documentation for the graphics subsystem, and that has everything I could want in there.

I knew I was missing something obvious. I'll go sit in the corner and read [b]ALL[/b] the documentation now. :blush: lol

Alt+Enter definitely works.
graphics.fullscreen only seems to be an accessor. But there is a graphics.ToggleFullscreen() method, and graphics.SetMode() seems to be the most useful for setting the sort of options I'd want accessible to the user.

Thanks for the responses. :slight_smile:

-------------------------

