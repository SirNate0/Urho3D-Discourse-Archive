mldevs | 2018-07-17 11:38:52 UTC | #1

It is pretty simple. Instead of rendering the entire scene in its own window, could I use Urho3D to render it to an OpenGL window, such as for use in wxWidgets?

-------------------------

alexrass | 2018-07-17 11:38:40 UTC | #2

Engine has parameter:

> ExternalWindow

Example: 
https://github.com/BlueMagnificent/wxUrho3D

-------------------------

elix22 | 2018-07-06 08:30:08 UTC | #3

Yes you can , see 
https://github.com/BlueMagnificent/wxUrho3D

Works on Windows

Don't know about Linux.

Does not work on MacOS , SDL doesn't play well with wxWidgets and QT on MacOS .
I found some possible fix , not sure it actually works
https://github.com/flowercodec/sdl2

-------------------------

mldevs | 2018-07-15 04:14:57 UTC | #4

I'm so sorry for being late to this. I completely forgot about this. But thank you very much!

-------------------------

mldevs | 2018-07-15 04:15:25 UTC | #5

I'm so sorry for being late to this. I completely forgot about this. But thank you very much! I wanted to reply to both hence the same message.

-------------------------

