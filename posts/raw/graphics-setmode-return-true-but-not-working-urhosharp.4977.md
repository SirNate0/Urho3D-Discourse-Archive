NessEngine | 2019-02-28 02:07:26 UTC | #1

Hi all,
I'm using Urho3d for C#. I try to set resolution using SetMode but it just return true and doesn't change anything. here's the call:

`var ret = Graphics.SetMode(800, 600, true, true, false, false, true, false, 0, 0, 0);`

Edit: I call it from first line of 'Start()'

What am I missing?
Thanks!

-------------------------

Leith | 2019-02-28 01:35:47 UTC | #2

Most likely this needs to be done *before* the context is created.
I do it in virtual Setup method, which I presume is executed prior to Start method.
[code]
    virtual void Setup()
    {
        // Called before engine initialization. engineParameters_ member variable can be modified here
        engineParameters_["FullScreen"]=false;
        engineParameters_["WindowWidth"]=1280;
        engineParameters_["WindowHeight"]=720;
        engineParameters_["WindowResizable"]=true;
        //engine_->DumpResources();
    }
[/code]

-------------------------

Modanung | 2019-02-28 02:10:51 UTC | #3

UrhoSharp is a *separate* project with its own forums, documentation and bugs.

-------------------------

Modanung | 2019-02-28 02:12:01 UTC | #4



-------------------------

