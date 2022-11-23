Hiovita | 2019-04-27 20:12:34 UTC | #1

I would like to hide the default window at initialization. Using Graphics functions or turning the opacity to 0 in SDL accomplishes this, but there is a nasty black screen for a split second before that code is run. I have tried passing a custom-created SDL window handle into the engine as a parameter, but it always says that it's invalid. I have found no examples of how to pre-make the window. Is there some way I don't know about to prevent displaying the window until it has been properly set up, or will I need to override the application class?

-------------------------

Leith | 2019-04-28 05:01:58 UTC | #2

Hi and welcome to the forum! :confetti_ball:

Showing and hiding the application window is a bit outside the scope of Urho3D, but we have access to Urho3D's core and thirdparty api's, so we can do almost anything, although working directly with Urho's dependencies is not recommended in general, we can do it.
Hopefully this gets you where you want to be (SDL can hide new windows on creation but I did not yet look into whether Urho allows us to specify window creation flags to control initial visibility).


First, you need to initialize the engine as usual.

Next, before you do much else at all, obtain access to the Graphics subsystem:
[code]
context_->GetSubsystem<Graphics>()
[/code]

Next, gain access to the underlying SDL Window object:
[code]
SDL_Window* appwindow = context_->GetSubsystem<Graphics>()->GetWindow();
[/code]

Now you can show and hide the app window like this:
[code]
SDL_HideWindow(appwindow);
SDL_ShowWindow(appwindow);
[/code]

The main reason that showing/hiding the window is an issue, is when Urho is running on mobile devices - generally, minimizing an app window on a mobile actually pauses the app, and we need a different way to poll for a "wakeup" event, which is operating system dependent.

-------------------------

Modanung | 2019-04-28 14:22:02 UTC | #3

[quote="Leith, post:2, topic:5124"]
The main reason that showing/hiding the window is an issue, is when Urho is running on mobile devices - generally, minimizing an app window on a mobile actually pauses the app, and we need a different way to poll for a “wakeup” event, which is operating system dependent.
[/quote]

@Leith Are you familiar with `Engine::SetPauseMinimized(bool)`?

@Hiovita Welcome! :confetti_ball: :slightly_smiling_face:

-------------------------

weitjong | 2019-04-28 16:41:54 UTC | #4

[quote="Hiovita, post:1, topic:5124"]
I have found no examples of how to pre-make the window.
[/quote]

Are you referring to “external window”? If so, searching on this as keyword in the forum should give you some results.

-------------------------

