miz | 2017-01-02 01:08:16 UTC | #1

Hi, after compiling on a Raspberry Pi (2) SetMouseVisible() doesn't seem to work. In fact, I think it might even be that it is not picking up mouse input at all? The code I'm using works on my PC and friend's Mac.

Has anyone else seen this? Anyone have any suggestions as to how to get around this?

Thanks :slight_smile:

-------------------------

weitjong | 2017-01-02 01:08:16 UTC | #2

Our Raspberry Pi port depends on video driver provided by SDL library. Currently the Pi video driver does not support operating system mouse cursor like native desktop does. You can only use software-rendered mouse cursor on Pi.

-------------------------

miz | 2017-01-02 01:08:16 UTC | #3

Thanks, is there a standard way of setting up a software rendered cursor?

-------------------------

thebluefish | 2017-01-02 01:08:17 UTC | #4

Software cursor [url=http://urho3d.github.io/documentation/1.5/_u_i.html]is handled by the UI system[/url]. There are examples at the bottom of that page for what you're looking for. While it specifically addresses multiple custom shapes, it's just as fine to use only one cursor shape.

-------------------------

miz | 2017-01-02 01:09:07 UTC | #5

Yep that's done it, thanks :slight_smile:

-------------------------

