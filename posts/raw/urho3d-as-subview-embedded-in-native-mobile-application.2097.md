mike_slembrouck | 2017-01-02 01:13:03 UTC | #1

Hi,

I am a software developer of the Belgium Mobile app developer company pegusapps.com. We build enterprise apps. Often we need to add 3D rendering of content (not game related) to our mobile applications and typically the 3D rendering is only a part/feature of a much larger mobile application.  In the past we used Unity and more recently also Ogre3D to do the job.  These engine integrate very well with native UI mobile applications.  

I recently discovered Urho3D and I'm really impressed with the quality of this software project. I would love to try the Urho3D engine on our mobile applications. 
But unfortunately after a short investigation of the engine I came to the conclusion that 'none fullscreen' mode on for example iOS is not supported. To be more precise: after a small debugging session on iOS using the [i]engineParameters_["ExternalWindow"] [/i] param, eventually the [i]SDL_CreateWindowFrom[/i] function internally calls the [i]SDL_Unsupported[/i]() function.

As mentioned other engines like Ogre3D integrate very well. For example on iOS, we have a UIView that embeds the Ogre3D engine. This UIView class can be added to a parent UIView. 

Similar to Urho3D, Ogre3D needs to be initialized with a NameValuePair table. But here you need to add both the main window handle (UIWindow*) and the parent View  control (UIView*). Like this:

[code] 
Ogre::NameValuePairList params;
params["externalWindowHandle"] = ((unsigned long)appUIWindowPtr);
params["externalViewHandle"] = ((unsigned long)parentUIViewPtr); [/code]

It would be fantastic if we could also embed Urho3D as a sub-view inside existing mobile applications.

Cheers,
Mike Slembrouck

-------------------------

cadaver | 2017-01-02 01:13:03 UTC | #2

Urho has the ExternalWindow mechanism, where you call Graphics::SetExternalWindow() with the OS-specific window handle before using Graphics::SetMode() to open the window. This feeds directly into the corresponding SDL external window handle mechanism.

This has been tested at least on Windows (in the past), but in general it's not an often tested feature so I'd actually not expect it to work on mobiles out of the box.

Contributions to verify or improve this mechanism are welcome, however they may be limited to what SDL can offer in that regard. Ogre does its own cross-platform window handling so it may be more robust or flexible for this task.

-------------------------

Egorbo | 2017-01-02 01:13:05 UTC | #3

Windows: It indeed works out of the box for Windows as it requires just a window handle so you can provide a handle of some subview to render.
macOS: it works if you create a child Window, but it doesn't support rendering to a custon NSView (it'd be better to have)
iOS: doesn't work at all for Urho afair.
Android: SDLSurface is tightly bound to SDLActivity 

We added support for standalone controls for all these platforms in UrhoSharp but the implementation is quite messy, I'll try to cleanup everything and create a PR.

-------------------------

csotiriou | 2017-03-08 20:40:11 UTC | #4

What is the state of this feature? Is this implemented?

We have an native app in which we want to add AR features, and this is a must have.

-------------------------

