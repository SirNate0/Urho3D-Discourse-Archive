fredlangva | 2019-07-06 03:31:30 UTC | #1

I had noticed that the Window Width and Height are ignored when set using engineParamters_[ ].  The window is initialized maximized. using SetMode works fine after the Graphics subsystem is initialized.

Am I doing something wrong?

Windows 10, VS2017, Urho3d 1.7.1

-------------------------

Leith | 2019-07-06 04:00:21 UTC | #2

Hey, fredlangva! Welcome to the community!

This is taken from "class MyApp : public Urho3D::Application" ... 

[code]
    virtual void Setup()
    {
        // Called before engine initialization. engineParameters_ member variable can be modified here
        engineParameters_["FullScreen"]=true;
        //engineParameters_["FullScreen"]=false;
        //engineParameters_["WindowWidth"]=1280;
        //engineParameters_["WindowHeight"]=720;
        //engineParameters_["WindowResizable"]=true;
        //engine_->DumpResources();

    }
[/code]

-------------------------

fredlangva | 2019-07-09 17:46:02 UTC | #3

Thanks,

That's correct. It doesn't work on my system. I need to explicitly set the size after initialization. Window title and fullscreen work OK.

-------------------------

