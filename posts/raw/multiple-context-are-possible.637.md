christianclavet | 2017-01-02 01:01:49 UTC | #1

Hi, I just downloaded Urho3D and evaluating it. I was able to compile the demos and editor. (My first time running CMAKE scripts and it was really painless!  :smiley: ) Really wonderful engine!

I looked all over the documentation, because I would have liked to open multiple windows with Urho3D rendering in GL inside each of them. Might also be useful for rendering on multiple screens (3 screens for racing games for example).

There seem to be a context class in the graphic subsystem that could perhaps do that, as I see that everything that is created in a screen need a context pointer. Is it something that is possible at the moment with Urho3D 1.32?

I have also another question, I was not able to produce the documentation, but I don't have doxigen, must it be installed so the docs are produced? This is not a big issue, as I'm looking on the site.

My primary interest for Urho is for creating game demos, and graphic tools.

-------------------------

OvermindDL1 | 2017-01-02 01:01:49 UTC | #2

I have not tested it, but assuming no singletons anywhere (not that I have seen anyway) it might be possible to create multiple different Context's and Engines to have unique renderers in different windows?  Worth a try.

-------------------------

cadaver | 2017-01-02 01:01:49 UTC | #3

Urho itself attempts to be as singleton-free as possible but some libraries like SDL may not like the approach. Multi-context is not a use case we support or plan for. 

I wouldn't recommend creating eg. 3 separate instances of Urho in the same process and loading the same scene content and resources in each to get multiple windows showing the same content, as that'd be 3 times the memory use. Rather, if you want that, you should see what modifications it takes in the graphics / window handling code to get multiple windows without hacks, and with only a single instance of Urho, by possibly "moving" its graphics context between the windows. Considering that you would need to handle both D3D and OpenGL, and all OS'es (if SDL doesn't do it for you) it can get complex, and it's exactly because of the possible complexity why Urho3D right now doesn't even try to support multiple OS windows. 

But if you manage to do it, and in a clean manner, we will naturally appreciate a pull request :slight_smile:

-------------------------

christianclavet | 2017-01-02 01:01:50 UTC | #4

Thanks! 

Since we have networking in the engine, for doing an editor external windows, I could use the localhost to have 2 instance of urho communicate with each other (I think Lightwave and it's modeler used that method). For doing a multi-monitor game, I'll put that aside, since I'm a hobbyist programmer. This engine cover a lot of things already and it's feature list is really impressive!

-------------------------

cadaver | 2017-01-02 01:01:51 UTC | #5

Another approach that is possible for non-realtime cases (eg. an infrequently updating editor viewport) is to render into a Texture2D, use GetData() to get the RGB pixels, and blit the pixels into a window created in your widget toolkit of choice (Qt / WxWidgets / raw Win32 API etc.) Even creating an extra SDL window for this might work.

-------------------------

