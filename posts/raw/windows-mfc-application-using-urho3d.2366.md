asparagusx | 2017-01-02 01:15:00 UTC | #1

Good morning

Looking at alternatives to Irrlicht. Have complex Windows MFC based C++ application. Want to use Urho3D to render scenes. Is this going to work for me???

Any feedback welcome!

Anton

-------------------------

1vanK | 2017-01-02 01:15:00 UTC | #2

Maybe it will help [discourse.urho3d.io/t/urho3d-in-qt-hello-world/143/1](http://discourse.urho3d.io/t/urho3d-in-qt-hello-world/143/1)
[discourse.urho3d.io/t/solved-problem-with-external-window/330/1](http://discourse.urho3d.io/t/solved-problem-with-external-window/330/1)

-------------------------

asparagusx | 2018-03-16 08:00:11 UTC | #3

Hello - I have restarted this project and need to write myself a sample of using Urho3D with a HWND and managing mouse messages etc. Are there any samples available for this. Suspect I will not be able to use the Application class out of the box.

Thanks

-------------------------

Eugene | 2018-03-16 08:33:48 UTC | #4

Just pass HWND into engine parameters while starting. Isn't it enough?

-------------------------

