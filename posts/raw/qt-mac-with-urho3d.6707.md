dprandle | 2021-02-13 09:42:44 UTC | #1

So I started building a game-specific editor in urho using Qt - I did this in linux. I actually got pretty far - life was good. I then started using an imac, and poof!

To work on linux you just pass the widget winId to urho as the external window id and it works fine.

It seems the SDL window creation code on Mac is expecting an NSWindow, and winID() from QWidget returns an NSView - so it was crashing. Im fairly new to Cocoa ecosystem, but looked up some obj c quick tutorials and wrote a little mm file to "convert" the NSView to a NSWindow. Okay no more crash.

Problem is that my editing widget is a child window of the main window - so although there was no crash, doing the above thing not only doesn't draw the scene correctly to the widget (doesn't draw anything to the widget), it makes all the input and drag/resize stuff go kind of crazy. I can see that the scene gets loaded and shaders get compiled though..

Anyone done this before that could share? It would be great to get this working on mac as it does on linux

-------------------------

Modanung | 2021-02-13 10:29:43 UTC | #2

What I do is pass the winID of a temporary widget, and dispose of it. Then basically rendering every view to its own texture which is then [converted to a QPixmap](https://gitlab.com/luckeyproductions/tools/manawarg/-/blob/master/src/weaver.h#L114-121). That way you can queue all render surfaces that need to be updated, and leave the rest unchanged.

-------------------------

dprandle | 2021-02-13 18:47:13 UTC | #3

Interesting - does doing this basically get rid of dealing with SDL all together?

In linux I was grabbing things like mouse movement and key strokes from the Qt window events and creating the SDL events manually for them..

If I can just throw away the SDL window and essentially use urho in a headless fashion, using Qt to control app flow and urho to render to a surface that would be great.

I'll give it a shot - I've got a bit of work in to the editor already

-------------------------

Modanung | 2021-02-14 10:26:44 UTC | #4

I use multiple inheritance from `QWidget` and `Object` to allow for the handling of both Qt and engine events by the same object as well as it accessing subsystems. As with for instance this [View3D](https://gitlab.com/luckeyproductions/tools/dolly/-/blob/master/view3d.cpp).

-------------------------

dprandle | 2021-02-15 06:28:58 UTC | #5

Assuming that the view needs to be updated every frame (playing animation or something), have you noticed any performance problems copying the Image to QPixmap?

From your code it does indeed look like your bypassing the sdl stuff and handling input manually from the QEvents passed to the widget.. have you been able to work with Urho UI components doing this (the ui system seems to handle mouse input from sdl events directly)

-------------------------

Modanung | 2021-02-15 08:30:11 UTC | #6

There is a notable FPS reduction for fullscreen purposes, yes. Maybe multi-threading could solve that?

I have not tried engine UI in this setup.

-------------------------

